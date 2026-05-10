"""MolNexTR OCSR: structure images → SMILES + RDKit-derived formula + InChIKey.

MolNexTR is designed for single-molecule images. structure_panel and
reaction_scheme images will mostly produce invalid SMILES — the valid flag
handles that. Panel segmentation is a Phase 3 addition.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import torch

from .triage import TriageResult


@dataclass
class OCSRResult:
    img_path: str          # same relative path as TriageResult.img_path
    smiles: str | None     # raw MolNexTR output; None on failure
    canonical_smiles: str | None   # RDKit-canonicalized
    formula: str | None    # RDKit molecular formula (e.g. "C8H9NO2")
    inchikey: str | None   # RDKit InChIKey
    valid: bool            # True iff smiles parsed successfully by RDKit


class MolNexTROCSR:
    """Wraps MolNexTR + RDKit for batch OCSR on kept triage images.

    Lazy-loads the MolNexTR checkpoint on first call. Designed to run in the
    vision Docker service where GPU + MolNexTR are available.

    The checkpoint is a local .pth file (downloaded from Zenodo at container
    start), not a HuggingFace model ID.
    """

    DEFAULT_CHECKPOINT = "/cache/molnextr/molnextr_best.pth"

    def __init__(
        self,
        *,
        checkpoint: str = DEFAULT_CHECKPOINT,
        device: str | None = None,
    ) -> None:
        self._checkpoint = checkpoint
        self._device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self._model = None

    def _load(self) -> None:
        if self._model is not None:
            return
        from MolNexTR.model import molnextr
        self._model = molnextr(self._checkpoint, device=torch.device(self._device))

    def process(
        self,
        triage_results: list[TriageResult],
        output_dir: Path,
    ) -> list[OCSRResult]:
        """Run OCSR on all kept images in triage_results.

        Args:
            triage_results: output of ImageTriage.triage_document().
            output_dir:     the MinerU auto/ dir (images are relative to it).

        Returns:
            One OCSRResult per kept image, in triage order.
            Discarded images are silently skipped.
        """
        kept = [r for r in triage_results if r.keep]
        if not kept:
            return []

        self._load()

        results: list[OCSRResult] = []
        for triage_r in kept:
            img_path = str(output_dir / triage_r.img_path)
            raw = self._model.predict_final_results(img_path)
            smiles = raw.get("predicted_smiles") or None
            results.append(OCSRResult(img_path=triage_r.img_path, **_rdkit_validate(smiles)))
        return results

    def process_paths(self, img_paths: list[str]) -> list[OCSRResult]:
        """Run OCSR on a list of absolute image paths (used by the HTTP service)."""
        if not img_paths:
            return []

        self._load()
        results: list[OCSRResult] = []
        for p in img_paths:
            raw = self._model.predict_final_results(p)
            smiles = raw.get("predicted_smiles") or None
            results.append(OCSRResult(img_path=p, **_rdkit_validate(smiles)))
        return results


def _rdkit_validate(smiles: str | None) -> dict:
    """Canonicalize SMILES via RDKit, derive formula + InChIKey.

    Returns a dict with keys: smiles, canonical_smiles, formula, inchikey, valid.
    """
    if not smiles:
        return dict(smiles=None, canonical_smiles=None, formula=None, inchikey=None, valid=False)

    try:
        from rdkit import Chem
        from rdkit.Chem import rdMolDescriptors
        from rdkit.Chem.inchi import MolToInchiKey

        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return dict(smiles=smiles, canonical_smiles=None, formula=None, inchikey=None, valid=False)

        return dict(
            smiles=smiles,
            canonical_smiles=Chem.MolToSmiles(mol),
            formula=rdMolDescriptors.CalcMolFormula(mol),
            inchikey=MolToInchiKey(mol),
            valid=True,
        )
    except Exception:
        return dict(smiles=smiles, canonical_smiles=None, formula=None, inchikey=None, valid=False)
