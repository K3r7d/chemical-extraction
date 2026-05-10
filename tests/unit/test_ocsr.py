"""Unit tests for vision.ocsr — no GPU, no MolNexTR install required."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from a2i2_extraction.vision.ocsr import OCSRResult, _rdkit_validate
from a2i2_extraction.vision.triage import ImageClass, TriageResult

# ---------------------------------------------------------------------------
# _rdkit_validate
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_rdkit_validate_valid_smiles():
    result = _rdkit_validate("CCO")
    assert result["valid"] is True
    assert result["smiles"] == "CCO"
    assert result["canonical_smiles"] == "CCO"
    assert result["formula"] == "C2H6O"
    assert result["inchikey"] is not None


@pytest.mark.unit
def test_rdkit_validate_complex_smiles():
    # Paracetamol
    result = _rdkit_validate("CC(=O)Nc1ccc(O)cc1")
    assert result["valid"] is True
    assert result["formula"] == "C8H9NO2"
    assert result["inchikey"] == "RZVAJINKPMORJF-UHFFFAOYSA-N"


@pytest.mark.unit
def test_rdkit_validate_invalid_smiles():
    result = _rdkit_validate("NOTASMILES!!!")
    assert result["valid"] is False
    assert result["smiles"] == "NOTASMILES!!!"
    assert result["canonical_smiles"] is None
    assert result["formula"] is None


@pytest.mark.unit
def test_rdkit_validate_none_input():
    result = _rdkit_validate(None)
    assert result["valid"] is False
    assert result["smiles"] is None


@pytest.mark.unit
def test_rdkit_validate_empty_string():
    result = _rdkit_validate("")
    assert result["valid"] is False


# ---------------------------------------------------------------------------
# OCSRResult dataclass
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_ocsr_result_valid():
    r = OCSRResult(
        img_path="images/x.jpg",
        smiles="CCO",
        canonical_smiles="CCO",
        formula="C2H6O",
        inchikey="LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
        valid=True,
    )
    assert r.valid is True
    assert r.formula == "C2H6O"


@pytest.mark.unit
def test_ocsr_result_invalid():
    r = OCSRResult(
        img_path="images/x.jpg",
        smiles=None,
        canonical_smiles=None,
        formula=None,
        inchikey=None,
        valid=False,
    )
    assert r.valid is False


# ---------------------------------------------------------------------------
# MolNexTROCSR with mocked MolNexTR model
# ---------------------------------------------------------------------------


def _make_triage_results(n: int, keep: bool = True) -> list[TriageResult]:
    return [
        TriageResult(
            img_path=f"images/{chr(97 + i)}.jpg",
            page_idx=i,
            bbox=[0, 0, 100, 100],
            image_class=ImageClass.SINGLE_STRUCTURE if keep else ImageClass.BIOLOGY,
            confidence=0.8,
            keep=keep,
            caption="",
        )
        for i in range(n)
    ]


@pytest.mark.unit
def test_process_skips_discarded_images(tmp_path):
    from a2i2_extraction.vision.ocsr import MolNexTROCSR

    triage_results = _make_triage_results(3, keep=False)
    ocsr = MolNexTROCSR()
    results = ocsr.process(triage_results, tmp_path)
    assert results == []
    assert ocsr._model is None  # model never loaded


@pytest.mark.unit
def test_process_returns_one_result_per_kept_image(tmp_path):
    from a2i2_extraction.vision.ocsr import MolNexTROCSR

    triage_results = _make_triage_results(2, keep=True)

    mock_model = MagicMock()
    mock_model.predict_final_results.side_effect = [
        {"predicted_smiles": "CCO"},
        {"predicted_smiles": "NOTASMILES!!!"},
    ]

    ocsr = MolNexTROCSR()
    ocsr._model = mock_model

    results = ocsr.process(triage_results, tmp_path)

    assert len(results) == 2
    assert results[0].valid is True
    assert results[0].formula == "C2H6O"
    assert results[1].valid is False


@pytest.mark.unit
def test_process_handles_empty_smiles_from_model(tmp_path):
    from a2i2_extraction.vision.ocsr import MolNexTROCSR

    triage_results = _make_triage_results(1, keep=True)

    mock_model = MagicMock()
    mock_model.predict_final_results.return_value = {"predicted_smiles": ""}

    ocsr = MolNexTROCSR()
    ocsr._model = mock_model

    results = ocsr.process(triage_results, tmp_path)

    assert len(results) == 1
    assert results[0].valid is False
    assert results[0].smiles is None


@pytest.mark.unit
def test_process_paths_empty():
    from a2i2_extraction.vision.ocsr import MolNexTROCSR

    ocsr = MolNexTROCSR()
    results = ocsr.process_paths([])
    assert results == []
    assert ocsr._model is None


@pytest.mark.unit
def test_process_paths_returns_results():
    from a2i2_extraction.vision.ocsr import MolNexTROCSR

    mock_model = MagicMock()
    mock_model.predict_final_results.return_value = {"predicted_smiles": "c1ccccc1"}

    ocsr = MolNexTROCSR()
    ocsr._model = mock_model

    results = ocsr.process_paths(["/outputs/images/x.jpg"])

    assert len(results) == 1
    assert results[0].img_path == "/outputs/images/x.jpg"
    assert results[0].valid is True
    assert results[0].formula == "C6H6"
