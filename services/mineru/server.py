"""MinerU HTTP wrapper.

Accepts a PDF upload, returns the parsed markdown + figures as JSON.

Output lives **inside the paper folder** under DATA_PAPERS_ROOT:
    <DATA_PAPERS_ROOT>/<N>/mineru/<stem>/auto/<stem>.md
        + auto/images/*.jpg

This means a freshly-downloaded data zip can ship pre-parsed mineru output
alongside its PDFs and the server will serve straight from the cache without
invoking the CLI. On a cache miss (no `<stem>.md` for the uploaded PDF) the
server falls back to running `mineru` on the raw PDF and writes the output
into the same folder.

Environment variables:
    DATA_PAPERS_ROOT    paper-index root (default data/papers)
    MINERU_DEVICE_MODE  cuda | cpu | auto-detected via torch
    MINERU_KEEP_DEBUG   1 = retain debug PDFs / model.json / middle.json
"""

from __future__ import annotations

import asyncio
import os
import shutil
import sys
import tempfile
from pathlib import Path

import uvicorn
from fastapi import FastAPI, File, HTTPException, UploadFile

DATA_PAPERS_ROOT = Path(os.getenv("DATA_PAPERS_ROOT", "data/papers"))
PARSE_TIMEOUT_S = float(os.getenv("MINERU_PARSE_TIMEOUT_S", "600"))
# By default, prune MinerU's debug artifacts (origin/layout/span PDFs, model.json,
# middle.json — together ~35 MB/paper) after a successful parse. Set
# MINERU_KEEP_DEBUG=1 to retain them for troubleshooting.
KEEP_DEBUG = os.getenv("MINERU_KEEP_DEBUG", "0") == "1"

app = FastAPI(title="mineru-service", version="0.1.0")


def _mineru_bin() -> str:
    candidate = Path(sys.executable).parent / "mineru"
    if candidate.exists():
        return str(candidate)
    found = shutil.which("mineru")
    if found:
        return found
    raise RuntimeError("mineru CLI not found")


def _resolve_paper_index(stem: str) -> str | None:
    """Return the paper-index folder name (e.g. "7") that contains `<stem>.pdf`."""
    if not DATA_PAPERS_ROOT.is_dir():
        return None
    for paper_dir in DATA_PAPERS_ROOT.iterdir():
        if not paper_dir.is_dir():
            continue
        if (paper_dir / f"{stem}.pdf").exists():
            return paper_dir.name
    return None


def _device() -> str:
    explicit = os.getenv("MINERU_DEVICE_MODE")
    if explicit:
        return explicit
    try:
        import torch
        return "cuda" if torch.cuda.is_available() else "cpu"
    except ImportError:
        return "cpu"


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


def _prune_debug_artifacts(auto_dir: Path) -> None:
    """Drop MinerU's debug PDFs and intermediate JSONs.

    Keeps only the markdown, the figures, and the small content_list.json
    (useful structured content). Saves ~35 MB / paper.
    """
    for child in auto_dir.iterdir():
        if child.is_dir():
            if child.name != "images":
                shutil.rmtree(child, ignore_errors=True)
            continue
        name = child.name
        if name.endswith(".md"):
            continue
        if name.endswith("_content_list.json"):
            continue
        child.unlink(missing_ok=True)


def _assemble_response(md_path: Path) -> dict:
    images_dir = md_path.parent / "images"
    text = md_path.read_text(encoding="utf-8", errors="replace")
    figures = []
    if images_dir.exists():
        for img in sorted(images_dir.iterdir()):
            if img.suffix.lower() in (".jpg", ".jpeg", ".png"):
                figures.append({
                    "page": -1,
                    "bbox": [0, 0, 0, 0],
                    "image_path": str(img),
                    "caption": None,
                })
    return {
        "text": text,
        "figures": figures,
        "tables_html": [],
        "output_dir": str(md_path.parent),
    }


def _cached_md(stem: str) -> Path | None:
    """Return cached <stem>.md under data/papers/<any>/mineru/ if present."""
    if not DATA_PAPERS_ROOT.is_dir():
        return None
    for paper_dir in DATA_PAPERS_ROOT.iterdir():
        candidate = paper_dir / "mineru" / stem / "auto" / f"{stem}.md"
        if candidate.exists():
            return candidate
    return None


@app.post("/parse")
async def parse(pdf: UploadFile = File(...)) -> dict:
    stem = Path(pdf.filename or "document").stem

    cached = _cached_md(stem)
    if cached is not None:
        return _assemble_response(cached)

    idx = _resolve_paper_index(stem)
    if idx is None:
        raise HTTPException(
            status_code=404,
            detail=(
                f"cannot locate {stem!r} under {DATA_PAPERS_ROOT}/<N>/ — "
                f"drop the PDF into a paper folder before parsing."
            ),
        )

    out_dir = DATA_PAPERS_ROOT / idx / "mineru"
    out_dir.mkdir(parents=True, exist_ok=True)

    pdf_bytes = await pdf.read()

    # Stage the upload as <stem>.pdf so MinerU writes
    # <out_dir>/<stem>/auto/<stem>.md (rather than tmp<rand>.md).
    work_dir = Path(tempfile.mkdtemp(prefix="mineru-"))
    pdf_path = work_dir / f"{stem}.pdf"
    pdf_path.write_bytes(pdf_bytes)

    try:
        env = os.environ.copy()
        env["MINERU_DEVICE_MODE"] = _device()

        proc = await asyncio.create_subprocess_exec(
            _mineru_bin(),
            "-p", str(pdf_path),
            "-o", str(out_dir),
            "-b", "pipeline",
            "-m", "auto",
            "-l", "en",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=env,
        )
        try:
            _, stderr = await asyncio.wait_for(
                proc.communicate(), timeout=PARSE_TIMEOUT_S
            )
        except TimeoutError:
            proc.kill()
            await proc.wait()
            raise HTTPException(
                status_code=504,
                detail=f"mineru timed out after {PARSE_TIMEOUT_S}s for {stem}",
            )

        if proc.returncode != 0:
            raise HTTPException(
                status_code=500,
                detail=f"mineru failed (exit {proc.returncode}):\n"
                       + stderr.decode("utf-8", errors="replace")[-2000:],
            )

        md_path = out_dir / stem / "auto" / f"{stem}.md"
        if not md_path.exists():
            fallback = list(out_dir.rglob(f"{stem}.md")) or list(out_dir.rglob("*.md"))
            if not fallback:
                raise HTTPException(
                    status_code=500,
                    detail=f"mineru produced no markdown for {stem}",
                )
            md_path = fallback[0]

        if not KEEP_DEBUG:
            _prune_debug_artifacts(md_path.parent)
        return _assemble_response(md_path)

    finally:
        shutil.rmtree(work_dir, ignore_errors=True)


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, log_level="info")
