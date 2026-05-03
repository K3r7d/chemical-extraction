# Implementation

### Prompt engineering limitation

After testing with multiple papers, prompt engineering alone hit a ceiling — the LLM still cannot reliably map compounds to their synthesis steps without structured document context. MinerU 2.5 was used to parse PDFs into Markdown, but at this point I only got that far; the downstream LLM pipeline is not yet wired up.

### Ground truth plan

Instead of waiting for the full pipeline, I decided to use Claude directly as an extraction engine on the raw paper and treat the output as a synthesis ground truth. The plan is to run the pipeline later and compare its output against this Claude-generated reference.

### Prompt v3.3 → v3.4

Running Claude Opus 4.7 with prompt v3.3 on the ROR1 paper produced an extraction that was noticeably longer and more redundant than the v3.2 output from Sonnet 4.6. The main culprits were:
- `description` fields on every compound running 30–50 words each
- A very long `extractor_notes` block that wrote out the model's reasoning
- Explicit `null` values repeated across all fields for every compound

This came primarily from the model (Opus is more verbose by nature) but the prompt also gave no word-count constraints. Prompt v3.4 was written to fix this — adding Rule 1A (≤15 words on description), Rule 9A (compress iterative SPPS into one step), and Rule 11B (notes carry new info only).

### Claude extractions

Claude extraction outputs are stored in `ground_truth/dataset_1/extraction.json`.


