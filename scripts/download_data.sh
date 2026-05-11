#!/usr/bin/env bash
# Download and extract the paper corpus from Google Drive.
# Safe to re-run — exits early if data/papers/ already exists.
# Works both locally (with gdown installed) and inside Docker (auto-installs gdown).
set -euo pipefail

GDRIVE_ID="1Z8VXF_O4iSa6ijTO3W3icnsfQxJgejgv"

if [ -d "data/papers" ]; then
    echo "[data-init] data/papers/ already present — skipping."
    exit 0
fi

if ! command -v gdown >/dev/null 2>&1; then
    echo "[data-init] installing gdown..."
    pip install -q --disable-pip-version-check gdown
fi

echo "[data-init] downloading paper corpus from Google Drive..."
gdown "$GDRIVE_ID" -O /tmp/corpus.zip

echo "[data-init] extracting..."
python3 -c "import zipfile; zipfile.ZipFile('/tmp/corpus.zip').extractall('.')"
rm /tmp/corpus.zip

echo "[data-init] done — $(find data/papers -name '*.pdf' | wc -l) PDFs ready."
