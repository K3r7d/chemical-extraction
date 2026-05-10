"""MinerU HTTP client.

The MinerU container exposes a `/parse` endpoint that accepts a PDF upload and
returns JSON with text, figure metadata, and tables. The exact contract is set
when we build docker/mineru.Dockerfile; this client is the consumer side.
"""

from __future__ import annotations

from pathlib import Path

import httpx

from .base import ParsedDocument, ParsedFigure


class MinerUHTTPClient:
    def __init__(self, base_url: str, *, timeout_s: float = 600.0) -> None:
        self._base_url = base_url.rstrip("/")
        self._timeout = httpx.Timeout(timeout_s)

    async def parse(self, pdf_path: Path) -> ParsedDocument:
        async with httpx.AsyncClient(timeout=self._timeout) as client:
            with pdf_path.open("rb") as fh:
                resp = await client.post(
                    f"{self._base_url}/parse",
                    files={"pdf": (pdf_path.name, fh, "application/pdf")},
                )
            resp.raise_for_status()
        data = resp.json()
        raw_output_dir = data.get("output_dir")
        return ParsedDocument(
            text=data["text"],
            figures=[
                ParsedFigure(
                    page=f["page"],
                    bbox=tuple(f["bbox"]),
                    image_path=Path(f["image_path"]),
                    caption=f.get("caption"),
                )
                for f in data.get("figures", [])
            ],
            tables_html=data.get("tables_html", []),
            source_path=pdf_path,
            output_dir=Path(raw_output_dir) if raw_output_dir else None,
        )

    async def health(self) -> bool:
        async with httpx.AsyncClient(timeout=httpx.Timeout(5.0)) as client:
            try:
                resp = await client.get(f"{self._base_url}/health")
                return resp.status_code == 200
            except httpx.RequestError:
                return False
