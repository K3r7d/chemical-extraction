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

# If the system Python already has torch (e.g. Vast.ai PyTorch template),
# create the venv with system-site-packages so we don't re-download ~3 GB.
if python3 -c "import torch" 2>/dev/null; then
    echo "  System torch found — creating venv with --system-site-packages"
    [ -d .venv ] || uv venv --system-site-packages
    uv sync \
        --no-install-package torch \
        --no-install-package torchvision \
        --no-install-package torchaudio
else
    echo "  No system torch — creating isolated venv (torch will be installed)"
    [ -d .venv ] || uv venv
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
