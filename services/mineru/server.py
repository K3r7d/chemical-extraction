"""MinerU HTTP wrapper.

Accepts a PDF upload, shells to the mineru 3.x CLI (same pattern as
MinerULocalClient), writes output to a shared volume, and returns the
parsed content as JSON.

Output root is shared with the orchestrator container via a bind-mounted
volume (both containers mount ./outputs at /outputs), so image_path values
in the response are valid absolute paths on both sides.

Outputs follow the canonical layout used by the HF dataset:
    <MINERU_OUTPUT_ROOT>/<N>/<stem>/auto/<stem>.md
where <N> is the paper-index folder under DATA_PAPERS_ROOT containing the
input PDF. Stems not found under DATA_PAPERS_ROOT fall back to
    <MINERU_OUTPUT_ROOT>/<stem>/auto/<stem>.md

Environment variables:
    MINERU_OUTPUT_ROOT  where parsed output lands (default /outputs/mineru)
    DATA_PAPERS_ROOT    paper-index source for resolving <N> (default data/papers)
    MINERU_DEVICE_MODE  cuda | cpu | auto-detected via torch
    MINERU_CACHE_ONLY   1 = serve cached results only, never invoke the CLI
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

OUTPUT_ROOT = Path(os.getenv("MINERU_OUTPUT_ROOT", "/outputs/mineru"))
# Used to resolve a PDF stem back to its paper index so outputs land in the
# canonical <root>/<N>/<stem>/auto/<stem>.md layout (matches the HF dataset).
# Stems not found under DATA_PAPERS_ROOT fall back to <root>/<stem>/auto/.
DATA_PAPERS_ROOT = Path(os.getenv("DATA_PAPERS_ROOT", "data/papers"))
PARSE_TIMEOUT_S = float(os.getenv("MINERU_PARSE_TIMEOUT_S", "600"))
# By default, prune MinerU's debug artifacts (origin/layout/span PDFs, model.json,
# middle.json — together ~35 MB/paper) after a successful parse. Set
# MINERU_KEEP_DEBUG=1 to retain them for troubleshooting.
KEEP_DEBUG = os.getenv("MINERU_KEEP_DEBUG", "0") == "1"
# Cache-only mode: return cached output if present, error otherwise. Never
# invoke the mineru CLI — keeps GPU free for vLLM and avoids downloading the
# ~5 GB of MinerU model weights. Use with scripts/pull_outputs.sh.
CACHE_ONLY = os.getenv("MINERU_CACHE_ONLY", "0") == "1"

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
    """Return the paper-index folder name (e.g. "7") that contains `<stem>.pdf`.

    Lets the server place fresh outputs at <root>/<N>/<stem>/ instead of the
    legacy flat <root>/<stem>/, so cached uploads and re-parses share one tree.
    """
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


@app.post("/parse")
async def parse(pdf: UploadFile = File(...)) -> dict:
    stem = Path(pdf.filename or "document").stem

    # Cache lookup: find <stem>.md anywhere under OUTPUT_ROOT. Handles both
    # the canonical <root>/<N>/<stem>/auto/<stem>.md layout and the legacy
    # flat <root>/<stem>/auto/<stem>.md path.
    cached = sorted(OUTPUT_ROOT.rglob(f"{stem}.md"))
    # Last-resort: very old caches used tmp-prefixed filenames under
    # <root>/<stem>/. Match any .md inside that legacy folder.
    if not cached:
        legacy_dir = OUTPUT_ROOT / stem
        if legacy_dir.is_dir():
            cached = sorted(legacy_dir.rglob("*.md"))
    if cached:
        return _assemble_response(cached[0])

    if CACHE_ONLY:
        raise HTTPException(
            status_code=404,
            detail=(
                f"cache miss for {stem!r} and MINERU_CACHE_ONLY=1. "
                f"Run scripts/pull_outputs.sh or unset MINERU_CACHE_ONLY."
            ),
        )

    idx = _resolve_paper_index(stem)
    out_dir = (OUTPUT_ROOT / idx) if idx else OUTPUT_ROOT
    out_dir.mkdir(parents=True, exist_ok=True)

    pdf_bytes = await pdf.read()

    # Stage the upload as <stem>.pdf so MinerU writes
    # <out_dir>/<stem>/auto/<stem>.md (rather than tmp<rand>.md from a
    # randomly-named tempfile).
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

        # MinerU 3.x writes <out_dir>/<stem>/auto/<stem>.md
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
