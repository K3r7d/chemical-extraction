#!/usr/bin/env bash
# One-time setup for local / Vast.ai deployment (no Docker).
# Run this once before the first `bash scripts/deploy.sh --local`.
#
# What it does:
#   1. Creates the project venv, reusing system torch if present.
#   2. Installs vllm (not in pyproject.toml — GPU-specific).
set -euo pipefail

# A2I2_TEST_MODE=1  skips vllm (needs CUDA).
# Set automatically by scripts/test_setup_local.sh.
TEST_MODE="${A2I2_TEST_MODE:-0}"

cd "$(dirname "$0")/.."

# ── 1. Python venv ─────────────────────────────────────────────────────────────
echo "=== Setting up Python environment ==="

# vllm 0.20.2 (and its flashinfer/cuda-tile deps) only ships wheels for
# CPython 3.10–3.13. Newer hosts (e.g. some Vast.ai templates default to
# 3.14) must use an isolated 3.12 venv instead of reusing system Python.
SUPPORTED_PY="${A2I2_PINNED_PY:-3.12}"
SYS_PY_OK=0
if python3 -c "import sys; sys.exit(0 if (3,12) <= sys.version_info[:2] <= (3,13) else 1)" 2>/dev/null; then
    SYS_PY_OK=1
fi

if [ "$SYS_PY_OK" = "1" ] && python3 -c "import torch" 2>/dev/null; then
    sys_py=$(python3 -c "import sys; print('%d.%d'%sys.version_info[:2])")
    echo "  System Python $sys_py with torch — creating venv with --system-site-packages"
    [ -d .venv ] || uv venv --system-site-packages
    uv sync \
        --no-install-package torch \
        --no-install-package torchvision \
        --no-install-package torchaudio
else
    if [ "$SYS_PY_OK" != "1" ]; then
        sys_py=$(python3 -c "import sys; print('%d.%d'%sys.version_info[:2])" 2>/dev/null || echo "unknown")
        echo "  System Python $sys_py is outside vllm's supported range (3.12-3.13)."
        echo "  Creating isolated venv on Python $SUPPORTED_PY (torch will be downloaded)."
    else
        echo "  No system torch — creating isolated venv (torch will be installed)"
    fi
    [ -d .venv ] || uv venv --python "$SUPPORTED_PY"
    uv sync
fi

# ── 2. vllm ───────────────────────────────────────────────────────────────────
echo ""
echo "=== Installing vllm ==="
if [ "$TEST_MODE" = "1" ]; then
    echo "  TEST_MODE — skipping (requires CUDA)."
else
    # Pinned to match docker/vllm.Dockerfile (FROM vllm/vllm-openai:v0.20.2).
    uv pip install "vllm==0.20.2"
fi

# ── Done ──────────────────────────────────────────────────────────────────────
echo ""
echo "=== Setup complete ==="
echo ""
echo "  Start the stack:"
echo "    bash scripts/deploy.sh --local"
