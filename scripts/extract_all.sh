#!/usr/bin/env bash
# Extract all papers in data/papers/ sequentially.
# Usage: bash scripts/extract_all.sh
set -euo pipefail

cd "$(dirname "$0")/.."

ORCHESTRATOR="http://localhost:8080"
PAPERS_DIR="data/papers"

if [ ! -d "$PAPERS_DIR" ]; then
    echo "ERROR: $PAPERS_DIR not found. Run bash scripts/deploy.sh first."
    exit 1
fi

papers=( "$PAPERS_DIR"/*/ )
total=${#papers[@]}
done=0
failed=0

echo "=== Extracting $total papers ==="
echo ""

for paper_path in "${papers[@]}"; do
    num=$(basename "$paper_path")
    container_path="/data/papers/$num"

    printf "[%2d/%d] paper %-3s ... " "$((done + failed + 1))" "$total" "$num"

    response=$(curl -sf -X POST "$ORCHESTRATOR/extract" \
        -H "Content-Type: application/json" \
        -d "{\"paper_dir\": \"$container_path\"}" 2>&1) || {
        echo "FAILED (connection error)"
        (( failed++ ))
        continue
    }

    errors=$(echo "$response" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('error_count',0))" 2>/dev/null)
    warnings=$(echo "$response" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('warning_count',0))" 2>/dev/null)

    if [ "${errors:-1}" -eq 0 ]; then
        echo "ok  (warnings=$warnings)"
        (( done++ ))
    else
        echo "FAILED  (errors=$errors warnings=$warnings)"
        (( failed++ ))
    fi
done

echo ""
echo "=== Done: $done ok, $failed failed out of $total papers ==="
echo "  Results: outputs/<paper-slug>/extraction.json"
echo "  Run bash scripts/status.sh for a full summary."
