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

# Force uv to use the project .venv even on hosts (e.g. Vast.ai PyTorch
# templates) that pre-set VIRTUAL_ENV to an incompatible system Python.
unset VIRTUAL_ENV
export UV_PROJECT_ENVIRONMENT="${UV_PROJECT_ENVIRONMENT:-.venv}"

HF_REPO="${HF_REPO:-Dyrekk/chem-extract}"
LOCAL_DIR="outputs/mineru"
SUBDIR="${1:-}"

mkdir -p "$LOCAL_DIR"

echo "=== Pulling $HF_REPO ${SUBDIR:+(subdir: $SUBDIR) }into $LOCAL_DIR/ ==="

HF_REPO="$HF_REPO" LOCAL_DIR="$LOCAL_DIR" SUBDIR="$SUBDIR" \
uv run python - <<'PY'
import os
import time
from huggingface_hub import snapshot_download
from huggingface_hub.errors import HfHubHTTPError

subdir = os.environ.get("SUBDIR", "").strip()
kwargs = dict(
    repo_id=os.environ["HF_REPO"],
    repo_type="dataset",
    local_dir=os.environ["LOCAL_DIR"],
    # Free-tier HF accounts are capped at 1000 API requests / 5 min and
    # Xet-backed repos refresh a token per file. 4 workers keeps the burst
    # under the budget for a 3k-file repo.
    max_workers=int(os.environ.get("HF_DOWNLOAD_WORKERS", "4")),
)
if subdir:
    kwargs["allow_patterns"] = [f"{subdir}/*", f"{subdir}/**"]

# snapshot_download is resumable: already-downloaded blobs in the HF cache
# are reused, so we just need to retry the whole call past a 429.
last_err = None
for attempt in range(1, 6):
    try:
        snapshot_download(**kwargs)
        break
    except HfHubHTTPError as e:
        last_err = e
        if e.response is None or e.response.status_code != 429:
            raise
        wait = 60 * attempt
        print(f"[pull] HF 429; sleeping {wait}s before retry {attempt}/5")
        time.sleep(wait)
else:
    raise last_err
PY

count=$(find "$LOCAL_DIR" -name "*.md" 2>/dev/null | wc -l)
size=$(du -sh "$LOCAL_DIR" 2>/dev/null | cut -f1)
echo ""
echo "=== Done ==="
echo "  Pulled $count markdown files ($size total)"
echo "  MinerU server will now serve these from cache — no CLI invocation, no GPU."
