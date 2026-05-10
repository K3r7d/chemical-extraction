"""Trim non-synthesis tail content (References, Bibliography).

Cuts at the first 'REFERENCES' or 'Bibliography' section header. ACS papers
mark this with a black-square decorator that cleaning.py already strips, so
we only see the bare heading here.
"""

from __future__ import annotations

import re

# Heading variants that signal end of synthesis-relevant content.
# Tolerates markdown heading prefix (#, ##, ###) since MinerU emits markdown.
_REF_HEADING = re.compile(
    r"^\s*#{0,4}\s*(REFERENCES|References|Bibliography|BIBLIOGRAPHY|"
    r"NOTES AND REFERENCES|REFERENCES AND NOTES)\s*$"
)


def trim_references(text: str) -> str:
    """Drop everything from the first References-style heading onward.

    Keeps Acknowledgments, Author Information, Funding (those appear BEFORE
    References in ACS layout). If no marker is found, the input is returned
    unchanged — never silently truncate by guessing.
    """
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if _REF_HEADING.match(line):
            return "\n".join(lines[:i]).rstrip()
    return text
