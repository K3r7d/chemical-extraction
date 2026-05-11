# vLLM serving Qwen 3.6 35B-A3B (or any HF-id model passed via env).
# Uses the official vLLM OpenAI-compatible image.
#
# Model name and tensor-parallel size are env-driven so multi-size A/B testing
# is a compose env swap, not a code change.

FROM vllm/vllm-openai:v0.20.2

ENV LLM_MODEL_NAME="Qwen/Qwen3.5-9B" \
    TENSOR_PARALLEL_SIZE=auto \
    LLM_DTYPE=auto \
    LLM_MAX_MODEL_LEN=65536 \
    HF_HOME=/cache/huggingface \
    VLLM_ALLOW_LONG_MAX_MODEL_LEN=1

COPY docker/vllm-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
