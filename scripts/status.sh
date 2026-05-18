#!/usr/bin/env bash
# Show stack health and a summary of all extraction results.
# Usage: bash scripts/status.sh
set -euo pipefail

cd "$(dirname "$0")/.."

ORCHESTRATOR="http://localhost:28080"

# ── Service health ────────────────────────────────────────────────────────────
echo "=== Service health ==="
health=$(curl -sf "$ORCHESTRATOR/health" 2>/dev/null) || {
    echo "  Orchestrator unreachable — is the stack running?"
    echo "  Run: docker compose ps"
    exit 1
}

echo "$health" | python3 -c "
import json, sys
d = json.load(sys.stdin)
for svc in ['mineru', 'llm']:
    mark = '✓' if d.get(svc) else '✗'
    print(f'  {mark} {svc}')
print(f\"  overall : {d['status']}\")
"

# ── Extraction results ────────────────────────────────────────────────────────
echo ""
echo "=== Extraction results ==="

total=0; ok=0; pending=0

for paper_dir in data/papers/*/; do
    num=$(basename "$paper_dir")
    extraction_file="outputs/$num/extraction.json"

    (( total++ ))
    if [ -f "$extraction_file" ]; then
        size=$(wc -c < "$extraction_file")
        echo "  [   ok   ] paper $num  (${size} bytes)"
        (( ok++ ))
    else
        echo "  [ pending ] paper $num"
        (( pending++ ))
    fi
done

echo ""
echo "  Total   : $total"
echo "  OK      : $ok"
echo "  Pending : $pending"
