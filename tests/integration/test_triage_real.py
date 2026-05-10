"""Integration test: real SigLIP 2 inference on paper 1's MinerU output.

Run with:
    uv run pytest tests/integration/test_triage_real.py -v -m slow -s
"""

from __future__ import annotations

from pathlib import Path

import pytest

from a2i2_extraction.vision.triage import KEEP_CLASSES

PAPER_1_AUTO_DIR = Path(
    "outputs/mineru/1/"
    "18f-68ga-labeled-peptide-based-probes-for-pet-imaging-of-ror1-expression/auto"
)


@pytest.mark.slow
@pytest.mark.integration
def test_triage_paper1_real(tmp_path):
    """Run real SigLIP 2 on paper 1 and print per-image classifications."""
    if not PAPER_1_AUTO_DIR.exists():
        pytest.skip(f"MinerU output not found: {PAPER_1_AUTO_DIR}")

    from a2i2_extraction.vision.triage import ImageTriage

    triage = ImageTriage(
        confidence_threshold=0.0,  # pure argmax — SigLIP zero-shot scores are low in absolute terms
        batch_size=8,
    )
    results = triage.triage_document(PAPER_1_AUTO_DIR)

    print(f"\n{'─'*72}")
    print(f"{'IMG':<55} {'CLASS':<18} {'CONF':>5}  KEEP")
    print(f"{'─'*72}")
    for r in results:
        name = Path(r.img_path).name[:52]
        keep_mark = "✓" if r.keep else "✗"
        print(f"{name:<55} {r.image_class:<18} {r.confidence:>5.2f}  {keep_mark}")
    print(f"{'─'*72}")

    kept = triage.kept(results)
    discarded = [r for r in results if not r.keep]
    print(f"\nTotal: {len(results)}  kept: {len(kept)}  discarded: {len(discarded)}")
    if kept:
        print("\nKept images (chemistry-relevant):")
        for r in kept:
            print(f"  page {r.page_idx:>2}  {r.image_class:<18}  {Path(r.img_path).name}")

    # Sanity assertions — not strict accuracy, just structural correctness.
    assert len(results) > 0, "should have classified at least one image"
    assert all(hasattr(r, "image_class") for r in results)
    assert all(0.0 <= r.confidence <= 1.0 for r in results)
    assert all(r.keep == (r.image_class in KEEP_CLASSES) for r in results)
    # Paper 1 is a radiolabeled peptide paper — expect at least some structures.
    assert len(kept) >= 1, "expected at least one chemistry image in paper 1"
