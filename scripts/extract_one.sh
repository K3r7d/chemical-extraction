#!/usr/bin/env bash
# Extract a single paper by number.
# Usage:
#   bash scripts/extract_one.sh <paper_number>           # Docker mode
#   bash scripts/extract_one.sh <paper_number> --local   # Local mode
set -euo pipefail

cd "$(dirname "$0")/.."

ORCHESTRATOR="http://localhost:8080"
NUM=""
MODE="docker"

for arg in "$@"; do
  case $arg in
    --local) MODE="local" ;;
    *) [ -z "$NUM" ] && NUM="$arg" ;;
  esac
done

if [ -z "$NUM" ]; then
    echo "Usage: bash scripts/extract_one.sh <paper_number> [--local]"
    echo "Available: $(ls data/papers/ 2>/dev/null | tr '\n' ' ')"
    exit 1
fi

if [ ! -d "data/papers/$NUM" ]; then
    echo "ERROR: data/papers/$NUM not found."
    exit 1
fi

if [ "$MODE" = "local" ]; then
    PAPER_PATH="$(pwd)/data/papers/$NUM"
else
    PAPER_PATH="/data/papers/$NUM"
fi

echo "=== Extracting paper $NUM (mode=$MODE) ==="
response=$(curl -sf -X POST "$ORCHESTRATOR/extract" \
    -H "Content-Type: application/json" \
    -d "{\"paper_dir\": \"$PAPER_PATH\"}")

echo "$response" | python3 -c "
import json, sys
d = json.load(sys.stdin)
print(f\"  status  : {'ok' if d['error_count'] == 0 else 'FAILED'}\")
print(f\"  errors  : {d['error_count']}\")
print(f\"  warnings: {d['warning_count']}\")
print(f\"  output  : {d['output_path']}\")
"

# Show audit
audit=$(echo "$response" | python3 -c "
import json, sys
d = json.load(sys.stdin)
p = d['output_path'].replace('extraction.json', 'audit.json').replace('/outputs', 'outputs')
print(p)
" 2>/dev/null)

if [ -f "$audit" ]; then
    echo ""
    echo "  audit.json:"
    python3 -c "
import json
d = json.load(open('$audit'))
print(f\"    extraction_status : {d['extraction_status']}\")
print(f\"    retries           : {d['retries']}\")
for i in d.get('issues', [])[:5]:
    print(f\"    [{i['severity']}] {i['code']}: {i['message'][:70]}\")
"
fi
