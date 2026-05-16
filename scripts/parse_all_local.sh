#!/usr/bin/env bash
# Send every PDF in data/papers/ through the local MinerU service.
# Outputs land in outputs/mineru/<pdf_stem>/ with debug artifacts pruned.
# Cache hits are returned instantly, so re-running is safe and resumable.
#
# Prereq: MinerU service running on port 28010 (start it via
#   bash scripts/deploy.sh --mineru-only
set -euo pipefail

cd "$(dirname "$0")/.."

MINERU_URL="${MINERU_URL:-http://127.0.0.1:28010}"

if ! curl -sf "$MINERU_URL/health" >/dev/null 2>&1; then
    echo "ERROR: MinerU is not reachable at $MINERU_URL" >&2
    echo "  Start it with: bash scripts/deploy.sh --mineru-only" >&2
    exit 1
fi

mapfile -t pdfs < <(find data/papers -type f -name "*.pdf" | sort)
if [ "${#pdfs[@]}" -eq 0 ]; then
    echo "ERROR: no PDFs found under data/papers/" >&2
    exit 1
fi

echo "=== Parsing ${#pdfs[@]} PDFs through $MINERU_URL ==="

i=0
for pdf in "${pdfs[@]}"; do
    i=$((i + 1))
    stem=$(basename "$pdf" .pdf)
    printf "[%2d/%d] %s ... " "$i" "${#pdfs[@]}" "$stem"

    status=$(curl -sS -o /tmp/mineru_resp.json -w "%{http_code}" \
        -F "pdf=@$pdf" "$MINERU_URL/parse" || echo "000")

    if [ "$status" = "200" ]; then
        echo "ok"
    else
        echo "FAILED (HTTP $status)"
        head -c 500 /tmp/mineru_resp.json
        echo ""
    fi
done

echo ""
echo "=== Done ==="
size=$(du -sh outputs/mineru 2>/dev/null | cut -f1)
echo "  outputs/mineru: $size"
echo ""
echo "  Next: push to HF"
echo "    bash scripts/push_outputs.sh"
