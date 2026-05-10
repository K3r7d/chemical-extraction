"""Unit tests for the Stage 5 panel-extraction prompt + response parser."""

from __future__ import annotations

from a2i2_extraction.prompts.vlm_panel import (
    build_panel_extraction_prompt,
    parse_panel_response,
)


class TestBuildPrompt:
    def test_minimal_prompt_has_instructions(self):
        prompt = build_panel_extraction_prompt()
        assert "JSON array" in prompt
        assert "compound_id" in prompt
        assert "smiles" in prompt

    def test_caption_included_when_provided(self):
        prompt = build_panel_extraction_prompt(caption="Figure 2. ROR1 precursors.")
        assert "Figure 2. ROR1 precursors." in prompt

    def test_context_text_included_when_provided(self):
        prompt = build_panel_extraction_prompt(
            context_text="R1 = H, R2 = OMe, R3 = DOTA."
        )
        assert "R1 = H" in prompt

    def test_caption_and_context_both_included(self):
        prompt = build_panel_extraction_prompt(
            caption="Figure 2.", context_text="R1 = H."
        )
        assert "Figure 2." in prompt
        assert "R1 = H." in prompt

    def test_empty_caption_skipped(self):
        prompt = build_panel_extraction_prompt(caption="")
        assert "Figure caption:" not in prompt


class TestParseResponse:
    def test_clean_json_array(self):
        raw = '[{"compound_id":"1","smiles":"CCO"},{"compound_id":"2","smiles":"CCN"}]'
        out = parse_panel_response(raw)
        assert out == [
            {"compound_id": "1", "smiles": "CCO"},
            {"compound_id": "2", "smiles": "CCN"},
        ]

    def test_strips_markdown_fence(self):
        raw = '```json\n[{"compound_id":"1","smiles":"CCO"}]\n```'
        assert parse_panel_response(raw) == [{"compound_id": "1", "smiles": "CCO"}]

    def test_tolerates_prose_around_array(self):
        raw = 'Sure, here are the compounds:\n[{"compound_id":"1a","smiles":"CCO"}]\nLet me know if you need more.'
        assert parse_panel_response(raw) == [{"compound_id": "1a", "smiles": "CCO"}]

    def test_empty_array_returns_empty(self):
        assert parse_panel_response("[]") == []

    def test_no_array_returns_empty(self):
        assert parse_panel_response("I cannot read this image.") == []

    def test_malformed_json_returns_empty(self):
        assert parse_panel_response("[{compound_id: 1, smiles: bad}]") == []

    def test_drops_entries_missing_fields(self):
        raw = '[{"compound_id":"1","smiles":"CCO"},{"compound_id":"2"},{"smiles":"CCN"}]'
        assert parse_panel_response(raw) == [{"compound_id": "1", "smiles": "CCO"}]

    def test_drops_non_string_values(self):
        raw = '[{"compound_id":1,"smiles":"CCO"},{"compound_id":"1","smiles":null}]'
        assert parse_panel_response(raw) == []

    def test_strips_whitespace_in_fields(self):
        raw = '[{"compound_id":" 1a ","smiles":" CCO "}]'
        assert parse_panel_response(raw) == [{"compound_id": "1a", "smiles": "CCO"}]
