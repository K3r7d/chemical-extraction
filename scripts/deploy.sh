#!/usr/bin/env bash
# One-touch deploy: start all services and wait until the stack is ready.
#
# Usage:
#   bash scripts/deploy.sh            # Docker mode (default)
#   bash scripts/deploy.sh --local    # Local mode (no Docker, uv + background processes)
set -euo pipefail

cd "$(dirname "$0")/.."

MODE="docker"
for arg in "$@"; do
  case $arg in
    --local) MODE="local" ;;
  esac
done

# ── Docker mode ───────────────────────────────────────────────────────────────
if [ "$MODE" = "docker" ]; then
    if ! docker info >/dev/null 2>&1; then
        echo "ERROR: Cannot connect to Docker daemon." >&2
        echo "  The deploy user must be in the 'docker' group before running this script." >&2
        echo "  On a new node, run this ONCE as an admin during provisioning:" >&2
        echo "    sudo usermod -aG docker <deploy-user>" >&2
        echo "  Then start a new session for the change to take effect." >&2
        echo "" >&2
        echo "  No Docker? Run local mode instead:" >&2
        echo "    bash scripts/deploy.sh --local" >&2
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
    echo "    bash scripts/extract_all.sh           # all papers"
    echo "    bash scripts/extract_one.sh 1         # single paper"
    exit 0
fi

# ── Local mode ────────────────────────────────────────────────────────────────
echo "=== Local mode: starting services without Docker ==="

echo ""
echo "=== Downloading paper corpus (skips if already present) ==="
bash "$(dirname "$0")/download_data.sh"

LLM_MODEL="${LLM_MODEL_NAME:-Qwen/Qwen3.5-9B}"
GPU_COUNT=$(nvidia-smi --list-gpus 2>/dev/null | wc -l || echo "1")

mkdir -p logs

# Kill any stale processes from a previous local run.
for pidfile in /tmp/a2i2-*.pid; do
    [ -f "$pidfile" ] || continue
    pid=$(cat "$pidfile")
    kill "$pid" 2>/dev/null || true
    rm -f "$pidfile"
done

echo ""
echo "=== Starting vLLM (port 8000) ==="
uv run python -m vllm.entrypoints.openai.api_server \
    --model "$LLM_MODEL" \
    --tensor-parallel-size "$GPU_COUNT" \
    --dtype auto \
    --max-model-len 65536 \
    --host 127.0.0.1 --port 8000 \
    > logs/llm.log 2>&1 &
echo $! > /tmp/a2i2-llm.pid

echo "=== Starting MinerU service (port 8010) ==="
MINERU_OUTPUT_ROOT=outputs/mineru \
PYTHONPATH=services/mineru \
uv run uvicorn server:app --host 127.0.0.1 --port 8010 \
    > logs/mineru.log 2>&1 &
echo $! > /tmp/a2i2-mineru.pid

echo "=== Starting vision service (port 8001) ==="
PYTHONPATH=src:services/vision \
uv run uvicorn server:app --host 127.0.0.1 --port 8001 \
    > logs/vision.log 2>&1 &
echo $! > /tmp/a2i2-vision.pid

echo "=== Starting ChemVLM service (port 8002) ==="
CHEMVLM_MODEL_DIR="${CHEMVLM_MODEL_DIR:-${HOME}/.cache/chemvlm/TinyChemVL}" \
CHEMVLM_MODEL_ID="${CHEMVLM_MODEL_ID:-Noct25/TinyChemVL}" \
PYTHONPATH=services/chemvlm \
uv run uvicorn server:app --host 127.0.0.1 --port 8002 \
    > logs/chemvlm.log 2>&1 &
echo $! > /tmp/a2i2-chemvlm.pid

echo "=== Starting orchestrator (port 8080) ==="
MINERU_URL=http://127.0.0.1:8010 \
LLM_URL=http://127.0.0.1:8000/v1 \
LLM_MODEL_NAME="$LLM_MODEL" \
VISION_URL=http://127.0.0.1:8001 \
CHEMVLM_URL=http://127.0.0.1:8002 \
OUTPUT_DIR=outputs \
uv run uvicorn a2i2_extraction.api:app --host 127.0.0.1 --port 8080 \
    > logs/orchestrator.log 2>&1 &
echo $! > /tmp/a2i2-orchestrator.pid

echo ""
echo "=== Waiting for stack to be ready ==="
echo "  (LLM model load can take several minutes on first run)"
echo "  Logs: logs/{llm,mineru,vision,chemvlm,orchestrator}.log"
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
echo "    bash scripts/extract_all.sh --local    # all papers"
echo "    bash scripts/extract_one.sh 1 --local  # single paper"
echo ""
echo "  Stop all local services:"
echo "    bash scripts/stop_local.sh"
