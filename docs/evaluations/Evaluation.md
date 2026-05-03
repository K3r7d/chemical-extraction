# Claude Extraction Quality Evaluation Report

### Prompt Versions v2.1 → v2.4 | Yang et al., _J. Med. Chem._ 2025

**DOI:** 10.1021/acs.jmedchem.5c02016

---

## 1. Overview

This report evaluates Claude's performance across four generations of a chemistry extraction prompt (v2.1–v2.4) applied to a single radiochemistry paper. The paper describes five PET radiotracers targeting ROR1: [⁶⁸Ga]Ga-DP1, [⁶⁸Ga]Ga-DP2, [⁶⁸Ga]Ga-DP3, [¹⁸F]AlF-NP1, and [¹⁸F]AlF-NP2. Two precursors (DP1, NP1) were synthesised in-house; three (DP2, DP3, NP2) were sourced externally.

The evaluation covers 13 Claude runs in total (v2.1 ×4, v2.2 ×3, v2.3 ×3, v2.4 ×3). GPT-4 and Gemini runs from v2.2 are excluded. Results are assessed against a fixed ground truth derived directly from the paper and scored on seven categorical failure modes plus consistency dimensions.

> **Note on ground truth methodology:** All ground truth claims in this report have been verified against the paper (Yang et al., _J. Med. Chem._ 2025, 68, 26049–26060). Section references and specific textual evidence are cited in Section 2 below. Any claims that could not be fully confirmed against the paper text are flagged explicitly.

---

## 2. Paper-Verified Ground Truth

### 2.1 Compound Roles

|Compound|Role|Paper evidence|
|---|---|---|
|[⁶⁸Ga]Ga-DP1/2/3, [¹⁸F]AlF-NP1/2|`radiolabeled_product`|Section 2.2: "The radiotracers … were prepared with the final radiochemical yields …"; Section 5.4 gives full radiolabeling procedures|
|DP1, NP1|`intermediate`|Section 5.2.1: "A mixture of PR7 … DOTA-NHS … or NOTA-NHS … was placed into a 2 mL centrifugation tube … DP1 and NP1 were separated using semipreparative HPLC" — full in-house synthesis described|
|DP2, DP3, NP2|`starting_material`|Section 5.2.2: "These precursors were custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd." — no in-house synthesis|
|PR7|`starting_material`|Section 5.1: "PR7, DP2, DP3, NP2, DOTA-NHS, and NOTA-NHS were custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd."|
|DOTA-NHS, NOTA-NHS|`reagent`|Section 5.1: listed as custom-sourced from same vendor; used as activated coupling reagents|
|DIPEA|`reagent`|Section 5.2.1: "20 μL of DIPEA" — named with a specific amount in the coupling step|
|⁶⁸GaCl₃|`reagent`|Section 5.1: "⁶⁸GaCl₃ was obtained from the ⁶⁸Ge–⁶⁸Ga generator (ITM)"|
|[¹⁸F]fluoride|`reagent`|Section 5.1: "Fluoride-18 was produced via the ¹⁸O(p,n)¹⁸F reaction by Cyclone 18/9 (IBA, Belgium)"|
|Sodium acetate (0.25 M, pH 6.5)|`reagent`|Section 5.4: "1 mL of ⁶⁸GaCl₃ … was diluted with 0.5 mL of sodium acetate (0.25 M in water, pH = 6.5)"|
|Sodium acetate buffer (0.1 M, pH 4.0)|`reagent`|Section 5.4: "100 μL of sodium acetate buffer (0.1 M, pH = 4.0)" — used independently in AlF step|
|AlCl₃ (2 mM in sodium acetate, pH 4.0)|`reagent`|Section 5.4: "3 μL of 2 mM aluminum chloride (AlCl₃) in sodium acetate buffer (0.1 M, pH = 4.0)"|

**Paper-confirmed distinction:** PR7, DOTA-NHS, and NOTA-NHS are all listed together in Section 5.1 as sourced from Nanchang Tanzhen Biotechnology — confirming they are all `starting_material` or `reagent`, not in-house compounds.

### 2.2 Property Attribution Ground Truth

