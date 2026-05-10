#!/usr/bin/env bash
# Download vision models on first run (idempotent — cached on named volumes).
# SigLIP 2 SO400M: ~1.9 GB   MolNexTR checkpoint: ~400 MB
set -euo pipefail

TRIAGE_MODEL="${VISION_TRIAGE_MODEL:-google/siglip2-so400m-patch14-384}"
OCSR_CHECKPOINT="${VISION_OCSR_CHECKPOINT:-/cache/molnextr/molnextr_best.pth}"
MOLNEXTR_ZENODO_URL="https://zenodo.org/records/13304899/files/molnextr_best.pth"

echo "[vision] pre-fetching ${TRIAGE_MODEL}..."
python - <<EOF
from transformers import AutoModel, AutoProcessor
AutoProcessor.from_pretrained("${TRIAGE_MODEL}")
AutoModel.from_pretrained("${TRIAGE_MODEL}")
EOF

if [ ! -f "${OCSR_CHECKPOINT}" ]; then
    echo "[vision] downloading MolNexTR checkpoint to ${OCSR_CHECKPOINT}..."
    mkdir -p "$(dirname "${OCSR_CHECKPOINT}")"
    curl -fL --retry 3 -o "${OCSR_CHECKPOINT}" "${MOLNEXTR_ZENODO_URL}"
else
    echo "[vision] MolNexTR checkpoint already cached at ${OCSR_CHECKPOINT}."
fi

echo "[vision] models ready. starting server..."
exec uvicorn server:app --host 0.0.0.0 --port 8001 --log-level info
