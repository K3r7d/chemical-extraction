"""Client Protocols.

Concrete clients (HTTP, mock, future cluster-specific impls) implement these.
Tests inject mocks via the Protocol contract.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol


@dataclass(frozen=True)
class ParsedFigure:
    page: int
    bbox: tuple[float, float, float, float]
    image_path: Path
    caption: str | None = None


@dataclass(frozen=True)
class ParsedDocument:
    """Output of a document-parsing service (MinerU)."""

    text: str
    figures: list[ParsedFigure] = field(default_factory=list)
    tables_html: list[str] = field(default_factory=list)
    source_path: Path | None = None
    output_dir: Path | None = None  # the auto/ directory; needed by triage to find content_list.json


class MinerUClient(Protocol):
    async def parse(self, pdf_path: Path) -> ParsedDocument: ...


class LLMClient(Protocol):
    async def complete(
        self,
        prompt: str,
        *,
        max_tokens: int | None = None,
        temperature: float | None = None,
    ) -> str: ...
