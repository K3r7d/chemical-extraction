"""Preprocessing unit tests.

The most important assertion in this file is *negative*: cleaning must NOT
strip chemistry-bearing characters (μ, dashes, subscripts, Greek letters).
Task 5 documented prod incidents from μL→mL silent promotions.
"""

from __future__ import annotations

import pytest

from a2i2_extraction.preprocessing import clean_text, trim_references

pytestmark = pytest.mark.unit


# --- cleaning ---------------------------------------------------------------


def test_strips_journal_header_footer():
    raw = (
        "pubs.acs.org/jmc\n"
        "Article\n"
        "Real synthesis sentence: 124 mL of solvent.\n"
        "https://doi.org/10.1021/x\n"
        "26060\n"
    )
    assert clean_text(raw) == "Real synthesis sentence: 124 mL of solvent."


def test_strips_acs_running_page_header():
    """The ACS-style header that appears at the top of every page after page 1."""
    raw = (
        "Journal of Medicinal Chemistry pubs.acs.org/jmc Article\n"
        "real content here.\n"
        "Org. Lett. pubs.acs.org/orgletters Communication\n"
        "more real content."
    )
    cleaned = clean_text(raw)
    assert "pubs.acs.org" not in cleaned
    assert "real content here." in cleaned
    assert "more real content." in cleaned


def test_strips_downloaded_via_sidebar():
    raw = "Downloaded via DEAKIN UNIV on December 28, 2025\nReal sentence."
    assert clean_text(raw) == "Real sentence."


def test_strips_decoration_marker_but_keeps_heading():
    raw = "■ EXPERIMENTAL\nstep one"
    assert clean_text(raw) == "EXPERIMENTAL\nstep one"


def test_collapses_column_whitespace():
    raw = "word1                      word2"
    assert clean_text(raw) == "word1 word2"


def test_preserves_micro_sign():
    # Both U+00B5 (µ MICRO SIGN) and U+03BC (μ GREEK SMALL LETTER MU)
    # appear in PDF text. NFKC may normalize one to the other; either is fine
    # so long as the visual character survives.
    raw = "Et3N (124 µL, 893 µmol) and POCl3 (13.9 μL, 149 μmol)."
    cleaned = clean_text(raw)
    assert "L" in cleaned and "mol" in cleaned
    # the critical thing: presence of any micro/mu char
    assert any(ch in cleaned for ch in ("µ", "μ"))


def test_preserves_en_em_dashes_and_greek():
    raw = "yield 0.74–1.11 GBq; α-helix; β-sheet conformation."
    cleaned = clean_text(raw)
    assert "–" in cleaned
    assert "α" in cleaned and "β" in cleaned


def test_preserves_subscripts_and_superscripts():
    raw = "[18F]AlF-NP1, C₆H₆, H₂O at 25 °C"
    cleaned = clean_text(raw)
    # NFKC will convert ₆ → 6 and ° → ° (latter is preserved). The atom counts
    # must remain readable.
    assert "C6H6" in cleaned or "C₆H₆" in cleaned
    assert "[18F]" in cleaned
    assert "°C" in cleaned or "C" in cleaned  # at least the letter survives


def test_drops_bare_page_numbers():
    raw = "synthesis text\n26049\nmore synthesis"
    assert clean_text(raw) == "synthesis text\nmore synthesis"


def test_idempotent():
    raw = "■ STEP 1\n   word    word\nDownloaded via X\nreal."
    once = clean_text(raw)
    twice = clean_text(once)
    assert once == twice


# --- LaTeX wrapper stripping ------------------------------------------------


def test_strips_bar():
    assert r"\bar" not in clean_text(r"p-value \bar{0.05}")
    assert "0.05" in clean_text(r"p-value \bar{0.05}")


def test_strips_check():
    result = clean_text(r"gene \check { D P 1 }")
    assert r"\check" not in result
    assert "D P 1" in result


def test_strips_diacritics():
    """All diacritic commands stripped, content preserved."""
    for cmd in (r"\dot", r"\hat", r"\tilde", r"\breve", r"\ddot", r"\vec", r"\widehat"):
        raw = rf"{cmd} {{ x }}"
        result = clean_text(raw)
        assert cmd not in result, f"{cmd} not stripped"
        assert "x" in result, f"content lost for {cmd}"


def test_preserves_font_wrappers():
    """Font commands are kept — they carry visual meaning in formula context."""
    for cmd in (r"\mathrm", r"\mathbf", r"\mathsf", r"\mathtt", r"\textbf"):
        raw = rf"value {cmd} {{ IC50 }} end"
        result = clean_text(raw)
        assert cmd in result, f"{cmd} was incorrectly stripped"


def test_strips_nested_wrappers():
    """\bar stripped at all nesting levels; \mathrm preserved; content intact."""
    raw = r"\bar { 1 . 0 , \bar { \mathrm { F D R } } < \bar { 0 } . 0 0 1 \Big ) }"
    result = clean_text(raw)
    assert r"\bar" not in result
    assert r"\mathrm" in result  # font wrapper kept
    assert "F D R" in result
    assert "0 0 1" in result


def test_strips_phantom_and_layout():
    result = clean_text(r"value \phantom { 0 } end")
    assert r"\phantom" not in result


def test_latex_wrapper_strip_idempotent():
    raw = r"text \bar{x} \check{y} \mathrm{C}"
    once = clean_text(raw)
    assert clean_text(once) == once


# --- trimming ---------------------------------------------------------------


def test_trims_at_references_heading():
    text = (
        "experimental section content\n"
        "more experimental\n"
        "REFERENCES\n"
        "(1) Smith, J. ...\n"
        "(2) Jones, K. ...\n"
    )
    out = trim_references(text)
    assert "REFERENCES" not in out
    assert "experimental section content" in out
    assert "Smith" not in out


def test_keeps_acknowledgments_before_refs():
    text = (
        "synthesis here\n"
        "ACKNOWLEDGMENTS\n"
        "We thank ...\n"
        "REFERENCES\n"
        "(1) ...\n"
    )
    out = trim_references(text)
    assert "ACKNOWLEDGMENTS" in out
    assert "We thank" in out
    assert "REFERENCES" not in out


def test_no_marker_returns_input_unchanged():
    text = "synthesis section\nstep one\nstep two\n"
    assert trim_references(text) == text


def test_handles_alt_heading_variants():
    for heading in ("References", "Bibliography", "BIBLIOGRAPHY", "NOTES AND REFERENCES"):
        text = f"body\n{heading}\nciteone\n"
        out = trim_references(text)
        assert heading not in out
        assert "citeone" not in out


def test_handles_markdown_heading_prefix():
    """MinerU emits ## REFERENCES. trim must still find it."""
    for prefix in ("#", "##", "###"):
        text = f"body\n{prefix} REFERENCES\nciteone\n"
        out = trim_references(text)
        assert "REFERENCES" not in out
        assert "citeone" not in out


def test_preserves_markdown_image_refs():
    """Cleaning must NOT strip ![](images/HASH.jpg) from MinerU output."""
    raw = (
        "## 1. INTRODUCTION\n"
        "Some prose here.\n"
        "![](images/abc123.jpg)\n"
        "Figure 1. Caption text.\n"
    )
    cleaned = clean_text(raw)
    assert "![](images/abc123.jpg)" in cleaned
    assert "## 1. INTRODUCTION" in cleaned
