"""MS arithmetic unit tests."""

from __future__ import annotations

import pytest

from a2i2_extraction.validators import check_ms_arithmetic
from a2i2_extraction.validators.ms_arithmetic import (
    _exact_mass_from_formula,
    exact_mass_for_smiles,
)

pytestmark = pytest.mark.unit


def test_benzoic_acid_mass():
    # C7H6O2 monoisotopic = 122.0368
    m = _exact_mass_from_formula("C7H6O2")
    assert m is not None
    assert abs(m - 122.0368) < 0.001


def test_unknown_element_returns_none():
    assert _exact_mass_from_formula("U2O3") is None


def test_clean_sample_no_mismatch(sample_extraction):
    assert check_ms_arithmetic(sample_extraction) == []


def test_mismatch_flagged(sample_extraction):
    sample_extraction["compounds"][0]["ms_calculated_exact_mass"] = 999.0
    issues = check_ms_arithmetic(sample_extraction)
    assert any(i.code == "ms_arithmetic_mismatch" for i in issues)


def test_smiles_mass_matches_formula_mass():
    # benzene C6H6: monoisotopic 78.0470
    m = exact_mass_for_smiles("c1ccccc1")
    assert m is not None
    assert abs(m - 78.0470) < 0.001
