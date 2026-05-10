# Vision service: SigLIP 2 (triage) + MolNexTR (OCSR).
# GPU access provided at runtime by nvidia-container-toolkit.
# Python 3.10 used for MolNexTR dep compatibility (albumentations, timm, etc.).

FROM python:3.10-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HF_HOME=/cache/huggingface \
    PYTHONPATH=/app/src

# Runtime libs for OpenCV / image processing.
RUN apt-get update && apt-get install -y --no-install-recommends \
        libgl1 libglib2.0-0 libsm6 libxrender1 libxext6 curl git \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:0.11.8 /uv /usr/local/bin/uv

WORKDIR /app

# Install vision deps. MolNexTR pulls in torch, torchvision, timm, albumentations.
# Installed independently of pyproject.toml to keep this image self-contained.
RUN uv pip install --system \
        torch \
        torchvision \
        "transformers>=4.49.0" \
        pillow \
        rdkit \
        fastapi \
        "uvicorn[standard]" \
        pydantic \
        "git+https://github.com/CYF2000127/MolNexTR"

# Copy the package source so the service can import a2i2_extraction.vision.
# PYTHONPATH=/app/src is set in ENV above — no install needed (no compiled extensions).
COPY src ./src

COPY services/vision/server.py ./server.py
COPY docker/vision-entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

EXPOSE 8001
ENTRYPOINT ["./entrypoint.sh"]
