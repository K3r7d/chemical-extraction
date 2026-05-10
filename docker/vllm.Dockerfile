# vLLM serving Qwen 3.6-72B (or any HF-id model passed via env).
# Uses the official vLLM OpenAI-compatible image.
#
# Model name and tensor-parallel size are env-driven so multi-size A/B testing
# (per architecture_v2.md GPU budget section) is a compose env swap, not a
# code change.

FROM vllm/vllm-openai:v0.20.2

ENV LLM_MODEL_NAME="Qwen/Qwen3.6-72B-Instruct" \
    TENSOR_PARALLEL_SIZE=auto \
    LLM_DTYPE=auto \
    LLM_MAX_MODEL_LEN=32768 \
    HF_HOME=/cache/huggingface \
    VLLM_ALLOW_LONG_MAX_MODEL_LEN=1

COPY docker/vllm-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
