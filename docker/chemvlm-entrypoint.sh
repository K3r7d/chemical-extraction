#!/usr/bin/env bash
# Download TinyChemVL weights from ModelScope on first run (idempotent).
# Cached on the chemvlm-cache named volume between runs.
set -euo pipefail

MODEL_DIR="${CHEMVLM_MODEL_DIR:-/cache/chemvlm/TinyChemVL}"
MODEL_ID="${CHEMVLM_MODEL_ID:-Noct25/TinyChemVL}"

if [ ! -f "${MODEL_DIR}/config.json" ]; then
    echo "[chemvlm] downloading ${MODEL_ID} from ModelScope to ${MODEL_DIR}..."
    mkdir -p "$(dirname "${MODEL_DIR}")"
    python - <<EOF
from modelscope import snapshot_download
snapshot_download("${MODEL_ID}", local_dir="${MODEL_DIR}")
EOF
else
    echo "[chemvlm] model already cached at ${MODEL_DIR}."
fi

echo "[chemvlm] starting server..."
exec uvicorn server:app --host 0.0.0.0 --port 8002 --log-level info
