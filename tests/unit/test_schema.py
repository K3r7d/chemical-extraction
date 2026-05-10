"""Schema-shape unit tests."""

from __future__ import annotations

import pytest

from a2i2_extraction.validators import Severity, check_schema

pytestmark = pytest.mark.unit


def test_valid_sample_passes(sample_extraction):
    assert check_schema(sample_extraction) == []


def test_missing_top_level_key_fails(sample_extraction):
    del sample_extraction["paper"]
    issues = check_schema(sample_extraction)
    assert any("paper" in i.message for i in issues)


def test_invalid_role_rejected(sample_extraction):
    sample_extraction["compounds"][0]["role"] = "not_a_real_role"
    issues = check_schema(sample_extraction)
    assert any(i.severity is Severity.ERROR for i in issues)


def test_compound_id_pattern_enforced(sample_extraction):
    sample_extraction["compounds"][0]["id"] = "CX"
    issues = check_schema(sample_extraction)
    # jsonschema phrases this as "does not match ... C\\d{2,}"
    assert any(
        i.severity is Severity.ERROR and "compounds/0/id" in i.path
        for i in issues
    )


def test_extraction_date_format_enforced(sample_extraction):
    sample_extraction["extraction"]["extraction_date"] = "May 3, 2026"
    issues = check_schema(sample_extraction)
    assert any(i.severity is Severity.ERROR for i in issues)


def test_extra_property_rejected(sample_extraction):
    sample_extraction["compounds"][0]["smiles"] = "c1ccccc1"  # not in v3.4
    issues = check_schema(sample_extraction)
    assert any("smiles" in i.message.lower() for i in issues)
