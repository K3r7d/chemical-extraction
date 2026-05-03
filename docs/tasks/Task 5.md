# Universal test after prompt evolution

## 18f-68ga-labeled-peptide-based-probes-for-pet-imaging-of-ror1-expression

#### Claude

##### Attempt 1
```
{
  "extraction": {
    "prompt_version": "v3.2",
    "extraction_date": "2026-03-30",
    "model_name": "claude-sonnet-4-6",
    "extractor_notes": "SI found: jm5c02016_si_001.pdf (Supporting Information). SI schemes identified: Scheme S1 (synthesis of PR7), Scheme S2 (synthesis of DP2), Scheme S3 (synthesis of DP3), Scheme S4 (synthesis of NP2), Scheme S5 (synthesis of DP1 and NP1). SI compounds identified (author labels): PR7 (C96H133N25O31), DP1, DP2, DP3, NP1, NP2 — all appearing in SI schemes; no separate 'S-numbered' author labels are used, compounds are named PR7/DP1/DP2/DP3/NP1/NP2 throughout. Total pathway count: 8 (P1=PR7 via SPPS; P2=DP2 via SPPS+cyclization; P3=DP3 via SPPS+cyclization+bisalkylation; P4=NP2 via SPPS+cyclization; P5=DP1 from PR7+DOTA-NHS; P6=NP1 from PR7+NOTA-NHS; P7=[68Ga]Ga-DP1/DP2/DP3 radiolabeling; P8=[18F]AlF-NP1/NP2 radiolabeling — note P7 and P8 each label a class of precursors under a common method; split to individual product pathways where needed per Rule 14, giving 10 pathways total: P1 PR7, P2 DP2, P3 DP3, P4 NP2, P5 DP1, P6 NP1, P7 [68Ga]Ga-DP1, P8 [68Ga]Ga-DP2, P9 [68Ga]Ga-DP3, P10 [18F]AlF-NP1, P11 [18F]AlF-NP2). Excluded reference compounds: none (PR7, DP1-DP3, NP1-NP2 are all synthesized in this study or custom-ordered for use as precursors). Mass type notes: all MS data are multiply charged ESI-MS m/z values for large peptides (MW ~2100–3015 Da); reported as [M+2H]2+ and [M+3H]3+ ions; exact monoisotopic masses are provided in SI scheme figures. SPPS coupling cycle details (each amino acid coupling = one step per Rule 9) are summarized as repeat steps in schemes; individual coupling cycles are recorded as step groups. QMA trapping and [18F]AlF complexation are recorded as two separate steps per Rule 9. Rink Amide MBHA Resin and CTC Resin are starting materials for SPPS. DIPEA = N,N-diisopropylethylamine; DIC = N,N'-diisopropylcarbodiimide; HOBt = hydroxybenzotriazole; HBTU = O-benzotriazole-N,N,N',N'-tetramethyluronium hexafluorophosphate; NMM = N-methylmorpholine; HATU = hexafluorophosphate azabenzotriazole tetramethyl uronium; Dde = 1-(4,4-dimethyl-2,6-dioxocyclohexylidene)ethyl; Pip = piperidine; DPPA = diphenylphosphoryl azide; TFA = trifluoroacetic acid; DCM = dichloromethane; DMF = dimethylformamide. Procedures genuinely absent from all available documents: detailed HPLC purification conditions for DP2, DP3, NP2 (only analytical HPLC conditions given for PR7/DP2/DP3/NP2 group; no semipreparative conditions stated for these); exact amounts of each Fmoc-amino acid used in SPPS coupling cycles; resin loading values. The DP3 synthesis involves two cysteine residues cyclized via a bisalkylating linker (1,3-bis(bromomethyl)benzene + cysteamine) in steps 5 and 6."
  },

  "paper": {
    "title": "18F-/68Ga-Labeled Peptide-Based Probes for PET Imaging of ROR1 Expression",
    "authors": [
      "Tao Yang",
      "Jiahui Sun",
      "Guolong Huang",
      "Hong Wang",
      "Zhexin He",
      "Siying Lin",
      "Yanjie Wang",
      "Rongqiang Zhuang",
      "Xianzhong Zhang",
      "Hongwu Liu",
      "Zhide Guo"
    ],
    "doi": "10.1021/acs.jmedchem.5c02016",
    "journal": "Journal of Medicinal Chemistry",
    "year": 2025,
    "synthesis_scale": "preclinical",
    "method_completeness": "partial",
    "has_synthesis": true,
    "extraction_notes": "DP1 and NP1 synthesized in-house (section 5.2.1). PR7, DP2, DP3, NP2 custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. Radiolabeling performed in-house (section 5.4). SI contains Schemes S1–S5 with graphical synthetic routes; detailed step-by-step SPPS conditions readable from scheme annotations. Preparative purification conditions for DP2/DP3/NP2 not stated. Fmoc SPPS coupling cycle details are shown schematically in Schemes S1–S4 as numbered amino acid lists with reagents HOBt/DIC/DMF or HBTU/NMM/DMF indicated."
  },

  "compounds": [
    {
      "id": "C01",
      "name": "PR7",
      "iupac_name": null,
      "molecular_formula": "C96H133N25O31",
      "role": "starting_material",
      "is_newly_synthesized": true,
      "source": "custom synthesis — Nanchang Tanzhen Biotechnology Co., Ltd. (also synthesized in-house via SPPS as Scheme S1)",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ = 1067.47",
      "ms_calculated_exact_mass": 2131.96,
      "description": "ROR1-targeting linear peptide lead compound; used as starting material for conjugation with DOTA-NHS and NOTA-NHS to give DP1 and NP1 respectively; sequence H-Ser(tBu)-Asp(OtBu)-Ile-Asn(Trt)-Asp(OtBu)-Arg(Pbf)-Gln(Trt)-Ile-Pro-Gly-Tyr(tBu)-Ser(tBu)-Thr(tBu)-Tyr(tBu)-Trp(Boc)-Gly-Asp(OtBu)-Phe-Rink Amide MBHA Resin (SPPS); also custom-ordered."
    },
    {
      "id": "C02",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "custom synthesis — Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "DOTA N-hydroxysuccinimide ester; amine-reactive chelator reagent used to conjugate DOTA macrocycle to the N-terminus of PR7 to produce DP1."
    },
    {
      "id": "C03",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "custom synthesis — Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "NOTA N-hydroxysuccinimide ester; amine-reactive chelator reagent used to conjugate NOTA macrocycle to the N-terminus of PR7 to produce NP1."
    },
    {
      "id": "C04",
      "name": "DIPEA",
      "iupac_name": "N,N-diisopropylethylamine",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Hindered amine base used in conjugation of PR7 with DOTA-NHS or NOTA-NHS (synthesis of DP1/NP1) and in SPPS coupling steps."
    },
    {
      "id": "C05",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ = 1260.54, [M+3H]3+ = 840.68",
      "ms_calculated_exact_mass": 2518.14,
      "description": "DOTA-conjugated linear ROR1-targeting peptide precursor; used as precursor for 68Ga radiolabeling to give [68Ga]Ga-DP1; HPLC retention time 11.230 min."
    },
    {
      "id": "C06",
      "name": "NP1",
      "iupac_name": null,
      "molecular_formula": "C108H152N28O36",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ = 1210.22, [M+3H]3+ = 807.00",
      "ms_calculated_exact_mass": 2417.09,
      "description": "NOTA-conjugated linear ROR1-targeting peptide precursor; used as precursor for Al18F radiolabeling to give [18F]AlF-NP1; HPLC retention time 12.780 min."
    },
    {
      "id": "C07",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "custom synthesis — Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ = 1373.07, [M+3H]3+ = 915.72",
      "ms_calculated_exact_mass": 2743.2514,
      "description": "Cyclic DOTA-bearing ROR1-targeting peptide precursor synthesized via SPPS on CTC resin with on-resin DOTA(3tBu) conjugation and head-to-tail cyclization using DPPA; precursor for [68Ga]Ga-DP2; HPLC retention time 10.328 min."
    },
    {
      "id": "C08",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "custom synthesis — Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ = 1509.05, [M+3H]3+ = 1006.39",
      "ms_calculated_exact_mass": 3015.2514,
      "description": "Cyclic DOTA-bearing ROR1-targeting peptide precursor containing two cysteine residues cyclized via bisalkylation with 1,3-bis(bromomethyl)benzene linker; precursor for [68Ga]Ga-DP3; HPLC retention time 10.404 min."
    },
    {
      "id": "C09",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "custom synthesis — Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ = 1322.56",
      "ms_calculated_exact_mass": 2642.20,
      "description": "Cyclic NOTA-bearing ROR1-targeting peptide precursor synthesized via SPPS on CTC resin with on-resin NOTA(2tBu) conjugation and head-to-tail cyclization using DPPA; precursor for [18F]AlF-NP2; HPLC retention time 10.620 min."
    },
    {
      "id": "C10",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "68Ga-radiolabeled DOTA-PR7 linear peptide; primary ROR1 PET imaging agent; HPLC retention time 12.26 ± 0.03 min; RCY 89.55 ± 0.12%; molar activity 14.37 ± 0.97 GBq/µmol."
    },
    {
      "id": "C11",
      "name": "[68Ga]Ga-DP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "68Ga-radiolabeled cyclic DOTA peptide; ROR1 PET imaging agent; HPLC retention time 11.22 ± 0.03 min; RCY 97.67 ± 1.05%; molar activity 20.05 ± 1.35 GBq/µmol."
    },
    {
      "id": "C12",
      "name": "[68Ga]Ga-DP3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "68Ga-radiolabeled cysteine-stapled cyclic DOTA peptide; ROR1 PET imaging agent; HPLC retention time 12.48 ± 0.04 min; RCY 98.01 ± 0.97%; molar activity 14.09 ± 2.12 GBq/µmol."
    },
    {
      "id": "C13",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "18F-labeled AlF-NOTA linear peptide; primary ROR1 18F-PET imaging agent; HPLC retention time 12.93 ± 0.01 min; RCY 62.58 ± 0.32%; molar activity 13.13 ± 1.71 GBq/µmol."
    },
    {
      "id": "C14",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "18F-labeled AlF-NOTA cyclic peptide; ROR1 18F-PET imaging agent; HPLC retention time 11.30 ± 0.01 min; RCY 62.76 ± 0.22%; molar activity 13.42 ± 1.25 GBq/µmol."
    },
    {
      "id": "C15",
      "name": "Rink Amide MBHA Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solid-phase peptide synthesis support resin for C-terminal amide peptides; used in Scheme S1 (PR7 synthesis) as the initial resin."
    },
    {
      "id": "C16",
      "name": "Fmoc-Phe-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "First Fmoc-amino acid loaded onto Rink Amide MBHA Resin in PR7 SPPS (Step 1, Scheme S1); also used in DP2, DP3, NP2 SPPS."
    },
    {
      "id": "C17",
      "name": "HOBt",
      "iupac_name": "1-hydroxybenzotriazole",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling additive used in SPPS coupling steps in Schemes S1, S3, S4 (with DIC); suppresses racemization and activates carboxyl groups."
    },
    {
      "id": "C18",
      "name": "DIC",
      "iupac_name": "N,N'-diisopropylcarbodiimide",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Carbodiimide coupling reagent used with HOBt in SPPS steps in Schemes S1, S3, S4."
    },
    {
      "id": "C19",
      "name": "20% piperidine in DMF",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc deprotection reagent used after each amino acid coupling cycle in all SPPS schemes (S1–S4)."
    },
    {
      "id": "C20",
      "name": "H-Phe-Rink Amide MBHA Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Resin-bound Phe after Fmoc deprotection; transient intermediate at start of PR7 SPPS; input to sequential amino acid coupling cycles."
    },
    {
      "id": "C21",
      "name": "Fmoc-Asp(OtBu)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-protected Asp(OtBu) amino acid building block; coupled in position 1 of PR7 SPPS chain elongation (Scheme S1, Step 2) and in DP2, DP3, NP2 SPPS."
    },
    {
      "id": "C22",
      "name": "Fmoc-Gly-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-Gly amino acid building block used in SPPS of PR7, DP2, DP3, NP2 (Schemes S1–S4)."
    },
    {
      "id": "C23",
      "name": "Fmoc-Trp(Boc)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-Trp(Boc) building block used in SPPS of PR7, DP2, DP3, NP2."
    },
    {
      "id": "C24",
      "name": "Fmoc-Tyr(tBu)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-Tyr(tBu) building block used in SPPS of PR7, DP2, DP3, NP2."
    },
    {
      "id": "C25",
      "name": "Fmoc-Thr(tBu)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-Thr(tBu) building block used in SPPS of PR7, DP2, DP3, NP2."
    },
    {
      "id": "C26",
      "name": "Fmoc-Ser(tBu)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-Ser(tBu) building block used in SPPS of PR7, DP2, DP3, NP2."
    },
    {
      "id": "C27",
      "name": "Fmoc-Ile-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-Ile building block used in SPPS of PR7, DP2, DP3, NP2."
    },
    {
      "id": "C28",
      "name": "Fmoc-Pro-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-Pro building block used in SPPS of PR7, DP2, DP3, NP2."
    },
    {
      "id": "C29",
      "name": "Fmoc-Gln(Trt)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-Gln(Trt) building block used in SPPS of PR7, DP2, DP3, NP2."
    },
    {
      "id": "C30",
      "name": "Fmoc-Arg(Pbf)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-Arg(Pbf) building block used in SPPS of PR7, DP2, DP3, NP2."
    },
    {
      "id": "C31",
      "name": "Fmoc-Asn(Trt)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-Asn(Trt) building block used in SPPS of PR7, DP2, DP3, NP2."
    },
    {
      "id": "C32",
      "name": "TFA",
      "iupac_name": "trifluoroacetic acid",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Global deprotection/cleavage reagent used to cleave fully protected peptides from resin and remove side-chain protecting groups (Schemes S1, S2, S4); also used at 1% in DCM for partial cleavage from CTC resin (Schemes S2, S4, Step 6)."
    },
    {
      "id": "C33",
      "name": "protected PR7-resin (fully assembled)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fully assembled protected PR7 peptide on Rink Amide MBHA Resin after 17 coupling cycles; transient SPPS intermediate prior to TFA global deprotection/cleavage."
    },
    {
      "id": "C34",
      "name": "CTC Resin",
      "iupac_name": "2-chlorotrityl chloride resin",
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solid support for SPPS in Schemes S2 (DP2), S3 (DP3), S4 (NP2); enables mild partial cleavage with 1% TFA/DCM leaving side-chain protecting groups intact for solution-phase cyclization."
    },
    {
      "id": "C35",
      "name": "Fmoc-Gly-Gly-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Dipeptide building block loaded onto CTC Resin as first step in DP2 and NP2 SPPS (Schemes S2, S4, Step 1) with DIPEA/DMF."
    },
    {
      "id": "C36",
      "name": "H-Gly-Gly-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Gly-Gly dipeptide loaded on CTC Resin after Fmoc removal; transient SPPS intermediate for DP2 and NP2 synthesis."
    },
    {
      "id": "C37",
      "name": "Dde-Lys(Fmoc)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Orthogonally protected lysine building block for on-resin bifunctional coupling in DP2 synthesis (Scheme S2, Step 2); Dde on alpha-amine, Fmoc on epsilon-amine."
    },
    {
      "id": "C38",
      "name": "HBTU",
      "iupac_name": "O-benzotriazole-N,N,N',N'-tetramethyluronium hexafluorophosphate",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling reagent used with NMM in Scheme S2 Step 2 (Dde-Lys(Fmoc)-OH coupling) and Scheme S4 Step 2."
    },
    {
      "id": "C39",
      "name": "NMM",
      "iupac_name": "N-methylmorpholine",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base used with HBTU in coupling steps in Schemes S2 and S4."
    },
    {
      "id": "C40",
      "name": "Dde-Lys-Gly-Gly-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Resin-bound Dde-Lys(H)-Gly-Gly after Fmoc removal from epsilon-amine; transient SPPS intermediate in DP2 synthesis."
    },
    {
      "id": "C41",
      "name": "DOTA(3tBu)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Tri-tert-butyl-protected DOTA chelator coupled to the free Lys epsilon-amine on resin in Scheme S2 Step 3 using HATU/NMM."
    },
    {
      "id": "C42",
      "name": "HATU",
      "iupac_name": "hexafluorophosphate azabenzotriazole tetramethyl uronium",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling reagent used with NMM for DOTA(3tBu)/NOTA(2tBu) conjugation to resin-bound Lys in Schemes S2, S4."
    },
    {
      "id": "C43",
      "name": "5% hydrazine in DMF",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Dde deprotection reagent used after DOTA(3tBu)/NOTA(2tBu) coupling in Schemes S2, S4 Step 3 to unmask the alpha-amine of Lys for chain elongation."
    },
    {
      "id": "C44",
      "name": "H-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Resin-bound Lys(DOTA(3tBu))-Gly-Gly after Dde removal; used as anchor for sequential Fmoc SPPS chain elongation in DP2 synthesis."
    },
    {
      "id": "C45",
      "name": "H-Phe-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Resin-bound Phe-Lys(DOTA)-Gly-Gly after Fmoc-Phe coupling and deprotection (Scheme S2 Step 4); template for 17-residue chain elongation."
    },
    {
      "id": "C46",
      "name": "fully assembled protected DP2-precursor on CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fully assembled side-chain-protected linear DP2 precursor peptide on CTC Resin after 17 amino acid coupling cycles (Scheme S2 Step 5)."
    },
    {
      "id": "C47",
      "name": "side-chain-protected linear DP2 precursor (free acid)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Side-chain-protected linear peptide cleaved from CTC Resin with 1% TFA/DCM, retaining all protecting groups; used for head-to-tail cyclization with DPPA in Scheme S2 Step 7."
    },
    {
      "id": "C48",
      "name": "1% TFA in DCM",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Mild acid solution used for partial cleavage of protected peptide from CTC Resin in Schemes S2 and S4 (Steps 6) without removing side-chain protecting groups."
    },
    {
      "id": "C49",
      "name": "DPPA",
      "iupac_name": "diphenylphosphoryl azide",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Peptide cyclization reagent used with DIPEA/DMF for head-to-tail cyclization in Scheme S2 Step 7 (DP2) and Scheme S4 Step 7 (NP2)."
    },
    {
      "id": "C50",
      "name": "protected cyclic DP2 precursor",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Side-chain-protected cyclic DP2 peptide formed after DPPA cyclization; precursor to global TFA deprotection giving DP2."
    },
    {
      "id": "C51",
      "name": "Fmoc-Cys(Trt)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-Cys(Trt) building block loaded as first residue onto CTC Resin in DP3 synthesis (Scheme S3 Step 1); also used as residue 19 in the chain elongation."
    },
    {
      "id": "C52",
      "name": "H-Cys(Trt)-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Resin-bound Cys(Trt) after Fmoc removal; first residue on CTC Resin for DP3 SPPS (Scheme S3 Step 1)."
    },
    {
      "id": "C53",
      "name": "H-Phe-Cys(Trt)-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Resin-bound Phe-Cys(Trt) after Step 2 Fmoc-Phe coupling and deprotection in Scheme S3; template for 20-residue chain elongation including second Cys."
    },
    {
      "id": "C54",
      "name": "Acetic anhydride",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acetylating agent used in Scheme S3 Step 3 (residue 20 in SPPS list) to cap the N-terminus of the DP3 peptide sequence on resin."
    },
    {
      "id": "C55",
      "name": "fully assembled protected DP3-precursor on CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fully assembled N-acetylated side-chain-protected linear DP3 precursor on CTC Resin after 19 amino acid couplings and N-acetylation (Scheme S3 Step 3)."
    },
    {
      "id": "C56",
      "name": "fully deprotected linear DP3 precursor (free Cys thiols)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Global TFA deprotection product of DP3 SPPS resin (Scheme S3 Step 4); linear peptide bearing free Cys thiols and deprotected side chains; used for bisalkylation cyclization."
    },
    {
      "id": "C57",
      "name": "1,3-bis(bromomethyl)benzene",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Bisalkylating cyclization linker that reacts with two free cysteine thiols to form the thioether-stapled cyclic scaffold in DP3 (Scheme S3 Steps 5 and 6)."
    },
    {
      "id": "C58",
      "name": "NH4HCO3 in acetonitrile/water",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Ammonium bicarbonate buffer/ACN solvent system used for bisalkylation cyclization reactions in Scheme S3 Steps 5 and 6."
    },
    {
      "id": "C59",
      "name": "mono-alkylated DP3 intermediate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Intermediate in DP3 synthesis after first thioether bond formation between one Cys and the bisalkylating linker (Scheme S3 Step 5); bears one remaining bromomethyl group for second cyclization."
    },
    {
      "id": "C60",
      "name": "NOTA(2tBu)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Di-tert-butyl-protected NOTA chelator coupled to the free Lys epsilon-amine on resin in Scheme S4 Step 3 (NP2 synthesis) using HATU/DIPEA."
    },
    {
      "id": "C61",
      "name": "H-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Resin-bound Lys(NOTA(2tBu))-Gly-Gly after Dde removal; anchor for NP2 chain elongation in Scheme S4."
    },
    {
      "id": "C62",
      "name": "H-Phe-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Resin-bound Phe-Lys(NOTA(2tBu))-Gly-Gly after Step 4 Fmoc-Phe coupling; template for 17-residue chain elongation in NP2 synthesis."
    },
    {
      "id": "C63",
      "name": "fully assembled protected NP2-precursor on CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fully assembled side-chain-protected linear NP2 precursor peptide on CTC Resin after 17 amino acid coupling cycles (Scheme S4 Step 5)."
    },
    {
      "id": "C64",
      "name": "side-chain-protected linear NP2 precursor (free acid)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Protected linear NP2 peptide cleaved from CTC Resin with 1% TFA/DCM for cyclization."
    },
    {
      "id": "C65",
      "name": "protected cyclic NP2 precursor",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Side-chain-protected cyclic NP2 peptide formed after DPPA/DIPEA cyclization (Scheme S4 Step 7); precursor to global TFA deprotection giving NP2."
    },
    {
      "id": "C66",
      "name": "68GaCl3",
      "iupac_name": "gallium-68 trichloride",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "68Ge/68Ga generator (ITM)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Radionuclide source for 68Ga radiolabeling; eluted in 0.1 M HCl from 68Ge/68Ga generator; used in preparation of [68Ga]Ga-DP1, [68Ga]Ga-DP2, [68Ga]Ga-DP3."
    },
    {
      "id": "C67",
      "name": "sodium acetate buffer (0.25 M, pH 6.5)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Buffer used to adjust pH of 68GaCl3 solution to pH 4–4.5 prior to radiolabeling of DP1/DP2/DP3."
    },
    {
      "id": "C68",
      "name": "fluoride-18 ([18F]fluoride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Cyclone 18/9 cyclotron (IBA, Belgium) at Xiamen University",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "18F radionuclide source produced via 18O(p,n)18F reaction; trapped on QMA cartridge then eluted for Al18F radiolabeling of NP1 and NP2."
    },
    {
      "id": "C69",
      "name": "QMA cartridge",
      "iupac_name": "quaternary methyl ammonium anion-exchange cartridge",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Ion-exchange solid-phase trap used to capture [18F]fluoride from cyclotron water target; preconditioned with 10 mL saline and 10 mL pure water; [18F]F- subsequently eluted with saline."
    },
    {
      "id": "C70",
      "name": "aluminum chloride solution (2 mM AlCl3 in 0.1 M sodium acetate buffer, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Al3+ source for Al18F chelation by NOTA in [18F]AlF-NP1 and [18F]AlF-NP2 synthesis; added as 3 µL of 2 mM solution."
    },
    {
      "id": "C71",
      "name": "sodium acetate buffer (0.1 M, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "pH 4.0 buffer used in [18F]AlF radiolabeling reaction mixture for NP1 and NP2."
    },
    {
      "id": "C72",
      "name": "SepPak C18 cartridge",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Waters (WAT020515)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Reversed-phase solid-phase extraction cartridge used to purify all five radiolabeled products ([68Ga]Ga-DP1/DP2/DP3 and [18F]AlF-NP1/NP2) after radiolabeling; eluted with 1.5 mL ethanol."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of PR7 (SI Scheme S1)",
      "source_section": "SI_scheme_S1",
      "target_compound_id": "C01",
      "target_compound_name": "PR7",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Fmoc SPPS — resin loading",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "Rink Amide MBHA Resin",
              "amount": null
            },
            {
              "compound_id": "C16",
              "name": "Fmoc-Phe-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C17",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C18",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Fmoc-Phe-Rink Amide MBHA Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Fmoc-Phe-OH loaded onto Rink Amide MBHA Resin using HOBt/DIC/DMF per Scheme S1."
        },
        {
          "step_number": 2,
          "reaction_type": "Fmoc deprotection",
          "reactants": [
            {
              "compound_id": null,
              "name": "Fmoc-Phe-Rink Amide MBHA Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C19",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C20",
            "name": "H-Phe-Rink Amide MBHA Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Fmoc SPPS — sequential coupling of 17 amino acids (residues 1–17 of PR7 sequence)",
          "reactants": [
            {
              "compound_id": "C20",
              "name": "H-Phe-Rink Amide MBHA Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C21",
              "name": "Fmoc-Asp(OtBu)-OH (residue 1)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C22",
              "name": "Fmoc-Gly-OH (residues 2, 8)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C23",
              "name": "Fmoc-Trp(Boc)-OH (residue 3)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C24",
              "name": "Fmoc-Tyr(tBu)-OH (residues 4, 7)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C25",
              "name": "Fmoc-Thr(tBu)-OH (residue 5)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C26",
              "name": "Fmoc-Ser(tBu)-OH (residues 6, 10, 17)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C27",
              "name": "Fmoc-Ile-OH (residues 9, 15)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C28",
              "name": "Fmoc-Pro-OH (residue 9)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C29",
              "name": "Fmoc-Gln(Trt)-OH (residue 11)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C30",
              "name": "Fmoc-Arg(Pbf)-OH (residue 12)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C31",
              "name": "Fmoc-Asn(Trt)-OH (residues 13, 14)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C17",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C18",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C19",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Coupling and deprotection cycles repeated 17 times; sequence (N→C on resin): Asp(OtBu)-Gly-Trp(Boc)-Tyr(tBu)-Thr(tBu)-Ser(tBu)-Tyr(tBu)-Gly-Pro-Ile-Gln(Trt)-Arg(Pbf)-Asp(OtBu)-Asn(Trt)-Ile-Asp(OtBu)-Ser(tBu)"
          },
          "product": {
            "compound_id": "C33",
            "name": "fully assembled protected PR7 peptide on Rink Amide MBHA Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Residue numbering and identity read from Scheme S1 annotation. Exact amounts of each amino acid not stated."
        },
        {
          "step_number": 4,
          "reaction_type": "Global deprotection and cleavage from resin",
          "reactants": [
            {
              "compound_id": "C33",
              "name": "fully assembled protected PR7 peptide on Rink Amide MBHA Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C32",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C01",
            "name": "PR7",
            "yield": null,
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 10.642
          },
          "purification": null,
          "notes": "Cleavage cocktail composition not specified in SI Scheme S1; standard TFA cocktail assumed. Purification method not stated for the custom-synthesized batch; peptide was custom-ordered from vendor."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of DP2 (SI Scheme S2)",
      "source_section": "SI_scheme_S2",
      "target_compound_id": "C07",
      "target_compound_name": "DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Fmoc SPPS — loading Fmoc-Gly-Gly-OH onto CTC Resin",
          "reactants": [
            {
              "compound_id": "C34",
              "name": "CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C35",
              "name": "Fmoc-Gly-Gly-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Fmoc-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Fmoc deprotection",
          "reactants": [
            {
              "compound_id": null,
              "name": "Fmoc-Gly-Gly-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C19",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C36",
            "name": "H-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Fmoc SPPS — coupling Dde-Lys(Fmoc)-OH",
          "reactants": [
            {
              "compound_id": "C36",
              "name": "H-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C37",
              "name": "Dde-Lys(Fmoc)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C38",
              "name": "HBTU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C39",
              "name": "NMM",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Dde-Lys(Fmoc)-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "Fmoc deprotection of Lys epsilon-amine",
          "reactants": [
            {
              "compound_id": null,
              "name": "Dde-Lys(Fmoc)-Gly-Gly-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C19",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C40",
            "name": "Dde-Lys(H)-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "On-resin DOTA(3tBu) coupling to Lys epsilon-amine",
          "reactants": [
            {
              "compound_id": "C40",
              "name": "Dde-Lys(H)-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C41",
              "name": "DOTA(3tBu)",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C42",
              "name": "HATU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C39",
              "name": "NMM",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Dde-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 6,
          "reaction_type": "Dde deprotection",
          "reactants": [
            {
              "compound_id": null,
              "name": "Dde-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C43",
              "name": "5% hydrazine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "H2O/DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C44",
            "name": "H-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 7,
          "reaction_type": "Fmoc SPPS — coupling Fmoc-Phe-OH",
          "reactants": [
            {
              "compound_id": "C44",
              "name": "H-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C16",
              "name": "Fmoc-Phe-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C17",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C18",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Fmoc-Phe-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 8,
          "reaction_type": "Fmoc deprotection",
          "reactants": [
            {
              "compound_id": null,
              "name": "Fmoc-Phe-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C19",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C45",
            "name": "H-Phe-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 9,
          "reaction_type": "Fmoc SPPS — sequential coupling of 17 amino acids (PR7 sequence, residues 1–17)",
          "reactants": [
            {
              "compound_id": "C45",
              "name": "H-Phe-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C21",
              "name": "Fmoc-Asp(OtBu)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C22",
              "name": "Fmoc-Gly-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C23",
              "name": "Fmoc-Trp(Boc)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C24",
              "name": "Fmoc-Tyr(tBu)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C25",
              "name": "Fmoc-Thr(tBu)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C26",
              "name": "Fmoc-Ser(tBu)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C27",
              "name": "Fmoc-Ile-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C28",
              "name": "Fmoc-Pro-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C29",
              "name": "Fmoc-Gln(Trt)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C30",
              "name": "Fmoc-Arg(Pbf)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C31",
              "name": "Fmoc-Asn(Trt)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C17",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C18",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C19",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Sequence elongation: H-Ser(tBu)-Asp(OtBu)-Ile-Asn(Trt)-Asp(OtBu)-Arg(Pbf)-Gln(Trt)-Ile-Pro-Gly-Tyr(tBu)-Ser(tBu)-Thr(tBu)-Tyr(tBu)-Trp(Boc)-Gly-Asp(OtBu)-Phe-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin"
          },
          "product": {
            "compound_id": "C46",
            "name": "fully assembled protected DP2-precursor on CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 10,
          "reaction_type": "Partial cleavage from CTC Resin with 1% TFA/DCM",
          "reactants": [
            {
              "compound_id": "C46",
              "name": "fully assembled protected DP2-precursor on CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C48",
              "name": "1% TFA in DCM",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DCM",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Side-chain protecting groups retained; only backbone–resin ester cleaved."
          },
          "product": {
            "compound_id": "C47",
            "name": "side-chain-protected linear DP2 precursor (free acid)",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 11,
          "reaction_type": "Head-to-tail macrolactamization (cyclization) then global deprotection",
          "reactants": [
            {
              "compound_id": "C47",
              "name": "side-chain-protected linear DP2 precursor (free acid)",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C49",
              "name": "DPPA",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C32",
              "name": "TFA (global deprotection, second sub-step)",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DMF (cyclization)",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cyclization with DPPA/DIPEA/DMF followed by global TFA deprotection as two sequential sub-steps (Scheme S2 Step 7)."
          },
          "product": {
            "compound_id": "C07",
            "name": "DP2",
            "yield": null,
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 10.328
          },
          "purification": null,
          "notes": "Purification method for DP2 not specified in main text or SI; custom synthesis by vendor; analytical HPLC retention time from main text section 5.2.2."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Synthesis of DP3 (SI Scheme S3)",
      "source_section": "SI_scheme_S3",
      "target_compound_id": "C08",
      "target_compound_name": "DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Fmoc SPPS — loading Fmoc-Cys(Trt)-OH onto CTC Resin",
          "reactants": [
            {
              "compound_id": "C34",
              "name": "CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C51",
              "name": "Fmoc-Cys(Trt)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Fmoc-Cys(Trt)-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Fmoc deprotection then Fmoc-Phe-OH coupling",
          "reactants": [
            {
              "compound_id": null,
              "name": "Fmoc-Cys(Trt)-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C16",
              "name": "Fmoc-Phe-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C19",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            },
            {
              "compound_id": "C17",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C18",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C53",
            "name": "H-Phe-Cys(Trt)-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Scheme S3 Step 2 shows deprotection then Fmoc-Phe coupling as a combined step."
        },
        {
          "step_number": 3,
          "reaction_type": "Fmoc SPPS — sequential coupling of 20 amino acids/residues including N-terminal acetylation",
          "reactants": [
            {
              "compound_id": "C53",
              "name": "H-Phe-Cys(Trt)-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C21",
              "name": "Fmoc-Asp(OtBu)-OH (residues 1, 13, 16)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C22",
              "name": "Fmoc-Gly-OH (residues 2, 8, 18)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C23",
              "name": "Fmoc-Trp(Boc)-OH (residue 3)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C24",
              "name": "Fmoc-Tyr(tBu)-OH (residues 4, 7)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C25",
              "name": "Fmoc-Thr(tBu)-OH (residue 5)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C26",
              "name": "Fmoc-Ser(tBu)-OH (residues 6, 17)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C27",
              "name": "Fmoc-Ile-OH (residues 9, 15)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C28",
              "name": "Fmoc-Pro-OH (residue 9)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C29",
              "name": "Fmoc-Gln(Trt)-OH (residue 11)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C30",
              "name": "Fmoc-Arg(Pbf)-OH (residue 12)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C31",
              "name": "Fmoc-Asn(Trt)-OH (residue 14)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C51",
              "name": "Fmoc-Cys(Trt)-OH (residue 19)",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C54",
              "name": "Acetic anhydride (N-terminal acetylation, residue 20)",
              "amount": null,
              "role": "protecting_group_reagent"
            },
            {
              "compound_id": "C17",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C18",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C19",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Final sequence on resin: Ac-Cys(Trt)-Gly-Ser(tBu)-Asp(OtBu)-Ile-Asn(Trt)-Asp(OtBu)-Arg(Pbf)-Gln(Trt)-Ile-Pro-Gly-Tyr(tBu)-Ser(tBu)-Thr(tBu)-Tyr(tBu)-Trp(Boc)-Gly-Asp(OtBu)-Phe-Cys(Trt)-CTC Resin"
          },
          "product": {
            "compound_id": "C55",
            "name": "fully assembled protected DP3-precursor on CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "Global deprotection and cleavage from resin with TFA",
          "reactants": [
            {
              "compound_id": "C55",
              "name": "fully assembled protected DP3-precursor on CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C32",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C56",
            "name": "fully deprotected linear DP3 precursor (free Cys thiols)",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "First thioether alkylation (mono-alkylation with 1,3-bis(bromomethyl)benzene)",
          "reactants": [
            {
              "compound_id": "C56",
              "name": "fully deprotected linear DP3 precursor (free Cys thiols)",
              "amount": null
            },
            {
              "compound_id": "C57",
              "name": "1,3-bis(bromomethyl)benzene",
              "amount": null
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "NH4HCO3 / acetonitrile",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C59",
            "name": "mono-alkylated DP3 intermediate",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Scheme S3 Step 5 shows reaction of linear deprotected peptide with bisalkylating linker in NH4HCO3/ACN."
        },
        {
          "step_number": 6,
          "reaction_type": "Second thioether alkylation (intramolecular cyclization to complete bisthioether staple)",
          "reactants": [
            {
              "compound_id": "C59",
              "name": "mono-alkylated DP3 intermediate",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C58",
              "name": "NH4HCO3 in acetonitrile/water",
              "amount": null,
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile / water",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C08",
            "name": "DP3",
            "yield": null,
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 10.404
          },
          "purification": null,
          "notes": "Scheme S3 Step 6 shows cyclization completed by second Cys reacting with remaining bromomethyl group; purification method not stated."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Synthesis of NP2 (SI Scheme S4)",
      "source_section": "SI_scheme_S4",
      "target_compound_id": "C09",
      "target_compound_name": "NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Fmoc SPPS — loading Fmoc-Gly-Gly-OH onto CTC Resin",
          "reactants": [
            {
              "compound_id": "C34",
              "name": "CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C35",
              "name": "Fmoc-Gly-Gly-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Fmoc-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Fmoc deprotection then Dde-Lys(Fmoc)-OH coupling",
          "reactants": [
            {
              "compound_id": null,
              "name": "Fmoc-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C37",
              "name": "Dde-Lys(Fmoc)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C19",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            },
            {
              "compound_id": "C38",
              "name": "HBTU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C40",
            "name": "Dde-Lys(H)-Gly-Gly-CTC Resin (after Fmoc removal from epsilon-NH2)",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Scheme S4 Step 2 uses HBTU/DIPEA instead of HBTU/NMM as in Scheme S2."
        },
        {
          "step_number": 3,
          "reaction_type": "On-resin NOTA(2tBu) coupling to Lys epsilon-amine then Dde removal",
          "reactants": [
            {
              "compound_id": "C40",
              "name": "Dde-Lys(H)-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C60",
              "name": "NOTA(2tBu)",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C42",
              "name": "HATU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C43",
              "name": "5% hydrazine in DMF/H2O",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C61",
            "name": "H-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "Fmoc-Phe-OH coupling and deprotection",
          "reactants": [
            {
              "compound_id": "C61",
              "name": "H-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C16",
              "name": "Fmoc-Phe-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C17",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C18",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C19",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C62",
            "name": "H-Phe-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "Fmoc SPPS — sequential coupling of 17 amino acids (PR7 sequence, residues 1–17)",
          "reactants": [
            {
              "compound_id": "C62",
              "name": "H-Phe-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C21",
              "name": "Fmoc-Asp(OtBu)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C22",
              "name": "Fmoc-Gly-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C23",
              "name": "Fmoc-Trp(Boc)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C24",
              "name": "Fmoc-Tyr(tBu)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C25",
              "name": "Fmoc-Thr(tBu)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C26",
              "name": "Fmoc-Ser(tBu)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C27",
              "name": "Fmoc-Ile-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C28",
              "name": "Fmoc-Pro-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C29",
              "name": "Fmoc-Gln(Trt)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C30",
              "name": "Fmoc-Arg(Pbf)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C31",
              "name": "Fmoc-Asn(Trt)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C17",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C18",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C19",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Sequence: H-Ser(tBu)-Asp(OtBu)-Ile-Asn(Trt)-Asp(OtBu)-Arg(Pbf)-Gln(Trt)-Ile-Pro-Gly-Tyr(tBu)-Ser(tBu)-Thr(tBu)-Tyr(tBu)-Trp(Boc)-Gly-Asp(OtBu)-Phe-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin"
          },
          "product": {
            "compound_id": "C63",
            "name": "fully assembled protected NP2-precursor on CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 6,
          "reaction_type": "Partial cleavage from CTC Resin with 1% TFA/DCM",
          "reactants": [
            {
              "compound_id": "C63",
              "name": "fully assembled protected NP2-precursor on CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C48",
              "name": "1% TFA in DCM",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DCM",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C64",
            "name": "side-chain-protected linear NP2 precursor (free acid)",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 7,
          "reaction_type": "Head-to-tail macrolactamization then global deprotection",
          "reactants": [
            {
              "compound_id": "C64",
              "name": "side-chain-protected linear NP2 precursor (free acid)",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C49",
              "name": "DPPA",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C32",
              "name": "TFA (global deprotection)",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DMF (cyclization)",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cyclization with DPPA/DIPEA/DMF followed by TFA global deprotection as two sequential sub-steps."
          },
          "product": {
            "compound_id": "C09",
            "name": "NP2",
            "yield": null,
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 10.620
          },
          "purification": null,
          "notes": "Purification conditions not specified; custom synthesis by vendor."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Synthesis of DP1 from PR7 + DOTA-NHS (SI Scheme S5 / main text Section 5.2.1)",
      "source_section": "SI_scheme_S5",
      "target_compound_id": "C05",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester conjugation of DOTA-NHS to PR7",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 µmol)"
            },
            {
              "compound_id": "C02",
              "name": "DOTA-NHS",
              "amount": "2.5 mg (5 µmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": "20 µL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 µL"
            }
          ],
          "conditions": {
            "temperature": "room temperature (RT)",
            "time": "12 h",
            "atmosphere": null,
            "ph": null,
            "other": "Reaction performed in a 2 mL centrifugation tube with oscillation."
          },
          "product": {
            "compound_id": "C05",
            "name": "DP1",
            "yield": "4.2 mg (55.6%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 11.230
          },
          "purification": "semipreparative HPLC, UV detection at 254 nm; lyophilization",
          "notes": "Parallel reaction with NOTA-NHS in the same vessel yields NP1 in a separate experiment (section 5.2.1 describes both in one paragraph but as independent reactions)."
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Synthesis of NP1 from PR7 + NOTA-NHS (SI Scheme S5 / main text Section 5.2.1)",
      "source_section": "SI_scheme_S5",
      "target_compound_id": "C06",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester conjugation of NOTA-NHS to PR7",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 µmol)"
            },
            {
              "compound_id": "C03",
              "name": "NOTA-NHS",
              "amount": "2 mg (5 µmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": "20 µL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 µL"
            }
          ],
          "conditions": {
            "temperature": "room temperature (RT)",
            "time": "12 h",
            "atmosphere": null,
            "ph": null,
            "other": "Reaction performed in a 2 mL centrifugation tube with oscillation."
          },
          "product": {
            "compound_id": "C06",
            "name": "NP1",
            "yield": "3.9 mg (54%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 12.780
          },
          "purification": "semipreparative HPLC, UV detection at 254 nm; lyophilization",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP1 (main text Section 5.4)",
      "source_section": "main_text",
      "target_compound_id": "C10",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3 with sodium acetate buffer",
          "reactants": [
            {
              "compound_id": "C66",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C67",
              "name": "sodium acetate buffer (0.25 M, pH 6.5)",
              "amount": "0.5 mL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "68Ga radiolabeling (chelation of 68Ga3+ by DOTA)",
          "reactants": [
            {
              "compound_id": "C05",
              "name": "DP1 precursor",
              "amount": "50 µg (16–20 nmol) in 50 µL DMSO"
            },
            {
              "compound_id": null,
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL"
            }
          ],
          "reagents": [],
          "solvents": [],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to RT after heating."
          },
          "product": {
            "compound_id": null,
            "name": "crude [68Ga]Ga-DP1 reaction mixture",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Solid-phase extraction purification",
          "reactants": [
            {
              "compound_id": null,
              "name": "crude [68Ga]Ga-DP1 reaction mixture",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C72",
              "name": "SepPak C18 cartridge",
              "amount": null,
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "ethanol",
              "volume": "1.5 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C10",
            "name": "[68Ga]Ga-DP1",
            "yield": "89.55 ± 0.12%",
            "purity": ">95% RCP by radio-HPLC",
            "hplc_retention_time_min": 12.26
          },
          "purification": "SepPak C18 cartridge, 1.5 mL ethanol eluent",
          "notes": "Radiochemical yield, purity and molar activity determined by radio-HPLC (Dionex UltiMate 3000; mobile phase 0.1% TFA/water to 0.1% TFA/ACN, 5–95% B over 20 min, 1 mL/min); molar activity 14.37 ± 0.97 GBq/µmol (n ≥ 3)."
        }
      ]
    },
    {
      "pathway_id": "P8",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP2 (main text Section 5.4)",
      "source_section": "main_text",
      "target_compound_id": "C11",
      "target_compound_name": "[68Ga]Ga-DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3 with sodium acetate buffer",
          "reactants": [
            {
              "compound_id": "C66",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C67",
              "name": "sodium acetate buffer (0.25 M, pH 6.5)",
              "amount": "0.5 mL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "68Ga radiolabeling (chelation by DOTA)",
          "reactants": [
            {
              "compound_id": "C07",
              "name": "DP2 precursor",
              "amount": "50 µg (16–20 nmol) in 50 µL DMSO"
            },
            {
              "compound_id": null,
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL"
            }
          ],
          "reagents": [],
          "solvents": [],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to RT after heating."
          },
          "product": {
            "compound_id": null,
            "name": "crude [68Ga]Ga-DP2 reaction mixture",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Solid-phase extraction purification",
          "reactants": [
            {
              "compound_id": null,
              "name": "crude [68Ga]Ga-DP2 reaction mixture",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C72",
              "name": "SepPak C18 cartridge",
              "amount": null,
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "ethanol",
              "volume": "1.5 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C11",
            "name": "[68Ga]Ga-DP2",
            "yield": "97.67 ± 1.05%",
            "purity": ">95% RCP by radio-HPLC",
            "hplc_retention_time_min": 11.22
          },
          "purification": "SepPak C18 cartridge, 1.5 mL ethanol eluent",
          "notes": "Molar activity 20.05 ± 1.35 GBq/µmol (n ≥ 3)."
        }
      ]
    },
    {
      "pathway_id": "P9",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP3 (main text Section 5.4)",
      "source_section": "main_text",
      "target_compound_id": "C12",
      "target_compound_name": "[68Ga]Ga-DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3 with sodium acetate buffer",
          "reactants": [
            {
              "compound_id": "C66",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C67",
              "name": "sodium acetate buffer (0.25 M, pH 6.5)",
              "amount": "0.5 mL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "68Ga radiolabeling (chelation by DOTA)",
          "reactants": [
            {
              "compound_id": "C08",
              "name": "DP3 precursor",
              "amount": "50 µg (16–20 nmol) in 50 µL DMSO"
            },
            {
              "compound_id": null,
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL"
            }
          ],
          "reagents": [],
          "solvents": [],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to RT after heating."
          },
          "product": {
            "compound_id": null,
            "name": "crude [68Ga]Ga-DP3 reaction mixture",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Solid-phase extraction purification",
          "reactants": [
            {
              "compound_id": null,
              "name": "crude [68Ga]Ga-DP3 reaction mixture",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C72",
              "name": "SepPak C18 cartridge",
              "amount": null,
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "ethanol",
              "volume": "1.5 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C12",
            "name": "[68Ga]Ga-DP3",
            "yield": "98.01 ± 0.97%",
            "purity": ">95% RCP by radio-HPLC",
            "hplc_retention_time_min": 12.48
          },
          "purification": "SepPak C18 cartridge, 1.5 mL ethanol eluent",
          "notes": "Molar activity 14.09 ± 2.12 GBq/µmol (n ≥ 3)."
        }
      ]
    },
    {
      "pathway_id": "P10",
      "pathway_name": "Radiolabeling of [18F]AlF-NP1 (main text Section 5.4)",
      "source_section": "main_text",
      "target_compound_id": "C13",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "18F trapping on QMA cartridge",
          "reactants": [
            {
              "compound_id": "C68",
              "name": "fluoride-18 ([18F]fluoride) in cyclotron target water",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [
            {
              "compound_id": "C69",
              "name": "QMA cartridge (preconditioned with 10 mL saline, 10 mL pure water)",
              "amount": null,
              "role": "other"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride trapped on QMA cartridge",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "18F elution from QMA and Al18F complexation with NOTA-peptide precursor",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride trapped on QMA cartridge",
              "amount": null
            },
            {
              "compound_id": "C06",
              "name": "NP1 precursor",
              "amount": "50 µg (18–25 nmol) in 50 µL DMSO"
            }
          ],
          "reagents": [
            {
              "compound_id": "C70",
              "name": "aluminum chloride solution (2 mM AlCl3 in 0.1 M sodium acetate buffer, pH 4.0)",
              "amount": "3 µL",
              "role": "other"
            },
            {
              "compound_id": "C71",
              "name": "sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "100 µL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "saline (for QMA elution)",
              "volume": "0.2 mL"
            },
            {
              "name": "acetonitrile",
              "volume": "200 µL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to RT after heating."
          },
          "product": {
            "compound_id": null,
            "name": "crude [18F]AlF-NP1 reaction mixture",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "[18F]fluoride eluted from QMA with 0.2 mL saline into the vial containing AlCl3, ACN, sodium acetate buffer, and NP1 precursor."
        },
        {
          "step_number": 3,
          "reaction_type": "Solid-phase extraction purification and formulation",
          "reactants": [
            {
              "compound_id": null,
              "name": "crude [18F]AlF-NP1 reaction mixture",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C72",
              "name": "SepPak C18 cartridge",
              "amount": null,
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "ethanol",
              "volume": "1.5 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Ethanol evaporated after SPE; product reconstituted in saline."
          },
          "product": {
            "compound_id": "C13",
            "name": "[18F]AlF-NP1",
            "yield": "62.58 ± 0.32%",
            "purity": ">95% RCP by radio-HPLC",
            "hplc_retention_time_min": 12.93
          },
          "purification": "SepPak C18 cartridge, 1.5 mL ethanol eluent; solvent removed; reconstituted in saline",
          "notes": "Molar activity 13.13 ± 1.71 GBq/µmol (n ≥ 3)."
        }
      ]
    },
    {
      "pathway_id": "P11",
      "pathway_name": "Radiolabeling of [18F]AlF-NP2 (main text Section 5.4)",
      "source_section": "main_text",
      "target_compound_id": "C14",
      "target_compound_name": "[18F]AlF-NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "18F trapping on QMA cartridge",
          "reactants": [
            {
              "compound_id": "C68",
              "name": "fluoride-18 ([18F]fluoride) in cyclotron target water",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [
            {
              "compound_id": "C69",
              "name": "QMA cartridge (preconditioned with 10 mL saline, 10 mL pure water)",
              "amount": null,
              "role": "other"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride trapped on QMA cartridge",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "18F elution from QMA and Al18F complexation with NOTA-peptide precursor",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride trapped on QMA cartridge",
              "amount": null
            },
            {
              "compound_id": "C09",
              "name": "NP2 precursor",
              "amount": "50 µg (18–25 nmol) in 50 µL DMSO"
            }
          ],
          "reagents": [
            {
              "compound_id": "C70",
              "name": "aluminum chloride solution (2 mM AlCl3 in 0.1 M sodium acetate buffer, pH 4.0)",
              "amount": "3 µL",
              "role": "other"
            },
            {
              "compound_id": "C71",
              "name": "sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "100 µL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "saline (for QMA elution)",
              "volume": "0.2 mL"
            },
            {
              "name": "acetonitrile",
              "volume": "200 µL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to RT after heating."
          },
          "product": {
            "compound_id": null,
            "name": "crude [18F]AlF-NP2 reaction mixture",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Solid-phase extraction purification and formulation",
          "reactants": [
            {
              "compound_id": null,
              "name": "crude [18F]AlF-NP2 reaction mixture",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C72",
              "name": "SepPak C18 cartridge",
              "amount": null,
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "ethanol",
              "volume": "1.5 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Ethanol evaporated; product reconstituted in saline."
          },
          "product": {
            "compound_id": "C14",
            "name": "[18F]AlF-NP2",
            "yield": "62.76 ± 0.22%",
            "purity": ">95% RCP by radio-HPLC",
            "hplc_retention_time_min": 11.30
          },
          "purification": "SepPak C18 cartridge, 1.5 mL ethanol eluent; solvent removed; reconstituted in saline",
          "notes": "Molar activity 13.42 ± 1.25 GBq/µmol (n ≥ 3)."
        }
      ]
    }
  ]
}
```
##### Attempt 2
```
{
  "extraction": {
    "prompt_version": "v3.2",
    "extraction_date": "2026-03-31",
    "model_name": "claude-sonnet-4-6",
    "extractor_notes": "SI found: jm5c02016_si_001.pdf. SI schemes identified: Scheme S1 (synthetic route of PR7), Scheme S2 (synthetic route of DP2), Scheme S3 (synthetic route of DP3), Scheme S4 (synthetic route of NP2), Scheme S5 (synthetic route of DP1 and NP1). SI compounds identified (author labels): PR7, DP1, DP2, DP3, NP1, NP2, and radiolabeled products [68Ga]Ga-DP1, [68Ga]Ga-DP2, [68Ga]Ga-DP3, [18F]AlF-NP1, [18F]AlF-NP2. Total pathway count: 7 (P1: PR7 via SPPS, main text section 5.2.2 and SI Scheme S1; P2: DP2 via SPPS + cyclization, SI Scheme S2; P3: DP3 via SPPS + cyclization, SI Scheme S3; P4: NP2 via SPPS + cyclization, SI Scheme S4; P5: DP1 from PR7, SI Scheme S5/main text 5.2.1; P6: NP1 from PR7, SI Scheme S5/main text 5.2.1; P7: radiolabeling of [68Ga]Ga-DP1/DP2/DP3 and [18F]AlF-NP1/NP2, main text 5.4). Excluded reference compounds: none identifiable (PR7 is synthesised in this study and serves as starting material for DP1/NP1). Mass type notes: all compounds are large peptides (MW ~2100–3015 Da); the paper reports both calculated exact mass (monoisotopic) and average molecular weight in SI schemes; ESI-MS data are reported as multiply charged ions [M+2H]2+ and [M+3H]3+, consistent with monoisotopic/high-resolution ESI-TOF MS. Procedures for PR7, DP2, DP3, and NP2 are custom synthesis (Nanchang Tanzhen Biotechnology Co., Ltd.) with full SPPS routes shown in SI Schemes S1–S4 but lacking detailed step-level quantities beyond reagent names; DP1 and NP1 have full procedural detail in main text section 5.2.1 and SI Scheme S5. Radiolabeling procedures are fully described in main text section 5.4."
  },

  "paper": {
    "title": "18F-/68Ga-Labeled Peptide-Based Probes for PET Imaging of ROR1 Expression",
    "authors": [
      "Tao Yang",
      "Jiahui Sun",
      "Guolong Huang",
      "Hong Wang",
      "Zhexin He",
      "Siying Lin",
      "Yanjie Wang",
      "Rongqiang Zhuang",
      "Xianzhong Zhang",
      "Hongwu Liu",
      "Zhide Guo"
    ],
    "doi": "10.1021/acs.jmedchem.5c02016",
    "journal": "Journal of Medicinal Chemistry",
    "year": 2025,
    "synthesis_scale": "preclinical",
    "method_completeness": "full",
    "has_synthesis": true,
    "extraction_notes": "PR7, DP2, DP3, and NP2 were custom synthesised externally (Nanchang Tanzhen Biotechnology Co., Ltd.) and full SPPS routes are shown in SI Schemes S1–S4; individual coupling step quantities are not provided for these custom-synthesised compounds. DP1 and NP1 were synthesised in-house with full procedural detail. All five radiotracers were prepared in-house with full procedural detail."
  },

  "compounds": [
    {
      "id": "C01",
      "name": "PR7",
      "iupac_name": null,
      "molecular_formula": "C96H133N25O31",
      "role": "starting_material",
      "is_newly_synthesized": true,
      "source": "custom synthesis, Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ = 1067.47",
      "ms_calculated_exact_mass": 2131.96,
      "description": "ROR1-targeting linear peptide lead compound used as the starting material for conjugation to DOTA-NHS (to give DP1) and NOTA-NHS (to give NP1); also synthesised via SPPS as shown in SI Scheme S1."
    },
    {
      "id": "C02",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ = 1260.54, [M+3H]3+ = 840.68",
      "ms_calculated_exact_mass": 2518.14,
      "description": "DOTA-conjugated linear peptide precursor prepared by coupling PR7 with DOTA-NHS; serves as the chelating precursor for 68Ga radiolabeling to give [68Ga]Ga-DP1."
    },
    {
      "id": "C03",
      "name": "NP1",
      "iupac_name": null,
      "molecular_formula": "C108H152N28O36",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ = 1210.22, [M+3H]3+ = 807.00",
      "ms_calculated_exact_mass": 2417.09,
      "description": "NOTA-conjugated linear peptide precursor prepared by coupling PR7 with NOTA-NHS; serves as the chelating precursor for AlF-18F radiolabeling to give [18F]AlF-NP1."
    },
    {
      "id": "C04",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "custom synthesis, Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ = 1373.07, [M+3H]3+ = 915.72",
      "ms_calculated_exact_mass": 2743.2514,
      "description": "DOTA-containing cyclic peptide precursor (P2+L1+R3 architecture) synthesised by SPPS and on-resin cyclization; serves as precursor for [68Ga]Ga-DP2."
    },
    {
      "id": "C05",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "custom synthesis, Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ = 1509.05, [M+3H]3+ = 1006.39",
      "ms_calculated_exact_mass": 3015.2514,
      "description": "DOTA-containing cyclic disulfide-bridged peptide precursor (P2+L2+R3 architecture) synthesised by SPPS and thioether cyclization; serves as precursor for [68Ga]Ga-DP3."
    },
    {
      "id": "C06",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "custom synthesis, Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ = 1322.56",
      "ms_calculated_exact_mass": 2642.20,
      "description": "NOTA-containing cyclic peptide precursor (P2+L1+R2 architecture) synthesised by SPPS and on-resin cyclization; serves as precursor for [18F]AlF-NP2."
    },
    {
      "id": "C07",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "custom synthesis, Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "N-hydroxysuccinimide ester of DOTA used as the chelator coupling reagent for conjugation to PR7 to yield DP1."
    },
    {
      "id": "C08",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "custom synthesis, Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "N-hydroxysuccinimide ester of NOTA used as the chelator coupling reagent for conjugation to PR7 to yield NP1."
    },
    {
      "id": "C09",
      "name": "DIPEA",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Diisopropylethylamine base used in the conjugation of PR7 with DOTA-NHS or NOTA-NHS and in SPPS steps."
    },
    {
      "id": "C10",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "68Ga-labeled DOTA-linear peptide radiotracer targeting ROR1; final radiopharmaceutical prepared by heating DP1 with 68GaCl3 in sodium acetate buffer and purifying on SepPak C18."
    },
    {
      "id": "C11",
      "name": "[68Ga]Ga-DP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "68Ga-labeled DOTA-cyclic peptide radiotracer targeting ROR1; prepared analogously to [68Ga]Ga-DP1 using DP2 as precursor."
    },
    {
      "id": "C12",
      "name": "[68Ga]Ga-DP3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "68Ga-labeled DOTA-disulfide-cyclic peptide radiotracer targeting ROR1; prepared analogously to [68Ga]Ga-DP1 using DP3 as precursor."
    },
    {
      "id": "C13",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "18F-AlF-labeled NOTA-linear peptide radiotracer targeting ROR1; prepared by combining QMA-trapped [18F]fluoride with AlCl3 and NP1 precursor in sodium acetate/acetonitrile, heating at 100°C, then purifying on SepPak C18."
    },
    {
      "id": "C14",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "18F-AlF-labeled NOTA-cyclic peptide radiotracer targeting ROR1; prepared analogously to [18F]AlF-NP1 using NP2 as precursor."
    },
    {
      "id": "C15",
      "name": "68GaCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "68Ge-68Ga generator (ITM)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Gallium-68 chloride radionuclide source obtained from a 68Ge/68Ga generator, used for radiolabeling of DOTA-peptide precursors DP1, DP2, and DP3."
    },
    {
      "id": "C16",
      "name": "Fluoride-18 ([18F]F-)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Cyclone 18/9 cyclotron (IBA), Center for Molecular Imaging and Translational Medicine, Xiamen University",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fluoride-18 radionuclide source produced by 18O(p,n)18F reaction, used for AlF radiolabeling of NOTA-peptide precursors NP1 and NP2."
    },
    {
      "id": "C17",
      "name": "Aluminum chloride (AlCl3)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Aluminum(III) chloride used as the aluminum source to form the AlF chelate complex with 18F and the NOTA-peptide precursors NP1 and NP2."
    },
    {
      "id": "C18",
      "name": "Sodium acetate buffer (0.25 M, pH 6.5)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Sodium acetate solution used to adjust the pH of the 68GaCl3 solution to pH 4–4.5 prior to radiolabeling of DOTA-peptide precursors."
    },
    {
      "id": "C19",
      "name": "Sodium acetate buffer (0.1 M, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Sodium acetate buffer used in the AlF-18F radiolabeling reaction mixture for NP1 and NP2."
    },
    {
      "id": "C20",
      "name": "Rink Amide MBHA Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solid support resin used for Fmoc SPPS synthesis of PR7 (Scheme S1); provides C-terminal amide upon TFA cleavage."
    },
    {
      "id": "C21",
      "name": "Fmoc-Phe-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-protected phenylalanine amino acid building block used in Step 1 of PR7 SPPS and in SPPS steps of DP2, DP3, and NP2."
    },
    {
      "id": "C22",
      "name": "HOBt",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "1-Hydroxybenzotriazole coupling additive used in SPPS coupling steps for PR7, DP2, DP3, and NP2."
    },
    {
      "id": "C23",
      "name": "DIC",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "N,N'-Diisopropylcarbodiimide coupling reagent used in SPPS coupling steps for PR7, DP2, DP3, and NP2."
    },
    {
      "id": "C24",
      "name": "Piperidine (20% in DMF)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base solution used for Fmoc deprotection in all SPPS sequences (PR7, DP2, DP3, NP2)."
    },
    {
      "id": "C25",
      "name": "TFA",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Trifluoroacetic acid used for global deprotection and resin cleavage to release peptide products from solid support in SPPS of PR7, DP2, DP3, and NP2."
    },
    {
      "id": "C26",
      "name": "CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "2-Chlorotrityl chloride resin solid support used for Fmoc SPPS of DP2, DP3, and NP2; allows mild cleavage to preserve side-chain protecting groups for on-resin cyclization."
    },
    {
      "id": "C27",
      "name": "Fmoc-Gly-Gly-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-protected dipeptide used as the first building block loaded onto CTC resin in SPPS of DP2 and NP2 (Step 1 of Schemes S2 and S4)."
    },
    {
      "id": "C28",
      "name": "Dde-Lys(Fmoc)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Orthogonally protected lysine building block used in Step 2 of DP2 and NP2 SPPS to introduce the branching point for DOTA/NOTA chelator attachment."
    },
    {
      "id": "C29",
      "name": "HBTU",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling reagent used in Steps 2 and 3 of the DP2 SPPS (Scheme S2) for Dde-Lys(Fmoc)-OH coupling and DOTA(3tBu) attachment."
    },
    {
      "id": "C30",
      "name": "NMM",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "N-Methylmorpholine base used as auxiliary base in HBTU-mediated coupling steps in the SPPS of DP2."
    },
    {
      "id": "C31",
      "name": "DOTA(3tBu)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Tri-tert-butyl ester protected DOTA chelator activated with HATU/NMM and coupled to the Lys epsilon-amine on resin in Step 3 of DP2 SPPS (Scheme S2)."
    },
    {
      "id": "C32",
      "name": "HATU",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling reagent used in Steps 3 of DP2 SPPS and Step 3 of NP2 SPPS for DOTA(3tBu)/NOTA(2tBu) attachment to the lysine side chain on resin."
    },
    {
      "id": "C33",
      "name": "5% N2H4 in H2O/DMF",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Hydrazine solution used to remove the Dde protecting group from the lysine epsilon-amine after DOTA/NOTA attachment in Step 3 of DP2 and NP2 SPPS."
    },
    {
      "id": "C34",
      "name": "1% TFA in DCM",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Dilute TFA solution used for mild cleavage of the fully protected peptide from the CTC resin in Step 6 of DP2 and NP2 SPPS."
    },
    {
      "id": "C35",
      "name": "DPPA",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Diphenylphosphoryl azide used as the macrolactamization/cyclization reagent in Step 7 of DP2 and NP2 SPPS (Schemes S2 and S4) to form the cyclic peptide backbone."
    },
    {
      "id": "C36",
      "name": "Fmoc-Cys(Trt)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-cysteine(Trt) building block used for loading onto CTC resin and for incorporation into DP3 sequence in Scheme S3."
    },
    {
      "id": "C37",
      "name": "Acetic anhydride",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Capping reagent used in Step 3 of DP3 SPPS (Scheme S3) to cap unreacted amines during iterative coupling cycles."
    },
    {
      "id": "C38",
      "name": "1,3-bis(bromomethyl)benzene",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Dibromo crosslinker reacted with the bis-cysteine linear peptide and cysteamine in Step 5 of DP3 SPPS (Scheme S3) to form the thioether-cyclized DP3 scaffold."
    },
    {
      "id": "C39",
      "name": "Cysteamine (HS-CH2-CH2-NH2)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Thiol-amine bifunctional linker reacted with 1,3-bis(bromomethyl)benzene and the linear bis-Cys peptide in Step 5 of DP3 SPPS (Scheme S3) to form the DP3 cyclized scaffold."
    },
    {
      "id": "C40",
      "name": "NH4HCO3/ACN",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Ammonium bicarbonate in acetonitrile used as the reaction medium for Steps 5 and 6 of DP3 SPPS (thioether crosslinking and DOTA conjugation, Scheme S3)."
    },
    {
      "id": "C41",
      "name": "NOTA(2tBu)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Di-tert-butyl ester protected NOTA chelator coupled to the Lys epsilon-amine on resin via HATU/DIPEA in Step 3 of NP2 SPPS (Scheme S4)."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of PR7 (SI Scheme S1)",
      "source_section": "SI_scheme_S1",
      "target_compound_id": "C01",
      "target_compound_name": "PR7",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Fmoc SPPS – first amino acid loading",
          "reactants": [
            {
              "compound_id": "C20",
              "name": "Rink Amide MBHA Resin",
              "amount": null
            },
            {
              "compound_id": "C21",
              "name": "Fmoc-Phe-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C22",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C23",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C09",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Standard Fmoc SPPS loading of Fmoc-Phe-OH onto Rink Amide MBHA Resin."
          },
          "product": {
            "compound_id": null,
            "name": "H-Phe-Rink Amide MBHA Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Step 1 of Scheme S1. Individual coupling amounts not provided for this custom-synthesized compound. Fmoc deprotection with 20% piperidine/DMF follows each coupling (incorporated in Step 2 label)."
        },
        {
          "step_number": 2,
          "reaction_type": "Fmoc SPPS – iterative chain elongation (17 residues)",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Phe-Rink Amide MBHA Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Fmoc-Asp(OtBu)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Fmoc-Gly-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Fmoc-Trp(Boc)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Fmoc-Tyr(tBu)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Fmoc-Thr(tBu)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Fmoc-Ser(tBu)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Fmoc-Tyr(tBu)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Fmoc-Gly-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Fmoc-Pro-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Fmoc-Ile-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Fmoc-Gln(Trt)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Fmoc-Arg(Pbf)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Fmoc-Asp(OtBu)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Fmoc-Asn(Trt)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Fmoc-Ile-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Fmoc-Asp(OtBu)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Fmoc-Ser(tBu)-OH",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C22",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C23",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C24",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Iterative Fmoc deprotection/coupling cycles to assemble the 17-residue sequence H-Ser(tBu)-Asp(OtBu)-Ile-Asn(Trt)-Asp(OtBu)-Arg(Pbf)-Gln(Trt)-Ile-Pro-Gly-Tyr(tBu)-Ser(tBu)-Thr(tBu)-Tyr(tBu)-Trp(Boc)-Gly-Asp(OtBu)-Phe-Rink Amide MBHA Resin."
          },
          "product": {
            "compound_id": null,
            "name": "Protected 17-mer peptide-Rink Amide MBHA Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Residue order listed in Scheme S1 (residues 1–17 from C- to N-terminus). Individual coupling amounts not provided."
        },
        {
          "step_number": 3,
          "reaction_type": "Global deprotection and resin cleavage",
          "reactants": [
            {
              "compound_id": null,
              "name": "Protected 17-mer peptide-Rink Amide MBHA Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C25",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "TFA cleavage cocktail removes all protecting groups and releases peptide amide from resin."
          },
          "product": {
            "compound_id": "C01",
            "name": "PR7",
            "yield": null,
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 10.642
          },
          "purification": "semipreparative HPLC; mobile phase 0.1% TFA/H2O (A) and 0.1% TFA/MeCN (B), 23% B to 43% B over 20 min, 1 mL/min",
          "notes": "Yield not reported for this custom-synthesised compound. ESI-MS calcd for C96H133N25O31: 2131.96; found [M+2H]2+ = 1067.47."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of DP2 (SI Scheme S2)",
      "source_section": "SI_scheme_S2",
      "target_compound_id": "C04",
      "target_compound_name": "DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Fmoc SPPS – dipeptide loading onto CTC resin",
          "reactants": [
            {
              "compound_id": "C26",
              "name": "CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C27",
              "name": "Fmoc-Gly-Gly-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C09",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "H-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Fmoc deprotection with 20% piperidine/DMF follows loading. Amounts not provided for this custom-synthesised compound."
        },
        {
          "step_number": 2,
          "reaction_type": "Fmoc SPPS – Dde-Lys(Fmoc) coupling",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C28",
              "name": "Dde-Lys(Fmoc)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C29",
              "name": "HBTU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C30",
              "name": "NMM",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C24",
              "name": "20% piperidine/DMF",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Dde-Lys-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Fmoc deprotection after coupling to reveal alpha-amine for next step."
        },
        {
          "step_number": 3,
          "reaction_type": "On-resin DOTA(3tBu) conjugation and Dde removal",
          "reactants": [
            {
              "compound_id": null,
              "name": "Dde-Lys-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C31",
              "name": "DOTA(3tBu)",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C32",
              "name": "HATU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C30",
              "name": "NMM",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C33",
              "name": "5% N2H4 in H2O/DMF",
              "amount": null,
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "DOTA(3tBu) coupled to Lys epsilon-amine; Dde removed with 5% N2H4/H2O/DMF."
          },
          "product": {
            "compound_id": null,
            "name": "H-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "Fmoc SPPS – Fmoc-Phe-OH coupling",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C21",
              "name": "Fmoc-Phe-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C22",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C23",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C24",
              "name": "20% piperidine/DMF",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "H-Phe-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Fmoc deprotection after coupling."
        },
        {
          "step_number": 5,
          "reaction_type": "Fmoc SPPS – iterative chain elongation (17 residues)",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Phe-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Fmoc amino acids (Asp(OtBu), Gly, Trp(Boc), Tyr(tBu), Thr(tBu), Ser(tBu), Tyr(tBu), Gly, Pro, Ile, Gln(Trt), Arg(Pbf), Asp(OtBu), Asn(Trt), Ile, Asp(OtBu), Ser(tBu)) coupled sequentially",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C22",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C23",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C24",
              "name": "20% piperidine/DMF",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Fully protected linear peptide sequence assembled by repeat of Step 4 coupling/deprotection cycles."
          },
          "product": {
            "compound_id": null,
            "name": "Protected 17-mer peptide-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Residues listed in Scheme S2 (1–17 as in PR7 sequence)."
        },
        {
          "step_number": 6,
          "reaction_type": "Mild acid cleavage from CTC resin (protecting groups retained)",
          "reactants": [
            {
              "compound_id": null,
              "name": "Protected peptide-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C34",
              "name": "1% TFA in DCM",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DCM",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Mild cleavage preserves all side-chain protecting groups to allow solution-phase cyclization."
          },
          "product": {
            "compound_id": null,
            "name": "Protected linear peptide-Lys[DOTA(3tBu)]-Gly-Gly (fully protected, free C- and N-termini)",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 7,
          "reaction_type": "Solution-phase macrolactamization and global deprotection (TFA)",
          "reactants": [
            {
              "compound_id": null,
              "name": "Protected linear peptide for cyclization",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C35",
              "name": "DPPA",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C09",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C25",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "DPPA/DIPEA/DMF for head-to-tail macrolactamization, then TFA for global deprotection."
          },
          "product": {
            "compound_id": "C04",
            "name": "DP2",
            "yield": null,
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 10.328
          },
          "purification": "semipreparative HPLC; mobile phase 0.1% TFA/H2O (A) and 0.1% TFA/MeCN (B), 23% B to 43% B over 20 min, 1 mL/min",
          "notes": "Yield not reported for this custom-synthesised compound. ESI-MS calcd for C122H174N32O41: 2743.2514; found [M+2H]2+ = 1373.07, [M+3H]3+ = 915.72."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Synthesis of DP3 (SI Scheme S3)",
      "source_section": "SI_scheme_S3",
      "target_compound_id": "C05",
      "target_compound_name": "DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Fmoc SPPS – Fmoc-Cys(Trt) loading onto CTC resin",
          "reactants": [
            {
              "compound_id": "C26",
              "name": "CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C36",
              "name": "Fmoc-Cys(Trt)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C09",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C24",
              "name": "20% piperidine/DMF",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "H-Cys(Trt)-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Amounts not provided for this custom-synthesised compound."
        },
        {
          "step_number": 2,
          "reaction_type": "Fmoc SPPS – Fmoc-Phe-OH coupling",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Cys(Trt)-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C21",
              "name": "Fmoc-Phe-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C22",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C23",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C24",
              "name": "20% piperidine/DMF",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "H-Phe-Cys(Trt)-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Fmoc SPPS – iterative chain elongation (20 residues including second Cys)",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Phe-Cys(Trt)-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Fmoc amino acids (Asp(OtBu), Gly, Trp(Boc), Tyr(tBu), Thr(tBu), Ser(tBu), Tyr(tBu), Gly, Pro, Ile, Gln(Trt), Arg(Pbf), Asp(OtBu), Asn(Trt), Ile, Ser(tBu), Gly, Cys(Trt), and acetic anhydride cap) coupled sequentially",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C22",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C23",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C24",
              "name": "20% piperidine/DMF",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C37",
              "name": "Acetic anhydride",
              "amount": null,
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Iterative coupling/deprotection to build the 20-residue bis-Cys linear sequence Ac-Cys(Trt)-Gly-Ser(tBu)-Asp(OtBu)-Ile-Asn(Trt)-Asp(OtBu)-Arg(Pbf)-Gln(Trt)-Ile-Pro-Gly-Tyr(tBu)-Ser(tBu)-Thr(tBu)-Tyr(tBu)-Trp(Boc)-Gly-Asp(OtBu)-Phe-Cys(Trt)-CTC Resin."
          },
          "product": {
            "compound_id": null,
            "name": "Protected 20-mer bis-Cys(Trt) peptide-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Residue sequence read from Scheme S3."
        },
        {
          "step_number": 4,
          "reaction_type": "Global deprotection and resin cleavage (TFA)",
          "reactants": [
            {
              "compound_id": null,
              "name": "Protected 20-mer bis-Cys(Trt) peptide-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C25",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Standard TFA cocktail removes all protecting groups and cleaves from resin; free bis-Cys linear peptide obtained."
          },
          "product": {
            "compound_id": null,
            "name": "Deprotected bis-Cys linear peptide",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "Thioether cyclization with 1,3-bis(bromomethyl)benzene and cysteamine",
          "reactants": [
            {
              "compound_id": null,
              "name": "Deprotected bis-Cys linear peptide",
              "amount": null
            },
            {
              "compound_id": "C38",
              "name": "1,3-bis(bromomethyl)benzene",
              "amount": null
            },
            {
              "compound_id": "C39",
              "name": "Cysteamine (HS-CH2-CH2-NH2)",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C40",
              "name": "NH4HCO3/ACN",
              "amount": null,
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile/NH4HCO3 buffer",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Thioalkylation of both Cys thiol groups with the dibromo scaffold and cysteamine linker to form cyclized bis-thioether peptide."
          },
          "product": {
            "compound_id": null,
            "name": "Thioether-cyclized DP3 precursor (before DOTA attachment)",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Cysteamine serves as linker providing a free amine for subsequent DOTA conjugation."
        },
        {
          "step_number": 6,
          "reaction_type": "DOTA conjugation to cyclic scaffold amine",
          "reactants": [
            {
              "compound_id": null,
              "name": "Thioether-cyclized DP3 precursor",
              "amount": null
            },
            {
              "compound_id": "C31",
              "name": "DOTA(3tBu)",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C40",
              "name": "NH4HCO3/ACN",
              "amount": null,
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile/NH4HCO3 buffer",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "DOTA tBu ester conjugated to cysteamine amine of the cyclized scaffold; tBu groups removed during TFA workup (implied)."
          },
          "product": {
            "compound_id": "C05",
            "name": "DP3",
            "yield": null,
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 10.404
          },
          "purification": "semipreparative HPLC; mobile phase 0.1% TFA/H2O (A) and 0.1% TFA/MeCN (B), 23% B to 43% B over 20 min, 1 mL/min",
          "notes": "Yield not reported. ESI-MS calcd for C133H186N32O43S3: 3015.2514; found [M+2H]2+ = 1509.05, [M+3H]3+ = 1006.39. Exact TFA deprotection step for DOTA tBu esters not explicitly labelled as separate step in Scheme S3 but implied."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Synthesis of NP2 (SI Scheme S4)",
      "source_section": "SI_scheme_S4",
      "target_compound_id": "C06",
      "target_compound_name": "NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Fmoc SPPS – dipeptide loading onto CTC resin",
          "reactants": [
            {
              "compound_id": "C26",
              "name": "CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C27",
              "name": "Fmoc-Gly-Gly-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C09",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C24",
              "name": "20% piperidine/DMF",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "H-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Amounts not provided for this custom-synthesised compound."
        },
        {
          "step_number": 2,
          "reaction_type": "Fmoc SPPS – Dde-Lys(Fmoc) coupling",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C28",
              "name": "Dde-Lys(Fmoc)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C29",
              "name": "HBTU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C09",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C24",
              "name": "20% piperidine/DMF",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Dde-Lys-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "On-resin NOTA(2tBu) conjugation and Dde removal",
          "reactants": [
            {
              "compound_id": null,
              "name": "Dde-Lys-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C41",
              "name": "NOTA(2tBu)",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C32",
              "name": "HATU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C09",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C33",
              "name": "5% N2H4 in H2O/DMF",
              "amount": null,
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "NOTA(2tBu) coupled to Lys epsilon-amine via HATU/DIPEA; Dde removed with 5% N2H4/H2O/DMF."
          },
          "product": {
            "compound_id": null,
            "name": "H-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "Fmoc SPPS – Fmoc-Phe-OH coupling",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C21",
              "name": "Fmoc-Phe-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C22",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C23",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C24",
              "name": "20% piperidine/DMF",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "H-Phe-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "Fmoc SPPS – iterative chain elongation (17 residues)",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Phe-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Fmoc amino acids (Asp(OtBu), Gly, Trp(Boc), Tyr(tBu), Thr(tBu), Ser(Trt), Tyr(tBu), Gly, Pro, Ile, Gln(Trt), Arg(Pbf), Asp(OtBu), Asn(Trt), Ile, Asp(OtBu), Ser(tBu)) coupled sequentially",
              "amount": null,
              "role": "other"
            },
            {
              "compound_id": "C22",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C23",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C24",
              "name": "20% piperidine/DMF",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Repeat of Step 4 for each residue to assemble the full 17-residue sequence."
          },
          "product": {
            "compound_id": null,
            "name": "Protected 17-mer peptide-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Ser(Trt) noted in Scheme S4 residue 6 position."
        },
        {
          "step_number": 6,
          "reaction_type": "Mild acid cleavage from CTC resin (protecting groups retained)",
          "reactants": [
            {
              "compound_id": null,
              "name": "Protected peptide-NOTA-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C34",
              "name": "1% TFA in DCM",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DCM",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Mild cleavage retains side-chain protecting groups for solution-phase cyclization."
          },
          "product": {
            "compound_id": null,
            "name": "Protected linear peptide for NP2 cyclization",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 7,
          "reaction_type": "Solution-phase macrolactamization and global deprotection (TFA)",
          "reactants": [
            {
              "compound_id": null,
              "name": "Protected linear peptide for NP2 cyclization",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C35",
              "name": "DPPA",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C09",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C25",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "DPPA/DIPEA/DMF for head-to-tail macrolactamization, then TFA for global deprotection."
          },
          "product": {
            "compound_id": "C06",
            "name": "NP2",
            "yield": null,
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 10.620
          },
          "purification": "semipreparative HPLC; mobile phase 0.1% TFA/H2O (A) and 0.1% TFA/MeCN (B), 23% B to 43% B over 20 min, 1 mL/min",
          "notes": "Yield not reported. ESI-MS calcd for C118H167N31O39: 2642.20; found [M+2H]2+ = 1322.56."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Synthesis of DP1 (SI Scheme S5 / main text Section 5.2.1)",
      "source_section": "SI_scheme_S5",
      "target_compound_id": "C02",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling (chelator conjugation)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 umol)"
            },
            {
              "compound_id": "C07",
              "name": "DOTA-NHS",
              "amount": "2.5 mg (5 umol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C09",
              "name": "DIPEA",
              "amount": "20 uL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 uL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "12 h",
            "atmosphere": null,
            "ph": null,
            "other": "Reaction performed in a 2 mL centrifugation tube with oscillator agitation."
          },
          "product": {
            "compound_id": "C02",
            "name": "DP1",
            "yield": "4.2 mg (55.6%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 11.230
          },
          "purification": "semipreparative HPLC, UV detection at 254 nm; mobile phase 0.1% TFA/H2O (A) and 0.1% TFA/MeCN (B), 5% B to 95% B over 20 min, 1 mL/min; lyophilization",
          "notes": "ESI-MS calcd for C112H159N29O38: 2518.14; found [M+2H]2+ = 1260.54, [M+3H]3+ = 840.68."
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Synthesis of NP1 (SI Scheme S5 / main text Section 5.2.1)",
      "source_section": "SI_scheme_S5",
      "target_compound_id": "C03",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling (chelator conjugation)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 umol)"
            },
            {
              "compound_id": "C08",
              "name": "NOTA-NHS",
              "amount": "2 mg (5 umol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C09",
              "name": "DIPEA",
              "amount": "20 uL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 uL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "12 h",
            "atmosphere": null,
            "ph": null,
            "other": "Reaction performed in a 2 mL centrifugation tube with oscillator agitation."
          },
          "product": {
            "compound_id": "C03",
            "name": "NP1",
            "yield": "3.9 mg (54%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 12.780
          },
          "purification": "semipreparative HPLC, UV detection at 254 nm; mobile phase 0.1% TFA/H2O (A) and 0.1% TFA/MeCN (B), 5% B to 95% B over 20 min, 1 mL/min; lyophilization",
          "notes": "ESI-MS calcd for C108H152N28O36: 2417.09; found [M+2H]2+ = 1210.22, [M+3H]3+ = 807.00."
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP1, [68Ga]Ga-DP2, [68Ga]Ga-DP3, [18F]AlF-NP1, and [18F]AlF-NP2 (main text Section 5.4)",
      "source_section": "main_text",
      "target_compound_id": "C10",
      "target_compound_name": "[68Ga]Ga-DP1, [68Ga]Ga-DP2, [68Ga]Ga-DP3 (68Ga series); [18F]AlF-NP1, [18F]AlF-NP2 (18F series)",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3 with sodium acetate",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C18",
              "name": "Sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "68GaCl3-sodium acetate solution pH 4–4.5",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Applied to preparation of [68Ga]Ga-DP1, [68Ga]Ga-DP2, and [68Ga]Ga-DP3."
        },
        {
          "step_number": 2,
          "reaction_type": "68Ga radiolabeling of DOTA-peptide precursor",
          "reactants": [
            {
              "compound_id": null,
              "name": "68GaCl3-sodium acetate solution pH 4–4.5",
              "amount": "1.5 mL"
            },
            {
              "compound_id": "C02",
              "name": "DP1 (or DP2 or DP3) precursor in DMSO",
              "amount": "50 ug (16–20 nmol) in 50 uL DMSO"
            }
          ],
          "reagents": [],
          "solvents": [],
          "conditions": {
            "temperature": "95°C",
            "time": "20 min",
            "atmosphere": null,
            "ph": "4–4.5",
            "other": "After heating, cooled to RT before purification."
          },
          "product": {
            "compound_id": "C10",
            "name": "[68Ga]Ga-DP1 (or [68Ga]Ga-DP2 / [68Ga]Ga-DP3)",
            "yield": "89.55 ± 0.12% ([68Ga]Ga-DP1); 97.67 ± 1.05% ([68Ga]Ga-DP2); 98.01 ± 0.97% ([68Ga]Ga-DP3)",
            "purity": ">95% RCP by radio-HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters), eluted with 1.5 mL ethanol",
          "notes": "Product IDs C10 (DP1), C11 (DP2), C12 (DP3) represent the three 68Ga radiolabeled products prepared by this identical procedure applied to each precursor. HPLC radio-purity method: 0.1% TFA/H2O (A) and 0.1% TFA/MeCN (B), 5% B to 95% B over 20 min, 1 mL/min. RCP values from Table S1: [68Ga]Ga-DP1: 92.56 ± 0.02%; [68Ga]Ga-DP2: 99.45 ± 0.01%; [68Ga]Ga-DP3: 98.46 ± 0.05%."
        },
        {
          "step_number": 3,
          "reaction_type": "QMA trapping of [18F]fluoride",
          "reactants": [
            {
              "compound_id": "C16",
              "name": "Fluoride-18 ([18F]F-)",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline (10 mL for conditioning), pure water (10 mL for conditioning)",
              "volume": "10 mL each"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "QMA cartridge preconditioned with 10 mL saline then 10 mL water; [18F]fluoride trapped on cartridge, then eluted with 0.2 mL saline into reaction vial."
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride in 0.2 mL saline",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Applied to preparation of [18F]AlF-NP1 and [18F]AlF-NP2."
        },
        {
          "step_number": 4,
          "reaction_type": "AlF-18F complexation and NOTA-peptide radiolabeling",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride in 0.2 mL saline",
              "amount": "0.2 mL"
            },
            {
              "compound_id": "C03",
              "name": "NP1 (or NP2) precursor in DMSO",
              "amount": "50 ug (18–25 nmol) in 50 uL DMSO"
            }
          ],
          "reagents": [
            {
              "compound_id": "C17",
              "name": "Aluminum chloride (AlCl3) in sodium acetate buffer (2 mM)",
              "amount": "3 uL",
              "role": "other"
            },
            {
              "compound_id": "C19",
              "name": "Sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "100 uL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": "200 uL"
            }
          ],
          "conditions": {
            "temperature": "100°C",
            "time": "20 min",
            "atmosphere": null,
            "ph": null,
            "other": "After heating, cooled to RT; ethanol solvent removed after SepPak purification and final product dissolved in saline."
          },
          "product": {
            "compound_id": "C13",
            "name": "[18F]AlF-NP1 (or [18F]AlF-NP2)",
            "yield": "62.58 ± 0.32% ([18F]AlF-NP1); 62.76 ± 0.22% ([18F]AlF-NP2)",
            "purity": ">95% RCP by radio-HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge, eluted with 1.5 mL ethanol; ethanol evaporated; product reconstituted in saline",
          "notes": "Product IDs C13 ([18F]AlF-NP1) and C14 ([18F]AlF-NP2) represent the two 18F radiolabeled products prepared by this identical procedure. HPLC radio-purity method: 0.1% TFA/H2O (A) and 0.1% TFA/MeCN (B), 5% B to 95% B over 20 min, 1 mL/min. RCP values from Table S1: [18F]AlF-NP1: 99.46 ± 0.15%; [18F]AlF-NP2: 99.56 ± 0.04%."
        }
      ]
    }
  ]
}
```
##### Attempt 3
```
{
  "extraction": {
    "prompt_version": "v3.2",
    "extraction_date": "2026-03-31",
    "model_name": "claude-sonnet-4-6",
    "extractor_notes": "SI found: jm5c02016_si_001.pdf. SI schemes identified: Scheme S1 (synthesis of PR7), Scheme S2 (synthesis of DP2), Scheme S3 (synthesis of DP3), Scheme S4 (synthesis of NP2), Scheme S5 (synthesis of DP1 and NP1). SI compounds identified: no author-labeled S-series compounds; all SI schemes produce main-text named compounds (PR7, DP1, DP2, DP3, NP1, NP2). Total pathway count: 8 (P1=PR7 via Scheme S1, P2=DP2 via Scheme S2, P3=DP3 via Scheme S3, P4=NP2 via Scheme S4, P5=DP1 via Scheme S5/main text, P6=NP1 via Scheme S5/main text, P7=[68Ga]Ga-DP1/DP2/DP3 radiolabeling, P8=[18F]AlF-NP1/NP2 radiolabeling). Excluded reference compounds: none (all named compounds in the study have synthetic roles). Mass type notes: All precursor compounds are large peptides (MW 2100-3100 Da); MS values reported are multiply-charged ESI ions ([M+2H]2+, [M+3H]3+) consistent with monoisotopic or average mass assignments for peptides of this size; calculated exact masses are explicitly stated in the paper and SI schemes and are recorded. Procedural gap: The main text section 5.2 states 'synthetic routes are described in Schemes S1-S5' but provides full narrative procedure only for DP1 and NP1 (section 5.2.1) and states PR7, DP2, DP3, NP2 were custom synthesized externally (section 5.2.2). The SI Schemes S1-S4 show the synthetic routes for PR7, DP2, DP3, and NP2 respectively as they were performed by the custom synthesis vendor; these are schematic routes with reagents shown on arrows but no narrative experimental procedures (amounts, times, temperatures) are provided for individual steps. Scheme S3 for DP3 involves a thiol-alkylation cyclization using a dibromomethylbenzene linker; an intermediate linear peptide is implied. For the 68Ga and 18F radiolabeling pathways, DP1/DP2/DP3 share a single procedure (P7) and NP1/NP2 share a single procedure (P8); separate pathway entries are created per Rule 14 targeting each distinct radiolabeled product."
  },

  "paper": {
    "title": "18F-/68Ga-Labeled Peptide-Based Probes for PET Imaging of ROR1 Expression",
    "authors": [
      "Tao Yang",
      "Jiahui Sun",
      "Guolong Huang",
      "Hong Wang",
      "Zhexin He",
      "Siying Lin",
      "Yanjie Wang",
      "Rongqiang Zhuang",
      "Xianzhong Zhang",
      "Hongwu Liu",
      "Zhide Guo"
    ],
    "doi": "10.1021/acs.jmedchem.5c02016",
    "journal": "Journal of Medicinal Chemistry",
    "year": 2025,
    "synthesis_scale": "preclinical",
    "method_completeness": "partial",
    "has_synthesis": true,
    "extraction_notes": "Full narrative experimental procedures available only for DP1 and NP1 synthesis (section 5.2.1) and the radiolabeling procedures (section 5.4). PR7, DP2, DP3, and NP2 were custom-synthesized externally; their SI Schemes show schematic routes without narrative step-level detail (amounts/times/temperatures not given). Radiolabeling of DP1/DP2/DP3 uses the same procedure; NP1/NP2 use the same AlF-18F procedure."
  },

  "compounds": [
    {
      "id": "C01",
      "name": "PR7",
      "iupac_name": null,
      "molecular_formula": "C96H133N25O31",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "custom synthesis / Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ = 1067.47",
      "ms_calculated_exact_mass": 2131.96,
      "description": "ROR1-targeting linear peptide lead compound; externally custom-synthesized; serves as the starting substrate for conjugation to DOTA-NHS or NOTA-NHS to produce DP1 and NP1; also used as a blocking agent in biological assays."
    },
    {
      "id": "C02",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "N-hydroxysuccinimide ester of DOTA chelator; used as coupling reagent in the synthesis of DP1 from PR7."
    },
    {
      "id": "C03",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "N-hydroxysuccinimide ester of NOTA chelator; used as coupling reagent in the synthesis of NP1 from PR7."
    },
    {
      "id": "C04",
      "name": "DIPEA",
      "iupac_name": "N,N-diisopropylethylamine",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Hünig's base; used as non-nucleophilic base in DP1/NP1 conjugation reaction and in SPPS steps for DP2, DP3, NP2 synthesis."
    },
    {
      "id": "C05",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ = 1260.54, [M+3H]3+ = 840.68",
      "ms_calculated_exact_mass": 2518.14,
      "description": "DOTA-conjugated linear ROR1-targeting peptide precursor synthesized in-house from PR7 and DOTA-NHS; serves as precursor for 68Ga radiolabeling to give [68Ga]Ga-DP1."
    },
    {
      "id": "C06",
      "name": "NP1",
      "iupac_name": null,
      "molecular_formula": "C108H152N28O36",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ = 1210.22, [M+3H]3+ = 807.00",
      "ms_calculated_exact_mass": 2417.09,
      "description": "NOTA-conjugated linear ROR1-targeting peptide precursor synthesized in-house from PR7 and NOTA-NHS; serves as precursor for AlF-18F radiolabeling to give [18F]AlF-NP1."
    },
    {
      "id": "C07",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "intermediate",
      "is_newly_synthesized": false,
      "source": "custom synthesis / Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ = 1373.07, [M+3H]3+ = 915.72",
      "ms_calculated_exact_mass": 2743.2514,
      "description": "DOTA-conjugated cyclic ROR1-targeting peptide precursor externally custom-synthesized via SPPS and on-resin DOTA incorporation followed by cyclization and TFA deprotection; serves as precursor for [68Ga]Ga-DP2."
    },
    {
      "id": "C08",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "intermediate",
      "is_newly_synthesized": false,
      "source": "custom synthesis / Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ = 1509.05, [M+3H]3+ = 1006.39",
      "ms_calculated_exact_mass": 3015.2514,
      "description": "DOTA-conjugated disulfide/thioether-cyclized ROR1-targeting peptide precursor externally custom-synthesized via SPPS with Cys-containing sequence, TFA deprotection, thiol-alkylation cyclization using dibromomethylbenzene linker, and DOTA conjugation; serves as precursor for [68Ga]Ga-DP3."
    },
    {
      "id": "C09",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "intermediate",
      "is_newly_synthesized": false,
      "source": "custom synthesis / Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ = 1322.56",
      "ms_calculated_exact_mass": 2642.20,
      "description": "NOTA-conjugated cyclic ROR1-targeting peptide precursor externally custom-synthesized via SPPS with on-resin NOTA incorporation and cyclization; serves as precursor for [18F]AlF-NP2."
    },
    {
      "id": "C10",
      "name": "68GaCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "68Ge-68Ga generator (ITM)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Gallium-68 chloride radionuclide source obtained from 68Ge/68Ga generator; used in radiolabeling of DOTA-peptide precursors DP1, DP2, and DP3."
    },
    {
      "id": "C11",
      "name": "sodium acetate buffer (0.25 M, pH 6.5)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Sodium acetate solution used to adjust the pH of the 68GaCl3 solution to pH 4–4.5 prior to reaction with DOTA-peptide precursors."
    },
    {
      "id": "C12",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "68Ga-radiolabeled DOTA-conjugated linear ROR1-targeting peptide; primary PET imaging radiotracer evaluated for ROR1 visualization in multiple tumor models."
    },
    {
      "id": "C13",
      "name": "[68Ga]Ga-DP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "68Ga-radiolabeled DOTA-conjugated cyclic ROR1-targeting peptide; PET imaging radiotracer evaluated in MC38 tumor-bearing mice."
    },
    {
      "id": "C14",
      "name": "[68Ga]Ga-DP3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "68Ga-radiolabeled DOTA-conjugated thioether-cyclized ROR1-targeting peptide; PET imaging radiotracer evaluated in MC38 tumor-bearing mice."
    },
    {
      "id": "C15",
      "name": "fluoride-18 ([18F]fluoride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Cyclone 18/9 cyclotron (IBA), Center for Molecular Imaging and Translational Medicine, Xiamen University",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "18F-fluoride radionuclide produced by 18O(p,n)18F reaction; trapped on QMA cartridge and eluted into AlCl3/acetate reaction mixture for AlF-18F radiolabeling of NOTA-peptide precursors."
    },
    {
      "id": "C16",
      "name": "aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Aluminum chloride solution used to form the Al3+ complex with 18F and NOTA-peptide precursor in the AlF radiolabeling method."
    },
    {
      "id": "C17",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "AlF-18F-radiolabeled NOTA-conjugated linear ROR1-targeting peptide; primary 18F-labeled PET imaging radiotracer showing highest cell uptake and favorable tumor-to-background ratios."
    },
    {
      "id": "C18",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "AlF-18F-radiolabeled NOTA-conjugated cyclic ROR1-targeting peptide; 18F-labeled PET imaging radiotracer showing lower tumor uptake compared to [18F]AlF-NP1."
    },
    {
      "id": "C19",
      "name": "Rink Amide MBHA Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solid-phase peptide synthesis resin used as the starting support in Scheme S1 (PR7 synthesis) via initial Fmoc-Phe-OH loading."
    },
    {
      "id": "C20",
      "name": "Fmoc-Phe-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "First Fmoc-protected amino acid loaded onto Rink Amide MBHA Resin in Scheme S1 (PR7 SPPS)."
    },
    {
      "id": "C21",
      "name": "HOBt",
      "iupac_name": "1-hydroxybenzotriazole",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling additive used with DIC in SPPS coupling cycles in Schemes S1, S2, S3, S4."
    },
    {
      "id": "C22",
      "name": "DIC",
      "iupac_name": "N,N'-diisopropylcarbodiimide",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling reagent used with HOBt in SPPS coupling cycles in Schemes S1, S2, S3, S4."
    },
    {
      "id": "C23",
      "name": "20% piperidine in DMF",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc deprotection reagent used between each SPPS coupling cycle in Schemes S1, S2, S3, S4."
    },
    {
      "id": "C24",
      "name": "TFA",
      "iupac_name": "trifluoroacetic acid",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Used for global deprotection and cleavage from resin in Scheme S1 (Step 3/PR7), Scheme S3 (Step 4/DP3 linear intermediate), and in final TFA deprotection steps in Schemes S2 and S4; also used as 1% TFA/DCM for partial CTC resin cleavage in Schemes S2 (Step 6) and S4 (Step 6)."
    },
    {
      "id": "C25",
      "name": "H-Phe-Rink Amide MBHA Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-deprotected Phe-loaded Rink Amide MBHA Resin intermediate produced after initial loading and Fmoc removal in Scheme S1 Step 1; used for subsequent iterative SPPS elongation."
    },
    {
      "id": "C26",
      "name": "fully protected PR7 peptide-resin (H-Ser(tBu)-Asp(OtBu)-Ile-Asn(Trt)-Asp(OtBu)-Arg(Pbf)-Gln(Trt)-Ile-Pro-Gly-Tyr(tBu)-Ser(tBu)-Thr(tBu)-Tyr(tBu)-Trp(Boc)-Gly-Asp(OtBu)-Phe-Rink Amide MBHA Resin)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fully assembled and side-chain protected PR7 peptide on Rink Amide MBHA Resin after 17 iterative Fmoc SPPS coupling/deprotection cycles in Scheme S1 Step 2; cleaved and globally deprotected by TFA in Step 3 to yield PR7."
    },
    {
      "id": "C27",
      "name": "CTC Resin",
      "iupac_name": "2-chlorotrityl chloride resin",
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acid-labile solid support used in Schemes S2 (DP2), S3 (DP3), and S4 (NP2) for SPPS; allows mild 1% TFA/DCM cleavage to release protected peptide for subsequent solution-phase cyclization."
    },
    {
      "id": "C28",
      "name": "Fmoc-Gly-Gly-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-protected dipeptide building block used as first residue loaded onto CTC resin in Scheme S2 (Step 1, DP2 synthesis) and Scheme S4 (Step 1, NP2 synthesis)."
    },
    {
      "id": "C29",
      "name": "H-Gly-Gly-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-deprotected Gly-Gly-CTC resin intermediate from Scheme S2 Step 1 and Scheme S4 Step 1; used as starting support for further SPPS elongation toward DP2 and NP2."
    },
    {
      "id": "C30",
      "name": "Dde-Lys(Fmoc)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Orthogonally protected lysine building block with Dde on alpha-amine and Fmoc on epsilon-amine; used in Scheme S2 Step 2 (DP2) and Scheme S4 Step 2 (NP2) to introduce a branching lysine for DOTA/NOTA conjugation."
    },
    {
      "id": "C31",
      "name": "HBTU",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "HBTU coupling reagent used in Schemes S2 (Steps 2, 3) and S4 (Steps 2) for SPPS coupling of Dde-Lys(Fmoc)-OH and DOTA(3tBu)/NOTA(2tBu)."
    },
    {
      "id": "C32",
      "name": "NMM",
      "iupac_name": "N-methylmorpholine",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base used with HBTU in SPPS coupling reactions in Schemes S2 and S4."
    },
    {
      "id": "C33",
      "name": "Dde-Lys-Gly-Gly-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Resin-bound intermediate bearing Dde-protected Lys after coupling and Fmoc removal in Scheme S2 Step 2 and Scheme S4 Step 2."
    },
    {
      "id": "C34",
      "name": "DOTA(3tBu)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Tri-tert-butyl protected DOTA chelator building block conjugated to the lysine epsilon-amine on resin in Scheme S2 Step 3 after Dde removal."
    },
    {
      "id": "C35",
      "name": "HATU",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling reagent used in Scheme S2 Step 3 for DOTA(3tBu) conjugation to lysine epsilon-amine after Dde removal, and in Scheme S4 Step 3 for NOTA(2tBu) conjugation."
    },
    {
      "id": "C36",
      "name": "5% hydrazine in DMF/water",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Dde-removing reagent used in Scheme S2 Step 3 and Scheme S4 Step 3 to selectively deprotect the Lys alpha-amine for DOTA/NOTA conjugation."
    },
    {
      "id": "C37",
      "name": "H-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Resin-bound intermediate with DOTA(3tBu) on lysine epsilon-amine and free alpha-amine after Dde removal in Scheme S2 Step 3; used for further SPPS elongation."
    },
    {
      "id": "C38",
      "name": "H-Phe-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Resin-bound intermediate after Fmoc-Phe-OH coupling and Fmoc removal in Scheme S2 Step 4; used as initiating residue for the 17-amino-acid SPPS elongation in Step 5."
    },
    {
      "id": "C39",
      "name": "fully protected DP2 peptide-resin (H-Ser(tBu)-Asp(OtBu)-Ile-Asn(Trt)-Asp(OtBu)-Arg(Pbf)-Gln(Trt)-Ile-Pro-Gly-Tyr(tBu)-Ser(tBu)-Thr(tBu)-Tyr(tBu)-Trp(Boc)-Gly-Asp(OtBu)-Phe-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fully assembled side-chain protected DP2 peptide on CTC resin after 17 iterative Fmoc SPPS cycles in Scheme S2 Step 5; partially cleaved in Step 6 with 1% TFA/DCM to release protected peptide for cyclization."
    },
    {
      "id": "C40",
      "name": "1% TFA in DCM",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Mild acid cleavage cocktail used to partially cleave the protected peptide from CTC resin while retaining side-chain protecting groups in Schemes S2 Step 6 and S4 Step 6."
    },
    {
      "id": "C41",
      "name": "fully protected linear DP2 peptide (solution-phase)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Side-chain protected linear DP2 precursor peptide released from CTC resin by 1% TFA/DCM in Scheme S2 Step 6; used for DPPA-mediated head-to-tail cyclization in Step 7."
    },
    {
      "id": "C42",
      "name": "DPPA",
      "iupac_name": "diphenyl phosphoryl azide",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Cyclization reagent used with DIPEA in DMF for head-to-tail macrolactamization of the protected linear peptide to give cyclic DP2 precursor in Scheme S2 Step 7 and similarly NP2 in Scheme S4 Step 7."
    },
    {
      "id": "C43",
      "name": "Fmoc-Cys(Trt)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc/Trt-protected cysteine building block loaded onto CTC resin as first residue in Scheme S3 Step 1 (DP3 synthesis)."
    },
    {
      "id": "C44",
      "name": "H-Cys(Trt)-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-deprotected Cys(Trt)-loaded CTC resin intermediate in Scheme S3 Step 1; used for Phe coupling in Step 2."
    },
    {
      "id": "C45",
      "name": "H-Phe-Cys(Trt)-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Resin-bound Phe-Cys(Trt) dipeptide intermediate after Fmoc-Phe-OH coupling and deprotection in Scheme S3 Step 2; initiation point for 20-residue SPPS elongation in Step 3."
    },
    {
      "id": "C46",
      "name": "acetic anhydride",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Capping reagent used during SPPS elongation cycle 20 in Scheme S3 Step 3 to acetylate the N-terminal Cys(Trt) residue for N-terminal acetylation of the DP3 product."
    },
    {
      "id": "C47",
      "name": "fully protected Ac-Cys(Trt)-Gly-Ser(tBu)-Asp(OtBu)-Ile-Asn(Trt)-Asp(OtBu)-Arg(Pbf)-Gln(Trt)-Ile-Pro-Gly-Tyr(tBu)-Ser(tBu)-Thr(tBu)-Tyr(tBu)-Trp(Boc)-Gly-Asp(OtBu)-Phe-Cys(Trt)-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fully assembled N-terminally acetylated protected linear DP3 precursor on CTC resin after 20 iterative SPPS cycles in Scheme S3 Step 3; cleaved by TFA in Step 4."
    },
    {
      "id": "C48",
      "name": "linear deprotected DP3 precursor (free dithiol)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fully deprotected linear peptide with two free cysteine thiols released from CTC resin by TFA in Scheme S3 Step 4; serves as substrate for thiol-alkylation cyclization in Steps 5 and 6."
    },
    {
      "id": "C49",
      "name": "alpha,alpha'-dibromo-m-xylene (dibromomethylbenzene)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Bis-electrophile used as thiol-alkylation crosslinker to cyclize the linear dithiol DP3 precursor via dual thioether bond formation in Scheme S3 Step 5."
    },
    {
      "id": "C50",
      "name": "NH4HCO3 in acetonitrile/water",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Ammonium bicarbonate buffer in acetonitrile used as solvent/base system for thiol-alkylation cyclization of DP3 precursor in Scheme S3 Steps 5 and 6."
    },
    {
      "id": "C51",
      "name": "thioether-cyclized DP3 precursor (before DOTA conjugation)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Cyclized peptide with two thioether bridges to m-xylylene linker produced in Scheme S3 Step 5; used as substrate for DOTA conjugation (Step 6) in NH4HCO3/ACN to give DP3."
    },
    {
      "id": "C52",
      "name": "NOTA(2tBu)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Di-tert-butyl protected NOTA chelator building block conjugated to lysine epsilon-amine on resin in Scheme S4 Step 3 (NP2 synthesis) after Dde removal."
    },
    {
      "id": "C53",
      "name": "H-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Resin-bound intermediate with NOTA(2tBu) on lysine epsilon-amine after Dde removal and NOTA conjugation in Scheme S4 Step 3; used for further SPPS elongation."
    },
    {
      "id": "C54",
      "name": "H-Phe-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Resin-bound intermediate after Fmoc-Phe-OH coupling and Fmoc removal in Scheme S4 Step 4; used as initiating residue for 17-amino-acid SPPS elongation in Step 5 toward NP2."
    },
    {
      "id": "C55",
      "name": "fully protected NP2 peptide-resin (H-Ser(tBu)-Asp(OtBu)-Ile-Asn(Trt)-Asp(OtBu)-Arg(Pbf)-Gln(Trt)-Ile-Pro-Gly-Tyr(tBu)-Ser(tBu)-Thr(tBu)-Tyr(tBu)-Trp(Boc)-Gly-Asp(OtBu)-Phe-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fully assembled side-chain protected NP2 peptide on CTC resin after 17 iterative Fmoc SPPS cycles in Scheme S4 Step 5; partially cleaved by 1% TFA/DCM in Step 6 for solution-phase cyclization."
    },
    {
      "id": "C56",
      "name": "fully protected linear NP2 peptide (solution-phase)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Side-chain protected linear NP2 precursor peptide released from CTC resin by 1% TFA/DCM in Scheme S4 Step 6; used for DPPA-mediated head-to-tail cyclization in Step 7."
    },
    {
      "id": "C57",
      "name": "ethanol",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Eluent (1.5 mL) used to elute radiolabeled products from SepPak C18 cartridges in the 68Ga and 18F radiolabeling purification steps."
    },
    {
      "id": "C58",
      "name": "SepPak C18 cartridge eluate containing radiolabeled product in ethanol",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Transient intermediate after SepPak C18 purification of radiolabeled products; ethanol solvent is removed and product redissolved in saline prior to final QC."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of PR7 (SI Scheme S1)",
      "source_section": "SI_scheme_S1",
      "target_compound_id": "C01",
      "target_compound_name": "PR7",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Fmoc SPPS resin loading",
          "reactants": [
            {
              "compound_id": "C19",
              "name": "Rink Amide MBHA Resin",
              "amount": null
            },
            {
              "compound_id": "C20",
              "name": "Fmoc-Phe-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C21",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C22",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C23",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C25",
            "name": "H-Phe-Rink Amide MBHA Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Step details derived from Scheme S1 schematic; amounts, time, and temperature not provided in available documents."
        },
        {
          "step_number": 2,
          "reaction_type": "Iterative Fmoc SPPS elongation (17 cycles)",
          "reactants": [
            {
              "compound_id": "C25",
              "name": "H-Phe-Rink Amide MBHA Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C21",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C22",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C23",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C26",
            "name": "fully protected PR7 peptide-resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "17 Fmoc amino acids coupled sequentially in order per Scheme S1: (1) Fmoc-Asp(OtBu)-OH, (2) Fmoc-Gly-OH, (3) Fmoc-Trp(Boc)-OH, (4) Fmoc-Tyr(tBu)-OH, (5) Fmoc-Thr(tBu)-OH, (6) Fmoc-Ser(tBu)-OH, (7) Fmoc-Tyr(tBu)-OH, (8) Fmoc-Gly-OH, (9) Fmoc-Pro-OH, (10) Fmoc-Ile-OH, (11) Fmoc-Gln(Trt)-OH, (12) Fmoc-Arg(Pbf)-OH, (13) Fmoc-Asp(OtBu)-OH, (14) Fmoc-Asn(Trt)-OH, (15) Fmoc-Ile-OH, (16) Fmoc-Asp(OtBu)-OH, (17) Fmoc-Ser(tBu)-OH. Individual coupling amounts and times not specified in available documents."
        },
        {
          "step_number": 3,
          "reaction_type": "Global deprotection and resin cleavage",
          "reactants": [
            {
              "compound_id": "C26",
              "name": "fully protected PR7 peptide-resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C24",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C01",
            "name": "PR7",
            "yield": null,
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 10.642
          },
          "purification": null,
          "notes": "TFA cleavage cocktail composition and workup details not specified in available documents; compound characterized externally. HPLC method: 0.1% TFA in water (A), 0.1% TFA in acetonitrile (B); 23% B to 43% B over 20 min, 1 mL/min."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of DP2 (SI Scheme S2)",
      "source_section": "SI_scheme_S2",
      "target_compound_id": "C07",
      "target_compound_name": "DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Fmoc SPPS resin loading",
          "reactants": [
            {
              "compound_id": "C27",
              "name": "CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C28",
              "name": "Fmoc-Gly-Gly-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C23",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C29",
            "name": "H-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Amounts, time, temperature not specified in Scheme S2 schematic."
        },
        {
          "step_number": 2,
          "reaction_type": "Fmoc SPPS coupling of Dde-Lys(Fmoc)-OH and Fmoc removal",
          "reactants": [
            {
              "compound_id": "C29",
              "name": "H-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C30",
              "name": "Dde-Lys(Fmoc)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C31",
              "name": "HBTU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C32",
              "name": "NMM",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C23",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C33",
            "name": "Dde-Lys-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Fmoc on epsilon-amine of Lys is removed by piperidine to give free epsilon-amine; alpha-amine remains Dde-protected. Amounts and times not specified."
        },
        {
          "step_number": 3,
          "reaction_type": "Dde removal and DOTA(3tBu) conjugation to lysine epsilon-amine",
          "reactants": [
            {
              "compound_id": "C33",
              "name": "Dde-Lys-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C34",
              "name": "DOTA(3tBu)",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C36",
              "name": "5% hydrazine in DMF/water",
              "amount": null,
              "role": "protecting_group_reagent"
            },
            {
              "compound_id": "C35",
              "name": "HATU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C32",
              "name": "NMM",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C37",
            "name": "H-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "5% hydrazine first removes Dde from alpha-amine of Lys; DOTA(3tBu) is then coupled via HATU to the free alpha-amine. Amounts and times not specified."
        },
        {
          "step_number": 4,
          "reaction_type": "Fmoc-Phe-OH coupling and Fmoc removal",
          "reactants": [
            {
              "compound_id": "C37",
              "name": "H-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C20",
              "name": "Fmoc-Phe-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C21",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C22",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C23",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C38",
            "name": "H-Phe-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Amounts and times not specified."
        },
        {
          "step_number": 5,
          "reaction_type": "Iterative Fmoc SPPS elongation (17 cycles)",
          "reactants": [
            {
              "compound_id": "C38",
              "name": "H-Phe-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C21",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C22",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C23",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C39",
            "name": "fully protected DP2 peptide-resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "17 Fmoc amino acids coupled in order per Scheme S2: (1) Fmoc-Asp(OtBu)-OH, (2) Fmoc-Gly-OH, (3) Fmoc-Trp(Boc)-OH, (4) Fmoc-Tyr(tBu)-OH, (5) Fmoc-Thr(tBu)-OH, (6) Fmoc-Ser(tBu)-OH, (7) Fmoc-Tyr(tBu)-OH, (8) Fmoc-Gly-OH, (9) Fmoc-Pro-OH, (10) Fmoc-Ile-OH, (11) Fmoc-Gln(Trt)-OH, (12) Fmoc-Arg(Pbf)-OH, (13) Fmoc-Asp(OtBu)-OH, (14) Fmoc-Asn(Trt)-OH, (15) Fmoc-Ile-OH, (16) Fmoc-Asp(OtBu)-OH, (17) Fmoc-Ser(tBu)-OH."
        },
        {
          "step_number": 6,
          "reaction_type": "Partial acid cleavage from CTC resin",
          "reactants": [
            {
              "compound_id": "C39",
              "name": "fully protected DP2 peptide-resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C40",
              "name": "1% TFA in DCM",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DCM",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C41",
            "name": "fully protected linear DP2 peptide (solution-phase)",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Mild 1% TFA/DCM cleaves from CTC resin while retaining side-chain protecting groups. Amounts and times not specified."
        },
        {
          "step_number": 7,
          "reaction_type": "Head-to-tail macrolactamization and global deprotection",
          "reactants": [
            {
              "compound_id": "C41",
              "name": "fully protected linear DP2 peptide (solution-phase)",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C42",
              "name": "DPPA",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C24",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C07",
            "name": "DP2",
            "yield": null,
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 10.328
          },
          "purification": null,
          "notes": "Step 7 per Scheme S2 label: DPPA/DIPEA/DMF for cyclization followed by TFA for global deprotection. These are shown as sequential sub-steps in the scheme. Amounts and times not specified. HPLC method: 0.1% TFA in water (A), 0.1% TFA in acetonitrile (B); 23% B to 43% B over 20 min, 1 mL/min."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Synthesis of DP3 (SI Scheme S3)",
      "source_section": "SI_scheme_S3",
      "target_compound_id": "C08",
      "target_compound_name": "DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Fmoc SPPS resin loading with Fmoc-Cys(Trt)-OH",
          "reactants": [
            {
              "compound_id": "C27",
              "name": "CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C43",
              "name": "Fmoc-Cys(Trt)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C23",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C44",
            "name": "H-Cys(Trt)-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Amounts and times not specified."
        },
        {
          "step_number": 2,
          "reaction_type": "Fmoc-Phe-OH coupling and Fmoc removal",
          "reactants": [
            {
              "compound_id": "C44",
              "name": "H-Cys(Trt)-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C20",
              "name": "Fmoc-Phe-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C21",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C22",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C23",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C45",
            "name": "H-Phe-Cys(Trt)-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Amounts and times not specified."
        },
        {
          "step_number": 3,
          "reaction_type": "Iterative Fmoc SPPS elongation (18 cycles) with N-terminal acetylation",
          "reactants": [
            {
              "compound_id": "C45",
              "name": "H-Phe-Cys(Trt)-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C21",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C22",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C23",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            },
            {
              "compound_id": "C46",
              "name": "acetic anhydride",
              "amount": null,
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C47",
            "name": "fully protected Ac-Cys(Trt)...-Phe-Cys(Trt)-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "19 additional residues coupled then N-terminal Cys acetylated with acetic anhydride per Scheme S3: (1) Fmoc-Asp(OtBu)-OH, (2) Fmoc-Gly-OH, (3) Fmoc-Trp(Boc)-OH, (4) Fmoc-Tyr(tBu)-OH, (5) Fmoc-Thr(tBu)-OH, (6) Fmoc-Ser(tBu)-OH, (7) Fmoc-Tyr(tBu)-OH, (8) Fmoc-Gly-OH, (9) Fmoc-Pro-OH, (10) Fmoc-Ile-OH, (11) Fmoc-Gln(Trt)-OH, (12) Fmoc-Arg(Pbf)-OH, (13) Fmoc-Asp(OtBu)-OH, (14) Fmoc-Asn(Trt)-OH, (15) Fmoc-Ile-OH, (16) Fmoc-Asp(OtBu)-OH, (17) Fmoc-Ser(tBu)-OH, (18) Fmoc-Gly-OH, (19) Fmoc-Cys(Trt)-OH, then acetylation."
        },
        {
          "step_number": 4,
          "reaction_type": "Global deprotection and resin cleavage",
          "reactants": [
            {
              "compound_id": "C47",
              "name": "fully protected Ac-Cys(Trt)...-Phe-Cys(Trt)-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C24",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C48",
            "name": "linear deprotected DP3 precursor (free dithiol)",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "TFA cleavage cocktail composition not specified. Yields two free Cys-SH groups for subsequent cyclization."
        },
        {
          "step_number": 5,
          "reaction_type": "Thiol-alkylation bis-cyclization with dibromomethylbenzene",
          "reactants": [
            {
              "compound_id": "C48",
              "name": "linear deprotected DP3 precursor (free dithiol)",
              "amount": null
            },
            {
              "compound_id": "C49",
              "name": "alpha,alpha'-dibromo-m-xylene",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C50",
              "name": "NH4HCO3 in acetonitrile/water",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile/water",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C51",
            "name": "thioether-cyclized DP3 precursor (before DOTA conjugation)",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Per Scheme S3: alpha,alpha'-dibromo-m-xylene reacts with both Cys-SH groups in NH4HCO3/ACN. Amounts and times not specified."
        },
        {
          "step_number": 6,
          "reaction_type": "DOTA conjugation to cyclized peptide",
          "reactants": [
            {
              "compound_id": "C51",
              "name": "thioether-cyclized DP3 precursor (before DOTA conjugation)",
              "amount": null
            },
            {
              "compound_id": "C34",
              "name": "DOTA(3tBu)",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C50",
              "name": "NH4HCO3 in acetonitrile/water",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile/water",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C08",
            "name": "DP3",
            "yield": null,
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 10.404
          },
          "purification": null,
          "notes": "Per Scheme S3 Step 6 label: NH4HCO3/ACN used for DOTA conjugation. The DOTA shown in the final DP3 structure appears to be free-acid DOTA (after tBu deprotection); whether tBu deprotection occurs here or is implicit in the TFA step is not explicitly described. Amounts, coupling reagents for DOTA, and times not specified. HPLC method: 0.1% TFA in water (A), 0.1% TFA in acetonitrile (B); 23% B to 43% B over 20 min, 1 mL/min."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Synthesis of NP2 (SI Scheme S4)",
      "source_section": "SI_scheme_S4",
      "target_compound_id": "C09",
      "target_compound_name": "NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Fmoc SPPS resin loading",
          "reactants": [
            {
              "compound_id": "C27",
              "name": "CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C28",
              "name": "Fmoc-Gly-Gly-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C23",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C29",
            "name": "H-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Identical first step to Scheme S2 (DP2 synthesis). Amounts and times not specified."
        },
        {
          "step_number": 2,
          "reaction_type": "Fmoc SPPS coupling of Dde-Lys(Fmoc)-OH and Fmoc removal",
          "reactants": [
            {
              "compound_id": "C29",
              "name": "H-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C30",
              "name": "Dde-Lys(Fmoc)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C31",
              "name": "HBTU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C23",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C33",
            "name": "Dde-Lys-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Scheme S4 uses HBTU/DIPEA (not NMM) for this step. Amounts and times not specified."
        },
        {
          "step_number": 3,
          "reaction_type": "Dde removal and NOTA(2tBu) conjugation to lysine epsilon-amine",
          "reactants": [
            {
              "compound_id": "C33",
              "name": "Dde-Lys-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C52",
              "name": "NOTA(2tBu)",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C36",
              "name": "5% hydrazine in DMF/water",
              "amount": null,
              "role": "protecting_group_reagent"
            },
            {
              "compound_id": "C35",
              "name": "HATU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C53",
            "name": "H-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Amounts and times not specified."
        },
        {
          "step_number": 4,
          "reaction_type": "Fmoc-Phe-OH coupling and Fmoc removal",
          "reactants": [
            {
              "compound_id": "C53",
              "name": "H-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C20",
              "name": "Fmoc-Phe-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C21",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C22",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C23",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C54",
            "name": "H-Phe-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Amounts and times not specified."
        },
        {
          "step_number": 5,
          "reaction_type": "Iterative Fmoc SPPS elongation (17 cycles)",
          "reactants": [
            {
              "compound_id": "C54",
              "name": "H-Phe-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C21",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C22",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C23",
              "name": "20% piperidine in DMF",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C55",
            "name": "fully protected NP2 peptide-resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "17 Fmoc amino acids coupled per Scheme S4: (1) Fmoc-Asp(OtBu)-OH, (2) Fmoc-Gly-OH, (3) Fmoc-Trp(Boc)-OH, (4) Fmoc-Tyr(tBu)-OH, (5) Fmoc-Thr(tBu)-OH, (6) Fmoc-Ser(tBu)-OH (listed as Fmoc-Ser(Trt)-OH in scheme), (7) Fmoc-Tyr(tBu)-OH, (8) Fmoc-Gly-OH, (9) Fmoc-Pro-OH, (10) Fmoc-Ile-OH, (11) Fmoc-Gln(Trt)-OH, (12) Fmoc-Arg(Pbf)-OH, (13) Fmoc-Asp(OtBu)-OH, (14) Fmoc-Asn(Trt)-OH (listed as Fmoc-Asn(Pbf)-OH in scheme), (15) Fmoc-Ile-OH, (16) Fmoc-Asp(OtBu)-OH, (17) Fmoc-Ser(tBu)-OH."
        },
        {
          "step_number": 6,
          "reaction_type": "Partial acid cleavage from CTC resin",
          "reactants": [
            {
              "compound_id": "C55",
              "name": "fully protected NP2 peptide-resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C40",
              "name": "1% TFA in DCM",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DCM",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C56",
            "name": "fully protected linear NP2 peptide (solution-phase)",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Amounts and times not specified."
        },
        {
          "step_number": 7,
          "reaction_type": "Head-to-tail macrolactamization and global deprotection",
          "reactants": [
            {
              "compound_id": "C56",
              "name": "fully protected linear NP2 peptide (solution-phase)",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C42",
              "name": "DPPA",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C24",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C09",
            "name": "NP2",
            "yield": null,
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 10.620
          },
          "purification": null,
          "notes": "DPPA/DIPEA/DMF for cyclization followed by TFA for global deprotection per Scheme S4 Step 7. Amounts and times not specified. HPLC method: 0.1% TFA in water (A), 0.1% TFA in acetonitrile (B); 23% B to 43% B over 20 min, 1 mL/min."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Synthesis of DP1 (SI Scheme S5 / main text section 5.2.1)",
      "source_section": "SI_scheme_S5",
      "target_compound_id": "C05",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling (DOTA conjugation)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 umol)"
            },
            {
              "compound_id": "C02",
              "name": "DOTA-NHS",
              "amount": "2.5 mg (5 umol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": "20 uL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 uL"
            }
          ],
          "conditions": {
            "temperature": "RT",
            "time": "12 h",
            "atmosphere": null,
            "ph": null,
            "other": "Reaction mixture agitated in an oscillator; product isolated after lyophilization."
          },
          "product": {
            "compound_id": "C05",
            "name": "DP1",
            "yield": "4.2 mg (55.6%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 11.230
          },
          "purification": "semipreparative HPLC, UV detection at 254 nm; 0.1% TFA in water (A) / 0.1% TFA in acetonitrile (B), 5% B to 95% B over 20 min, 1 mL/min; followed by lyophilization",
          "notes": "Reaction performed in a 2 mL centrifugation tube."
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Synthesis of NP1 (SI Scheme S5 / main text section 5.2.1)",
      "source_section": "SI_scheme_S5",
      "target_compound_id": "C06",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling (NOTA conjugation)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 umol)"
            },
            {
              "compound_id": "C03",
              "name": "NOTA-NHS",
              "amount": "2 mg (5 umol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": "20 uL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 uL"
            }
          ],
          "conditions": {
            "temperature": "RT",
            "time": "12 h",
            "atmosphere": null,
            "ph": null,
            "other": "Reaction mixture agitated in an oscillator; product isolated after lyophilization."
          },
          "product": {
            "compound_id": "C06",
            "name": "NP1",
            "yield": "3.9 mg (54%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 12.780
          },
          "purification": "semipreparative HPLC, UV detection at 254 nm; 0.1% TFA in water (A) / 0.1% TFA in acetonitrile (B), 5% B to 95% B over 20 min, 1 mL/min; followed by lyophilization",
          "notes": "Performed in the same reaction as DP1 synthesis (parallel reactions in separate 2 mL centrifugation tubes) but constitutes a distinct product pathway per Rule 14."
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP1 (main text section 5.4)",
      "source_section": "main_text",
      "target_compound_id": "C12",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3 solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74-1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C11",
              "name": "sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": "4-4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "68GaCl3-sodium acetate solution pH 4-4.5",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "68Ga radiolabeling of DOTA-peptide precursor",
          "reactants": [
            {
              "compound_id": "C05",
              "name": "DP1 precursor",
              "amount": "50 ug (16-20 nmol) in 50 uL DMSO"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "68GaCl3-sodium acetate solution pH 4-4.5",
              "amount": "1.5 mL (combined from Step 1)",
              "role": "radionuclide_source"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to RT after reaction; purified by SepPak C18 cartridge eluted with 1.5 mL ethanol; ethanol removed and product redissolved in saline."
          },
          "product": {
            "compound_id": "C12",
            "name": "[68Ga]Ga-DP1",
            "yield": "89.55 ± 0.12%",
            "purity": ">95% RCP by radio-HPLC",
            "hplc_retention_time_min": 12.26
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters), eluted with 1.5 mL ethanol",
          "notes": "n ≥ 3. RCP 92.56 ± 0.02%. Molar activity 14.37 ± 0.97 GBq/umol. Radio-HPLC method: 0.1% TFA in water (A) / 0.1% TFA in acetonitrile (B); 5% B to 95% B over 20 min, 1 mL/min. Same procedure used for DP2 (→[68Ga]Ga-DP2, P8) and DP3 (→[68Ga]Ga-DP3, P9)."
        }
      ]
    },
    {
      "pathway_id": "P8",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP2 (main text section 5.4)",
      "source_section": "main_text",
      "target_compound_id": "C13",
      "target_compound_name": "[68Ga]Ga-DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3 solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74-1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C11",
              "name": "sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": "4-4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "68GaCl3-sodium acetate solution pH 4-4.5",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "68Ga radiolabeling of DOTA-peptide precursor",
          "reactants": [
            {
              "compound_id": "C07",
              "name": "DP2 precursor",
              "amount": "50 ug (16-20 nmol) in 50 uL DMSO"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "68GaCl3-sodium acetate solution pH 4-4.5",
              "amount": "1.5 mL (combined from Step 1)",
              "role": "radionuclide_source"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to RT after reaction; purified by SepPak C18 cartridge eluted with 1.5 mL ethanol; ethanol removed and product redissolved in saline."
          },
          "product": {
            "compound_id": "C13",
            "name": "[68Ga]Ga-DP2",
            "yield": "97.67 ± 1.05%",
            "purity": ">95% RCP by radio-HPLC",
            "hplc_retention_time_min": 11.22
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters), eluted with 1.5 mL ethanol",
          "notes": "n ≥ 3. RCP 99.45 ± 0.01%. Molar activity 20.05 ± 1.35 GBq/umol."
        }
      ]
    },
    {
      "pathway_id": "P9",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP3 (main text section 5.4)",
      "source_section": "main_text",
      "target_compound_id": "C14",
      "target_compound_name": "[68Ga]Ga-DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3 solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74-1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C11",
              "name": "sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": "4-4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "68GaCl3-sodium acetate solution pH 4-4.5",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "68Ga radiolabeling of DOTA-peptide precursor",
          "reactants": [
            {
              "compound_id": "C08",
              "name": "DP3 precursor",
              "amount": "50 ug (16-20 nmol) in 50 uL DMSO"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "68GaCl3-sodium acetate solution pH 4-4.5",
              "amount": "1.5 mL (combined from Step 1)",
              "role": "radionuclide_source"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to RT after reaction; purified by SepPak C18 cartridge eluted with 1.5 mL ethanol; ethanol removed and product redissolved in saline."
          },
          "product": {
            "compound_id": "C14",
            "name": "[68Ga]Ga-DP3",
            "yield": "98.01 ± 0.97%",
            "purity": ">95% RCP by radio-HPLC",
            "hplc_retention_time_min": 12.48
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters), eluted with 1.5 mL ethanol",
          "notes": "n ≥ 3. RCP 98.46 ± 0.05%. Molar activity 14.09 ± 2.12 GBq/umol."
        }
      ]
    },
    {
      "pathway_id": "P10",
      "pathway_name": "Radiolabeling of [18F]AlF-NP1 (main text section 5.4)",
      "source_section": "main_text",
      "target_compound_id": "C17",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "18F-fluoride trapping on QMA cartridge",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "fluoride-18",
              "amount": "0.74-1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline (10 mL for preconditioning)",
              "volume": "10 mL"
            },
            {
              "name": "pure water (10 mL for preconditioning)",
              "volume": "10 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "18F-fluoride trapped on preconditioned QMA cartridge",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water prior to trapping."
        },
        {
          "step_number": 2,
          "reaction_type": "18F-fluoride elution and AlF-NOTA radiolabeling",
          "reactants": [
            {
              "compound_id": "C06",
              "name": "NP1 precursor",
              "amount": "50 ug (18-25 nmol) in 50 uL DMSO"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "18F-fluoride eluate in 0.2 mL saline",
              "amount": "0.2 mL",
              "role": "radionuclide_source"
            },
            {
              "compound_id": "C16",
              "name": "AlCl3 in sodium acetate buffer (2 mM, pH 4.0)",
              "amount": "3 uL",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "100 uL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": "200 uL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to RT after reaction; purified by SepPak C18 cartridge eluted with 1.5 mL ethanol; ethanol removed and final product redissolved in saline."
          },
          "product": {
            "compound_id": "C17",
            "name": "[18F]AlF-NP1",
            "yield": "62.58 ± 0.32%",
            "purity": ">95% RCP by radio-HPLC",
            "hplc_retention_time_min": 12.93
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters), eluted with 1.5 mL ethanol",
          "notes": "n ≥ 3. RCP 99.46 ± 0.15%. Molar activity 13.13 ± 1.71 GBq/umol. 18F eluted from QMA into reaction vial containing AlCl3 solution, acetonitrile, sodium acetate buffer, and precursor. Radio-HPLC method: 0.1% TFA in water (A) / 0.1% TFA in acetonitrile (B); 5% B to 95% B over 20 min, 1 mL/min."
        }
      ]
    },
    {
      "pathway_id": "P11",
      "pathway_name": "Radiolabeling of [18F]AlF-NP2 (main text section 5.4)",
      "source_section": "main_text",
      "target_compound_id": "C18",
      "target_compound_name": "[18F]AlF-NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "18F-fluoride trapping on QMA cartridge",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "fluoride-18",
              "amount": "0.74-1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline (10 mL for preconditioning)",
              "volume": "10 mL"
            },
            {
              "name": "pure water (10 mL for preconditioning)",
              "volume": "10 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "18F-fluoride trapped on preconditioned QMA cartridge",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "18F-fluoride elution and AlF-NOTA radiolabeling",
          "reactants": [
            {
              "compound_id": "C09",
              "name": "NP2 precursor",
              "amount": "50 ug (18-25 nmol) in 50 uL DMSO"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "18F-fluoride eluate in 0.2 mL saline",
              "amount": "0.2 mL",
              "role": "radionuclide_source"
            },
            {
              "compound_id": "C16",
              "name": "AlCl3 in sodium acetate buffer (2 mM, pH 4.0)",
              "amount": "3 uL",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "100 uL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": "200 uL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to RT after reaction; purified by SepPak C18 cartridge eluted with 1.5 mL ethanol; ethanol removed and final product redissolved in saline."
          },
          "product": {
            "compound_id": "C18",
            "name": "[18F]AlF-NP2",
            "yield": "62.76 ± 0.22%",
            "purity": ">95% RCP by radio-HPLC",
            "hplc_retention_time_min": 11.30
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters), eluted with 1.5 mL ethanol",
          "notes": "n ≥ 3. RCP 99.56 ± 0.04%. Molar activity 13.42 ± 1.25 GBq/umol."
        }
      ]
    }
  ]
}
```

#### Gemini
##### Attempt 1
```
{
  "extraction": {
    "prompt_version": "v3.2",
    "extraction_date": "2026-03-30",
    "model_name": "gemini-3.5-pro",
    "extractor_notes": "SI found: jm5c02016_si_001.pdf. SI schemes identified: Scheme S1, Scheme S2, Scheme S3, Scheme S4, Scheme S5. SI compounds identified: None (authors used main text labels PR7, DP1, DP2, DP3, NP1, NP2 within the SI instead of S-series prefixes). Total pathway count: 11. Excluded reference compounds: 2-[18F]FDG, [68Ga]Ga-DOTATATE, Lutathera, [68Ga]Ga-FAP-2286, [64Cu]Cu-WL12, [68Ga]Ga-NK224. Procedures genuinely absent: Specific reagent amounts, reaction times, and temperatures for the solid-phase peptide synthesis (SPPS) steps in SI Schemes S1-S4 are not provided. Mass type notes: observed exact and nominal masses are provided for large peptides."
  },
  "paper": {
    "title": "18F-/68Ga-Labeled Peptide-Based Probes for PET Imaging of ROR1 Expression",
    "authors": [
      "Tao Yang",
      "Jiahui Sun",
      "Guolong Huang",
      "Hong Wang",
      "Zhexin He",
      "Siying Lin",
      "Yanjie Wang",
      "Rongqiang Zhuang",
      "Xianzhong Zhang",
      "Hongwu Liu",
      "Zhide Guo"
    ],
    "doi": "10.1021/acs.jmedchem.5c02016",
    "journal": "Journal of Medicinal Chemistry",
    "year": 2025,
    "synthesis_scale": "lab",
    "method_completeness": "partial",
    "has_synthesis": true,
    "extraction_notes": "Main text details the conjugation of DP1 and NP1 and the radiolabeling of all five probes. The SI provides the theoretical SPPS schemes (S1-S4) utilized by the custom synthesis vendor for PR7, DP2, DP3, and NP2."
  },
  "compounds": [
    {
      "id": "C01",
      "name": "PR7",
      "iupac_name": null,
      "molecular_formula": "C96H133N25O31",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ 1067.47",
      "ms_calculated_exact_mass": 2131.96,
      "description": "Lead linear peptide used as a precursor for conjugation to chelators."
    },
    {
      "id": "C02",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Chelator with an NHS ester group used to conjugate with PR7."
    },
    {
      "id": "C03",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Chelator with an NHS ester group used to conjugate with PR7."
    },
    {
      "id": "C04",
      "name": "DIPEA",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "base",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base used in the conjugation of chelators to peptides."
    },
    {
      "id": "C05",
      "name": "DMSO",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solvent for conjugation and stock solutions."
    },
    {
      "id": "C06",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": null,
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ 1260.54, [M+3H]3+ 840.68",
      "ms_calculated_exact_mass": 2518.14,
      "description": "DOTA-conjugated linear peptide precursor."
    },
    {
      "id": "C07",
      "name": "NP1",
      "iupac_name": null,
      "molecular_formula": "C108H152N28O36",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": null,
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ 1210.22, [M+3H]3+ 807.00",
      "ms_calculated_exact_mass": 2417.09,
      "description": "NOTA-conjugated linear peptide precursor."
    },
    {
      "id": "C08",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ 1373.07, [M+3H]3+ 915.72",
      "ms_calculated_exact_mass": 2743.2514,
      "description": "DOTA-conjugated cyclic peptide precursor."
    },
    {
      "id": "C09",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ 1509.05, [M+3H]3+ 1006.39",
      "ms_calculated_exact_mass": 3015.2514,
      "description": "DOTA-conjugated cyclic peptide precursor."
    },
    {
      "id": "C10",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ 1322.56",
      "ms_calculated_exact_mass": 2642.20,
      "description": "NOTA-conjugated cyclic peptide precursor."
    },
    {
      "id": "C11",
      "name": "68GaCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "ITM",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Radionuclide source obtained from 68Ge/68Ga generator."
    },
    {
      "id": "C12",
      "name": "sodium acetate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "ph_adjuster",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Buffer used to adjust pH during radiolabeling."
    },
    {
      "id": "C13",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": null,
      "purity": "92.56% by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "68Ga-radiolabeled linear peptide probe."
    },
    {
      "id": "C14",
      "name": "[68Ga]Ga-DP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": null,
      "purity": "99.45% by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "68Ga-radiolabeled cyclic peptide probe."
    },
    {
      "id": "C15",
      "name": "[68Ga]Ga-DP3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": null,
      "purity": "98.46% by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "68Ga-radiolabeled cyclic peptide probe."
    },
    {
      "id": "C16",
      "name": "fluoride-18",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Center for Molecular Imaging and Translational Medicine of Xiamen University",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Radionuclide produced via cyclotron."
    },
    {
      "id": "C17",
      "name": "AlCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Aluminum source for Al18F complexation."
    },
    {
      "id": "C18",
      "name": "acetonitrile",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solvent component in Al18F radiolabeling."
    },
    {
      "id": "C19",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": null,
      "purity": "99.46% by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "18F-radiolabeled linear peptide probe."
    },
    {
      "id": "C20",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": null,
      "purity": "99.56% by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "18F-radiolabeled cyclic peptide probe."
    },
    {
      "id": "C21",
      "name": "Rink Amide MBHA Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solid support for the peptide synthesis of PR7."
    },
    {
      "id": "C22",
      "name": "Fmoc-Phe-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "First amino acid building block coupled to resin in SI Scheme S1."
    },
    {
      "id": "C23",
      "name": "HOBt",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "coupling_reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling additive used in SPPS."
    },
    {
      "id": "C24",
      "name": "DIC",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "coupling_reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling reagent used in SPPS."
    },
    {
      "id": "C25",
      "name": "DMF",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solvent for SPPS."
    },
    {
      "id": "C26",
      "name": "piperidine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc deprotection reagent in SPPS."
    },
    {
      "id": "C27",
      "name": "Fmoc-protected amino acids",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Generic entry for the various Fmoc-amino acids used to elongate the peptide chains in SPPS."
    },
    {
      "id": "C28",
      "name": "TFA",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "acid",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Cleavage and global deprotection cocktail component."
    },
    {
      "id": "C29",
      "name": "CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solid support for the synthesis of cyclic peptides."
    },
    {
      "id": "C30",
      "name": "Fmoc-Gly-Gly-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amino acid block used in SI Scheme S2 and S4."
    },
    {
      "id": "C31",
      "name": "Dde-Lys(Fmoc)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Orthogonally protected lysine block used in SI Scheme S2 and S4."
    },
    {
      "id": "C32",
      "name": "HBTU",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "coupling_reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling reagent used in SI Schemes."
    },
    {
      "id": "C33",
      "name": "NMM",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "base",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base used in SI Schemes."
    },
    {
      "id": "C34",
      "name": "DOTA(3tBu)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Protected DOTA derivative used in SI Scheme S2."
    },
    {
      "id": "C35",
      "name": "HATU",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "coupling_reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling reagent used in SI Schemes."
    },
    {
      "id": "C36",
      "name": "hydrazine hydrate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Dde deprotection reagent in SI Schemes S2 and S4."
    },
    {
      "id": "C37",
      "name": "DCM",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solvent used for mild cleavage of CTC resin."
    },
    {
      "id": "C38",
      "name": "DPPA",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "coupling_reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Cyclization reagent used in SI Schemes S2 and S4."
    },
    {
      "id": "C39",
      "name": "Fmoc-Cys(Trt)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Cysteine building block for SI Scheme S3."
    },
    {
      "id": "C40",
      "name": "acetic anhydride",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "N-terminal capping reagent in SI Scheme S3."
    },
    {
      "id": "C41",
      "name": "1,3-bis(bromomethyl)benzene",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Cyclization linker used in SI Scheme S3."
    },
    {
      "id": "C42",
      "name": "NH4HCO3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "base",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Buffer/base used in SI Scheme S3 cyclization."
    },
    {
      "id": "C43",
      "name": "NOTA(2tBu)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Protected NOTA derivative used in SI Scheme S4."
    }
  ],
  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of DP1 (Scheme S5)",
      "source_section": "main_text",
      "target_compound_id": "C06",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Amidation",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 umol)"
            },
            {
              "compound_id": "C02",
              "name": "DOTA-NHS",
              "amount": "2.5 mg (5 umol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": "20 uL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 uL"
            }
          ],
          "conditions": {
            "temperature": "RT",
            "time": "12 h",
            "atmosphere": null,
            "ph": null,
            "other": "Agitated in an oscillator."
          },
          "product": {
            "compound_id": "C06",
            "name": "DP1",
            "yield": "4.2 mg (55.6%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 11.23
          },
          "purification": "semipreparative HPLC",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of NP1 (Scheme S5)",
      "source_section": "main_text",
      "target_compound_id": "C07",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Amidation",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 umol)"
            },
            {
              "compound_id": "C03",
              "name": "NOTA-NHS",
              "amount": "2 mg (5 umol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": "20 uL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 uL"
            }
          ],
          "conditions": {
            "temperature": "RT",
            "time": "12 h",
            "atmosphere": null,
            "ph": null,
            "other": "Agitated in an oscillator."
          },
          "product": {
            "compound_id": "C07",
            "name": "NP1",
            "yield": "3.9 mg (54%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 12.78
          },
          "purification": "semipreparative HPLC",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP1",
      "source_section": "main_text",
      "target_compound_id": "C13",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Radiometal Chelation",
          "reactants": [
            {
              "compound_id": "C06",
              "name": "DP1",
              "amount": "50 ug (16-20 nmol)"
            },
            {
              "compound_id": "C11",
              "name": "68GaCl3",
              "amount": "1 mL (0.74-1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "sodium acetate",
              "amount": "0.5 mL (0.25 M)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 uL"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": "4-4.5",
            "other": null
          },
          "product": {
            "compound_id": "C13",
            "name": "[68Ga]Ga-DP1",
            "yield": "89.55%",
            "purity": "92.56% by radio-HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (1.5 mL ethanol eluent)",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP2",
      "source_section": "main_text",
      "target_compound_id": "C14",
      "target_compound_name": "[68Ga]Ga-DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Radiometal Chelation",
          "reactants": [
            {
              "compound_id": "C08",
              "name": "DP2",
              "amount": "50 ug (16-20 nmol)"
            },
            {
              "compound_id": "C11",
              "name": "68GaCl3",
              "amount": "1 mL (0.74-1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "sodium acetate",
              "amount": "0.5 mL (0.25 M)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 uL"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": "4-4.5",
            "other": null
          },
          "product": {
            "compound_id": "C14",
            "name": "[68Ga]Ga-DP2",
            "yield": "97.67%",
            "purity": "99.45% by radio-HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (1.5 mL ethanol eluent)",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP3",
      "source_section": "main_text",
      "target_compound_id": "C15",
      "target_compound_name": "[68Ga]Ga-DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Radiometal Chelation",
          "reactants": [
            {
              "compound_id": "C09",
              "name": "DP3",
              "amount": "50 ug (16-20 nmol)"
            },
            {
              "compound_id": "C11",
              "name": "68GaCl3",
              "amount": "1 mL (0.74-1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "sodium acetate",
              "amount": "0.5 mL (0.25 M)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 uL"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": "4-4.5",
            "other": null
          },
          "product": {
            "compound_id": "C15",
            "name": "[68Ga]Ga-DP3",
            "yield": "98.01%",
            "purity": "98.46% by radio-HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (1.5 mL ethanol eluent)",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Radiolabeling of [18F]AlF-NP1",
      "source_section": "main_text",
      "target_compound_id": "C19",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Isotope Trapping",
          "reactants": [
            {
              "compound_id": "C16",
              "name": "fluoride-18",
              "amount": "0.74-1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline",
              "volume": "0.2 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Trapped on a preconditioned QMA cartridge and eluted."
          },
          "product": {
            "compound_id": null,
            "name": "eluted fluoride-18",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Al18F Chelation",
          "reactants": [
            {
              "compound_id": "C07",
              "name": "NP1",
              "amount": "50 ug (18-25 nmol)"
            },
            {
              "compound_id": null,
              "name": "eluted fluoride-18",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C17",
              "name": "AlCl3",
              "amount": "3 uL (2 mM)",
              "role": "reagent"
            },
            {
              "compound_id": "C12",
              "name": "sodium acetate buffer",
              "amount": "100 uL (0.1 M)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": "200 uL"
            },
            {
              "name": "DMSO",
              "volume": "50 uL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": "4.0",
            "other": null
          },
          "product": {
            "compound_id": "C19",
            "name": "[18F]AlF-NP1",
            "yield": "62.58%",
            "purity": "99.46% by radio-HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (1.5 mL ethanol eluent)",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Radiolabeling of [18F]AlF-NP2",
      "source_section": "main_text",
      "target_compound_id": "C20",
      "target_compound_name": "[18F]AlF-NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Isotope Trapping",
          "reactants": [
            {
              "compound_id": "C16",
              "name": "fluoride-18",
              "amount": "0.74-1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline",
              "volume": "0.2 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Trapped on a preconditioned QMA cartridge and eluted."
          },
          "product": {
            "compound_id": null,
            "name": "eluted fluoride-18",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Al18F Chelation",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "NP2",
              "amount": "50 ug (18-25 nmol)"
            },
            {
              "compound_id": null,
              "name": "eluted fluoride-18",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C17",
              "name": "AlCl3",
              "amount": "3 uL (2 mM)",
              "role": "reagent"
            },
            {
              "compound_id": "C12",
              "name": "sodium acetate buffer",
              "amount": "100 uL (0.1 M)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": "200 uL"
            },
            {
              "name": "DMSO",
              "volume": "50 uL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": "4.0",
            "other": null
          },
          "product": {
            "compound_id": "C20",
            "name": "[18F]AlF-NP2",
            "yield": "62.76%",
            "purity": "99.56% by radio-HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (1.5 mL ethanol eluent)",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P8",
      "pathway_name": "Synthesis of PR7 (SI Scheme S1)",
      "source_section": "SI_scheme_S1",
      "target_compound_id": "C01",
      "target_compound_name": "PR7",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Solid Phase Peptide Synthesis",
          "reactants": [
            {
              "compound_id": "C21",
              "name": "Rink Amide MBHA Resin",
              "amount": null
            },
            {
              "compound_id": "C22",
              "name": "Fmoc-Phe-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C23",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C24",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C26",
              "name": "piperidine",
              "amount": "20%",
              "role": "reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "H-Phe-Rink Amide MBHA Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Solid Phase Peptide Synthesis",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Phe-Rink Amide MBHA Resin",
              "amount": null
            },
            {
              "compound_id": "C27",
              "name": "Fmoc-protected amino acids",
              "amount": null
            }
          ],
          "reagents": [],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Iterative SPPS cycles."
          },
          "product": {
            "compound_id": null,
            "name": "Protected PR7-Rink Amide MBHA Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Cleavage and Deprotection",
          "reactants": [
            {
              "compound_id": null,
              "name": "Protected PR7-Rink Amide MBHA Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C28",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C01",
            "name": "PR7",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P9",
      "pathway_name": "Synthesis of DP2 (SI Scheme S2)",
      "source_section": "SI_scheme_S2",
      "target_compound_id": "C08",
      "target_compound_name": "DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Solid Phase Peptide Synthesis",
          "reactants": [
            {
              "compound_id": "C29",
              "name": "CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C30",
              "name": "Fmoc-Gly-Gly-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C26",
              "name": "piperidine",
              "amount": "20%",
              "role": "reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "H-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Solid Phase Peptide Synthesis",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C31",
              "name": "Dde-Lys(Fmoc)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C32",
              "name": "HBTU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C33",
              "name": "NMM",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C26",
              "name": "piperidine",
              "amount": "20%",
              "role": "reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Dde-Lys-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Solid Phase Peptide Synthesis",
          "reactants": [
            {
              "compound_id": null,
              "name": "Dde-Lys-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C34",
              "name": "DOTA(3tBu)",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C35",
              "name": "HATU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C33",
              "name": "NMM",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C36",
              "name": "hydrazine hydrate",
              "amount": "5%",
              "role": "reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "H-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "Solid Phase Peptide Synthesis",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C27",
              "name": "Fmoc-protected amino acids",
              "amount": null
            }
          ],
          "reagents": [],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Iterative SPPS cycles."
          },
          "product": {
            "compound_id": null,
            "name": "Protected DP2-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "Resin Cleavage",
          "reactants": [
            {
              "compound_id": null,
              "name": "Protected DP2-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C28",
              "name": "TFA",
              "amount": "1%",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DCM",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Mild cleavage retaining side-chain protecting groups."
          },
          "product": {
            "compound_id": null,
            "name": "Protected linear DP2",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 6,
          "reaction_type": "Cyclization and Deprotection",
          "reactants": [
            {
              "compound_id": null,
              "name": "Protected linear DP2",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C38",
              "name": "DPPA",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C28",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cyclization followed by global deprotection with TFA."
          },
          "product": {
            "compound_id": "C08",
            "name": "DP2",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P10",
      "pathway_name": "Synthesis of DP3 (SI Scheme S3)",
      "source_section": "SI_scheme_S3",
      "target_compound_id": "C09",
      "target_compound_name": "DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Solid Phase Peptide Synthesis",
          "reactants": [
            {
              "compound_id": "C29",
              "name": "CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C39",
              "name": "Fmoc-Cys(Trt)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C26",
              "name": "piperidine",
              "amount": "20%",
              "role": "reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "H-Cys(Trt)-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Solid Phase Peptide Synthesis",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Cys(Trt)-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C27",
              "name": "Fmoc-protected amino acids",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C40",
              "name": "acetic anhydride",
              "amount": null,
              "role": "reagent"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Iterative SPPS cycles ending with N-terminal acetylation."
          },
          "product": {
            "compound_id": null,
            "name": "Protected DP3-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Cleavage and Deprotection",
          "reactants": [
            {
              "compound_id": null,
              "name": "Protected DP3-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C28",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "linear dithiol DP3 precursor",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "Alkylation",
          "reactants": [
            {
              "compound_id": null,
              "name": "linear dithiol DP3 precursor",
              "amount": null
            },
            {
              "compound_id": "C41",
              "name": "1,3-bis(bromomethyl)benzene",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C42",
              "name": "NH4HCO3",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "ACN",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cyclization via thioether formation."
          },
          "product": {
            "compound_id": "C09",
            "name": "DP3",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P11",
      "pathway_name": "Synthesis of NP2 (SI Scheme S4)",
      "source_section": "SI_scheme_S4",
      "target_compound_id": "C10",
      "target_compound_name": "NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Solid Phase Peptide Synthesis",
          "reactants": [
            {
              "compound_id": "C29",
              "name": "CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C30",
              "name": "Fmoc-Gly-Gly-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C26",
              "name": "piperidine",
              "amount": "20%",
              "role": "reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "H-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Solid Phase Peptide Synthesis",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C31",
              "name": "Dde-Lys(Fmoc)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C32",
              "name": "HBTU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C26",
              "name": "piperidine",
              "amount": "20%",
              "role": "reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Dde-Lys-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Solid Phase Peptide Synthesis",
          "reactants": [
            {
              "compound_id": null,
              "name": "Dde-Lys-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C43",
              "name": "NOTA(2tBu)",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C35",
              "name": "HATU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C36",
              "name": "hydrazine hydrate",
              "amount": "5%",
              "role": "reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "H-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "Solid Phase Peptide Synthesis",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C27",
              "name": "Fmoc-protected amino acids",
              "amount": null
            }
          ],
          "reagents": [],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Iterative SPPS cycles."
          },
          "product": {
            "compound_id": null,
            "name": "Protected NP2-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "Resin Cleavage",
          "reactants": [
            {
              "compound_id": null,
              "name": "Protected NP2-CTC Resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C28",
              "name": "TFA",
              "amount": "1%",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DCM",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Mild cleavage retaining side-chain protecting groups."
          },
          "product": {
            "compound_id": null,
            "name": "Protected linear NP2",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 6,
          "reaction_type": "Cyclization and Deprotection",
          "reactants": [
            {
              "compound_id": null,
              "name": "Protected linear NP2",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C38",
              "name": "DPPA",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C28",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cyclization followed by global deprotection with TFA."
          },
          "product": {
            "compound_id": "C10",
            "name": "NP2",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        }
      ]
    }
  ]
}
```
##### Attempt 2
```
{
  "extraction": {
    "prompt_version": "v3.2",
    "extraction_date": "2026-03-31",
    "model_name": "gemini-3.1-pro",
    "extractor_notes": "(1) SI search result: SI found: jm5c02016_si_001.pdf. (2) SI schemes identified: Scheme S1, Scheme S2, Scheme S3, Scheme S4, Scheme S5. (3) SI compounds identified: PR7, DP2, DP3, NP2, DP1, NP1. (4) Total pathway count: 11 (main text + SI). (5) Excluded reference compounds: None identified as standard reference inhibitors needing exclusion. (6) Missing procedures: Reagent amounts and intermediate yields for the SPPS steps in SI Schemes S1-S4 are genuinely absent from all available documents, as these precursors were custom-synthesized by a commercial vendor but their synthetic routes were illustrated. (7) Mass type notes: MS observed values reflect multiply-charged ions (e.g., [M+2H]2+, [M+3H]3+) typical of large peptides."
  },
  "paper": {
    "title": "18F-/68Ga-Labeled Peptide-Based Probes for PET Imaging of ROR1 Expression",
    "authors": [
      "Tao Yang",
      "Jiahui Sun",
      "Guolong Huang",
      "Hong Wang",
      "Zhexin He",
      "Siying Lin",
      "Yanjie Wang",
      "Rongqiang Zhuang",
      "Xianzhong Zhang",
      "Hongwu Liu",
      "Zhide Guo"
    ],
    "doi": "10.1021/acs.jmedchem.5c02016",
    "journal": "Journal of Medicinal Chemistry",
    "year": 2025,
    "synthesis_scale": "lab",
    "method_completeness": "full",
    "has_synthesis": true,
    "extraction_notes": null
  },
  "compounds": [
    {
      "id": "C01",
      "name": "PR7",
      "iupac_name": null,
      "molecular_formula": "C96H133N25O31",
      "role": "intermediate",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ 1067.47",
      "ms_calculated_exact_mass": 2131.96,
      "description": "Linear peptide targeting ROR1, custom-synthesized by a vendor and used as a precursor for DP1 and NP1."
    },
    {
      "id": "C02",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Bifunctional chelator conjugated to PR7."
    },
    {
      "id": "C03",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Bifunctional chelator conjugated to PR7."
    },
    {
      "id": "C04",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": null,
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ 1260.54, [M+3H]3+ 840.68",
      "ms_calculated_exact_mass": 2518.14,
      "description": "DOTA-conjugated linear peptide precursor for 68Ga radiolabeling."
    },
    {
      "id": "C05",
      "name": "NP1",
      "iupac_name": null,
      "molecular_formula": "C108H152N28O36",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": null,
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ 1210.22, [M+3H]3+ 807.00",
      "ms_calculated_exact_mass": 2417.09,
      "description": "NOTA-conjugated linear peptide precursor for 18F radiolabeling."
    },
    {
      "id": "C06",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "intermediate",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ 1373.07, [M+3H]3+ 915.72",
      "ms_calculated_exact_mass": 2743.2514,
      "description": "DOTA-conjugated cyclic peptide precursor."
    },
    {
      "id": "C07",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "intermediate",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ 1509.05, [M+3H]3+ 1006.39",
      "ms_calculated_exact_mass": 3015.2514,
      "description": "Thioether-cyclized DOTA-conjugated peptide precursor."
    },
    {
      "id": "C08",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "intermediate",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+2H]2+ 1322.56",
      "ms_calculated_exact_mass": 2642.20,
      "description": "NOTA-conjugated cyclic peptide precursor."
    },
    {
      "id": "C09",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": null,
      "purity": "92.56% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Gallium-68 labeled linear peptide."
    },
    {
      "id": "C10",
      "name": "[68Ga]Ga-DP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": null,
      "purity": "99.45% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Gallium-68 labeled cyclic peptide."
    },
    {
      "id": "C11",
      "name": "[68Ga]Ga-DP3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": null,
      "purity": "98.46% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Gallium-68 labeled thioether-cyclized peptide."
    },
    {
      "id": "C12",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": null,
      "purity": "99.46% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "18F-aluminum-fluoride labeled linear peptide."
    },
    {
      "id": "C13",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": null,
      "purity": "99.56% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "18F-aluminum-fluoride labeled cyclic peptide."
    },
    {
      "id": "C14",
      "name": "68GaCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "ITM (68Ge-68Ga generator)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Source of Gallium-68 for radiolabeling."
    },
    {
      "id": "C15",
      "name": "sodium acetate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Buffer used to adjust pH during radiolabeling."
    },
    {
      "id": "C16",
      "name": "Fluoride-18",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Cyclone 18/9 (IBA, Belgium)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Radioisotope produced via 18O(p,n)18F reaction."
    },
    {
      "id": "C17",
      "name": "aluminum chloride",
      "iupac_name": "aluminum trichloride",
      "molecular_formula": "AlCl3",
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Source of aluminum for Al18F complexation."
    },
    {
      "id": "C18",
      "name": "DIPEA",
      "iupac_name": "N,N-diisopropylethylamine",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base used in conjugation reactions."
    },
    {
      "id": "C19",
      "name": "DMSO",
      "iupac_name": "dimethyl sulfoxide",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solvent for conjugation reactions."
    },
    {
      "id": "C20",
      "name": "HCl",
      "iupac_name": "hydrochloric acid",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Elution acid from 68Ga generator."
    },
    {
      "id": "C21",
      "name": "ethanol",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solvent for SepPak C18 elution."
    },
    {
      "id": "C22",
      "name": "acetonitrile",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solvent component in Al18F radiolabeling."
    },
    {
      "id": "C23",
      "name": "saline",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Elution solvent for QMA cartridge and final formulation."
    },
    {
      "id": "C24",
      "name": "Rink Amide MBHA Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solid support for PR7 peptide synthesis."
    },
    {
      "id": "C25",
      "name": "Fmoc-Phe-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amino acid building block."
    },
    {
      "id": "C26",
      "name": "HOBt",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling additive."
    },
    {
      "id": "C27",
      "name": "DIC",
      "iupac_name": "N,N'-diisopropylcarbodiimide",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling reagent."
    },
    {
      "id": "C28",
      "name": "DMF",
      "iupac_name": "N,N-dimethylformamide",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solvent for solid phase peptide synthesis."
    },
    {
      "id": "C29",
      "name": "Piperidine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc deprotection reagent."
    },
    {
      "id": "C30",
      "name": "Fmoc-Asp(OtBu)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amino acid building block."
    },
    {
      "id": "C31",
      "name": "Fmoc-Gly-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amino acid building block."
    },
    {
      "id": "C32",
      "name": "Fmoc-Trp(Boc)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amino acid building block."
    },
    {
      "id": "C33",
      "name": "Fmoc-Tyr(tBu)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amino acid building block."
    },
    {
      "id": "C34",
      "name": "Fmoc-Thr(tBu)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amino acid building block."
    },
    {
      "id": "C35",
      "name": "Fmoc-Ser(tBu)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amino acid building block."
    },
    {
      "id": "C36",
      "name": "Fmoc-Pro-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amino acid building block."
    },
    {
      "id": "C37",
      "name": "Fmoc-Ile-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amino acid building block."
    },
    {
      "id": "C38",
      "name": "Fmoc-Gln(Trt)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amino acid building block."
    },
    {
      "id": "C39",
      "name": "Fmoc-Arg(Pbf)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amino acid building block."
    },
    {
      "id": "C40",
      "name": "Fmoc-Asn(Trt)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amino acid building block."
    },
    {
      "id": "C41",
      "name": "TFA",
      "iupac_name": "trifluoroacetic acid",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Cleavage and global deprotection reagent."
    },
    {
      "id": "C42",
      "name": "CTC Resin",
      "iupac_name": "2-chlorotrityl chloride resin",
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solid support for synthesis of head-to-tail cyclic peptides."
    },
    {
      "id": "C43",
      "name": "Fmoc-Gly-Gly-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amino acid building block."
    },
    {
      "id": "C44",
      "name": "Dde-Lys(Fmoc)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amino acid building block with orthogonal Dde protection."
    },
    {
      "id": "C45",
      "name": "HBTU",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling reagent."
    },
    {
      "id": "C46",
      "name": "NMM",
      "iupac_name": "N-methylmorpholine",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base for SPPS coupling."
    },
    {
      "id": "C47",
      "name": "DOTA(3tBu)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Protected chelator."
    },
    {
      "id": "C48",
      "name": "HATU",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling reagent."
    },
    {
      "id": "C49",
      "name": "hydrazine hydrate",
      "iupac_name": null,
      "molecular_formula": "N2H4.H2O",
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": "5%",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Dde deprotection reagent."
    },
    {
      "id": "C50",
      "name": "DCM",
      "iupac_name": "dichloromethane",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solvent for mild resin cleavage."
    },
    {
      "id": "C51",
      "name": "DPPA",
      "iupac_name": "diphenylphosphoryl azide",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Macrolactamization reagent."
    },
    {
      "id": "C52",
      "name": "Fmoc-Cys(Trt)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amino acid building block."
    },
    {
      "id": "C53",
      "name": "Acetic anhydride",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "N-terminal acetylation reagent."
    },
    {
      "id": "C54",
      "name": "1,3-bis(bromomethyl)benzene",
      "iupac_name": "1,3-bis(bromomethyl)benzene",
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Cross-linking linker for thioether cyclization."
    },
    {
      "id": "C55",
      "name": "NH4HCO3",
      "iupac_name": "ammonium bicarbonate",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base/buffer for cyclization reaction."
    },
    {
      "id": "C56",
      "name": "NOTA-(2tBu)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Protected chelator."
    },
    {
      "id": "C57",
      "name": "H-Phe-Rink Amide MBHA Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "First coupled amino acid on resin."
    },
    {
      "id": "C58",
      "name": "H-Gly-Gly-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Resin intermediate."
    },
    {
      "id": "C59",
      "name": "Dde-Lys-Gly-Gly-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Resin intermediate."
    },
    {
      "id": "C60",
      "name": "H-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Chelator-modified resin intermediate."
    },
    {
      "id": "C61",
      "name": "H-Phe-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Resin intermediate prior to full SPPS elongation."
    },
    {
      "id": "C62",
      "name": "H-Cys(Trt)-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "First coupled amino acid on resin."
    },
    {
      "id": "C63",
      "name": "H-Phe-Cys(Trt)-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Resin intermediate prior to full SPPS elongation."
    },
    {
      "id": "C64",
      "name": "H-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Chelator-modified resin intermediate."
    },
    {
      "id": "C65",
      "name": "H-Phe-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Resin intermediate prior to full SPPS elongation."
    }
  ],
  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of PR7 (SI Scheme S1)",
      "source_section": "SI_scheme_S1",
      "target_compound_id": "C01",
      "target_compound_name": "PR7",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Solid-phase peptide synthesis (first coupling)",
          "reactants": [
            {
              "compound_id": "C24",
              "name": "Rink Amide MBHA Resin",
              "amount": null
            },
            {
              "compound_id": "C25",
              "name": "Fmoc-Phe-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C26",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C27",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C29",
              "name": "Piperidine",
              "amount": "20% in DMF",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Fmoc coupling followed by deprotection."
          },
          "product": {
            "compound_id": "C57",
            "name": "H-Phe-Rink Amide MBHA Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Solid-phase peptide synthesis (iterative couplings)",
          "reactants": [
            {
              "compound_id": "C57",
              "name": "H-Phe-Rink Amide MBHA Resin",
              "amount": null
            },
            {
              "compound_id": "C30",
              "name": "Fmoc-Asp(OtBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C31",
              "name": "Fmoc-Gly-OH",
              "amount": null
            },
            {
              "compound_id": "C32",
              "name": "Fmoc-Trp(Boc)-OH",
              "amount": null
            },
            {
              "compound_id": "C33",
              "name": "Fmoc-Tyr(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C34",
              "name": "Fmoc-Thr(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C35",
              "name": "Fmoc-Ser(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C36",
              "name": "Fmoc-Pro-OH",
              "amount": null
            },
            {
              "compound_id": "C37",
              "name": "Fmoc-Ile-OH",
              "amount": null
            },
            {
              "compound_id": "C38",
              "name": "Fmoc-Gln(Trt)-OH",
              "amount": null
            },
            {
              "compound_id": "C39",
              "name": "Fmoc-Arg(Pbf)-OH",
              "amount": null
            },
            {
              "compound_id": "C40",
              "name": "Fmoc-Asn(Trt)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C26",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C27",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C29",
              "name": "Piperidine",
              "amount": "20% in DMF",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Iterative Fmoc coupling and deprotection steps."
          },
          "product": {
            "compound_id": null,
            "name": "protected peptide on resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Amino acid sequence includes repeating residues per PR7 sequence."
        },
        {
          "step_number": 3,
          "reaction_type": "Global deprotection and cleavage",
          "reactants": [
            {
              "compound_id": null,
              "name": "protected peptide on resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C41",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cleavage from MBHA resin and removal of side-chain protecting groups."
          },
          "product": {
            "compound_id": "C01",
            "name": "PR7",
            "yield": null,
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 10.642
          },
          "purification": null,
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of DP2 (SI Scheme S2)",
      "source_section": "SI_scheme_S2",
      "target_compound_id": "C06",
      "target_compound_name": "DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Solid-phase peptide synthesis",
          "reactants": [
            {
              "compound_id": "C42",
              "name": "CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C43",
              "name": "Fmoc-Gly-Gly-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C18",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C29",
              "name": "Piperidine",
              "amount": "20% in DMF",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C58",
            "name": "H-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Solid-phase peptide synthesis",
          "reactants": [
            {
              "compound_id": "C58",
              "name": "H-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C44",
              "name": "Dde-Lys(Fmoc)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C45",
              "name": "HBTU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C46",
              "name": "NMM",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C29",
              "name": "Piperidine",
              "amount": "20% in DMF",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C59",
            "name": "Dde-Lys-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Chelator conjugation and Dde deprotection",
          "reactants": [
            {
              "compound_id": "C59",
              "name": "Dde-Lys-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C47",
              "name": "DOTA(3tBu)",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C48",
              "name": "HATU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C46",
              "name": "NMM",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C49",
              "name": "hydrazine hydrate",
              "amount": "5% in DMF",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Dde removal following DOTA coupling."
          },
          "product": {
            "compound_id": "C60",
            "name": "H-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "Solid-phase peptide synthesis",
          "reactants": [
            {
              "compound_id": "C60",
              "name": "H-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C25",
              "name": "Fmoc-Phe-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C26",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C27",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C29",
              "name": "Piperidine",
              "amount": "20% in DMF",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C61",
            "name": "H-Phe-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "Solid-phase peptide synthesis (iterative couplings)",
          "reactants": [
            {
              "compound_id": "C61",
              "name": "H-Phe-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C30",
              "name": "Fmoc-Asp(OtBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C31",
              "name": "Fmoc-Gly-OH",
              "amount": null
            },
            {
              "compound_id": "C32",
              "name": "Fmoc-Trp(Boc)-OH",
              "amount": null
            },
            {
              "compound_id": "C33",
              "name": "Fmoc-Tyr(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C34",
              "name": "Fmoc-Thr(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C35",
              "name": "Fmoc-Ser(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C36",
              "name": "Fmoc-Pro-OH",
              "amount": null
            },
            {
              "compound_id": "C37",
              "name": "Fmoc-Ile-OH",
              "amount": null
            },
            {
              "compound_id": "C38",
              "name": "Fmoc-Gln(Trt)-OH",
              "amount": null
            },
            {
              "compound_id": "C39",
              "name": "Fmoc-Arg(Pbf)-OH",
              "amount": null
            },
            {
              "compound_id": "C40",
              "name": "Fmoc-Asn(Trt)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C26",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C27",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C29",
              "name": "Piperidine",
              "amount": "20% in DMF",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "fully assembled peptide on CTC resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 6,
          "reaction_type": "Resin cleavage",
          "reactants": [
            {
              "compound_id": null,
              "name": "fully assembled peptide on CTC resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C41",
              "name": "TFA",
              "amount": "1%",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DCM",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cleaves CTC resin while preserving side-chain protecting groups."
          },
          "product": {
            "compound_id": null,
            "name": "linear protected peptide",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 7,
          "reaction_type": "Macrolactamization and global deprotection",
          "reactants": [
            {
              "compound_id": null,
              "name": "linear protected peptide",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C51",
              "name": "DPPA",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C18",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C41",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cyclization followed by global deprotection."
          },
          "product": {
            "compound_id": "C06",
            "name": "DP2",
            "yield": null,
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 10.328
          },
          "purification": null,
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Synthesis of DP3 (SI Scheme S3)",
      "source_section": "SI_scheme_S3",
      "target_compound_id": "C07",
      "target_compound_name": "DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Solid-phase peptide synthesis",
          "reactants": [
            {
              "compound_id": "C42",
              "name": "CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C52",
              "name": "Fmoc-Cys(Trt)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C18",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C29",
              "name": "Piperidine",
              "amount": "20% in DMF",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C62",
            "name": "H-Cys(Trt)-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Solid-phase peptide synthesis",
          "reactants": [
            {
              "compound_id": "C62",
              "name": "H-Cys(Trt)-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C25",
              "name": "Fmoc-Phe-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C26",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C27",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C29",
              "name": "Piperidine",
              "amount": "20% in DMF",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C63",
            "name": "H-Phe-Cys(Trt)-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Solid-phase peptide synthesis (iterative couplings) and acetylation",
          "reactants": [
            {
              "compound_id": "C63",
              "name": "H-Phe-Cys(Trt)-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C30",
              "name": "Fmoc-Asp(OtBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C31",
              "name": "Fmoc-Gly-OH",
              "amount": null
            },
            {
              "compound_id": "C32",
              "name": "Fmoc-Trp(Boc)-OH",
              "amount": null
            },
            {
              "compound_id": "C33",
              "name": "Fmoc-Tyr(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C34",
              "name": "Fmoc-Thr(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C35",
              "name": "Fmoc-Ser(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C36",
              "name": "Fmoc-Pro-OH",
              "amount": null
            },
            {
              "compound_id": "C37",
              "name": "Fmoc-Ile-OH",
              "amount": null
            },
            {
              "compound_id": "C38",
              "name": "Fmoc-Gln(Trt)-OH",
              "amount": null
            },
            {
              "compound_id": "C39",
              "name": "Fmoc-Arg(Pbf)-OH",
              "amount": null
            },
            {
              "compound_id": "C40",
              "name": "Fmoc-Asn(Trt)-OH",
              "amount": null
            },
            {
              "compound_id": "C52",
              "name": "Fmoc-Cys(Trt)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C26",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C27",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C29",
              "name": "Piperidine",
              "amount": "20% in DMF",
              "role": "base"
            },
            {
              "compound_id": "C53",
              "name": "Acetic anhydride",
              "amount": null,
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Fmoc deprotection and final N-terminal acetylation."
          },
          "product": {
            "compound_id": null,
            "name": "acetylated and protected peptide on resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "Global deprotection and cleavage",
          "reactants": [
            {
              "compound_id": null,
              "name": "acetylated and protected peptide on resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C41",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "linear dithiol peptide",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "Thioether cyclization and chelator conjugation",
          "reactants": [
            {
              "compound_id": null,
              "name": "linear dithiol peptide",
              "amount": null
            },
            {
              "compound_id": "C54",
              "name": "1,3-bis(bromomethyl)benzene",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C55",
              "name": "NH4HCO3",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Followed by reaction with DOTA derivative (details missing in OCR) to yield DP3."
          },
          "product": {
            "compound_id": "C07",
            "name": "DP3",
            "yield": null,
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 10.404
          },
          "purification": null,
          "notes": "Step 6 in the scheme shows conjugation with a DOTA-like derivative, which is fully represented here as the final precursor DP3."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Synthesis of NP2 (SI Scheme S4)",
      "source_section": "SI_scheme_S4",
      "target_compound_id": "C08",
      "target_compound_name": "NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Solid-phase peptide synthesis",
          "reactants": [
            {
              "compound_id": "C42",
              "name": "CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C43",
              "name": "Fmoc-Gly-Gly-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C18",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C29",
              "name": "Piperidine",
              "amount": "20% in DMF",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C58",
            "name": "H-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Solid-phase peptide synthesis",
          "reactants": [
            {
              "compound_id": "C58",
              "name": "H-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C44",
              "name": "Dde-Lys(Fmoc)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C45",
              "name": "HBTU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C18",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C29",
              "name": "Piperidine",
              "amount": "20% in DMF",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C59",
            "name": "Dde-Lys-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Chelator conjugation and Dde deprotection",
          "reactants": [
            {
              "compound_id": "C59",
              "name": "Dde-Lys-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C56",
              "name": "NOTA-(2tBu)",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C48",
              "name": "HATU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C18",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C49",
              "name": "hydrazine hydrate",
              "amount": "5% in DMF",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Dde removal following NOTA coupling."
          },
          "product": {
            "compound_id": "C64",
            "name": "H-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "Solid-phase peptide synthesis",
          "reactants": [
            {
              "compound_id": "C64",
              "name": "H-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C25",
              "name": "Fmoc-Phe-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C26",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C27",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C29",
              "name": "Piperidine",
              "amount": "20% in DMF",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C65",
            "name": "H-Phe-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "Solid-phase peptide synthesis (iterative couplings)",
          "reactants": [
            {
              "compound_id": "C65",
              "name": "H-Phe-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C30",
              "name": "Fmoc-Asp(OtBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C31",
              "name": "Fmoc-Gly-OH",
              "amount": null
            },
            {
              "compound_id": "C32",
              "name": "Fmoc-Trp(Boc)-OH",
              "amount": null
            },
            {
              "compound_id": "C33",
              "name": "Fmoc-Tyr(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C34",
              "name": "Fmoc-Thr(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C35",
              "name": "Fmoc-Ser(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C36",
              "name": "Fmoc-Pro-OH",
              "amount": null
            },
            {
              "compound_id": "C37",
              "name": "Fmoc-Ile-OH",
              "amount": null
            },
            {
              "compound_id": "C38",
              "name": "Fmoc-Gln(Trt)-OH",
              "amount": null
            },
            {
              "compound_id": "C39",
              "name": "Fmoc-Arg(Pbf)-OH",
              "amount": null
            },
            {
              "compound_id": "C40",
              "name": "Fmoc-Asn(Trt)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C26",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C27",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C29",
              "name": "Piperidine",
              "amount": "20% in DMF",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "fully assembled peptide on CTC resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 6,
          "reaction_type": "Resin cleavage",
          "reactants": [
            {
              "compound_id": null,
              "name": "fully assembled peptide on CTC resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C41",
              "name": "TFA",
              "amount": "1%",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DCM",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cleaves CTC resin while preserving side-chain protecting groups."
          },
          "product": {
            "compound_id": null,
            "name": "linear protected peptide",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 7,
          "reaction_type": "Macrolactamization and global deprotection",
          "reactants": [
            {
              "compound_id": null,
              "name": "linear protected peptide",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C51",
              "name": "DPPA",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C18",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C41",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cyclization followed by global deprotection."
          },
          "product": {
            "compound_id": "C08",
            "name": "NP2",
            "yield": null,
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 10.62
          },
          "purification": null,
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Synthesis of DP1 (SI Scheme S5 / Main text 5.2.1)",
      "source_section": "main_text",
      "target_compound_id": "C04",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Amidation / Chelator Conjugation",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 umol)"
            },
            {
              "compound_id": "C02",
              "name": "DOTA-NHS",
              "amount": "2.5 mg (5 umol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C18",
              "name": "DIPEA",
              "amount": "20 uL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 uL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "12 h",
            "atmosphere": null,
            "ph": null,
            "other": "Agitated in an oscillator."
          },
          "product": {
            "compound_id": "C04",
            "name": "DP1",
            "yield": "4.2 mg (55.6%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 11.23
          },
          "purification": "semipreparative HPLC with UV detection at 254 nm",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Synthesis of NP1 (SI Scheme S5 / Main text 5.2.1)",
      "source_section": "main_text",
      "target_compound_id": "C05",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Amidation / Chelator Conjugation",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 umol)"
            },
            {
              "compound_id": "C03",
              "name": "NOTA-NHS",
              "amount": "2 mg (5 umol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C18",
              "name": "DIPEA",
              "amount": "20 uL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 uL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "12 h",
            "atmosphere": null,
            "ph": null,
            "other": "Agitated in an oscillator."
          },
          "product": {
            "compound_id": "C05",
            "name": "NP1",
            "yield": "3.9 mg (54%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": 12.78
          },
          "purification": "semipreparative HPLC with UV detection at 254 nm",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP1",
      "source_section": "main_text",
      "target_compound_id": "C09",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment",
          "reactants": [
            {
              "compound_id": "C14",
              "name": "68GaCl3",
              "amount": "1 mL (0.74-1.11 GBq in 0.1 M HCl)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C15",
              "name": "sodium acetate",
              "amount": "0.5 mL (0.25 M in water)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": "4-4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "pH adjusted 68Ga solution",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Radiolabeling / Chelation",
          "reactants": [
            {
              "compound_id": null,
              "name": "pH adjusted 68Ga solution",
              "amount": null
            },
            {
              "compound_id": "C04",
              "name": "DP1",
              "amount": "50 ug (16-20 nmol)"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 uL"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": null,
            "other": "Reaction mixture cooled to room temperature before purification."
          },
          "product": {
            "compound_id": "C09",
            "name": "[68Ga]Ga-DP1",
            "yield": "89.55%",
            "purity": "92.56% RCP by radio-HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridges, ethanol elution",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P8",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP2",
      "source_section": "main_text",
      "target_compound_id": "C10",
      "target_compound_name": "[68Ga]Ga-DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment",
          "reactants": [
            {
              "compound_id": "C14",
              "name": "68GaCl3",
              "amount": "1 mL (0.74-1.11 GBq in 0.1 M HCl)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C15",
              "name": "sodium acetate",
              "amount": "0.5 mL (0.25 M in water)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": "4-4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "pH adjusted 68Ga solution",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Radiolabeling / Chelation",
          "reactants": [
            {
              "compound_id": null,
              "name": "pH adjusted 68Ga solution",
              "amount": null
            },
            {
              "compound_id": "C06",
              "name": "DP2",
              "amount": "50 ug (16-20 nmol)"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 uL"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": null,
            "other": "Reaction mixture cooled to room temperature before purification."
          },
          "product": {
            "compound_id": "C10",
            "name": "[68Ga]Ga-DP2",
            "yield": "97.67%",
            "purity": "99.45% RCP by radio-HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridges, ethanol elution",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P9",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP3",
      "source_section": "main_text",
      "target_compound_id": "C11",
      "target_compound_name": "[68Ga]Ga-DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment",
          "reactants": [
            {
              "compound_id": "C14",
              "name": "68GaCl3",
              "amount": "1 mL (0.74-1.11 GBq in 0.1 M HCl)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C15",
              "name": "sodium acetate",
              "amount": "0.5 mL (0.25 M in water)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": "4-4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "pH adjusted 68Ga solution",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Radiolabeling / Chelation",
          "reactants": [
            {
              "compound_id": null,
              "name": "pH adjusted 68Ga solution",
              "amount": null
            },
            {
              "compound_id": "C07",
              "name": "DP3",
              "amount": "50 ug (16-20 nmol)"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 uL"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": null,
            "other": "Reaction mixture cooled to room temperature before purification."
          },
          "product": {
            "compound_id": "C11",
            "name": "[68Ga]Ga-DP3",
            "yield": "98.01%",
            "purity": "98.46% RCP by radio-HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridges, ethanol elution",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P10",
      "pathway_name": "Radiolabeling of [18F]AlF-NP1",
      "source_section": "main_text",
      "target_compound_id": "C12",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Trapping and Elution",
          "reactants": [
            {
              "compound_id": "C16",
              "name": "Fluoride-18",
              "amount": "0.74-1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline",
              "volume": "0.2 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Trapped on a preconditioned QMA cartridge and eluted with saline."
          },
          "product": {
            "compound_id": null,
            "name": "18F- eluate",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Radiolabeling / AlF complexation",
          "reactants": [
            {
              "compound_id": null,
              "name": "18F- eluate",
              "amount": null
            },
            {
              "compound_id": "C05",
              "name": "NP1",
              "amount": "50 ug (18-25 nmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C17",
              "name": "aluminum chloride",
              "amount": "3 uL of 2 mM",
              "role": "radionuclide_source"
            },
            {
              "compound_id": "C15",
              "name": "sodium acetate buffer",
              "amount": "100 uL (0.1 M)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": "200 uL"
            },
            {
              "name": "DMSO",
              "volume": "50 uL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": "4.0",
            "other": "Cooled to RT before purification; final product resolved in saline after ethanol removal."
          },
          "product": {
            "compound_id": "C12",
            "name": "[18F]AlF-NP1",
            "yield": "62.58%",
            "purity": "99.46% RCP by radio-HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridges, ethanol elution",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P11",
      "pathway_name": "Radiolabeling of [18F]AlF-NP2",
      "source_section": "main_text",
      "target_compound_id": "C13",
      "target_compound_name": "[18F]AlF-NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Trapping and Elution",
          "reactants": [
            {
              "compound_id": "C16",
              "name": "Fluoride-18",
              "amount": "0.74-1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline",
              "volume": "0.2 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": "Trapped on a preconditioned QMA cartridge and eluted with saline."
          },
          "product": {
            "compound_id": null,
            "name": "18F- eluate",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Radiolabeling / AlF complexation",
          "reactants": [
            {
              "compound_id": null,
              "name": "18F- eluate",
              "amount": null
            },
            {
              "compound_id": "C08",
              "name": "NP2",
              "amount": "50 ug (18-25 nmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C17",
              "name": "aluminum chloride",
              "amount": "3 uL of 2 mM",
              "role": "radionuclide_source"
            },
            {
              "compound_id": "C15",
              "name": "sodium acetate buffer",
              "amount": "100 uL (0.1 M)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": "200 uL"
            },
            {
              "name": "DMSO",
              "volume": "50 uL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "atmosphere": null,
            "ph": "4.0",
            "other": "Cooled to RT before purification; final product resolved in saline after ethanol removal."
          },
          "product": {
            "compound_id": "C13",
            "name": "[18F]AlF-NP2",
            "yield": "62.76%",
            "purity": "99.56% RCP by radio-HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridges, ethanol elution",
          "notes": null
        }
      ]
    }
  ]
}
```
##### Attempt 3
```
{
  "extraction": {
    "prompt_version": "v3.2",
    "extraction_date": "2025-01-20",
    "model_name": "gemini-2.5-pro",
    "extractor_notes": "SI found: jm5c02016_si_001.pdf. SI schemes identified: S1, S2, S3, S4, S5. SI compounds identified: PR7, DP1, DP2, DP3, NP1, NP2. Total pathway count: 11 (including 7 main text radiolabeling/conjugation and 4 SI SPPS schemes). Excluded reference compounds: none. Procedures genuinely absent: detailed iterative steps for SPPS are condensed into grouped steps based on schemes. Mass type notes: Exact masses calculated and found are provided in Section 5.2."
  },
  "paper": {
    "title": "18F-/68Ga-Labeled Peptide-Based Probes for PET Imaging of ROR1 Expression",
    "authors": [
      "Tao Yang",
      "Jiahui Sun",
      "Guolong Huang",
      "Hong Wang",
      "Zhexin He",
      "Siying Lin",
      "Yanjie Wang",
      "Rongqiang Zhuang",
      "Xianzhong Zhang",
      "Hongwu Liu",
      "Zhide Guo"
    ],
    "doi": "10.1021/acs.jmedchem.5c02016",
    "journal": "Journal of Medicinal Chemistry",
    "year": 2025,
    "synthesis_scale": "lab",
    "method_completeness": "full",
    "has_synthesis": true,
    "extraction_notes": "Synthesis covers both the conjugation/radiolabeling from the main text and the solid-phase peptide syntheses detailed in SI schemes."
  },
  "compounds": [
    {
      "id": "C01",
      "name": "PR7",
      "iupac_name": null,
      "molecular_formula": "C96H133N25O31",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": ">95% pure by HPLC",
      "ms_observed": "[M+2H]2+ 1067.47",
      "ms_calculated_exact_mass": 2131.96,
      "description": "Linear ROR1-targeted peptide precursor used for subsequent conjugation."
    },
    {
      "id": "C02",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Chelator ester used for conjugation to PR7."
    },
    {
      "id": "C03",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Chelator ester used for conjugation to PR7."
    },
    {
      "id": "C04",
      "name": "DIPEA",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base used in conjugation and solid phase synthesis."
    },
    {
      "id": "C05",
      "name": "DMSO",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solvent for conjugation and radiolabeling."
    },
    {
      "id": "C06",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% pure by HPLC",
      "ms_observed": "[M+2H]2+ 1260.54, [M+3H]3+ 840.68",
      "ms_calculated_exact_mass": 2518.14,
      "description": "DOTA-conjugated linear peptide precursor for 68Ga radiolabeling."
    },
    {
      "id": "C07",
      "name": "NP1",
      "iupac_name": null,
      "molecular_formula": "C108H152N28O36",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% pure by HPLC",
      "ms_observed": "[M+2H]2+ 1210.22, [M+3H]3+ 807.00",
      "ms_calculated_exact_mass": 2417.09,
      "description": "NOTA-conjugated linear peptide precursor for 18F radiolabeling."
    },
    {
      "id": "C08",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": ">95% pure by HPLC",
      "ms_observed": "[M+2H]2+ 1373.07, [M+3H]3+ 915.72",
      "ms_calculated_exact_mass": 2743.2514,
      "description": "Custom synthesized cyclic peptide precursor conjugated with DOTA."
    },
    {
      "id": "C09",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": ">95% pure by HPLC",
      "ms_observed": "[M+2H]2+ 1509.05, [M+3H]3+ 1006.39",
      "ms_calculated_exact_mass": 3015.2514,
      "description": "Custom synthesized cyclic peptide precursor conjugated with DOTA."
    },
    {
      "id": "C10",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "purity": ">95% pure by HPLC",
      "ms_observed": "[M+2H]2+ 1322.56",
      "ms_calculated_exact_mass": 2642.20,
      "description": "Custom synthesized cyclic peptide precursor conjugated with NOTA."
    },
    {
      "id": "C11",
      "name": "68GaCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "ITM generator",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Radionuclide source for 68Ga labeling."
    },
    {
      "id": "C12",
      "name": "sodium acetate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Buffer used to adjust pH in radiolabeling reactions."
    },
    {
      "id": "C13",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "92.56% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "68Ga-radiolabeled linear peptide probe."
    },
    {
      "id": "C14",
      "name": "[68Ga]Ga-DP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "99.45% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "68Ga-radiolabeled cyclic peptide probe."
    },
    {
      "id": "C15",
      "name": "[68Ga]Ga-DP3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "98.46% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "68Ga-radiolabeled cyclic peptide probe."
    },
    {
      "id": "C16",
      "name": "Fluoride-18",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Cyclone 18/9 (IBA)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Radionuclide source for 18F labeling."
    },
    {
      "id": "C17",
      "name": "AlCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Used to form the [18F]AlF complex."
    },
    {
      "id": "C18",
      "name": "acetonitrile",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Cosolvent used during 18F labeling."
    },
    {
      "id": "C19",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "99.46% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "18F-radiolabeled linear peptide probe."
    },
    {
      "id": "C20",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "99.56% RCP by radio-HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "18F-radiolabeled cyclic peptide probe."
    },
    {
      "id": "C21",
      "name": "Rink Amide MBHA Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solid support for SPPS of PR7 (SI Scheme S1)."
    },
    {
      "id": "C22",
      "name": "Fmoc-Phe-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "First amino acid coupled in SPPS (SI Schemes)."
    },
    {
      "id": "C23",
      "name": "HOBt",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling additive in SPPS."
    },
    {
      "id": "C24",
      "name": "DIC",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling reagent in SPPS."
    },
    {
      "id": "C25",
      "name": "DMF",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solvent for SPPS."
    },
    {
      "id": "C26",
      "name": "piperidine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc deprotection reagent in SPPS."
    },
    {
      "id": "C27",
      "name": "Fmoc-Asp(OtBu)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-protected amino acid used in SPPS."
    },
    {
      "id": "C28",
      "name": "Fmoc-Gly-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-protected amino acid used in SPPS."
    },
    {
      "id": "C29",
      "name": "Fmoc-Trp(Boc)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-protected amino acid used in SPPS."
    },
    {
      "id": "C30",
      "name": "Fmoc-Tyr(tBu)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-protected amino acid used in SPPS."
    },
    {
      "id": "C31",
      "name": "Fmoc-Thr(tBu)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-protected amino acid used in SPPS."
    },
    {
      "id": "C32",
      "name": "Fmoc-Ser(tBu)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-protected amino acid used in SPPS."
    },
    {
      "id": "C33",
      "name": "Fmoc-Pro-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-protected amino acid used in SPPS."
    },
    {
      "id": "C34",
      "name": "Fmoc-Ile-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-protected amino acid used in SPPS."
    },
    {
      "id": "C35",
      "name": "Fmoc-Gln(Trt)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-protected amino acid used in SPPS."
    },
    {
      "id": "C36",
      "name": "Fmoc-Arg(Pbf)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-protected amino acid used in SPPS."
    },
    {
      "id": "C37",
      "name": "Fmoc-Asn(Trt)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fmoc-protected amino acid used in SPPS."
    },
    {
      "id": "C38",
      "name": "TFA",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Cleavage and global deprotection reagent in SPPS."
    },
    {
      "id": "C39",
      "name": "CTC Resin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "2-Chlorotrityl chloride resin used as solid support for SI Schemes S2-S4."
    },
    {
      "id": "C40",
      "name": "Fmoc-Gly-Gly-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Dipeptide loaded onto CTC resin in SI Schemes S2 and S4."
    },
    {
      "id": "C41",
      "name": "Dde-Lys(Fmoc)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Orthogonally protected lysine derivative for branching."
    },
    {
      "id": "C42",
      "name": "HBTU",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling reagent."
    },
    {
      "id": "C43",
      "name": "NMM",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base used in SPPS couplings."
    },
    {
      "id": "C44",
      "name": "DOTA(3tBu)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Protected chelator coupled to the peptide sequence."
    },
    {
      "id": "C45",
      "name": "HATU",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Coupling reagent."
    },
    {
      "id": "C46",
      "name": "hydrazine hydrate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Reagent for selective removal of the Dde protecting group."
    },
    {
      "id": "C47",
      "name": "DCM",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Solvent for mild cleavage from CTC resin."
    },
    {
      "id": "C48",
      "name": "DPPA",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Cyclization reagent (diphenylphosphoryl azide)."
    },
    {
      "id": "C49",
      "name": "Fmoc-Cys(Trt)-OH",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Cysteine derivative for SPPS."
    },
    {
      "id": "C50",
      "name": "Acetanhydride",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "N-terminal capping reagent."
    },
    {
      "id": "C51",
      "name": "1,3-bis(bromomethyl)benzene",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Linker precursor used in Scheme S3."
    },
    {
      "id": "C52",
      "name": "2-aminoethanethiol",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Conjugation component for linker synthesis in Scheme S3."
    },
    {
      "id": "C53",
      "name": "NH4HCO3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base/buffer used for cyclization and conjugation in Scheme S3."
    },
    {
      "id": "C54",
      "name": "NOTA-(2tBu)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Protected NOTA chelator used in Scheme S4."
    },
    {
      "id": "C55",
      "name": "HCl",
      "iupac_name": "hydrochloric acid",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acid used to elute Ga-68."
    }
  ],
  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of DP1",
      "source_section": "main_text",
      "target_compound_id": "C06",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Amide Coupling",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 umol)"
            },
            {
              "compound_id": "C02",
              "name": "DOTA-NHS",
              "amount": "2.5 mg (5 umol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": "20 uL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 uL"
            }
          ],
          "conditions": {
            "temperature": "RT",
            "time": "12 h",
            "atmosphere": null,
            "ph": null,
            "other": "Agitated in an oscillator."
          },
          "product": {
            "compound_id": "C06",
            "name": "DP1",
            "yield": "4.2 mg (55.6%)",
            "purity": ">95% pure by HPLC",
            "hplc_retention_time_min": 11.23
          },
          "purification": "semipreparative HPLC",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of NP1",
      "source_section": "main_text",
      "target_compound_id": "C07",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Amide Coupling",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 umol)"
            },
            {
              "compound_id": "C03",
              "name": "NOTA-NHS",
              "amount": "2 mg (5 umol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": "20 uL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 uL"
            }
          ],
          "conditions": {
            "temperature": "RT",
            "time": "12 h",
            "atmosphere": null,
            "ph": null,
            "other": "Agitated in an oscillator."
          },
          "product": {
            "compound_id": "C07",
            "name": "NP1",
            "yield": "3.9 mg (54%)",
            "purity": ">95% pure by HPLC",
            "hplc_retention_time_min": 12.78
          },
          "purification": "semipreparative HPLC",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Preparation of [68Ga]Ga-DP1",
      "source_section": "main_text",
      "target_compound_id": "C13",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Radiometal Chelation",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "68GaCl3",
              "amount": "0.74-1.11 GBq"
            },
            {
              "compound_id": "C06",
              "name": "DP1",
              "amount": "50 ug (16-20 nmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C55",
              "name": "HCl",
              "amount": "1 mL of 0.1 M",
              "role": "acid"
            },
            {
              "compound_id": "C12",
              "name": "sodium acetate",
              "amount": "0.5 mL of 0.25 M",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 uL"
            }
          ],
          "conditions": {
            "temperature": "95°C",
            "time": "20 min",
            "atmosphere": null,
            "ph": "4-4.5",
            "other": "Cooled to room temperature prior to purification."
          },
          "product": {
            "compound_id": "C13",
            "name": "[68Ga]Ga-DP1",
            "yield": "89.55%",
            "purity": "92.56% RCP by radio-HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge, ethanol elution",
          "notes": "RCY and RCP values are from Table S1."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Preparation of [68Ga]Ga-DP2",
      "source_section": "main_text",
      "target_compound_id": "C14",
      "target_compound_name": "[68Ga]Ga-DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Radiometal Chelation",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "68GaCl3",
              "amount": "0.74-1.11 GBq"
            },
            {
              "compound_id": "C08",
              "name": "DP2",
              "amount": "50 ug (16-20 nmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C55",
              "name": "HCl",
              "amount": "1 mL of 0.1 M",
              "role": "acid"
            },
            {
              "compound_id": "C12",
              "name": "sodium acetate",
              "amount": "0.5 mL of 0.25 M",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 uL"
            }
          ],
          "conditions": {
            "temperature": "95°C",
            "time": "20 min",
            "atmosphere": null,
            "ph": "4-4.5",
            "other": "Cooled to room temperature prior to purification."
          },
          "product": {
            "compound_id": "C14",
            "name": "[68Ga]Ga-DP2",
            "yield": "97.67%",
            "purity": "99.45% RCP by radio-HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge, ethanol elution",
          "notes": "RCY and RCP values are from Table S1."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Preparation of [68Ga]Ga-DP3",
      "source_section": "main_text",
      "target_compound_id": "C15",
      "target_compound_name": "[68Ga]Ga-DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Radiometal Chelation",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "68GaCl3",
              "amount": "0.74-1.11 GBq"
            },
            {
              "compound_id": "C09",
              "name": "DP3",
              "amount": "50 ug (16-20 nmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C55",
              "name": "HCl",
              "amount": "1 mL of 0.1 M",
              "role": "acid"
            },
            {
              "compound_id": "C12",
              "name": "sodium acetate",
              "amount": "0.5 mL of 0.25 M",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 uL"
            }
          ],
          "conditions": {
            "temperature": "95°C",
            "time": "20 min",
            "atmosphere": null,
            "ph": "4-4.5",
            "other": "Cooled to room temperature prior to purification."
          },
          "product": {
            "compound_id": "C15",
            "name": "[68Ga]Ga-DP3",
            "yield": "98.01%",
            "purity": "98.46% RCP by radio-HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge, ethanol elution",
          "notes": "RCY and RCP values are from Table S1."
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Preparation of [18F]AlF-NP1",
      "source_section": "main_text",
      "target_compound_id": "C19",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Radiolabeling",
          "reactants": [
            {
              "compound_id": "C16",
              "name": "Fluoride-18",
              "amount": "0.74-1.11 GBq"
            },
            {
              "compound_id": "C07",
              "name": "NP1",
              "amount": "50 ug (18-25 nmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C17",
              "name": "AlCl3",
              "amount": "3 uL of 2 mM",
              "role": "other"
            },
            {
              "compound_id": "C12",
              "name": "sodium acetate buffer",
              "amount": "100 uL of 0.1 M",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": "200 uL"
            },
            {
              "name": "DMSO",
              "volume": "50 uL"
            }
          ],
          "conditions": {
            "temperature": "100°C",
            "time": "20 min",
            "atmosphere": null,
            "ph": "4.0",
            "other": "Cooled to room temperature."
          },
          "product": {
            "compound_id": "C19",
            "name": "[18F]AlF-NP1",
            "yield": "62.58%",
            "purity": "99.46% RCP by radio-HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge, ethanol elution",
          "notes": "Ethanol solvent was subsequently removed and product resolved in saline. RCY and RCP values from Table S1."
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Preparation of [18F]AlF-NP2",
      "source_section": "main_text",
      "target_compound_id": "C20",
      "target_compound_name": "[18F]AlF-NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Radiolabeling",
          "reactants": [
            {
              "compound_id": "C16",
              "name": "Fluoride-18",
              "amount": "0.74-1.11 GBq"
            },
            {
              "compound_id": "C10",
              "name": "NP2",
              "amount": "50 ug (18-25 nmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C17",
              "name": "AlCl3",
              "amount": "3 uL of 2 mM",
              "role": "other"
            },
            {
              "compound_id": "C12",
              "name": "sodium acetate buffer",
              "amount": "100 uL of 0.1 M",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": "200 uL"
            },
            {
              "name": "DMSO",
              "volume": "50 uL"
            }
          ],
          "conditions": {
            "temperature": "100°C",
            "time": "20 min",
            "atmosphere": null,
            "ph": "4.0",
            "other": "Cooled to room temperature."
          },
          "product": {
            "compound_id": "C20",
            "name": "[18F]AlF-NP2",
            "yield": "62.76%",
            "purity": "99.56% RCP by radio-HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge, ethanol elution",
          "notes": "Ethanol solvent was subsequently removed and product resolved in saline. RCY and RCP values from Table S1."
        }
      ]
    },
    {
      "pathway_id": "P8",
      "pathway_name": "Synthesis of PR7 (SI Scheme S1)",
      "source_section": "SI_scheme_S1",
      "target_compound_id": "C01",
      "target_compound_name": "PR7",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Solid Phase Peptide Synthesis (Resin Loading)",
          "reactants": [
            {
              "compound_id": "C21",
              "name": "Rink Amide MBHA Resin",
              "amount": null
            },
            {
              "compound_id": "C22",
              "name": "Fmoc-Phe-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C23",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C24",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C26",
              "name": "piperidine",
              "amount": "20%",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "H-Phe-Rink Amide MBHA Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "First amino acid loading and Fmoc deprotection."
        },
        {
          "step_number": 2,
          "reaction_type": "Solid Phase Peptide Synthesis (Iterative Coupling)",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Phe-Rink Amide MBHA Resin",
              "amount": null
            },
            {
              "compound_id": "C27",
              "name": "Fmoc-Asp(OtBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C28",
              "name": "Fmoc-Gly-OH",
              "amount": null
            },
            {
              "compound_id": "C29",
              "name": "Fmoc-Trp(Boc)-OH",
              "amount": null
            },
            {
              "compound_id": "C30",
              "name": "Fmoc-Tyr(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C31",
              "name": "Fmoc-Thr(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C32",
              "name": "Fmoc-Ser(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C33",
              "name": "Fmoc-Pro-OH",
              "amount": null
            },
            {
              "compound_id": "C34",
              "name": "Fmoc-Ile-OH",
              "amount": null
            },
            {
              "compound_id": "C35",
              "name": "Fmoc-Gln(Trt)-OH",
              "amount": null
            },
            {
              "compound_id": "C36",
              "name": "Fmoc-Arg(Pbf)-OH",
              "amount": null
            },
            {
              "compound_id": "C37",
              "name": "Fmoc-Asn(Trt)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C23",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C24",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C26",
              "name": "piperidine",
              "amount": "20%",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Linear protected peptide on MBHA resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Iterative SPPS repeating the coupling conditions of step 1."
        },
        {
          "step_number": 3,
          "reaction_type": "Cleavage and Deprotection",
          "reactants": [
            {
              "compound_id": null,
              "name": "Linear protected peptide on MBHA resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C38",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C01",
            "name": "PR7",
            "yield": null,
            "purity": ">95% pure by HPLC",
            "hplc_retention_time_min": 10.642
          },
          "purification": null,
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P9",
      "pathway_name": "Synthesis of DP2 (SI Scheme S2)",
      "source_section": "SI_scheme_S2",
      "target_compound_id": "C08",
      "target_compound_name": "DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Solid Phase Peptide Synthesis (Resin Loading)",
          "reactants": [
            {
              "compound_id": "C39",
              "name": "CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C40",
              "name": "Fmoc-Gly-Gly-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C26",
              "name": "piperidine",
              "amount": "20%",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "H-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Amide Coupling",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C41",
              "name": "Dde-Lys(Fmoc)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C42",
              "name": "HBTU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C43",
              "name": "NMM",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C26",
              "name": "piperidine",
              "amount": "20%",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Dde-Lys-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Amide Coupling & Dde Deprotection",
          "reactants": [
            {
              "compound_id": null,
              "name": "Dde-Lys-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C44",
              "name": "DOTA(3tBu)",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C45",
              "name": "HATU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C43",
              "name": "NMM",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C46",
              "name": "hydrazine hydrate",
              "amount": "5%",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "H-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Hydrazine removes the Dde protecting group to expose the free amine for subsequent chain elongation."
        },
        {
          "step_number": 4,
          "reaction_type": "Solid Phase Peptide Synthesis (Iterative Coupling)",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Lys[DOTA(3tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C22",
              "name": "Fmoc-Phe-OH",
              "amount": null
            },
            {
              "compound_id": "C27",
              "name": "Fmoc-Asp(OtBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C28",
              "name": "Fmoc-Gly-OH",
              "amount": null
            },
            {
              "compound_id": "C29",
              "name": "Fmoc-Trp(Boc)-OH",
              "amount": null
            },
            {
              "compound_id": "C30",
              "name": "Fmoc-Tyr(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C31",
              "name": "Fmoc-Thr(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C32",
              "name": "Fmoc-Ser(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C33",
              "name": "Fmoc-Pro-OH",
              "amount": null
            },
            {
              "compound_id": "C34",
              "name": "Fmoc-Ile-OH",
              "amount": null
            },
            {
              "compound_id": "C35",
              "name": "Fmoc-Gln(Trt)-OH",
              "amount": null
            },
            {
              "compound_id": "C36",
              "name": "Fmoc-Arg(Pbf)-OH",
              "amount": null
            },
            {
              "compound_id": "C37",
              "name": "Fmoc-Asn(Trt)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C23",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C24",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C26",
              "name": "piperidine",
              "amount": "20%",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Linear protected peptide on CTC resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "Mild Cleavage",
          "reactants": [
            {
              "compound_id": null,
              "name": "Linear protected peptide on CTC resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C38",
              "name": "TFA",
              "amount": "1%",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DCM",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Cleaved linear protected peptide",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Mild cleavage to retain side-chain protecting groups prior to cyclization."
        },
        {
          "step_number": 6,
          "reaction_type": "Macrocyclization and Global Deprotection",
          "reactants": [
            {
              "compound_id": null,
              "name": "Cleaved linear protected peptide",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C48",
              "name": "DPPA",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C38",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C08",
            "name": "DP2",
            "yield": null,
            "purity": ">95% pure by HPLC",
            "hplc_retention_time_min": 10.328
          },
          "purification": null,
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P10",
      "pathway_name": "Synthesis of DP3 (SI Scheme S3)",
      "source_section": "SI_scheme_S3",
      "target_compound_id": "C09",
      "target_compound_name": "DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Solid Phase Peptide Synthesis (Resin Loading)",
          "reactants": [
            {
              "compound_id": "C39",
              "name": "CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C49",
              "name": "Fmoc-Cys(Trt)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C26",
              "name": "piperidine",
              "amount": "20%",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "H-Cys(Trt)-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Solid Phase Peptide Synthesis (Iterative Coupling)",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Cys(Trt)-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C22",
              "name": "Fmoc-Phe-OH",
              "amount": null
            },
            {
              "compound_id": "C27",
              "name": "Fmoc-Asp(OtBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C28",
              "name": "Fmoc-Gly-OH",
              "amount": null
            },
            {
              "compound_id": "C29",
              "name": "Fmoc-Trp(Boc)-OH",
              "amount": null
            },
            {
              "compound_id": "C30",
              "name": "Fmoc-Tyr(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C31",
              "name": "Fmoc-Thr(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C32",
              "name": "Fmoc-Ser(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C33",
              "name": "Fmoc-Pro-OH",
              "amount": null
            },
            {
              "compound_id": "C34",
              "name": "Fmoc-Ile-OH",
              "amount": null
            },
            {
              "compound_id": "C35",
              "name": "Fmoc-Gln(Trt)-OH",
              "amount": null
            },
            {
              "compound_id": "C36",
              "name": "Fmoc-Arg(Pbf)-OH",
              "amount": null
            },
            {
              "compound_id": "C37",
              "name": "Fmoc-Asn(Trt)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C23",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C24",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C26",
              "name": "piperidine",
              "amount": "20%",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Linear peptide on resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Acetylation",
          "reactants": [
            {
              "compound_id": null,
              "name": "Linear peptide on resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C50",
              "name": "Acetanhydride",
              "amount": null,
              "role": "other"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Ac-peptide on resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "Cleavage and Deprotection",
          "reactants": [
            {
              "compound_id": null,
              "name": "Ac-peptide on resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C38",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Cleaved Ac-peptide with free thiols",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "Conjugation",
          "reactants": [
            {
              "compound_id": null,
              "name": "Cleaved Ac-peptide with free thiols",
              "amount": null
            },
            {
              "compound_id": "C51",
              "name": "1,3-bis(bromomethyl)benzene",
              "amount": null
            },
            {
              "compound_id": "C52",
              "name": "2-aminoethanethiol",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C53",
              "name": "NH4HCO3",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Linker-conjugated intermediate",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 6,
          "reaction_type": "Cyclization",
          "reactants": [
            {
              "compound_id": null,
              "name": "Linker-conjugated intermediate",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C53",
              "name": "NH4HCO3",
              "amount": null,
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C09",
            "name": "DP3",
            "yield": null,
            "purity": ">95% pure by HPLC",
            "hplc_retention_time_min": 10.404
          },
          "purification": null,
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P11",
      "pathway_name": "Synthesis of NP2 (SI Scheme S4)",
      "source_section": "SI_scheme_S4",
      "target_compound_id": "C10",
      "target_compound_name": "NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Solid Phase Peptide Synthesis (Resin Loading)",
          "reactants": [
            {
              "compound_id": "C39",
              "name": "CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C40",
              "name": "Fmoc-Gly-Gly-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C26",
              "name": "piperidine",
              "amount": "20%",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "H-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Amide Coupling",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C41",
              "name": "Dde-Lys(Fmoc)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C42",
              "name": "HBTU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C26",
              "name": "piperidine",
              "amount": "20%",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Dde-Lys-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Amide Coupling & Dde Deprotection",
          "reactants": [
            {
              "compound_id": null,
              "name": "Dde-Lys-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C54",
              "name": "NOTA-(2tBu)",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C45",
              "name": "HATU",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C46",
              "name": "hydrazine hydrate",
              "amount": "5%",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "H-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Hydrazine removes the Dde protecting group to expose the free amine for subsequent chain elongation."
        },
        {
          "step_number": 4,
          "reaction_type": "Solid Phase Peptide Synthesis (Iterative Coupling)",
          "reactants": [
            {
              "compound_id": null,
              "name": "H-Lys[NOTA(2tBu)]-Gly-Gly-CTC Resin",
              "amount": null
            },
            {
              "compound_id": "C22",
              "name": "Fmoc-Phe-OH",
              "amount": null
            },
            {
              "compound_id": "C27",
              "name": "Fmoc-Asp(OtBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C28",
              "name": "Fmoc-Gly-OH",
              "amount": null
            },
            {
              "compound_id": "C29",
              "name": "Fmoc-Trp(Boc)-OH",
              "amount": null
            },
            {
              "compound_id": "C30",
              "name": "Fmoc-Tyr(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C31",
              "name": "Fmoc-Thr(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C32",
              "name": "Fmoc-Ser(tBu)-OH",
              "amount": null
            },
            {
              "compound_id": "C33",
              "name": "Fmoc-Pro-OH",
              "amount": null
            },
            {
              "compound_id": "C34",
              "name": "Fmoc-Ile-OH",
              "amount": null
            },
            {
              "compound_id": "C35",
              "name": "Fmoc-Gln(Trt)-OH",
              "amount": null
            },
            {
              "compound_id": "C36",
              "name": "Fmoc-Arg(Pbf)-OH",
              "amount": null
            },
            {
              "compound_id": "C37",
              "name": "Fmoc-Asn(Trt)-OH",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C23",
              "name": "HOBt",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C24",
              "name": "DIC",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C26",
              "name": "piperidine",
              "amount": "20%",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Linear protected peptide on CTC resin",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "Mild Cleavage",
          "reactants": [
            {
              "compound_id": null,
              "name": "Linear protected peptide on CTC resin",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C38",
              "name": "TFA",
              "amount": "1%",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DCM",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "Cleaved linear protected peptide",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "Mild cleavage to retain side-chain protecting groups prior to cyclization."
        },
        {
          "step_number": 6,
          "reaction_type": "Macrocyclization and Global Deprotection",
          "reactants": [
            {
              "compound_id": null,
              "name": "Cleaved linear protected peptide",
              "amount": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C48",
              "name": "DPPA",
              "amount": null,
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": null,
              "role": "base"
            },
            {
              "compound_id": "C38",
              "name": "TFA",
              "amount": null,
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C10",
            "name": "NP2",
            "yield": null,
            "purity": ">95% pure by HPLC",
            "hplc_retention_time_min": 10.62
          },
          "purification": null,
          "notes": null
        }
      ]
    }
  ]
}
```

## a-nucleoside-analogue-bearing-a-c2-stereogenic-all-carbon-quaternary-center-for-the-treatment-of-heart-failure

#### Claude

##### Attempt 1
```
{
  "extraction": {
    "prompt_version": "v3.2",
    "extraction_date": "2026-03-30",
    "model_name": "claude-sonnet-4-6",
    "extractor_notes": "SI found: document named 'jm5c01999_si_001.pdf'. The SI contains: Supplementary Figures S1–S14, Stereochemical Proofs (including X-ray crystal data for S3), and NMR spectra pages S18–S119, and HPLC-UV chromatograms S120–S122. SI schemes identified: NONE — the SI contains no synthesis schemes and no additional experimental procedures. All synthetic procedures appear in the main text Experimental Section. SI compounds identified (author labels referenced in main text as pre-synthesized or co-products): S1 (benzoylated sugar, cited as ref 31, not re-synthesized here); S2, S3, S4, S5, S6, S7, S8, S9, S10 (ref 45 substrate), S11, S12, S13, S14 (ref 31 substrate), S15, S16a/b, S17a/b, S18a/b, S19a/b, S20a/b, S21a, S21b, S22, S23a/b (ref 31 substrate), S24, S25, S26, S27, S28. Total pathway count: 9 main-text pathways (P1–P9 for final compounds 11–19); no SI pathways. Excluded reference compounds (no synthetic role in this study, cited for comparison or pharmacology only): AMP (adenosine monophosphate, cited as natural endogenous ligand), doxorubicin/Dox (used as pharmacological stressor, not synthesized), imatinib mesylate (pharmacological stressor), compound C (AMPK inhibitor, commercial), MK-8722 (cited comparator), AICA riboside (cited comparator), metformin (cited comparator), dexrazoxane (cited comparator). Mass type notes: all masses reported are exact masses by HRMS (ESI) using Hybrid Quadrupole-Orbitrap; masses for small molecules (MW < 700) — monoisotopic masses apply."
  },

  "paper": {
    "title": "A Nucleoside Analogue Bearing a C2′-Stereogenic All-Carbon Quaternary Center for the Treatment of Heart Failure",
    "authors": [
      "Abir Almazloum",
      "Wael Maharsy",
      "Starr Dostie",
      "Fabiola Becerril-Jiménez",
      "Carla Eymard",
      "Hiba Komati",
      "Louis Leblanc",
      "Amarender Manchoju",
      "Philippe Mochirian",
      "Renaud Zelli",
      "Michel Prevost",
      "Mona Nemer",
      "Yvan Guindon"
    ],
    "doi": "10.1021/acs.jmedchem.5c01999",
    "journal": "Journal of Medicinal Chemistry",
    "year": 2025,
    "synthesis_scale": "lab",
    "method_completeness": "full",
    "has_synthesis": true,
    "extraction_notes": "All synthesis procedures are in the main text Experimental Section. Starting materials S1, S10, S14, and S23a,b are cited to prior publications (refs 31 and 45) and not synthesized in this paper; they are treated as starting_materials. S4 is described as 'previously reported nucleoside S4 (ref 32)' but is also generated as co-product in the S2 ammonolysis step. Compound 12 was obtained in low yield (22%) due to two-step sequence. Purity for all final compounds 11–19 is stated as >95% by HPLC. No SI synthesis schemes exist."
  },

  "compounds": [
    {
      "id": "C01",
      "name": "S1 (benzoylated sugar, 3,4-anti lactone precursor)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Prepared according to ref 31 (Becerril-Jiménez et al., J. Org. Chem. 2019)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Benzoylated sugar lactone starting material (3,4-anti series) used as the glycosyl donor in the N-glycosylation step to form nucleoside S2; prepared in-house according to a prior publication."
    },
    {
      "id": "C02",
      "name": "2,6-dichloropurine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Heterocyclic base used as nucleophile/nucleobase in N-glycosylation reactions to install the 2,6-dichloropurine moiety."
    },
    {
      "id": "C03",
      "name": "DBU (1,8-diazabicyclo[5.4.0]undec-7-ene)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Non-nucleophilic base used to activate the glycosyl donor in N-glycosylation reactions."
    },
    {
      "id": "C04",
      "name": "TMSOTf (trimethylsilyl trifluoromethanesulfonate)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Lewis acid activator used to promote N-glycosylation by activating the anomeric position of the glycosyl donor."
    },
    {
      "id": "C05",
      "name": "S2 ((−)-((2R,3R,4S,5R)-3-(Benzoyloxy)-5-(2,6-dichloro-9H-purin-9-yl)-4-methyltetrahydrofuran-2,4-diyl)bis(methylene)dibenzoate)",
      "iupac_name": "(−)-((2R,3R,4S,5R)-3-(Benzoyloxy)-5-(2,6-dichloro-9H-purin-9-yl)-4-methyltetrahydrofuran-2,4-diyl)bis(methylene)dibenzoate",
      "molecular_formula": "C33H26Cl2N4O7",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 683.1066",
      "ms_calculated_exact_mass": null,
      "description": "Perbenzoylated N-glycoside formed by Lewis acid-promoted coupling of benzoylated sugar S1 with 2,6-dichloropurine; β-anomer predominates (10:1 dr); key intermediate for both the furanose and 4′-thio series."
    },
    {
      "id": "C06",
      "name": "NH3 (ammonia gas)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Reagent used to effect simultaneous debenzoylation and aminolysis/methanolysis of the 2,6-dichloropurine C6 position to give either methoxy (S3) or amino (S4) products."
    },
    {
      "id": "C07",
      "name": "S3 ((+)-((2R,3S,4R,5R)-5-(2-Chloro-6-methoxy-9H-purin-9-yl)-3-hydroxy-4-methyltetrahydrofuran-2,4-diyl)dimethanol)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(2-Chloro-6-methoxy-9H-purin-9-yl)-3-hydroxy-4-methyltetrahydrofuran-2,4-diyl)dimethanol",
      "molecular_formula": "C13H17ClN4O5",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 367.0781",
      "ms_calculated_exact_mass": null,
      "description": "6-Methoxypurine nucleoside triol formed as minor co-product (43%) of ammonolysis of S2; used for stereochemical confirmation by X-ray crystallography."
    },
    {
      "id": "C08",
      "name": "S4 ((−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-methyltetrahydrofuran-2,4-diyl)dimethanol)",
      "iupac_name": "(−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-methyltetrahydrofuran-2,4-diyl)dimethanol",
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Previously reported (ref 32, Manchoju et al.); also obtainable as co-product from S2 ammonolysis",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "2-Chloroadenosine-like triol nucleoside that serves as the common advanced intermediate for compounds 11–14, 16, and 17; previously reported and used as received from prior work."
    },
    {
      "id": "C09",
      "name": "CSA (camphorsulfonic acid)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acid catalyst used in acetonide formation reactions with 2,2-dimethoxypropane."
    },
    {
      "id": "C10",
      "name": "2,2-dimethoxypropane",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Reagent for installation of the acetonide protecting group on 1,2- or 1,3-diol systems."
    },
    {
      "id": "C11",
      "name": "S5 ((+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methanol)",
      "iupac_name": "(+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methanol",
      "molecular_formula": "C15H20ClN5O4",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 392.1104",
      "ms_calculated_exact_mass": null,
      "description": "Acetonide-protected nucleoside primary alcohol; key branch-point intermediate used in synthesis of compounds 11, 12, 13, and 14."
    },
    {
      "id": "C12",
      "name": "t-BuMgCl (tert-butylmagnesium chloride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Grignard base used to deprotonate primary alcohols prior to phosphorylation with chlorophosphate reagents."
    },
    {
      "id": "C13",
      "name": "diethylchlorophosphate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Electrophilic phosphorylating agent used to install diethyl phosphate ester at primary alcohol positions."
    },
    {
      "id": "C14",
      "name": "S6 ((+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Diethyl Phosphate)",
      "iupac_name": "(+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C19H29ClN5O7P",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 528.1386",
      "ms_calculated_exact_mass": null,
      "description": "Acetonide-protected diethyl phosphate ester; direct precursor to final compound 11 (LCB-2122) after acetonide deprotection."
    },
    {
      "id": "C15",
      "name": "TFA/H2O (8:2) mixture",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acidic deprotection mixture used to cleave acetonide protecting groups from diol-acetonide intermediates."
    },
    {
      "id": "C16",
      "name": "11 (LCB-2122) ((+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C16H25ClN5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 488.1072",
      "ms_calculated_exact_mass": null,
      "description": "Lead cardioprotective compound LCB-2122; adenosine-like nucleoside analogue bearing C2′ all-carbon quaternary center with diethyl phosphate ester at C5′ and 2-chloroadenine base."
    },
    {
      "id": "C17",
      "name": "Et3N (triethylamine)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base used in phosphorylation of S5 with POCl3 to give the hydrogen phosphate S7."
    },
    {
      "id": "C18",
      "name": "POCl3 (phosphorus oxychloride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Phosphorylating agent used to install the monophosphate group at the primary alcohol of acetonide S5."
    },
    {
      "id": "C19",
      "name": "S7 (Triethylammonium (+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Hydrogen Phosphate)",
      "iupac_name": "Triethylammonium (+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Hydrogen Phosphate",
      "molecular_formula": "C21H36ClN6O7P",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 551.2138",
      "ms_calculated_exact_mass": null,
      "description": "Acetonide-protected hydrogen phosphate monoester (triethylammonium salt) and direct precursor to final compound 12 after acetonide deprotection."
    },
    {
      "id": "C20",
      "name": "12 ((+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Dihydrogen Phosphate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Dihydrogen Phosphate",
      "molecular_formula": "C12H17ClN5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M-H]- 408.0482",
      "ms_calculated_exact_mass": null,
      "description": "Free monophosphate analogue of LCB-2122; inactive in cardioprotection assay due to poor cellular uptake of the charged molecule."
    },
    {
      "id": "C21",
      "name": "dimethylchlorophosphate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Electrophilic phosphorylating agent used to install dimethyl phosphate ester at the primary alcohol of acetonide S5."
    },
    {
      "id": "C22",
      "name": "S8 ((+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Dimethyl Phosphate)",
      "iupac_name": "(+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Dimethyl Phosphate",
      "molecular_formula": "C17H25ClN5O7P",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 500.1061",
      "ms_calculated_exact_mass": null,
      "description": "Acetonide-protected dimethyl phosphate ester; direct precursor to final compound 13 after acetonide deprotection."
    },
    {
      "id": "C23",
      "name": "13 ((+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Dimethyl Phosphate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Dimethyl Phosphate",
      "molecular_formula": "C14H21ClN5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 460.0765",
      "ms_calculated_exact_mass": null,
      "description": "Dimethyl phosphate analogue of LCB-2122 (LCB-2234); inactive in cardioprotection assay."
    },
    {
      "id": "C24",
      "name": "diisopropyl chlorophosphate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Electrophilic phosphorylating agent used to install diisopropyl phosphate ester at the primary alcohol of acetonide S5."
    },
    {
      "id": "C25",
      "name": "S9 ((+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Diisopropyl Phosphate)",
      "iupac_name": "(+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Diisopropyl Phosphate",
      "molecular_formula": "C21H33ClN5O7P",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 534.1868",
      "ms_calculated_exact_mass": null,
      "description": "Acetonide-protected diisopropyl phosphate ester; direct precursor to final compound 14 after acetonide deprotection."
    },
    {
      "id": "C26",
      "name": "14 ((+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diisopropyl Phosphate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diisopropyl Phosphate",
      "molecular_formula": "C18H29ClN5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 516.1398",
      "ms_calculated_exact_mass": null,
      "description": "Diisopropyl phosphate analogue of LCB-2122 (LCB-2177); retains cardioprotective activity, suggesting LCB-2122 is not a prodrug of the free phosphate."
    },
    {
      "id": "C27",
      "name": "S10 (4′-thio primary alcohol precursor)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Previously reported (ref 45, Eymard et al., Molecules 2024)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Benzoylated 4′-thionucleoside primary alcohol used as starting material for synthesis of the 4′-thio diethyl phosphate compound 15."
    },
    {
      "id": "C28",
      "name": "S11 ((−)-((2R,3R,4S,5R)-4-(Benzoyloxy)-2-(2,6-dichloro-9H-purin-9-yl)-5-(((diethoxyphosphoryl)oxy)methyl)-3-methyltetrahydrothiophen-3-yl)methyl Benzoate)",
      "iupac_name": "(−)-((2R,3R,4S,5R)-4-(Benzoyloxy)-2-(2,6-dichloro-9H-purin-9-yl)-5-(((diethoxyphosphoryl)oxy)methyl)-3-methyltetrahydrothiophen-3-yl)methyl Benzoate",
      "molecular_formula": "C30H31Cl2N4O8PS",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 709.1048",
      "ms_calculated_exact_mass": null,
      "description": "Benzoyl-protected 4′-thionucleoside diethyl phosphate with 2,6-dichloropurine base; direct precursor to compound 15 after ammonolysis."
    },
    {
      "id": "C29",
      "name": "15 ((+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrothiophen-2-yl)methyl Diethyl Phosphate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrothiophen-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C16H25ClN5O6PS",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 504.0841",
      "ms_calculated_exact_mass": null,
      "description": "4′-Thio analogue of LCB-2122 (LCB-2346); lowered cardioprotective activity relative to the oxygen-containing ring system."
    },
    {
      "id": "C30",
      "name": "Pd/C (palladium on carbon, 10 wt%)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "catalyst",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Heterogeneous hydrogenation catalyst used for reductive hydrogenolysis of the C2-chloro substituent in compound 11 to give compound 16."
    },
    {
      "id": "C31",
      "name": "16 ((−)-((2R,3S,4R,5R)-5-(6-Amino-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate)",
      "iupac_name": "(−)-((2R,3S,4R,5R)-5-(6-Amino-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C16H26N5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+H]+ 432.1642",
      "ms_calculated_exact_mass": null,
      "description": "Dechlorinated analogue of LCB-2122 (LCB-2195) lacking the C2-chlorine; inactive in cardioprotection, implicating the 2Cl-purine as key pharmacophore."
    },
    {
      "id": "C32",
      "name": "S12 ((+)-2-Chloro-9-((2R,3R,4S,5R)-4-hydroxy-3,5-bis(hydroxymethyl)-3-methyltetrahydrofuran-2-yl)-1,9-dihydro-6H-purin-6-one)",
      "iupac_name": "(+)-2-Chloro-9-((2R,3R,4S,5R)-4-hydroxy-3,5-bis(hydroxymethyl)-3-methyltetrahydrofuran-2-yl)-1,9-dihydro-6H-purin-6-one",
      "molecular_formula": "C12H15ClN4O5",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 353.0618",
      "ms_calculated_exact_mass": null,
      "description": "2-Chlorohypoxanthine triol nucleoside obtained by saponification of perbenzoylated nucleoside S2 with NaOH; used in synthesis of inosine analogue compound 17."
    },
    {
      "id": "C33",
      "name": "S13 ((+)-2-Chloro-9-((4aR,5R,7R,7aS)-7-(hydroxymethyl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-5-yl)-1,9-dihydro-6H-purin-6-one)",
      "iupac_name": "(+)-2-Chloro-9-((4aR,5R,7R,7aS)-7-(hydroxymethyl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-5-yl)-1,9-dihydro-6H-purin-6-one",
      "molecular_formula": "C15H19ClN4O5",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 393.0944",
      "ms_calculated_exact_mass": null,
      "description": "Acetonide-protected 2-chlorohypoxanthine nucleoside primary alcohol; direct precursor to compound 17 after phosphorylation and simultaneous acetonide deprotection."
    },
    {
      "id": "C34",
      "name": "17 ((+)-((2R,3S,4R,5R)-5-(2-Chloro-9H-purin-9-yl-6-one)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(2-Chloro-9H-purin-9-yl-6-one)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C16H24ClN4O8P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M-H]- 465.0949",
      "ms_calculated_exact_mass": null,
      "description": "Inosine-type (hypoxanthine) analogue of LCB-2122 (LCB-2271); inactive in cardioprotection, confirming the importance of the adenine NH2 and suggesting the 2-chloroadenine cannot be a deaminated metabolite."
    },
    {
      "id": "C35",
      "name": "S14 (secondary alcohol precursor for S15 lactone)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Previously reported (ref 31, Becerril-Jiménez et al., J. Org. Chem. 2019)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Secondary alcohol lactone precursor used to access the bis-TBS-protected lactone S15 needed for C2′-methoxymethyl analogue 18."
    },
    {
      "id": "C36",
      "name": "imidazole",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base used in TBS protection of secondary alcohol S14 with TBSOTf."
    },
    {
      "id": "C37",
      "name": "TBSOTf (tert-butyldimethylsilyl trifluoromethanesulfonate)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Silylating agent used to install TBS protecting groups on hydroxyl groups."
    },
    {
      "id": "C38",
      "name": "S15 ((+)-(3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-methyl-3-vinyldihydrofuran-2(3H)-one)",
      "iupac_name": "(+)-(3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-methyl-3-vinyldihydrofuran-2(3H)-one",
      "molecular_formula": "C20H40O4Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 423.2356",
      "ms_calculated_exact_mass": null,
      "description": "Bis-TBS-protected vinyl lactone; used in DIBAL-H reduction to give lactols S16a,b in the synthesis of compound 18."
    },
    {
      "id": "C39",
      "name": "DIBAL-H (diisobutylaluminium hydride, 1M in hexanes)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Reducing agent used for partial reduction of lactone S15 to the lactol S16a,b at −78 °C."
    },
    {
      "id": "C40",
      "name": "S16a,b ((3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-methyl-3-vinyltetrahydrofuran-2-ol, mixture of anomers)",
      "iupac_name": null,
      "molecular_formula": "C20H42O4Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 425.2514",
      "ms_calculated_exact_mass": null,
      "description": "Lactol anomeric mixture (2:1 ratio) obtained by DIBAL-H partial reduction of lactone S15; used in benzoylation to give S17a,b."
    },
    {
      "id": "C41",
      "name": "BzCl (benzoyl chloride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acylating agent used to protect the anomeric hydroxyl of lactols S16a,b as anomeric benzoates."
    },
    {
      "id": "C42",
      "name": "DMAP (4-dimethylaminopyridine)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Nucleophilic acylation catalyst used in benzoylation of lactols S16a,b."
    },
    {
      "id": "C43",
      "name": "pyridine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base and co-solvent used in acylation and silylation reactions."
    },
    {
      "id": "C44",
      "name": "S17a,b ((3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-methyl-3-vinyltetrahydrofuran-2-yl Benzoate, mixture of anomers)",
      "iupac_name": null,
      "molecular_formula": "C27H46O5Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 529.2777",
      "ms_calculated_exact_mass": null,
      "description": "Anomeric benzoate mixture (2:1 dr) of the vinyl-substituted tetrahydrofuranose; used in ozonolysis/reduction sequence to give primary alcohols S18a,b."
    },
    {
      "id": "C45",
      "name": "O3 / NEt3 / NaBH4 (ozonolysis then reductive workup)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Sequential ozonolysis (O3, then NEt3 quench) followed by NaBH4 reduction to convert vinyl group of S17a,b to primary alcohol S18a,b."
    },
    {
      "id": "C46",
      "name": "S18a,b ((3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-(hydroxymethyl)-3-methyltetrahydrofuran-2-yl Benzoate, mixture of anomers)",
      "iupac_name": null,
      "molecular_formula": "C26H46O6Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 533.2729",
      "ms_calculated_exact_mass": null,
      "description": "Primary alcohol mixture (5:1 dr) obtained by ozonolysis/reduction of vinyl alkenes S17a,b; the hydroxymethyl group is subsequently methylated to give S19a,b."
    },
    {
      "id": "C47",
      "name": "2,6-di-tert-butyl-4-methylpyridine (DTBMP)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Hindered base used in O-methylation of primary alcohol S18a,b with MeOTf to avoid O-silylation side reactions."
    },
    {
      "id": "C48",
      "name": "MeOTf (methyl trifluoromethanesulfonate)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Methylating agent used to convert the primary hydroxyl of S18a,b to the methoxymethyl group in S19a,b."
    },
    {
      "id": "C49",
      "name": "S19a,b ((3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-(methoxymethyl)-3-methyltetrahydrofuran-2-yl Benzoate, mixture of anomers)",
      "iupac_name": null,
      "molecular_formula": "C27H48O6Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 547.2889",
      "ms_calculated_exact_mass": null,
      "description": "Methoxymethyl-bearing anomeric benzoate mixture (4:1 dr) used as glycosyl donor in N-glycosylation with 2-chloroadenine to give nucleosides S20a,b."
    },
    {
      "id": "C50",
      "name": "2-chloroadenine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Purine base used in Vorbrüggen-type N-glycosylation to install the 2-chloroadenine nucleobase onto the sugar S19a,b."
    },
    {
      "id": "C51",
      "name": "BSA (N,O-bis(trimethylsilyl)acetamide)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Silylating agent used to activate 2-chloroadenine as the per-TMS derivative for Vorbrüggen N-glycosylation."
    },
    {
      "id": "C52",
      "name": "S20a,b (9-((3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-(methoxymethyl)-3-methyltetrahydrofuran-2-yl)-2-chloro-9H-purin-6-amine, α/β mixture)",
      "iupac_name": null,
      "molecular_formula": "C25H46ClN5O4Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 572.2852",
      "ms_calculated_exact_mass": null,
      "description": "Bis-TBS-protected 2-chloroadenosine analogue bearing methoxymethyl at C2′; α/β mixture (1.2:1 ratio in favor of β) used in selective deprotection to give S21a and S21b."
    },
    {
      "id": "C53",
      "name": "TFA/H2O (1:1) mixture",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acidic aqueous mixture used for selective removal of one TBS group from the anomeric position of nucleosides S20a,b to give alcohols S21a and S21b."
    },
    {
      "id": "C54",
      "name": "S21a ((+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-((tert-butyldimethylsilyl)oxy)-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methanol)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-((tert-butyldimethylsilyl)oxy)-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methanol",
      "molecular_formula": "C19H32ClN5O4Si",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 458.1982",
      "ms_calculated_exact_mass": null,
      "description": "Minor diastereomer (α-anomer-enriched, 27%) primary alcohol obtained from S20a,b by selective TBS removal; not used further (S21b used for compound 18)."
    },
    {
      "id": "C55",
      "name": "S21b ((−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-((tert-butyldimethylsilyl)oxy)-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methanol)",
      "iupac_name": "(−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-((tert-butyldimethylsilyl)oxy)-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methanol",
      "molecular_formula": "C19H32ClN5O4Si",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 458.1984",
      "ms_calculated_exact_mass": null,
      "description": "Major diastereomer (β-anomer, 38%) primary alcohol obtained from S20a,b by selective TBS removal; used in phosphorylation to give S22."
    },
    {
      "id": "C56",
      "name": "S22 ((+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-((tert-butyldimethylsilyl)oxy)-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-((tert-butyldimethylsilyl)oxy)-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C23H41ClN5O7PSi",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 594.2271",
      "ms_calculated_exact_mass": null,
      "description": "TBS-protected diethyl phosphate intermediate; TBS removed with TBAF to give final compound 18."
    },
    {
      "id": "C57",
      "name": "TBAF (tetrabutylammonium fluoride, 1M in THF)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fluoride source used for desilylation of TBS ether in S22 to give final compound 18."
    },
    {
      "id": "C58",
      "name": "18 ((−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate)",
      "iupac_name": "(−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C17H27ClN5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+H]+ 480.1399",
      "ms_calculated_exact_mass": null,
      "description": "C2′-Methoxymethyl analogue of LCB-2122 (LCB-2336); active in cardioprotection assay, demonstrating tolerance of C2′-OH methylation."
    },
    {
      "id": "C59",
      "name": "S23a,b (aldehyde precursors from photoredox chemistry)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Previously reported (ref 31, Becerril-Jiménez et al., J. Org. Chem. 2019)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Aldehyde intermediates from prior photoredox work; used in NaBH4 reduction and subsequent benzylation/N-glycosylation sequence to give S24 in synthesis of compound 19."
    },
    {
      "id": "C60",
      "name": "NaBH4 (sodium borohydride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Reducing agent used to reduce aldehydes S23a,b to the corresponding alcohols and in the ozonolysis workup (reduction of intermediate aldehyde from S17a,b)."
    },
    {
      "id": "C61",
      "name": "benzyl 2,2,2-trichloroacetimidate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "O-Benzylation reagent used with catalytic TfOH to install a benzyl ether on the C3′-hydroxyl of the alcohol derived from S23a,b."
    },
    {
      "id": "C62",
      "name": "TfOH (triflic acid)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acid catalyst used in catalytic amount for O-benzylation with benzyl 2,2,2-trichloroacetimidate."
    },
    {
      "id": "C63",
      "name": "S24 ((+)-((2R,3S,4R,5R)-3-(Benzyloxy)-5-(2,6-dichloro-9H-purin-9-yl)-4-methyltetrahydrofuran-2,4-diyl)bis(methylene) Dibenzoate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-3-(Benzyloxy)-5-(2,6-dichloro-9H-purin-9-yl)-4-methyltetrahydrofuran-2,4-diyl)bis(methylene) Dibenzoate",
      "molecular_formula": "C33H28Cl2N4O6",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 669.1272",
      "ms_calculated_exact_mass": null,
      "description": "3′-O-Benzyl perbenzoylated nucleoside with 2,6-dichloropurine base (β-anomer, 56% over 3 steps); used in ammonolysis to give diol S25."
    },
    {
      "id": "C64",
      "name": "S25 ((−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-methyltetrahydrofuran-2,4-diyl)dimethanol)",
      "iupac_name": "(−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-methyltetrahydrofuran-2,4-diyl)dimethanol",
      "molecular_formula": "C19H22ClN5O4",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 420.1429",
      "ms_calculated_exact_mass": null,
      "description": "3′-O-Benzyl diol nucleoside with 2-chloroadenine base; obtained by ammonolysis of S24, used in bis-TBS protection to give S26."
    },
    {
      "id": "C65",
      "name": "2,6-lutidine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Hindered base used in TBS protection of diol S25 to avoid N-silylation side reactions."
    },
    {
      "id": "C66",
      "name": "S26 ((+)-9-((2R,3R,4S,5R)-4-(Benzyloxy)-3,5-bis(((tert-butyldimethylsilyl)oxy)methyl)-3-methyltetrahydrofuran-2-yl)-2-chloro-9H-purin-6-amine)",
      "iupac_name": "(+)-9-((2R,3R,4S,5R)-4-(Benzyloxy)-3,5-bis(((tert-butyldimethylsilyl)oxy)methyl)-3-methyltetrahydrofuran-2-yl)-2-chloro-9H-purin-6-amine",
      "molecular_formula": "C31H50ClN5O4Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 648.3175",
      "ms_calculated_exact_mass": null,
      "description": "Bis-TBS-protected 3′-O-benzyl nucleoside; used in selective TBS removal to give primary alcohol S27."
    },
    {
      "id": "C67",
      "name": "S27 ((−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-(((tert-butyldimethylsilyl)oxy)methyl)-4-methyltetrahydrofuran-2-yl)methanol)",
      "iupac_name": "(−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-(((tert-butyldimethylsilyl)oxy)methyl)-4-methyltetrahydrofuran-2-yl)methanol)",
      "molecular_formula": "C25H36ClN5O4Si",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 534.2290",
      "ms_calculated_exact_mass": null,
      "description": "Mono-TBS-protected primary alcohol with free C5′-OH; obtained by selective TBS removal from S26 with TFA/H2O (1:1), used in phosphorylation to give S28."
    },
    {
      "id": "C68",
      "name": "S28 ((+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-(((tert-butyldimethylsilyl)oxy)methyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-(((tert-butyldimethylsilyl)oxy)methyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C29H45ClN5O7PSi",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 692.2419",
      "ms_calculated_exact_mass": null,
      "description": "TBS-protected diethyl phosphate with 3′-O-benzyl group; TBS removal with TFA/H2O (8:2) gives final compound 19."
    },
    {
      "id": "C69",
      "name": "19 ((+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C23H31ClN5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+H]+ 556.1748",
      "ms_calculated_exact_mass": null,
      "description": "3′-O-Benzyl analogue of LCB-2122 (LCB-2165); active in cardioprotection assay, demonstrating tolerance of C3′ benzylation."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of compound 11 (LCB-2122)",
      "source_section": "main_text",
      "target_compound_id": "C16",
      "target_compound_name": "11 (LCB-2122)",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "N-glycosylation (Lewis acid-promoted)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "S1 (benzoylated sugar lactone)",
              "amount": "4.77 g (8.02 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "2,6-dichloropurine",
              "amount": "1.67 g (8.82 mmol, 1.10 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C03",
              "name": "DBU",
              "amount": "3.67 mL (24.1 mmol, 3.00 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C04",
              "name": "TMSOTf",
              "amount": "5.9 mL (32 mmol, 4.0 equiv)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "dry acetonitrile",
              "volume": "32 mL"
            }
          ],
          "conditions": {
            "temperature": "−10 °C",
            "time": "6 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with saturated NaHCO3; organic layer washed with 0.1 M citric acid and NaHCO3, dried over MgSO4."
          },
          "product": {
            "compound_id": "C05",
            "name": "S2",
            "yield": "3.96 g (74%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, Hexanes/EtOAc 80:20",
          "notes": "Anomeric ratio ~8:1 by 1H NMR of crude; after purification 10:1 dr in favor of β-anomer."
        },
        {
          "step_number": 2,
          "reaction_type": "Ammonolysis / debenzoylation / C6-amination",
          "reactants": [
            {
              "compound_id": "C05",
              "name": "S2",
              "amount": "3.29 g (4.97 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C06",
              "name": "NH3(g)",
              "amount": "saturation",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "50 mL"
            }
          ],
          "conditions": {
            "temperature": "80 °C",
            "time": "24 h",
            "atmosphere": null,
            "ph": null,
            "other": "Performed in high-pressure flask; with additional NH3 saturation and 48 h heating, S4 can be obtained in 71% yield."
          },
          "product": {
            "compound_id": "C08",
            "name": "S4 (desired amino product, 44%) and C07/S3 (methoxy co-product, 43%)",
            "yield": "714 mg (44%) of S4; 702 mg (43%) of S3",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, DCM/MeOH 90:10",
          "notes": "S4 corresponds to previously reported compound (ref 32). Both S3 and S4 isolated."
        },
        {
          "step_number": 3,
          "reaction_type": "Acetonide protection",
          "reactants": [
            {
              "compound_id": "C08",
              "name": "S4",
              "amount": "1.05 g (3.18 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C09",
              "name": "CSA",
              "amount": "737 mg (3.18 mmol, 1.00 equiv)",
              "role": "acid"
            },
            {
              "compound_id": "C10",
              "name": "2,2-dimethoxypropane",
              "amount": "7.0 mL (57 mmol, 18 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "molecular sieves 3 Å",
              "amount": "3.0 g",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "dry acetone",
              "volume": "32 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "16 h",
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C11",
            "name": "S5",
            "yield": "739 mg (63%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, DCM/MeOH 90:10",
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "O-Phosphorylation (diethyl phosphate installation)",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "S5",
              "amount": "1.13 g (3.06 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl (1.0 M in THF)",
              "amount": "4.6 mL (4.6 mmol, 1.5 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C13",
              "name": "diethylchlorophosphate",
              "amount": "0.66 mL (4.6 mmol, 1.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "31 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "4 h (after 45 min Grignard formation)",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with MeOH."
          },
          "product": {
            "compound_id": "C14",
            "name": "S6",
            "yield": "1.33 g (86%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN 50:50",
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "Acetonide deprotection",
          "reactants": [
            {
              "compound_id": "C14",
              "name": "S6",
              "amount": "360 mg (0.711 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C15",
              "name": "TFA/H2O (8:2)",
              "amount": "7.1 mL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "7.1 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "2 h",
            "atmosphere": null,
            "ph": null,
            "other": "MeOH added then concentrated; coevaporated with MeOH (3×)."
          },
          "product": {
            "compound_id": "C16",
            "name": "11 (LCB-2122)",
            "yield": "294 mg (88%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN 70:30",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of compound 12 (free monophosphate)",
      "source_section": "main_text",
      "target_compound_id": "C20",
      "target_compound_name": "12",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "O-Phosphorylation (monophosphate installation)",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "S5",
              "amount": "36.7 mg (99.2 μmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C17",
              "name": "Et3N",
              "amount": "124 μL (893 μmol, 9.00 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C18",
              "name": "POCl3",
              "amount": "13.9 μL (149 μmol, 1.50 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "1 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C",
            "time": "2 h, then 1 h after ice addition",
            "atmosphere": null,
            "ph": null,
            "other": "Ice chips added after 2 h; reaction mixture concentrated under reduced pressure."
          },
          "product": {
            "compound_id": "C19",
            "name": "S7 (triethylammonium salt)",
            "yield": "49 mg (90%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN 70:30",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Acetonide deprotection",
          "reactants": [
            {
              "compound_id": "C19",
              "name": "S7",
              "amount": "156 mg (0.347 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C15",
              "name": "TFA/H2O (8:2)",
              "amount": "3.5 mL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "3.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "4 h",
            "atmosphere": null,
            "ph": null,
            "other": "MeOH added then concentrated; coevaporated with MeOH (3×)."
          },
          "product": {
            "compound_id": "C20",
            "name": "12",
            "yield": "31 mg (22%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN 75:25",
          "notes": "NEt3 was added to resolve NMR signals of compound 12."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Synthesis of compound 13 (dimethyl phosphate)",
      "source_section": "main_text",
      "target_compound_id": "C23",
      "target_compound_name": "13",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "O-Phosphorylation (dimethyl phosphate installation)",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "S5",
              "amount": "54.4 mg (147 μmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl (1.0 M in THF)",
              "amount": "0.16 mL (0.16 mmol, 1.1 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C21",
              "name": "dimethylchlorophosphate",
              "amount": "18 μL (0.16 mmol, 1.1 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "1.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "4.5 h (after 45 min Grignard formation)",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with MeOH; 34% of S5 recovered."
          },
          "product": {
            "compound_id": "C22",
            "name": "S8",
            "yield": "35 mg (50%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, DCM/MeOH 95:5",
          "notes": "18.3 mg (34%) of starting material S5 recovered."
        },
        {
          "step_number": 2,
          "reaction_type": "Acetonide deprotection",
          "reactants": [
            {
              "compound_id": "C22",
              "name": "S8",
              "amount": "24.7 mg (51.7 μmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C15",
              "name": "TFA/H2O (8:2)",
              "amount": "0.6 mL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "0.6 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "3 h",
            "atmosphere": null,
            "ph": null,
            "other": "MeOH added then concentrated; coevaporated with MeOH (3×)."
          },
          "product": {
            "compound_id": "C23",
            "name": "13",
            "yield": "8.2 mg (36%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN 50:50",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Synthesis of compound 14 (diisopropyl phosphate)",
      "source_section": "main_text",
      "target_compound_id": "C26",
      "target_compound_name": "14",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "O-Phosphorylation (diisopropyl phosphate installation)",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "S5",
              "amount": "75 mg (0.20 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl (1.7 M in THF)",
              "amount": "0.13 mL (0.23 mmol, 1.1 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C24",
              "name": "diisopropyl chlorophosphate",
              "amount": "40 μL (0.23 mmol, 1.1 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "2 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "16 h (after 45 min Grignard formation)",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with MeOH."
          },
          "product": {
            "compound_id": "C25",
            "name": "S9",
            "yield": "79 mg (73%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, DCM/MeOH 90:10",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Acetonide deprotection",
          "reactants": [
            {
              "compound_id": "C25",
              "name": "S9",
              "amount": "34.8 mg (0.065 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C15",
              "name": "TFA/H2O (8:2)",
              "amount": "0.7 mL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "0.7 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "4 h",
            "atmosphere": null,
            "ph": null,
            "other": "MeOH added then concentrated; coevaporated with MeOH (3×)."
          },
          "product": {
            "compound_id": "C26",
            "name": "14",
            "yield": "24 mg (74%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN 60:40",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Synthesis of compound 15 (4′-thio analogue)",
      "source_section": "main_text",
      "target_compound_id": "C29",
      "target_compound_name": "15",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "O-Phosphorylation (diethyl phosphate installation on thiosugar)",
          "reactants": [
            {
              "compound_id": "C27",
              "name": "S10 (4′-thio primary alcohol)",
              "amount": "95 mg (0.17 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl (1.7 M in THF)",
              "amount": "0.15 mL (0.25 mmol, 1.5 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C13",
              "name": "diethylchlorophosphate",
              "amount": "36 μL (0.25 mmol, 1.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "1.7 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "16 h (after 45 min Grignard formation)",
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C28",
            "name": "S11",
            "yield": "56 mg (48%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, Hexanes/EtOAc 60:40",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Ammonolysis / debenzoylation / C6-amination",
          "reactants": [
            {
              "compound_id": "C28",
              "name": "S11",
              "amount": "33 mg (0.047 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C06",
              "name": "NH3(g)",
              "amount": "saturation (twice)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "1.2 mL"
            }
          ],
          "conditions": {
            "temperature": "80 °C",
            "time": "16 h, then additional NH3 saturation and 24 h at 80 °C",
            "atmosphere": null,
            "ph": null,
            "other": "Performed in high-pressure flask."
          },
          "product": {
            "compound_id": "C29",
            "name": "15",
            "yield": "13 mg (58%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, EtOAc/MeOH 70:30",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Synthesis of compound 16 (dechlorinated analogue)",
      "source_section": "main_text",
      "target_compound_id": "C31",
      "target_compound_name": "16",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Hydrogenolysis (reductive dechlorination)",
          "reactants": [
            {
              "compound_id": "C16",
              "name": "11 (LCB-2122)",
              "amount": "23 mg (0.049 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C30",
              "name": "Pd/C (10 wt%)",
              "amount": "23 mg (1.0 equiv)",
              "role": "catalyst"
            },
            {
              "compound_id": null,
              "name": "H2 gas (positive pressure)",
              "amount": null,
              "role": "reductant"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "6 h",
            "atmosphere": "H2 (positive pressure; N2 removed and replaced with H2)",
            "ph": null,
            "other": "Filtered over Celite with MeOH/EtOAc (50:50)."
          },
          "product": {
            "compound_id": "C31",
            "name": "16",
            "yield": "15.2 mg (72%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN 60:40",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Synthesis of compound 17 (inosine/hypoxanthine analogue)",
      "source_section": "main_text",
      "target_compound_id": "C34",
      "target_compound_name": "17",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Saponification / debenzoylation",
          "reactants": [
            {
              "compound_id": "C05",
              "name": "S2",
              "amount": "500 mg (0.756 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "2 N NaOH",
              "amount": "3.8 mL",
              "role": "base"
            },
            {
              "compound_id": null,
              "name": "trifluoroacetic acid (excess, for acidification)",
              "amount": "excess",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "EtOH",
              "volume": "7.6 mL"
            }
          ],
          "conditions": {
            "temperature": "50 °C (dissolution), then room temperature for reaction",
            "time": "5 h",
            "atmosphere": null,
            "ph": null,
            "other": "Extracted with CH2Cl2 (3×) after acidification."
          },
          "product": {
            "compound_id": "C32",
            "name": "S12",
            "yield": "176 mg (70%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeOH 80:20",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Acetonide protection",
          "reactants": [
            {
              "compound_id": "C32",
              "name": "S12",
              "amount": "100 mg (0.302 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C09",
              "name": "CSA",
              "amount": "70 mg (0.302 mmol, 1.0 equiv)",
              "role": "acid"
            },
            {
              "compound_id": "C10",
              "name": "2,2-dimethoxypropane",
              "amount": "0.67 mL (5.4 mmol, 18 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "molecular sieves 3 Å",
              "amount": "180 mg",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "dry acetone",
              "volume": "3 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "16 h",
            "atmosphere": null,
            "ph": null,
            "other": "Dissolved in EtOAc; washed with 0.1 M HCl, aqueous layer extracted with EtOAc (3×)."
          },
          "product": {
            "compound_id": "C33",
            "name": "S13",
            "yield": "80 mg (71%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, CH2Cl2/MeOH 85:15",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "O-Phosphorylation and simultaneous acetonide deprotection (one-pot)",
          "reactants": [
            {
              "compound_id": "C33",
              "name": "S13",
              "amount": "22 mg (0.059 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl",
              "amount": "148 μL (0.148 mmol, 2.5 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C13",
              "name": "diethylchlorophosphate",
              "amount": "22 μL (0.148 mmol, 2.5 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C15",
              "name": "TFA/H2O (8:2)",
              "amount": "3.0 mL (open atmosphere)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "0.6 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "4 h phosphorylation, then 2 h deprotection",
            "atmosphere": "open atmosphere (for TFA/H2O addition step)",
            "ph": null,
            "other": "TFA/H2O added dropwise after phosphorylation; MeOH added then concentrated; coevaporated with MeOH (3×)."
          },
          "product": {
            "compound_id": "C34",
            "name": "17",
            "yield": "10 mg (36%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN 70:30",
          "notes": "Phosphorylation and acetonide removal performed in one pot without isolation of the phosphorylated acetonide."
        }
      ]
    },
    {
      "pathway_id": "P8",
      "pathway_name": "Synthesis of compound 18 (C2′-methoxymethyl analogue)",
      "source_section": "main_text",
      "target_compound_id": "C58",
      "target_compound_name": "18",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "TBS protection of secondary alcohol",
          "reactants": [
            {
              "compound_id": "C35",
              "name": "S14 (secondary alcohol)",
              "amount": "140 mg (0.489 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C36",
              "name": "imidazole",
              "amount": "83 mg (1.2 mmol, 2.5 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C37",
              "name": "TBSOTf",
              "amount": "0.17 mL (0.73 mmol, 1.5 equiv)",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "1.9 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C then room temperature",
            "time": "21 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with saturated NaHCO3; extracted with Et2O (3×); washed with brine."
          },
          "product": {
            "compound_id": "C38",
            "name": "S15",
            "yield": "188 mg (96%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, Hexanes/EtOAc 70:30",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "DIBAL-H partial reduction (lactone to lactol)",
          "reactants": [
            {
              "compound_id": "C38",
              "name": "S15",
              "amount": "329 mg (0.821 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C39",
              "name": "DIBAL-H (1M in hexanes)",
              "amount": "1.2 mL (1.2 mmol, 1.5 equiv)",
              "role": "reductant"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "4.5 mL"
            }
          ],
          "conditions": {
            "temperature": "−78 °C",
            "time": "3.5 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with saturated potassium sodium tartrate at −78 °C; warmed to room temperature with stirring 1 h; extracted with Et2O (3×)."
          },
          "product": {
            "compound_id": "C40",
            "name": "S16a,b (2:1 mixture of anomers)",
            "yield": "232 mg (70%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, Hexanes/EtOAc 80:20",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Benzoylation of anomeric hydroxyl",
          "reactants": [
            {
              "compound_id": "C40",
              "name": "S16a,b",
              "amount": "232 mg (0.576 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C42",
              "name": "DMAP",
              "amount": "7 mg (0.06 mmol, 0.1 equiv)",
              "role": "catalyst"
            },
            {
              "compound_id": "C43",
              "name": "pyridine",
              "amount": "0.28 mL (3.5 mmol, 6.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C41",
              "name": "BzCl",
              "amount": "0.10 mL (0.86 mmol, 1.5 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "ethylenediamine (quench)",
              "amount": "0.09 mL (1.4 mmol, 2.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "3.1 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C then room temperature",
            "time": "16 h, then 30 min with ethylenediamine at 0 °C",
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C44",
            "name": "S17a,b (2:1 diastereomeric mixture)",
            "yield": "266 mg (91%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, Hexanes/EtOAc 70:30",
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "Ozonolysis / reductive workup (vinyl to primary alcohol)",
          "reactants": [
            {
              "compound_id": "C44",
              "name": "S17a,b",
              "amount": "4.07 g (8.02 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C45",
              "name": "O3 (ozone gas)",
              "amount": "until solution turns blue (~2 h)",
              "role": "oxidant"
            },
            {
              "compound_id": null,
              "name": "NEt3",
              "amount": "1.2 mL (8.0 mmol, 1.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C60",
              "name": "NaBH4",
              "amount": "0.46 g (12 mmol, 1.5 equiv)",
              "role": "reductant"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "0.4 L (ozonolysis)"
            }
          ],
          "conditions": {
            "temperature": "−78 °C (ozonolysis); 0 °C (NaBH4 reduction)",
            "time": "~2 h ozonolysis; 1 h N2 purge/NEt3; 5 h NaBH4 reduction at 0 °C",
            "atmosphere": "N2 (after ozone purging)",
            "ph": null,
            "other": "Crude diluted in MeOH (84 mL) at 0 °C for NaBH4 step; quenched with H2O; extracted with EtOAc (3×)."
          },
          "product": {
            "compound_id": "C46",
            "name": "S18a,b (5:1 diastereomeric mixture)",
            "yield": "3.12 g (76%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, Hexanes/EtOAc 80:20",
          "notes": "Crude washed with 0.1 M citric acid and saturated NaHCO3 before NaBH4 step."
        },
        {
          "step_number": 5,
          "reaction_type": "O-Methylation of primary alcohol",
          "reactants": [
            {
              "compound_id": "C46",
              "name": "S18a,b",
              "amount": "425 mg (0.832 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C47",
              "name": "2,6-di-tert-butyl-4-methylpyridine (DTBMP)",
              "amount": "683 mg (3.33 mmol, 4.00 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C48",
              "name": "MeOTf",
              "amount": "0.66 mL (5.8 mmol, 7.0 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "8.5 mL"
            }
          ],
          "conditions": {
            "temperature": "40 °C",
            "time": "18 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with water; aqueous layer extracted with CH2Cl2 (3×)."
          },
          "product": {
            "compound_id": "C49",
            "name": "S19a,b (4:1 diastereomeric mixture)",
            "yield": "373 mg (85%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, Hexanes/EtOAc 80:20",
          "notes": null
        },
        {
          "step_number": 6,
          "reaction_type": "N-Glycosylation (Vorbrüggen-type)",
          "reactants": [
            {
              "compound_id": "C49",
              "name": "S19a,b",
              "amount": "231 mg (0.440 mmol)"
            },
            {
              "compound_id": "C50",
              "name": "2-chloroadenine",
              "amount": "149 mg (0.880 mmol, 2.00 equiv)",
              "role": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C51",
              "name": "BSA",
              "amount": "0.70 mL (2.9 mmol, 6.5 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C04",
              "name": "TMSOTf",
              "amount": "0.16 mL (0.88 mmol, 2.0 equiv)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "anhydrous DCE (1,2-dichloroethane)",
              "volume": "1.8 mL (for base activation) + 0.88 mL (for sugar)"
            }
          ],
          "conditions": {
            "temperature": "84 °C",
            "time": "3 h",
            "atmosphere": null,
            "ph": null,
            "other": "2-Chloroadenine activated with BSA at 84 °C until clear, then added to sugar solution; diluted with EtOAc and saturated NaHCO3."
          },
          "product": {
            "compound_id": "C52",
            "name": "S20a,b (1.2:1 dr in favor of β)",
            "yield": "222 mg (88%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, CH2Cl2/MeOH 70:30",
          "notes": "~1.2:1 diastereomeric ratio by 1H NMR."
        },
        {
          "step_number": 7,
          "reaction_type": "Selective TBS deprotection (anomeric position)",
          "reactants": [
            {
              "compound_id": "C52",
              "name": "S20a,b",
              "amount": "295 mg (0.515 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C53",
              "name": "TFA/H2O (1:1)",
              "amount": "2.86 mL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "5.7 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C",
            "time": "4 h",
            "atmosphere": null,
            "ph": null,
            "other": "Saturated NaHCO3 added; warmed to room temperature; extracted with Et2O (4×)."
          },
          "product": {
            "compound_id": null,
            "name": "S21a (27%) and S21b (38%) — isolated separately",
            "yield": "S21a: 64 mg (27%); S21b: 89 mg (38%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, EtOAc/MeOH 90:10",
          "notes": "S21a and S21b are diastereomers at C1′; S21b (major, β-configured) used in next step."
        },
        {
          "step_number": 8,
          "reaction_type": "O-Phosphorylation (diethyl phosphate on S21b)",
          "reactants": [
            {
              "compound_id": "C55",
              "name": "S21b",
              "amount": "84 mg (0.18 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl (1 M in THF)",
              "amount": "0.46 mL (0.46 mmol, 2.5 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C13",
              "name": "diethylchlorophosphate",
              "amount": "40 μL (0.28 mmol, 1.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "1.1 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "16 h (after 30 min Grignard formation)",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with MeOH."
          },
          "product": {
            "compound_id": "C56",
            "name": "S22",
            "yield": "47 mg (43%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, Hexanes/EtOAc 0:100",
          "notes": null
        },
        {
          "step_number": 9,
          "reaction_type": "TBS deprotection with TBAF",
          "reactants": [
            {
              "compound_id": "C56",
              "name": "S22",
              "amount": "45 mg (0.076 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C57",
              "name": "TBAF (1.0 M in THF)",
              "amount": "1.5 mL (0.15 mmol, 2.0 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "0.76 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C then room temperature",
            "time": "16 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with MeOH."
          },
          "product": {
            "compound_id": "C58",
            "name": "18",
            "yield": "31 mg (85%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, EtOAc/MeOH 50:50",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P9",
      "pathway_name": "Synthesis of compound 19 (C3′-O-benzyl analogue)",
      "source_section": "main_text",
      "target_compound_id": "C69",
      "target_compound_name": "19",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Reduction of aldehydes to alcohols",
          "reactants": [
            {
              "compound_id": "C59",
              "name": "S23a,b (aldehydes)",
              "amount": "12.0 g (24.6 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C60",
              "name": "NaBH4",
              "amount": "1.02 g (27 mmol, 1.1 equiv)",
              "role": "reductant"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "0.16 L"
            }
          ],
          "conditions": {
            "temperature": "0 °C",
            "time": "3 h",
            "atmosphere": null,
            "ph": null,
            "other": "H2O added upon completion; warmed to RT; concentrated then diluted with EtOAc; filtered over silica with Et2O."
          },
          "product": {
            "compound_id": null,
            "name": "crude alcohols from S23a,b",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Filtered over silica with Et2O; used crude in next step",
          "notes": "Product used crude without further purification."
        },
        {
          "step_number": 2,
          "reaction_type": "O-Benzylation of C3′-OH",
          "reactants": [
            {
              "compound_id": null,
              "name": "crude alcohols from S23a,b",
              "amount": "2.53 g (4.36 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C61",
              "name": "benzyl 2,2,2-trichloroacetimidate",
              "amount": "2.4 mL (13 mmol, 3.0 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C62",
              "name": "TfOH (catalytic)",
              "amount": "50 μL (0.44 mmol, 0.10 equiv)",
              "role": "acid"
            },
            {
              "compound_id": null,
              "name": "NEt3 (quench)",
              "amount": "92 μL (0.65 mmol, 0.15 equiv)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DCM/cyclohexane (1:2)",
              "volume": "44 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C then room temperature",
            "time": "16 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with NEt3 at 0 °C, stirred 15 min; filtered over Celite with DCM."
          },
          "product": {
            "compound_id": null,
            "name": "anomeric benzoates with C3′-OBn (crude)",
            "yield": null,
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Filtered over Celite; used crude",
          "notes": "Crude anomeric benzoates carried directly to N-glycosylation."
        },
        {
          "step_number": 3,
          "reaction_type": "N-Glycosylation with 2,6-dichloropurine",
          "reactants": [
            {
              "compound_id": null,
              "name": "crude anomeric benzoates (C3′-OBn)",
              "amount": "in MeCN (22 mL, 0.20 M)"
            },
            {
              "compound_id": "C02",
              "name": "2,6-dichloropurine",
              "amount": "907 mg (4.79 mmol, 1.10 equiv)",
              "role": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C03",
              "name": "DBU",
              "amount": "2.0 mL (13 mmol, 3.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C04",
              "name": "TMSOTf",
              "amount": "3.21 mL (17.4 mmol, 4.00 equiv)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "dry MeCN",
              "volume": "22 mL"
            }
          ],
          "conditions": {
            "temperature": "−10 °C",
            "time": "5 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with saturated NaHCO3; washed with NaHCO3 and 0.1 M citric acid; dried over MgSO4."
          },
          "product": {
            "compound_id": "C63",
            "name": "S24 (β-anomer)",
            "yield": "1.58 g (56% over 3 steps from S23a,b)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, Hexanes/EtOAc 70:30",
          "notes": "~10:1 dr by 1H NMR in favor of β-anomer."
        },
        {
          "step_number": 4,
          "reaction_type": "Ammonolysis / debenzoylation / C6-amination",
          "reactants": [
            {
              "compound_id": "C63",
              "name": "S24",
              "amount": "371 mg (0.573 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C06",
              "name": "NH3(g)",
              "amount": "saturation (twice)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "12 mL"
            }
          ],
          "conditions": {
            "temperature": "80 °C",
            "time": "24 h, then second NH3 saturation and 16 h at 80 °C",
            "atmosphere": null,
            "ph": null,
            "other": "Performed in high-pressure flask."
          },
          "product": {
            "compound_id": "C64",
            "name": "S25",
            "yield": "178 mg (74%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, CH2Cl2/MeOH 90:10",
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "Bis-TBS protection of primary alcohols",
          "reactants": [
            {
              "compound_id": "C64",
              "name": "S25",
              "amount": "317 mg (0.756 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C65",
              "name": "2,6-lutidine",
              "amount": "0.44 mL (3.8 mmol, 5.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C37",
              "name": "TBSOTf",
              "amount": "0.52 mL (2.3 mmol, 3.0 equiv)",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DCM",
              "volume": "7.6 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C then room temperature",
            "time": "16 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with saturated NaHCO3; diluted with Et2O; washed with brine and 0.1 N HCl."
          },
          "product": {
            "compound_id": "C66",
            "name": "S26",
            "yield": "321 mg (65%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, Hexanes/EtOAc 60:40",
          "notes": "1 drop of DMF added as additive."
        },
        {
          "step_number": 6,
          "reaction_type": "Selective mono-TBS deprotection (C5′-TBS removal)",
          "reactants": [
            {
              "compound_id": "C66",
              "name": "S26",
              "amount": "358 mg (0.552 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C53",
              "name": "TFA/H2O (1:1)",
              "amount": "3.1 mL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "6.1 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C",
            "time": "4 h",
            "atmosphere": null,
            "ph": null,
            "other": "Saturated NaHCO3 added; extracted with Et2O (2×); washed with brine."
          },
          "product": {
            "compound_id": "C67",
            "name": "S27",
            "yield": "207 mg (70%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, CH2Cl2/MeOH 95:5",
          "notes": null
        },
        {
          "step_number": 7,
          "reaction_type": "O-Phosphorylation (diethyl phosphate installation)",
          "reactants": [
            {
              "compound_id": "C67",
              "name": "S27",
              "amount": "200 mg (0.374 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl",
              "amount": "0.56 mL (0.56 mmol, 1.5 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C13",
              "name": "diethylchlorophosphate",
              "amount": "81 μL (0.56 mmol, 1.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "4 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "16 h (after 45 min Grignard formation)",
            "atmosphere": null,
            "ph": null,
            "other": "MeOH added; concentrated under reduced pressure."
          },
          "product": {
            "compound_id": "C68",
            "name": "S28",
            "yield": "216 mg (86%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN gradient",
          "notes": null
        },
        {
          "step_number": 8,
          "reaction_type": "TBS deprotection (acid-mediated)",
          "reactants": [
            {
              "compound_id": "C68",
              "name": "S28",
              "amount": "29.3 mg (0.0437 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C15",
              "name": "TFA/H2O (8:2)",
              "amount": "0.5 mL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "4 h",
            "atmosphere": null,
            "ph": null,
            "other": "MeOH added; concentrated; coevaporated with MeOH (3×)."
          },
          "product": {
            "compound_id": "C69",
            "name": "19",
            "yield": "10.9 mg (45%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN 50:50",
          "notes": null
        }
      ]
    }
  ]
}
```
##### Attempt 2
```
{
  "extraction": {
    "prompt_version": "v3.2",
    "extraction_date": "2026-03-31",
    "model_name": "claude-sonnet-4-6",
    "extractor_notes": "SI found: jm5c01999_si_001.pdf. SI document examined in full. SI contains only: (1) supplementary biological figures (Figures S1–S8), (2) stereochemical proofs (Figure S9–S11, Tables S1–S7, Figure S11), and (3) NMR spectra and HPLC-UV chromatograms for the final compounds (pages S18–S122). No additional synthesis schemes (Scheme S1, S2, etc.) and no new experimental procedures are present in the SI — all synthesis is contained in the main article Experimental Section. SI schemes identified: none. SI compounds identified (author labels): S1 through S28 — all appear in and are fully described in the main text Experimental Section. Total pathway count: 9 (P1 = compound 11/LCB-2122; P2 = compound 12; P3 = compound 13; P4 = compound 14; P5 = compound 15; P6 = compound 16; P7 = compound 17; P8 = compound 18; P9 = compound 19). Excluded reference compounds: AMP (adenosine monophosphate, cited for comparison only), MK-8722, AICA riboside, resveratrol, quercetin, berberine, metformin, canagliflozin, doxorubicin (biological tool), imatinib mesylate (biological tool), compound C (AMPK inhibitor, used in biological assays only), dexrazoxane. S1 (benzoylated sugar lactone precursor, referenced as ref 31) and S10 (4'-thio primary alcohol, referenced as ref 45) and S14 (secondary alcohol lactone precursor, referenced as ref 31) and S23a,b (aldehydes, referenced as ref 31) and S4 (previously reported nucleoside, referenced as ref 32) are commercially or previously synthesized and referenced to prior publications; they appear as starting materials in this study. Mass data: all masses are exact masses (HRMS, ESI) except where noted as nominal MW. Monoisotopic masses are used in HRMS. Note compound 12 purity: paper states >95% HPLC for all tested compounds; compound 12 was not listed in HPLC-UV section (only 11, 13, 14, 15, 16, 17, 18, 19 listed) — purity set to >95% by HPLC per general statement."
  },

  "paper": {
    "title": "A Nucleoside Analogue Bearing a C2′-Stereogenic All-Carbon Quaternary Center for the Treatment of Heart Failure",
    "authors": [
      "Abir Almazloum",
      "Wael Maharsy",
      "Starr Dostie",
      "Fabiola Becerril-Jiménez",
      "Carla Eymard",
      "Hiba Komati",
      "Louis Leblanc",
      "Amarender Manchoju",
      "Philippe Mochirian",
      "Renaud Zelli",
      "Michel Prevost",
      "Mona Nemer",
      "Yvan Guindon"
    ],
    "doi": "10.1021/acs.jmedchem.5c01999",
    "journal": "Journal of Medicinal Chemistry",
    "year": 2025,
    "synthesis_scale": "lab",
    "method_completeness": "full",
    "has_synthesis": true,
    "extraction_notes": "All synthesis procedures are in the main text Experimental Section. SI contains NMR spectra, HPLC chromatograms, stereochemical proofs, and X-ray data only — no additional synthesis schemes or procedures. Compounds S1, S4, S10, S14, and S23a,b are previously reported materials from prior Guindon lab publications (refs 31, 32, 45) used as starting materials."
  },

  "compounds": [
    {
      "id": "C01",
      "name": "S1 (benzoylated sugar lactone; 3,4-anti-configured α-bromo lactone precursor)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Previously reported by Guindon lab (ref 31, Becerril-Jiménez et al., J. Org. Chem. 2019)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Benzoylated sugar lactone with 3,4-anti configuration bearing an α-bromo group, used as the substrate in Vorbrüggen glycosylation to give S2."
    },
    {
      "id": "C02",
      "name": "2,6-Dichloropurine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Nucleobase used in Vorbrüggen-type glycosylation reactions to install the 2,6-dichloropurine onto sugar electrophiles."
    },
    {
      "id": "C03",
      "name": "DBU (1,8-diazabicyclo[5.4.0]undec-7-ene)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Non-nucleophilic base used to activate the glycosylation reaction."
    },
    {
      "id": "C04",
      "name": "TMSOTf (trimethylsilyl trifluoromethanesulfonate)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Lewis acid activator used to promote Vorbrüggen-type glycosylation."
    },
    {
      "id": "C05",
      "name": "S2 (−)-((2R,3R,4S,5R)-3-(Benzoyloxy)-5-(2,6-dichloro-9H-purin-9-yl)-4-methyltetrahydrofuran-2,4-diyl)bis(methylene)dibenzoate",
      "iupac_name": "(−)-((2R,3R,4S,5R)-3-(Benzoyloxy)-5-(2,6-dichloro-9H-purin-9-yl)-4-methyltetrahydrofuran-2,4-diyl)bis(methylene)dibenzoate",
      "molecular_formula": "C33H26Cl2N4O7",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 683.1066",
      "ms_calculated_exact_mass": null,
      "description": "Perbenzoylated 2,6-dichloropurine nucleoside intermediate obtained as a 10:1 β/α anomeric mixture; key glycosylation product used in two downstream routes (ammonolysis to S3/S4, and NaOH debenzoylation to S12)."
    },
    {
      "id": "C06",
      "name": "NH3 (ammonia gas)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Gaseous ammonia used under pressure to effect simultaneous debenzoylation and aminolysis of the 6-chloro position of the purine."
    },
    {
      "id": "C07",
      "name": "S3 (+)-((2R,3S,4R,5R)-5-(2-Chloro-6-methoxy-9H-purin-9-yl)-3-hydroxy-4-methyltetrahydrofuran-2,4-diyl)dimethanol",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(2-Chloro-6-methoxy-9H-purin-9-yl)-3-hydroxy-4-methyltetrahydrofuran-2,4-diyl)dimethanol",
      "molecular_formula": "C13H17ClN4O5",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 367.0781",
      "ms_calculated_exact_mass": null,
      "description": "6-Methoxypurine nucleoside triol byproduct of the ammonolysis of S2; β-stereochemistry confirmed by X-ray analysis of the EtOAc crystal."
    },
    {
      "id": "C08",
      "name": "S4 (−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-methyltetrahydrofuran-2,4-diyl)dimethanol",
      "iupac_name": "(−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-methyltetrahydrofuran-2,4-diyl)dimethanol",
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Previously reported by Guindon lab (ref 32, Manchoju et al., Molecules 2022); also obtained in-house as byproduct of S2 ammonolysis",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "2-Chloroadenosine-like nucleoside triol; the key previously reported intermediate used as starting material for acetonide formation (S5) and the core scaffold for LCB-2122 and all analogues."
    },
    {
      "id": "C09",
      "name": "CSA (camphorsulfonic acid)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acid catalyst used in acetonide (isopropylidene) protection steps."
    },
    {
      "id": "C10",
      "name": "2,2-Dimethoxypropane",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Reagent for acetonide (isopropylidene ketal) formation under acidic conditions."
    },
    {
      "id": "C11",
      "name": "S5 (+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methanol",
      "iupac_name": "(+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methanol",
      "molecular_formula": "C15H20ClN5O4",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 392.1104",
      "ms_calculated_exact_mass": null,
      "description": "Acetonide-protected nucleoside with free primary alcohol at C5'; central intermediate diverging into four phosphorylation pathways (S6, S7, S8, S9)."
    },
    {
      "id": "C12",
      "name": "t-BuMgCl (tert-butylmagnesium chloride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Grignard base used to deprotonate the primary alcohol before phosphorylation with chlorophosphate electrophiles."
    },
    {
      "id": "C13",
      "name": "Diethylchlorophosphate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Phosphorylating agent used to install the diethyl phosphate ester at C5'."
    },
    {
      "id": "C14",
      "name": "S6 (+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Diethyl Phosphate",
      "iupac_name": "(+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C19H29ClN5O7P",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 528.1386",
      "ms_calculated_exact_mass": null,
      "description": "Acetonide-protected diethyl phosphate intermediate; directly precedes acetonide deprotection to give LCB-2122 (compound 11)."
    },
    {
      "id": "C15",
      "name": "TFA/H2O (trifluoroacetic acid/water mixture 8:2)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acidic mixture used to remove the acetonide protecting group in the final deprotection steps."
    },
    {
      "id": "C16",
      "name": "11 (LCB-2122) (+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C16H25ClN5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 488.1072",
      "ms_calculated_exact_mass": null,
      "description": "Lead cardioprotective compound LCB-2122; 2-chloroadenosine-like nucleoside monophosphate diethyl ester with C2'-all-carbon quaternary center; evaluated in vitro and in vivo as cardioprotective agent."
    },
    {
      "id": "C17",
      "name": "Et3N (triethylamine)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amine base used in phosphorylation reactions (POCl3 step for compound 12 synthesis)."
    },
    {
      "id": "C18",
      "name": "POCl3 (phosphorus oxychloride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Reagent used to install a monophosphate ester at the primary alcohol of S5."
    },
    {
      "id": "C19",
      "name": "S7 Triethylammonium (+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Hydrogen Phosphate",
      "iupac_name": "Triethylammonium (+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Hydrogen Phosphate",
      "molecular_formula": "C21H36ClN6O7P",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 551.2138",
      "ms_calculated_exact_mass": null,
      "description": "Acetonide-protected monophosphate triethylammonium salt intermediate on the route to compound 12."
    },
    {
      "id": "C20",
      "name": "12 (+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Dihydrogen Phosphate",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Dihydrogen Phosphate",
      "molecular_formula": "C12H17ClN5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M−H]− 408.0482",
      "ms_calculated_exact_mass": null,
      "description": "Free monophosphate analogue of LCB-2122; inactive in Dox-induced cell death assay, presumably due to poor cellular uptake of the charged species."
    },
    {
      "id": "C21",
      "name": "Dimethylchlorophosphate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Phosphorylating agent used to install the dimethyl phosphate ester at C5'."
    },
    {
      "id": "C22",
      "name": "S8 (+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Dimethyl Phosphate",
      "iupac_name": "(+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Dimethyl Phosphate",
      "molecular_formula": "C17H25ClN5O7P",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 500.1061",
      "ms_calculated_exact_mass": null,
      "description": "Acetonide-protected dimethyl phosphate intermediate on the route to compound 13."
    },
    {
      "id": "C23",
      "name": "13 (+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Dimethyl Phosphate",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Dimethyl Phosphate",
      "molecular_formula": "C14H21ClN5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 460.0765",
      "ms_calculated_exact_mass": null,
      "description": "Dimethyl phosphate ester analogue of LCB-2122; inactive in cardioprotection assay."
    },
    {
      "id": "C24",
      "name": "Diisopropyl chlorophosphate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Phosphorylating agent used to install the diisopropyl phosphate ester at C5'."
    },
    {
      "id": "C25",
      "name": "S9 (+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Diisopropyl Phosphate",
      "iupac_name": "(+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Diisopropyl Phosphate",
      "molecular_formula": "C21H33ClN5O7P",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 534.1868",
      "ms_calculated_exact_mass": null,
      "description": "Acetonide-protected diisopropyl phosphate intermediate on the route to compound 14."
    },
    {
      "id": "C26",
      "name": "14 (+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diisopropyl Phosphate",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diisopropyl Phosphate",
      "molecular_formula": "C18H29ClN5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 516.1398",
      "ms_calculated_exact_mass": null,
      "description": "Diisopropyl phosphate ester analogue of LCB-2122; retains cardioprotective activity, indicating LCB-2122 is not a prodrug of the free phosphate."
    },
    {
      "id": "C27",
      "name": "S10 (previously reported 4'-thio primary alcohol)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Previously reported by Guindon lab (ref 45, Eymard et al., Molecules 2024)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "4'-Thionucleoside primary alcohol precursor used to make the 4'-thio diethyl phosphate intermediate S11 en route to compound 15."
    },
    {
      "id": "C28",
      "name": "S11 (−)-((2R,3R,4S,5R)-4-(Benzoyloxy)-2-(2,6-dichloro-9H-purin-9-yl)-5-(((diethoxyphosphoryl)oxy)methyl)-3-methyltetrahydrothiophen-3-yl)methyl Benzoate",
      "iupac_name": "(−)-((2R,3R,4S,5R)-4-(Benzoyloxy)-2-(2,6-dichloro-9H-purin-9-yl)-5-(((diethoxyphosphoryl)oxy)methyl)-3-methyltetrahydrothiophen-3-yl)methyl Benzoate",
      "molecular_formula": "C30H31Cl2N4O8PS",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 709.1048",
      "ms_calculated_exact_mass": null,
      "description": "4'-Thionucleoside dibenzoate diethyl phosphate intermediate with 2,6-dichloropurine; subjected to ammonolysis to give compound 15."
    },
    {
      "id": "C29",
      "name": "15 (+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrothiophen-2-yl)methyl Diethyl Phosphate",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrothiophen-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C16H25ClN5O6PS",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 504.0841",
      "ms_calculated_exact_mass": null,
      "description": "4'-Thio analogue of LCB-2122; shows lowered cardioprotective activity compared to the oxygen furanoside."
    },
    {
      "id": "C30",
      "name": "Palladium on carbon (Pd/C, 10 wt%)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "catalyst",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Heterogeneous hydrogenation catalyst used to remove the C2-chloro substituent from LCB-2122 under H2 atmosphere."
    },
    {
      "id": "C31",
      "name": "16 (−)-((2R,3S,4R,5R)-5-(6-Amino-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "iupac_name": "(−)-((2R,3S,4R,5R)-5-(6-Amino-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C16H26N5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+H]+ 432.1642",
      "ms_calculated_exact_mass": null,
      "description": "2-Dechlorinated analogue of LCB-2122 (adenosine diethyl phosphate analogue); inactive, implicating the 2-Cl-purine in pharmacological activity."
    },
    {
      "id": "C32",
      "name": "NaOH (sodium hydroxide, 2N aqueous)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base used to hydrolyze the three benzoate esters of S2 en route to triol S12."
    },
    {
      "id": "C33",
      "name": "S12 (+)-2-Chloro-9-((2R,3R,4S,5R)-4-hydroxy-3,5-bis(hydroxymethyl)-3-methyltetrahydrofuran-2-yl)-1,9-dihydro-6H-purin-6-one",
      "iupac_name": "(+)-2-Chloro-9-((2R,3R,4S,5R)-4-hydroxy-3,5-bis(hydroxymethyl)-3-methyltetrahydrofuran-2-yl)-1,9-dihydro-6H-purin-6-one",
      "molecular_formula": "C12H15ClN4O5",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 353.0618",
      "ms_calculated_exact_mass": null,
      "description": "2-Chloro inosine triol analogue obtained by NaOH-mediated debenzoylation of S2; intermediate on the route to compound 17."
    },
    {
      "id": "C34",
      "name": "S13 (+)-2-Chloro-9-((4aR,5R,7R,7aS)-7-(hydroxymethyl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-5-yl)-1,9-dihydro-6H-purin-6-one",
      "iupac_name": "(+)-2-Chloro-9-((4aR,5R,7R,7aS)-7-(hydroxymethyl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-5-yl)-1,9-dihydro-6H-purin-6-one",
      "molecular_formula": "C15H19ClN4O5",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 393.0944",
      "ms_calculated_exact_mass": null,
      "description": "Acetonide-protected 2-chloroinosine primary alcohol intermediate; phosphorylated and deprotected in a one-pot sequence to give compound 17."
    },
    {
      "id": "C35",
      "name": "17 (+)-((2R,3S,4R,5R)-5-(2-Chloro-9H-purin-9-yl-6-one)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(2-Chloro-9H-purin-9-yl-6-one)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C16H24ClN4O8P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M−H]− 465.0949",
      "ms_calculated_exact_mass": null,
      "description": "Inosine (2-chlorohypoxanthine) analogue of LCB-2122 bearing a 6-oxo group instead of 6-amino; inactive, implicating the 2-chloroadenine pharmacophore."
    },
    {
      "id": "C36",
      "name": "S14 (previously reported secondary alcohol lactone)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Previously reported by Guindon lab (ref 31, Becerril-Jiménez et al., J. Org. Chem. 2019)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Previously reported secondary alcohol lactone precursor used as the starting point for the synthesis of compound 18 via TBS protection to give S15."
    },
    {
      "id": "C37",
      "name": "TBSOTf (tert-butyldimethylsilyl trifluoromethanesulfonate)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Silylating agent used to introduce TBS protecting groups on hydroxyl groups."
    },
    {
      "id": "C38",
      "name": "Imidazole",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base/catalyst used to promote TBS silylation of secondary alcohol S14."
    },
    {
      "id": "C39",
      "name": "S15 (+)-(3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-methyl-3-vinyldihydrofuran-2(3H)-one",
      "iupac_name": "(+)-(3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-methyl-3-vinyldihydrofuran-2(3H)-one",
      "molecular_formula": "C20H40O4Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 423.2356",
      "ms_calculated_exact_mass": null,
      "description": "Bis-TBS-protected vinyl lactone; reduced with DIBAL-H to give lactol S16a,b."
    },
    {
      "id": "C40",
      "name": "DIBAL-H (diisobutylaluminium hydride, 1 M in hexanes)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Reducing agent used for selective reduction of lactone S15 to lactol S16a,b at −78 °C."
    },
    {
      "id": "C41",
      "name": "S16a,b (3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-methyl-3-vinyltetrahydrofuran-2-ol (2:1 mixture of diastereomers)",
      "iupac_name": null,
      "molecular_formula": "C20H42O4Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 425.2514",
      "ms_calculated_exact_mass": null,
      "description": "Lactol mixture (2:1 dr) obtained by DIBAL-H reduction of lactone S15; benzoylated at the anomeric position to give S17a,b."
    },
    {
      "id": "C42",
      "name": "BzCl (benzoyl chloride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acylating agent used to install the anomeric benzoate on lactols S16a,b and to introduce the benzoate activating group."
    },
    {
      "id": "C43",
      "name": "DMAP (4-dimethylaminopyridine)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Nucleophilic catalyst used to promote benzoylation."
    },
    {
      "id": "C44",
      "name": "Pyridine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base used in benzoylation reactions."
    },
    {
      "id": "C45",
      "name": "Ethylenediamine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Quench reagent added at 0 °C to consume excess BzCl."
    },
    {
      "id": "C46",
      "name": "S17a,b (3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-methyl-3-vinyltetrahydrofuran-2-yl Benzoate (2:1 mixture)",
      "iupac_name": null,
      "molecular_formula": "C27H46O5Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 529.2777",
      "ms_calculated_exact_mass": null,
      "description": "Anomeric benzoate vinyl-furanose mixture; vinyl group cleaved by ozonolysis followed by NaBH4 reduction to give primary alcohol S18a,b."
    },
    {
      "id": "C47",
      "name": "O3 (ozone)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial (generated in situ)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Reagent for ozonolysis of the vinyl group in S17a,b to give an aldehyde intermediate."
    },
    {
      "id": "C48",
      "name": "NEt3 (triethylamine, used as ozonolysis workup reductant)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base added after ozonolysis to facilitate reductive workup before NaBH4 reduction."
    },
    {
      "id": "C49",
      "name": "NaBH4 (sodium borohydride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Reducing agent used to convert the ozonolysis-derived aldehyde to a primary alcohol."
    },
    {
      "id": "C50",
      "name": "S18a,b (3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-(hydroxymethyl)-3-methyltetrahydrofuran-2-yl Benzoate (5:1 mixture)",
      "iupac_name": null,
      "molecular_formula": "C26H46O6Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 533.2729",
      "ms_calculated_exact_mass": null,
      "description": "Primary alcohol anomeric benzoate mixture (5:1 dr); C2'-hydroxymethyl methylated with MeOTf to give S19a,b."
    },
    {
      "id": "C51",
      "name": "MeOTf (methyl trifluoromethanesulfonate)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Powerful methylating agent used to convert the primary hydroxymethyl group of S18a,b into a methoxymethyl group."
    },
    {
      "id": "C52",
      "name": "2,6-di-tert-butyl-4-methylpyridine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Hindered base (proton sponge) used to prevent O-methylation side reactions during MeOTf methylation."
    },
    {
      "id": "C53",
      "name": "S19a,b (3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-(methoxymethyl)-3-methyltetrahydrofuran-2-yl Benzoate (4:1 mixture)",
      "iupac_name": null,
      "molecular_formula": "C27H48O6Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 547.2889",
      "ms_calculated_exact_mass": null,
      "description": "Methoxymethyl-bearing anomeric benzoate sugar mixture (4:1 dr); used in Vorbrüggen-type glycosylation with 2-chloroadenine to give S20a,b."
    },
    {
      "id": "C54",
      "name": "2-Chloroadenine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Nucleobase used in BSA/TMSOTf-mediated glycosylation to install the 2-chloroadenine onto the sugar S19a,b."
    },
    {
      "id": "C55",
      "name": "BSA (N,O-bis(trimethylsilyl)acetamide)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Silylating agent used to per-silylate 2-chloroadenine and render it reactive in Vorbrüggen glycosylation."
    },
    {
      "id": "C56",
      "name": "S20a,b 9-((3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-(methoxymethyl)-3-methyltetrahydrofuran-2-yl)-2-chloro-9H-purin-6-amine (1.2:1 α/β mixture)",
      "iupac_name": null,
      "molecular_formula": "C25H46ClN5O4Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 572.2852",
      "ms_calculated_exact_mass": null,
      "description": "Bis-TBS-protected nucleoside anomeric mixture (1.2:1 β/α) obtained from glycosylation; partially deprotected with TFA/H2O to give S21a and S21b."
    },
    {
      "id": "C57",
      "name": "TFA/H2O (1:1) (trifluoroacetic acid / water 1:1)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acidic mixture used for selective partial TBS deprotection at 0 °C to remove one TBS group selectively."
    },
    {
      "id": "C58",
      "name": "S21a (+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-((tert-butyldimethylsilyl)oxy)-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methanol",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-((tert-butyldimethylsilyl)oxy)-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methanol",
      "molecular_formula": "C19H32ClN5O4Si",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 458.1982",
      "ms_calculated_exact_mass": null,
      "description": "α-Anomer partially deprotected nucleoside alcohol (27% yield); not used further in the described synthesis of compound 18."
    },
    {
      "id": "C59",
      "name": "S21b (−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-((tert-butyldimethylsilyl)oxy)-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methanol",
      "iupac_name": "(−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-((tert-butyldimethylsilyl)oxy)-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methanol",
      "molecular_formula": "C19H32ClN5O4Si",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 458.1984",
      "ms_calculated_exact_mass": null,
      "description": "β-Anomer partially deprotected nucleoside primary alcohol (38% yield); used for phosphorylation to give S22."
    },
    {
      "id": "C60",
      "name": "S22 (+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-((tert-butyldimethylsilyl)oxy)-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-((tert-butyldimethylsilyl)oxy)-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C23H41ClN5O7PSi",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 594.2271",
      "ms_calculated_exact_mass": null,
      "description": "TBS-protected diethyl phosphate nucleoside; TBS removed with TBAF to give final compound 18."
    },
    {
      "id": "C61",
      "name": "TBAF (tetrabutylammonium fluoride, 1.0 M in THF)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fluoride source used to remove the TBS protecting group from S22 to give compound 18."
    },
    {
      "id": "C62",
      "name": "18 (−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "iupac_name": "(−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C17H27ClN5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+H]+ 480.1399",
      "ms_calculated_exact_mass": null,
      "description": "C2'-methoxymethyl analogue of LCB-2122 (C2'-OH methylated); retains cardioprotective activity."
    },
    {
      "id": "C63",
      "name": "S23a,b (previously reported aldehydes)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Previously reported by Guindon lab (ref 31, Becerril-Jiménez et al., J. Org. Chem. 2019)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Previously reported aldehyde mixture used as starting material for compound 19 synthesis; reduced then O-benzylated and glycosylated."
    },
    {
      "id": "C64",
      "name": "Benzyl 2,2,2-trichloroacetimidate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Benzylating reagent used under TfOH catalysis to introduce the O-benzyl protecting group at C3'."
    },
    {
      "id": "C65",
      "name": "TfOH (triflic acid)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acid catalyst for the benzyl trichloroacetimidate O-benzylation step."
    },
    {
      "id": "C66",
      "name": "S24 (+)-((2R,3S,4R,5R)-3-(Benzyloxy)-5-(2,6-dichloro-9H-purin-9-yl)-4-methyltetrahydrofuran-2,4-diyl)bis(methylene) Dibenzoate",
      "iupac_name": "(+)-((2R,3S,4R,5R)-3-(Benzyloxy)-5-(2,6-dichloro-9H-purin-9-yl)-4-methyltetrahydrofuran-2,4-diyl)bis(methylene) Dibenzoate",
      "molecular_formula": "C33H28Cl2N4O6",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 669.1272",
      "ms_calculated_exact_mass": null,
      "description": "3'-Benzylated dibenzoate 2,6-dichloropurine nucleoside (β-anomer, 10:1 dr); obtained in 56% over 3 steps and converted to diol S25 by ammonolysis."
    },
    {
      "id": "C67",
      "name": "S25 (−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-methyltetrahydrofuran-2,4-diyl)dimethanol",
      "iupac_name": "(−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-methyltetrahydrofuran-2,4-diyl)dimethanol",
      "molecular_formula": "C19H22ClN5O4",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 420.1429",
      "ms_calculated_exact_mass": null,
      "description": "3'-Benzyl-protected 2-chloroadenosine diol after ammonolysis of S24; bis-TBS protected in next step to give S26."
    },
    {
      "id": "C68",
      "name": "2,6-Lutidine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Hindered base used to prevent N-silylation during TBSOTf-mediated protection."
    },
    {
      "id": "C69",
      "name": "S26 (+)-9-((2R,3R,4S,5R)-4-(Benzyloxy)-3,5-bis(((tert-butyldimethylsilyl)oxy)methyl)-3-methyltetrahydrofuran-2-yl)-2-chloro-9H-purin-6-amine",
      "iupac_name": "(+)-9-((2R,3R,4S,5R)-4-(Benzyloxy)-3,5-bis(((tert-butyldimethylsilyl)oxy)methyl)-3-methyltetrahydrofuran-2-yl)-2-chloro-9H-purin-6-amine",
      "molecular_formula": "C31H50ClN5O4Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 648.3175",
      "ms_calculated_exact_mass": null,
      "description": "Bis-TBS-protected 3'-benzyl nucleoside; selectively de-TBS-protected at C5' with TFA/H2O to give S27."
    },
    {
      "id": "C70",
      "name": "TFA/H2O (1:1) for selective TBS deprotection of S26",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acidic mixture used at 0 °C for selective removal of one TBS group from S26 to expose the C5'-primary alcohol."
    },
    {
      "id": "C71",
      "name": "S27 (−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-(((tert-butyldimethylsilyl)oxy)methyl)-4-methyltetrahydrofuran-2-yl)methanol",
      "iupac_name": "(−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-(((tert-butyldimethylsilyl)oxy)methyl)-4-methyltetrahydrofuran-2-yl)methanol",
      "molecular_formula": "C25H36ClN5O4Si",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H]+ 534.2290",
      "ms_calculated_exact_mass": null,
      "description": "Selectively deprotected primary alcohol with retained TBS on the C4'-hydroxymethyl; phosphorylated to give S28."
    },
    {
      "id": "C72",
      "name": "S28 (+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-(((tert-butyldimethylsilyl)oxy)methyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-(((tert-butyldimethylsilyl)oxy)methyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C29H45ClN5O7PSi",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 692.2419",
      "ms_calculated_exact_mass": null,
      "description": "TBS/benzyl-protected diethyl phosphate nucleoside; both protecting groups removed with TFA/H2O to give final compound 19."
    },
    {
      "id": "C73",
      "name": "19 (+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C23H31ClN5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+H]+ 556.1748",
      "ms_calculated_exact_mass": null,
      "description": "3'-Benzyl C3'-secondary alcohol analogue of LCB-2122; retains cardioprotective activity, demonstrating tolerance of C3'-benzylation."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of Compound 11 (LCB-2122)",
      "source_section": "main_text",
      "target_compound_id": "C16",
      "target_compound_name": "11 (LCB-2122)",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Vorbrüggen-type N-glycosylation",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "S1 (benzoylated sugar lactone 3,4-anti)",
              "amount": "4.77 g (8.02 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "2,6-Dichloropurine",
              "amount": "1.67 g (8.82 mmol, 1.10 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C03",
              "name": "DBU",
              "amount": "3.67 mL (24.1 mmol, 3.00 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C04",
              "name": "TMSOTf",
              "amount": "5.9 mL (32 mmol, 4.0 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "dry acetonitrile",
              "volume": "32 mL (0.25 M)"
            }
          ],
          "conditions": {
            "temperature": "−10 °C",
            "time": "6 h",
            "atmosphere": null,
            "ph": null,
            "other": "TMSOTf added dropwise after 5 min pre-stirring; quenched with sat. NaHCO3, extracted with DCM, washed with 0.1 M citric acid, dried with MgSO4."
          },
          "product": {
            "compound_id": "C05",
            "name": "S2",
            "yield": "3.96 g (74%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, Hexanes/EtOAc 80:20",
          "notes": "1H NMR of crude showed ~8:1 anomeric ratio; purified product is 10:1 β/α."
        },
        {
          "step_number": 2,
          "reaction_type": "Ammonolysis (simultaneous debenzoylation and purine C6 aminolysis)",
          "reactants": [
            {
              "compound_id": "C05",
              "name": "S2",
              "amount": "3.29 g (4.97 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C06",
              "name": "NH3(g)",
              "amount": "excess (bubbled until saturation)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "50 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "80 °C",
            "time": "24 h",
            "atmosphere": "sealed high-pressure flask",
            "ph": null,
            "other": "Flask rapidly closed with high-pressure seal after NH3 saturation; diluted with MeOH and concentrated."
          },
          "product": {
            "compound_id": "C08",
            "name": "S4",
            "yield": "714 mg (44%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, DCM/MeOH 90:10",
          "notes": "Reaction also produces S3 (702 mg, 43%); with additional NH3 saturation and heating at 80 °C for 48 h, S4 can be obtained in 71% yield. S4 was previously reported by the Guindon lab (ref 32). Only S4 is the substrate for subsequent steps."
        },
        {
          "step_number": 3,
          "reaction_type": "Acetonide (isopropylidene ketal) formation",
          "reactants": [
            {
              "compound_id": "C08",
              "name": "S4",
              "amount": "1.05 g (3.18 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C09",
              "name": "CSA",
              "amount": "737 mg (3.18 mmol, 1.00 equiv)",
              "role": "acid"
            },
            {
              "compound_id": "C10",
              "name": "2,2-Dimethoxypropane",
              "amount": "7.0 mL (57 mmol, 18 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "dry acetone",
              "volume": "32 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "16 h",
            "atmosphere": null,
            "ph": null,
            "other": "Molecular sieves 3 Å (3.0 g) added; reaction concentrated under reduced pressure."
          },
          "product": {
            "compound_id": "C11",
            "name": "S5",
            "yield": "739 mg (63%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, DCM/MeOH 90:10",
          "notes": "Product obtained as white foam."
        },
        {
          "step_number": 4,
          "reaction_type": "O-Phosphorylation (diethyl phosphate installation)",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "S5",
              "amount": "1.13 g (3.06 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl (1.0 M in THF)",
              "amount": "4.6 mL (4.6 mmol, 1.5 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C13",
              "name": "Diethylchlorophosphate",
              "amount": "0.66 mL (4.6 mmol, 1.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "31 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "4 h (after phosphate addition); 45 min (Grignard pre-stirring)",
            "atmosphere": null,
            "ph": null,
            "other": "t-BuMgCl added dropwise; after 45 min diethylchlorophosphate added slowly; quenched with MeOH."
          },
          "product": {
            "compound_id": "C14",
            "name": "S6",
            "yield": "1.33 g (86%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN 50:50",
          "notes": "Product obtained as white foam."
        },
        {
          "step_number": 5,
          "reaction_type": "Acetonide deprotection (acid hydrolysis)",
          "reactants": [
            {
              "compound_id": "C14",
              "name": "S6",
              "amount": "360 mg (0.711 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C15",
              "name": "TFA/H2O (8:2)",
              "amount": "7.1 mL (0.10 M)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "7.1 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "2 h",
            "atmosphere": null,
            "ph": null,
            "other": "MeOH added after 2 h; concentrated and coevaporated with MeOH (3×)."
          },
          "product": {
            "compound_id": "C16",
            "name": "11 (LCB-2122)",
            "yield": "294 mg (88%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN 70:30",
          "notes": "Product obtained as white foam."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of Compound 12 (free monophosphate analogue)",
      "source_section": "main_text",
      "target_compound_id": "C20",
      "target_compound_name": "12",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "O-Phosphorylation with POCl3 (monophosphate installation)",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "S5",
              "amount": "36.7 mg (99.2 μmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C17",
              "name": "Et3N",
              "amount": "124 μL (893 μmol, 9.00 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C18",
              "name": "POCl3",
              "amount": "13.9 μL (149 μmol, 1.50 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "1 mL (0.1 M)"
            }
          ],
          "conditions": {
            "temperature": "0 °C",
            "time": "2 h then 1 h (after ice addition)",
            "atmosphere": null,
            "ph": null,
            "other": "Ice chips added after 2 h with stirring for 1 h at 0 °C; concentrated under reduced pressure."
          },
          "product": {
            "compound_id": "C19",
            "name": "S7 (triethylammonium salt)",
            "yield": "49 mg (90%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN 70:30",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Acetonide deprotection (acid hydrolysis)",
          "reactants": [
            {
              "compound_id": "C19",
              "name": "S7",
              "amount": "156 mg (0.347 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C15",
              "name": "TFA/H2O (8:2)",
              "amount": "3.5 mL (0.10 M)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "3.5 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "4 h",
            "atmosphere": null,
            "ph": null,
            "other": "MeOH added, concentrated, coevaporated with MeOH (3×)."
          },
          "product": {
            "compound_id": "C20",
            "name": "12",
            "yield": "31 mg (22%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN 75:25",
          "notes": "NEt3 was added to resolve NMR signals (acidic NH broadening)."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Synthesis of Compound 13 (dimethyl phosphate analogue)",
      "source_section": "main_text",
      "target_compound_id": "C23",
      "target_compound_name": "13",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "O-Phosphorylation (dimethyl phosphate installation)",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "S5",
              "amount": "54.4 mg (147 μmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl (1.0 M in THF)",
              "amount": "0.16 mL (0.16 mmol, 1.1 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C21",
              "name": "Dimethylchlorophosphate",
              "amount": "18 μL (0.16 mmol, 1.1 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "1.5 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "4.5 h (after phosphate addition); 45 min (Grignard pre-stirring)",
            "atmosphere": null,
            "ph": null,
            "other": "t-BuMgCl added dropwise; quenched with MeOH; 18.3 mg (34%) of S5 recovered."
          },
          "product": {
            "compound_id": "C22",
            "name": "S8",
            "yield": "35 mg (50%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, DCM/MeOH 95:5",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Acetonide deprotection (acid hydrolysis)",
          "reactants": [
            {
              "compound_id": "C22",
              "name": "S8",
              "amount": "24.7 mg (51.7 μmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C15",
              "name": "TFA/H2O (8:2)",
              "amount": "0.6 mL (0.09 M)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "0.6 mL (0.09 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "3 h",
            "atmosphere": null,
            "ph": null,
            "other": "MeOH added, concentrated, coevaporated with MeOH (3×)."
          },
          "product": {
            "compound_id": "C23",
            "name": "13",
            "yield": "8.2 mg (36%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN 50:50",
          "notes": "Product obtained as white foam."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Synthesis of Compound 14 (diisopropyl phosphate analogue)",
      "source_section": "main_text",
      "target_compound_id": "C26",
      "target_compound_name": "14",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "O-Phosphorylation (diisopropyl phosphate installation)",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "S5",
              "amount": "75 mg (0.20 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl (1.7 M in THF)",
              "amount": "0.13 mL (0.23 mmol, 1.1 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C24",
              "name": "Diisopropyl chlorophosphate",
              "amount": "40 μL (0.23 mmol, 1.1 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "2 mL (0.1 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "16 h (after phosphate addition); 45 min (Grignard pre-stirring)",
            "atmosphere": null,
            "ph": null,
            "other": "t-BuMgCl added dropwise; quenched with MeOH."
          },
          "product": {
            "compound_id": "C25",
            "name": "S9",
            "yield": "79 mg (73%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, DCM/MeOH 90:10",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Acetonide deprotection (acid hydrolysis)",
          "reactants": [
            {
              "compound_id": "C25",
              "name": "S9",
              "amount": "34.8 mg (0.065 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C15",
              "name": "TFA/H2O (8:2)",
              "amount": "0.7 mL (0.1 M)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "0.7 mL (0.1 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "4 h",
            "atmosphere": null,
            "ph": null,
            "other": "MeOH added, concentrated, coevaporated with MeOH (3×)."
          },
          "product": {
            "compound_id": "C26",
            "name": "14",
            "yield": "24 mg (74%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN 60:40",
          "notes": "Product obtained as white foam."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Synthesis of Compound 15 (4'-thio analogue)",
      "source_section": "main_text",
      "target_compound_id": "C29",
      "target_compound_name": "15",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "O-Phosphorylation (diethyl phosphate on 4'-thio alcohol)",
          "reactants": [
            {
              "compound_id": "C27",
              "name": "S10 (previously reported 4'-thio primary alcohol)",
              "amount": "95 mg (0.17 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl (1.7 M in THF)",
              "amount": "0.15 mL (0.25 mmol, 1.5 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C13",
              "name": "Diethylchlorophosphate",
              "amount": "36 μL (0.25 mmol, 1.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "1.7 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "16 h (after phosphate addition); 45 min (Grignard pre-stirring)",
            "atmosphere": null,
            "ph": null,
            "other": "t-BuMgCl added dropwise."
          },
          "product": {
            "compound_id": "C28",
            "name": "S11",
            "yield": "56 mg (48%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, Hexanes/EtOAc 60:40",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Ammonolysis (debenzoylation and purine C6 aminolysis)",
          "reactants": [
            {
              "compound_id": "C28",
              "name": "S11",
              "amount": "33 mg (0.047 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C06",
              "name": "NH3(g)",
              "amount": "excess (bubbled until saturation, twice)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "1.2 mL (0.040 M)"
            }
          ],
          "conditions": {
            "temperature": "80 °C",
            "time": "16 h then additional 24 h at 80 °C after second NH3 saturation",
            "atmosphere": "sealed high-pressure flask",
            "ph": null,
            "other": "Cooled to room temperature, re-saturated with NH3, sealed again, heated for another 24 h."
          },
          "product": {
            "compound_id": "C29",
            "name": "15",
            "yield": "13 mg (58%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, EtOAc/MeOH 70:30",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Synthesis of Compound 16 (2-dechlorinated analogue)",
      "source_section": "main_text",
      "target_compound_id": "C31",
      "target_compound_name": "16",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Hydrogenolytic dechlorination",
          "reactants": [
            {
              "compound_id": "C16",
              "name": "11 (LCB-2122)",
              "amount": "23 mg (0.049 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C30",
              "name": "Palladium on carbon (10 wt %)",
              "amount": "23 mg (1.0 equiv by weight)",
              "role": "catalyst"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "0.5 mL (0.1 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "6 h",
            "atmosphere": "H2 (positive pressure, replacing N2)",
            "ph": null,
            "other": "N2 removed and replaced with H2; filtered over Celite with MeOH/EtOAc (50:50)."
          },
          "product": {
            "compound_id": "C31",
            "name": "16",
            "yield": "15.2 mg (72%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN 60:40",
          "notes": "Product obtained as white foam."
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Synthesis of Compound 17 (2-chlorohypoxanthine/inosine analogue)",
      "source_section": "main_text",
      "target_compound_id": "C35",
      "target_compound_name": "17",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Base hydrolysis (debenzoylation)",
          "reactants": [
            {
              "compound_id": "C05",
              "name": "S2",
              "amount": "500 mg (0.756 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C32",
              "name": "2N NaOH (aqueous)",
              "amount": "3.8 mL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "EtOH",
              "volume": "7.6 mL (1.0 M)"
            }
          ],
          "conditions": {
            "temperature": "50 °C (dissolution), then room temperature",
            "time": "5 h",
            "atmosphere": null,
            "ph": null,
            "other": "NaOH added dropwise; excess TFA added after reaction; concentrated, extracted with CH2Cl2."
          },
          "product": {
            "compound_id": "C33",
            "name": "S12",
            "yield": "176 mg (70%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeOH 80:20",
          "notes": "Product obtained as white foam."
        },
        {
          "step_number": 2,
          "reaction_type": "Acetonide (isopropylidene ketal) formation",
          "reactants": [
            {
              "compound_id": "C33",
              "name": "S12",
              "amount": "100 mg (0.302 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C09",
              "name": "CSA",
              "amount": "70 mg (0.302 mmol, 1.0 equiv)",
              "role": "acid"
            },
            {
              "compound_id": "C10",
              "name": "2,2-Dimethoxypropane",
              "amount": "0.67 mL (5.4 mmol, 18 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "dry acetone",
              "volume": "3 mL (0.1 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "16 h",
            "atmosphere": null,
            "ph": null,
            "other": "Molecular sieves 3 Å (180 mg) added; concentrated, dissolved in EtOAc, washed with 0.1 M HCl, extracted with EtOAc."
          },
          "product": {
            "compound_id": "C34",
            "name": "S13",
            "yield": "80 mg (71%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, CH2Cl2/MeOH 85:15",
          "notes": "Product obtained as white foam."
        },
        {
          "step_number": 3,
          "reaction_type": "O-Phosphorylation then one-pot acetonide deprotection",
          "reactants": [
            {
              "compound_id": "C34",
              "name": "S13",
              "amount": "22 mg (0.059 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl",
              "amount": "148 μL (0.148 mmol, 2.5 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C13",
              "name": "Diethylchlorophosphate",
              "amount": "22 μL (0.148 mmol, 2.5 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C15",
              "name": "TFA/H2O (8:2)",
              "amount": "3.0 mL (0.02 M)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "0.6 mL (0.1 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "4 h (phosphorylation) + 2 h (deprotection)",
            "atmosphere": "open (for TFA addition)",
            "ph": null,
            "other": "t-BuMgCl added, stirred 45 min; diethylchlorophosphate added, stirred 4 h; then TFA/H2O added dropwise at RT with open atmosphere; MeOH added, concentrated, coevaporated with MeOH (3×)."
          },
          "product": {
            "compound_id": "C35",
            "name": "17",
            "yield": "10 mg (36%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN 70:30",
          "notes": "Phosphorylation and acetonide deprotection performed in a single reaction vessel as sequential operations."
        }
      ]
    },
    {
      "pathway_id": "P8",
      "pathway_name": "Synthesis of Compound 18 (C2'-methoxymethyl analogue)",
      "source_section": "main_text",
      "target_compound_id": "C62",
      "target_compound_name": "18",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "TBS silylation of secondary alcohol",
          "reactants": [
            {
              "compound_id": "C36",
              "name": "S14 (previously reported secondary alcohol)",
              "amount": "140 mg (0.489 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C38",
              "name": "Imidazole",
              "amount": "83 mg (1.2 mmol, 2.5 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C37",
              "name": "TBSOTf",
              "amount": "0.17 mL (0.73 mmol, 1.5 equiv)",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "1.9 mL (0.50 M)"
            }
          ],
          "conditions": {
            "temperature": "0 °C then room temperature",
            "time": "21 h",
            "atmosphere": null,
            "ph": null,
            "other": "Solution cooled to 0 °C before TBSOTf addition; quenched with sat. NaHCO3; extracted with Et2O, washed with brine, dried over MgSO4."
          },
          "product": {
            "compound_id": "C39",
            "name": "S15",
            "yield": "188 mg (96%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, Hexanes/EtOAc 70:30",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Partial reduction of lactone to lactol (DIBAL-H)",
          "reactants": [
            {
              "compound_id": "C39",
              "name": "S15",
              "amount": "329 mg (0.821 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C40",
              "name": "DIBAL-H (1 M in Hexanes)",
              "amount": "1.2 mL (1.2 mmol, 1.5 equiv)",
              "role": "reductant"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "4.5 mL (0.18 M)"
            }
          ],
          "conditions": {
            "temperature": "−78 °C",
            "time": "3.5 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with sat. aq. potassium sodium tartrate at −78 °C; warmed to RT and stirred 1 h; extracted with Et2O, washed with brine, dried over MgSO4."
          },
          "product": {
            "compound_id": "C41",
            "name": "S16a,b (2:1 mixture)",
            "yield": "232 mg (70%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography, Hexanes/EtOAc 80:20",
          "notes": "Product is a 2:1 mixture of anomeric lactols."
        },
        {
          "step_number": 3,
          "reaction_type": "Benzoylation of anomeric hydroxyl",
          "reactants": [
            {
              "compound_id": "C41",
              "name": "S16a,b (2:1 mixture)",
              "amount": "232 mg (0.576 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C43",
              "name": "DMAP",
              "amount": "7 mg (0.06 mmol, 0.1 equiv)",
              "role": "catalyst"
            },
            {
              "compound_id": "C44",
              "name": "Pyridine",
              "amount": "0.28 mL (3.5 mmol, 6.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C42",
              "name": "BzCl",
              "amount": "0.10 mL (0.86 mmol, 1.5 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C45",
              "name": "Ethylenediamine",
              "amount": "0.09 mL (1.4 mmol, 2.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "3.1 mL (0.18 M)"
            }
          ],
          "conditions": {
            "temperature": "0 °C then room temperature",
            "time": "16 h then 30 min (quench with ethylenediamine at 0 °C)",
            "atmosphere": null,
            "ph": null,
            "other": "BzCl added slowly at 0 °C; quenched with ethylenediamine at 0 °C."
          },
          "product": {
            "compound_id": "C46",
            "name": "S17a,b (2:1 mixture)",
            "yield": "266 mg (91%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, Hexanes/EtOAc 70:30",
          "notes": "Product is a 2:1 diastereomeric mixture."
        },
        {
          "step_number": 4,
          "reaction_type": "Ozonolysis of vinyl group followed by NaBH4 reduction",
          "reactants": [
            {
              "compound_id": "C46",
              "name": "S17a,b (2:1 mixture)",
              "amount": "4.07 g (8.02 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C47",
              "name": "O3 (ozone)",
              "amount": "bubbled until solution turned blue (~2 h)",
              "role": "oxidant"
            },
            {
              "compound_id": "C48",
              "name": "NEt3",
              "amount": "1.2 mL (8.0 mmol, 1.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C49",
              "name": "NaBH4",
              "amount": "0.46 g (12 mmol, 1.5 equiv)",
              "role": "reductant"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "0.4 L (0.02 M)"
            },
            {
              "name": "MeOH (for NaBH4 step)",
              "volume": "84 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "−78 °C (ozonolysis); 0 °C (NaBH4 reduction)",
            "time": "2 h (O3) + 1 h (warm-up after NEt3) + 5 h (NaBH4)",
            "atmosphere": "purged with N2 after ozonolysis",
            "ph": null,
            "other": "After ozonolysis purge with N2, NEt3 added, stirred 1 h warming to RT; crude redissolved in MeOH, NaBH4 added at 0 °C, quenched with H2O at 0 °C, warmed to RT."
          },
          "product": {
            "compound_id": "C50",
            "name": "S18a,b (5:1 mixture)",
            "yield": "3.12 g (76%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, Hexanes/EtOAc 80:20",
          "notes": "Two-step procedure (ozonolysis then in-situ reduction) performed sequentially."
        },
        {
          "step_number": 5,
          "reaction_type": "O-Methylation (methoxymethyl introduction via MeOTf)",
          "reactants": [
            {
              "compound_id": "C50",
              "name": "S18a,b (5:1 mixture)",
              "amount": "425 mg (0.832 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C52",
              "name": "2,6-di-tert-butyl-4-methylpyridine",
              "amount": "683 mg (3.33 mmol, 4.00 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C51",
              "name": "MeOTf",
              "amount": "0.66 mL (5.8 mmol, 7.0 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "8.5 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "40 °C",
            "time": "18 h",
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to RT; quenched with water; extracted with CH2Cl2, dried over MgSO4."
          },
          "product": {
            "compound_id": "C53",
            "name": "S19a,b (4:1 mixture)",
            "yield": "373 mg (85%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, Hexanes/EtOAc 80:20",
          "notes": "Product is a 4:1 diastereomeric mixture."
        },
        {
          "step_number": 6,
          "reaction_type": "Vorbrüggen-type N-glycosylation with 2-chloroadenine",
          "reactants": [
            {
              "compound_id": "C53",
              "name": "S19a,b (4:1 mixture)",
              "amount": "231 mg (0.440 mmol)"
            },
            {
              "compound_id": "C54",
              "name": "2-Chloroadenine",
              "amount": "149 mg (0.880 mmol, 2.00 equiv)",
              "role": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C55",
              "name": "BSA",
              "amount": "0.70 mL (2.9 mmol, 6.5 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C04",
              "name": "TMSOTf",
              "amount": "0.16 mL (0.88 mmol, 2.0 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "anhydrous DCE (1,2-dichloroethane)",
              "volume": "1.8 mL (0.50 M) for BSA step + 0.88 mL (0.50 M) for sugar"
            }
          ],
          "conditions": {
            "temperature": "84 °C",
            "time": "3 h",
            "atmosphere": null,
            "ph": null,
            "other": "BSA added to suspension of 2-chloroadenine, warmed to 84 °C until clear; cooled, added to S19a,b solution, TMSOTf added dropwise; quenched with EtOAc and sat. NaHCO3."
          },
          "product": {
            "compound_id": "C56",
            "name": "S20a,b (1.2:1 β/α mixture)",
            "yield": "222 mg (88%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, CH2Cl2/MeOH 70:30",
          "notes": "1H NMR of crude showed ~1.2:1 dr."
        },
        {
          "step_number": 7,
          "reaction_type": "Selective partial TBS deprotection (anomeric separation)",
          "reactants": [
            {
              "compound_id": "C56",
              "name": "S20a,b (1.2:1 α/β mixture)",
              "amount": "295 mg (0.515 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C57",
              "name": "TFA/H2O (1:1)",
              "amount": "2.86 mL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "5.7 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "0 °C",
            "time": "4 h",
            "atmosphere": null,
            "ph": null,
            "other": "Sat. NaHCO3 added; warmed to RT; extracted with Et2O, dried over MgSO4."
          },
          "product": {
            "compound_id": "C59",
            "name": "S21b (β-anomer)",
            "yield": "89 mg (38%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, EtOAc/MeOH 90:10",
          "notes": "Reaction also produces S21a (α-anomer, 64 mg, 27%); only S21b (β) is used for subsequent phosphorylation."
        },
        {
          "step_number": 8,
          "reaction_type": "O-Phosphorylation (diethyl phosphate installation on S21b)",
          "reactants": [
            {
              "compound_id": "C59",
              "name": "S21b",
              "amount": "84 mg (0.18 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl (1 M in THF)",
              "amount": "0.46 mL (0.46 mmol, 2.5 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C13",
              "name": "Diethylchlorophosphate",
              "amount": "40 μL (0.28 mmol, 1.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "1.1 mL (0.17 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "16 h (after phosphate addition); 30 min (Grignard pre-stirring)",
            "atmosphere": null,
            "ph": null,
            "other": "t-BuMgCl added dropwise; quenched with MeOH."
          },
          "product": {
            "compound_id": "C60",
            "name": "S22",
            "yield": "47 mg (43%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, Hexanes/EtOAc 0:100",
          "notes": null
        },
        {
          "step_number": 9,
          "reaction_type": "TBS deprotection (fluoride-mediated)",
          "reactants": [
            {
              "compound_id": "C60",
              "name": "S22",
              "amount": "45 mg (0.076 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C61",
              "name": "TBAF (1.0 M in THF)",
              "amount": "1.5 mL (0.15 mmol, 2.0 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "0.76 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "0 °C then room temperature",
            "time": "16 h",
            "atmosphere": null,
            "ph": null,
            "other": "TBAF added dropwise at 0 °C; quenched with MeOH."
          },
          "product": {
            "compound_id": "C62",
            "name": "18",
            "yield": "31 mg (85%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, EtOAc/MeOH 50:50",
          "notes": "Product obtained as white foam."
        }
      ]
    },
    {
      "pathway_id": "P9",
      "pathway_name": "Synthesis of Compound 19 (3'-benzyl C3'-OH analogue)",
      "source_section": "main_text",
      "target_compound_id": "C73",
      "target_compound_name": "19",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NaBH4 reduction of aldehyde then O-benzylation and Vorbrüggen glycosylation (3 steps)",
          "reactants": [
            {
              "compound_id": "C63",
              "name": "S23a,b (previously reported aldehydes)",
              "amount": "12.0 g (24.6 mmol)"
            },
            {
              "compound_id": "C02",
              "name": "2,6-Dichloropurine",
              "amount": "907 mg (4.79 mmol, 1.10 equiv) [for glycosylation step on 4.36 mmol crude]",
              "role": null
            }
          ],
          "reagents": [
            {
              "compound_id": "C49",
              "name": "NaBH4",
              "amount": "1.02 g (0.22 mmol, 1.1 equiv) [relative to crude 24.6 mmol aldehyde]",
              "role": "reductant"
            },
            {
              "compound_id": "C64",
              "name": "Benzyl 2,2,2-trichloroacetimidate",
              "amount": "2.4 mL (13 mmol, 3.0 equiv) [relative to 4.36 mmol crude alcohol]",
              "role": "other"
            },
            {
              "compound_id": "C65",
              "name": "TfOH",
              "amount": "50 μL (0.44 mmol, 0.10 equiv)",
              "role": "acid"
            },
            {
              "compound_id": "C17",
              "name": "Et3N (quench)",
              "amount": "92 μL (0.65 mmol, 0.15 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C03",
              "name": "DBU",
              "amount": "2.0 mL (13 mmol, 3.0 equiv) [for glycosylation step]",
              "role": "base"
            },
            {
              "compound_id": "C04",
              "name": "TMSOTf",
              "amount": "3.21 mL (17.4 mmol, 4.00 equiv) [for glycosylation step]",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "MeOH (NaBH4 step)",
              "volume": "0.16 L (0.15 M)"
            },
            {
              "name": "DCM/Cyclohexane 1:2 (benzylation step)",
              "volume": "44 mL (0.10 M)"
            },
            {
              "name": "MeCN (glycosylation step)",
              "volume": "22 mL (0.20 M)"
            }
          ],
          "conditions": {
            "temperature": "0 °C (NaBH4); room temperature (benzylation, 16 h); −10 °C (glycosylation, 5 h)",
            "time": "3 h (NaBH4) + 16 h (benzylation) + 5 h (glycosylation)",
            "atmosphere": null,
            "ph": null,
            "other": "NaBH4 step at 0 °C, 3 h; crude alcohol filtered over silica (Et2O); benzylation quenched with NEt3; glycosylation quenched with sat. NaHCO3/DCM workup, washed with 0.1 M citric acid."
          },
          "product": {
            "compound_id": "C66",
            "name": "S24 (β-anomer)",
            "yield": "1.58 g (56% over 3 steps)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, Hexanes/EtOAc 70:30",
          "notes": "Three-step telescoped sequence: reduction, O-benzylation, glycosylation. 1H NMR of crude glycosylation showed ~10:1 dr (β-anomer favored)."
        },
        {
          "step_number": 2,
          "reaction_type": "Ammonolysis (debenzoylation and purine C6 aminolysis)",
          "reactants": [
            {
              "compound_id": "C66",
              "name": "S24",
              "amount": "371 mg (0.573 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C06",
              "name": "NH3(g)",
              "amount": "excess (bubbled until saturation, twice)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "12 mL (0.048 M)"
            }
          ],
          "conditions": {
            "temperature": "80 °C",
            "time": "24 h then additional 16 h at 80 °C after second NH3 saturation",
            "atmosphere": "sealed high-pressure flask",
            "ph": null,
            "other": "NH3 bubbled twice until saturation; diluted with MeOH (10 mL) after completion."
          },
          "product": {
            "compound_id": "C67",
            "name": "S25",
            "yield": "178 mg (74%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, CH2Cl2/MeOH 90:10",
          "notes": "Product obtained as white foam."
        },
        {
          "step_number": 3,
          "reaction_type": "Bis-TBS silylation of diol",
          "reactants": [
            {
              "compound_id": "C67",
              "name": "S25",
              "amount": "317 mg (0.756 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C68",
              "name": "2,6-Lutidine",
              "amount": "0.44 mL (3.8 mmol, 5.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C37",
              "name": "TBSOTf",
              "amount": "0.52 mL (2.3 mmol, 3.0 equiv)",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DCM",
              "volume": "7.6 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "0 °C then room temperature",
            "time": "16 h",
            "atmosphere": null,
            "ph": null,
            "other": "1 drop DMF added; reaction quenched with sat. NaHCO3; diluted with Et2O, washed with brine and 0.1 N HCl."
          },
          "product": {
            "compound_id": "C69",
            "name": "S26",
            "yield": "321 mg (65%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, Hexanes/EtOAc 60:40",
          "notes": "Product obtained as white foam."
        },
        {
          "step_number": 4,
          "reaction_type": "Selective mono-TBS deprotection",
          "reactants": [
            {
              "compound_id": "C69",
              "name": "S26",
              "amount": "358 mg (0.552 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C70",
              "name": "TFA/H2O (1:1)",
              "amount": "3.1 mL (0.18 M)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "6.1 mL (0.090 M)"
            }
          ],
          "conditions": {
            "temperature": "0 °C",
            "time": "4 h",
            "atmosphere": null,
            "ph": null,
            "other": "Sat. NaHCO3 added; aqueous phase extracted with Et2O (2×); washed with brine, dried over MgSO4."
          },
          "product": {
            "compound_id": "C71",
            "name": "S27",
            "yield": "207 mg (70%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Flash chromatography on silica gel, CH2Cl2/MeOH 95:5",
          "notes": "Product obtained as white foam."
        },
        {
          "step_number": 5,
          "reaction_type": "O-Phosphorylation (diethyl phosphate installation)",
          "reactants": [
            {
              "compound_id": "C71",
              "name": "S27",
              "amount": "200 mg (0.374 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl",
              "amount": "0.56 mL (0.56 mmol, 1.5 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C13",
              "name": "Diethylchlorophosphate",
              "amount": "81 μL (0.56 mmol, 1.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "4 mL (0.1 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "16 h (after phosphate addition); 45 min (Grignard pre-stirring)",
            "atmosphere": null,
            "ph": null,
            "other": "MeOH added; concentrated."
          },
          "product": {
            "compound_id": "C72",
            "name": "S28",
            "yield": "216 mg (86%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN gradient",
          "notes": "Product obtained as white foam."
        },
        {
          "step_number": 6,
          "reaction_type": "TBS deprotection (acid-mediated)",
          "reactants": [
            {
              "compound_id": "C72",
              "name": "S28",
              "amount": "29.3 mg (0.0437 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C15",
              "name": "TFA/H2O (8:2)",
              "amount": "0.5 mL (0.1 M)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "0.5 mL (0.1 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "4 h",
            "atmosphere": null,
            "ph": null,
            "other": "MeOH added; concentrated; coevaporated with MeOH (3×)."
          },
          "product": {
            "compound_id": "C73",
            "name": "19",
            "yield": "10.9 mg (45%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "Reversed-phase (C18) flash chromatography, H2O/MeCN 50:50",
          "notes": "Product obtained as white foam."
        }
      ]
    }
  ]
}
```
##### Attempt 3
```
{
  "extraction": {
    "prompt_version": "v3.2",
    "extraction_date": "2026-04-05",
    "model_name": "claude-sonnet-4-6",
    "extractor_notes": "SI found: jm5c01999_si_001.pdf. SI schemes identified: none — the SI document contains only supplementary biological figures (S1–S8), stereochemical proofs, X-ray crystallographic data for S3, and NMR/HPLC spectra pages (S18–S120+). There are no SI synthesis schemes (no Scheme S1, S2, etc.) and no new experimental procedures in the SI beyond the main text. All synthesis procedures are contained in the main text Experimental Section. Total pathway count: 9 pathways (P1–P9), all from main text. SI compounds identified as author labels in main text: S1 (previously reported, ref 31), S2, S3, S4, S5, S6, S7, S8, S9, S10 (previously reported, ref 45), S11, S12, S13, S14 (previously reported, ref 31), S15, S16a/b, S17a/b, S18a/b, S19a/b, S20a/b, S21a, S21b, S22, S23a/b (previously reported, ref 31), S24, S25, S26, S27, S28; final compounds 11–19. Excluded reference compounds (no synthetic role in this study): AMP (adenosine monophosphate, cited for comparison), MK-8722, AICA riboside, resveratrol, quercetin, berberine, metformin, dexrazoxane, doxorubicin/Dox (used as biological stressor only, not synthesized), imatinib mesylate (used as biological stressor only). Mass type notes: all MS data reported as HRMS ESI exact mass (monoisotopic) unless otherwise noted. S1 is described as benzoylated sugars from ref 31 (Becerril-Jimenez 2019 J. Org. Chem.); S10 is previously reported from ref 45 (Eymard 2024 Molecules); S14 is previously reported from ref 31; S23a,b are previously reported from ref 31. These four receive IDs but role = starting_material and is_newly_synthesized = false."
  },

  "paper": {
    "title": "A Nucleoside Analogue Bearing a C2′-Stereogenic All-Carbon Quaternary Center for the Treatment of Heart Failure",
    "authors": [
      "Abir Almazloum",
      "Wael Maharsy",
      "Starr Dostie",
      "Fabiola Becerril-Jiménez",
      "Carla Eymard",
      "Hiba Komati",
      "Louis Leblanc",
      "Amarender Manchoju",
      "Philippe Mochirian",
      "Renaud Zelli",
      "Michel Prevost",
      "Mona Nemer",
      "Yvan Guindon"
    ],
    "doi": "10.1021/acs.jmedchem.5c01999",
    "journal": "Journal of Medicinal Chemistry",
    "year": 2025,
    "synthesis_scale": "lab",
    "method_completeness": "full",
    "has_synthesis": true,
    "extraction_notes": "Full experimental procedures provided in main text for all 9 target compounds (11–19) and all intermediates S2–S9, S11–S13, S15–S22, S24–S28. Four starting materials (S1, S10, S14, S23a/b) referenced as previously reported from other publications. All compounds >95% pure by HPLC. SI contains spectra and biological figures only; no additional synthesis schemes."
  },

  "compounds": [
    {
      "id": "C01",
      "name": "S1 (benzoylated sugars, 3,4-anti lactone precursors)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "previously reported (Becerril-Jiménez et al. J. Org. Chem. 2019, ref 31)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Previously reported benzoylated sugar lactone precursors (3,4-anti) used as glycosyl donor for N-glycosidic bond formation to give nucleoside S2."
    },
    {
      "id": "C02",
      "name": "2,6-Dichloropurine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Commercial purine base used as nucleobase coupling partner in N-glycosidic bond formation steps."
    },
    {
      "id": "C03",
      "name": "DBU (1,8-diazabicyclo[5.4.0]undec-7-ene)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Non-nucleophilic base used to promote N-glycosidic coupling reactions."
    },
    {
      "id": "C04",
      "name": "TMSOTf (trimethylsilyl trifluoromethanesulfonate)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Lewis acid activator used to activate sugar anomeric position for N-glycosidic coupling."
    },
    {
      "id": "C05",
      "name": "S2 ((−)-((2R,3R,4S,5R)-3-(Benzoyloxy)-5-(2,6-dichloro-9H-purin-9-yl)-4-methyltetrahydrofuran-2,4-diyl)bis(methylene)dibenzoate)",
      "iupac_name": "(−)-((2R,3R,4S,5R)-3-(Benzoyloxy)-5-(2,6-dichloro-9H-purin-9-yl)-4-methyltetrahydrofuran-2,4-diyl)bis(methylene)dibenzoate",
      "molecular_formula": "C33H26Cl2N4O7",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 683.1066",
      "ms_calculated_exact_mass": null,
      "description": "Tribenzoylated N-glycoside bearing 2,6-dichloropurine base with C2′ quaternary center; key intermediate used in multiple subsequent transformations."
    },
    {
      "id": "C06",
      "name": "NH3 (ammonia gas)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Ammonia gas used to displace benzoyl protecting groups and convert 6-chloro to 6-amino purine substituent under high-pressure conditions."
    },
    {
      "id": "C07",
      "name": "S3 ((+)-((2R,3S,4R,5R)-5-(2-Chloro-6-methoxy-9H-purin-9-yl)-3-hydroxy-4-methyltetrahydrofuran-2,4-diyl)dimethanol)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(2-Chloro-6-methoxy-9H-purin-9-yl)-3-hydroxy-4-methyltetrahydrofuran-2,4-diyl)dimethanol",
      "molecular_formula": "C13H17ClN4O5",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 367.0781",
      "ms_calculated_exact_mass": null,
      "description": "Methanolysis byproduct of S2 aminolysis bearing 2-chloro-6-methoxypurine base and free diol; isolated alongside S4, confirmed by X-ray."
    },
    {
      "id": "C08",
      "name": "S4 ((−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-methyltetrahydrofuran-2,4-diyl)dimethanol)",
      "iupac_name": "(−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-methyltetrahydrofuran-2,4-diyl)dimethanol",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "2-Chloroadenosine-like nucleoside triol with C2′ quaternary center; key central intermediate previously reported (ref 32) and used for acetonide protection toward S5."
    },
    {
      "id": "C09",
      "name": "CSA (camphorsulfonic acid)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acid catalyst used to promote acetonide formation on diol nucleosides."
    },
    {
      "id": "C10",
      "name": "2,2-Dimethoxypropane",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acetonide-forming reagent used to protect vicinal diol groups."
    },
    {
      "id": "C11",
      "name": "S5 ((+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methanol)",
      "iupac_name": "(+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methanol",
      "molecular_formula": "C15H20ClN5O4",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 392.1104",
      "ms_calculated_exact_mass": null,
      "description": "Acetonide-protected nucleoside with free primary alcohol at C5′; central branch-point intermediate for phosphorylation to give compounds 11, 12, 13, 14."
    },
    {
      "id": "C12",
      "name": "t-BuMgCl (tert-butylmagnesium chloride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Hindered Grignard base used to deprotonate primary alcohol prior to phosphorylation with chlorophosphate reagents."
    },
    {
      "id": "C13",
      "name": "Diethylchlorophosphate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Phosphorylating agent used to install diethyl phosphate at C5′ position."
    },
    {
      "id": "C14",
      "name": "S6 ((+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Diethyl Phosphate)",
      "iupac_name": "(+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C19H29ClN5O7P",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 528.1386",
      "ms_calculated_exact_mass": null,
      "description": "Acetonide-protected diethyl phosphate nucleoside; direct precursor to lead compound LCB-2122 (11) after acetonide removal."
    },
    {
      "id": "C15",
      "name": "TFA/H2O (trifluoroacetic acid/water mixture)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acidic deprotection mixture (8:2 TFA:H2O) used to remove acetonide protecting groups from multiple intermediates."
    },
    {
      "id": "C16",
      "name": "11 (LCB-2122) ((+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C16H25ClN5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 488.1072",
      "ms_calculated_exact_mass": null,
      "description": "Lead cardioprotective compound LCB-2122; 2-chloroadenosine monophosphate diethyl ester analogue with C2′ all-carbon quaternary center and north conformational bias."
    },
    {
      "id": "C17",
      "name": "Et3N (triethylamine)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base used in phosphorylation reactions and pH adjustment steps."
    },
    {
      "id": "C18",
      "name": "POCl3 (phosphorus oxychloride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Phosphorylating agent used to install hydrogen phosphate monoester at C5′ for compound S7."
    },
    {
      "id": "C19",
      "name": "S7 (Triethylammonium (+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Hydrogen Phosphate)",
      "iupac_name": "Triethylammonium (+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Hydrogen Phosphate",
      "molecular_formula": "C21H36ClN6O7P",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+H]+ 551.2138",
      "ms_calculated_exact_mass": null,
      "description": "Acetonide-protected monohydrogen phosphate triethylammonium salt; precursor to free phosphate compound 12."
    },
    {
      "id": "C20",
      "name": "12 ((+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Dihydrogen Phosphate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Dihydrogen Phosphate",
      "molecular_formula": "C12H17ClN5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M−H]− 408.0482",
      "ms_calculated_exact_mass": null,
      "description": "Free phosphate analogue of LCB-2122 (compound 12); inactive in cardioprotective assay due to poor cellular uptake."
    },
    {
      "id": "C21",
      "name": "Dimethylchlorophosphate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Phosphorylating agent used to install dimethyl phosphate ester at C5′ for compound S8/13."
    },
    {
      "id": "C22",
      "name": "S8 ((+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Dimethyl Phosphate)",
      "iupac_name": "(+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Dimethyl Phosphate",
      "molecular_formula": "C17H25ClN5O7P",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 500.1061",
      "ms_calculated_exact_mass": null,
      "description": "Acetonide-protected dimethyl phosphate nucleoside; precursor to compound 13 after acetonide deprotection."
    },
    {
      "id": "C23",
      "name": "13 ((+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Dimethyl Phosphate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Dimethyl Phosphate",
      "molecular_formula": "C14H21ClN5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 460.0765",
      "ms_calculated_exact_mass": null,
      "description": "Dimethyl phosphate analogue of LCB-2122 (compound 13); inactive in cardioprotective assay."
    },
    {
      "id": "C24",
      "name": "Diisopropyl chlorophosphate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Phosphorylating agent used to install diisopropyl phosphate ester at C5′ for compound S9/14."
    },
    {
      "id": "C25",
      "name": "S9 ((+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Diisopropyl Phosphate)",
      "iupac_name": "(+)-((4aR,5R,7R,7aS)-5-(6-Amino-2-chloro-9H-purin-9-yl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-7-yl)methyl Diisopropyl Phosphate",
      "molecular_formula": "C21H33ClN5O7P",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+H]+ 534.1868",
      "ms_calculated_exact_mass": null,
      "description": "Acetonide-protected diisopropyl phosphate nucleoside; precursor to compound 14 after acetonide deprotection."
    },
    {
      "id": "C26",
      "name": "14 ((+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diisopropyl Phosphate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diisopropyl Phosphate",
      "molecular_formula": "C18H29ClN5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 516.1398",
      "ms_calculated_exact_mass": null,
      "description": "Diisopropyl phosphate analogue of LCB-2122 (compound 14); retains cardioprotective activity, indicating LCB-2122 is not a prodrug."
    },
    {
      "id": "C27",
      "name": "S10 (previously reported 4′-thio primary alcohol precursor)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "previously reported (Eymard et al. Molecules 2024, ref 45)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Previously reported primary alcohol 4′-thio nucleoside bearing 2,6-dichloropurine and benzoyl protecting groups; starting material for synthesis of compound 15."
    },
    {
      "id": "C28",
      "name": "S11 ((−)-((2R,3R,4S,5R)-4-(Benzoyloxy)-2-(2,6-dichloro-9H-purin-9-yl)-5-(((diethoxyphosphoryl)oxy)methyl)-3-methyltetrahydrothiophen-3-yl)methyl Benzoate)",
      "iupac_name": "(−)-((2R,3R,4S,5R)-4-(Benzoyloxy)-2-(2,6-dichloro-9H-purin-9-yl)-5-(((diethoxyphosphoryl)oxy)methyl)-3-methyltetrahydrothiophen-3-yl)methyl Benzoate",
      "molecular_formula": "C30H31Cl2N4O8PS",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+H]+ 709.1048",
      "ms_calculated_exact_mass": null,
      "description": "4′-Thio protected diethyl phosphate nucleoside bearing 2,6-dichloropurine and benzoyl groups; precursor to 4′-thio final compound 15 after ammonolysis."
    },
    {
      "id": "C29",
      "name": "15 ((+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrothiophen-2-yl)methyl Diethyl Phosphate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrothiophen-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C16H25ClN5O6PS",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 504.0841",
      "ms_calculated_exact_mass": null,
      "description": "4′-Thio analogue of LCB-2122 (compound 15); showed lower cardioprotective activity than the oxygen-containing lead compound."
    },
    {
      "id": "C30",
      "name": "Palladium on carbon (Pd/C, 10 wt%)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "catalyst",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Heterogeneous hydrogenation catalyst used for reductive dechlorination of 2-chloro group in synthesis of compound 16."
    },
    {
      "id": "C31",
      "name": "16 ((−)-((2R,3S,4R,5R)-5-(6-Amino-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate)",
      "iupac_name": "(−)-((2R,3S,4R,5R)-5-(6-Amino-9H-purin-9-yl)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C16H26N5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+H]+ 432.1642",
      "ms_calculated_exact_mass": null,
      "description": "Des-2-chloro analogue of LCB-2122 (compound 16); loss of C2-Cl abolished cardioprotective activity."
    },
    {
      "id": "C32",
      "name": "S12 ((+)-2-Chloro-9-((2R,3R,4S,5R)-4-hydroxy-3,5-bis(hydroxymethyl)-3-methyltetrahydrofuran-2-yl)-1,9-dihydro-6H-purin-6-one)",
      "iupac_name": "(+)-2-Chloro-9-((2R,3R,4S,5R)-4-hydroxy-3,5-bis(hydroxymethyl)-3-methyltetrahydrofuran-2-yl)-1,9-dihydro-6H-purin-6-one",
      "molecular_formula": "C12H15ClN4O5",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 353.0618",
      "ms_calculated_exact_mass": null,
      "description": "Hypoxanthine-type triol nucleoside (inosine analogue); obtained by NaOH saponification of benzoyl groups from S2, precursor to S13."
    },
    {
      "id": "C33",
      "name": "NaOH (2 N sodium hydroxide)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base used for saponification of benzoyl groups and simultaneous ammonolysis of 6-chloro group from S2 to give S12."
    },
    {
      "id": "C34",
      "name": "S13 ((+)-2-Chloro-9-((4aR,5R,7R,7aS)-7-(hydroxymethyl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-5-yl)-1,9-dihydro-6H-purin-6-one)",
      "iupac_name": "(+)-2-Chloro-9-((4aR,5R,7R,7aS)-7-(hydroxymethyl)-2,2,4a-trimethyltetrahydro-4H-furo[3,4-d][1,3]dioxin-5-yl)-1,9-dihydro-6H-purin-6-one",
      "molecular_formula": "C15H19ClN4O5",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 393.0944",
      "ms_calculated_exact_mass": null,
      "description": "Acetonide-protected inosine analogue with free primary alcohol; precursor to compound 17 via one-pot phosphorylation/deprotection."
    },
    {
      "id": "C35",
      "name": "17 ((+)-((2R,3S,4R,5R)-5-(2-Chloro-9H-purin-9-yl-6-one)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(2-Chloro-9H-purin-9-yl-6-one)-3-hydroxy-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C16H24ClN4O8P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M−H]− 465.0949",
      "ms_calculated_exact_mass": null,
      "description": "Inosine-based analogue of LCB-2122 with 2-chlorohypoxanthine base (compound 17); inactive, potential deaminated metabolite analogue."
    },
    {
      "id": "C36",
      "name": "S14 (previously reported secondary alcohol lactone)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "previously reported (Becerril-Jiménez et al. J. Org. Chem. 2019, ref 31)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Previously reported secondary alcohol furanone precursor used as starting material for compound 18 synthesis via silyl protection."
    },
    {
      "id": "C37",
      "name": "TBSOTf (tert-butyldimethylsilyl trifluoromethanesulfonate)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Silylating agent used to install TBS protecting groups on hydroxyl functions."
    },
    {
      "id": "C38",
      "name": "Imidazole",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base used to activate TBSOTf and promote silylation of alcohols."
    },
    {
      "id": "C39",
      "name": "S15 ((+)-(3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-methyl-3-vinyldihydrofuran-2(3H)-one)",
      "iupac_name": "(+)-(3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-methyl-3-vinyldihydrofuran-2(3H)-one",
      "molecular_formula": "C20H40O4Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 423.2356",
      "ms_calculated_exact_mass": null,
      "description": "Bis-TBS-protected vinyl lactone; prepared from S14 by silyl protection and used for DIBAL-H reduction to lactols S16a,b."
    },
    {
      "id": "C40",
      "name": "DIBAL-H (diisobutylaluminium hydride, 1M in hexanes)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Reducing agent used to partially reduce lactone S15 to lactol S16a,b at −78 °C."
    },
    {
      "id": "C41",
      "name": "S16a,b ((3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-methyl-3-vinyltetrahydrofuran-2-ol, 2:1 mixture of anomers)",
      "iupac_name": null,
      "molecular_formula": "C20H42O4Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 425.2514",
      "ms_calculated_exact_mass": null,
      "description": "Bis-TBS-protected lactols (2:1 diastereomeric mixture) obtained from DIBAL-H reduction of S15; used for benzoylation to give S17a,b."
    },
    {
      "id": "C42",
      "name": "BzCl (benzoyl chloride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acylating agent used to install benzoate ester at anomeric position of lactols S16a,b."
    },
    {
      "id": "C43",
      "name": "DMAP (4-dimethylaminopyridine)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acylation catalyst used in benzoylation of lactols S16a,b."
    },
    {
      "id": "C44",
      "name": "Pyridine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base/solvent used in benzoylation reactions."
    },
    {
      "id": "C45",
      "name": "Ethylenediamine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Quenching reagent added after benzoylation to destroy excess BzCl."
    },
    {
      "id": "C46",
      "name": "S17a,b ((3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-methyl-3-vinyltetrahydrofuran-2-yl Benzoate, 2:1 mixture)",
      "iupac_name": null,
      "molecular_formula": "C27H46O5Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 529.2777",
      "ms_calculated_exact_mass": null,
      "description": "Anomeric benzoate sugar donors (2:1 diastereomeric mixture) with pendant vinyl group; used for ozonolysis/reduction sequence to give S18a,b."
    },
    {
      "id": "C47",
      "name": "Ozone (O3)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Oxidant for ozonolysis of vinyl group in S17a,b to give an aldehyde intermediate."
    },
    {
      "id": "C48",
      "name": "NaBH4 (sodium borohydride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Reductant used to reduce aldehyde from ozonolysis to primary alcohol in S18a,b."
    },
    {
      "id": "C49",
      "name": "S18a,b ((3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-(hydroxymethyl)-3-methyltetrahydrofuran-2-yl Benzoate, 5:1 mixture)",
      "iupac_name": null,
      "molecular_formula": "C26H46O6Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 533.2729",
      "ms_calculated_exact_mass": null,
      "description": "Primary hydroxymethyl sugars (5:1 diastereomeric mixture) obtained after ozonolysis/reduction of S17a,b; methylated to give S19a,b."
    },
    {
      "id": "C50",
      "name": "2,6-Di-tert-butyl-4-methylpyridine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Hindered base used to facilitate O-methylation with MeOTf without N-alkylation."
    },
    {
      "id": "C51",
      "name": "MeOTf (methyl trifluoromethanesulfonate)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "O-methylating agent used to convert primary alcohol of S18a,b to methoxymethyl group in S19a,b."
    },
    {
      "id": "C52",
      "name": "S19a,b ((3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-(methoxymethyl)-3-methyltetrahydrofuran-2-yl Benzoate, 4:1 mixture)",
      "iupac_name": null,
      "molecular_formula": "C27H48O6Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 547.2889",
      "ms_calculated_exact_mass": null,
      "description": "Methoxymethyl-substituted anomeric benzoate sugar donors (4:1 diastereomeric mixture); used as glycosyl donors for N-glycosidic coupling with 2-chloroadenine."
    },
    {
      "id": "C53",
      "name": "2-Chloroadenine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Nucleobase used for N-glycosidic coupling with silylated sugar S19a,b to give nucleosides S20a,b."
    },
    {
      "id": "C54",
      "name": "BSA (N,O-bis(trimethylsilyl)acetamide)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Silylating agent used to generate in situ per-TMS-2-chloroadenine for improved solubility and reactivity in N-glycosidic coupling."
    },
    {
      "id": "C55",
      "name": "S20a,b (9-((3R,4S,5R)-4-((tert-Butyldimethylsilyl)oxy)-5-(((tert-butyldimethylsilyl)oxy)methyl)-3-(methoxymethyl)-3-methyltetrahydrofuran-2-yl)-2-chloro-9H-purin-6-amine, 1.2:1 mixture)",
      "iupac_name": null,
      "molecular_formula": "C25H46ClN5O4Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+H]+ 572.2852",
      "ms_calculated_exact_mass": null,
      "description": "Bis-TBS-protected nucleosides (1.2:1 α/β mixture) from N-glycosidic coupling; partial deprotection gives S21a and S21b."
    },
    {
      "id": "C56",
      "name": "TFA/H2O (1:1, trifluoroacetic acid/water for TBS removal)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Dilute acidic mixture used for selective removal of one TBS group from S20a,b."
    },
    {
      "id": "C57",
      "name": "S21a ((+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-((tert-butyldimethylsilyl)oxy)-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methanol)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-((tert-butyldimethylsilyl)oxy)-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methanol",
      "molecular_formula": "C19H32ClN5O4Si",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+H]+ 458.1982",
      "ms_calculated_exact_mass": null,
      "description": "α-anomer mono-TBS nucleoside with free primary alcohol; byproduct from S20a,b deprotection, not used further for compound 18."
    },
    {
      "id": "C58",
      "name": "S21b ((−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-((tert-butyldimethylsilyl)oxy)-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methanol)",
      "iupac_name": "(−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-((tert-butyldimethylsilyl)oxy)-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methanol",
      "molecular_formula": "C19H32ClN5O4Si",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+H]+ 458.1984",
      "ms_calculated_exact_mass": null,
      "description": "β-anomer mono-TBS nucleoside with free primary alcohol; used for phosphorylation to give S22."
    },
    {
      "id": "C59",
      "name": "S22 ((+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-((tert-butyldimethylsilyl)oxy)-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-((tert-butyldimethylsilyl)oxy)-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C23H41ClN5O7PSi",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+H]+ 594.2271",
      "ms_calculated_exact_mass": null,
      "description": "TBS-protected diethyl phosphate nucleoside with methoxymethyl substituent; precursor to compound 18 after TBS removal with TBAF."
    },
    {
      "id": "C60",
      "name": "TBAF (tetrabutylammonium fluoride, 1M in THF)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fluoride source used to remove TBS protecting group from S22 to give compound 18."
    },
    {
      "id": "C61",
      "name": "18 ((−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate)",
      "iupac_name": "(−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-hydroxy-4-(methoxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C17H27ClN5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+H]+ 480.1399",
      "ms_calculated_exact_mass": null,
      "description": "C2′-methoxymethyl analogue of LCB-2122 (compound 18); active cardioprotective compound, demonstrating C2′-OH modification is tolerated."
    },
    {
      "id": "C62",
      "name": "S23a,b (previously reported aldehyde intermediates, 3,4-syn)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "previously reported (Becerril-Jiménez et al. J. Org. Chem. 2019, ref 31)",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Previously reported aldehyde sugar intermediates (3,4-syn) used as starting materials for compound 19 synthesis via NaBH4 reduction and benzylation sequence."
    },
    {
      "id": "C63",
      "name": "Benzyl 2,2,2-trichloroacetimidate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Benzylating agent used under TfOH catalysis to install benzyl ether on the alcohol intermediate from S23a,b."
    },
    {
      "id": "C64",
      "name": "TfOH (triflic acid)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Strong acid catalyst used in benzylation with benzyl trichloroacetimidate."
    },
    {
      "id": "C65",
      "name": "S24 ((+)-((2R,3S,4R,5R)-3-(Benzyloxy)-5-(2,6-dichloro-9H-purin-9-yl)-4-methyltetrahydrofuran-2,4-diyl)bis(methylene) Dibenzoate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-3-(Benzyloxy)-5-(2,6-dichloro-9H-purin-9-yl)-4-methyltetrahydrofuran-2,4-diyl)bis(methylene) Dibenzoate",
      "molecular_formula": "C33H28Cl2N4O6",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 669.1272",
      "ms_calculated_exact_mass": null,
      "description": "Benzyl-protected dibenzoylated N-glycoside with 2,6-dichloropurine; obtained in 56% over 3 steps from S23a,b as β-anomer."
    },
    {
      "id": "C66",
      "name": "S25 ((−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-methyltetrahydrofuran-2,4-diyl)dimethanol)",
      "iupac_name": "(−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-methyltetrahydrofuran-2,4-diyl)dimethanol",
      "molecular_formula": "C19H22ClN5O4",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+H]+ 420.1429",
      "ms_calculated_exact_mass": null,
      "description": "Benzyl-protected diol nucleoside with 2-chloroadenine base; obtained from S24 by ammonolysis, used for bis-TBS protection to S26."
    },
    {
      "id": "C67",
      "name": "2,6-Lutidine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Hindered base used in silylation reactions with TBSOTf."
    },
    {
      "id": "C68",
      "name": "S26 ((+)-9-((2R,3R,4S,5R)-4-(Benzyloxy)-3,5-bis(((tert-butyldimethylsilyl)oxy)methyl)-3-methyltetrahydrofuran-2-yl)-2-chloro-9H-purin-6-amine)",
      "iupac_name": "(+)-9-((2R,3R,4S,5R)-4-(Benzyloxy)-3,5-bis(((tert-butyldimethylsilyl)oxy)methyl)-3-methyltetrahydrofuran-2-yl)-2-chloro-9H-purin-6-amine",
      "molecular_formula": "C31H50ClN5O4Si2",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+H]+ 648.3175",
      "ms_calculated_exact_mass": null,
      "description": "Bis-TBS-protected benzyl-ether nucleoside; used for selective mono-deprotection to give primary alcohol S27."
    },
    {
      "id": "C69",
      "name": "S27 ((−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-(((tert-butyldimethylsilyl)oxy)methyl)-4-methyltetrahydrofuran-2-yl)methanol)",
      "iupac_name": "(−)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-(((tert-butyldimethylsilyl)oxy)methyl)-4-methyltetrahydrofuran-2-yl)methanol",
      "molecular_formula": "C25H36ClN5O4Si",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+H]+ 534.2290",
      "ms_calculated_exact_mass": null,
      "description": "Mono-TBS primary alcohol with benzyl ether at C3′; precursor to S28 via phosphorylation."
    },
    {
      "id": "C70",
      "name": "S28 ((+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-(((tert-butyldimethylsilyl)oxy)methyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-(((tert-butyldimethylsilyl)oxy)methyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C29H45ClN5O7PSi",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+Na]+ 692.2419",
      "ms_calculated_exact_mass": null,
      "description": "TBS- and benzyl-protected diethyl phosphate nucleoside; precursor to compound 19 via TBS removal with TFA/H2O."
    },
    {
      "id": "C71",
      "name": "19 ((+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate)",
      "iupac_name": "(+)-((2R,3S,4R,5R)-5-(6-Amino-2-chloro-9H-purin-9-yl)-3-(benzyloxy)-4-(hydroxymethyl)-4-methyltetrahydrofuran-2-yl)methyl Diethyl Phosphate",
      "molecular_formula": "C23H31ClN5O7P",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by HPLC",
      "ms_observed": "[M+H]+ 556.1748",
      "ms_calculated_exact_mass": null,
      "description": "C3′-benzyl analogue of LCB-2122 (compound 19); active cardioprotective compound, showing C3′-OBn modification is tolerated."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of Compound 11 (LCB-2122) — Steps 1 and 2: S1 to S2",
      "source_section": "main_text",
      "target_compound_id": "C05",
      "target_compound_name": "S2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "N-glycosidic coupling (Vorbrüggen-type)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "S1 (benzoylated sugar lactone precursors)",
              "amount": "4.77 g (8.02 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "2,6-Dichloropurine",
              "amount": "1.67 g (8.82 mmol, 1.10 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C03",
              "name": "DBU",
              "amount": "3.67 mL (24.1 mmol, 3.00 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C04",
              "name": "TMSOTf",
              "amount": "5.9 mL (32 mmol, 4.0 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "dry acetonitrile",
              "volume": "32 mL (0.25 M)"
            }
          ],
          "conditions": {
            "temperature": "−10 °C",
            "time": "6 h",
            "atmosphere": null,
            "ph": null,
            "other": "Reaction quenched with saturated NaHCO3, washed with 0.1 M citric acid; crude ∼8:1 anomeric ratio."
          },
          "product": {
            "compound_id": "C05",
            "name": "S2",
            "yield": "3.96 g (74%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, Hexanes/EtOAc 80:20; isolated as 10:1 β/α diastereomeric mixture",
          "notes": "TMSOTf added dropwise after initial 5 min stirring; product is predominantly β-anomer."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of Compound 11 (LCB-2122) — Steps 2–4: S2 to S3/S4 to S5 to S6 to 11",
      "source_section": "main_text",
      "target_compound_id": "C16",
      "target_compound_name": "11 (LCB-2122)",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Ammonolysis / debenzoylation / 6-Cl to 6-NH2 conversion",
          "reactants": [
            {
              "compound_id": "C05",
              "name": "S2",
              "amount": "3.29 g (4.97 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C06",
              "name": "NH3(g)",
              "amount": "excess (bubbled until saturation)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "50 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "80 °C",
            "time": "24 h",
            "atmosphere": null,
            "ph": null,
            "other": "High-pressure flask sealed; reaction diluted with MeOH (100 mL) and concentrated after completion. With additional NH3 saturation and heating at 80 °C for 48 h, S4 can be obtained in 71% yield."
          },
          "product": {
            "compound_id": null,
            "name": "Mixture of S3 and S4",
            "yield": "S3: 702 mg (43%); S4: 714 mg (44%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, DCM/MeOH 90:10",
          "notes": "Step produces two products: S3 (C07, 6-methoxy byproduct) and S4 (C08, desired 6-amino). S4 corresponds to previously reported compound from Guindon lab (ref 32)."
        },
        {
          "step_number": 2,
          "reaction_type": "Acetonide protection of vicinal diol",
          "reactants": [
            {
              "compound_id": "C08",
              "name": "S4",
              "amount": "1.05 g (3.18 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C09",
              "name": "CSA",
              "amount": "737 mg (3.18 mmol, 1.00 equiv)",
              "role": "acid"
            },
            {
              "compound_id": "C10",
              "name": "2,2-Dimethoxypropane",
              "amount": "7.0 mL (57 mmol, 18 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "dry acetone",
              "volume": "32 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "16 h",
            "atmosphere": null,
            "ph": null,
            "other": "Molecular sieves 3 Å (3.0 g) added; concentrated under reduced pressure after reaction."
          },
          "product": {
            "compound_id": "C11",
            "name": "S5",
            "yield": "739 mg (63%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, DCM/MeOH 90:10",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Phosphorylation of primary alcohol (C5′-OH)",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "S5",
              "amount": "1.13 g (3.06 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl (1.0 M in THF)",
              "amount": "4.6 mL (4.6 mmol, 1.5 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C13",
              "name": "Diethylchlorophosphate",
              "amount": "0.66 mL (4.6 mmol, 1.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "31 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "4 h (after t-BuMgCl 45 min pre-stirring)",
            "atmosphere": null,
            "ph": null,
            "other": "t-BuMgCl added dropwise; diethylchlorophosphate added slowly; quenched with MeOH."
          },
          "product": {
            "compound_id": "C14",
            "name": "S6",
            "yield": "1.33 g (86%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "reversed-phase (C18) flash chromatography, H2O/MeCN 50:50",
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "Acetonide deprotection (acid-labile ketal removal)",
          "reactants": [
            {
              "compound_id": "C14",
              "name": "S6",
              "amount": "360 mg (0.711 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C15",
              "name": "TFA/H2O (8:2)",
              "amount": "7.1 mL (0.10 M)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "7.1 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "2 h",
            "atmosphere": null,
            "ph": null,
            "other": "MeOH added after reaction; coevaporated with MeOH (3×) after concentration."
          },
          "product": {
            "compound_id": "C16",
            "name": "11 (LCB-2122)",
            "yield": "294 mg (88%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "reversed-phase (C18) flash chromatography, H2O/MeCN 70:30",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Synthesis of Compound 12 (free phosphate analogue)",
      "source_section": "main_text",
      "target_compound_id": "C20",
      "target_compound_name": "12",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Phosphorylation of primary alcohol (C5′-OH) with POCl3",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "S5",
              "amount": "36.7 mg (99.2 μmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C17",
              "name": "Et3N",
              "amount": "124 μL (893 μmol, 9.00 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C18",
              "name": "POCl3",
              "amount": "13.9 μL (149 μmol, 1.50 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "1 mL (0.1 M)"
            }
          ],
          "conditions": {
            "temperature": "0 °C",
            "time": "2 h then 1 h after addition of ice chips",
            "atmosphere": null,
            "ph": null,
            "other": "Ice chips added after 2 h; mixture stirred for another 1 h at 0 °C; concentrated under reduced pressure."
          },
          "product": {
            "compound_id": "C19",
            "name": "S7 (triethylammonium salt)",
            "yield": "49 mg (90%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "reversed-phase (C18) flash chromatography, H2O/MeCN 70:30",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Acetonide deprotection",
          "reactants": [
            {
              "compound_id": "C19",
              "name": "S7",
              "amount": "156 mg (0.347 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C15",
              "name": "TFA/H2O (8:2)",
              "amount": "3.5 mL (0.10 M)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "3.5 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "4 h",
            "atmosphere": null,
            "ph": null,
            "other": "MeOH added after reaction; coevaporated with MeOH (3×) after concentration."
          },
          "product": {
            "compound_id": "C20",
            "name": "12",
            "yield": "31 mg (22%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "reversed-phase (C18) flash chromatography, H2O/MeCN 75:25",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Synthesis of Compound 13 (dimethyl phosphate analogue)",
      "source_section": "main_text",
      "target_compound_id": "C23",
      "target_compound_name": "13",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Phosphorylation of primary alcohol with dimethylchlorophosphate",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "S5",
              "amount": "54.4 mg (147 μmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl (1.0 M in THF)",
              "amount": "0.16 mL (0.16 mmol, 1.1 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C21",
              "name": "Dimethylchlorophosphate",
              "amount": "18 μL (0.16 mmol, 1.1 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "1.5 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "4.5 h (after 45 min pre-stirring with t-BuMgCl)",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with MeOH; 34% of S5 recovered as starting material alongside S8."
          },
          "product": {
            "compound_id": "C22",
            "name": "S8",
            "yield": "35 mg (50%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, DCM/MeOH 95:5",
          "notes": "18.3 mg (34%) of recovered starting material S5 also obtained."
        },
        {
          "step_number": 2,
          "reaction_type": "Acetonide deprotection",
          "reactants": [
            {
              "compound_id": "C22",
              "name": "S8",
              "amount": "24.7 mg (51.7 μmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C15",
              "name": "TFA/H2O (8:2)",
              "amount": "0.6 mL (0.09 M)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "0.6 mL (0.09 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "3 h",
            "atmosphere": null,
            "ph": null,
            "other": "MeOH added after reaction; coevaporated with MeOH (3×) after concentration."
          },
          "product": {
            "compound_id": "C23",
            "name": "13",
            "yield": "8.2 mg (36%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "reversed-phase (C18) flash chromatography, H2O/MeCN 50:50",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Synthesis of Compound 14 (diisopropyl phosphate analogue)",
      "source_section": "main_text",
      "target_compound_id": "C26",
      "target_compound_name": "14",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Phosphorylation of primary alcohol with diisopropyl chlorophosphate",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "S5",
              "amount": "75 mg (0.20 mmol, 1.0 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl (1.7 M in THF)",
              "amount": "0.13 mL (0.23 mmol, 1.1 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C24",
              "name": "Diisopropyl chlorophosphate",
              "amount": "40 μL (0.23 mmol, 1.1 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "2 mL (0.1 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "16 h (after 45 min pre-stirring with t-BuMgCl)",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with MeOH and concentrated."
          },
          "product": {
            "compound_id": "C25",
            "name": "S9",
            "yield": "79 mg (73%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, DCM/MeOH 90:10",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Acetonide deprotection",
          "reactants": [
            {
              "compound_id": "C25",
              "name": "S9",
              "amount": "34.8 mg (0.065 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C15",
              "name": "TFA/H2O (8:2)",
              "amount": "0.7 mL (0.1 M)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "0.7 mL (0.1 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "4 h",
            "atmosphere": null,
            "ph": null,
            "other": "MeOH added; coevaporated with MeOH (3×)."
          },
          "product": {
            "compound_id": "C26",
            "name": "14",
            "yield": "24 mg (74%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "reversed-phase (C18) flash chromatography, H2O/MeCN 60:40",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Synthesis of Compound 15 (4′-thio analogue)",
      "source_section": "main_text",
      "target_compound_id": "C29",
      "target_compound_name": "15",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Phosphorylation of primary alcohol (C5′-OH)",
          "reactants": [
            {
              "compound_id": "C27",
              "name": "S10 (previously reported 4′-thio primary alcohol)",
              "amount": "95 mg (0.17 mmol, 1.0 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl (1.7 M in THF)",
              "amount": "0.15 mL (0.25 mmol, 1.5 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C13",
              "name": "Diethylchlorophosphate",
              "amount": "36 μL (0.25 mmol, 1.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "1.7 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "16 h (after 45 min pre-stirring with t-BuMgCl)",
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C28",
            "name": "S11",
            "yield": "56 mg (48%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, Hexanes/EtOAc 60:40",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Ammonolysis (debenzoylation and 6-Cl to 6-NH2 conversion)",
          "reactants": [
            {
              "compound_id": "C28",
              "name": "S11",
              "amount": "33 mg (0.047 mmol, 1.0 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C06",
              "name": "NH3(g)",
              "amount": "excess (bubbled until saturation, twice)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "1.2 mL (0.040 M)"
            }
          ],
          "conditions": {
            "temperature": "80 °C",
            "time": "16 h then additional 24 h after second NH3 saturation",
            "atmosphere": null,
            "ph": null,
            "other": "High-pressure flask; upon cooling to RT, NH3 saturated again and stirred 24 h more at 80 °C; concentrated after cooling."
          },
          "product": {
            "compound_id": "C29",
            "name": "15",
            "yield": "13 mg (58%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, EtOAc/MeOH 70:30",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Synthesis of Compound 16 (des-2-Cl analogue)",
      "source_section": "main_text",
      "target_compound_id": "C31",
      "target_compound_name": "16",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Hydrogenolysis (reductive dechlorination)",
          "reactants": [
            {
              "compound_id": "C16",
              "name": "11 (LCB-2122)",
              "amount": "23 mg (0.049 mmol, 1.0 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C30",
              "name": "Pd/C (10 wt %)",
              "amount": "23 mg (1.0 equiv by mass)",
              "role": "catalyst"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "0.5 mL (0.1 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "6 h",
            "atmosphere": "H2 (positive pressure, after N2 removal)",
            "ph": null,
            "other": "Filtered over Celite with MeOH/EtOAc (50:50) after reaction."
          },
          "product": {
            "compound_id": "C31",
            "name": "16",
            "yield": "15.2 mg (72%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "reversed-phase (C18) flash chromatography, H2O/MeCN 60:40",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P8",
      "pathway_name": "Synthesis of Compound 17 (inosine analogue)",
      "source_section": "main_text",
      "target_compound_id": "C35",
      "target_compound_name": "17",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Saponification and 6-Cl hydrolysis to 6-oxo (hypoxanthine)",
          "reactants": [
            {
              "compound_id": "C05",
              "name": "S2",
              "amount": "500 mg (0.756 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C33",
              "name": "2 N NaOH",
              "amount": "3.8 mL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "EtOH",
              "volume": "7.6 mL (1.0 M)"
            }
          ],
          "conditions": {
            "temperature": "50 °C (pre-dissolution), then RT",
            "time": "5 h",
            "atmosphere": null,
            "ph": null,
            "other": "Excess TFA added after reaction; concentrated, dissolved in H2O/CH2Cl2, extracted with CH2Cl2 (3×)."
          },
          "product": {
            "compound_id": "C32",
            "name": "S12",
            "yield": "176 mg (70%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "reversed-phase (C18) flash chromatography, H2O/MeOH 80:20",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Acetonide protection of vicinal diol",
          "reactants": [
            {
              "compound_id": "C32",
              "name": "S12",
              "amount": "100 mg (0.302 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C09",
              "name": "CSA",
              "amount": "70 mg (0.302 mmol, 1.0 equiv)",
              "role": "acid"
            },
            {
              "compound_id": "C10",
              "name": "2,2-Dimethoxypropane",
              "amount": "0.67 mL (5.4 mmol, 18 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "dry acetone",
              "volume": "3 mL (0.1 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "16 h",
            "atmosphere": null,
            "ph": null,
            "other": "Molecular sieves 3 Å (180 mg); EtOAc workup with 0.1 M HCl wash."
          },
          "product": {
            "compound_id": "C34",
            "name": "S13",
            "yield": "80 mg (71%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, CH2Cl2/MeOH 85:15",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Phosphorylation then in situ acetonide deprotection (one-pot)",
          "reactants": [
            {
              "compound_id": "C34",
              "name": "S13",
              "amount": "22 mg (0.059 mmol, 1.0 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl",
              "amount": "148 μL (0.148 mmol, 2.5 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C13",
              "name": "Diethylchlorophosphate",
              "amount": "22 μL (0.148 mmol, 2.5 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C15",
              "name": "TFA/H2O (8:2)",
              "amount": "3.0 mL (0.02 M)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "0.6 mL (0.1 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "4 h (phosphorylation) then 2 h (deprotection)",
            "atmosphere": "open atmosphere for deprotection step",
            "ph": null,
            "other": "TFA/H2O added dropwise after phosphorylation; MeOH added and coevaporated (3×)."
          },
          "product": {
            "compound_id": "C35",
            "name": "17",
            "yield": "10 mg (36%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "reversed-phase (C18) flash chromatography, H2O/MeCN 70:30",
          "notes": "Two-step sequence performed without isolation of intermediate phosphorylated acetonide."
        }
      ]
    },
    {
      "pathway_id": "P9",
      "pathway_name": "Synthesis of Compound 18 (C2′-methoxymethyl analogue)",
      "source_section": "main_text",
      "target_compound_id": "C61",
      "target_compound_name": "18",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "TBS silyl protection of secondary alcohol",
          "reactants": [
            {
              "compound_id": "C36",
              "name": "S14 (previously reported secondary alcohol lactone)",
              "amount": "140 mg (0.489 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C38",
              "name": "Imidazole",
              "amount": "83 mg (1.2 mmol, 2.5 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C37",
              "name": "TBSOTf",
              "amount": "0.17 mL (0.73 mmol, 1.5 equiv)",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "1.9 mL (0.50 M)"
            }
          ],
          "conditions": {
            "temperature": "0 °C then room temperature",
            "time": "21 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with saturated NaHCO3; aqueous layer extracted with Et2O (3×); washed with brine."
          },
          "product": {
            "compound_id": "C39",
            "name": "S15",
            "yield": "188 mg (96%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, Hexanes/EtOAc 70:30",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "DIBAL-H reduction of lactone to lactol",
          "reactants": [
            {
              "compound_id": "C39",
              "name": "S15",
              "amount": "329 mg (0.821 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C40",
              "name": "DIBAL-H (1 M in Hexanes)",
              "amount": "1.2 mL (1.2 mmol, 1.5 equiv)",
              "role": "reductant"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "4.5 mL (0.18 M)"
            }
          ],
          "conditions": {
            "temperature": "−78 °C",
            "time": "3.5 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with saturated potassium sodium tartrate at −78 °C; warmed to RT and stirred 1 h; aqueous layer extracted with Et2O (3×)."
          },
          "product": {
            "compound_id": "C41",
            "name": "S16a,b",
            "yield": "232 mg (70%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography, Hexanes/EtOAc 80:20",
          "notes": "Obtained as 2:1 mixture of anomers."
        },
        {
          "step_number": 3,
          "reaction_type": "Benzoylation of anomeric hydroxyl",
          "reactants": [
            {
              "compound_id": "C41",
              "name": "S16a,b",
              "amount": "232 mg (0.576 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C43",
              "name": "DMAP",
              "amount": "7 mg (0.06 mmol, 0.1 equiv)",
              "role": "catalyst"
            },
            {
              "compound_id": "C44",
              "name": "Pyridine",
              "amount": "0.28 mL (3.5 mmol, 6.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C42",
              "name": "BzCl",
              "amount": "0.10 mL (0.86 mmol, 1.5 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C45",
              "name": "Ethylenediamine",
              "amount": "0.09 mL (1.4 mmol, 2.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "3.1 mL (0.18 M)"
            }
          ],
          "conditions": {
            "temperature": "0 °C then room temperature",
            "time": "16 h (then 30 min with ethylenediamine at 0 °C)",
            "atmosphere": null,
            "ph": null,
            "other": "BzCl added slowly at 0 °C; ethylenediamine added at 0 °C to quench excess BzCl."
          },
          "product": {
            "compound_id": "C46",
            "name": "S17a,b",
            "yield": "266 mg (91%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, Hexanes/EtOAc 70:30",
          "notes": "Isolated as 2:1 diastereomeric mixture."
        },
        {
          "step_number": 4,
          "reaction_type": "Ozonolysis of vinyl group followed by NaBH4 reduction",
          "reactants": [
            {
              "compound_id": "C46",
              "name": "S17a,b",
              "amount": "4.07 g (8.02 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C47",
              "name": "O3",
              "amount": "excess (bubbled ~2 h until blue)",
              "role": "oxidant"
            },
            {
              "compound_id": "C17",
              "name": "NEt3",
              "amount": "1.2 mL (8.0 mmol, 1.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C48",
              "name": "NaBH4",
              "amount": "0.46 g (12 mmol, 1.5 equiv)",
              "role": "reductant"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "0.4 L (0.02 M) for ozonolysis"
            }
          ],
          "conditions": {
            "temperature": "−78 °C (ozonolysis); 0 °C (NaBH4 reduction)",
            "time": "~2 h (O3); 1 h warm-up; 5 h (NaBH4)",
            "atmosphere": "N2 (purged after ozonolysis)",
            "ph": null,
            "other": "After ozonolysis, N2 purge; NEt3 added; stirred 1 h warming to RT. Crude diluted in MeOH for NaBH4 reduction at 0 °C; quenched with H2O."
          },
          "product": {
            "compound_id": "C49",
            "name": "S18a,b",
            "yield": "3.12 g (76%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, Hexanes/EtOAc 80:20",
          "notes": "Obtained as 5:1 diastereomeric mixture."
        },
        {
          "step_number": 5,
          "reaction_type": "O-Methylation of primary alcohol",
          "reactants": [
            {
              "compound_id": "C49",
              "name": "S18a,b",
              "amount": "425 mg (0.832 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C50",
              "name": "2,6-Di-tert-butyl-4-methylpyridine",
              "amount": "683 mg (3.33 mmol, 4.00 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C51",
              "name": "MeOTf",
              "amount": "0.66 mL (5.8 mmol, 7.0 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "8.5 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "40 °C",
            "time": "18 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with water; aqueous layer extracted with CH2Cl2 (3×)."
          },
          "product": {
            "compound_id": "C52",
            "name": "S19a,b",
            "yield": "373 mg (85%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, Hexanes/EtOAc 80:20",
          "notes": "Obtained as 4:1 diastereomeric mixture."
        },
        {
          "step_number": 6,
          "reaction_type": "N-glycosidic coupling with 2-chloroadenine (Vorbrüggen-type)",
          "reactants": [
            {
              "compound_id": "C52",
              "name": "S19a,b",
              "amount": "231 mg (0.440 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C53",
              "name": "2-Chloroadenine",
              "amount": "149 mg (0.880 mmol, 2.00 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C54",
              "name": "BSA",
              "amount": "0.70 mL (2.9 mmol, 6.5 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C04",
              "name": "TMSOTf",
              "amount": "0.16 mL (0.88 mmol, 2.0 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "anhydrous DCE (1,2-dichloroethane)",
              "volume": "1.8 mL (0.50 M) for BSA step + 0.88 mL (0.50 M) for sugar"
            }
          ],
          "conditions": {
            "temperature": "84 °C",
            "time": "3 h",
            "atmosphere": null,
            "ph": null,
            "other": "BSA heated with 2-chloroadenine at 84 °C until clear solution; cooled to RT then added to sugar solution; TMSOTf added dropwise; diluted with EtOAc and saturated NaHCO3 workup; crude ~1.2:1 diastereomeric ratio."
          },
          "product": {
            "compound_id": "C55",
            "name": "S20a,b",
            "yield": "222 mg (88%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, CH2Cl2/MeOH 70:30",
          "notes": "Obtained as 1.2:1 diastereomeric mixture in favor of β-anomer."
        },
        {
          "step_number": 7,
          "reaction_type": "Selective mono-TBS deprotection",
          "reactants": [
            {
              "compound_id": "C55",
              "name": "S20a,b",
              "amount": "295 mg (0.515 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C56",
              "name": "TFA/H2O (1:1)",
              "amount": "2.86 mL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "5.7 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "0 °C",
            "time": "4 h",
            "atmosphere": null,
            "ph": null,
            "other": "Saturated NaHCO3 added; warmed to RT; aqueous layer extracted with Et2O (4×)."
          },
          "product": {
            "compound_id": null,
            "name": "Mixture of S21a (α) and S21b (β)",
            "yield": "S21a: 64 mg (27%); S21b: 89 mg (38%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, EtOAc/MeOH 90:10",
          "notes": "S21a (C57) and S21b (C58) isolated separately by chromatography; S21b (β-anomer) used for the next step."
        },
        {
          "step_number": 8,
          "reaction_type": "Phosphorylation of primary alcohol",
          "reactants": [
            {
              "compound_id": "C58",
              "name": "S21b",
              "amount": "84 mg (0.18 mmol, 1.0 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl (1 M in THF)",
              "amount": "0.46 mL (0.46 mmol, 2.5 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C13",
              "name": "Diethylchlorophosphate",
              "amount": "40 μL (0.28 mmol, 1.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "1.1 mL (0.17 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "16 h (after 30 min pre-stirring with t-BuMgCl)",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with MeOH; concentrated under reduced pressure."
          },
          "product": {
            "compound_id": "C59",
            "name": "S22",
            "yield": "47 mg (43%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, Hexanes/EtOAc 0:100",
          "notes": null
        },
        {
          "step_number": 9,
          "reaction_type": "TBS deprotection with TBAF",
          "reactants": [
            {
              "compound_id": "C59",
              "name": "S22",
              "amount": "45 mg (0.076 mmol, 1.0 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C60",
              "name": "TBAF (1.0 M in THF)",
              "amount": "1.5 mL (0.15 mmol, 2.0 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "0.76 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "0 °C then room temperature",
            "time": "16 h",
            "atmosphere": null,
            "ph": null,
            "other": "TBAF added dropwise at 0 °C; warmed to RT; quenched with MeOH and concentrated."
          },
          "product": {
            "compound_id": "C61",
            "name": "18",
            "yield": "31 mg (85%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, EtOAc/MeOH 50:50",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P10",
      "pathway_name": "Synthesis of Compound 19 (C3′-benzyl analogue)",
      "source_section": "main_text",
      "target_compound_id": "C71",
      "target_compound_name": "19",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NaBH4 reduction of aldehyde, then benzyl etherification, then N-glycosidic coupling (3-step sequence)",
          "reactants": [
            {
              "compound_id": "C62",
              "name": "S23a,b (aldehyde intermediates)",
              "amount": "12.0 g (24.6 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C48",
              "name": "NaBH4",
              "amount": "1.02 g (0.22 mmol [sic, 27 mmol], 1.1 equiv)",
              "role": "reductant"
            },
            {
              "compound_id": "C63",
              "name": "Benzyl 2,2,2-trichloroacetimidate",
              "amount": "2.4 mL (13 mmol, 3.0 equiv based on 4.36 mmol crude alcohol)",
              "role": "other"
            },
            {
              "compound_id": "C64",
              "name": "TfOH",
              "amount": "50 μL (0.44 mmol, 0.10 equiv based on 4.36 mmol crude alcohol)",
              "role": "acid"
            },
            {
              "compound_id": "C02",
              "name": "2,6-Dichloropurine",
              "amount": "907 mg (4.79 mmol, 1.10 equiv based on benzoate step)",
              "role": "other"
            },
            {
              "compound_id": "C03",
              "name": "DBU",
              "amount": "2.0 mL (13 mmol, 3.0 equiv based on benzoate step)",
              "role": "base"
            },
            {
              "compound_id": "C04",
              "name": "TMSOTf",
              "amount": "3.21 mL (17.4 mmol, 4.00 equiv based on benzoate step)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "MeOH (NaBH4 step); DCM/Cyclohexane 1:2 (benzylation); MeCN (N-glycosidic coupling)",
              "volume": "0.16 L / 44 mL / 22 mL respectively"
            }
          ],
          "conditions": {
            "temperature": "0 °C (NaBH4); RT (benzylation, 16 h); −10 °C (N-glycosidic, 5 h)",
            "time": "3 h (NaBH4); 16 h (benzylation); 5 h (coupling)",
            "atmosphere": null,
            "ph": null,
            "other": "Crude alcohols from NaBH4 filtered over silica with Et2O without further purification; benzylation quenched with NEt3 (0.15 equiv) then filtered over Celite; N-glycosidic coupling quenched with saturated NaHCO3; crude ~10:1 β/α ratio."
          },
          "product": {
            "compound_id": "C65",
            "name": "S24",
            "yield": "1.58 g (56% over 3 steps)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, Hexanes/EtOAc 70:30",
          "notes": "Three-step sequence (reduction, benzylation, N-glycosidic coupling) performed with only one intermediate purification step (silica filtration after NaBH4)."
        },
        {
          "step_number": 2,
          "reaction_type": "Ammonolysis (debenzoylation and 6-Cl to 6-NH2)",
          "reactants": [
            {
              "compound_id": "C65",
              "name": "S24",
              "amount": "371 mg (0.573 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C06",
              "name": "NH3(g)",
              "amount": "excess (bubbled twice until saturation)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "12 mL (0.048 M)"
            }
          ],
          "conditions": {
            "temperature": "80 °C",
            "time": "24 h then additional 16 h after second NH3 saturation",
            "atmosphere": null,
            "ph": null,
            "other": "High-pressure flask; diluted with MeOH (10 mL) and concentrated."
          },
          "product": {
            "compound_id": "C66",
            "name": "S25",
            "yield": "178 mg (74%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, CH2Cl2/MeOH 90:10",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Bis-TBS silyl protection of diol",
          "reactants": [
            {
              "compound_id": "C66",
              "name": "S25",
              "amount": "317 mg (0.756 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C67",
              "name": "2,6-Lutidine",
              "amount": "0.44 mL (3.8 mmol, 5.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C37",
              "name": "TBSOTf",
              "amount": "0.52 mL (2.3 mmol, 3.0 equiv)",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "DCM with 1 drop DMF",
              "volume": "7.6 mL (0.10 M)"
            }
          ],
          "conditions": {
            "temperature": "0 °C then room temperature",
            "time": "16 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with saturated NaHCO3; washed with brine and 0.1 N HCl."
          },
          "product": {
            "compound_id": "C68",
            "name": "S26",
            "yield": "321 mg (65%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, Hexanes/EtOAc 60:40",
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "Selective mono-TBS deprotection",
          "reactants": [
            {
              "compound_id": "C68",
              "name": "S26",
              "amount": "358 mg (0.552 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C56",
              "name": "TFA/H2O (1:1)",
              "amount": "3.1 mL (0.18 M)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "6.1 mL (0.090 M)"
            }
          ],
          "conditions": {
            "temperature": "0 °C",
            "time": "4 h",
            "atmosphere": null,
            "ph": null,
            "other": "Saturated NaHCO3 added; aqueous phase extracted with Et2O (2×); washed with brine."
          },
          "product": {
            "compound_id": "C69",
            "name": "S27",
            "yield": "207 mg (70%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "flash chromatography on silica gel, CH2Cl2/MeOH 95:5",
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "Phosphorylation of primary alcohol",
          "reactants": [
            {
              "compound_id": "C69",
              "name": "S27",
              "amount": "200 mg (0.374 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C12",
              "name": "t-BuMgCl",
              "amount": "0.56 mL (0.56 mmol, 1.5 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C13",
              "name": "Diethylchlorophosphate",
              "amount": "81 μL (0.56 mmol, 1.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "4 mL (0.1 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "16 h (after 45 min pre-stirring)",
            "atmosphere": null,
            "ph": null,
            "other": "MeOH added; concentrated under reduced pressure."
          },
          "product": {
            "compound_id": "C70",
            "name": "S28",
            "yield": "216 mg (86%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "reversed-phase (C18) flash chromatography, H2O/MeCN gradient",
          "notes": null
        },
        {
          "step_number": 6,
          "reaction_type": "TBS deprotection (acid-mediated)",
          "reactants": [
            {
              "compound_id": "C70",
              "name": "S28",
              "amount": "29.3 mg (0.0437 mmol, 1.00 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C15",
              "name": "TFA/H2O (8:2)",
              "amount": "0.5 mL (0.1 M)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "0.5 mL (0.1 M)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "4 h",
            "atmosphere": null,
            "ph": null,
            "other": "MeOH added; concentrated and coevaporated with MeOH (3×)."
          },
          "product": {
            "compound_id": "C71",
            "name": "19",
            "yield": "10.9 mg (45%)",
            "purity": ">95% by HPLC",
            "hplc_retention_time_min": null
          },
          "purification": "reversed-phase (C18) flash chromatography, H2O/MeCN 50:50",
          "notes": null
        }
      ]
    }
  ]
}
```


## conformational-dynamics-in-the-cell-membrane-interactions-of-bispecific-targeted-degrader-therapeutics

#### Claude

##### Attempt 1
```
{
  "extraction": {
    "prompt_version": "v3.2",
    "extraction_date": "2026-03-30",
    "model_name": "claude-sonnet-4-20250514",
    "extractor_notes": "SI found: jm5c01499_si_001.pdf (Supporting Information for the main article). SI schemes identified: one reaction scheme page (S28) showing synthesis routes for compounds 11–17, including SI intermediates S-1 through S-9. SI compounds identified: S-1, S-2, S-3, S-4, S-5, S-6, S-7, S-8, S-9. Total pathway count: 8 pathways — P1 (compound 11), P2 (compound 12), P3 (compound 13), P4 (compound 14), P5 (compound 15), P6 (compound 16), P7 (compound S-9, intermediate for 17), P8 (compound 17). Excluded reference compounds: Commercially sourced PROTACs 1–10 (sourced from Tocris and used only for biological/membrane assay measurements, not synthesized in this study; they appear in Figures 2–4 and experimental binding measurements but have no synthesis described), atorvastatin, lopinavir, verapamil (internal standards/controls in analytical assays only). Any procedures genuinely absent: Full experimental procedures for SI starting materials S-1, S-2, S-3, S-4, S-5, S-6 are not provided in either the main text or SI — only their structures appear in reaction schemes and they are referenced by label as coupling partners. Their synthesis or commercial sourcing details are not described. S-7 (2-(2,6-dioxopiperidin-3-yl)-4-hydroxyisoindoline-1,3-dione) and S-8 (tert-butyl 3-hydroxypyrrolidine-1-carboxylate) are named reactants in the synthesis of S-9 but no separate synthesis procedures are given for them — they appear to be commercially available starting materials. Mass type notes: All HRMS data reported as monoisotopic exact masses (ESI+, QTOF instrument)."
  },

  "paper": {
    "title": "Conformational Dynamics in the Cell Membrane Interactions of Bispecific Targeted Degrader Therapeutics",
    "authors": [
      "Emma Inganäs",
      "Hanna Lavén",
      "Rémi Caraballo",
      "Fredrik Klingegård",
      "MyLan Eklund",
      "Linda Andersson",
      "Constanze Hilgendorf",
      "Pär Matsson"
    ],
    "doi": "10.1021/acs.jmedchem.5c01499",
    "journal": "Journal of Medicinal Chemistry",
    "year": 2025,
    "synthesis_scale": "lab",
    "method_completeness": "full",
    "has_synthesis": true,
    "extraction_notes": "Compounds 11–17 were synthesized in-house at SciLifeLab (Solna, Sweden). SI starting materials S-1 through S-6 are depicted in the SI reaction scheme but no synthesis or sourcing procedures are explicitly described for them; they function as coupling partners (VHL/pomalidomide/thalidomide-linked amine intermediates). S-7 and S-8 are commercially available reactants named in the text."
  },

  "compounds": [
    {
      "id": "C01",
      "name": "JQ-1 carboxylic acid",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "BET bromodomain (BRD4) ligand bearing a free carboxylic acid; used as the POI ligand–acid coupling partner in all amide bond-forming reactions to produce compounds 11–17."
    },
    {
      "id": "C02",
      "name": "TBTU",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "O-(Benzotriazol-1-yl)-N,N,N',N'-tetramethyluronium tetrafluoroborate; amide coupling reagent used in all coupling reactions to produce compounds 11–17."
    },
    {
      "id": "C03",
      "name": "DIPEA",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "N,N-Diisopropylethylamine; Hünig's base used as a non-nucleophilic base in all amide coupling reactions."
    },
    {
      "id": "C04",
      "name": "S-1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial or externally sourced; synthesis not described in available documents",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "VHL-recruiting amine-containing intermediate (structure visible in SI scheme S28); used as the amine coupling partner for synthesis of compound 11."
    },
    {
      "id": "C05",
      "name": "compound 11",
      "iupac_name": "(2S,4R)-1-((2S)-2-(5-(2-((6S)-4-(4-Chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)acetamido)pentanamido)-3,3-dimethylbutanoyl)-4-hydroxy-N-(4-(4-methylthiazol-5-yl)benzyl)pyrrolidine-2-carboxamide",
      "molecular_formula": "C46H54ClN9O5S2",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 912.3447",
      "ms_calculated_exact_mass": 912.3451,
      "description": "VHL-directed PROTAC (BRD4 POI ligand JQ-1 + VHL E3 ligand, alkane linker); synthesized by TBTU-mediated amide coupling of JQ-1 carboxylic acid and S-1."
    },
    {
      "id": "C06",
      "name": "S-2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial or externally sourced; synthesis not described in available documents",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Pomalidomide-derived cyclohexylmethyl amine intermediate (structure visible in SI scheme S28); used as the amine coupling partner for synthesis of compound 12."
    },
    {
      "id": "C07",
      "name": "compound 12",
      "iupac_name": "2-((6S)-4-(4-Chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)-N-(((1RS,3SR)-3-(((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)amino)methyl)cyclohexyl)methyl)acetamide",
      "molecular_formula": "C40H41ClN8O5S",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 781.2677",
      "ms_calculated_exact_mass": 781.2682,
      "description": "CRBN-directed PROTAC (BRD4 POI ligand JQ-1 + pomalidomide CRBN ligand with cyclohexane ring linker); synthesized by TBTU-mediated amide coupling of JQ-1 carboxylic acid and S-2."
    },
    {
      "id": "C08",
      "name": "S-3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial or externally sourced; synthesis not described in available documents",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Pomalidomide-derived propylamine intermediate (structure visible in SI scheme S28); used as the amine coupling partner for synthesis of compound 13."
    },
    {
      "id": "C09",
      "name": "compound 13",
      "iupac_name": "2-((6S)-4-(4-Chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)-N-(3-((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)amino)propyl)acetamide",
      "molecular_formula": "C35H33ClN8O5S",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 713.2052",
      "ms_calculated_exact_mass": 713.2056,
      "description": "CRBN-directed PROTAC (BRD4 POI ligand JQ-1 + pomalidomide CRBN ligand, short propyl linker); synthesized by TBTU-mediated amide coupling of JQ-1 carboxylic acid and S-3."
    },
    {
      "id": "C10",
      "name": "S-4",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial or externally sourced; synthesis not described in available documents",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Pomalidomide-derived PEG-triethyleneglycol amine intermediate (structure visible in SI scheme S28); used as the amine coupling partner for synthesis of compound 14."
    },
    {
      "id": "C11",
      "name": "compound 14",
      "iupac_name": "2-((6S)-4-(4-Chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)-N-(2-(2-(2-(2-((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)oxy)acetamido)ethoxy)ethoxy)ethyl)acetamide",
      "molecular_formula": "C40H41ClN8O9S",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 845.2475",
      "ms_calculated_exact_mass": 845.2479,
      "description": "CRBN-directed PROTAC (BRD4 POI ligand JQ-1 + pomalidomide CRBN ligand, long PEG linker with oxyacetamido connector); synthesized by TBTU-mediated amide coupling of JQ-1 carboxylic acid and S-4."
    },
    {
      "id": "C12",
      "name": "S-5",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial or externally sourced; synthesis not described in available documents",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Pomalidomide-piperazine intermediate (structure visible in SI scheme S28); used as the amine coupling partner for synthesis of compound 15."
    },
    {
      "id": "C13",
      "name": "compound 15",
      "iupac_name": "4-(4-(2-((6S)-4-(4-Chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)acetyl)piperazin-1-yl)-2-(2,6-dioxopiperidin-3-yl)isoindoline-1,3-dione",
      "molecular_formula": "C36H33ClN8O5S",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 725.2054",
      "ms_calculated_exact_mass": 725.2056,
      "description": "CRBN-directed PROTAC (BRD4 POI ligand JQ-1 + pomalidomide CRBN ligand, piperazine ring linker); synthesized by TBTU-mediated amide coupling of JQ-1 carboxylic acid and S-5."
    },
    {
      "id": "C14",
      "name": "S-6",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial or externally sourced; synthesis not described in available documents",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Pomalidomide-derived shorter PEG amine intermediate (structure visible in SI scheme S28); used as the amine coupling partner for synthesis of compound 16."
    },
    {
      "id": "C15",
      "name": "compound 16",
      "iupac_name": "2-((6S)-4-(4-Chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)-N-(2-(2-(2-((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)oxy)acetamido)ethoxy)ethyl)acetamide",
      "molecular_formula": "C38H37ClN8O8S",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 801.2215",
      "ms_calculated_exact_mass": 801.2217,
      "description": "CRBN-directed PROTAC (BRD4 POI ligand JQ-1 + pomalidomide CRBN ligand, shorter PEG linker with oxyacetamido connector); synthesized by TBTU-mediated amide coupling of JQ-1 carboxylic acid and S-6."
    },
    {
      "id": "C16",
      "name": "S-7 (2-(2,6-dioxopiperidin-3-yl)-4-hydroxyisoindoline-1,3-dione)",
      "iupac_name": "2-(2,6-dioxopiperidin-3-yl)-4-hydroxyisoindoline-1,3-dione",
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Pomalidomide precursor bearing a free 4-hydroxyl group on the isoindolinone ring; used as the phenol component in Mitsunobu reaction to produce S-9."
    },
    {
      "id": "C17",
      "name": "S-8 (tert-butyl 3-hydroxypyrrolidine-1-carboxylate)",
      "iupac_name": "tert-butyl 3-hydroxypyrrolidine-1-carboxylate",
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Boc-protected 3-hydroxypyrrolidine; used as the alcohol component in Mitsunobu reaction with S-7 to provide Boc-protected intermediate S-9."
    },
    {
      "id": "C18",
      "name": "triphenylphosphine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Phosphine component of the Mitsunobu reagent system used in the synthesis of S-9."
    },
    {
      "id": "C19",
      "name": "DIAD",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Diisopropyl azodicarboxylate; azo component of the Mitsunobu reagent system used in the synthesis of S-9."
    },
    {
      "id": "C20",
      "name": "S-9 (tert-butyl 3-((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)oxy)pyrrolidine-1-carboxylate)",
      "iupac_name": "tert-Butyl 3-((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)oxy)pyrrolidine-1-carboxylate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H-Boc]+ 344.1",
      "ms_calculated_exact_mass": null,
      "description": "Boc-protected pomalidomide-pyrrolidine ether intermediate; synthesized by Mitsunobu coupling of S-7 and S-8, then used after Boc deprotection in the synthesis of compound 17."
    },
    {
      "id": "C21",
      "name": "HCl (4N in 1,4-dioxane)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Hydrogen chloride solution used to remove the Boc protecting group from S-9 to generate the pyrrolidine HCl salt for coupling."
    },
    {
      "id": "C22",
      "name": "2-(2,6-dioxopiperidin-3-yl)-4-(pyrrolidin-3-yloxy)isoindoline-1,3-dione HCl salt",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Boc-deprotected pyrrolidine HCl salt obtained from S-9 by treatment with HCl/dioxane; used directly as the amine component in TBTU-mediated coupling to give compound 17."
    },
    {
      "id": "C23",
      "name": "compound 17",
      "iupac_name": "4-((1-(2-((6S)-4-(4-Chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)acetyl)pyrrolidin-3-yl)oxy)-2-(2,6-dioxopiperidin-3-yl)isoindoline-1,3-dione",
      "molecular_formula": "C36H32ClN7O6S",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 726.1890",
      "ms_calculated_exact_mass": 726.1896,
      "description": "CRBN-directed PROTAC (BRD4 POI ligand JQ-1 + pomalidomide CRBN ligand, pyrrolidine ether ring linker); synthesized in two steps from S-9 via Boc deprotection and TBTU coupling with JQ-1 carboxylic acid; isolated as a 2:3 mixture of diastereoisomers."
    },
    {
      "id": "C24",
      "name": "sodium sulfate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Drying agent used in workup of reactions for compounds 11–17 and S-9."
    },
    {
      "id": "C25",
      "name": "NaHCO3 saturated aqueous solution",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Aqueous wash reagent used in workup of reactions for compounds 11–17."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of compound 11 (VHL-PROTAC, JQ-1 + S-1, alkane linker)",
      "source_section": "main_text",
      "target_compound_id": "C05",
      "target_compound_name": "compound 11",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide bond formation (TBTU-mediated coupling)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C04",
              "name": "S-1",
              "amount": "13 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C03",
              "name": "DIPEA",
              "amount": "17 µL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "30 min pre-activation of acid with TBTU, then 2 h after S-1 addition",
            "atmosphere": null,
            "ph": null,
            "other": "S-1 added 30 min after initial mixing of acid, TBTU and DIPEA; workup: dilute with EtOAc, wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C05",
            "name": "compound 11",
            "yield": "16 mg (70%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.739
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": "S-1 structure is visible in SI scheme S28 but its own synthesis/sourcing procedure is not provided in any available document."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of compound 12 (CRBN-PROTAC, JQ-1 + S-2, cyclohexane ring linker)",
      "source_section": "main_text",
      "target_compound_id": "C07",
      "target_compound_name": "compound 12",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide bond formation (TBTU-mediated coupling)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C06",
              "name": "S-2",
              "amount": "9.9 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C03",
              "name": "DIPEA",
              "amount": "17 µL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "Workup: dilute with EtOAc, wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C07",
            "name": "compound 12",
            "yield": "12.5 mg (65%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.988
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": "S-2 structure is visible in SI scheme S28 but its own synthesis/sourcing procedure is not provided in any available document."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Synthesis of compound 13 (CRBN-PROTAC, JQ-1 + S-3, short propyl linker)",
      "source_section": "main_text",
      "target_compound_id": "C09",
      "target_compound_name": "compound 13",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide bond formation (TBTU-mediated coupling)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C08",
              "name": "S-3",
              "amount": "8.2 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C03",
              "name": "DIPEA",
              "amount": "17 µL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "Workup: dilute with EtOAc, wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C09",
            "name": "compound 13",
            "yield": "10.7 mg (60%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.698
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": "S-3 structure is visible in SI scheme S28 but its own synthesis/sourcing procedure is not provided in any available document."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Synthesis of compound 14 (CRBN-PROTAC, JQ-1 + S-4, long PEG linker)",
      "source_section": "main_text",
      "target_compound_id": "C11",
      "target_compound_name": "compound 14",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide bond formation (TBTU-mediated coupling)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C10",
              "name": "S-4",
              "amount": "12 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C03",
              "name": "DIPEA",
              "amount": "17 µL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "Workup: dilute with EtOAc, wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C11",
            "name": "compound 14",
            "yield": "16 mg (76%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.596
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": "S-4 structure is visible in SI scheme S28 but its own synthesis/sourcing procedure is not provided in any available document."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Synthesis of compound 15 (CRBN-PROTAC, JQ-1 + S-5, piperazine ring linker)",
      "source_section": "main_text",
      "target_compound_id": "C13",
      "target_compound_name": "compound 15",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide bond formation (TBTU-mediated coupling)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C12",
              "name": "S-5",
              "amount": "8.5 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C03",
              "name": "DIPEA",
              "amount": "17 µL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "Workup: dilute with EtOAc, wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C13",
            "name": "compound 15",
            "yield": "9.9 mg (55%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.744
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": "S-5 structure is visible in SI scheme S28 but its own synthesis/sourcing procedure is not provided in any available document."
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Synthesis of compound 16 (CRBN-PROTAC, JQ-1 + S-6, shorter PEG linker)",
      "source_section": "main_text",
      "target_compound_id": "C15",
      "target_compound_name": "compound 16",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide bond formation (TBTU-mediated coupling)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C14",
              "name": "S-6",
              "amount": "10 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C03",
              "name": "DIPEA",
              "amount": "17 µL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "Workup: dilute with EtOAc, wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C15",
            "name": "compound 16",
            "yield": "13 mg (65%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.585
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": "S-6 structure is visible in SI scheme S28 but its own synthesis/sourcing procedure is not provided in any available document."
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Synthesis of S-9 (Boc-protected pomalidomide-pyrrolidine ether intermediate)",
      "source_section": "main_text",
      "target_compound_id": "C20",
      "target_compound_name": "S-9 (tert-butyl 3-((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)oxy)pyrrolidine-1-carboxylate)",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Mitsunobu reaction (O-alkylation)",
          "reactants": [
            {
              "compound_id": "C16",
              "name": "S-7 (2-(2,6-dioxopiperidin-3-yl)-4-hydroxyisoindoline-1,3-dione)",
              "amount": "250 mg (0.91 mmol)"
            },
            {
              "compound_id": "C17",
              "name": "S-8 (tert-butyl 3-hydroxypyrrolidine-1-carboxylate)",
              "amount": "162 mg (0.87 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C18",
              "name": "triphenylphosphine",
              "amount": "526 mg (2 mmol)",
              "role": "other"
            },
            {
              "compound_id": "C19",
              "name": "DIAD",
              "amount": "358 µL",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "10 mL (+ 6 mL for DIAD dilution)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "DIAD diluted in THF (6 mL) and added dropwise; workup: dilute with EtOAc, wash with water, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C20",
            "name": "S-9 (tert-butyl 3-((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)oxy)pyrrolidine-1-carboxylate)",
            "yield": "200 mg (50%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "automated flash chromatography, 40 g silica cartridge, iso-Hexane/EtOAc 1:3",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P8",
      "pathway_name": "Synthesis of compound 17 (CRBN-PROTAC, JQ-1 + pyrrolidine ether, ring linker)",
      "source_section": "main_text",
      "target_compound_id": "C23",
      "target_compound_name": "compound 17",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Boc deprotection (acid-mediated)",
          "reactants": [
            {
              "compound_id": "C20",
              "name": "S-9",
              "amount": "200 mg (0.45 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C21",
              "name": "HCl (4N in 1,4-dioxane)",
              "amount": "6 mL (24 mmol)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "1,4-dioxane",
              "volume": "4 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": "3 h",
            "atmosphere": null,
            "ph": null,
            "other": "Heterogeneous solution diluted with iso-hexane and filtered through P3 glass-silica pad; white solid dried under vacuum."
          },
          "product": {
            "compound_id": "C22",
            "name": "2-(2,6-dioxopiperidin-3-yl)-4-(pyrrolidin-3-yloxy)isoindoline-1,3-dione HCl salt",
            "yield": "140 mg (94%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "filtration through P3 glass-silica pad, washed with iso-hexane",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "amide bond formation (TBTU-mediated coupling)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C22",
              "name": "2-(2,6-dioxopiperidin-3-yl)-4-(pyrrolidin-3-yloxy)isoindoline-1,3-dione HCl salt",
              "amount": "8.6 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C03",
              "name": "DIPEA",
              "amount": "17 µL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "Workup: dilute with EtOAc, wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C23",
            "name": "compound 17",
            "yield": "13.5 mg (75%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.674
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": "Isolated as a 2:3 mixture of diastereoisomers; NMR and HRMS data reported separately for major and minor diastereoisomers."
        }
      ]
    }
  ]
}
```
##### Attempt 2
```
{
  "extraction": {
    "prompt_version": "v3.2",
    "extraction_date": "2026-03-31",
    "model_name": "claude-sonnet-4-20250514",
    "extractor_notes": "SI found: jm5c01499_si_001.pdf (Supporting Information for the main article). SI schemes identified: Reaction schemes for compounds 11–17 (one combined scheme page, S28), showing synthesis routes for all seven target compounds. SI compounds identified by author label: S-1, S-2, S-3, S-4, S-5, S-6, S-7, S-8, S-9. Total pathway count: 8 (P1 = compound 11, P2 = compound 12, P3 = compound 13, P4 = compound 14, P5 = compound 15, P6 = compound 16, P7 = compound 17 via two steps including S-9, P8 = S-9). Excluded reference compounds (no synthetic role in this study; sourced commercially for biological testing only): compounds 1–10 (commercial PROTACs obtained from Tocris for membrane affinity and Caco-2 assays). JQ-1 carboxylic acid is used as a reactant in every coupling step and receives a single compound ID. SI compounds S-1 through S-8 are amine linker/E3 ligand precursors used as reactants; their structures are shown in the SI scheme but no full experimental procedures (amounts, conditions) for their own synthesis are provided in either document — they appear to be commercially sourced or custom-ordered external materials. S-9 is synthesised in-house with a full procedure given in the main text. Mass data: all compounds are small molecules (<1000 Da); monoisotopic exact masses are used (HRMS, QTOF, ESI+, [M+H]+). S-9 has only LC-MS nominal mass reported."
  },

  "paper": {
    "title": "Conformational Dynamics in the Cell Membrane Interactions of Bispecific Targeted Degrader Therapeutics",
    "authors": [
      "Emma Inganäs",
      "Hanna Lavén",
      "Rémi Caraballo",
      "Fredrik Klingegård",
      "MyLan Eklund",
      "Linda Andersson",
      "Constanze Hilgendorf",
      "Pär Matsson"
    ],
    "doi": "10.1021/acs.jmedchem.5c01499",
    "journal": "Journal of Medicinal Chemistry",
    "year": 2025,
    "synthesis_scale": "lab",
    "method_completeness": "full",
    "has_synthesis": true,
    "extraction_notes": "Compounds 11–17 are newly synthesised PROTACs. S-9 is a newly synthesised Boc-protected intermediate. S-1 through S-8 are amine/linker building blocks used as reactants but no synthetic procedures for them are provided; they are treated as externally sourced starting materials. JQ-1 carboxylic acid is a commercially available BET bromodomain inhibitor carboxylic acid used as the POI ligand acid partner in all couplings."
  },

  "compounds": [
    {
      "id": "C01",
      "name": "JQ-1 carboxylic acid",
      "iupac_name": "(S)-2-(4-(4-chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)acetic acid",
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Commercially sourced BET bromodomain POI ligand carboxylic acid used as the acid coupling partner in all amide bond-forming reactions to produce compounds 11–17."
    },
    {
      "id": "C02",
      "name": "TBTU",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "O-(Benzotriazol-1-yl)-N,N,N',N'-tetramethyluronium tetrafluoroborate; amide coupling reagent used in all coupling reactions to produce compounds 11–17."
    },
    {
      "id": "C03",
      "name": "DIPEA",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "N,N-diisopropylethylamine; base used in all amide coupling reactions to produce compounds 11–17."
    },
    {
      "id": "C04",
      "name": "S-1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial or custom-ordered",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "VHL E3 ligand amine building block (author label S-1) used as amine coupling partner to produce compound 11; structure shown in SI scheme S28 but no synthesis procedure provided."
    },
    {
      "id": "C05",
      "name": "compound 11 — (2S,4R)-1-((2S)-2-(5-(2-((6S)-4-(4-Chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)acetamido)pentanamido)-3,3-dimethylbutanoyl)-4-hydroxy-N-(4-(4-methylthiazol-5-yl)benzyl)pyrrolidine-2-carboxamide",
      "iupac_name": "(2S,4R)-1-((2S)-2-(5-(2-((6S)-4-(4-chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)acetamido)pentanamido)-3,3-dimethylbutanoyl)-4-hydroxy-N-(4-(4-methylthiazol-5-yl)benzyl)pyrrolidine-2-carboxamide",
      "molecular_formula": "C46H54ClN9O5S2",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 912.3447",
      "ms_calculated_exact_mass": 912.3451,
      "description": "VHL-directed PROTAC synthesised by TBTU-mediated amide coupling of JQ-1 carboxylic acid with amine S-1; used to study membrane affinity."
    },
    {
      "id": "C06",
      "name": "S-2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial or custom-ordered",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "CRBN E3 ligand amine building block (author label S-2; cyclohexyl-methylene linked pomalidomide amine) used as amine coupling partner to produce compound 12; structure shown in SI scheme S28 but no synthesis procedure provided."
    },
    {
      "id": "C07",
      "name": "compound 12 — 2-((6S)-4-(4-Chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)-N-(((1RS,3SR)-3-(((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)amino)methyl)cyclohexyl)methyl)acetamide",
      "iupac_name": null,
      "molecular_formula": "C40H41ClN8O5S",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 781.2677",
      "ms_calculated_exact_mass": 781.2682,
      "description": "CRBN-directed PROTAC synthesised by TBTU-mediated amide coupling of JQ-1 carboxylic acid with amine S-2; used to study membrane affinity."
    },
    {
      "id": "C08",
      "name": "S-3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial or custom-ordered",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "CRBN E3 ligand amine building block (author label S-3; propyl-linked pomalidomide amine) used as amine coupling partner to produce compound 13; structure shown in SI scheme S28 but no synthesis procedure provided."
    },
    {
      "id": "C09",
      "name": "compound 13 — 2-((6S)-4-(4-Chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)-N-(3-((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)amino)propyl)acetamide",
      "iupac_name": null,
      "molecular_formula": "C35H33ClN8O5S",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 713.2052",
      "ms_calculated_exact_mass": 713.2056,
      "description": "CRBN-directed PROTAC with short propyl linker synthesised by TBTU-mediated amide coupling of JQ-1 carboxylic acid with amine S-3; used to study membrane affinity."
    },
    {
      "id": "C10",
      "name": "S-4",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial or custom-ordered",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "CRBN E3 ligand amine building block (author label S-4; PEG-linked thalidomide amine) used as amine coupling partner to produce compound 14; structure shown in SI scheme S28 but no synthesis procedure provided."
    },
    {
      "id": "C11",
      "name": "compound 14 — 2-((6S)-4-(4-Chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)-N-(2-(2-(2-(2-((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)oxy)acetamido)ethoxy)ethoxy)ethyl)acetamide",
      "iupac_name": null,
      "molecular_formula": "C40H41ClN8O9S",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 845.2475",
      "ms_calculated_exact_mass": 845.2479,
      "description": "CRBN-directed PROTAC with long PEG linker synthesised by TBTU-mediated amide coupling of JQ-1 carboxylic acid with amine S-4; used to study membrane affinity."
    },
    {
      "id": "C12",
      "name": "S-5",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial or custom-ordered",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "CRBN E3 ligand amine building block (author label S-5; piperazine-linked pomalidomide amine) used as amine coupling partner to produce compound 15; structure shown in SI scheme S28 but no synthesis procedure provided."
    },
    {
      "id": "C13",
      "name": "compound 15 — 4-(4-(2-((6S)-4-(4-Chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)acetyl)piperazin-1-yl)-2-(2,6-dioxopiperidin-3-yl)isoindoline-1,3-dione",
      "iupac_name": null,
      "molecular_formula": "C36H33ClN8O5S",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 725.2054",
      "ms_calculated_exact_mass": 725.2056,
      "description": "CRBN-directed PROTAC with piperazine ring linker synthesised by TBTU-mediated amide coupling of JQ-1 carboxylic acid with amine S-5; used to study membrane affinity."
    },
    {
      "id": "C14",
      "name": "S-6",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial or custom-ordered",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "CRBN E3 ligand amine building block (author label S-6; shorter PEG-linked thalidomide amine) used as amine coupling partner to produce compound 16; structure shown in SI scheme S28 but no synthesis procedure provided."
    },
    {
      "id": "C15",
      "name": "compound 16 — 2-((6S)-4-(4-Chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)-N-(2-(2-(2-((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)oxy)acetamido)ethoxy)ethyl)acetamide",
      "iupac_name": null,
      "molecular_formula": "C38H37ClN8O8S",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 801.2215",
      "ms_calculated_exact_mass": 801.2217,
      "description": "CRBN-directed PROTAC with shorter PEG linker synthesised by TBTU-mediated amide coupling of JQ-1 carboxylic acid with amine S-6; used to study membrane affinity."
    },
    {
      "id": "C16",
      "name": "S-7 — 2-(2,6-dioxopiperidin-3-yl)-4-hydroxyisoindoline-1,3-dione",
      "iupac_name": "2-(2,6-dioxopiperidin-3-yl)-4-hydroxyisoindoline-1,3-dione",
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Hydroxy-thalidomide analogue (pomalidomide phenol; author label S-7) used as the phenol substrate in the Mitsunobu reaction to synthesise S-9."
    },
    {
      "id": "C17",
      "name": "S-8 — tert-butyl 3-hydroxypyrrolidine-1-carboxylate",
      "iupac_name": "tert-butyl 3-hydroxypyrrolidine-1-carboxylate",
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Boc-protected 3-hydroxypyrrolidine (author label S-8) used as the alcohol nucleophile in the Mitsunobu reaction to synthesise S-9."
    },
    {
      "id": "C18",
      "name": "triphenylphosphine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Phosphine reagent used in the Mitsunobu reaction to form S-9."
    },
    {
      "id": "C19",
      "name": "DIAD",
      "iupac_name": "diisopropyl azodicarboxylate",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Azo reagent used in the Mitsunobu reaction to form S-9."
    },
    {
      "id": "C20",
      "name": "S-9 — tert-butyl 3-((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)oxy)pyrrolidine-1-carboxylate",
      "iupac_name": "tert-butyl 3-((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)oxy)pyrrolidine-1-carboxylate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H-Boc]+ 344.1",
      "ms_calculated_exact_mass": null,
      "description": "Boc-protected pyrrolidine-thalidomide Mitsunobu adduct (author label S-9) synthesised in-house; used as intermediate for compound 17 after Boc deprotection."
    },
    {
      "id": "C21",
      "name": "HCl in 1,4-dioxane (4N)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "4 N hydrochloric acid in 1,4-dioxane used for Boc deprotection of S-9 to give the HCl salt of the pyrrolidine amine."
    },
    {
      "id": "C22",
      "name": "2-(2,6-dioxopiperidin-3-yl)-4-(pyrrolidin-3-yloxy)isoindoline-1,3-dione HCl salt",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "HCl salt of the Boc-deprotected pyrrolidine amine intermediate, produced from S-9; used directly as amine coupling partner in the synthesis of compound 17."
    },
    {
      "id": "C23",
      "name": "compound 17 — 4-((1-(2-((6S)-4-(4-Chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)acetyl)pyrrolidin-3-yl)oxy)-2-(2,6-dioxopiperidin-3-yl)isoindoline-1,3-dione",
      "iupac_name": null,
      "molecular_formula": "C36H32ClN7O6S",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 726.1890",
      "ms_calculated_exact_mass": 726.1896,
      "description": "CRBN-directed PROTAC with pyrrolidine-ether ring linker synthesised by TBTU-mediated amide coupling of JQ-1 carboxylic acid with the deprotected pyrrolidine amine C22; isolated as a 2:3 mixture of diastereoisomers."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of compound 11 (VHL-directed PROTAC)",
      "source_section": "main_text",
      "target_compound_id": "C05",
      "target_compound_name": "compound 11",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide bond formation (TBTU-mediated coupling)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C03",
              "name": "DIPEA",
              "amount": "17 μL (0.1 mmol)",
              "role": "base"
            },
            {
              "compound_id": "C04",
              "name": "S-1",
              "amount": "13 mg (0.025 mmol)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "30 min pre-activation, then 2 h after S-1 addition",
            "atmosphere": null,
            "ph": null,
            "other": "DIPEA and TBTU added first; S-1 added after 30 min; workup: dilute with EtOAc, wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C05",
            "name": "compound 11",
            "yield": "16 mg (70%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.739
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of compound 12 (CRBN-directed PROTAC, cyclohexyl linker)",
      "source_section": "main_text",
      "target_compound_id": "C07",
      "target_compound_name": "compound 12",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide bond formation (TBTU-mediated coupling)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C06",
              "name": "S-2",
              "amount": "9.9 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C03",
              "name": "DIPEA",
              "amount": "17 μL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "Workup: dilute with EtOAc, wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C07",
            "name": "compound 12",
            "yield": "12.5 mg (65%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.988
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Synthesis of compound 13 (CRBN-directed PROTAC, propyl linker)",
      "source_section": "main_text",
      "target_compound_id": "C09",
      "target_compound_name": "compound 13",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide bond formation (TBTU-mediated coupling)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C08",
              "name": "S-3",
              "amount": "8.2 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C03",
              "name": "DIPEA",
              "amount": "17 μL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "Workup: dilute with EtOAc, wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C09",
            "name": "compound 13",
            "yield": "10.7 mg (60%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.698
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Synthesis of compound 14 (CRBN-directed PROTAC, long PEG linker)",
      "source_section": "main_text",
      "target_compound_id": "C11",
      "target_compound_name": "compound 14",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide bond formation (TBTU-mediated coupling)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C10",
              "name": "S-4",
              "amount": "12 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C03",
              "name": "DIPEA",
              "amount": "17 μL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "Workup: dilute with EtOAc, wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C11",
            "name": "compound 14",
            "yield": "16 mg (76%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.596
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Synthesis of compound 15 (CRBN-directed PROTAC, piperazine linker)",
      "source_section": "main_text",
      "target_compound_id": "C13",
      "target_compound_name": "compound 15",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide bond formation (TBTU-mediated coupling)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C12",
              "name": "S-5",
              "amount": "8.5 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C03",
              "name": "DIPEA",
              "amount": "17 μL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "Workup: dilute with EtOAc, wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C13",
            "name": "compound 15",
            "yield": "9.9 mg (55%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.744
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Synthesis of compound 16 (CRBN-directed PROTAC, short PEG linker)",
      "source_section": "main_text",
      "target_compound_id": "C15",
      "target_compound_name": "compound 16",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide bond formation (TBTU-mediated coupling)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C14",
              "name": "S-6",
              "amount": "10 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C03",
              "name": "DIPEA",
              "amount": "17 μL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "Workup: dilute with EtOAc, wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C15",
            "name": "compound 16",
            "yield": "13 mg (65%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.585
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Synthesis of S-9 (tert-butyl 3-((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)oxy)pyrrolidine-1-carboxylate)",
      "source_section": "main_text",
      "target_compound_id": "C20",
      "target_compound_name": "S-9",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Mitsunobu reaction",
          "reactants": [
            {
              "compound_id": "C16",
              "name": "S-7 — 2-(2,6-dioxopiperidin-3-yl)-4-hydroxyisoindoline-1,3-dione",
              "amount": "250 mg (0.91 mmol)"
            },
            {
              "compound_id": "C17",
              "name": "S-8 — tert-butyl 3-hydroxypyrrolidine-1-carboxylate",
              "amount": "162 mg (0.87 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C18",
              "name": "triphenylphosphine",
              "amount": "526 mg (2 mmol)",
              "role": "other"
            },
            {
              "compound_id": "C19",
              "name": "DIAD",
              "amount": "358 μL",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "10 mL (+ 6 mL for DIAD dilution)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "DIAD diluted in THF (6 mL) and added dropwise; workup: dilute with EtOAc, wash with water, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C20",
            "name": "S-9",
            "yield": "200 mg (50%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "automated flash chromatography, 40 g silica cartridge, iso-hexane/EtOAc 1:3",
          "notes": "LC-MS ESI+ m/z 344.1 [M+H-Boc]+ reported for S-9."
        }
      ]
    },
    {
      "pathway_id": "P8",
      "pathway_name": "Synthesis of compound 17 (CRBN-directed PROTAC, pyrrolidine-ether ring linker)",
      "source_section": "main_text",
      "target_compound_id": "C23",
      "target_compound_name": "compound 17",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Boc deprotection (HCl in dioxane)",
          "reactants": [
            {
              "compound_id": "C20",
              "name": "S-9",
              "amount": "200 mg (0.45 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C21",
              "name": "HCl (4N in 1,4-dioxane)",
              "amount": "6 mL (24 mmol)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "1,4-dioxane",
              "volume": "4 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": "3 h",
            "atmosphere": null,
            "ph": null,
            "other": "Heterogeneous solution diluted with iso-hexane and filtered through a P3 glass-silica pad; white solid dried under vacuum."
          },
          "product": {
            "compound_id": "C22",
            "name": "2-(2,6-dioxopiperidin-3-yl)-4-(pyrrolidin-3-yloxy)isoindoline-1,3-dione HCl salt",
            "yield": "140 mg (94%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "filtration through P3 glass-silica pad, washed with iso-hexane",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "amide bond formation (TBTU-mediated coupling)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C22",
              "name": "2-(2,6-dioxopiperidin-3-yl)-4-(pyrrolidin-3-yloxy)isoindoline-1,3-dione HCl salt",
              "amount": "8.6 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C03",
              "name": "DIPEA",
              "amount": "17 μL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "Workup: dilute with EtOAc, wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C23",
            "name": "compound 17",
            "yield": "13.5 mg (75%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.674
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": "Isolated as a mixture of diastereoisomers in a 2:3 ratio (major:minor); NMR data reported separately for each diastereoisomer in the main text."
        }
      ]
    }
  ]
}
```
##### Attempt 3
```
{
  "extraction": {
    "prompt_version": "v3.2",
    "extraction_date": "2026-03-31",
    "model_name": "claude-sonnet-4-20250514",
    "extractor_notes": "SI found: jm5c01499_si_001.pdf (Supporting Information document). SI schemes identified: Reaction schemes for compounds 11–17 (SI page S28), depicting one-step amide couplings of JQ-1 carboxylic acid with amine linkers S-1 through S-6 to give compounds 11–16, and a two-step sequence (Mitsunobu then Boc deprotection/amide coupling) for compound 17 via intermediate S-9. SI compounds identified by author labels: S-1 (amine linker, VHL E3 ligand fragment for compound 11), S-2 (amine linker for compound 12), S-3 (amine linker for compound 13), S-4 (amine linker for compound 14), S-5 (amine linker for compound 15), S-6 (amine linker for compound 16), S-7 (2-(2,6-dioxopiperidin-3-yl)-4-hydroxyisoindoline-1,3-dione), S-8 (tert-butyl 3-hydroxypyrrolidine-1-carboxylate), S-9 (tert-butyl 3-((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)oxy)pyrrolidine-1-carboxylate). Total pathway count: 8 (P1 through P8 — one each for compounds 11, 12, 13, 14, 15, 16, S-9, and 17). Excluded reference compounds (no synthetic role in this study, cited for comparison only or sourced as commercial PROTACs 1–10): compounds 1–10 as sourced commercial PROTACs from Tocris (these are used in biological/binding assays only, not synthesised or used as reactants). JQ-1 carboxylic acid is used as a reactant in all syntheses and is therefore in-scope as a starting material. Linker amines S-1 through S-6 are used as reactants but their individual synthesis procedures are not described in either the main text or SI — they are referenced only as named starting materials with amounts. Purity for all final products 11–17: >95% by LCMS (stated in General Chemistry Methods section). Mass type note: all reported masses are monoisotopic (HRMS/ESI+ from QTOF instrument)."
  },

  "paper": {
    "title": "Conformational Dynamics in the Cell Membrane Interactions of Bispecific Targeted Degrader Therapeutics",
    "authors": [
      "Emma Inganäs",
      "Hanna Lavén",
      "Rémi Caraballo",
      "Fredrik Klingegård",
      "MyLan Eklund",
      "Linda Andersson",
      "Constanze Hilgendorf",
      "Pär Matsson"
    ],
    "doi": "10.1021/acs.jmedchem.5c01499",
    "journal": "Journal of Medicinal Chemistry",
    "year": 2025,
    "synthesis_scale": "lab",
    "method_completeness": "full",
    "has_synthesis": true,
    "extraction_notes": "Compounds 11–17 synthesised in-house at SciLifeLab (Solna, Sweden). Amine linker starting materials S-1 through S-6 are commercially sourced or custom-ordered; their individual structures are depicted in the SI reaction scheme (page S28) but no synthesis procedure is provided for them. All final compounds assessed >95% pure by LCMS (UV at 254 and 305 nm)."
  },

  "compounds": [
    {
      "id": "C01",
      "name": "JQ-1 carboxylic acid",
      "iupac_name": "(S)-2-(4-(4-chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)acetic acid",
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "BET bromodomain ligand bearing a carboxylic acid handle, used as the common POI-ligand building block in amide coupling reactions to give compounds 11–17."
    },
    {
      "id": "C02",
      "name": "S-1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial or custom-ordered",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "VHL E3 ligand amine (13 mg, 0.025 mmol used), used as the amine coupling partner for synthesis of PROTAC 11; structure visible in SI reaction scheme page S28."
    },
    {
      "id": "C03",
      "name": "TBTU",
      "iupac_name": "O-(benzotriazol-1-yl)-N,N,N',N'-tetramethyluronium tetrafluoroborate",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amide coupling reagent used in all synthesis steps for compounds 11–17."
    },
    {
      "id": "C04",
      "name": "DIPEA",
      "iupac_name": "N,N-diisopropylethylamine",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Hindered amine base used in all amide coupling reactions for compounds 11–17."
    },
    {
      "id": "C05",
      "name": "Compound 11",
      "iupac_name": "(2S,4R)-1-((2S)-2-(5-(2-((6S)-4-(4-chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)acetamido)pentanamido)-3,3-dimethylbutanoyl)-4-hydroxy-N-(4-(4-methylthiazol-5-yl)benzyl)pyrrolidine-2-carboxamide",
      "molecular_formula": "C46H54ClN9O5S2",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 912.3447",
      "ms_calculated_exact_mass": 912.3451,
      "description": "VHL-directed PROTAC synthesised by TBTU-mediated amide coupling of JQ-1 carboxylic acid with amine S-1; used in cell membrane binding and Caco-2 permeability studies."
    },
    {
      "id": "C06",
      "name": "S-2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial or custom-ordered",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amine linker bearing a CRBN ligand fragment (9.9 mg, 0.025 mmol), used as coupling partner for synthesis of compound 12; structure shown in SI reaction scheme page S28."
    },
    {
      "id": "C07",
      "name": "Compound 12",
      "iupac_name": "2-((6S)-4-(4-chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)-N-(((1RS,3SR)-3-(((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)amino)methyl)cyclohexyl)methyl)acetamide",
      "molecular_formula": "C40H41ClN8O5S",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 781.2677",
      "ms_calculated_exact_mass": 781.2682,
      "description": "CRBN-directed PROTAC with cyclohexyl-containing linker, synthesised by TBTU-mediated amide coupling of JQ-1 carboxylic acid with amine S-2."
    },
    {
      "id": "C08",
      "name": "S-3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial or custom-ordered",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Amine linker bearing a CRBN ligand (8.2 mg, 0.025 mmol), coupling partner for synthesis of compound 13; structure shown in SI reaction scheme page S28."
    },
    {
      "id": "C09",
      "name": "Compound 13",
      "iupac_name": "2-((6S)-4-(4-chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)-N-(3-((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)amino)propyl)acetamide",
      "molecular_formula": "C35H33ClN8O5S",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 713.2052",
      "ms_calculated_exact_mass": 713.2056,
      "description": "CRBN-directed PROTAC with short propyl linker, synthesised by TBTU-mediated amide coupling of JQ-1 carboxylic acid with amine S-3."
    },
    {
      "id": "C10",
      "name": "S-4",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial or custom-ordered",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "PEG-containing amine linker with CRBN ligand fragment (12 mg, 0.025 mmol), coupling partner for synthesis of compound 14; structure shown in SI reaction scheme page S28."
    },
    {
      "id": "C11",
      "name": "Compound 14",
      "iupac_name": "2-((6S)-4-(4-chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)-N-(2-(2-(2-((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)oxy)acetamido)ethoxy)ethoxy)ethyl)acetamide",
      "molecular_formula": "C40H41ClN8O9S",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 845.2475",
      "ms_calculated_exact_mass": 845.2479,
      "description": "CRBN-directed PROTAC with long PEG-based linker (triethylene glycol), synthesised by TBTU coupling of JQ-1 carboxylic acid with amine S-4."
    },
    {
      "id": "C12",
      "name": "S-5",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial or custom-ordered",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Piperazine-containing CRBN ligand amine (8.5 mg, 0.025 mmol), coupling partner for synthesis of compound 15; structure shown in SI reaction scheme page S28."
    },
    {
      "id": "C13",
      "name": "Compound 15",
      "iupac_name": "4-(4-(2-((6S)-4-(4-chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)acetyl)piperazin-1-yl)-2-(2,6-dioxopiperidin-3-yl)isoindoline-1,3-dione",
      "molecular_formula": "C36H33ClN8O5S",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 725.2054",
      "ms_calculated_exact_mass": 725.2056,
      "description": "CRBN-directed PROTAC with piperazine ring linker, synthesised by TBTU coupling of JQ-1 carboxylic acid with amine S-5."
    },
    {
      "id": "C14",
      "name": "S-6",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial or custom-ordered",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "PEG-containing amine linker with CRBN ligand fragment (10 mg, 0.025 mmol), coupling partner for synthesis of compound 16; structure shown in SI reaction scheme page S28."
    },
    {
      "id": "C15",
      "name": "Compound 16",
      "iupac_name": "2-((6S)-4-(4-chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)-N-(2-(2-((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)oxy)acetamido)ethoxy)ethyl)acetamide",
      "molecular_formula": "C38H37ClN8O8S",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 801.2215",
      "ms_calculated_exact_mass": 801.2217,
      "description": "CRBN-directed PROTAC with shorter PEG linker (diethylene glycol), synthesised by TBTU coupling of JQ-1 carboxylic acid with amine S-6."
    },
    {
      "id": "C16",
      "name": "S-7 (2-(2,6-dioxopiperidin-3-yl)-4-hydroxyisoindoline-1,3-dione)",
      "iupac_name": "2-(2,6-dioxopiperidin-3-yl)-4-hydroxyisoindoline-1,3-dione",
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Hydroxyl-bearing pomalidomide analogue used as the electrophilic component in the Mitsunobu reaction to give intermediate S-9."
    },
    {
      "id": "C17",
      "name": "S-8 (tert-butyl 3-hydroxypyrrolidine-1-carboxylate)",
      "iupac_name": "tert-butyl 3-hydroxypyrrolidine-1-carboxylate",
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Boc-protected pyrrolinol used as the alcohol nucleophile in the Mitsunobu reaction to introduce the pyrrolidine ring onto the CRBN ligand in the synthesis of intermediate S-9."
    },
    {
      "id": "C18",
      "name": "Triphenylphosphine",
      "iupac_name": "triphenylphosphine",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu reagent (phosphine component) used in the synthesis of intermediate S-9."
    },
    {
      "id": "C19",
      "name": "DIAD",
      "iupac_name": "diisopropyl azodicarboxylate",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu reagent (azo component) used in the synthesis of intermediate S-9."
    },
    {
      "id": "C20",
      "name": "S-9 (tert-butyl 3-((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)oxy)pyrrolidine-1-carboxylate)",
      "iupac_name": "tert-butyl 3-((2-(2,6-dioxopiperidin-3-yl)-1,3-dioxoisoindolin-4-yl)oxy)pyrrolidine-1-carboxylate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+H-Boc]+ 344.1",
      "ms_calculated_exact_mass": null,
      "description": "Boc-protected pyrrolidine-CRBN ligand intermediate obtained by Mitsunobu coupling of S-7 and S-8; subsequently Boc-deprotected to give the HCl salt used in final coupling to form compound 17."
    },
    {
      "id": "C21",
      "name": "HCl (4N in 1,4-dioxane)",
      "iupac_name": "hydrogen chloride",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acid used for Boc deprotection of intermediate S-9 to give the pyrrolidine HCl salt prior to coupling with JQ-1 carboxylic acid."
    },
    {
      "id": "C22",
      "name": "2-(2,6-dioxopiperidin-3-yl)-4-(pyrrolidin-3-yloxy)isoindoline-1,3-dione HCl salt",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Boc-deprotected pyrrolidine-CRBN ligand HCl salt obtained from S-9; used directly as the amine coupling partner in the final step to give compound 17."
    },
    {
      "id": "C23",
      "name": "Compound 17",
      "iupac_name": "4-((1-(2-((6S)-4-(4-chlorophenyl)-2,3,9-trimethyl-6H-thieno[3,2-f][1,2,4]triazolo[4,3-a][1,4]diazepin-6-yl)acetyl)pyrrolidin-3-yl)oxy)-2-(2,6-dioxopiperidin-3-yl)isoindoline-1,3-dione",
      "molecular_formula": "C36H32ClN7O6S",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": ">95% by LCMS",
      "ms_observed": "[M+H]+ 726.1890",
      "ms_calculated_exact_mass": 726.1896,
      "description": "CRBN-directed PROTAC with pyrrolidine ring linker directly attached to the CRBN ligand via an ether bond; obtained as a 2:3 mixture of diastereoisomers from TBTU coupling of JQ-1 carboxylic acid with C22."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of compound 11",
      "source_section": "main_text",
      "target_compound_id": "C05",
      "target_compound_name": "Compound 11",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide coupling",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C02",
              "name": "S-1",
              "amount": "13 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C03",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": "17 µL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "30 min pre-activation, then 2 h after S-1 addition",
            "atmosphere": null,
            "ph": null,
            "other": "DIPEA and TBTU added to JQ-1 carboxylic acid first for 30 min, then S-1 added; workup with EtOAc wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C05",
            "name": "Compound 11",
            "yield": "16 mg (70%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.739
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of compound 12",
      "source_section": "main_text",
      "target_compound_id": "C07",
      "target_compound_name": "Compound 12",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide coupling",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C06",
              "name": "S-2",
              "amount": "9.9 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C03",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": "17 µL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "Workup with EtOAc wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C07",
            "name": "Compound 12",
            "yield": "12.5 mg (65%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.988
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Synthesis of compound 13",
      "source_section": "main_text",
      "target_compound_id": "C09",
      "target_compound_name": "Compound 13",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide coupling",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C08",
              "name": "S-3",
              "amount": "8.2 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C03",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": "17 µL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "Workup with EtOAc wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C09",
            "name": "Compound 13",
            "yield": "10.7 mg (60%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.698
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Synthesis of compound 14",
      "source_section": "main_text",
      "target_compound_id": "C11",
      "target_compound_name": "Compound 14",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide coupling",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C10",
              "name": "S-4",
              "amount": "12 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C03",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": "17 µL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "Workup with EtOAc wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C11",
            "name": "Compound 14",
            "yield": "16 mg (76%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.596
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Synthesis of compound 15",
      "source_section": "main_text",
      "target_compound_id": "C13",
      "target_compound_name": "Compound 15",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide coupling",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C12",
              "name": "S-5",
              "amount": "8.5 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C03",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": "17 µL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "Workup with EtOAc wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C13",
            "name": "Compound 15",
            "yield": "9.9 mg (55%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.744
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Synthesis of compound 16",
      "source_section": "main_text",
      "target_compound_id": "C15",
      "target_compound_name": "Compound 16",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide coupling",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C14",
              "name": "S-6",
              "amount": "10 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C03",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": "17 µL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "Workup with EtOAc wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C15",
            "name": "Compound 16",
            "yield": "13 mg (65%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.585
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Synthesis of S-9 (intermediate for compound 17)",
      "source_section": "main_text",
      "target_compound_id": "C20",
      "target_compound_name": "S-9",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Mitsunobu reaction",
          "reactants": [
            {
              "compound_id": "C16",
              "name": "S-7 (2-(2,6-dioxopiperidin-3-yl)-4-hydroxyisoindoline-1,3-dione)",
              "amount": "250 mg (0.91 mmol)"
            },
            {
              "compound_id": "C17",
              "name": "S-8 (tert-butyl 3-hydroxypyrrolidine-1-carboxylate)",
              "amount": "162 mg (0.87 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C18",
              "name": "triphenylphosphine",
              "amount": "526 mg (2 mmol)",
              "role": "other"
            },
            {
              "compound_id": "C19",
              "name": "DIAD",
              "amount": "358 µL",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "10 mL (reaction) + 6 mL (DIAD dilution)"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "DIAD diluted in THF (6 mL) added dropwise; workup with EtOAc wash with water, dry over Na2SO4, filter, concentrate."
          },
          "product": {
            "compound_id": "C20",
            "name": "S-9",
            "yield": "200 mg (50%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "automated flash chromatography, 40 g silica cartridge, iso-hexane/EtOAc 1:3",
          "notes": "LC-MS ESI+ m/z: 344.1 [M+H-Boc]+."
        }
      ]
    },
    {
      "pathway_id": "P8",
      "pathway_name": "Synthesis of compound 17",
      "source_section": "main_text",
      "target_compound_id": "C23",
      "target_compound_name": "Compound 17",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Boc deprotection",
          "reactants": [
            {
              "compound_id": "C20",
              "name": "S-9",
              "amount": "200 mg (0.45 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C21",
              "name": "HCl (4N in 1,4-dioxane)",
              "amount": "6 mL (24 mmol)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "1,4-dioxane",
              "volume": "4 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "3 h",
            "atmosphere": null,
            "ph": null,
            "other": "Heterogeneous solution diluted with iso-hexane and filtered through a P3 glass-silica pad; white solid dried under vacuum."
          },
          "product": {
            "compound_id": "C22",
            "name": "2-(2,6-dioxopiperidin-3-yl)-4-(pyrrolidin-3-yloxy)isoindoline-1,3-dione HCl salt",
            "yield": "140 mg (94%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "filtration through P3 glass-silica pad",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "amide coupling",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "JQ-1 carboxylic acid",
              "amount": "10 mg (0.025 mmol)"
            },
            {
              "compound_id": "C22",
              "name": "2-(2,6-dioxopiperidin-3-yl)-4-(pyrrolidin-3-yloxy)isoindoline-1,3-dione HCl salt",
              "amount": "8.6 mg (0.025 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C03",
              "name": "TBTU",
              "amount": "8.4 mg (0.026 mmol)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": "C04",
              "name": "DIPEA",
              "amount": "17 µL (0.1 mmol)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "0.5 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "overnight",
            "atmosphere": null,
            "ph": null,
            "other": "Workup with EtOAc wash with sat. aq. NaHCO3, dry over Na2SO4, filter, concentrate; product obtained as 2:3 mixture of diastereoisomers."
          },
          "product": {
            "compound_id": "C23",
            "name": "Compound 17",
            "yield": "13.5 mg (75%)",
            "purity": ">95% by LCMS",
            "hplc_retention_time_min": 2.674
          },
          "purification": "automated flash chromatography, 12 g silica cartridge, DCM/MeOH 0–10% over 7 column volumes",
          "notes": "Product isolated as a 2:3 mixture of diastereoisomers; NMR data reported separately for major and minor diastereoisomers in main text and SI."
        }
      ]
    }
  ]
}
```


# Evaluation 
After using Claude to evaluate, I found that Due to the SI, the accuracy reduce a little bit because it increase the detail. The most fatal error is the unit incorrectness. 
## Failure category 1 — Numerical transcription of units

**Root cause:** The prompt has no rule requiring the model to verify that derived values (mmol from mass/MW) are arithmetically consistent with reported values. The model copies text token-by-token without sanity-checking units.

|Observed error|Paper 1 instance|Why the prompt allows it|
|---|---|---|
|μL/μmol silently promoted to mL/mmol|Et₃N "124 mL, 893 mmol"; POCl₃ "13.9 mL, 149 mmol" — both are actually μL/μmol|RULE 8 says format amounts as "N unit (N unit)" but gives no instruction to verify the unit symbol. The model sees μL in the PDF text, loses the Greek prefix during tokenization, and emits mL. The prompt has no cross-check step.|
|Same error in substrate amount|S5 amount "99.2 mmol" — actually 99.2 μmol|Same root cause. No verification rule.|
|NaBH₄ stoichiometry nonsensical (0.22 mmol for 1.02 g)|Attempt 3 only; 1.02 g NaBH₄ = ~27 mmol, not 0.22 mmol|Prompt never asks the model to check: does mass / MW ≈ stated mmol? A single arithmetic gate would catch this.|

### FixAdd a mandatory arithmetic verification step

`RULE 8A — UNIT VERIFICATION (mandatory for every amount string)   For each amount "N mg (M mmol)" or "N µL (M µmol)", verify that N/MW ≈ M (±10%).   If inconsistent, flag in notes and use the value that is consistent with the paper text.   Pay special attention to µ (micro) prefix — μL and μmol must never be recorded as mL or mmol.`

## Failure category 2 — ms_calculated_exact_mass universally null

**Root cause:** The prompt instruction says "Record calculated exact mass only if explicitly stated in the paper." Papers routinely write "calcd for C₁₆H₂₅ClN₅O₇P [M+H]⁺ 488.1072; found 488.1072" — the calcd value IS explicitly stated, but the model puts it all into ms_observed and leaves ms_calculated_exact_mass null.

|Evidence|Prompt gap|
|---|---|
|All three attempts for both papers: ms_calculated_exact_mass = null for every compound despite papers consistently reporting "calcd … found …"|RULE 13 gives an example `[M+H]+ 616.2` for ms_observed but does not say where the "calcd" value goes. The model defaults to putting everything in ms_observed.|

### FixClarify the split between calcd and found

`RULE 13A — HRMS SPLIT   When paper reports "calcd for [formula] [ion] X.XXXX; found Y.YYYY":   ms_calculated_exact_mass = X.XXXX (the calculated value, as a number)   ms_observed = "[ion] Y.YYYY (found)" (the experimentally measured value)   Do NOT merge both into ms_observed.`

## Failure category 3 — Pathway count drift and structure

**Root cause:** RULE 14 says "each pathway targets exactly one compound" but does not define what happens when the same compound is reached via a linear sequence of steps that spans multiple author-labeled schemes. Attempt 3 of Paper 1 split compound 11's synthesis into two pathways (P1 = S1→S2, P2 = S2→11), creating an orphan pathway that doesn't reach a final product. The prompt has no rule against this.

|Observed error|Prompt gap|
|---|---|
|Attempt 3, Paper 1: 10 pathways instead of 9; P1 terminates at an intermediate (S2), not a final product|RULE 14 doesn't specify that target_compound_id must be a final_product or intermediate with clear downstream use. It doesn't prohibit pathways that terminate at intermediates.|
|Inconsistent pathway counts across attempts (8 vs 9 vs 10)|No rule requiring the model to count pathways before assigning IDs|

### FixClarify pathway termination rule

`RULE 14A — PATHWAY SCOPE   A pathway must terminate at a compound with role = final_product OR at a   named intermediate that is explicitly used in a subsequent, separately   numbered pathway. A pathway that ends at an intermediate only in order to   split the extraction is prohibited. When a paper's scheme shows a linear   A→B→C→D synthesis, use one pathway with multiple steps, not multiple pathways.`

## Failure category 4 — Purity over-assignment to intermediates

**Root cause:** Attempt 3 of Paper 1 assigns ">95% by HPLC" to all compounds including intermediates. The prompt says "Record null for absent data" but never explicitly says: do not inherit purity from a general statement that applies only to final products.

|Paper says|What happened|Prompt gap|
|---|---|---|
|"All final compounds were assessed to be >95% pure by HPLC analysis" (Paper 2)|Attempt 3, Paper 1: purity applied to S2 through S28 — all intermediates|RULE 3 says null for absent data but doesn't warn against propagating a scope-limited general statement to entities outside its scope|

### FixScope-limit purity inheritance

`RULE 12A — PURITY SCOPE   General purity statements (e.g. "all final compounds >95% pure") apply ONLY to   compounds with role = final_product. Do not propagate them to intermediates,   starting materials, or reagents. Record null for those unless a specific purity   measurement is stated for that compound individually.`

## Failure category 5 — Reactant vs. reagent misclassification

**Root cause:** RULE 5 defines roles for compounds (starting_material, reagent…) but the step-level arrays "reactants" and "reagents" have no analogous decision rule. The model must infer which array a compound belongs to from chemical knowledge, which it does inconsistently.

|Observed error|Prompt gap|
|---|---|
|Paper 2, Attempt 2: S-1 (amine coupling partner) placed in "reagents" array with role "other" instead of "reactants"|No rule defines what distinguishes a reactant (substrate, partner) from a reagent (consumable enabler) at the step level|

### FixAdd step-level classification rule

`RULE 17 — REACTANT vs. REAGENT IN STEPS   reactants[] = compounds that contribute atoms to the product (substrates, coupling partners).   reagents[] = compounds that enable the reaction but whose atoms do not appear in the product   (bases, coupling reagents, catalysts, oxidants, reducing agents, solvents).   Amide coupling partners (both acid and amine) are reactants, not reagents.   TBTU, HATU, EDC, DIC and similar coupling activators are reagents.`

## Failure category 6 — Order-of-addition / procedural detail loss

**Root cause:** RULE 9 defines step granularity by "physically distinct operation" but doesn't say to capture order-of-addition within a single step. The prompt's conditions.other field is "1 sentence max" — too restrictive for multi-component additions where sequence matters.

|Observed error|Impact|
|---|---|
|Paper 2 compound 11: 30 min pre-activation of JQ-1 acid with TBTU before S-1 addition not fully captured in attempts 2 and 3|The procedure is not reproducible from the extraction alone|
|Paper 1 compound 17: one-pot sequential phosphorylation → acetonide deprotection partially lost in some attempts|Step boundary ambiguity|

### FixExpand conditions.other and add order-of-addition

`RULE 11A — ORDER OF ADDITION   When the paper specifies that components are added sequentially (not simultaneously),   capture this in the step as follows:   - If a pre-activation or pre-mixing step involves the same vessel before the main   reaction begins, record it as a sub-note in conditions.other (up to 2 sentences).   - If a separate vessel or significant time gap separates operations, create a new step.   conditions.other may be up to 2 sentences when order-of-addition is critical to reproducibility.`

## Failure category 7 — Missing NMR characterization data

**Root cause:** The schema has no field for NMR data (solvent, frequency, chemical shifts). This is by design for a synthesis-focused extractor, but it means characterization data that helps confirm compound identity is systematically lost.

|Universally missing|Recommendation|
|---|---|
|NMR solvent (DMSO-d₆, CDCl₃, CD₃OD), spectrometer frequency (400 MHz), optical rotation ([α]D), IR, mp|Add optional characterization block OR document explicitly that these are out of scope|

### Design choiceEither add a characterization field or explicitly exclude it

`Option A — Add field to compound schema:   "characterization": {   "nmr_solvent": "string or null",   "nmr_frequency_mhz": "number or null",   "optical_rotation": "string or null",   "mp_celsius": "string or null",   "ir_cm_inv": "string or null"   }      Option B — Add to RULE 1 explicitly:   "NMR spectra, IR spectra, optical rotations, and melting points are OUT OF SCOPE.   Do not extract them even if present."`