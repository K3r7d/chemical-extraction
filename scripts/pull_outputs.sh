#!/usr/bin/env bash
# Pull pre-computed MinerU outputs from a Hugging Face dataset.
# Use this on vast.ai to skip running MinerU entirely — server.py's cache
# lookup will serve these directly to the orchestrator, so no MinerU model
# weights are downloaded and no GPU is consumed by MinerU.
#
# Usage:
#   bash scripts/pull_outputs.sh                  # pull from repo root
#   bash scripts/pull_outputs.sh runs/2026-05-16  # pull a specific dated snapshot
#   HF_REPO=foo/bar bash scripts/pull_outputs.sh  # override target repo
#
# Auth (only needed for private repos): export HF_TOKEN before invoking, or
# cache a token via `uv run python -c "from huggingface_hub import login; login(token='hf_...')"`.
set -euo pipefail

cd "$(dirname "$0")/.."

HF_REPO="${HF_REPO:-Dyrekk/chem-extract}"
LOCAL_DIR="outputs/mineru"
SUBDIR="${1:-}"

mkdir -p "$LOCAL_DIR"

echo "=== Pulling $HF_REPO ${SUBDIR:+(subdir: $SUBDIR) }into $LOCAL_DIR/ ==="

HF_REPO="$HF_REPO" LOCAL_DIR="$LOCAL_DIR" SUBDIR="$SUBDIR" \
uv run python - <<'PY'
import os
from huggingface_hub import snapshot_download
subdir = os.environ.get("SUBDIR", "").strip()
kwargs = dict(
    repo_id=os.environ["HF_REPO"],
    repo_type="dataset",
    local_dir=os.environ["LOCAL_DIR"],
)
if subdir:
    kwargs["allow_patterns"] = [f"{subdir}/*", f"{subdir}/**"]
snapshot_download(**kwargs)
PY

count=$(find "$LOCAL_DIR" -name "*.md" 2>/dev/null | wc -l)
size=$(du -sh "$LOCAL_DIR" 2>/dev/null | cut -f1)
echo ""
echo "=== Done ==="
echo "  Pulled $count markdown files ($size total)"
echo "  MinerU server will now serve these from cache — no CLI invocation, no GPU."
