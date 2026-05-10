"""Vision service: SigLIP 2 image triage + MolNexTR OCSR.

Both models are loaded once at startup and kept in memory.
All paths are absolute paths inside the shared /outputs volume.

Environment variables:
    VISION_TRIAGE_MODEL      SigLIP 2 HF model id (default: google/siglip2-so400m-patch14-384)
    VISION_OCSR_CHECKPOINT   local path to molnextr_best.pth (default: /cache/molnextr/molnextr_best.pth)
    VISION_DEVICE            cuda | cpu (default: auto-detected)
    VISION_BATCH_SIZE        images per forward pass for triage (default: 8)
"""

from __future__ import annotations

import os
from contextlib import asynccontextmanager
from pathlib import Path

import torch
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

TRIAGE_MODEL = os.getenv("VISION_TRIAGE_MODEL", "google/siglip2-so400m-patch14-384")
OCSR_CHECKPOINT = os.getenv("VISION_OCSR_CHECKPOINT", "/cache/molnextr/molnextr_best.pth")
DEVICE = os.getenv("VISION_DEVICE") or ("cuda" if torch.cuda.is_available() else "cpu")
BATCH_SIZE = int(os.getenv("VISION_BATCH_SIZE", "8"))

_triage = None
_ocsr = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global _triage, _ocsr

    # Import here so the module can be imported without GPU deps installed.
    from a2i2_extraction.vision.ocsr import MolNexTROCSR
    from a2i2_extraction.vision.triage import ImageTriage

    print(f"[vision] loading SigLIP 2 ({TRIAGE_MODEL}) on {DEVICE}...")
    _triage = ImageTriage(model_name=TRIAGE_MODEL, device=DEVICE, batch_size=BATCH_SIZE)
    _triage._load()
    print("[vision] SigLIP 2 ready.")

    print(f"[vision] loading MolNexTR ({OCSR_CHECKPOINT}) on {DEVICE}...")
    _ocsr = MolNexTROCSR(checkpoint=OCSR_CHECKPOINT, device=DEVICE)
    _ocsr._load()
    print("[vision] MolNexTR ready.")

    yield


app = FastAPI(title="vision-service", version="0.1.0", lifespan=lifespan)


# ------------------------------------------------------------------
# Request / response models
# ------------------------------------------------------------------

class TriageRequest(BaseModel):
    output_dir: str   # absolute path to MinerU auto/ dir on shared volume


class OCSRRequest(BaseModel):
    img_paths: list[str]   # absolute paths to kept image files on shared volume


# ------------------------------------------------------------------
# Endpoints
# ------------------------------------------------------------------

@app.get("/health")
async def health() -> dict:
    return {
        "status": "ok",
        "triage_ready": _triage is not None and _triage._model is not None,
        "ocsr_ready": _ocsr is not None and _ocsr._model is not None,
    }


@app.post("/triage")
async def triage(req: TriageRequest) -> dict:
    output_dir = Path(req.output_dir)
    if not output_dir.exists():
        raise HTTPException(status_code=400, detail=f"output_dir not found: {output_dir}")

    results = _triage.triage_document(output_dir)
    return {
        "results": [
            {
                "img_path": r.img_path,
                "page_idx": r.page_idx,
                "bbox": r.bbox,
                "image_class": r.image_class,
                "confidence": r.confidence,
                "keep": r.keep,
                "caption": r.caption,
            }
            for r in results
        ]
    }


@app.post("/ocsr")
async def ocsr(req: OCSRRequest) -> dict:
    if not req.img_paths:
        return {"results": []}

    missing = [p for p in req.img_paths if not Path(p).exists()]
    if missing:
        raise HTTPException(status_code=400, detail=f"images not found: {missing[:3]}")

    results = _ocsr.process_paths(req.img_paths)
    return {
        "results": [
            {
                "img_path": r.img_path,
                "smiles": r.smiles,
                "canonical_smiles": r.canonical_smiles,
                "formula": r.formula,
                "inchikey": r.inchikey,
                "valid": r.valid,
            }
            for r in results
        ]
    }


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8001, log_level="info")