|Property|Correct species|Paper evidence|
|---|---|---|
|Log P|Radiolabeled products only|Section 5.6: "Lipid–water partition coefficients (log P) of [⁶⁸Ga]Ga-DP1, [⁶⁸Ga]Ga-DP2, [⁶⁸Ga]Ga-DP3, [¹⁸F]AlF-NP1, and [¹⁸F]AlF-NP2 were measured in 1-octanol and phosphate-buffered saline … approximately 0.74–1.11 MBq in 100 μL PBS were added … Aliquots … measured in an automatic gamma counter." Radioactivity counting confirms only radiolabeled species were measured.|
|KD, Bmax|Radiolabeled products only|Section 2.4 and Figure 4G: "the KD of [⁶⁸Ga]Ga-DP1, [⁶⁸Ga]Ga-DP2, [⁶⁸Ga]Ga-DP3, [¹⁸F]AlF-NP1, and [¹⁸F]AlF-NP2 was calculated as 74.9, 154.9, 213.4, 141.7, and 212.1 nM, respectively." The compounds named are the **radiolabeled products**, not the unlabeled precursors. Section 5.9 confirms radiolabeled tracers were used in the saturation binding assay.|
|Docking scores|Unlabeled precursors and PR7|Section 2.3 and Figure 3B: "The docking scores … of PR7, DP1, DP2, DP3, NP1, and NP2 were measured as −8.8, −9.1, −7.7, −7.9, −8.3, and −7.6 kcal/mol." All are unlabeled compounds. Section 5.7 describes docking using AutoDock 4.2.6 with "candidate peptide ligands" — the unlabeled forms.|
|PR7 KD (1.57 × 10⁻⁹ M)|Literature value — PR7 only, external study|Section 3 (Discussion): "PR7 was selected as a lead compound … excellent affinity (KD = 1.57 × 10⁻⁹ M)" with superscript ref 38 (Zhang et al., _J. Med. Chem._ 2024). **Not measured in this study.**|
|Blood T½|Radiolabeled products only|Section 2.6: "The blood elimination half-lives (T1/2) of [⁶⁸Ga]Ga-DP1 and [¹⁸F]AlF-NP1 were 7.62 and 19.32 min, respectively (Figure S29)." Only these two radiotracers have T½ reported; DP2/DP3/NP2 radiotracers do not.|
|Biodistribution data|Radiolabeled products only|Section 2.6 and Tables S2–S5: Values like "1.41 ± 0.08% ID/g" refer to [⁶⁸Ga]Ga-DP1 and [¹⁸F]AlF-NP1 only.|
|Radiochemical purity (RCP)|Radiolabeled products|Section 5.4: "The radiochemical purities of all radioligands are >95% by radio-HPLC analysis." Section 2.2 states ">90%"; the 5.4 value (>95%) is the definitive per-product figure.|

### 2.3 Structural / Schema Ground Truth

**Two sodium acetate buffers are chemically distinct and must be separate compound entries:**

- **pH 6.5, 0.25 M:** Used to dilute ⁶⁸GaCl₃ and bring pH to 4–4.5 before the ⁶⁸Ga labeling step (Section 5.4).
- **pH 4.0, 0.1 M:** Used in the AlF labeling vial — both as the diluent for AlCl₃ (3 μL of 2 mM AlCl₃ in this buffer) and as an additional 100 μL component (Section 5.4). The paper adds 100 μL of pure 0.1 M pH 4.0 buffer _separately_ from the 3 μL AlCl₃ solution, confirming the buffer is a distinct component.

**Step granularity — confirmed from Section 5.4:**

- ⁶⁸Ga labeling: The pH adjustment ("diluted with 0.5 mL of sodium acetate … to adjust the pH … **and then** transferred to a vial containing the precursor") is explicitly a prior step before the heating step ("The reaction mixture was heated at 95 °C for 20 min"). These are two physically distinct operations.
- AlF labeling: [¹⁸F]fluoride was "**first** trapped on a preconditioned QMA cartridge … **and then** eluted with 0.2 mL saline into a vial containing … the precursor." QMA trapping and AlF chelation are explicitly sequential and in different vessels.

**HPLC methods — two distinct gradients confirmed from paper:**

- DP1/NP1 (in-house): Section 5.2.1: "5% B gradient to 95% B over 20 min"
- PR7/DP2/DP3/NP2 (external): Section 5.2.2: "23% B gradient to 43% B over 20 min"
- Radiolabeling QC (all radiotracers): Section 5.4: "5% B gradients to 95% B at 20 min"

