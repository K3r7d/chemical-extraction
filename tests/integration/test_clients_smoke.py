"""Live HTTP smoke tests against running services.

Marked @pytest.mark.docker so they're skipped on machines without the stack
running. Run on the cluster (or locally with `docker compose up`) with:

    uv run pytest -m docker

These verify the HTTP contract — they do NOT push real LLM inference
(per the user constraint: "test all tools except pushing to LLMs").
For LLM, we only hit /v1/models which is metadata-only.
"""

from __future__ import annotations

import os

import pytest

from a2i2_extraction.clients import MinerUHTTPClient, VLLMClient

pytestmark = pytest.mark.docker  # NOT also `integration` — those run without services


MINERU_URL = os.environ.get("MINERU_URL", "http://localhost:8001")
LLM_URL = os.environ.get("LLM_URL", "http://localhost:8000/v1")
LLM_MODEL = os.environ.get("LLM_MODEL_NAME", "Qwen/Qwen3.5-9B")


async def test_mineru_health() -> None:
    client = MinerUHTTPClient(MINERU_URL)
    assert await client.health(), f"MinerU not reachable at {MINERU_URL}"


async def test_vllm_models_endpoint() -> None:
    """Hits /v1/models — confirms vLLM is up without spending tokens."""
    client = VLLMClient(LLM_URL, model_name=LLM_MODEL)
    assert await client.health(), f"vLLM not reachable at {LLM_URL}"
