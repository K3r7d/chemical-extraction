"""Stage 5 prompt: structure panel / reaction scheme → labeled SMILES list.

TinyChemVL is trained on single-molecule SMILES extraction and reaction
prediction. It hasn't been explicitly evaluated on multi-compound panels with
text labels (Markush R-groups, compound numbers like "1a", "2b"). We hold its
hand with a strict output schema and tell it explicitly to find every label
visible in the image.
"""

from __future__ import annotations

import json
import re


_PANEL_INSTRUCTION = """\
You are reading a chemistry figure containing one or more chemical structures.
For every numbered or labeled compound visible in the image, output one row.
If the figure defines Markush R-groups (e.g. "R1 = H", "R2 = OMe"), output one
row per fully-substituted compound, using the resolved SMILES.

Output format: a JSON array, no prose, no markdown fences.
Each element: {"compound_id": "<label as printed, e.g. '1', '2a', 'PR7'>", \
"smiles": "<canonical SMILES of the fully-resolved compound>"}.

If a label has no parseable structure (text-only, ambiguous), skip it.
Return [] if no chemical structures are visible.
"""


def build_panel_extraction_prompt(
    *,
    caption: str | None = None,
    context_text: str | None = None,
) -> str:
    """Build the user prompt for a single panel image.

    Args:
        caption: Figure caption text, if available from MinerU.
        context_text: Markush definition text or surrounding paragraph from
            the same page — gives the model textual support for resolving
            R-group placeholders.

    Returns:
        A plain-text user prompt to send alongside the image.
    """
    parts = [_PANEL_INSTRUCTION.strip()]
    if caption:
        parts.append(f"Figure caption: {caption.strip()}")
    if context_text:
        parts.append(f"Relevant text near the figure:\n{context_text.strip()}")
    return "\n\n".join(parts)


_FENCE_RE = re.compile(r"^```(?:json)?\s*|\s*```$", re.MULTILINE)


def parse_panel_response(raw: str) -> list[dict]:
    """Tolerant parser for the model's JSON output.

    Strips optional markdown fences, finds the first JSON array in the text,
    and returns a list of {compound_id, smiles} dicts. Silently drops malformed
    entries.
    """
    text = _FENCE_RE.sub("", raw).strip()

    # Find the first '[' ... ']' span.
    start = text.find("[")
    end = text.rfind("]")
    if start == -1 or end == -1 or end <= start:
        return []

    try:
        payload = json.loads(text[start : end + 1])
    except json.JSONDecodeError:
        return []

    if not isinstance(payload, list):
        return []

    out: list[dict] = []
    for item in payload:
        if not isinstance(item, dict):
            continue
        cid = item.get("compound_id")
        smi = item.get("smiles")
        if isinstance(cid, str) and isinstance(smi, str) and cid and smi:
            out.append({"compound_id": cid.strip(), "smiles": smi.strip()})
    return out