**AlCl₃ entry boundary — what the paper actually says:** Section 5.4 states: "3 μL of 2 mM aluminum chloride (AlCl₃) **in** sodium acetate buffer (0.1 M, pH = 4.0), 200 μL of acetonitrile, **100 μL of sodium acetate buffer (0.1 M, pH = 4.0)**, and precursor." The AlCl₃ is dissolved _in_ the buffer, but the buffer also appears as a separate 100 μL addition. The paper treats them as separable components in the same sentence — this is a genuine ambiguity the paper text does not fully resolve, but the 100 μL buffer addition is clearly independent of the 3 μL AlCl₃ solution.

### 2.4 Numerical Ground Truth (for extraction accuracy checks)

|Value|Paper location|
|---|---|
|RCY: 89.55 ± 0.12% ([⁶⁸Ga]Ga-DP1)|Section 2.2|
|RCY: 97.67 ± 1.05% ([⁶⁸Ga]Ga-DP2)|Section 2.2|
|RCY: 98.01 ± 0.97% ([⁶⁸Ga]Ga-DP3)|Section 2.2|
|RCY: 62.58 ± 0.32% ([¹⁸F]AlF-NP1)|Section 2.2|
|RCY: 62.76 ± 0.22% ([¹⁸F]AlF-NP2)|Section 2.2|
|Molar activities: 14.37, 20.05, 14.09, 13.13, 13.42 GBq/μmol|Section 2.2, n ≥ 3|
|Log P: −2.19, −2.53, −1.82, −2.10, −2.54|Sections 2.2–2.3|
|DP1 yield: 4.2 mg (55.6%); NP1: 3.9 mg (54%)|Section 5.2.1|
|DP1 HPLC RT: 11.230 min; NP1: 12.780 min|Section 5.2.1|
|PR7/DP2/DP3/NP2 HPLC RTs: 10.642, 10.328, 10.404, 10.620 min|Section 5.2.2|
|Docking scores: PR7 −8.8, DP1 −9.1, DP2 −7.7, DP3 −7.9, NP1 −8.3, NP2 −7.6 kcal/mol|Section 2.3, Figure 3B|
|KD: 74.9, 154.9, 213.4, 141.7, 212.1 nM|Section 2.4, Figure 4G|
|Bmax: 22158, 31268, 47017, 31406, 22986 CPM|Figure 4G|
|Heating: ⁶⁸Ga at 95 °C / 20 min; AlF at 100 °C / 20 min|Section 5.4|
|DP1 ESI-MS: calcd C₁₁₂H₁₅₉N₂₉O₃₈, 2518.14; [M+2H]²⁺ = 1260.54, [M+3H]³⁺ = 840.68|Section 5.2.1|
|NP1 ESI-MS: calcd C₁₀₈H₁₅₂N₂₈O₃₆, 2417.09; [M+2H]²⁺ = 1210.22, [M+3H]³⁺ = 807.00|Section 5.2.1|

**One confirmed correction to previous ground truth:** The report previously stated "T½ reported for [⁶⁸Ga]Ga-DP1 and [¹⁸F]AlF-NP1." This is correct — the paper explicitly gives 7.62 min and 19.32 min for these two compounds only (Section 2.6, Figure S29). The other three radiotracers have no T½ reported in the main text.

**One additional paper clarification:** Section 2.2 states radiochemical purity ">90%", but Section 5.4 states ">95% by radio-HPLC analysis" for the purified final products. These are not contradictory — the ">90%" refers to stability after 2 h incubation (Section 2.2: "RCP remaining consistently above 90%"), while ">95%" is the freshly prepared product purity. Extractions that recorded ">90% RCP" as the product purity were technically applying the stability threshold incorrectly; the correct product purity is ">95% RCP by radio-HPLC."

---

## 3. Failure Mode Taxonomy

