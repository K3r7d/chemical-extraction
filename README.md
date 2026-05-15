# chemical-extraction

PDF to JSON extraction. Extracts compounds, synthesis pathways, reaction conditions, and characterisation data from journal papers and their supporting information.

## Architecture

Three services: `mineru` · `llm` · `orchestrator`.

```
PDF → MinerU (markdown + figures) → Qwen3.5-9B vision LLM → synthesis JSON → validator
```

Can run via Docker Compose or directly as local processes.

---

## Prerequisites

- NVIDIA GPU(s) with CUDA 12+
- `uv` (Python package manager)
- **Docker mode only:** Docker ≥ 24 with [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)

---

## Deploy

### Docker mode

```bash
git clone https://github.com/K3r7d/chemical-extraction.git && cd chemical-extraction

bash scripts/deploy.sh
```

Paper data is downloaded automatically on first run. Subsequent starts skip the download.

### Local mode (no Docker)

Use this when Docker is unavailable (e.g. Vast.ai, WSL, unprivileged containers).

```bash
git clone https://github.com/K3r7d/chemical-extraction.git && cd chemical-extraction

# First-time setup: creates venv, installs vllm.
# Safe to re-run — already-done steps are skipped.
bash scripts/setup_local.sh

bash scripts/deploy.sh --local
```

On Vast.ai PyTorch templates, `setup_local.sh` reuses the pre-installed torch automatically (no re-download). On a plain machine it installs torch from scratch.

Services start as background processes on localhost. Logs are written to `logs/`.

To stop all local services:

```bash
bash scripts/stop_local.sh
```

---

## Watching logs during startup

The LLM model download + load takes 10–20 min on first run. `deploy.sh` tails logs automatically, but you can also watch them directly:

```bash
# Follow a single service (most useful during startup)
tail -f logs/llm.log          # LLM — slowest, watch this first
tail -f logs/mineru.log
tail -f logs/orchestrator.log

# Follow all at once with labels
tail -f logs/llm.log logs/mineru.log logs/orchestrator.log

# Check stack health at any time
bash scripts/status.sh
```

**What to look for:**

| Service | Ready signal |
|---|---|
| LLM | `INFO: Uvicorn running on http://127.0.0.1:28000` |
| MinerU | `INFO: Uvicorn running on http://127.0.0.1:28010` |
| Orchestrator | `INFO: Uvicorn running on http://127.0.0.1:28080` |

Once all three are up, `bash scripts/status.sh` will show all green.

> **Ctrl+C is safe** — it exits the log tail but leaves all services running in the background.

---

## Extract papers

```bash
# Docker mode
bash scripts/extract_all.sh             # all papers
bash scripts/extract_one.sh 1           # single paper

# Local mode
bash scripts/extract_all.sh --local
bash scripts/extract_one.sh 1 --local

bash scripts/status.sh                  # health + results summary
```

Output written to `./outputs/<paper-slug>/extraction.json` and `audit.json`.

---

## Port assignments

Host-facing ports (what you connect to from outside):

| Service | Docker (host) | Local |
|---|---|---|
| LLM (vLLM) | 28000 | 28000 |
| MinerU | — (internal only) | 28010 |
| Orchestrator | 28080 | 28080 |

Docker inter-service communication uses container names on the internal bridge network (e.g. `http://mineru:8000`) — those internal ports are unchanged.

### GPU assignment

MinerU is lightweight and runs on GPU 0. The LLM service automatically uses all GPUs with tensor-parallel — no configuration needed.

---

## Local development

### Setup

```bash
bash scripts/setup_local.sh   # install deps (one-time)
make data                      # download paper corpus
make test                      # 52 unit + integration tests (no GPU, no network)
```

### Running a subset of services (Docker)

```bash
# Start only the services you need
docker compose up -d mineru llm

# Override the LLM model without editing the compose file
LLM_MODEL_NAME=Qwen/Qwen3.5-9B \
TENSOR_PARALLEL_SIZE=1 \
  docker compose up -d llm
```

### Overriding config (local mode)

All settings can be overridden via environment variables:

```bash
LLM_MODEL_NAME=Qwen/Qwen3.5-9B bash scripts/deploy.sh --local
```

---

## Output format

```
outputs/
  cleaned/                    # preprocessed markdown (headers, refs, noise stripped)
    <n>/<paper-slug>/auto/<slug>.md
  mineru/                     # raw MinerU markdown + extracted figure images
    <n>/<paper-slug>/auto/
      <slug>.md
      images/*.jpg
  <paper-slug>/               # extraction results
    extraction.json           # v3.4 schema output
    audit.json                # retries, extraction_status, validation issues
logs/                         # local mode service logs
  llm.log  mineru.log  orchestrator.log
```

### `extraction.json` top-level keys

| Key | Description |
|---|---|
| `extraction` | metadata: model, prompt version, date, status |
| `paper` | bibliographic info |
| `compounds` | list of compounds with id, name, formula, MS data, role |
| `synthesis` | list of pathways: target, steps, conditions, yields |

### `audit.json`

```json
{
  "retries": 0,
  "extraction_status": "ok",
  "issues": [
    {"code": "MS_ARITHMETIC", "severity": "warning", "message": "...", "path": "..."}
  ]
}
```

`extraction_status` is `"ok"` or `"failed_validation"` (errors remain after 2 retries).

---

## Running tests

```bash
make test                  # unit + integration (no GPU, no network required)
uv run pytest -m docker    # smoke tests against a running Docker stack
```

---

## Adding a new paper

Drop one or two PDFs into `data/papers/<n>/`:
- Main paper: any filename not containing `_si_` or `supporting`
- SI: filename must contain `_si_` or `supporting` (case-insensitive)

Then run:
```bash
bash scripts/extract_one.sh <n>           # Docker
bash scripts/extract_one.sh <n> --local   # Local
```
