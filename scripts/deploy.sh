#!/usr/bin/env bash
# One-touch deploy: start all services and wait until the stack is ready.
set -euo pipefail

cd "$(dirname "$0")/.."

# Preflight: verify Docker is accessible.
if ! docker info >/dev/null 2>&1; then
    echo "ERROR: Cannot connect to Docker daemon." >&2
    echo "  The deploy user must be in the 'docker' group before running this script." >&2
    echo "  On a new node, run this ONCE as an admin during provisioning:" >&2
    echo "    sudo usermod -aG docker <deploy-user>" >&2
    echo "  Then start a new session for the change to take effect." >&2
    exit 1
fi

echo "=== Downloading paper corpus (skips if already present) ==="
bash "$(dirname "$0")/download_data.sh"

echo ""
echo "=== Building and starting all services ==="
docker compose up -d --build

echo ""
echo "=== Waiting for stack to be ready ==="
echo "  (LLM model download + load can take several minutes on first run)"
echo "  Following orchestrator health..."

until curl -sf http://localhost:8080/health | python3 -c "
import json, sys
d = json.load(sys.stdin)
ok = all(d.get(k) for k in ['mineru', 'llm', 'vision', 'chemvlm'])
print('  ' + ('✓ All services healthy' if ok else '✗ ' + str(d)))
sys.exit(0 if ok else 1)
" 2>/dev/null; do
    sleep 15
done

echo ""
echo "=== Stack is ready ==="
echo "  Orchestrator : http://localhost:8080"
echo "  LLM API      : http://localhost:8000/v1"
echo ""
echo "  Run extractions:"
echo "    bash scripts/extract_all.sh       # all papers"
echo "    bash scripts/extract_one.sh 1     # single paper"