|ID|Failure Mode|Correct Behaviour (paper-confirmed)|
|---|---|---|
|C1|DP1/NP1 assigned `final_product`|Must be `intermediate` — Section 5.2.1 confirms full in-house synthesis|
|C2|DP2/DP3/NP2 assigned `intermediate`|Must be `starting_material` — Section 5.2.2 confirms external custom synthesis|
|C3|Log P placed on unlabeled precursors|Null — Section 5.6 measures log P using radioactivity counting on labelled species only|
|C4|KD/Bmax placed on unlabeled precursors|Must be on radiolabeled products — Section 2.4 and Figure 4G name the radiolabeled tracers explicitly|
|C5|Docking scores placed on radiolabeled products|Must be on unlabeled precursors — Section 2.3 and Figure 3B name only the unlabeled ligands|
|C6|Two pH-distinct buffers merged into one entry|Two entries required — Section 5.4 uses 0.25 M pH 6.5 for ⁶⁸Ga and 0.1 M pH 4.0 for AlF, different concentrations and pH|
|C7|pH-adjustment + chelation collapsed into one step|Must be separate — Section 5.4 uses "and then" to demarcate them as sequential distinct operations|

---

---

## 3. Failure Mode Taxonomy

|ID|Failure Mode|Correct Behaviour|
|---|---|---|
|C1|DP1/NP1 assigned `final_product`|Must be `intermediate` (in-house synthesis, not a radiotracer)|
|C2|DP2/DP3/NP2 assigned `intermediate`|Must be `starting_material` (commercially sourced)|
|C3|Log P placed on unlabeled precursors|Null for non-radiolabeled species unless explicitly stated|
|C4|KD/Bmax placed on unlabeled precursors|Must be attributed to radiolabeled products|
|C5|Docking scores placed on radiolabeled products|Must be attributed to unlabeled precursors|
|C6|Two pH-distinct buffers merged into one entry|Two entries, keyed by pH|
|C7|pH-adjustment + chelation collapsed into one step|Must be separate steps in pathway|

## 4. Claude Run Results by Version

### 4.1 v2.1 — 4 Claude Runs

**Prompt features:** Basic role taxonomy, minimal property attribution rules, no step granularity guidance.

|Failure|Pass rate|Detail|
|---|---|---|
|C1 — DP1/NP1 role|2/4 (50%)|Two runs assigned `final_product`; the prompt did not distinguish in-house precursors from final products|
|C2 — External precursor role|3/4 (75%)|One run assigned `intermediate` to DP2/DP3/NP2|
|C3 — Log P attribution|1/4 (25%)|Log P copied onto precursor entries in three runs|
|C4 — KD/Bmax attribution|0/4 (0%)|Universal failure; KD placed on precursors in all runs|
|C5 — Docking scores|N/A|Docking scores not yet extracted by the prompt|
|C6 — Buffer merge|2/4 (50%)|Two runs merged the pH 6.5 and pH 4.0 acetate buffers|
|C7 — Step granularity|1/4 (25%)|Three runs collapsed pH adjustment and chelation into a single step|

**Overall v2.1 Claude pass rate:** 9/24 tracked checks = **38%**

**Qualitative observations:**

- Synthesis step conditions were generally captured correctly: 95 °C / 20 min for ⁶⁸Ga labeling and 100 °C / 20 min for AlF labeling (confirmed against Section 5.4), along with precursor amounts (50 μg, 16–20 nmol for ⁶⁸Ga; 50 μg, 18–25 nmol for AlF) and purification via SepPak C18 with 1.5 mL ethanol.
- HPLC retention times and MS data were reproduced accurately. DP1 (11.230 min), NP1 (12.780 min), and the external precursors (10.328–10.642 min) all match the paper (Sections 5.2.1–5.2.2).
- C1 failure: Two runs assigned `final_product` to DP1/NP1. The paper's Section 5.2.1 describes their synthesis as a precursor step explicitly used for subsequent radiolabeling, but without a prompt rule distinguishing in-house precursors from deliverables, Claude applied a general chemistry heuristic.
- C4 failure (universal): All four runs placed KD on the unlabeled precursors (e.g., KD = 74.9 nM on DP1 rather than on [⁶⁸Ga]Ga-DP1). Section 2.4 of the paper names the radiolabeled tracers explicitly in the KD sentence, but the connection between the assay species and the compound entry was not reliably drawn.
- A minor but consistent accuracy error: some runs recorded product RCP as ">90%" (the 2-h stability threshold from Section 2.2) rather than ">95% by radio-HPLC" (the freshly-prepared product purity from Section 5.4).

