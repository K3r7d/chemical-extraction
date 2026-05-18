#!/usr/bin/env bash
# One-touch deploy: start all services and wait until the stack is ready.
#
# Usage:
#   bash scripts/deploy.sh            # Docker mode (default)
#   bash scripts/deploy.sh --local    # Local mode (no Docker, uv + background processes)
set -euo pipefail

cd "$(dirname "$0")/.."

MODE="docker"
MINERU_ONLY=0
for arg in "$@"; do
  case $arg in
    --local) MODE="local" ;;
    --mineru-only) MINERU_ONLY=1; MODE="local" ;;
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

    until curl -sf http://localhost:28080/health | python3 -c "
import json, sys
d = json.load(sys.stdin)
ok = all(d.get(k) for k in ['mineru', 'llm'])
print('  ' + ('✓ All services healthy' if ok else '✗ ' + str(d)))
sys.exit(0 if ok else 1)
" 2>/dev/null; do
        sleep 15
    done

    echo ""
    echo "=== Stack is ready ==="
    echo "  Orchestrator : http://localhost:28080"
    echo "  LLM API      : http://localhost:28000/v1"
    echo ""
    echo "  Run extractions:"
    echo "    bash scripts/extract_all.sh           # all papers"
    echo "    bash scripts/extract_one.sh 1         # single paper"
    exit 0
fi

# ── Local mode ────────────────────────────────────────────────────────────────
echo "=== Local mode: starting services without Docker ==="

# Pin uv to ./.venv on hosts (e.g. Vast.ai PyTorch templates) that pre-set
# VIRTUAL_ENV to a system Python that lacks our deps. Setup_local.sh does
# the same — keep them in sync.
unset VIRTUAL_ENV
export UV_PROJECT_ENVIRONMENT="${UV_PROJECT_ENVIRONMENT:-.venv}"

echo ""
echo "=== Downloading paper corpus (skips if already present) ==="
bash "$(dirname "$0")/download_data.sh"

LLM_MODEL="${LLM_MODEL_NAME:-Qwen/Qwen3.5-9B}"
GPU_COUNT=$(nvidia-smi --list-gpus 2>/dev/null | wc -l || echo "1")
# Cap vLLM VRAM so MinerU has room for its layout/OCR models (~4 GB headroom
# per card). 0.75 works on 16 GiB cards; override via VLLM_GPU_MEM_UTIL.
# If the bundled data zip already contains parsed mineru output for every PDF,
# MinerU never invokes the CLI and you can safely raise this to ~0.90.
VLLM_GPU_MEM_UTIL="${VLLM_GPU_MEM_UTIL:-0.75}"

mkdir -p logs

# Kill any stale processes from a previous local run.
for pidfile in /tmp/a2i2-*.pid; do
    [ -f "$pidfile" ] || continue
    pid=$(cat "$pidfile")
    kill "$pid" 2>/dev/null || true
    rm -f "$pidfile"
done

if [ "$MINERU_ONLY" = "1" ]; then
    echo ""
    echo "=== Skipping vLLM (--mineru-only) ==="
else
    echo ""
    echo "=== Starting vLLM (port 28000) ==="
    uv run python -m vllm.entrypoints.openai.api_server \
        --model "$LLM_MODEL" \
        --tensor-parallel-size "$GPU_COUNT" \
        --gpu-memory-utilization "$VLLM_GPU_MEM_UTIL" \
        --dtype bfloat16 \
        --max-model-len 131072 \
        --host 127.0.0.1 --port 28000 \
        > logs/llm.log 2>&1 &
    echo $! > /tmp/a2i2-llm.pid
fi

echo "=== Starting MinerU service (port 28010) ==="
# Device auto-detects (cuda when available). VRAM headroom is reserved by
# capping vLLM via VLLM_GPU_MEM_UTIL above. Override with MINERU_DEVICE_MODE=cpu
# only if the GPU truly has no room.
# Parsed output is written into data/papers/<N>/mineru/, so a pre-built data
# zip can ship cached mineru output alongside its PDFs.
DATA_PAPERS_ROOT="${DATA_PAPERS_ROOT:-data/papers}" \
PYTHONPATH=services/mineru \
uv run uvicorn server:app --host 127.0.0.1 --port 28010 \
    > logs/mineru.log 2>&1 &
echo $! > /tmp/a2i2-mineru.pid

if [ "$MINERU_ONLY" = "1" ]; then
    echo ""
    echo "=== Skipping orchestrator (--mineru-only) ==="
    echo ""
    echo "=== Waiting for MinerU to be ready ==="
    until curl -sf http://127.0.0.1:28010/health >/dev/null 2>&1; do
        sleep 2
    done
    echo "  ✓ MinerU ready at http://127.0.0.1:28010"
    echo ""
    echo "  Next: parse all papers (outputs land in data/papers/<N>/mineru/)"
    echo "    bash scripts/parse_all_local.sh"
    exit 0
fi

echo "=== Starting orchestrator (port 28080) ==="
MINERU_URL=http://127.0.0.1:28010 \
LLM_URL=http://127.0.0.1:28000/v1 \
LLM_MODEL_NAME="$LLM_MODEL" \
OUTPUT_DIR=outputs \
uv run uvicorn a2i2_extraction.api:app --host 127.0.0.1 --port 28080 \
    > logs/orchestrator.log 2>&1 &
echo $! > /tmp/a2i2-orchestrator.pid

echo ""
echo "=== Waiting for stack to be ready ==="
echo "  LLM model load can take 10-20 min on first run (downloading weights)."
echo "  Live log tail below — Ctrl+C is safe, services keep running in background."
echo ""

_tail_log() {
    local label="$1" file="$2"
    local line
    line=$(tail -1 "$file" 2>/dev/null | tr -d '\r' | sed 's/^[[:space:]]*//')
    [ -n "$line" ] && printf "  [%-12s] %s\n" "$label" "${line:0:100}"
}

_check_health() {
    curl -sf http://localhost:28080/health 2>/dev/null | python3 -c "
import json, sys
d = json.load(sys.stdin)
parts = []
for k in ['mineru', 'llm']:
    parts.append(('✓' if d.get(k) else '✗') + k)
print('  health: ' + '  '.join(parts))
sys.exit(0 if all(d.get(k) for k in ['mineru','llm']) else 1)
" 2>/dev/null
}

until _check_health; do
    echo "-- $(date '+%H:%M:%S') --"
    _tail_log "llm"        logs/llm.log
    _tail_log "mineru"     logs/mineru.log
    _tail_log "orchestrat" logs/orchestrator.log
    echo ""
    sleep 15
done

echo ""
echo "=== Stack is ready ==="
echo "  Orchestrator : http://localhost:28080"
echo "  LLM API      : http://localhost:28000/v1"
echo ""
echo "  Run extractions:"
echo "    bash scripts/extract_all.sh --local    # all papers"
echo "    bash scripts/extract_one.sh 1 --local  # single paper"
echo ""
echo "  Stop all local services:"
echo "    bash scripts/stop_local.sh"
