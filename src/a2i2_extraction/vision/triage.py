"""SigLIP 2 zero-shot image triage for MinerU-extracted figures.

Classifies each figure into one of 7 categories and marks the three
chemistry-relevant ones (reaction_scheme, single_structure, structure_panel)
as keep=True for downstream MolNexTR OCSR processing.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

import torch
from PIL import Image


class ImageClass(str, Enum):
    REACTION_SCHEME = "reaction_scheme"
    SINGLE_STRUCTURE = "single_structure"
    STRUCTURE_PANEL = "structure_panel"
    SPECTRUM = "spectrum"
    BIOLOGY = "biology"
    TABLE_IMAGE = "table_image"
    OTHER = "other"


KEEP_CLASSES: frozenset[ImageClass] = frozenset({
    ImageClass.REACTION_SCHEME,
    ImageClass.SINGLE_STRUCTURE,
    ImageClass.STRUCTURE_PANEL,
})

# Text prompts used for zero-shot classification with SigLIP 2.
# Order matches _ORDERED_CLASSES — do not reorder independently.
_CLASS_PROMPTS: list[str] = [
    # reaction_scheme
    "a two-dimensional chemical reaction scheme drawn as flat black-on-white "
    "skeletal line-bond formulas connected by horizontal arrows, with reagents, "
    "solvents, temperatures, and percent yields written above or below each arrow",
    # single_structure
    "one isolated two-dimensional skeletal chemical structure of a small molecule, "
    "drawn as flat black line bonds on a white background with explicit heteroatom "
    "labels (N, O, S, F, Cl) and wedge or dash stereo bonds, no other structures present",
    # structure_panel
    "a panel of several two-dimensional skeletal chemical structures of small "
    "organic drug-like molecules drawn as flat black line bonds on a white "
    "background, each labeled with a bold compound number such as 1, 2a, 3b, "
    "and arranged in a grid; not a 3D protein render, not a binding pocket",
    # spectrum
    "a scientific spectrum or chromatogram plot with an x-y axis showing peaks "
    "and signals, such as a 1H or 13C NMR spectrum, an infrared IR spectrum, a "
    "UV-Vis absorption curve, a mass spectrometry MS trace, or an HPLC chromatogram",
    # biology
    "a biology figure: a western blot or SDS-PAGE gel with dark protein bands; "
    "a fluorescence or confocal microscopy photograph of cells or tissue; a flow "
    "cytometry dot plot; a histology stain; OR a three-dimensional rendered "
    "protein structure showing a grey or white cartoon ribbon backbone with "
    "cyan, magenta, or coloured amino acid side chains drawn as sticks, often "
    "labeled with residue codes like S55, N51, R70, Y341, depicting a binding "
    "pocket, ligand pose, or docking model from PyMOL or ChimeraX",
    # table_image
    "a data table captured as an image showing rows and columns of numerical "
    "values, IC50 data, selectivity data, or activity results",
    # other
    "a bar chart, line graph, dose-response sigmoid curve, scatter plot, "
    "pie chart, photograph, journal logo, or general scientific figure",
]

_ORDERED_CLASSES: list[ImageClass] = [
    ImageClass.REACTION_SCHEME,
    ImageClass.SINGLE_STRUCTURE,
    ImageClass.STRUCTURE_PANEL,
    ImageClass.SPECTRUM,
    ImageClass.BIOLOGY,
    ImageClass.TABLE_IMAGE,
    ImageClass.OTHER,
]

assert len(_CLASS_PROMPTS) == len(_ORDERED_CLASSES), "prompt/class count mismatch"


@dataclass
class TriageResult:
    img_path: str          # relative to output_dir, e.g. "images/HASH.jpg"
    page_idx: int
    bbox: list[float]
    image_class: ImageClass
    confidence: float      # sigmoid score of the winning class (0-1)
    keep: bool             # True iff image_class in KEEP_CLASSES and confidence >= threshold
    caption: str           # from MinerU content_list; often empty


class ImageTriage:
    """Zero-shot image classifier using SigLIP 2.

    Model and text features are loaded lazily on the first call to
    triage_document(), then cached for the lifetime of this instance.
    Call from a long-running worker to amortize the load cost.
    """

    DEFAULT_MODEL = "google/siglip2-so400m-patch14-384"

    def __init__(
        self,
        *,
        model_name: str = DEFAULT_MODEL,
        device: str | None = None,
        confidence_threshold: float = 0.0,
        batch_size: int = 16,
    ) -> None:
        self._model_name = model_name
        self._device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self._confidence_threshold = confidence_threshold
        self._batch_size = batch_size
        self._model = None
        self._processor = None
        self._text_features: torch.Tensor | None = None

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def triage_document(self, output_dir: Path) -> list[TriageResult]:
        """Classify all images listed in a MinerU auto/ output directory.

        Args:
            output_dir: the ``auto/`` directory produced by MinerU
                        (contains *_content_list.json and images/).

        Returns:
            One TriageResult per image entry in the content list,
            in content-list order (≈ document order).
        """
        entries = _load_image_entries(output_dir)
        if not entries:
            return []

        self._load()

        results: list[TriageResult] = []
        for i in range(0, len(entries), self._batch_size):
            batch = entries[i : i + self._batch_size]
            results.extend(self._classify_batch(batch, output_dir))
        return results

    def kept(self, results: list[TriageResult]) -> list[TriageResult]:
        """Return only the chemistry-relevant entries (keep=True)."""
        return [r for r in results if r.keep]

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _load(self) -> None:
        if self._model is not None:
            return
        import torch
        from transformers import AutoModel, AutoProcessor

        self._processor = AutoProcessor.from_pretrained(self._model_name)
        # fp16 halves VRAM (~0.8 GB vs ~1.6 GB for SO400M) so vision and
        # chemvlm can share a single 8 GB GPU.
        self._model = (
            AutoModel.from_pretrained(self._model_name, torch_dtype=torch.float16)
            .to(self._device)
            .eval()
        )
        self._text_features = self._encode_texts()

    def _encode_texts(self) -> torch.Tensor:
        """Pre-encode all class prompts once. Returns (7, D) normalized tensor."""
        inputs = self._processor(
            text=_CLASS_PROMPTS,
            padding="max_length",
            truncation=True,
            return_tensors="pt",
        ).to(self._device)
        with torch.no_grad():
            # SigLIP 2 tokenizer returns only input_ids (no attention_mask).
            out = self._model.get_text_features(input_ids=inputs.input_ids)
            features = out if isinstance(out, torch.Tensor) else out.pooler_output
        return torch.nn.functional.normalize(features, dim=-1)  # (7, D)

    def _classify_batch(
        self,
        entries: list[dict],
        output_dir: Path,
    ) -> list[TriageResult]:
        images: list[Image.Image] = []
        for entry in entries:
            images.append(
                Image.open(output_dir / entry["img_path"]).convert("RGB")
            )

        inputs = self._processor(images=images, return_tensors="pt").to(self._device)
        with torch.no_grad():
            out = self._model.get_image_features(pixel_values=inputs.pixel_values)
            image_features = out if isinstance(out, torch.Tensor) else out.pooler_output
        image_features = torch.nn.functional.normalize(image_features, dim=-1)  # (B, D)

        scale = self._model.logit_scale.exp()
        bias = self._model.logit_bias
        logits = image_features @ self._text_features.T * scale + bias  # (B, 7)
        probs = torch.sigmoid(logits).cpu()  # (B, 7)

        results: list[TriageResult] = []
        for entry, prob_row in zip(entries, probs, strict=True):
            best_idx = int(prob_row.argmax())
            best_class = _ORDERED_CLASSES[best_idx]
            confidence = float(prob_row[best_idx].detach())
            keep = best_class in KEEP_CLASSES and confidence >= self._confidence_threshold
            results.append(
                TriageResult(
                    img_path=entry["img_path"],
                    page_idx=entry.get("page_idx", -1),
                    bbox=entry.get("bbox", []),
                    image_class=best_class,
                    confidence=confidence,
                    keep=keep,
                    caption=" ".join(entry.get("image_caption", [])),
                )
            )
        return results


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------

def _load_image_entries(output_dir: Path) -> list[dict]:
    """Parse content_list.json and return only image-type entries."""
    content_list = _find_content_list(output_dir)
    data: list[dict] = json.loads(content_list.read_text(encoding="utf-8"))
    return [item for item in data if item.get("type") == "image"]


def _find_content_list(output_dir: Path) -> Path:
    """Return the non-v2 content_list JSON path inside output_dir."""
    candidates = sorted(
        p for p in output_dir.iterdir()
        if p.name.endswith("_content_list.json") and "_v2" not in p.name
    )
    if not candidates:
        raise FileNotFoundError(
            f"No *_content_list.json found in {output_dir}"
        )
    return candidates[0]
