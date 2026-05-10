# CPU-only orchestrator service.
# Build: docker build -f docker/orchestrator.Dockerfile -t a2i2/orchestrator .
# Run:   exposed via docker compose (port 8080)

FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1

# Install uv via official image — single layer, no curl/sh.
COPY --from=ghcr.io/astral-sh/uv:0.11.8 /uv /usr/local/bin/uv

WORKDIR /app

# Install deps first (cache-friendly).
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project --no-dev

# Then code.
COPY src ./src
RUN uv sync --frozen --no-dev

EXPOSE 8080
CMD ["uv", "run", "uvicorn", "a2i2_extraction.api:app", "--host", "0.0.0.0", "--port", "8080"]
