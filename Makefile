.PHONY: data models test lint

data:
	bash scripts/download_data.sh

models:
	mineru-models-download -s huggingface -m pipeline

test:
	uv run pytest

lint:
	uv run ruff check src tests
