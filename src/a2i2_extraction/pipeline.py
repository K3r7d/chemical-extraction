"""Pipeline: parse → vision → extract → validate."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import TYPE_CHECKING

import structlog

import httpx

from .clients.base import LLMClient, MinerUClient, ParsedDocument
from .preprocessing import clean_text, trim_references
from .prompts import build_extraction_prompt
from .validators import Issue, Severity, validate_extraction
from .vision.intermediate import build_intermediate
from .vision.panel_extract import extract_panels

if TYPE_CHECKING:
    from .clients.chemvlm import ChemVLMHTTPClient
    from .clients.vision import VisionClient

log = structlog.get_logger(__name__)

_MAX_RETRIES = 2


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
        vision: VisionClient | None = None,
        chemvlm: ChemVLMHTTPClient | None = None,
    ) -> None:
        self._mineru = mineru
        self._llm = llm
        self._model_name = model_name
        self._output_dir = output_dir
        self._vision = vision
        self._chemvlm = chemvlm

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

        intermediate = await self._run_vision(main_doc, main_text)

        prompt = build_extraction_prompt(
            paper_text=main_text,
            si_text=si_text,
            intermediate=intermediate.to_dict() if intermediate else None,
        )
        log.info("pipeline.llm_call", prompt_chars=len(prompt))

        extraction, issues, retries = await self._extract_with_retry(prompt)

        # Stamp the runtime metadata if the model didn't.
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
        """Call the LLM and validate, retrying up to _MAX_RETRIES times on errors.

        Returns (extraction, issues, retry_count).
        retry_count is 0 when the first attempt passes validation.
        """
        raw = ""
        extraction: dict = {}
        issues: list[Issue] = []

        for attempt in range(_MAX_RETRIES + 1):
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
                if attempt < _MAX_RETRIES:
                    continue
                return extraction, issues, attempt

            issues = validate_extraction(extraction)
            errors = [i for i in issues if i.severity is Severity.ERROR]
            if not errors:
                return extraction, issues, attempt
            if attempt < _MAX_RETRIES:
                log.info("pipeline.retry", attempt=attempt + 1, violations=len(errors))

        return extraction, issues, _MAX_RETRIES

    async def _run_vision(self, doc: ParsedDocument, markdown_text: str):
        """Stages 2–4: triage → OCSR → ChemVLM → intermediate.

        Returns None when vision clients are not configured or output_dir is
        unavailable (e.g. MinerUHTTPClient before the output_dir fix is deployed).
        """
        if self._vision is None or doc.output_dir is None:
            log.info("pipeline.vision_skipped",
                     reason="no vision client" if self._vision is None else "output_dir not set")
            return None

        log.info("pipeline.triage", output_dir=str(doc.output_dir))
        try:
            triage_results = await self._vision.triage(doc.output_dir)
        except (httpx.RequestError, httpx.HTTPStatusError) as exc:
            log.warning("pipeline.vision_unavailable", error=str(exc))
            return None

        kept = [r for r in triage_results if r["keep"]]
        log.info("pipeline.triage_done", total=len(triage_results), kept=len(kept))

        single_paths = [
            doc.output_dir / r["img_path"]
            for r in kept if r["image_class"] == "single_structure"
        ]
        ocsr_results: list[dict] = []
        if single_paths:
            log.info("pipeline.ocsr", n=len(single_paths))
            try:
                ocsr_results = await self._vision.ocsr(single_paths)
                valid = sum(1 for r in ocsr_results if r.get("valid"))
                log.info("pipeline.ocsr_done", valid=valid, total=len(ocsr_results))
            except (httpx.RequestError, httpx.HTTPStatusError) as exc:
                log.warning("pipeline.ocsr_unavailable", error=str(exc))

        panel_compounds = []
        if self._chemvlm is not None:
            panels = [r for r in kept
                      if r["image_class"] in {"structure_panel", "reaction_scheme"}]
            if panels:
                log.info("pipeline.chemvlm", n=len(panels))
                try:
                    panel_compounds = await extract_panels(
                        triage_results,
                        output_dir=doc.output_dir,
                        client=self._chemvlm,
                    )
                    log.info("pipeline.chemvlm_done", compounds=len(panel_compounds))
                except (httpx.RequestError, httpx.HTTPStatusError) as exc:
                    log.warning("pipeline.chemvlm_unavailable", error=str(exc))

        return build_intermediate(
            markdown_text=markdown_text,
            triage_results=triage_results,
            ocsr_results=ocsr_results,
            panel_compounds=panel_compounds,
        )

    def _save_cleaned(self, doc: ParsedDocument, cleaned_text: str) -> None:
        """Write cleaned markdown to outputs/cleaned/ mirroring the MinerU layout.

        Only runs when doc.output_dir is set (MinerULocalClient always sets it;
        MinerUHTTPClient currently does not — that is a known gap).
        """
        if doc.output_dir is None:
            return
        mineru_root = self._output_dir / "mineru"
        try:
            rel = doc.output_dir.relative_to(mineru_root)
        except ValueError:
            return  # output_dir not inside our mineru/ tree
        cleaned_dir = self._output_dir / "cleaned" / rel
        cleaned_dir.mkdir(parents=True, exist_ok=True)
        stem = doc.output_dir.parent.name   # the paper slug, one level above auto/
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
    """Pick (main_pdf, si_pdf) from a paper directory.

    Convention: SI files contain '_si_' or 'supporting' (case-insensitive).
    Anything else is treated as the main paper.
    """
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
    """Build a follow-up prompt that shows the model its violations and asks it to fix them."""
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
    """Strip optional markdown fences then parse JSON.

    The prompt forbids text-before-or-after, but models occasionally wrap in
    ```json fences. We tolerate that and nothing else.
    """
    text = raw.strip()
    if text.startswith("```"):
        # drop the opening fence (with or without language tag) and the closing one
        text = text.split("\n", 1)[1] if "\n" in text else text
        if text.endswith("```"):
            text = text[: -3].rstrip()
    return json.loads(text)
