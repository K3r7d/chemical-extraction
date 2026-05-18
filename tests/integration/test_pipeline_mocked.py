"""End-to-end pipeline test with mocked MinerU + LLM clients.

Verifies the orchestrator wires the stages correctly: parse → prompt → LLM →
JSON parse → write. No network, no GPUs.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from a2i2_extraction.clients.base import ParsedDocument
from a2i2_extraction.pipeline import Pipeline

pytestmark = pytest.mark.integration


class _MockMinerU:
    def __init__(self, text: str) -> None:
        self._text = text
        self.calls = 0

    async def parse(self, pdf_path: Path) -> ParsedDocument:
        self.calls += 1
        return ParsedDocument(text=f"{self._text} ({pdf_path.name})", source_path=pdf_path)


class _MockLLM:
    def __init__(self, response: dict) -> None:
        self._response = response
        self.last_prompt: str | None = None

    async def complete(self, prompt: str, **_: object) -> str:
        self.last_prompt = prompt
        return json.dumps(self._response)


async def test_pipeline_writes_extraction(
    tmp_path: Path, sample_extraction: dict
) -> None:
    paper_dir = tmp_path / "paper_42"
    paper_dir.mkdir()
    (paper_dir / "main.pdf").write_bytes(b"%PDF-fake")
    (paper_dir / "study_si_001.pdf").write_bytes(b"%PDF-fake-si")

    mineru = _MockMinerU("parsed body")
    llm = _MockLLM(sample_extraction)
    output_dir = tmp_path / "outputs"

    pipeline = Pipeline(
        mineru=mineru,
        llm=llm,
        model_name="test/dummy",
        output_dir=output_dir,
    )

    await pipeline.run(paper_dir)

    assert mineru.calls == 2  # main + SI
    assert "=== SUPPORTING INFORMATION ===" in (llm.last_prompt or "")
    out_dir = output_dir / "paper_42"
    assert (out_dir / "extraction.json").exists()
    # Only extraction.json should be written — no audit, no raw_llm.
    assert sorted(p.name for p in out_dir.iterdir()) == ["extraction.json"]


async def test_pipeline_tolerates_markdown_fenced_json(
    tmp_path: Path, sample_extraction: dict
) -> None:
    paper_dir = tmp_path / "paper_1"
    paper_dir.mkdir()
    (paper_dir / "main.pdf").write_bytes(b"%PDF-fake")

    class _FencedLLM:
        async def complete(self, prompt: str, **_: object) -> str:
            return f"```json\n{json.dumps(sample_extraction)}\n```"

    pipeline = Pipeline(
        mineru=_MockMinerU("parsed"),
        llm=_FencedLLM(),
        model_name="test/dummy",
        output_dir=tmp_path / "outputs",
    )
    result = await pipeline.run(paper_dir)
    assert result.extraction["paper"]["title"] == sample_extraction["paper"]["title"]
