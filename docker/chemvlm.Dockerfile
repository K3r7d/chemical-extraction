# ChemVLM service: TinyChemVL (InternVL2.5-4B chemistry-tuned).
# Default deployment is 4-bit NF4 (bitsandbytes) for 8 GB consumer GPUs.
# Override CHEMVLM_QUANTIZE=none on cluster nodes for fp16/bf16.

FROM python:3.10-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HF_HOME=/cache/huggingface \
    MODELSCOPE_CACHE=/cache/modelscope \
    PYTHONPATH=/app/src

RUN apt-get update && apt-get install -y --no-install-recommends \
        libgl1 libglib2.0-0 libsm6 libxrender1 libxext6 curl git \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:0.11.8 /uv /usr/local/bin/uv

WORKDIR /app

# Inference deps. bitsandbytes for 4-bit NF4. einops/timm/sentencepiece are
# InternVL transitive deps. modelscope is the official weight host.
RUN uv pip install --system \
        torch \
        torchvision \
        "transformers>=4.49.0" \
        "accelerate>=0.30" \
        "bitsandbytes>=0.43" \
        einops \
        timm \
        sentencepiece \
        pillow \
        modelscope \
        fastapi \
        "uvicorn[standard]" \
        pydantic

COPY src ./src
COPY services/chemvlm/server.py ./server.py
COPY docker/chemvlm-entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

EXPOSE 8002
ENTRYPOINT ["./entrypoint.sh"]
