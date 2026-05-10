#!/usr/bin/env bash
# Start vLLM, auto-detecting tensor-parallel size from visible GPUs.
# Override by setting TENSOR_PARALLEL_SIZE explicitly in the environment.
set -euo pipefail

if [ "${TENSOR_PARALLEL_SIZE:-auto}" = "auto" ]; then
    GPU_COUNT=$(nvidia-smi --list-gpus 2>/dev/null | wc -l)
    TENSOR_PARALLEL_SIZE=${GPU_COUNT:-1}
    echo "[llm] auto-detected ${TENSOR_PARALLEL_SIZE} GPU(s) for tensor parallel"
else
    echo "[llm] using TENSOR_PARALLEL_SIZE=${TENSOR_PARALLEL_SIZE} (explicit)"
fi

exec python3 -m vllm.entrypoints.openai.api_server \
    --model "${LLM_MODEL_NAME}" \
    --tensor-parallel-size "${TENSOR_PARALLEL_SIZE}" \
    --dtype "${LLM_DTYPE}" \
    --max-model-len "${LLM_MAX_MODEL_LEN}" \
    --host 0.0.0.0 --port 8000
