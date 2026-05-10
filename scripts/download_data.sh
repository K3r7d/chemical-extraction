#!/usr/bin/env bash
# Download and extract the paper dataset from Google Drive.
# Safe to re-run — exits early if data/papers/ already exists.
set -euo pipefail

GDRIVE_ID="1Z8VXF_O4iSa6ijTO3W3icnsfQxJgejgv"
ZIP="data.zip"

if [ -d "data/papers" ]; then
    echo "data/papers/ already exists — skipping download"
    exit 0
fi

command -v gdown >/dev/null 2>&1 || {
    echo "gdown not found — run: uv sync"
    exit 1
}

echo "downloading data.zip from Google Drive..."
gdown "$GDRIVE_ID" -O "$ZIP"

echo "extracting..."
unzip -q "$ZIP"
rm "$ZIP"

echo "done — $(find data/papers -name '*.pdf' | wc -l) PDFs ready in data/papers/"
