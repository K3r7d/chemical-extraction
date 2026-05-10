"""End-to-end pipeline test with mocked MinerU + LLM clients.

Verifies the orchestrator wires the stages correctly: parse → prompt → LLM →
JSON parse → validate → write. No network, no GPUs.
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


async def test_pipeline_writes_extraction_and_audit(
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

    result = await pipeline.run(paper_dir)

    assert mineru.calls == 2  # main + SI
    assert "=== SUPPORTING INFORMATION ===" in (llm.last_prompt or "")
    assert not result.has_errors
    assert (output_dir / "paper_42" / "extraction.json").exists()
    assert (output_dir / "paper_42" / "audit.json").exists()


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
    assert not result.has_errors


async def test_pipeline_surfaces_validation_errors(
    tmp_path: Path, sample_extraction: dict
) -> None:
    sample_extraction["compounds"][0]["id"] = "INVALID"
    paper_dir = tmp_path / "paper_1"
    paper_dir.mkdir()
    (paper_dir / "main.pdf").write_bytes(b"%PDF-fake")

    pipeline = Pipeline(
        mineru=_MockMinerU("parsed"),
        llm=_MockLLM(sample_extraction),
        model_name="test/dummy",
        output_dir=tmp_path / "outputs",
    )
    result = await pipeline.run(paper_dir)
    assert result.has_errors


async def test_pipeline_retries_on_validation_error(
    tmp_path: Path, sample_extraction: dict
) -> None:
    """LLM returns invalid JSON on first call, valid on second — pipeline retries."""
    paper_dir = tmp_path / "paper_retry"
    paper_dir.mkdir()
    (paper_dir / "main.pdf").write_bytes(b"%PDF-fake")

    good_response = json.dumps(sample_extraction)
    bad_response = json.dumps({**sample_extraction, "compounds": [{
        **sample_extraction["compounds"][0], "id": "INVALID"
    }]})

    calls: list[str] = []

    class _FlakeyLLM:
        async def complete(self, prompt: str, **_: object) -> str:
            calls.append(prompt)
            # First call returns invalid compound id; second call returns valid.
            return bad_response if len(calls) == 1 else good_response

    pipeline = Pipeline(
        mineru=_MockMinerU("parsed"),
        llm=_FlakeyLLM(),
        model_name="test/dummy",
        output_dir=tmp_path / "outputs",
    )
    result = await pipeline.run(paper_dir)

    assert len(calls) == 2, "should have retried exactly once"
    assert result.retries == 1
    assert not result.has_errors
    # Retry prompt must include the previous bad output and violation info.
    assert "=== YOUR PREVIOUS OUTPUT ===" in calls[1]
    assert "VIOLATIONS" in calls[1]


async def test_pipeline_marks_failed_validation_after_max_retries(
    tmp_path: Path, sample_extraction: dict
) -> None:
    """After _MAX_RETRIES exhausted, audit.json records failed_validation."""
    paper_dir = tmp_path / "paper_fail"
    paper_dir.mkdir()
    (paper_dir / "main.pdf").write_bytes(b"%PDF-fake")

    always_bad = {**sample_extraction, "compounds": [{
        **sample_extraction["compounds"][0], "id": "INVALID"
    }]}

    pipeline = Pipeline(
        mineru=_MockMinerU("parsed"),
        llm=_MockLLM(always_bad),
        model_name="test/dummy",
        output_dir=tmp_path / "outputs",
    )
    result = await pipeline.run(paper_dir)

    assert result.has_errors
    assert result.retries == 2  # _MAX_RETRIES

    audit = json.loads(
        (tmp_path / "outputs" / "paper_fail" / "audit.json").read_text()
    )
    assert audit["extraction_status"] == "failed_validation"
    assert audit["retries"] == 2
