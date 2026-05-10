"""Local PDF→text fallback using poppler's `pdftotext`.

Implements the MinerUClient Protocol so the pipeline can run end-to-end on a
laptop without a GPU or Docker. Quality is well below MinerU 2.x — no layout,
no figure extraction, no tables-as-HTML. Use ONLY for dry-runs and tests.
"""

from __future__ import annotations

import asyncio
import shutil
from pathlib import Path

from .base import ParsedDocument


class PdfToTextLocalClient:
    """Shell-out to system `pdftotext` (poppler-utils)."""

    def __init__(self) -> None:
        if shutil.which("pdftotext") is None:
            raise RuntimeError(
                "pdftotext not found on PATH; install poppler-utils "
                "or use the real MinerU service"
            )

    async def parse(self, pdf_path: Path) -> ParsedDocument:
        proc = await asyncio.create_subprocess_exec(
            "pdftotext",
            "-layout",
            str(pdf_path),
            "-",  # stdout
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        if proc.returncode != 0:
            raise RuntimeError(
                f"pdftotext failed for {pdf_path}: {stderr.decode(errors='replace')}"
            )
        return ParsedDocument(
            text=stdout.decode("utf-8", errors="replace"),
            source_path=pdf_path,
        )

    async def health(self) -> bool:
        return True
