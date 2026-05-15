from __future__ import annotations

from pathlib import Path

_PROMPT = (Path(__file__).parent / "v3_4_1.txt").read_text(encoding="utf-8")


def build_extraction_prompt(
    paper_text: str,
    *,
    si_text: str | None = None,
    reference_table: str | None = None,
) -> str:
    parts = [_PROMPT, "", "=== PAPER (MAIN TEXT) ===", paper_text]
    if si_text:
        parts += ["", "=== SUPPORTING INFORMATION ===", si_text]
    if reference_table:
        parts += ["", "=== COMPOUND REFERENCE TABLE ===", reference_table]
    return "\n".join(parts)
