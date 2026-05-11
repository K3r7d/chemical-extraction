# chemical-extraction

PDF to JSON extraction. Extracts compounds, synthesis pathways, reaction conditions, and characterisation data from journal papers and their supporting information.

## Architecture

<img src="asset/architecture.png" width="480" alt="Pipeline architecture">

Five Docker services: `mineru` (8000) · `vision` (8001) · `chemvlm` (8002) · `llm` (8000/v1) · `orchestrator` (8080).

---

## Prerequisites

- Docker ≥ 24 with [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)
- NVIDIA GPU(s) with CUDA 12+
- HuggingFace account with access to Qwen models
- `uv` (Python package manager) — only needed for local dev/testing

---

## Deploy

```bash
git clone https://github.com/K3r7d/chemical-extraction.git && cd chemical-extraction

bash scripts/deploy.sh
```

Paper data is downloaded automatically on first run (from Google Drive). Subsequent starts skip the download.

### Extract papers

```bash
bash scripts/extract_all.sh          # all papers in data/papers/
bash scripts/extract_one.sh 1        # single paper by number
bash scripts/status.sh               # health + results summary
```

Output written to `./outputs/<paper-slug>/extraction.json` and `audit.json`.

### GPU assignment

MinerU, Vision (SigLIP 2 + MolNexTR), and ChemVLM (TinyChemVL 4-bit) are lightweight and share a single GPU (default: GPU 0). The LLM service automatically uses all remaining GPUs and sets tensor-parallel size to match — no configuration needed on a standard cluster node.

---

## Local development

### Setup

```bash
uv sync          # install Python deps into .venv
make data        # download paper corpus
make models      # download MinerU pipeline weights (~1.2 GB, one-time)
make test        # 100 unit + integration tests (no GPU, no network)
```

### Running a subset of services

Each service can be started independently. The orchestrator only requires `mineru`, `vision`, and `llm` to be healthy before it starts; `chemvlm` is optional and the pipeline degrades gracefully if it is unavailable.

```bash
# Start only the services you need
docker compose up -d mineru vision llm

# Override the LLM model without editing the compose file
LLM_MODEL_NAME=Qwen/Qwen2.5-7B-Instruct \
TENSOR_PARALLEL_SIZE=1 \
  docker compose up -d llm
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
```

### `extraction.json` top-level keys

| Key | Description |
|---|---|
| `extraction` | metadata: model, prompt version, date, status |
| `paper` | bibliographic info |
| `compounds` | list of compounds with id, name, SMILES, formula, role |
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
uv run pytest -m slow      # real SigLIP 2 triage on paper 1 (requires MinerU output)
```

---

## Adding a new paper

Drop one or two PDFs into `data/papers/<n>/`:
- Main paper: any filename not containing `_si_` or `supporting`
- SI: filename must contain `_si_` or `supporting` (case-insensitive)

Then POST to `/extract` with `"paper_dir": "/data/papers/<n>"`.
