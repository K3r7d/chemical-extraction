# MinerU 3.x as an HTTP service.
# python:3.12-slim base — CUDA device access is provided at runtime by
# nvidia-container-toolkit (runtime: nvidia in compose); torch bundles its
# own CUDA libraries so no nvidia/cuda base image is required.

FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HF_HOME=/cache/huggingface \
    MINERU_OUTPUT_ROOT=/outputs/mineru

# Runtime libs required by OpenCV / MinerU layout models.
RUN apt-get update && apt-get install -y --no-install-recommends \
        libgl1 libglib2.0-0 libsm6 libxrender1 libxext6 \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv — same version pinned as local dev for reproducibility.
COPY --from=ghcr.io/astral-sh/uv:0.11.8 /uv /usr/local/bin/uv

WORKDIR /app

# Install mineru + server dependencies.
# Separate from the orchestrator's pyproject so this image stays lean.
RUN uv pip install --system \
        "mineru[pipeline]>=3.1.6" \
        fastapi \
        "uvicorn[standard]"

COPY services/mineru/server.py ./server.py
COPY docker/mineru-entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["./entrypoint.sh"]
