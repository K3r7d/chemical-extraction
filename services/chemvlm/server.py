"""ChemVLM service: TinyChemVL panel-extraction endpoint.

Loads TinyChemVL once at startup, kept resident. Optional 4-bit NF4
quantisation via env so the same image works on a 5060 8 GB laptop and on
cluster nodes (override CHEMVLM_QUANTIZE=none for cluster deployment).

Environment variables:
    CHEMVLM_MODEL_DIR       local path to TinyChemVL weights
                            (default: /cache/chemvlm/TinyChemVL)
    CHEMVLM_QUANTIZE        "4bit" | "none" (default: 4bit)
    CHEMVLM_DEVICE          cuda | cpu (default: auto)
    CHEMVLM_MAX_NEW_TOKENS  generation cap (default: 512)
"""

from __future__ import annotations

import os
from contextlib import asynccontextmanager
from pathlib import Path

import torch
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

MODEL_DIR = os.getenv("CHEMVLM_MODEL_DIR", "/cache/chemvlm/TinyChemVL")
QUANTIZE = os.getenv("CHEMVLM_QUANTIZE", "4bit")
DEVICE = os.getenv("CHEMVLM_DEVICE") or ("cuda" if torch.cuda.is_available() else "cpu")
MAX_NEW_TOKENS = int(os.getenv("CHEMVLM_MAX_NEW_TOKENS", "512"))

_chemvlm = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global _chemvlm
    from a2i2_extraction.vision.chemvlm import TinyChemVL

    print(
        f"[chemvlm] loading TinyChemVL from {MODEL_DIR} "
        f"(quantize={QUANTIZE}, device={DEVICE})..."
    )
    _chemvlm = TinyChemVL(
        model_dir=MODEL_DIR,
        device=DEVICE,
        quantize=QUANTIZE,
        max_new_tokens=MAX_NEW_TOKENS,
    )
    _chemvlm._load()
    print("[chemvlm] TinyChemVL ready.")
    yield


app = FastAPI(title="chemvlm-service", version="0.1.0", lifespan=lifespan)


class PanelExtractRequest(BaseModel):
    img_path: str
    prompt: str


@app.get("/health")
async def health() -> dict:
    return {
        "status": "ok",
        "model_ready": _chemvlm is not None and _chemvlm._model is not None,
        "quantize": QUANTIZE,
        "device": DEVICE,
    }


@app.post("/panel_extract")
async def panel_extract(req: PanelExtractRequest) -> dict:
    if not Path(req.img_path).exists():
        raise HTTPException(status_code=400, detail=f"image not found: {req.img_path}")
    out = _chemvlm.generate(req.img_path, req.prompt)
    return {"response": out.response}


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8002, log_level="info")