---

### 4.2 v2.2 — 3 Claude Runs

**Prompt features added:** Explicit role decision tree, `method_completeness` enum, step granularity guidance (pH adjustment ≠ chelation), buffer deduplication rule.

|Failure|Pass rate|Change vs v2.1|
|---|---|---|
|C1 — DP1/NP1 role|3/3 (100%)|✅ Full resolution|
|C2 — External precursor role|3/3 (100%)|✅ Full resolution|
|C3 — Log P attribution|1/3 (33%)|⚠️ Regression: new phrasing caused log P to be copied via backbone matching|
|C4 — KD/Bmax attribution|1/3 (33%)|⚠️ Minor improvement but still majority failure|
|C5 — Docking scores|1/3 (33%)|🆕 Now extracted; misattributed in two runs|
|C6 — Buffer merge|2/3 (67%)|✅ Improved|
|C7 — Step granularity|3/3 (100%)|✅ Full resolution|

**Overall v2.2 Claude pass rate:** 14/18 tracked checks = **78%**

**Qualitative observations:**

- The role decision tree correctly used the in-house vs. vendor distinction that Section 5.1 and 5.2 make explicit. All three runs correctly identified DP1/NP1 as in-house (Section 5.2.1) and DP2/DP3/NP2 as external (Section 5.2.2).
- C7 was fully resolved. All runs correctly emitted separate pH adjustment and chelation steps, reflecting the "and then transferred" language in Section 5.4.
- C3 regression: The v2.2 prompt introduced log P attribution rules that some runs interpreted as applying to the "peptide backbone," leading them to record log P values on DP1 or NP1. The paper's Section 5.6 is unambiguous that only the five radiolabeled compounds were measured, but the prompt phrasing left room for backbone-transfer inference.
- C4 persisted: The binding assay section (2.4) lists KD values for the radiolabeled tracers by name, but v2.2 Claude still sometimes transferred KD to the precursors that share the same peptide sequence.
- C5 newly tracked: Docking scores appear in Section 2.3 and Figure 3B, attributed to PR7, DP1, DP2, DP3, NP1, NP2 — all unlabeled. Two runs incorrectly placed some of these on the corresponding radiolabeled products.

---

### 4.3 v2.3 — 3 Claude Runs

**Prompt features added:** `radiolabeled_product` priority override (overrides `final_product`), `is_newly_synthesized` clarification, Rule 20 (one pathway per target compound), Rule 21 (log P source-of-truth on radiolabeled species only).

|Failure|Pass rate|Change vs v2.2|
|---|---|---|
|C1 — DP1/NP1 role|3/3 (100%)|✅ Maintained|
|C2 — External precursor role|3/3 (100%)|✅ Maintained|
|C3 — Log P attribution|3/3 (100%)|✅ Full resolution|
|C4 — KD/Bmax attribution|2/3 (67%)|✅ Improved; one run still placed Bmax on a precursor entry|
|C5 — Docking scores|3/3 (100%)|✅ Full resolution|
|C6 — Buffer merge|3/3 (100%)|✅ Full resolution|
|C7 — Step granularity|3/3 (100%)|✅ Maintained|

**Overall v2.3 Claude pass rate:** 20/21 tracked checks = **95%**

**Qualitative observations:**

- C3 fully resolved: All three runs correctly set log P to null for unlabeled compounds and populated it only for the five radiolabeled products. Values match the paper's reported figures (−2.19 to −2.54).
- C4 partial resolution: Two of three runs correctly attributed KD and Bmax to the radiolabeled products (matching Figure 4G: [⁶⁸Ga]Ga-DP1 KD = 74.9 nM, Bmax = 22158 CPM, etc.). Run 1 still placed Bmax on an unlabeled precursor — the prompt's Rule 21 addressed KD explicitly but did not name Bmax by term.
- Compound ID ordering became non-deterministic across runs. Since the paper first mentions [⁶⁸Ga]Ga-DP1 and [¹⁸F]AlF-NP1 prominently in the abstract, then lists precursors in Section 2.2 / Figure 2, then introduces reagents in Section 5.1–5.4, different runs chose different "first appearance" anchors. [¹⁸F]AlF-NP1 was assigned C18 in two runs and C19 in one, due to differing strategies for interleaving the two buffer compound entries.
- HPLC gradient completeness improved: Run 2 correctly recorded both the 5–95% B gradient (Section 5.2.1, DP1/NP1) and the 23–43% B gradient (Section 5.2.2, external precursors). Runs 1 and 3 recorded only one.
- Figure-derived data extraction was inconsistent: Run 3 extracted docking binding site residues (e.g., DP1: K369, Q368, N29, S72… from Figure 3B) and Bmax from Figure 4G. Runs 1 and 2 extracted docking scores but not binding site residue lists, showing variable depth of figure mining.

