"""Pipeline: parse → extract → validate."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import structlog

from .clients.base import LLMClient, MinerUClient, ParsedDocument
from .preprocessing import clean_text, trim_references
from .prompts import build_extraction_prompt
from .validators import Issue, Severity, validate_extraction

log = structlog.get_logger(__name__)


@dataclass
class ExtractionResult:
    paper_dir: Path
    extraction: dict
    issues: list[Issue] = field(default_factory=list)
    retries: int = 0

    @property
    def has_errors(self) -> bool:
        return any(i.severity is Severity.ERROR for i in self.issues)


class Pipeline:
    def __init__(
        self,
        *,
        mineru: MinerUClient,
        llm: LLMClient,
        model_name: str,
        output_dir: Path,
        max_retries: int = 2,
    ) -> None:
        self._mineru = mineru
        self._llm = llm
        self._model_name = model_name
        self._output_dir = output_dir
        self._max_retries = max_retries

    async def run(self, paper_dir: Path) -> ExtractionResult:
        log.info("pipeline.start", paper_dir=str(paper_dir))
        main_pdf, si_pdf = _resolve_paper_files(paper_dir)

        log.info("pipeline.parse", main=main_pdf.name, si=si_pdf and si_pdf.name)
        main_doc = await self._mineru.parse(main_pdf)
        si_doc: ParsedDocument | None = (
            await self._mineru.parse(si_pdf) if si_pdf else None
        )

        main_text = trim_references(clean_text(main_doc.text))
        si_text = trim_references(clean_text(si_doc.text)) if si_doc else None
        self._save_cleaned(main_doc, main_text)
        if si_doc and si_text:
            self._save_cleaned(si_doc, si_text)

        prompt = build_extraction_prompt(
            paper_text=main_text,
            si_text=si_text,
        )
        log.info("pipeline.llm_call", prompt_chars=len(prompt))

        extraction, issues, retries = await self._extract_with_retry(prompt)

        extraction.setdefault("extraction", {})
        extraction["extraction"].setdefault("prompt_version", "v3.4")
        extraction["extraction"].setdefault("model_name", self._model_name)
        extraction["extraction"].setdefault(
            "extraction_date", date.today().isoformat()
        )
        if any(i.severity is Severity.ERROR for i in issues):
            extraction["extraction"]["extraction_status"] = "failed_validation"

        log.info(
            "pipeline.validated",
            errors=sum(1 for i in issues if i.severity is Severity.ERROR),
            warnings=sum(1 for i in issues if i.severity is Severity.WARNING),
            retries=retries,
        )

        result = ExtractionResult(
            paper_dir=paper_dir, extraction=extraction, issues=issues, retries=retries,
        )
        self._write_output(result)
        return result

    async def _extract_with_retry(
        self, prompt: str
    ) -> tuple[dict, list[Issue], int]:
        raw = ""
        extraction: dict = {}
        issues: list[Issue] = []

        for attempt in range(self._max_retries + 1):
            current_prompt = prompt if attempt == 0 else _retry_prompt(prompt, raw, issues)
            try:
                raw = await self._llm.complete(current_prompt)
                extraction = _parse_llm_json(raw)
            except Exception as exc:
                issues = [Issue(
                    code="JSON_PARSE",
                    severity=Severity.ERROR,
                    message=str(exc),
                    path="$",
                )]
                log.warning("pipeline.llm_json_error", attempt=attempt, error=str(exc))
                if attempt < self._max_retries:
                    continue
                return extraction, issues, attempt

            issues = validate_extraction(extraction)
            errors = [i for i in issues if i.severity is Severity.ERROR]
            if not errors:
                return extraction, issues, attempt
            if attempt < self._max_retries:
                log.info("pipeline.retry", attempt=attempt + 1, violations=len(errors))

        return extraction, issues, self._max_retries

    def _save_cleaned(self, doc: ParsedDocument, cleaned_text: str) -> None:
        if doc.output_dir is None:
            return
        mineru_root = self._output_dir / "mineru"
        try:
            rel = doc.output_dir.relative_to(mineru_root)
        except ValueError:
            return
        cleaned_dir = self._output_dir / "cleaned" / rel
        cleaned_dir.mkdir(parents=True, exist_ok=True)
        stem = doc.output_dir.parent.name
        out = cleaned_dir / f"{stem}.md"
        out.write_text(cleaned_text, encoding="utf-8")
        log.info("pipeline.cleaned_saved", path=str(out), chars=len(cleaned_text))

    def _write_output(self, result: ExtractionResult) -> None:
        out = self._output_dir / result.paper_dir.name
        out.mkdir(parents=True, exist_ok=True)
        (out / "extraction.json").write_text(
            json.dumps(result.extraction, indent=2, ensure_ascii=False)
        )
        (out / "audit.json").write_text(
            json.dumps(
                {
                    "retries": result.retries,
                    "extraction_status": (
                        "failed_validation" if result.has_errors else "ok"
                    ),
                    "issues": [
                        {
                            "code": i.code,
                            "severity": i.severity.value,
                            "message": i.message,
                            "path": i.path,
                        }
                        for i in result.issues
                    ],
                },
                indent=2,
            )
        )


def _resolve_paper_files(paper_dir: Path) -> tuple[Path, Path | None]:
    pdfs = sorted(p for p in paper_dir.iterdir() if p.suffix.lower() == ".pdf")
    if not pdfs:
        raise FileNotFoundError(f"no PDFs in {paper_dir}")
    si_keys = ("_si_", "supporting")
    si = next(
        (p for p in pdfs if any(k in p.name.lower() for k in si_keys)), None
    )
    main = next((p for p in pdfs if p is not si), None)
    if main is None:
        raise FileNotFoundError(f"no main PDF in {paper_dir} (only SI found)")
    return main, si


def _retry_prompt(original: str, previous_raw: str, issues: list[Issue]) -> str:
    violations = "\n".join(
        f"- [{i.code}] {i.path or '$'}: {i.message}"
        for i in issues
        if i.severity is Severity.ERROR
    )
    return "\n\n".join([
        original,
        "=== YOUR PREVIOUS OUTPUT ===",
        previous_raw,
        "=== VALIDATION VIOLATIONS ===",
        violations,
        "Re-output the complete JSON object fixing only these violations. No commentary before or after the JSON.",
    ])


def _parse_llm_json(raw: str) -> dict:
    text = raw.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1] if "\n" in text else text
        if text.endswith("```"):
            text = text[: -3].rstrip()
    return json.loads(text)
