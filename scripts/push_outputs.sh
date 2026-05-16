#!/usr/bin/env bash
# Push outputs/mineru to a Hugging Face dataset repo.
# Usage:
#   bash scripts/push_outputs.sh                  # upload to repo root
#   bash scripts/push_outputs.sh --dated          # upload under runs/<YYYY-MM-DD>/
#   HF_REPO=foo/bar bash scripts/push_outputs.sh  # override target repo
#
# Auth: either run `uv run python -c "from huggingface_hub import login; login(token='hf_...')"`
# once to cache a token, or export HF_TOKEN before invoking this script.
set -euo pipefail

cd "$(dirname "$0")/.."

# Force uv to use the project .venv even on hosts (e.g. Vast.ai PyTorch
# templates) that pre-set VIRTUAL_ENV to an incompatible system Python.
unset VIRTUAL_ENV
export UV_PROJECT_ENVIRONMENT="${UV_PROJECT_ENVIRONMENT:-.venv}"

HF_REPO="${HF_REPO:-Dyrekk/chem-extract}"
LOCAL_DIR="outputs/mineru"
PATH_IN_REPO="."

for arg in "$@"; do
  case $arg in
    --dated) PATH_IN_REPO="runs/$(date +%Y-%m-%d)" ;;
  esac
done

if [ ! -d "$LOCAL_DIR" ] || [ -z "$(ls -A "$LOCAL_DIR" 2>/dev/null)" ]; then
    echo "ERROR: $LOCAL_DIR is empty or missing — nothing to upload." >&2
    exit 1
fi

size=$(du -sh "$LOCAL_DIR" | cut -f1)
echo "=== Uploading $LOCAL_DIR ($size) to $HF_REPO at '$PATH_IN_REPO' ==="

HF_REPO="$HF_REPO" LOCAL_DIR="$LOCAL_DIR" PATH_IN_REPO="$PATH_IN_REPO" \
uv run python - <<'PY'
import os
from huggingface_hub import upload_folder
upload_folder(
    folder_path=os.environ["LOCAL_DIR"],
    repo_id=os.environ["HF_REPO"],
    repo_type="dataset",
    path_in_repo=os.environ["PATH_IN_REPO"],
    commit_message=f"Upload {os.environ['LOCAL_DIR']} -> {os.environ['PATH_IN_REPO']}",
)
PY

echo ""
echo "=== Done ==="
echo "  View at: https://huggingface.co/datasets/$HF_REPO"
