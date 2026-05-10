"""Unit tests for vision.triage — no GPU, no model download."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
import torch

from a2i2_extraction.vision.triage import (
    _ORDERED_CLASSES,
    KEEP_CLASSES,
    ImageClass,
    ImageTriage,
    TriageResult,
    _find_content_list,
    _load_image_entries,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

FAKE_CONTENT_LIST = [
    {
        "type": "image",
        "img_path": "images/aaa.jpg",
        "image_caption": ["Scheme 1."],
        "image_footnote": [],
        "bbox": [10, 20, 300, 400],
        "page_idx": 1,
    },
    {
        "type": "image",
        "img_path": "images/bbb.jpg",
        "image_caption": [],
        "image_footnote": [],
        "bbox": [50, 60, 200, 300],
        "page_idx": 2,
    },
    {
        "type": "text",  # should be ignored
        "text": "Some paragraph text.",
    },
    {
        "type": "image",
        "img_path": "images/ccc.jpg",
        "image_caption": ["Figure 3."],
        "image_footnote": [],
        "bbox": [0, 0, 100, 100],
        "page_idx": 3,
    },
]


@pytest.fixture()
def fake_output_dir(tmp_path: Path) -> Path:
    """Create a minimal MinerU auto/ directory with content_list + dummy images."""
    (tmp_path / "images").mkdir()
    for name in ("aaa.jpg", "bbb.jpg", "ccc.jpg"):
        # 1x1 white JPEG written as raw bytes — no Pillow needed for file creation
        (tmp_path / "images" / name).write_bytes(
            b"\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00"
            b"\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t"
            b"\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a"
            b"\x1f\x1e\x1d\x1a\x1c\x1c $.' \",#\x1c\x1c(7),01444\x1f'9=82<.342\x1e"
            b"\xff\xc0\x00\x0b\x08\x00\x01\x00\x01\x01\x01\x11\x00"
            b"\xff\xc4\x00\x1f\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00"
            b"\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b"
            b"\xff\xc4\x00\xb5\x10\x00\x02\x01\x03\x03\x02\x04\x03\x05\x05\x04"
            b"\x04\x00\x00\x01}\x01\x02\x03\x00\x04\x11\x05\x12!1A\x06\x13Qa"
            b'\x07"q\x142\x81\x91\xa1\x08#B\xb1\xc1\x15R\xd1\xf0$3br'
            b"\xff\xda\x00\x08\x01\x01\x00\x00?\x00\xfb\xd4P\x00\x00\x00\x1f\xff\xd9"
        )

    cl_path = tmp_path / "doc_content_list.json"
    cl_path.write_text(json.dumps(FAKE_CONTENT_LIST), encoding="utf-8")
    return tmp_path


# ---------------------------------------------------------------------------
# ImageClass / KEEP_CLASSES
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_keep_classes_are_chemistry():
    assert ImageClass.REACTION_SCHEME in KEEP_CLASSES
    assert ImageClass.SINGLE_STRUCTURE in KEEP_CLASSES
    assert ImageClass.STRUCTURE_PANEL in KEEP_CLASSES


@pytest.mark.unit
def test_non_chemistry_classes_not_kept():
    for cls in (
        ImageClass.SPECTRUM,
        ImageClass.BIOLOGY,
        ImageClass.TABLE_IMAGE,
        ImageClass.OTHER,
    ):
        assert cls not in KEEP_CLASSES


@pytest.mark.unit
def test_ordered_classes_covers_all():
    assert set(_ORDERED_CLASSES) == set(ImageClass)
    assert len(_ORDERED_CLASSES) == 7


# ---------------------------------------------------------------------------
# _find_content_list
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_find_content_list_returns_non_v2(fake_output_dir: Path):
    path = _find_content_list(fake_output_dir)
    assert path.name == "doc_content_list.json"


@pytest.mark.unit
def test_find_content_list_ignores_v2(tmp_path: Path):
    (tmp_path / "doc_content_list_v2.json").write_text("[]")
    (tmp_path / "doc_content_list.json").write_text("[]")
    path = _find_content_list(tmp_path)
    assert "_v2" not in path.name


@pytest.mark.unit
def test_find_content_list_raises_when_missing(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        _find_content_list(tmp_path)


# ---------------------------------------------------------------------------
# _load_image_entries
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_load_image_entries_filters_non_image(fake_output_dir: Path):
    entries = _load_image_entries(fake_output_dir)
    assert len(entries) == 3  # only the 3 image-type entries
    assert all(e["type"] == "image" for e in entries)


@pytest.mark.unit
def test_load_image_entries_preserves_order(fake_output_dir: Path):
    entries = _load_image_entries(fake_output_dir)
    assert entries[0]["img_path"] == "images/aaa.jpg"
    assert entries[1]["img_path"] == "images/bbb.jpg"
    assert entries[2]["img_path"] == "images/ccc.jpg"


# ---------------------------------------------------------------------------
# TriageResult
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_triage_result_keep_flag():
    r = TriageResult(
        img_path="images/x.jpg",
        page_idx=0,
        bbox=[0, 0, 100, 100],
        image_class=ImageClass.REACTION_SCHEME,
        confidence=0.87,
        keep=True,
        caption="Scheme 1.",
    )
    assert r.keep is True
    assert r.image_class is ImageClass.REACTION_SCHEME


@pytest.mark.unit
def test_triage_result_discard_flag():
    r = TriageResult(
        img_path="images/x.jpg",
        page_idx=1,
        bbox=[],
        image_class=ImageClass.BIOLOGY,
        confidence=0.91,
        keep=False,
        caption="",
    )
    assert r.keep is False


# ---------------------------------------------------------------------------
# ImageTriage with mocked model
# ---------------------------------------------------------------------------


def _inject_model(triage: ImageTriage, n_images: int) -> MagicMock:
    """Bypass _load() by directly injecting a mock model and processor.

    get_image_features returns (n_images, 64) ones; logit_scale=1, bias=0.
    text_features are set to all-ones (normalised), so all class logits are
    equal — caller controls final class via patch("torch.sigmoid").
    """
    mock_model = MagicMock()
    mock_model.get_image_features.return_value = torch.ones(n_images, 64)
    mock_model.logit_scale = MagicMock()
    mock_model.logit_scale.exp.return_value = torch.tensor(1.0)
    mock_model.logit_bias = torch.tensor(0.0)

    mock_processor = MagicMock()
    mock_processor.return_value.to.return_value.pixel_values = torch.zeros(
        n_images, 3, 224, 224
    )

    triage._model = mock_model
    triage._processor = mock_processor
    # Normalised text features: shape (7, 64) with equal magnitude.
    triage._text_features = torch.ones(7, 64) / (64**0.5)
    return mock_model


@pytest.mark.unit
def test_triage_keeps_reaction_scheme(fake_output_dir: Path):
    """When SigLIP predicts reaction_scheme with high confidence, keep=True."""
    scheme_idx = _ORDERED_CLASSES.index(ImageClass.REACTION_SCHEME)
    triage = ImageTriage(confidence_threshold=0.5)
    _inject_model(triage, n_images=3)

    fake_probs = torch.zeros(3, 7)
    fake_probs[:, scheme_idx] = 0.85

    with (
        patch("a2i2_extraction.vision.triage.Image") as mock_pil,
        patch("torch.sigmoid", return_value=fake_probs),
    ):
        mock_pil.open.return_value.convert.return_value = MagicMock()
        results = triage.triage_document(fake_output_dir)

    assert len(results) == 3
    assert all(r.image_class is ImageClass.REACTION_SCHEME for r in results)
    assert all(r.keep for r in results)


@pytest.mark.unit
def test_triage_discards_biology(fake_output_dir: Path):
    """When SigLIP predicts biology, keep=False regardless of confidence."""
    bio_idx = _ORDERED_CLASSES.index(ImageClass.BIOLOGY)
    triage = ImageTriage(confidence_threshold=0.5)
    _inject_model(triage, n_images=3)

    fake_probs = torch.zeros(3, 7)
    fake_probs[:, bio_idx] = 0.95

    with (
        patch("a2i2_extraction.vision.triage.Image") as mock_pil,
        patch("torch.sigmoid", return_value=fake_probs),
    ):
        mock_pil.open.return_value.convert.return_value = MagicMock()
        results = triage.triage_document(fake_output_dir)

    assert all(r.image_class is ImageClass.BIOLOGY for r in results)
    assert not any(r.keep for r in results)


@pytest.mark.unit
def test_triage_confidence_threshold_gates_keep(fake_output_dir: Path):
    """A chemistry class below the confidence threshold → keep=False."""
    scheme_idx = _ORDERED_CLASSES.index(ImageClass.REACTION_SCHEME)
    triage = ImageTriage(confidence_threshold=0.8)
    _inject_model(triage, n_images=3)

    # Chemistry class wins, but confidence 0.6 < threshold 0.8.
    fake_probs = torch.zeros(3, 7)
    fake_probs[:, scheme_idx] = 0.6

    with (
        patch("a2i2_extraction.vision.triage.Image") as mock_pil,
        patch("torch.sigmoid", return_value=fake_probs),
    ):
        mock_pil.open.return_value.convert.return_value = MagicMock()
        results = triage.triage_document(fake_output_dir)

    assert all(r.image_class is ImageClass.REACTION_SCHEME for r in results)
    assert not any(r.keep for r in results)


@pytest.mark.unit
def test_triage_empty_content_list(tmp_path: Path):
    """No images in content_list → empty result, model never loaded."""
    (tmp_path / "doc_content_list.json").write_text(
        json.dumps([{"type": "text", "text": "hello"}])
    )
    triage = ImageTriage()
    results = triage.triage_document(tmp_path)
    assert results == []
    assert triage._model is None  # never loaded


@pytest.mark.unit
def test_kept_helper_filters_correctly():
    results = [
        TriageResult("a.jpg", 0, [], ImageClass.REACTION_SCHEME, 0.9, True, ""),
        TriageResult("b.jpg", 1, [], ImageClass.BIOLOGY, 0.8, False, ""),
        TriageResult("c.jpg", 2, [], ImageClass.SINGLE_STRUCTURE, 0.7, True, ""),
    ]
    triage = ImageTriage()
    kept = triage.kept(results)
    assert len(kept) == 2
    assert all(r.keep for r in kept)
