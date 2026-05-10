"""Unit tests for Stage 5 panel-extraction orchestrator."""

from __future__ import annotations

from pathlib import Path

import pytest

from a2i2_extraction.vision.panel_extract import (
    CompoundExtraction,
    extract_panels,
)


class FakeChemVLMClient:
    def __init__(self, responses: dict[str, str]) -> None:
        self.responses = responses
        self.calls: list[tuple[str, str]] = []

    async def panel_extract(self, *, img_path: str, prompt: str) -> str:
        self.calls.append((img_path, prompt))
        return self.responses.get(img_path, "[]")


@pytest.mark.asyncio
async def test_skips_dropped_images():
    triage = [
        {"img_path": "images/a.jpg", "image_class": "structure_panel", "keep": False, "page_idx": 0},
    ]
    client = FakeChemVLMClient({})
    out = await extract_panels(triage, output_dir=Path("/x"), client=client)
    assert out == []
    assert client.calls == []


@pytest.mark.asyncio
async def test_skips_single_structure():
    """single_structure goes through OCSR, not VLM."""
    triage = [
        {"img_path": "images/a.jpg", "image_class": "single_structure", "keep": True, "page_idx": 0},
    ]
    client = FakeChemVLMClient({"/x/images/a.jpg": '[{"compound_id":"1","smiles":"CCO"}]'})
    out = await extract_panels(triage, output_dir=Path("/x"), client=client)
    assert out == []
    assert client.calls == []


@pytest.mark.asyncio
async def test_extracts_structure_panel():
    triage = [
        {
            "img_path": "images/p.jpg",
            "image_class": "structure_panel",
            "keep": True,
            "page_idx": 2,
            "caption": "Figure 2.",
        },
    ]
    client = FakeChemVLMClient({
        "/x/images/p.jpg": '[{"compound_id":"1","smiles":"CCO"},{"compound_id":"2","smiles":"CCN"}]'
    })
    out = await extract_panels(triage, output_dir=Path("/x"), client=client)
    assert out == [
        CompoundExtraction(img_path="/x/images/p.jpg", compound_id="1", smiles="CCO"),
        CompoundExtraction(img_path="/x/images/p.jpg", compound_id="2", smiles="CCN"),
    ]
    assert len(client.calls) == 1
    assert "Figure 2." in client.calls[0][1]


@pytest.mark.asyncio
async def test_extracts_reaction_scheme():
    triage = [
        {"img_path": "images/r.jpg", "image_class": "reaction_scheme", "keep": True, "page_idx": 1},
    ]
    client = FakeChemVLMClient({"/x/images/r.jpg": '[{"compound_id":"3","smiles":"O=C(C)O"}]'})
    out = await extract_panels(triage, output_dir=Path("/x"), client=client)
    assert len(out) == 1
    assert out[0].compound_id == "3"


@pytest.mark.asyncio
async def test_page_text_threaded_into_prompt():
    triage = [
        {"img_path": "images/p.jpg", "image_class": "structure_panel", "keep": True, "page_idx": 2},
    ]
    client = FakeChemVLMClient({"/x/images/p.jpg": "[]"})
    await extract_panels(
        triage,
        output_dir=Path("/x"),
        client=client,
        page_text={2: "R1 = H. R2 = OMe."},
    )
    assert "R1 = H. R2 = OMe." in client.calls[0][1]


@pytest.mark.asyncio
async def test_handles_unparseable_response():
    triage = [
        {"img_path": "images/p.jpg", "image_class": "structure_panel", "keep": True, "page_idx": 0},
    ]
    client = FakeChemVLMClient({"/x/images/p.jpg": "I cannot read this."})
    out = await extract_panels(triage, output_dir=Path("/x"), client=client)
    assert out == []


@pytest.mark.asyncio
async def test_processes_panels_in_order():
    triage = [
        {"img_path": "images/a.jpg", "image_class": "structure_panel", "keep": True, "page_idx": 0},
        {"img_path": "images/b.jpg", "image_class": "biology", "keep": False, "page_idx": 0},
        {"img_path": "images/c.jpg", "image_class": "reaction_scheme", "keep": True, "page_idx": 1},
    ]
    client = FakeChemVLMClient({
        "/x/images/a.jpg": '[{"compound_id":"1","smiles":"C"}]',
        "/x/images/c.jpg": '[{"compound_id":"2","smiles":"CC"}]',
    })
    out = await extract_panels(triage, output_dir=Path("/x"), client=client)
    assert [c.compound_id for c in out] == ["1", "2"]
    assert [path for path, _ in client.calls] == ["/x/images/a.jpg", "/x/images/c.jpg"]
