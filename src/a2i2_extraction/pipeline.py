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

_IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp"}


@dataclass
class ExtractionResult:
    paper_dir: Path
    extraction: dict
    issues: list[Issue] = field(default_factory=list)
    retries: int = 0
    raw_responses: list[str] = field(default_factory=list)

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
        send_images: bool = True,
    ) -> None:
        self._mineru = mineru
        self._llm = llm
        self._model_name = model_name
        self._output_dir = output_dir
        self._max_retries = max_retries
        self._send_images = send_images

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

        images = _collect_images(main_doc, si_doc) if self._send_images else []
        log.info("pipeline.images", count=len(images), enabled=self._send_images)

        prompt = build_extraction_prompt(
            paper_text=main_text,
            si_text=si_text,
        )
        log.info("pipeline.llm_call", prompt_chars=len(prompt), images=len(images))

        extraction, issues, retries, raw_responses = await self._extract_with_retry(
            prompt, images=images
        )

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
            paper_dir=paper_dir,
            extraction=extraction,
            issues=issues,
            retries=retries,
            raw_responses=raw_responses,
        )
        self._write_output(result)
        return result

    async def _extract_with_retry(
        self, prompt: str, *, images: list[Path] | None = None
    ) -> tuple[dict, list[Issue], int, list[str]]:
        raw = ""
        extraction: dict = {}
        issues: list[Issue] = []
        raws: list[str] = []

        for attempt in range(self._max_retries + 1):
            current_prompt = prompt if attempt == 0 else _retry_prompt(prompt, raw, issues)
            try:
                # Images only on first attempt — retry prompts are text-only to
                # avoid re-sending large payloads when fixing validation issues.
                attempt_images = images if attempt == 0 else None
                raw = await self._llm.complete(current_prompt, images=attempt_images)
                raws.append(raw)
                extraction = _parse_llm_json(raw)
            except Exception as exc:
                # If complete() itself raised, we never appended — record the failure.
                if len(raws) <= attempt:
                    raws.append(f"<<llm call failed: {exc}>>")
                issues = [Issue(
                    code="JSON_PARSE",
                    severity=Severity.ERROR,
                    message=str(exc),
                    path="$",
                )]
                log.warning(
                    "pipeline.llm_json_error",
                    attempt=attempt,
                    error=str(exc),
                    raw_chars=len(raw),
                )
                if attempt < self._max_retries:
                    continue
                return extraction, issues, attempt, raws

            issues = validate_extraction(extraction)
            errors = [i for i in issues if i.severity is Severity.ERROR]
            if not errors:
                return extraction, issues, attempt, raws
            if attempt < self._max_retries:
                log.info("pipeline.retry", attempt=attempt + 1, violations=len(errors))

        return extraction, issues, self._max_retries, raws

    def _save_cleaned(self, doc: ParsedDocument, cleaned_text: str) -> None:
        if doc.output_dir is None:
            return
        # mineru output_dir is <data_root>/<N>/mineru/<stem>/auto
        parts = doc.output_dir.parts
        if len(parts) < 4 or parts[-3] != "mineru" or parts[-1] != "auto":
            return
        n, stem = parts[-4], parts[-2]
        cleaned_dir = self._output_dir / "cleaned" / n / stem / "auto"
        cleaned_dir.mkdir(parents=True, exist_ok=True)
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
                    "raw_response_chars": [len(r) for r in result.raw_responses],
                },
                indent=2,
            )
        )
        if result.raw_responses:
            raw_dir = out / "raw_llm"
            raw_dir.mkdir(exist_ok=True)
            for i, raw in enumerate(result.raw_responses):
                (raw_dir / f"attempt_{i}.txt").write_text(raw, encoding="utf-8")


def _collect_images(*docs: ParsedDocument | None) -> list[Path]:
    """Collect all figure images from MinerU output directories."""
    images: list[Path] = []
    for doc in docs:
        if doc is None or doc.output_dir is None:
            continue
        img_dir = doc.output_dir / "images"
        if img_dir.is_dir():
            images.extend(sorted(
                p for p in img_dir.iterdir()
                if p.suffix.lower() in _IMAGE_SUFFIXES
            ))
    return images


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
