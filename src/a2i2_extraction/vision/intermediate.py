"""Stage 4: build the structured intermediate from all vision outputs.

Takes triage + OCSR + ChemVLM panel results and produces the JSON blob
that is injected into the LLM synthesis-extraction prompt.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class StructuredIntermediate:
    markdown_text: str
    validated_structures: list[dict] = field(default_factory=list)
    panel_compounds: list[dict] = field(default_factory=list)
    scheme_images: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "markdown_text": self.markdown_text,
            "validated_structures": self.validated_structures,
            "panel_compounds": self.panel_compounds,
            "scheme_images": self.scheme_images,
        }


def build_intermediate(
    *,
    markdown_text: str,
    triage_results: list[dict],
    ocsr_results: list[dict],
    panel_compounds: list,
) -> StructuredIntermediate:
    """Assemble the structured intermediate from vision stage outputs.

    Args:
        markdown_text:   cleaned + trimmed markdown for the paper.
        triage_results:  dicts from VisionClient.triage().
        ocsr_results:    dicts from VisionClient.ocsr() (single_structure only).
        panel_compounds: CompoundExtraction list from panel_extract.extract_panels().

    Returns:
        StructuredIntermediate ready to be serialised into the LLM prompt.
    """
    validated_structures = [
        {
            "img_path": r["img_path"],
            "smiles": r.get("canonical_smiles") or r.get("smiles"),
            "formula": r.get("formula"),
            "inchikey": r.get("inchikey"),
            "source": "ocsr",
        }
        for r in ocsr_results
        if r.get("valid")
    ]

    panel_compounds_dicts = [
        {
            "img_path": c.img_path,
            "compound_id": c.compound_id,
            "smiles": c.smiles,
            "source": c.source,
        }
        for c in panel_compounds
    ]

    # Reaction scheme images are listed by path so the LLM knows they exist
    # even though it doesn't receive them as image tokens (text-only Stage 5).
    scheme_images = [
        r["img_path"]
        for r in triage_results
        if r.get("keep") and r.get("image_class") == "reaction_scheme"
    ]

    return StructuredIntermediate(
        markdown_text=markdown_text,
        validated_structures=validated_structures,
        panel_compounds=panel_compounds_dicts,
        scheme_images=scheme_images,
    )
