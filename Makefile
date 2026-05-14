.PHONY: data models test lint deploy deploy-local stop-local

data:
	bash scripts/download_data.sh

models:
	mineru-models-download -s huggingface -m pipeline

test:
	uv run pytest

lint:
	uv run ruff check src tests

deploy:
	bash scripts/deploy.sh

deploy-local:
	bash scripts/deploy.sh --local

stop-local:
	bash scripts/stop_local.sh