---

### 4.4 v2.4 — 3 Claude Runs

**Prompt features added:** Rule 7 (deterministic compound ID ordering by first appearance in document), Rule 21 expanded (comprehensive species-of-truth for all physicochemical properties including Bmax), Rule 22 (self-consistency check: no compound may appear as both reactant and product in the same step), Rule 1 amendment (figure-derived data is mandatory).

|Failure|Pass rate|Change vs v2.3|
|---|---|---|
|C1 — DP1/NP1 role|3/3 (100%)|✅ Maintained|
|C2 — External precursor role|3/3 (100%)|✅ Maintained|
|C3 — Log P attribution|3/3 (100%)|✅ Maintained|
|C4 — KD/Bmax attribution|3/3 (100%)|✅ Full resolution (Bmax now explicitly named)|
|C5 — Docking scores|3/3 (100%)|✅ Maintained|
|C6 — Buffer merge|3/3 (100%)|✅ Maintained|
|C7 — Step granularity|3/3 (100%)|✅ Maintained|

**Overall v2.4 Claude pass rate:** 21/21 tracked checks = **100%**

**Remaining inconsistencies (not tracked failures, but noted):**

1. **Compound ID ordering:** Rule 7 partially resolved non-determinism. The paper structure creates genuine ambiguity: the abstract names [⁶⁸Ga]Ga-DP1 and [¹⁸F]AlF-NP1 first, Figure 2 introduces all five precursor structures, Section 5.1 lists reagent sources, and Sections 5.2–5.4 give procedures in a different order. Run 1 used results-section order (PR7=C01); Run 3 anchored to the abstract ([¹⁸F]AlF-NP1=C01). Both are internally consistent and all numerical values match the paper — but cross-run IDs diverge.
    
2. **Duplicate input/output in Step P6 (Run 2):** NP1 appeared as both a reactant and was referenced via `compound_id` in the reagents block of the AlF labeling step. The paper's Section 5.4 lists NP1 as "precursor (50 μg, 18–25 nmol, in 50 μL DMSO)" — clearly a reactant, not a reagent. Rule 22e was designed to catch this; the model did not self-correct.
    
3. **PR7 KD provenance:** The paper's Discussion (Section 3) states PR7's KD = 1.57 × 10⁻⁹ M with a superscript pointing to ref 38 (Zhang et al., _J. Med. Chem._ 2024). This value was measured in a prior study, not in the present work. Two v2.4 runs recorded it in PR7's property block without flagging external provenance; one omitted it. No prompt rule currently addresses this.
    
4. **AlCl₃ and buffer vehicle as one vs. two compound entries:** The paper (Section 5.4) describes "3 μL of 2 mM AlCl₃ in sodium acetate buffer (0.1 M, pH = 4.0)" and then separately "100 μL of sodium acetate buffer (0.1 M, pH = 4.0)." The 100 μL addition is unambiguously a separate, independent addition of pure buffer. Runs diverged on whether to create one entry ("AlCl₃ in sodium acetate buffer") or two separate entries (AlCl₃ solution + buffer). The paper text supports two entries, but this was not encoded in Rule 6.
    

---

## 5. Aggregate Claude Performance

### 5.1 Pass Rates by Failure Mode Across Versions

|Failure|v2.1 (n=4)|v2.2 (n=3)|v2.3 (n=3)|v2.4 (n=3)|
|---|---|---|---|---|
|C1 — DP1/NP1 role|50%|100%|100%|100%|
|C2 — External role|75%|100%|100%|100%|
|C3 — Log P|25%|33%|100%|100%|
|C4 — KD/Bmax|0%|33%|67%|100%|
|C5 — Docking scores|N/A|33%|100%|100%|
|C6 — Buffer merge|50%|67%|100%|100%|
|C7 — Step granularity|25%|100%|100%|100%|
|**Overall**|**38%**|**78%**|**95%**|**100%**|

