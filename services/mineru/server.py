"""MinerU HTTP wrapper.

Accepts a PDF upload, shells to the mineru 3.x CLI (same pattern as
MinerULocalClient), writes output to a shared volume, and returns the
parsed content as JSON.

Output root is shared with the orchestrator container via a bind-mounted
volume (both containers mount ./outputs at /outputs), so image_path values
in the response are valid absolute paths on both sides.

Environment variables:
    MINERU_OUTPUT_ROOT  where parsed output lands (default /outputs/mineru)
    MINERU_DEVICE_MODE  cuda | cpu | auto-detected via torch
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
PARSE_TIMEOUT_S = float(os.getenv("MINERU_PARSE_TIMEOUT_S", "600"))

app = FastAPI(title="mineru-service", version="0.1.0")


def _mineru_bin() -> str:
    candidate = Path(sys.executable).parent / "mineru"
    if candidate.exists():
        return str(candidate)
    found = shutil.which("mineru")
    if found:
        return found
    raise RuntimeError("mineru CLI not found")


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


@app.post("/parse")
async def parse(pdf: UploadFile = File(...)) -> dict:
    stem = Path(pdf.filename or "document").stem
    out_dir = OUTPUT_ROOT / stem
    out_dir.mkdir(parents=True, exist_ok=True)

    pdf_bytes = await pdf.read()

    # Write to a named temp file — mineru CLI requires a real .pdf path.
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp.write(pdf_bytes)
        tmp_path = Path(tmp.name)

    try:
        env = os.environ.copy()
        env["MINERU_DEVICE_MODE"] = _device()

        proc = await asyncio.create_subprocess_exec(
            _mineru_bin(),
            "-p", str(tmp_path),
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

        md_candidates = list(out_dir.rglob("*.md"))
        if not md_candidates:
            raise HTTPException(
                status_code=500,
                detail=f"mineru produced no markdown for {stem}",
            )

        # MinerU 3.x layout: <out_dir>/<stem>/auto/<stem>.md
        md_path = md_candidates[0]
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
            "output_dir": str(md_path.parent),   # auto/ dir inside the container
        }

    finally:
        tmp_path.unlink(missing_ok=True)


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, log_level="info")
