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
for svc in ['mineru', 'vision', 'chemvlm', 'llm']:
    mark = '✓' if d.get(svc) else '✗'
    print(f'  {mark} {svc}')
print(f\"  overall : {d['status']}\")
"

# ── Extraction results ────────────────────────────────────────────────────────
echo ""
echo "=== Extraction results ==="

total=0; ok=0; failed=0; pending=0

for paper_dir in data/papers/*/; do
    num=$(basename "$paper_dir")
    # Find the output dir for this paper (slug-named subfolder in outputs/)
    audit_file=$(find outputs -maxdepth 2 -name "audit.json" -path "*$(ls "$paper_dir"*.pdf 2>/dev/null | head -1 | xargs basename -s .pdf 2>/dev/null | cut -c1-20)*" 2>/dev/null | head -1)

    (( total++ ))
    if [ -z "$audit_file" ] || [ ! -f "$audit_file" ]; then
        echo "  [ pending ] paper $num"
        (( pending++ ))
    else
        status=$(python3 -c "import json; d=json.load(open('$audit_file')); print(d['extraction_status'])" 2>/dev/null)
        retries=$(python3 -c "import json; d=json.load(open('$audit_file')); print(d['retries'])" 2>/dev/null)
        if [ "$status" = "ok" ]; then
            echo "  [   ok   ] paper $num  (retries=$retries)"
            (( ok++ ))
        else
            echo "  [ FAILED ] paper $num  (retries=$retries)"
            (( failed++ ))
        fi
    fi
done

echo ""
echo "  Total   : $total"
echo "  OK      : $ok"
echo "  Failed  : $failed"
echo "  Pending : $pending"