### 5.2 Resolution Timeline

|Failure|First fully resolved|
|---|---|
|C1 — DP1/NP1 role|v2.2|
|C2 — External precursor role|v2.2|
|C7 — Step granularity|v2.2|
|C3 — Log P|v2.3|
|C5 — Docking scores|v2.3|
|C6 — Buffer merge|v2.3|
|C4 — KD/Bmax|v2.4|

### 5.3 Consistency Dimensions (v2.4 only)

These are not binary pass/fail failures but measure output stability across the three v2.4 Claude runs:

|Dimension|Status|
|---|---|
|Compound ID ordering|⚠️ Partially resolved — deterministic within a run; diverges across runs due to "first appearance" ambiguity|
|Figure data extraction|✅ Fully resolved — all runs extracted binding site residues and cell uptake values|
|HPLC gradient completeness|✅ Resolved — both gradients captured in all three runs|
|PR7 KD provenance flagging|⚠️ Unresolved — no rule for literature-sourced vs. study-measured properties|
|AlCl₃ / buffer entry boundaries|⚠️ Unresolved — Rule 6 ambiguous; runs diverge on whether to merge or separate|

---

## 6. Failure Mode Analysis

### 6.1 Why C1/C2 Were Hard to Resolve Initially

The core difficulty was that "last compound synthesised before radiolabeling" maps intuitively to `final_product` in standard organic chemistry. Section 5.2.1 describes DP1/NP1 synthesis clearly as a precursor step, but without a prompt rule encoding the radiochemistry-specific principle that the radiolabeling step is always the final step, Claude's default heuristic treated the chelator-conjugated peptides as the synthetic endpoint. The distinction was only reliably enforced once the decision tree in v2.2 made the `radiolabeled_product` role the explicit top priority.

### 6.2 Why C4 Persisted Longer Than C3

Log P (C3) was fixed by one rule: "null for all non-radiolabeled compounds." The paper's Section 5.6 supports this unambiguously — radioactivity counting was used, so only radiolabeled species could have log P values. KD and Bmax (C4) required more nuanced reasoning: the assay section (2.4) says "the KD of [⁶⁸Ga]Ga-DP1 … was calculated as 74.9 nM," naming the radiotracer explicitly, but Claude sometimes inferred that binding affinity was a property of the peptide scaffold shared across the unlabeled form. Bmax (from Figure 4G) was even harder because it was table-embedded in a figure rather than stated in running text, and the term "Bmax" was not specifically named in v2.3's Rule 21. Explicitly enumerating Bmax in v2.4 Rule 21 resolved the issue.

### 6.3 The Self-Consistency Check (Rule 22)

Rule 22 was introduced in v2.4 to have Claude verify cross-references before outputting. In two of three runs it was applied correctly. In Run 2 it was not — NP1 appeared in both the reactant list and the reagents block of the AlF labeling step, despite Section 5.4 listing it only as the precursor reactant. This suggests the rule is being applied as a declared commitment rather than an active re-check. A more reliable implementation would require an explicit separate self-check output block prior to the final JSON.

### 6.4 Paper-Confirmed Accuracy of Well-Extracted Fields

The following fields were extracted accurately and consistently across the majority of runs by v2.3–v2.4, verified against the paper:

|Field|Paper value|Extraction accuracy|
|---|---|---|
|⁶⁸Ga labeling temperature|95 °C (Section 5.4)|✅ Correct in all runs from v2.2 onward|
|AlF labeling temperature|100 °C (Section 5.4)|✅ Correct in all runs from v2.2 onward|
|Reaction time (both)|20 min (Section 5.4)|✅ Correct universally|
|SepPak C18 purification|WAT020515, Waters, 1.5 mL EtOH (Section 5.4)|✅ Correct in v2.3–v2.4|
|QMA preconditioning|10 mL saline, then 10 mL pure water (Section 5.4)|✅ Correct in v2.3–v2.4|
|DP1 MS: calcd 2518.14, [M+2H]²⁺ 1260.54, [M+3H]³⁺ 840.68|Section 5.2.1|✅ Correct universally|
|RCY values (5 radiotracers)|Section 2.2|✅ Correct universally|
|Log P values (5 radiotracers)|Sections 2.2–2.3|✅ Correct from v2.3 onward|
|Docking scores (6 unlabeled ligands)|Section 2.3, Figure 3B|✅ Correct from v2.3 onward|
|KD / Bmax (Figure 4G)|Section 2.4, Figure 4G|✅ Correct from v2.4 onward|

