"""FastAPI entrypoint."""

from __future__ import annotations

from pathlib import Path

import structlog
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .clients import MinerUHTTPClient, VLLMClient
from .clients.chemvlm import ChemVLMHTTPClient
from .clients.vision import VisionClient
from .config import get_settings
from .pipeline import Pipeline

log = structlog.get_logger(__name__)
app = FastAPI(title="a2i2-extraction", version="0.1.0")


class ExtractRequest(BaseModel):
    paper_dir: str


class ExtractResponse(BaseModel):
    paper_dir: str
    error_count: int
    warning_count: int
    output_path: str


def _build_pipeline() -> Pipeline:
    s = get_settings()
    return Pipeline(
        mineru=MinerUHTTPClient(s.mineru_url, timeout_s=s.llm_request_timeout_s),
        llm=VLLMClient(
            s.llm_url,
            model_name=s.llm_model_name,
            api_key=s.llm_api_key,
            timeout_s=s.llm_request_timeout_s,
            default_max_tokens=s.llm_max_tokens,
            default_temperature=s.llm_temperature,
        ),
        model_name=s.llm_model_name,
        output_dir=Path(s.output_dir),
        vision=VisionClient(s.vision_url),
        chemvlm=ChemVLMHTTPClient(s.chemvlm_url),
    )


@app.get("/health")
async def health() -> dict:
    s = get_settings()
    mineru_ok = await MinerUHTTPClient(s.mineru_url).health()
    llm_ok = await VLLMClient(
        s.llm_url, model_name=s.llm_model_name, api_key=s.llm_api_key
    ).health()
    vision_ok = await VisionClient(s.vision_url).health()
    chemvlm_ok = await ChemVLMHTTPClient(s.chemvlm_url).health()
    all_ok = mineru_ok and llm_ok and vision_ok and chemvlm_ok
    return {
        "status": "ok" if all_ok else "degraded",
        "mineru": mineru_ok,
        "llm": llm_ok,
        "vision": vision_ok,
        "chemvlm": chemvlm_ok,
    }


@app.post("/extract", response_model=ExtractResponse)
async def extract(req: ExtractRequest) -> ExtractResponse:
    paper_dir = Path(req.paper_dir)
    if not paper_dir.is_dir():
        raise HTTPException(404, f"paper_dir not found: {paper_dir}")
    pipeline = _build_pipeline()
    result = await pipeline.run(paper_dir)
    out = Path(get_settings().output_dir) / paper_dir.name / "extraction.json"
    return ExtractResponse(
        paper_dir=str(paper_dir),
        error_count=sum(1 for i in result.issues if i.severity.value == "error"),
        warning_count=sum(1 for i in result.issues if i.severity.value == "warning"),
        output_path=str(out),
    )
