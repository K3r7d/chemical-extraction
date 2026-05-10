"""Clean PDF-extraction artifacts.

Hard rule: PRESERVE every chemistry-bearing character. μ vs m, en/em dashes,
subscripts/superscripts, Greek letters all carry information per Task 5
(unit-mismatch incidents). Only strip what is provably journal/PDF noise.
"""

from __future__ import annotations

import re
import unicodedata

# Normalization-safe ligatures: ﬁ→fi, ﬂ→fl, etc. NFKC handles these.
# We use NFKC because no chemistry character is decomposed in a lossy way by it.

# Lines we DROP entirely (matched after stripping leading/trailing whitespace):
_DROP_LINE_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"^pubs\.acs\.org(/\w+)?$", re.IGNORECASE),
    re.compile(r"^https?://doi\.org/.*$", re.IGNORECASE),
    re.compile(r"^https?://pubs\.acs\.org/.*$", re.IGNORECASE),
    re.compile(r"^Downloaded via .*$", re.IGNORECASE),
    re.compile(r"^See https?://pubs\.acs\.org/sharingguidelines.*$", re.IGNORECASE),
    # ACS running page header (after our column-collapse runs, this becomes one line):
    # "Journal of Medicinal Chemistry pubs.acs.org/jmc Article"
    re.compile(
        r"^[\w&. ]{4,80}\s+pubs\.acs\.org/\w+\s+(Article|Perspective|Review|Communication)$",
        re.IGNORECASE,
    ),
    re.compile(r"^Article$"),  # standalone column header
    re.compile(r"^[Pp]erspective$"),
    re.compile(r"^[Rr]eview$"),
    re.compile(r"^\d{1,5}$"),  # bare page number
    re.compile(r"^J\. Med\. Chem\. \d{4}.*$", re.IGNORECASE),  # running footer
    re.compile(r"^J\. Org\. Chem\. \d{4}.*$", re.IGNORECASE),
    re.compile(r"^ACS Med\. Chem\. Lett\..*$", re.IGNORECASE),
    re.compile(r"^Chem\. Rev\. \d{4}.*$", re.IGNORECASE),
    re.compile(r"^Org\. Lett\..*$", re.IGNORECASE),
    re.compile(r"^Cite This:.*$", re.IGNORECASE),
    re.compile(r"^Read Online$", re.IGNORECASE),
    re.compile(r"^ACCESS$"),
    re.compile(r"^Metrics & More$"),
    re.compile(r"^Article Recommendations$"),
    re.compile(r"^\*?sı?\s*Supporting Information$", re.IGNORECASE),
)

# Markers we strip from line starts (decoration, no content):
_DECORATION_RE = re.compile(r"^[■▪◆●○▲△□◇★☆\*]+\s*")

# Standalone superscript/subscript fragment lines that pdftotext spits out
# when it breaks "[18F]" across columns. Lines that are just digits with
# trailing whitespace and no other content.
_BARE_DIGIT_LINE = re.compile(r"^\d{1,3}$")

# Long whitespace runs from column-aware extraction.
_LONG_WS = re.compile(r" {4,}")

# MinerU's formula parser wraps plain text in LaTeX commands that have no
# chemistry meaning. Strip command, keep content inside braces.
#
# Diacritics: \bar \check \dot \hat \tilde \breve \ddot \vec \widehat \widetilde \mathring
# Layout noise: \phantom \scriptstyle \small \overline \underline \operatorname
#
# Font wrappers (\mathrm, \mathbf, \mathsf, etc.) are intentionally kept —
# they carry visual meaning in formula context.
_LATEX_WRAPPER_RE = re.compile(
    r"\\(?:"
    # diacritics
    r"bar|check|dot|hat|tilde|breve|ddot|vec|widehat|widetilde|mathring"
    r"|"
    # layout noise
    r"phantom|scriptstyle|small|overline|underline|operatorname"
    r")\s*\{"
)


def _strip_latex_wrappers(text: str) -> str:
    """Remove LaTeX wrapper commands, keeping the inner content.

    Handles nesting and spaces between command and brace. Applies
    iteratively until no matched command remains.
    """
    while True:
        m = _LATEX_WRAPPER_RE.search(text)
        if not m:
            break
        depth = 1
        pos = m.end()  # just after the opening '{'
        while pos < len(text) and depth > 0:
            if text[pos] == "{":
                depth += 1
            elif text[pos] == "}":
                depth -= 1
            pos += 1
        inner = text[m.end() : pos - 1]
        text = text[: m.start()] + inner + text[pos:]
    return text


def clean_text(text: str) -> str:
    """Apply all cleaning passes. Idempotent."""
    text = unicodedata.normalize("NFKC", text)
    text = _strip_latex_wrappers(text)

    out_lines: list[str] = []
    blank_run = 0
    for raw in text.splitlines():
        line = raw.rstrip()
        # collapse big internal whitespace runs first (column gutters)
        line = _LONG_WS.sub(" ", line)
        stripped = line.strip()

        if not stripped:
            blank_run += 1
            if blank_run <= 2:  # keep at most one paragraph break
                out_lines.append("")
            continue
        blank_run = 0

        # Strip decorative leading markers BEFORE pattern check (so "■ REFERENCES"
        # would still be caught by trim_references, which sees the cleaned form).
        stripped = _DECORATION_RE.sub("", stripped)

        if any(p.match(stripped) for p in _DROP_LINE_PATTERNS):
            continue
        if _BARE_DIGIT_LINE.match(stripped):
            continue

        out_lines.append(stripped)

    # Re-collapse trailing/leading blank runs created by drops.
    while out_lines and out_lines[0] == "":
        out_lines.pop(0)
    while out_lines and out_lines[-1] == "":
        out_lines.pop()

    return "\n".join(out_lines)