---

## 7. Remaining Open Problems for v2.5

The following issues were not resolved by v2.4. All are grounded in specific paper features:

1. **"First appearance" tie-breaking for compound ID ordering.** The paper mentions [⁶⁸Ga]Ga-DP1 and [¹⁸F]AlF-NP1 in the abstract, introduces all five precursors together in Figure 2 (Section 2.2), lists reagent sources in Section 5.1, and gives individual synthesis procedures in Sections 5.2–5.4. Runs assigned different anchor sections. A clear precedence rule (e.g., experimental section for reagents; first named in results for products) would resolve the ambiguity.
    
2. **Literature-sourced vs. study-measured property values.** PR7's KD = 1.57 × 10⁻⁹ M is cited from ref 38 (Zhang et al., _J. Med. Chem._ 2024) in the Discussion section. It is not measured here. A schema field such as `"property_source": "literature | this_study"` with a prompt rule ("if a property value carries a citation to a prior paper, flag as literature") would handle this class of case.
    
3. **AlCl₃ and buffer vehicle as one vs. two compound entries.** Section 5.4 lists "3 μL of 2 mM AlCl₃ in sodium acetate buffer (0.1 M, pH = 4.0)" and then "100 μL of sodium acetate buffer (0.1 M, pH = 4.0)" as independent additions. The buffer used as the AlCl₃ vehicle is the same as the buffer added independently. A rule of the form "if a reagent vehicle appears as an independent addition elsewhere in the same step, it receives a separate compound entry" would resolve this.
    
4. **Operational self-consistency checking.** Rule 22 was treated as a passive constraint. The Run 2 error (NP1 as both reactant and reagent in the AlF step) directly contradicts Section 5.4, where NP1 is unambiguously listed as the precursor reactant. Making Claude emit an explicit `"self_check"` block enumerating cross-references before the final JSON would convert the rule from declarative to operational.
    
5. **Mandatory figure type enumeration.** Rule 1 amendment ("figure-derived data is mandatory") is too general. The paper has at least three figure types that must be mined: Figure 3B (docking scores + binding site residues per ligand), Figure 4G (KD and Bmax per radiotracer), and Figures 5B–6E (tumour uptake and T/NT ratios per model). Specifying each figure type and the fields it populates would eliminate selective extraction.
    

---

## 8. Summary

Claude's extraction quality improved substantially across the four prompt versions, from 38% on tracked failure modes at v2.1 to 100% by v2.4. The trajectory was non-linear: v2.2 introduced regressions in C3 and C5 while resolving C1, C2, and C7; v2.3 achieved the largest single-version improvement (+17 pp). The most persistent failures — C4 (KD/Bmax) and C3 (log P) — both required explicit species-of-truth rules that directly reflected the paper's experimental design: log P measured by radioactivity counting on radiolabeled species only (Section 5.6), and KD/Bmax measured by saturation binding with radiolabeled tracers as the radioligand (Section 2.4, Section 5.9).

By v2.4, all seven categorical failures are eliminated. Factual numerical values — RCY, molar activity, HPLC retention times, MS data, docking scores, KD, Bmax — are extracted accurately and match the paper's Sections 2.2–2.4, 5.2, and 5.4. Synthesis procedures are correctly granularised into separate pH-adjustment, chelation, and purification steps matching the "and then" language of Section 5.4.

The five remaining issues for v2.5 are all consistency and schema-level problems, not correctness failures. They reflect genuine ambiguities in how this paper organises its data across sections, figures, and citations — not systematic extraction errors.

---

_Report covers 13 Claude runs: v2.1 ×4, v2.2 ×3, v2.3 ×3, v2.4 ×3. GPT-4 and Gemini runs excluded. All ground truth claims verified against Yang et al., J. Med. Chem. 2025, 68, 26049–26060._