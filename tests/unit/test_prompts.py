"""Prompt unit tests."""

from __future__ import annotations

import pytest

from a2i2_extraction.prompts import build_extraction_prompt

pytestmark = pytest.mark.unit


def test_prompt_contains_schema_and_version():
    prompt = build_extraction_prompt(paper_text="MAIN BODY")
    assert "v3.4.1" in prompt
    assert "OUTPUT SCHEMA" in prompt


def test_rule_4_deterministic_traversal():
    prompt = build_extraction_prompt(paper_text="MAIN BODY")
    assert "RULE 4" in prompt
    assert "SI Scheme S1" in prompt


def test_build_prompt_with_si():
    prompt = build_extraction_prompt(paper_text="MAIN BODY", si_text="SI BODY")
    assert "MAIN BODY" in prompt
    assert "SI BODY" in prompt
    assert "=== SUPPORTING INFORMATION ===" in prompt


def test_build_prompt_without_si():
    prompt = build_extraction_prompt(paper_text="MAIN BODY")
    assert "MAIN BODY" in prompt
    assert "SUPPORTING INFORMATION" not in prompt


def test_build_prompt_with_reference_table():
    prompt = build_extraction_prompt(
        paper_text="MAIN BODY", reference_table="TABLE CONTENT"
    )
    assert "TABLE CONTENT" in prompt
    assert "=== COMPOUND REFERENCE TABLE ===" in prompt
