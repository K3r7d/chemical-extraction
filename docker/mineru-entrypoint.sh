#!/usr/bin/env bash
# Download pipeline models on first run (idempotent — HF cache on named volume).
# Subsequent container starts skip straight to uvicorn since all files are cached.
set -euo pipefail

echo "[mineru-service] checking pipeline models..."
mineru-models-download -s huggingface -m pipeline

echo "[mineru-service] starting server..."
exec uvicorn server:app --host 0.0.0.0 --port 8000 --log-level info
