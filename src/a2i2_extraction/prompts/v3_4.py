from __future__ import annotations

import json
from pathlib import Path

_PROMPT = (Path(__file__).parent / "v3_4_1.txt").read_text(encoding="utf-8")


def build_extraction_prompt(
    paper_text: str,
    *,
    si_text: str | None = None,
    reference_table: str | None = None,
    intermediate: dict | None = None,
) -> str:
    parts = [_PROMPT, "", "=== PAPER (MAIN TEXT) ===", paper_text]
    if si_text:
        parts += ["", "=== SUPPORTING INFORMATION ===", si_text]
    if reference_table:
        parts += ["", "=== COMPOUND REFERENCE TABLE ===", reference_table]
    if intermediate:
        # Inject vision-derived compound structures so the LLM can cross-reference
        # image-extracted SMILES against the synthesis text. Strip the full markdown
        # (already in the prompt above) to keep this section compact.
        compact = {
            k: v for k, v in intermediate.items() if k != "markdown_text"
        }
        parts += [
            "",
            "=== VISION-EXTRACTED STRUCTURES ===",
            json.dumps(compact, indent=2, ensure_ascii=False),
        ]
    return "\n".join(parts)
