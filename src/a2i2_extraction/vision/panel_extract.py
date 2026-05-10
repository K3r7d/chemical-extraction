"""Stage 5 orchestrator: triage-kept panels/schemes → labeled compound list.

For each kept image classified as `structure_panel` or `reaction_scheme`,
calls the ChemVLM service with a panel-extraction prompt and parses the
JSON response into structured CompoundExtraction records.

Single-structure images skip Stage 5 — MolNexTR (Stage 3 OCSR) already
produced a SMILES for those, and the VLM call would be wasted budget.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from ..prompts.vlm_panel import build_panel_extraction_prompt, parse_panel_response


# Triage classes routed to Stage 5 (panel-style figures, not single structures).
_VLM_CLASSES: frozenset[str] = frozenset({"structure_panel", "reaction_scheme"})


@dataclass(frozen=True)
class CompoundExtraction:
    img_path: str          # absolute path the VLM saw
    compound_id: str       # label as printed (e.g. "1", "2a", "PR7")
    smiles: str
    source: str = "vlm"    # provenance for downstream merge with OCSR results


class ChemVLMClient(Protocol):
    async def panel_extract(
        self, *, img_path: str, prompt: str
    ) -> str: ...


async def extract_panels(
    triage_results: list[dict],
    *,
    output_dir: Path,
    client: ChemVLMClient,
    page_text: dict[int, str] | None = None,
) -> list[CompoundExtraction]:
    """Run VLM panel extraction over kept structure_panel / reaction_scheme images.

    Args:
        triage_results: dicts from VisionClient.triage() (image_class, keep, …).
        output_dir: the MinerU auto/ dir; img_path is relative to this.
        client: ChemVLM HTTP client.
        page_text: optional {page_idx: text} map for surrounding-paragraph
            context (helps resolve Markush R-group definitions). When omitted,
            only the caption is sent.

    Returns:
        Flat list of CompoundExtraction records across all panels, in panel
        order. May contain duplicates if the same compound appears in multiple
        panels — deduplication is a downstream concern.
    """
    page_text = page_text or {}
    out: list[CompoundExtraction] = []

    for entry in triage_results:
        if not entry.get("keep"):
            continue
        if entry.get("image_class") not in _VLM_CLASSES:
            continue

        img_abs = str(output_dir / entry["img_path"])
        prompt = build_panel_extraction_prompt(
            caption=entry.get("caption") or None,
            context_text=page_text.get(entry.get("page_idx", -1)),
        )

        raw = await client.panel_extract(img_path=img_abs, prompt=prompt)
        for item in parse_panel_response(raw):
            out.append(
                CompoundExtraction(
                    img_path=img_abs,
                    compound_id=item["compound_id"],
                    smiles=item["smiles"],
                )
            )
    return out
