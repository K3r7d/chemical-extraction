#!/usr/bin/env bash
# One-time setup for local / Vast.ai deployment (no Docker).
# Run this once before the first `bash scripts/deploy.sh --local`.
#
# What it does:
#   1. Creates the project venv, reusing system torch if present.
#   2. Installs vllm, MolNexTR, and ChemVLM deps not in pyproject.toml.
#   3. Downloads the MolNexTR checkpoint (~400 MB, Zenodo).
#   4. Downloads TinyChemVL weights (~8 GB, ModelScope).
set -euo pipefail

cd "$(dirname "$0")/.."

MOLNEXTR_CHECKPOINT="${VISION_OCSR_CHECKPOINT:-${HOME}/.cache/molnextr/molnextr_best.pth}"
CHEMVLM_MODEL_DIR="${CHEMVLM_MODEL_DIR:-${HOME}/.cache/chemvlm/TinyChemVL}"
CHEMVLM_MODEL_ID="${CHEMVLM_MODEL_ID:-Noct25/TinyChemVL}"
MOLNEXTR_ZENODO_URL="https://zenodo.org/records/13304899/files/molnextr_best.pth"

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
# Pinned to match docker/vllm.Dockerfile (FROM vllm/vllm-openai:v0.20.2).
uv pip install "vllm==0.20.2"

# ── 3. MolNexTR ───────────────────────────────────────────────────────────────
echo ""
echo "=== Installing MolNexTR ==="
# MolNexTR pins pyonmttok==1.37.1 which has no cp312 wheel (only up to cp311).
# Install without deps first, then pull in a newer pyonmttok that has cp312 wheels.
uv pip install --no-deps "git+https://github.com/CYF2000127/MolNexTR"
uv pip install "pyonmttok>=1.37.1" albumentations timm opencv-python-headless

# ── 4. ChemVLM inference deps ─────────────────────────────────────────────────
echo ""
echo "=== Installing ChemVLM deps ==="
# hf_transfer: Rust-based parallel downloader — saturates high-bandwidth links.
# modelscope kept as fallback in case HF is unavailable.
uv pip install \
    hf_transfer \
    modelscope \
    "accelerate>=0.30" \
    "bitsandbytes>=0.43" \
    einops \
    timm \
    sentencepiece

# ── 5. MolNexTR checkpoint ────────────────────────────────────────────────────
echo ""
echo "=== Downloading MolNexTR checkpoint ==="
if [ -f "$MOLNEXTR_CHECKPOINT" ]; then
    echo "  Already cached at ${MOLNEXTR_CHECKPOINT} — skipping."
else
    mkdir -p "$(dirname "$MOLNEXTR_CHECKPOINT")"
    echo "  Downloading to ${MOLNEXTR_CHECKPOINT} (~400 MB)..."
    curl -fL --retry 3 --progress-bar \
        -o "$MOLNEXTR_CHECKPOINT" \
        "$MOLNEXTR_ZENODO_URL"
    echo "  Done."
fi

# ── 6. TinyChemVL weights ─────────────────────────────────────────────────────
echo ""
echo "=== Downloading TinyChemVL weights ==="
if [ -f "${CHEMVLM_MODEL_DIR}/config.json" ]; then
    echo "  Already cached at ${CHEMVLM_MODEL_DIR} — skipping."
else
    mkdir -p "${CHEMVLM_MODEL_DIR}"
    echo "  Downloading ${CHEMVLM_MODEL_ID} to ${CHEMVLM_MODEL_DIR} (~8 GB)..."
    # hf_transfer uses parallel chunked downloads — much faster than ModelScope
    # on high-bandwidth nodes. Falls back to ModelScope if HF download fails.
    if HF_HUB_ENABLE_HF_TRANSFER=1 uv run python - <<EOF 2>/dev/null
from huggingface_hub import snapshot_download
snapshot_download("${CHEMVLM_MODEL_ID}", local_dir="${CHEMVLM_MODEL_DIR}", local_dir_use_symlinks=False)
EOF
        echo "  Done (via HuggingFace)."
    else
        echo "  HuggingFace failed, falling back to ModelScope..."
        uv run python - <<EOF
from modelscope import snapshot_download
snapshot_download("${CHEMVLM_MODEL_ID}", local_dir="${CHEMVLM_MODEL_DIR}")
EOF
        echo "  Done (via ModelScope)."
    fi
fi

# ── Done ──────────────────────────────────────────────────────────────────────
echo ""
echo "=== Setup complete ==="
echo "  MolNexTR checkpoint : ${MOLNEXTR_CHECKPOINT}"
echo "  TinyChemVL weights  : ${CHEMVLM_MODEL_DIR}"
echo ""
echo "  Start the stack:"
echo "    VISION_OCSR_CHECKPOINT=${MOLNEXTR_CHECKPOINT} bash scripts/deploy.sh --local"
