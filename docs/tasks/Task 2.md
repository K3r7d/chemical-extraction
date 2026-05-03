# Continue working and prompting with LLMs

### Task
After giving me a new dataset with some result from expert Mahmoud, now I need to read the result that tested from Mahmoud. Then, from the experience that he tried, I will modify the prompt and test to ensure the reproducibility. 

### Reading Mahmoud Experiment result
There are 4 files of his experiment. after reading all of it, I can get some perspective that I need for my prompt:
- He always use article-only to make sure that LLM did hallucinate.
- Explicit negative cases in prompt
- Give clearly and completely Enum
- Controlled the vocabulary
### Prompt Engineering
Okay now I will start to improve my prompt, test it to observe what will happen. I will add Rules for the prompt for LLM to read it based on the experience I get from Mahmoud. Adding meta table for later relief in reviewing. Adding more enough vocabulary and enum for each feature will increase consistence in every time I use.
#### v2.0 prompt
```
SYSTEM ROLE
You are an expert chemist and scientific information extraction specialist with deep knowledge of organic, medicinal, and radiochemical synthesis. Your task is to extract chemical synthesis information from the academic paper provided below with maximum precision.

CRITICAL EXTRACTION RULES — read before answering:
1. ARTICLE-ONLY: Answer exclusively from information explicitly stated in the article (main text, schemes, figures, and experimental section). Do NOT supplement with prior chemical knowledge.
2. NOT REPORTED: If a field's value is absent from the article, use null — never invent plausible values.
3. NEGATIVE CASE: If the paper contains NO synthesis (e.g., drug repurposing, purely biological study), still return valid JSON with has_synthesis: false and all synthesis arrays empty.
4. YIELD FORMAT: Express yields as a string matching the paper exactly (e.g., "76%", "51–68%", ">95% RCP"). Use null if not stated.
5. AMOUNTS FORMAT: Express amounts exactly as written (e.g., "2 mmol", "0.312 g", "40 μg"). Use null if not stated.
6. ALL COMPOUNDS: Include ALL compounds — final products, intermediates, catalysts, co-ligands, and radiolabeled derivatives.
7. SUPPORTING INFO: If the paper references Supporting Information for experimental details, note this in the relevant step's "notes" field.

---

Return a single JSON object following this exact schema:

{
  "meta": {
    "prompt_version": "v2.0",
    "extraction_date": "[today's date]",
    "has_synthesis": true,
    "synthesis_scale": "lab | preclinical | gmp | none",
    "mechanism_discussed": "synthetic | biological_only | none",
    "method_completeness": "full | partial | referenced_to_SI | none",
    "extraction_notes": "string or null — flag any ambiguities, multi-paper analyses, or unusual features"
  },

  "paper": {
    "title": "string",
    "authors": ["string"],
    "doi": "string or null",
    "journal": "string or null",
    "year": "integer or null"
  },

  "compounds": [
    {
      "id": "C01",
      "name": "string — name as used in the paper",
      "iupac_name": "string or null — only if explicitly stated in the paper",
      "molecular_formula": "string or null — only if explicitly stated",
      "role": "starting_material | intermediate | reagent | catalyst | coligand | radiolabeled_product | final_product | reference_compound",
      "is_newly_synthesized": true,
      "description": "one sentence describing this compound's function in the synthesis"
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "string — e.g., 'Organic ligand synthesis (HA)', 'Radiolabeling (68Ga)'",
      "target_compound_id": "C01",
      "target_compound_name": "string",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "string or null — e.g., 'O-alkylation', 'amide coupling', 'SNAr', 'Suzuki-Miyaura', 'Boc deprotection', 'radiolabeling'",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "string",
              "amount": "string or null"
            }
          ],
          "reagents": [
            {
              "name": "string",
              "amount": "string or null",
              "role": "coupling_reagent | base | acid | oxidant | reductant | catalyst | protecting_group_reagent | other"
            }
          ],
          "solvents": [
            {
              "name": "string",
              "volume": "string or null"
            }
          ],
          "conditions": {
            "temperature": "string or null",
            "time": "string or null",
            "pressure": "string or null",
            "atmosphere": "string or null",
            "ph": "string or null",
            "other": "string or null"
          },
          "product": {
            "compound_id": "C02",
            "name": "string",
            "yield": "string or null",
            "purity": "string or null",
            "characterization": ["NMR", "HRMS", "HPLC"]
          },
          "purification": "string or null — e.g., 'silica gel chromatography', 'RP-HPLC', 'C18 Sep-Pak', 'recrystallization'",
          "notes": "string or null — flag if detail is in SI, if yield was not optimized, if step is iterative (SPPS), etc."
        }
      ]
    }
  ]
}
```

Now I will test it on some LLM to see what will happen

##### Gemini:
```
{
  "meta": {
    "prompt_version": "v2.0",
    "extraction_date": "2026-03-15",
    "has_synthesis": true,
    "synthesis_scale": "preclinical",
    "mechanism_discussed": "synthetic",
    "method_completeness": "referenced_to_SI",
    "extraction_notes": "The synthesis of DP1 and NP1 is detailed in the experimental section, while precursors PR7, DP2, DP3, and NP2 were custom synthesized. Detailed radiolabeling procedures are provided for both 68Ga and 18F-AlF complexation. Synthetic schemes and intermediate characterization are referenced to the Supporting Information."
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
    "year": 2025
  },
  "compounds": [
    {
      "id": "C01",
      "name": "PR7",
      "iupac_name": null,
      "molecular_formula": "C96H133N25O31",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "description": "Lead peptide-based probe used as the scaffold for modification and conjugation[cite: 638, 712]."
    },
    {
      "id": "C02",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "description": "Activated chelator used for conjugation to the peptide scaffold[cite: 700]."
    },
    {
      "id": "C03",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "description": "Activated chelator used for conjugation to the peptide scaffold[cite: 700]."
    },
    {
      "id": "C04",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "final_product",
      "is_newly_synthesized": true,
      "description": "Linear peptide conjugated with DOTA chelator[cite: 168, 707]."
    },
    {
      "id": "C05",
      "name": "NP1",
      "iupac_name": null,
      "molecular_formula": "C108H152N28O36",
      "role": "final_product",
      "is_newly_synthesized": true,
      "description": "Linear peptide conjugated with NOTA chelator[cite: 168, 708]."
    },
    {
      "id": "C06",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "description": "Cyclic peptide-based precursor with a DOTA chelator[cite: 168, 716]."
    },
    {
      "id": "C07",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "description": "Cyclic peptide-based precursor with a DOTA chelator and distinct linker[cite: 168, 717]."
    },
    {
      "id": "C08",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "description": "Cyclic peptide-based precursor with a NOTA chelator[cite: 168, 718]."
    },
    {
      "id": "C09",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "description": "Radiolabeled linear peptide probe for PET imaging of ROR1[cite: 21, 171]."
    },
    {
      "id": "C10",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "description": "Radiolabeled linear peptide probe for PET imaging of ROR1[cite: 21, 171]."
    }
  ],
  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of DP1 and NP1",
      "target_compound_id": "C04",
      "target_compound_name": "DP1/NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide coupling",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 μmol)"
            }
          ],
          "reagents": [
            {
              "name": "DOTA-NHS",
              "amount": "2.5 mg (5 μmol)",
              "role": "coupling_reagent"
            },
            {
              "name": "NOTA-NHS",
              "amount": "2 mg (5 μmol)",
              "role": "coupling_reagent"
            },
            {
              "name": "DIPEA",
              "amount": "20 μL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 μL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "12 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "agitated in an oscillator"
          },
          "product": {
            "compound_id": "C04",
            "name": "DP1",
            "yield": "55.6% (4.2 mg)",
            "purity": ">95%",
            "characterization": [
              "ESI-MS",
              "HPLC"
            ]
          },
          "purification": "semipreparative HPLC with UV detection at 254 nm",
          "notes": "Yield for NP1 was 3.9 mg (54%)[cite: 702]. Detailed synthetic routes for all precursors are in Schemes S1-S5 of SI[cite: 699]."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Radiolabeling with 68Ga",
      "target_compound_id": "C09",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "complexation",
          "reactants": [
            {
              "compound_id": "C04",
              "name": "DP1 (or DP2, DP3)",
              "amount": "50 μg (16-20 nmol)"
            },
            {
              "compound_id": null,
              "name": "68GaCl3",
              "amount": "0.74-1.11 GBq"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate",
              "amount": "0.5 mL (0.25 M)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "0.1 M HCl (aqueous)",
              "volume": "1 mL"
            },
            {
              "name": "DMSO",
              "volume": "50 μL"
            }
          ],
          "conditions": {
            "temperature": "95°C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": "4-4.5",
            "other": null
          },
          "product": {
            "compound_id": "C09",
            "name": "[68Ga]Ga-DP1",
            "yield": "89.55 ± 0.12%",
            "purity": ">90% RCP",
            "characterization": [
              "radio-HPLC"
            ]
          },
          "purification": "SepPak C18 cartridge elution with 1.5 mL ethanol",
          "notes": "RCY for [68Ga]Ga-DP2 was 7.67 ± 1.05%; for [68Ga]Ga-DP3 was 98.01 ± 0.97% [cite: 171, 726-728]."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Radiolabeling with 18F-AlF",
      "target_compound_id": "C10",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "complexation",
          "reactants": [
            {
              "compound_id": "C05",
              "name": "NP1 (or NP2)",
              "amount": "50 μg (18-25 nmol)"
            },
            {
              "compound_id": null,
              "name": "fluoride-18",
              "amount": "0.74-1.11 GBq"
            }
          ],
          "reagents": [
            {
              "name": "AlCl3",
              "amount": "3 μL (2 mM)",
              "role": "other"
            },
            {
              "name": "sodium acetate buffer",
              "amount": "100 μL (0.1 M)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": "200 μL"
            },
            {
              "name": "saline",
              "volume": "0.2 mL"
            }
          ],
          "conditions": {
            "temperature": "100°C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": "4.0",
            "other": null
          },
          "product": {
            "compound_id": "C10",
            "name": "[18F]AlF-NP1",
            "yield": "62.58 ± 0.32%",
            "purity": ">90% RCP",
            "characterization": [
              "radio-HPLC"
            ]
          },
          "purification": "SepPak C18 cartridge elution with 1.5 mL ethanol",
          "notes": "RCY for [18F]AlF-NP2 was 62.76 ± 0.22% [cite: 171, 729-731]."
        }
      ]
    }
  ]
}
```

##### ChatGPT:
```
{
  "meta": {
    "prompt_version": "v2.0",
    "extraction_date": "2026-03-15",
    "has_synthesis": true,
    "synthesis_scale": "preclinical",
    "mechanism_discussed": "biological_only",
    "method_completeness": "referenced_to_SI",
    "extraction_notes": "Detailed synthetic routes for peptide precursors are referenced to Schemes S1–S5 in the Supporting Information. Only the coupling reaction for DP1 and NP1 and the radiolabeling procedures are explicitly described in the main text. PR7, DP2, DP3, and NP2 were custom synthesized externally."
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
    "year": 2025
  },
  "compounds": [
    {
      "id": "C01",
      "name": "PR7",
      "iupac_name": null,
      "molecular_formula": "C96H133N25O31",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "description": "ROR1-targeting peptide used as the parent scaffold for modification and precursor synthesis."
    },
    {
      "id": "C02",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "description": "Chelator reagent used to conjugate DOTA to PR7 to produce the DP1 precursor."
    },
    {
      "id": "C03",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "description": "Chelator reagent used to conjugate NOTA to PR7 to produce the NP1 precursor."
    },
    {
      "id": "C04",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "description": "DOTA-conjugated PR7 peptide precursor used for 68Ga radiolabeling."
    },
    {
      "id": "C05",
      "name": "NP1",
      "iupac_name": null,
      "molecular_formula": "C108H152N28O36",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "description": "NOTA-conjugated PR7 peptide precursor used for Al18F radiolabeling."
    },
    {
      "id": "C06",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "description": "Peptide precursor synthesized externally and used for 68Ga radiolabeling."
    },
    {
      "id": "C07",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "description": "Peptide precursor synthesized externally and used for 68Ga radiolabeling."
    },
    {
      "id": "C08",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "description": "Peptide precursor synthesized externally and used for Al18F radiolabeling."
    },
    {
      "id": "C09",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "description": "Gallium-68 labeled ROR1-targeted peptide radiotracer derived from DP1."
    },
    {
      "id": "C10",
      "name": "[68Ga]Ga-DP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "description": "Gallium-68 labeled radiotracer derived from DP2."
    },
    {
      "id": "C11",
      "name": "[68Ga]Ga-DP3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "description": "Gallium-68 labeled radiotracer derived from DP3."
    },
    {
      "id": "C12",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "description": "Fluorine-18 aluminum fluoride labeled radiotracer derived from NP1."
    },
    {
      "id": "C13",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "description": "Fluorine-18 aluminum fluoride labeled radiotracer derived from NP2."
    }
  ],
  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Peptide precursor synthesis (DP1 and NP1)",
      "target_compound_id": "C04",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide coupling",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg, 3 μmol"
            }
          ],
          "reagents": [
            {
              "name": "DOTA-NHS",
              "amount": "2.5 mg, 5 μmol",
              "role": "coupling_reagent"
            },
            {
              "name": "DIPEA",
              "amount": "20 μL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 μL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "12 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "agitated in oscillator"
          },
          "product": {
            "compound_id": "C04",
            "name": "DP1",
            "yield": "55.6%",
            "purity": ">95%",
            "characterization": [
              "ESI-MS",
              "HPLC"
            ]
          },
          "purification": "semipreparative HPLC followed by lyophilization",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "amide coupling",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg, 3 μmol"
            }
          ],
          "reagents": [
            {
              "name": "NOTA-NHS",
              "amount": "2 mg, 5 μmol",
              "role": "coupling_reagent"
            },
            {
              "name": "DIPEA",
              "amount": "20 μL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 μL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "12 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "agitated in oscillator"
          },
          "product": {
            "compound_id": "C05",
            "name": "NP1",
            "yield": "54%",
            "purity": ">95%",
            "characterization": [
              "ESI-MS",
              "HPLC"
            ]
          },
          "purification": "semipreparative HPLC followed by lyophilization",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "68Ga radiolabeling",
      "target_compound_id": "C09",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "radiolabeling",
          "reactants": [
            {
              "compound_id": "C04",
              "name": "DP1",
              "amount": "50 μg, 16–20 nmol"
            }
          ],
          "reagents": [
            {
              "name": "68GaCl3",
              "amount": "0.74–1.11 GBq in 1 mL 0.1 M HCl",
              "role": "other"
            },
            {
              "name": "sodium acetate",
              "amount": "0.5 mL (0.25 M)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 μL"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": "C09",
            "name": "[68Ga]Ga-DP1",
            "yield": "89.55 ± 0.12%",
            "purity": ">95%",
            "characterization": [
              "radio-HPLC"
            ]
          },
          "purification": "SepPak C18 cartridge",
          "notes": "Same protocol used for DP2 and DP3 precursors."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "18F-AlF radiolabeling",
      "target_compound_id": "C12",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "radiolabeling",
          "reactants": [
            {
              "compound_id": "C05",
              "name": "NP1",
              "amount": "50 μg, 18–25 nmol"
            }
          ],
          "reagents": [
            {
              "name": "fluoride-18",
              "amount": "0.74–1.11 GBq",
              "role": "other"
            },
            {
              "name": "AlCl3",
              "amount": "3 μL of 2 mM solution",
              "role": "other"
            },
            {
              "name": "sodium acetate buffer",
              "amount": "100 μL (0.1 M, pH 4.0)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": "200 μL"
            },
            {
              "name": "DMSO",
              "volume": "50 μL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": "4.0",
            "other": null
          },
          "product": {
            "compound_id": "C12",
            "name": "[18F]AlF-NP1",
            "yield": "62.58 ± 0.32%",
            "purity": ">95%",
            "characterization": [
              "radio-HPLC"
            ]
          },
          "purification": "SepPak C18 cartridge",
          "notes": "Same procedure applied to NP2 precursor."
        }
      ]
    }
  ]
}
```

##### Claude:
```
{
  "meta": {
    "prompt_version": "v2.0",
    "extraction_date": "2026-03-15",
    "has_synthesis": true,
    "synthesis_scale": "preclinical",
    "mechanism_discussed": "synthetic",
    "method_completeness": "partial",
    "extraction_notes": "Detailed synthetic routes for DP2, DP3, NP2, and PR7 are in Supporting Information (Schemes S1–S5) and are not reproduced in the main text. Only DP1 and NP1 syntheses are described in the main experimental section. Radiochemical characteristics (RCY, molar activity) are summarized in Table S1 (SI). The paper states PR7, DP2, DP3, and NP2 were custom synthesized externally (Nanchang Tanzhen Biotechnology Co., Ltd.) and not synthesized in-house by the authors."
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
    "year": 2025
  },

  "compounds": [
    {
      "id": "C01",
      "name": "PR7",
      "iupac_name": null,
      "molecular_formula": "C96H133N25O31",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "description": "ROR1-targeting linear peptide lead compound used as the starting scaffold for chelator conjugation and as a blocking agent in specificity assays; custom synthesized externally."
    },
    {
      "id": "C02",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "description": "NHS ester-activated DOTA chelator used for conjugation to PR7 to produce DP1; custom synthesized externally."
    },
    {
      "id": "C03",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "description": "NHS ester-activated NOTA chelator used for conjugation to PR7 to produce NP1; custom synthesized externally."
    },
    {
      "id": "C04",
      "name": "DIPEA",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "description": "Base used in the amide coupling reaction for synthesis of DP1 and NP1."
    },
    {
      "id": "C05",
      "name": "DMSO",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "description": "Solvent used in the synthesis of DP1 and NP1 and as vehicle for precursor dissolution in radiolabeling steps."
    },
    {
      "id": "C06",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "final_product",
      "is_newly_synthesized": true,
      "description": "DOTA-conjugated linear ROR1-targeting peptide precursor prepared by coupling PR7 with DOTA-NHS; precursor for [68Ga]Ga-DP1 radiolabeling."
    },
    {
      "id": "C07",
      "name": "NP1",
      "iupac_name": null,
      "molecular_formula": "C108H152N28O36",
      "role": "final_product",
      "is_newly_synthesized": true,
      "description": "NOTA-conjugated linear ROR1-targeting peptide precursor prepared by coupling PR7 with NOTA-NHS; precursor for [18F]AlF-NP1 radiolabeling."
    },
    {
      "id": "C08",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "final_product",
      "is_newly_synthesized": false,
      "description": "DOTA-conjugated cyclic ROR1-targeting peptide precursor; custom synthesized externally, used as precursor for [68Ga]Ga-DP2."
    },
    {
      "id": "C09",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "final_product",
      "is_newly_synthesized": false,
      "description": "DOTA-conjugated cyclic ROR1-targeting peptide precursor; custom synthesized externally, used as precursor for [68Ga]Ga-DP3."
    },
    {
      "id": "C10",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "final_product",
      "is_newly_synthesized": false,
      "description": "NOTA-conjugated cyclic ROR1-targeting peptide precursor; custom synthesized externally, used as precursor for [18F]AlF-NP2."
    },
    {
      "id": "C11",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "description": "68Ga-radiolabeled DOTA-linear peptide radiotracer for PET imaging of ROR1 expression."
    },
    {
      "id": "C12",
      "name": "[68Ga]Ga-DP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "description": "68Ga-radiolabeled DOTA-cyclic peptide radiotracer for PET imaging of ROR1 expression."
    },
    {
      "id": "C13",
      "name": "[68Ga]Ga-DP3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "description": "68Ga-radiolabeled DOTA-cyclic peptide radiotracer for PET imaging of ROR1 expression."
    },
    {
      "id": "C14",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "description": "18F-labeled (via Al18F chelation) NOTA-linear peptide radiotracer for PET imaging of ROR1 expression."
    },
    {
      "id": "C15",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "description": "18F-labeled (via Al18F chelation) NOTA-cyclic peptide radiotracer for PET imaging of ROR1 expression."
    },
    {
      "id": "C16",
      "name": "68GaCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "description": "Gallium-68 chloride obtained from 68Ge/68Ga generator; radionuclide source for 68Ga radiolabeling."
    },
    {
      "id": "C17",
      "name": "Fluoride-18",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "description": "18F produced via 18O(p,n)18F reaction by cyclotron; radionuclide source for AlF radiolabeling."
    },
    {
      "id": "C18",
      "name": "AlCl3 (aluminum chloride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "description": "Aluminum chloride used to form the Al18F complex for 18F radiolabeling of NOTA-peptide precursors."
    },
    {
      "id": "C19",
      "name": "sodium acetate buffer",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "description": "Buffer used to adjust pH for both 68Ga and 18F radiolabeling reactions."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Chelator conjugation — synthesis of DP1",
      "target_compound_id": "C06",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide coupling (NHS ester conjugation)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg, 3 μmol"
            },
            {
              "compound_id": "C02",
              "name": "DOTA-NHS",
              "amount": "2.5 mg, 5 μmol"
            }
          ],
          "reagents": [
            {
              "name": "DIPEA",
              "amount": "20 μL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 μL"
            }
          ],
          "conditions": {
            "temperature": "room temperature (RT)",
            "time": "12 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "agitated in oscillator; reaction performed in a 2 mL centrifugation tube"
          },
          "product": {
            "compound_id": "C06",
            "name": "DP1",
            "yield": "4.2 mg (55.6%)",
            "purity": ">95% by HPLC",
            "characterization": ["ESI-MS", "HPLC"]
          },
          "purification": "semipreparative HPLC with UV detection at 254 nm; lyophilization",
          "notes": "ESI-MS m/z: calcd for C112H159N29O38, 2518.14; found [M+2H]2+ = 1260.54, [M+3H]3+ = 840.68. HPLC retention time: 11.230 min. HPLC method: 0.1% TFA in water (A) / 0.1% TFA in acetonitrile (B); 5% B to 95% B over 20 min at 1 mL/min."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Chelator conjugation — synthesis of NP1",
      "target_compound_id": "C07",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide coupling (NHS ester conjugation)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg, 3 μmol"
            },
            {
              "compound_id": "C03",
              "name": "NOTA-NHS",
              "amount": "2 mg, 5 μmol"
            }
          ],
          "reagents": [
            {
              "name": "DIPEA",
              "amount": "20 μL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 μL"
            }
          ],
          "conditions": {
            "temperature": "room temperature (RT)",
            "time": "12 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "agitated in oscillator; reaction performed in a 2 mL centrifugation tube"
          },
          "product": {
            "compound_id": "C07",
            "name": "NP1",
            "yield": "3.9 mg (54%)",
            "purity": ">95% by HPLC",
            "characterization": ["ESI-MS", "HPLC"]
          },
          "purification": "semipreparative HPLC with UV detection at 254 nm; lyophilization",
          "notes": "ESI-MS m/z: calcd for C108H152N28O36, 2417.09; found [M+2H]2+ = 1210.22, [M+3H]3+ = 807.00. HPLC retention time: 12.780 min. Same HPLC method as DP1."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "External custom synthesis — PR7, DP2, DP3, NP2",
      "target_compound_id": "C08",
      "target_compound_name": "DP2 (representative; also covers PR7, DP3, NP2)",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": null,
          "reactants": [],
          "reagents": [],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C08",
            "name": "PR7, DP2, DP3, NP2",
            "yield": null,
            "purity": ">95% by HPLC",
            "characterization": ["ESI-MS", "HPLC"]
          },
          "purification": null,
          "notes": "PR7, DP2, DP3, and NP2 were custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. Synthetic routes are in Schemes S1–S5 (Supporting Information) and not described in the main text. HPLC retention times: PR7 10.642 min, DP2 10.328 min, DP3 10.404 min, NP2 10.620 min. HPLC method: 0.1% TFA/water (A), 0.1% TFA/acetonitrile (B); 23% B to 43% B over 20 min at 1 mL/min. ESI-MS: PR7 C96H133N25O31 calcd 2131.96, found [M+2H]2+ = 1067.47; DP2 C122H174N32O41 calcd 2743.2514, found [M+2H]2+ = 1373.07, [M+3H]3+ = 915.72; DP3 C133H186N32O43S3 calcd 3015.2514, found [M+2H]2+ = 1509.05, [M+3H]3+ = 1006.39; NP2 C118H167N31O39 calcd 2642.20, found [M+2H]2+ = 1322.56."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Radiolabeling (68Ga) — [68Ga]Ga-DP1, [68Ga]Ga-DP2, [68Ga]Ga-DP3",
      "target_compound_id": "C11",
      "target_compound_name": "[68Ga]Ga-DP1 (representative; same method for DP2 and DP3)",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "radiolabeling (68Ga chelation with DOTA)",
          "reactants": [
            {
              "compound_id": "C16",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL, 0.74–1.11 GBq"
            },
            {
              "compound_id": "C06",
              "name": "precursor (DP1, DP2, or DP3)",
              "amount": "50 μg, 16–20 nmol, in 50 μL DMSO"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 μL (precursor vehicle)"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5 (68GaCl3–sodium acetate solution)",
            "other": "After heating, cooled to RT before purification"
          },
          "product": {
            "compound_id": "C11",
            "name": "[68Ga]Ga-DP1",
            "yield": "89.55 ± 0.12% RCY ([68Ga]Ga-DP1); 97.67 ± 1.05% ([68Ga]Ga-DP2); 98.01 ± 0.97% ([68Ga]Ga-DP3)",
            "purity": ">95% by radio-HPLC; >90% RCP",
            "characterization": ["radio-HPLC"]
          },
          "purification": "SepPak C18 cartridges (WAT020515, Waters) eluted with 1.5 mL ethanol",
          "notes": "Molar activities: [68Ga]Ga-DP1 14.37 ± 0.97 GBq/μmol; [68Ga]Ga-DP2 20.05 ± 1.35 GBq/μmol; [68Ga]Ga-DP3 14.09 ± 2.12 GBq/μmol (n ≥ 3). Radiochemical characteristics summarized in Table S1 (Supporting Information). Final product resolved in saline after ethanol evaporation."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Radiolabeling (18F via AlF method) — [18F]AlF-NP1, [18F]AlF-NP2",
      "target_compound_id": "C14",
      "target_compound_name": "[18F]AlF-NP1 (representative; same method for NP2)",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "18F trapping on QMA cartridge",
          "reactants": [
            {
              "compound_id": "C17",
              "name": "Fluoride-18",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline (for conditioning)",
              "volume": "10 mL"
            },
            {
              "name": "pure water (for conditioning)",
              "volume": "10 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water; 18F trapped and eluted with 0.2 mL saline"
          },
          "product": {
            "compound_id": "C17",
            "name": "18F in saline (trapped/eluted)",
            "yield": null,
            "purity": null,
            "characterization": []
          },
          "purification": null,
          "notes": "18F eluted with 0.2 mL saline into reaction vial."
        },
        {
          "step_number": 2,
          "reaction_type": "radiolabeling (Al18F chelation with NOTA)",
          "reactants": [
            {
              "compound_id": "C17",
              "name": "18F in saline",
              "amount": "0.2 mL saline eluate"
            },
            {
              "compound_id": "C07",
              "name": "precursor (NP1 or NP2)",
              "amount": "50 μg, 18–25 nmol, in 50 μL DMSO"
            },
            {
              "compound_id": "C18",
              "name": "AlCl3 (2 mM in sodium acetate buffer, 0.1 M, pH 4.0)",
              "amount": "3 μL"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "100 μL",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": "200 μL"
            },
            {
              "name": "DMSO",
              "volume": "50 μL (precursor vehicle)"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": "4.0",
            "other": "After heating, cooled to RT before purification; ethanol evaporated and final product resolved in saline"
          },
          "product": {
            "compound_id": "C14",
            "name": "[18F]AlF-NP1",
            "yield": "62.58 ± 0.32% RCY ([18F]AlF-NP1); 62.76 ± 0.22% ([18F]AlF-NP2)",
            "purity": ">95% by radio-HPLC",
            "characterization": ["radio-HPLC"]
          },
          "purification": "SepPak C18 cartridges eluted with 1.5 mL ethanol; ethanol evaporated and product resolved in saline",
          "notes": "Molar activities: [18F]AlF-NP1 13.13 ± 1.71 GBq/μmol; [18F]AlF-NP2 13.42 ± 1.25 GBq/μmol (n ≥ 3). Radiochemical characteristics summarized in Table S1 (Supporting Information). Radio-HPLC method: 0.1% TFA in water (A) / 0.1% TFA in acetonitrile (B); 5% B to 95% B at 20 min, flow rate 1 mL/min."
        }
      ]
    }
  ]
}
```

##### Observation
I created a full report [[Prompt v2.0 Evaluation Report]] about the comparison and observation.


#### v2.1 prompt
After reviewing all of that I come up with a new prompt
```
SYSTEM ROLE
You are an expert chemist and scientific information extraction specialist with deep knowledge of organic, medicinal, and radiochemical synthesis. Your task is to extract chemical synthesis information from the academic paper provided below with maximum precision.

CRITICAL EXTRACTION RULES — read before answering:

1. ARTICLE-ONLY: Extract exclusively from the version of the paper provided to you
   (main text, schemes, figures, experimental section). If the paper references
   Supporting Information for details not present in your input, record null for
   those fields and note the SI reference in the step's "notes" field
   (e.g. "Full synthetic route in Scheme S2, SI"). Do NOT supplement with
   prior chemical knowledge.

2. NOT REPORTED: If a field's value is absent from the article, use null —
   never invent plausible values.

3. NEGATIVE CASE: If the paper contains NO synthesis (e.g., drug repurposing,
   purely biological study), still return valid JSON with has_synthesis: false
   and all synthesis arrays empty.

4. YIELD FORMAT: Use "N mg (N%)" when both mass and percentage are stated;
   "N%" when only a percentage is given. For radiochemical yields, append the
   RCY suffix: "89.55 ± 0.12% RCY". ONE compound per yield string — never
   concatenate multiple compounds' data into a single yield field.

5. AMOUNTS FORMAT: Express amounts as "N unit (N unit)" for mass + moles
   (e.g. "6.4 mg (3 μmol)"). Use an en dash for ranges: "0.74–1.11 GBq".
   NEVER append solvent or concentration context into the amount string —
   those go in the solvents array or reagents list respectively.

6. ALL COMPOUNDS: Include ALL compounds — final products, intermediates,
   catalysts, co-ligands, and radiolabeled derivatives. Also promote to
   compound entries: radionuclide sources (68GaCl3, [18F]fluoride, etc.),
   key inorganic reagents with a defined mechanistic role (e.g. AlCl3 in
   AlF labeling), and any custom or commercial precursor named in the paper
   with a catalog or vendor reference.

7. SUPPORTING INFO: If the paper references Supporting Information for
   experimental details not in your input, note this in the relevant step's
   "notes" field.

8. STEP GRANULARITY: Each physically distinct operation that requires its
   own materials list should be a separate numbered step, even if the paper
   narrates them within a single paragraph. Indicator: if a sub-operation
   uses different equipment, reagents, or conditions from the preceding
   sub-operation, it is a separate step. Example: QMA cartridge 18F trapping
   and Al18F complexation are two steps, not one.

9. NO CITATION ARTIFACTS: All string values (especially "description") must
   be plain prose. Strip any citation tags, reference numbers, footnote
   markers, or retrieval-system metadata (e.g. [cite: N], [1], etc.).

10. TEMPERATURE: Use SI convention with a space between numeral and unit
    symbol: "95 °C", "−20 °C", "room temperature". Never "95°C".

11. PURITY: Always include the analytical method used: ">95% by HPLC" for
    precursors; ">95% RCP by radio-HPLC" for radiolabeled products.

12. ONE ENTRY PER COMPOUND: Each compound, radiolabeled product, and
    synthesis pathway must have its own entry. Never merge two distinct
    compounds or pathways into one entry using "or" / "alternatively" logic.

---

Return a single JSON object following this exact schema:

{
  "meta": {
    "prompt_version": "v2.1",
    "extraction_date": "[today's date]",
    "has_synthesis": true,
    "synthesis_scale": "lab | preclinical | gmp | none",
    "mechanism_discussed": "synthetic | biological_only | none",
    "method_completeness": "full | partial | referenced_to_SI | none",
    "extraction_notes": "string or null — flag ambiguities, SI references, multi-paper analyses, or unusual features"
  },

  "paper": {
    "title": "string",
    "authors": ["string"],
    "doi": "string or null",
    "journal": "string or null",
    "year": "integer or null"
  },

  "compounds": [
    {
      "id": "C01",
      "name": "string — name as used in the paper",
      "iupac_name": "string or null — only if explicitly stated in the paper",
      "molecular_formula": "string or null — only if explicitly stated",
      "role": "starting_material | intermediate | reagent | catalyst | coligand | radiolabeled_product | final_product | reference_compound",
      "is_newly_synthesized": true,
      "source": "string or null — 'in-house', 'commercial', 'custom_synthesis', or vendor name if explicitly stated in the paper",
      "physicochemical_properties": {
        "log_p": "string or null — e.g. '−2.19 ± 0.05'",
        "other": "string or null — any other physicochemical values stated in the paper"
      },
      "description": "one sentence of plain prose describing this compound's function in the synthesis — no citation tags or reference numbers"
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "string — e.g. 'Chelator conjugation — DP1', 'Radiolabeling (68Ga) — [68Ga]Ga-DP1'",
      "target_compound_id": "C01",
      "target_compound_name": "string",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "string or null — e.g. 'O-alkylation', 'amide coupling', 'NHS ester conjugation', 'SNAr', 'Suzuki-Miyaura', 'Boc deprotection', '68Ga chelation', 'Al18F complexation', 'QMA trapping'",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "string",
              "amount": "string or null — format: 'N mg (N μmol)' for mass+moles; 'N–N GBq' for radioactivity ranges; never append solvent context here"
            }
          ],
          "reagents": [
            {
              "name": "string",
              "amount": "string or null — format: 'N mL (N M, pH N)' for buffer solutions",
              "role": "coupling_reagent | base | acid | oxidant | reductant | catalyst | protecting_group_reagent | ph_adjuster | radionuclide_source | chelation_catalyst | other"
              // base          = organic amines only (DIPEA, TEA, etc.)
              // ph_adjuster   = inorganic buffers (sodium acetate, ammonium acetate)
              // radionuclide_source = 68GaCl3, [18F]fluoride, etc.
              // chelation_catalyst  = AlCl3 in AlF labeling contexts
            }
          ],
          "solvents": [
            {
              "name": "string",
              "volume": "string or null"
            }
          ],
          "conditions": {
            "temperature": "string or null — SI format with space: '95 °C', 'room temperature'",
            "time": "string or null",
            "pressure": "string or null",
            "atmosphere": "string or null",
            "ph": "string or null",
            "other": "string or null — reaction-phase details only: stirring mode, post-reaction cooling (e.g. 'cooled to RT before purification'), special handling. Vessel/equipment details go in 'notes'."
          },
          "product": {
            "compound_id": "C02",
            "name": "string",
            "yield": "string or null — 'N mg (N%)' when both stated; 'N% RCY' for radiochemical; one compound per string",
            "purity": "string or null — always include analytical method: '>95% by HPLC' or '>95% RCP by radio-HPLC'",
            "molar_activity": "string or null — radiolabeled products only; e.g. '14.37 ± 0.97 GBq/μmol'",
            "characterization": ["ESI-MS", "HPLC", "radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": "number or null — monoisotopic mass as stated in paper",
              "formula": "string or null",
              "observed_ions": [
                {
                  "adduct": "string — e.g. '[M+2H]2+', '[M+3H]3+'",
                  "mz": "number or null — observed m/z value"
                }
              ]
            },
            "hplc_retention_time_min": "number or null — retention time in minutes as stated"
          },
          "purification": "string or null — include: method, catalog number if given, elution solvent + volume, and any post-purification formulation steps (solvent removal, reconstitution). Example: 'SepPak C18 (WAT020515, Waters), 1.5 mL EtOH; EtOH evaporated under stream; product reconstituted in saline'",
          "notes": "string or null — flag if detail is in SI, if yield was not optimized, if step is iterative (e.g. SPPS), vessel/equipment details, or any other procedural context"
        }
      ]
    }
  ]
}
```

##### Gemini:
```
{
  "meta": {
    "prompt_version": "v2.1",
    "extraction_date": "2024-05-20",
    "has_synthesis": true,
    "synthesis_scale": "lab",
    "mechanism_discussed": "synthetic",
    "method_completeness": "referenced_to_SI",
    "extraction_notes": "Synthesis routes for custom-synthesized precursors (DP2, DP3, NP2) are referenced to the Supporting Information and not detailed in the main text. Details for DP1, NP1, and radiolabeling steps are fully extracted from the experimental section."
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
    "year": 2025
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
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.642 min"
      },
      "description": "A linear peptide used as a lead compound and precursor for targeted imaging probes."
    },
    {
      "id": "C02",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "An NHS-ester functionalized macrocyclic chelator used to conjugate DOTA to the PR7 peptide."
    },
    {
      "id": "C03",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "An NHS-ester functionalized macrocyclic chelator used to conjugate NOTA to the PR7 peptide."
    },
    {
      "id": "C04",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "A DOTA-conjugated linear peptide precursor synthesized for subsequent 68Ga radiolabeling."
    },
    {
      "id": "C05",
      "name": "NP1",
      "iupac_name": null,
      "molecular_formula": "C108H152N28O36",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "A NOTA-conjugated linear peptide precursor synthesized for subsequent 18F radiolabeling."
    },
    {
      "id": "C06",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.328 min"
      },
      "description": "A custom-synthesized cyclic peptide precursor featuring a DOTA chelator for 68Ga labeling."
    },
    {
      "id": "C07",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.404 min"
      },
      "description": "A custom-synthesized cyclic peptide precursor featuring a DOTA chelator for 68Ga labeling."
    },
    {
      "id": "C08",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.620 min"
      },
      "description": "A custom-synthesized cyclic peptide precursor featuring a NOTA chelator for 18F labeling."
    },
    {
      "id": "C09",
      "name": "68GaCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "ITM",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "A radioisotope source obtained from a 68Ge-68Ga generator."
    },
    {
      "id": "C10",
      "name": "[18F]fluoride",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Center for Molecular Imaging and Translational Medicine of Xiamen University",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "A positron-emitting radionuclide produced via the 18O(p,n)18F reaction."
    },
    {
      "id": "C11",
      "name": "AlCl3",
      "iupac_name": "aluminum trichloride",
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Used as a chelation metal catalyst to form the Al18F complex for NOTA conjugation."
    },
    {
      "id": "C12",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.19 ± 0.05",
        "other": null
      },
      "description": "A 68Ga-labeled linear peptide radiotracer targeting ROR1."
    },
    {
      "id": "C13",
      "name": "[68Ga]Ga-DP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.53 ± 0.04",
        "other": null
      },
      "description": "A 68Ga-labeled cyclic peptide radiotracer targeting ROR1."
    },
    {
      "id": "C14",
      "name": "[68Ga]Ga-DP3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−1.82 ± 0.03",
        "other": null
      },
      "description": "A 68Ga-labeled cyclic peptide radiotracer targeting ROR1 with high lipophilicity."
    },
    {
      "id": "C15",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.10 ± 0.04",
        "other": null
      },
      "description": "An 18F-labeled linear peptide radiotracer targeting ROR1 using aluminum fluoride chemistry."
    },
    {
      "id": "C16",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.54 ± 0.04",
        "other": null
      },
      "description": "An 18F-labeled cyclic peptide radiotracer targeting ROR1 using aluminum fluoride chemistry."
    }
  ],
  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Chelator conjugation — DP1",
      "target_compound_id": "C04",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester conjugation",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 μmol)"
            },
            {
              "compound_id": "C02",
              "name": "DOTA-NHS",
              "amount": "2.5 mg (5 μmol)"
            }
          ],
          "reagents": [
            {
              "name": "DIPEA",
              "amount": "20 μL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 μL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "12 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "agitated in an oscillator"
          },
          "product": {
            "compound_id": "C04",
            "name": "DP1",
            "yield": "4.2 mg (55.6%)",
            "purity": ">95% by HPLC",
            "molar_activity": null,
            "characterization": [
              "ESI-MS",
              "HPLC"
            ],
            "ms_data": {
              "calculated_exact_mass": 2518.14,
              "formula": "C112H159N29O38",
              "observed_ions": [
                {
                  "adduct": "[M+2H]2+",
                  "mz": 1260.54
                },
                {
                  "adduct": "[M+3H]3+",
                  "mz": 840.68
                }
              ]
            },
            "hplc_retention_time_min": 11.23
          },
          "purification": "Semipreparative HPLC with UV detection at 254 nm, followed by lyophilization",
          "notes": "Reaction performed in a 2 mL centrifugation tube."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Chelator conjugation — NP1",
      "target_compound_id": "C05",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester conjugation",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 μmol)"
            },
            {
              "compound_id": "C03",
              "name": "NOTA-NHS",
              "amount": "2 mg (5 μmol)"
            }
          ],
          "reagents": [
            {
              "name": "DIPEA",
              "amount": "20 μL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 μL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "12 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "agitated in an oscillator"
          },
          "product": {
            "compound_id": "C05",
            "name": "NP1",
            "yield": "3.9 mg (54%)",
            "purity": ">95% by HPLC",
            "molar_activity": null,
            "characterization": [
              "ESI-MS",
              "HPLC"
            ],
            "ms_data": {
              "calculated_exact_mass": 2417.09,
              "formula": "C108H152N28O36",
              "observed_ions": [
                {
                  "adduct": "[M+2H]2+",
                  "mz": 1210.22
                },
                {
                  "adduct": "[M+3H]3+",
                  "mz": 807.0
                }
              ]
            },
            "hplc_retention_time_min": 12.78
          },
          "purification": "Semipreparative HPLC with UV detection at 254 nm, followed by lyophilization",
          "notes": "Reaction performed in a 2 mL centrifugation tube."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Radiolabeling (68Ga) — [68Ga]Ga-DP1",
      "target_compound_id": "C12",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "68Ga chelation",
          "reactants": [
            {
              "compound_id": "C09",
              "name": "68GaCl3",
              "amount": "0.74–1.11 GBq"
            },
            {
              "compound_id": "C04",
              "name": "DP1",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate",
              "amount": "0.5 mL (0.25 M, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "0.1 M HCl",
              "volume": "1 mL"
            },
            {
              "name": "DMSO",
              "volume": "50 μL"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": "4-4.5",
            "other": "cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C12",
            "name": "[68Ga]Ga-DP1",
            "yield": "89.55 ± 0.12% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "14.37 ± 0.97 GBq/μmol",
            "characterization": [
              "radio-HPLC"
            ],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridges (WAT020515, Waters) with 1.5 mL of ethanol as eluent",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Radiolabeling (68Ga) — [68Ga]Ga-DP2",
      "target_compound_id": "C13",
      "target_compound_name": "[68Ga]Ga-DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "68Ga chelation",
          "reactants": [
            {
              "compound_id": "C09",
              "name": "68GaCl3",
              "amount": "0.74–1.11 GBq"
            },
            {
              "compound_id": "C06",
              "name": "DP2",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate",
              "amount": "0.5 mL (0.25 M, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "0.1 M HCl",
              "volume": "1 mL"
            },
            {
              "name": "DMSO",
              "volume": "50 μL"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": "4-4.5",
            "other": "cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C13",
            "name": "[68Ga]Ga-DP2",
            "yield": "7.67 ± 1.05% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "20.05 ± 1.35 GBq/μmol",
            "characterization": [
              "radio-HPLC"
            ],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridges (WAT020515, Waters) with 1.5 mL of ethanol as eluent",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Radiolabeling (68Ga) — [68Ga]Ga-DP3",
      "target_compound_id": "C14",
      "target_compound_name": "[68Ga]Ga-DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "68Ga chelation",
          "reactants": [
            {
              "compound_id": "C09",
              "name": "68GaCl3",
              "amount": "0.74–1.11 GBq"
            },
            {
              "compound_id": "C07",
              "name": "DP3",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate",
              "amount": "0.5 mL (0.25 M, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "0.1 M HCl",
              "volume": "1 mL"
            },
            {
              "name": "DMSO",
              "volume": "50 μL"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": "4-4.5",
            "other": "cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C14",
            "name": "[68Ga]Ga-DP3",
            "yield": "98.01 ± 0.97% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "14.09 ± 2.12 GBq/μmol",
            "characterization": [
              "radio-HPLC"
            ],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridges (WAT020515, Waters) with 1.5 mL of ethanol as eluent",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Radiolabeling (18F) — [18F]AlF-NP1",
      "target_compound_id": "C15",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "QMA trapping",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "[18F]fluoride",
              "amount": "0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline",
              "volume": "10 mL"
            },
            {
              "name": "pure water",
              "volume": "10 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "trapped on a preconditioned QMA cartridge"
          },
          "product": {
            "compound_id": null,
            "name": "eluted [18F]fluoride",
            "yield": null,
            "purity": null,
            "molar_activity": null,
            "characterization": [],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "Eluted with 0.2 mL saline",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Al18F complexation",
          "reactants": [
            {
              "compound_id": "C05",
              "name": "NP1",
              "amount": "50 μg (18–25 nmol)"
            },
            {
              "compound_id": "C10",
              "name": "eluted [18F]fluoride",
              "amount": null
            }
          ],
          "reagents": [
            {
              "name": "AlCl3",
              "amount": "3 μL (2 mM)",
              "role": "chelation_catalyst"
            },
            {
              "name": "sodium acetate buffer",
              "amount": "100 μL (0.1 M, pH 4.0)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": "200 μL"
            },
            {
              "name": "DMSO",
              "volume": "50 μL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C15",
            "name": "[18F]AlF-NP1",
            "yield": "62.58 ± 0.32% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "13.13 ± 1.71 GBq/μmol",
            "characterization": [
              "radio-HPLC"
            ],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridges with 1.5 mL of ethanol as eluent; ethanol solvent removed and final product resolved in saline",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Radiolabeling (18F) — [18F]AlF-NP2",
      "target_compound_id": "C16",
      "target_compound_name": "[18F]AlF-NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "QMA trapping",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "[18F]fluoride",
              "amount": "0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline",
              "volume": "10 mL"
            },
            {
              "name": "pure water",
              "volume": "10 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "trapped on a preconditioned QMA cartridge"
          },
          "product": {
            "compound_id": null,
            "name": "eluted [18F]fluoride",
            "yield": null,
            "purity": null,
            "molar_activity": null,
            "characterization": [],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "Eluted with 0.2 mL saline",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Al18F complexation",
          "reactants": [
            {
              "compound_id": "C08",
              "name": "NP2",
              "amount": "50 μg (18–25 nmol)"
            },
            {
              "compound_id": "C10",
              "name": "eluted [18F]fluoride",
              "amount": null
            }
          ],
          "reagents": [
            {
              "name": "AlCl3",
              "amount": "3 μL (2 mM)",
              "role": "chelation_catalyst"
            },
            {
              "name": "sodium acetate buffer",
              "amount": "100 μL (0.1 M, pH 4.0)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": "200 μL"
            },
            {
              "name": "DMSO",
              "volume": "50 μL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C16",
            "name": "[18F]AlF-NP2",
            "yield": "62.76 ± 0.22% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "13.42 ± 1.25 GBq/μmol",
            "characterization": [
              "radio-HPLC"
            ],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridges with 1.5 mL of ethanol as eluent; ethanol solvent removed and final product resolved in saline",
          "notes": null
        }
      ]
    }
  ]
}
```

##### Claude

```
{
  "meta": {
    "prompt_version": "v2.1",
    "extraction_date": "2026-03-15",
    "has_synthesis": true,
    "synthesis_scale": "preclinical",
    "mechanism_discussed": "synthetic",
    "method_completeness": "partial",
    "extraction_notes": "Detailed synthetic routes for all five precursors (DP1, DP2, DP3, NP1, NP2) are referenced to Schemes S1–S5 in Supporting Information, which are not present in the provided input. Only the in-house synthesis of DP1 and NP1 is described in full in the main text (Section 5.2.1). PR7, DP2, DP3, and NP2 are commercially custom-synthesized (Nanchang Tanzhen Biotechnology Co., Ltd.) with MS and HPLC data reported in the main text. Radiochemical yields, molar activities, and RCPs are summarised in Table S1 (SI); aggregate values are reported in the main text. Log P values are reported for all five radiotracers. Stability data are in Figures S18–S24 (SI)."
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
    "year": 2025
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
      "physicochemical_properties": {
        "log_p": null,
        "other": "KD = 1.57 × 10−9 M (ROR1 binding); HPLC retention time: 10.642 min; >95% purity by HPLC; docking score: −8.8 kcal/mol"
      },
      "description": "PR7 is the parent ROR1-targeting peptide scaffold used as the starting material for chelator conjugation to produce DP1 and NP1, and as a reference compound and blocking agent throughout in vitro and in vivo studies."
    },
    {
      "id": "C02",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "DOTA-NHS ester is the activated chelator reagent used for conjugation to PR7 to produce the DOTA-bearing precursor DP1 for 68Ga radiolabeling."
    },
    {
      "id": "C03",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "NOTA-NHS ester is the activated chelator reagent used for conjugation to PR7 to produce the NOTA-bearing precursor NP1 for Al18F radiolabeling."
    },
    {
      "id": "C04",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 11.230 min; >95% purity by HPLC; ESI-MS calcd 2518.14; docking score: −9.1 kcal/mol"
      },
      "description": "DP1 is a linear DOTA-conjugated PR7 peptide precursor synthesized in-house by NHS ester coupling and used as the precursor for 68Ga radiolabeling to produce [68Ga]Ga-DP1."
    },
    {
      "id": "C05",
      "name": "NP1",
      "iupac_name": null,
      "molecular_formula": "C108H152N28O36",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 12.780 min; >95% purity by HPLC; ESI-MS calcd 2417.09; docking score: −8.3 kcal/mol"
      },
      "description": "NP1 is a linear NOTA-conjugated PR7 peptide precursor synthesized in-house by NHS ester coupling and used as the precursor for Al18F radiolabeling to produce [18F]AlF-NP1."
    },
    {
      "id": "C06",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "intermediate",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.328 min; >95% purity by HPLC; ESI-MS calcd 2743.2514; docking score: −7.7 kcal/mol"
      },
      "description": "DP2 is a cyclic DOTA-conjugated peptide precursor custom-synthesized externally, derived from the PR7 scaffold, and used as the precursor for 68Ga radiolabeling to produce [68Ga]Ga-DP2."
    },
    {
      "id": "C07",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "intermediate",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.404 min; >95% purity by HPLC; ESI-MS calcd 3015.2514; docking score: −7.9 kcal/mol"
      },
      "description": "DP3 is a cyclic DOTA-conjugated peptide precursor containing disulfide-forming cysteine residues, custom-synthesized externally, and used as the precursor for 68Ga radiolabeling to produce [68Ga]Ga-DP3."
    },
    {
      "id": "C08",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "intermediate",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.620 min; >95% purity by HPLC; ESI-MS calcd 2642.20; docking score: −7.6 kcal/mol"
      },
      "description": "NP2 is a cyclic NOTA-conjugated peptide precursor custom-synthesized externally and used as the precursor for Al18F radiolabeling to produce [18F]AlF-NP2."
    },
    {
      "id": "C09",
      "name": "68GaCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "68Ge–68Ga generator (ITM)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "68GaCl3 eluted from a 68Ge–68Ga generator serves as the radionuclide source for 68Ga chelation radiolabeling of DOTA-bearing peptide precursors DP1, DP2, and DP3."
    },
    {
      "id": "C10",
      "name": "[18F]fluoride",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Cyclone 18/9 cyclotron (IBA, Belgium), Center for Molecular Imaging and Translational Medicine, Xiamen University",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Produced via the 18O(p,n)18F reaction"
      },
      "description": "[18F]fluoride produced by cyclotron serves as the radionuclide source for Al18F complexation radiolabeling of NOTA-bearing peptide precursors NP1 and NP2."
    },
    {
      "id": "C11",
      "name": "aluminum chloride (AlCl3)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "AlCl3 in sodium acetate buffer acts as the aluminium source to form the Al18F complex that coordinates with the NOTA chelator of NP1 and NP2 during Al18F radiolabeling."
    },
    {
      "id": "C12",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.19 ± 0.05",
        "other": "KD = 74.9 nM (MC38 saturation binding); blood T1/2 = 7.62 min; MC38 tumor uptake: 1.41 ± 0.08% ID/g at 30 min p.i., 0.94 ± 0.07% ID/g at 60 min p.i."
      },
      "description": "[68Ga]Ga-DP1 is the 68Ga-labeled DOTA-conjugated linear PR7-derived radiotracer and the lead 68Ga candidate, demonstrating the highest ROR1-targeting performance among the 68Ga series in cell and in vivo PET studies."
    },
    {
      "id": "C13",
      "name": "[68Ga]Ga-DP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.53 ± 0.04",
        "other": "KD = 154.9 nM (MC38 saturation binding)"
      },
      "description": "[68Ga]Ga-DP2 is the 68Ga-labeled cyclic DOTA-conjugated peptide radiotracer evaluated for ROR1-targeted PET imaging with tumor uptake comparable to [68Ga]Ga-DP1 but with higher renal accumulation."
    },
    {
      "id": "C14",
      "name": "[68Ga]Ga-DP3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−1.82 ± 0.03",
        "other": "KD = 213.4 nM (MC38 saturation binding)"
      },
      "description": "[68Ga]Ga-DP3 is the 68Ga-labeled cyclic disulfide-containing DOTA-conjugated peptide radiotracer evaluated for ROR1 PET imaging, showing the lowest tumor uptake among the 68Ga series."
    },
    {
      "id": "C15",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.10 ± 0.04",
        "other": "KD = 141.7 nM (MC38 saturation binding); blood T1/2 = 19.32 min; MC38 tumor uptake: 2.89 ± 0.07% ID/g at 30 min p.i., 1.32 ± 0.14% ID/g at 60 min p.i.; tumor-to-muscle ratio: 2.62 ± 0.06 at 60 min p.i."
      },
      "description": "[18F]AlF-NP1 is the Al18F-labeled NOTA-conjugated linear PR7-derived radiotracer and the lead 18F candidate, demonstrating the highest ROR1-targeting PET imaging performance among the 18F series across multiple tumor models."
    },
    {
      "id": "C16",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.54 ± 0.04",
        "other": "KD = 212.1 nM (MC38 saturation binding)"
      },
      "description": "[18F]AlF-NP2 is the Al18F-labeled cyclic NOTA-conjugated peptide radiotracer evaluated for ROR1-targeted PET imaging, showing significantly lower cell uptake and tumor accumulation compared to [18F]AlF-NP1."
    },
    {
      "id": "C17",
      "name": "DIPEA",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "DIPEA (N,N-diisopropylethylamine) is used as an organic base in the NHS ester conjugation reaction for the synthesis of DP1 and NP1."
    },
    {
      "id": "C18",
      "name": "sodium acetate buffer",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate buffer is used as a pH-adjusting reagent to bring the 68GaCl3 solution to pH 4–4.5 for 68Ga chelation radiolabeling, and also as the buffer medium for AlCl3 and the reaction mixture in Al18F radiolabeling."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Chelator conjugation — DP1 (DOTA-PR7)",
      "target_compound_id": "C04",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester conjugation",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 μmol)"
            },
            {
              "compound_id": "C02",
              "name": "DOTA-NHS",
              "amount": "2.5 mg (5 μmol)"
            }
          ],
          "reagents": [
            {
              "name": "DIPEA",
              "amount": "20 μL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 μL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "12 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Reaction carried out in a 2 mL centrifugation tube under agitation on an oscillator."
          },
          "product": {
            "compound_id": "C04",
            "name": "DP1",
            "yield": "4.2 mg (55.6%)",
            "purity": ">95% by HPLC",
            "molar_activity": null,
            "characterization": ["ESI-MS", "HPLC"],
            "ms_data": {
              "calculated_exact_mass": 2518.14,
              "formula": "C112H159N29O38",
              "observed_ions": [
                {
                  "adduct": "[M+2H]2+",
                  "mz": 1260.54
                },
                {
                  "adduct": "[M+3H]3+",
                  "mz": 840.68
                }
              ]
            },
            "hplc_retention_time_min": 11.230
          },
          "purification": "Semipreparative HPLC with UV detection at 254 nm; product obtained after lyophilization. HPLC mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min at 1 mL/min.",
          "notes": "DP1 and NP1 were synthesized simultaneously from PR7 in parallel reactions using DOTA-NHS and NOTA-NHS, respectively, in the same procedure (Section 5.2.1). Full synthetic route including any upstream steps is in Scheme S1, SI."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Chelator conjugation — NP1 (NOTA-PR7)",
      "target_compound_id": "C05",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester conjugation",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 μmol)"
            },
            {
              "compound_id": "C03",
              "name": "NOTA-NHS",
              "amount": "2 mg (5 μmol)"
            }
          ],
          "reagents": [
            {
              "name": "DIPEA",
              "amount": "20 μL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "400 μL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": "12 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Reaction carried out in a 2 mL centrifugation tube under agitation on an oscillator."
          },
          "product": {
            "compound_id": "C05",
            "name": "NP1",
            "yield": "3.9 mg (54%)",
            "purity": ">95% by HPLC",
            "molar_activity": null,
            "characterization": ["ESI-MS", "HPLC"],
            "ms_data": {
              "calculated_exact_mass": 2417.09,
              "formula": "C108H152N28O36",
              "observed_ions": [
                {
                  "adduct": "[M+2H]2+",
                  "mz": 1210.22
                },
                {
                  "adduct": "[M+3H]3+",
                  "mz": 807.00
                }
              ]
            },
            "hplc_retention_time_min": 12.780
          },
          "purification": "Semipreparative HPLC with UV detection at 254 nm; product obtained after lyophilization. HPLC mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min at 1 mL/min.",
          "notes": "NP1 and DP1 were synthesized simultaneously from PR7 in parallel reactions. Full synthetic route is in Scheme S4, SI."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Custom synthesis — PR7, DP2, DP3, NP2",
      "target_compound_id": "C01",
      "target_compound_name": "PR7",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": null,
          "reactants": [],
          "reagents": [],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C01",
            "name": "PR7",
            "yield": null,
            "purity": ">95% by HPLC",
            "molar_activity": null,
            "characterization": ["ESI-MS", "HPLC"],
            "ms_data": {
              "calculated_exact_mass": 2131.96,
              "formula": "C96H133N25O31",
              "observed_ions": [
                {
                  "adduct": "[M+2H]2+",
                  "mz": 1067.47
                }
              ]
            },
            "hplc_retention_time_min": 10.642
          },
          "purification": null,
          "notes": "PR7, DP2, DP3, and NP2 were custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. No synthetic details are provided in the paper; full routes are in Schemes S2, S3, and S5 (SI). HPLC method for purity analysis: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 23% B gradient to 43% B over 20 min at 1 mL/min."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Custom synthesis — DP2",
      "target_compound_id": "C06",
      "target_compound_name": "DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": null,
          "reactants": [],
          "reagents": [],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C06",
            "name": "DP2",
            "yield": null,
            "purity": ">95% by HPLC",
            "molar_activity": null,
            "characterization": ["ESI-MS", "HPLC"],
            "ms_data": {
              "calculated_exact_mass": 2743.2514,
              "formula": "C122H174N32O41",
              "observed_ions": [
                {
                  "adduct": "[M+2H]2+",
                  "mz": 1373.07
                },
                {
                  "adduct": "[M+3H]3+",
                  "mz": 915.72
                }
              ]
            },
            "hplc_retention_time_min": 10.328
          },
          "purification": null,
          "notes": "Custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. Full synthetic route in Scheme S2, SI. HPLC method: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 23% B gradient to 43% B over 20 min at 1 mL/min."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Custom synthesis — DP3",
      "target_compound_id": "C07",
      "target_compound_name": "DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": null,
          "reactants": [],
          "reagents": [],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C07",
            "name": "DP3",
            "yield": null,
            "purity": ">95% by HPLC",
            "molar_activity": null,
            "characterization": ["ESI-MS", "HPLC"],
            "ms_data": {
              "calculated_exact_mass": 3015.2514,
              "formula": "C133H186N32O43S3",
              "observed_ions": [
                {
                  "adduct": "[M+2H]2+",
                  "mz": 1509.05
                },
                {
                  "adduct": "[M+3H]3+",
                  "mz": 1006.39
                }
              ]
            },
            "hplc_retention_time_min": 10.404
          },
          "purification": null,
          "notes": "Custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. Full synthetic route in Scheme S3, SI. HPLC method: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 23% B gradient to 43% B over 20 min at 1 mL/min."
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Custom synthesis — NP2",
      "target_compound_id": "C08",
      "target_compound_name": "NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": null,
          "reactants": [],
          "reagents": [],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C08",
            "name": "NP2",
            "yield": null,
            "purity": ">95% by HPLC",
            "molar_activity": null,
            "characterization": ["ESI-MS", "HPLC"],
            "ms_data": {
              "calculated_exact_mass": 2642.20,
              "formula": "C118H167N31O39",
              "observed_ions": [
                {
                  "adduct": "[M+2H]2+",
                  "mz": 1322.56
                }
              ]
            },
            "hplc_retention_time_min": 10.620
          },
          "purification": null,
          "notes": "Custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. Full synthetic route in Scheme S5, SI. HPLC method: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 23% B gradient to 43% B over 20 min at 1 mL/min."
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Radiolabeling (68Ga) — [68Ga]Ga-DP1",
      "target_compound_id": "C12",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3 with sodium acetate buffer",
          "reactants": [
            {
              "compound_id": "C09",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate",
              "amount": "0.5 mL (0.25 M in water, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5 (after mixing)",
            "other": "68GaCl3 solution diluted with sodium acetate solution to achieve pH 4–4.5 before transfer to precursor vial."
          },
          "product": {
            "compound_id": null,
            "name": "68GaCl3–sodium acetate solution at pH 4–4.5",
            "yield": null,
            "purity": null,
            "molar_activity": null,
            "characterization": [],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "This pH-adjustment step is a prerequisite before addition to the precursor and constitutes a physically distinct operation."
        },
        {
          "step_number": 2,
          "reaction_type": "68Ga chelation",
          "reactants": [
            {
              "compound_id": "C04",
              "name": "DP1 (precursor)",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5, from Step 1)",
              "amount": "1.5 mL",
              "role": "radionuclide_source"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 μL"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "After heating, cooled to room temperature before purification."
          },
          "product": {
            "compound_id": "C12",
            "name": "[68Ga]Ga-DP1",
            "yield": "89.55 ± 0.12% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "14.37 ± 0.97 GBq/μmol",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters), eluted with 1.5 mL ethanol.",
          "notes": "Radiochemical yield, purity, and molar activity details are summarised in Table S1 (SI). Radio-HPLC method: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B at 20 min, flow rate 1 mL/min. Molar activity is mean ± SD (n ≥ 3)."
        }
      ]
    },
    {
      "pathway_id": "P8",
      "pathway_name": "Radiolabeling (68Ga) — [68Ga]Ga-DP2",
      "target_compound_id": "C13",
      "target_compound_name": "[68Ga]Ga-DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3 with sodium acetate buffer",
          "reactants": [
            {
              "compound_id": "C09",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate",
              "amount": "0.5 mL (0.25 M in water, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5 (after mixing)",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "68GaCl3–sodium acetate solution at pH 4–4.5",
            "yield": null,
            "purity": null,
            "molar_activity": null,
            "characterization": [],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "68Ga chelation",
          "reactants": [
            {
              "compound_id": "C06",
              "name": "DP2 (precursor)",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5, from Step 1)",
              "amount": "1.5 mL",
              "role": "radionuclide_source"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 μL"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "After heating, cooled to room temperature before purification."
          },
          "product": {
            "compound_id": "C13",
            "name": "[68Ga]Ga-DP2",
            "yield": "97.67 ± 1.05% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "20.05 ± 1.35 GBq/μmol",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters), eluted with 1.5 mL ethanol.",
          "notes": "Radiochemical yield, purity, and molar activity details are summarised in Table S1 (SI). Molar activity is mean ± SD (n ≥ 3)."
        }
      ]
    },
    {
      "pathway_id": "P9",
      "pathway_name": "Radiolabeling (68Ga) — [68Ga]Ga-DP3",
      "target_compound_id": "C14",
      "target_compound_name": "[68Ga]Ga-DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3 with sodium acetate buffer",
          "reactants": [
            {
              "compound_id": "C09",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate",
              "amount": "0.5 mL (0.25 M in water, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5 (after mixing)",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "68GaCl3–sodium acetate solution at pH 4–4.5",
            "yield": null,
            "purity": null,
            "molar_activity": null,
            "characterization": [],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "68Ga chelation",
          "reactants": [
            {
              "compound_id": "C07",
              "name": "DP3 (precursor)",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5, from Step 1)",
              "amount": "1.5 mL",
              "role": "radionuclide_source"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 μL"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "After heating, cooled to room temperature before purification."
          },
          "product": {
            "compound_id": "C14",
            "name": "[68Ga]Ga-DP3",
            "yield": "98.01 ± 0.97% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "14.09 ± 2.12 GBq/μmol",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters), eluted with 1.5 mL ethanol.",
          "notes": "Radiochemical yield, purity, and molar activity details are summarised in Table S1 (SI). Molar activity is mean ± SD (n ≥ 3)."
        }
      ]
    },
    {
      "pathway_id": "P10",
      "pathway_name": "Radiolabeling (Al18F) — [18F]AlF-NP1",
      "target_compound_id": "C15",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "QMA trapping",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "[18F]fluoride",
              "amount": "0.74–1.11 GBq (approximately)"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline (preconditioning)",
              "volume": "10 mL"
            },
            {
              "name": "pure water (preconditioning)",
              "volume": "10 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water before trapping."
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride trapped on QMA cartridge",
            "yield": null,
            "purity": null,
            "molar_activity": null,
            "characterization": [],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": "QMA cartridge used for [18F]fluoride trapping and elution as a separate step prior to Al18F complexation."
        },
        {
          "step_number": 2,
          "reaction_type": "Al18F complexation",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "[18F]fluoride (eluted from QMA)",
              "amount": "0.74–1.11 GBq (approximately), eluted in 0.2 mL saline"
            },
            {
              "compound_id": "C05",
              "name": "NP1 (precursor)",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "aluminum chloride (AlCl3) in sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "3 μL (2 mM)",
              "role": "chelation_catalyst"
            },
            {
              "name": "sodium acetate buffer",
              "amount": "100 μL (0.1 M, pH 4.0)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": "200 μL"
            },
            {
              "name": "DMSO",
              "volume": "50 μL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "After heating, cooled to room temperature before purification. Ethanol solvent removed after SepPak purification; final product reconstituted in saline."
          },
          "product": {
            "compound_id": "C15",
            "name": "[18F]AlF-NP1",
            "yield": "62.58 ± 0.32% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "13.13 ± 1.71 GBq/μmol",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters), eluted with 1.5 mL ethanol; ethanol evaporated; product reconstituted in saline.",
          "notes": "Radiochemical yield, purity, and molar activity details are summarised in Table S1 (SI). Radio-HPLC method: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B at 20 min, flow rate 1 mL/min. Molar activity is mean ± SD (n ≥ 3)."
        }
      ]
    },
    {
      "pathway_id": "P11",
      "pathway_name": "Radiolabeling (Al18F) — [18F]AlF-NP2",
      "target_compound_id": "C16",
      "target_compound_name": "[18F]AlF-NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "QMA trapping",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "[18F]fluoride",
              "amount": "0.74–1.11 GBq (approximately)"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline (preconditioning)",
              "volume": "10 mL"
            },
            {
              "name": "pure water (preconditioning)",
              "volume": "10 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water before trapping."
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride trapped on QMA cartridge",
            "yield": null,
            "purity": null,
            "molar_activity": null,
            "characterization": [],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Al18F complexation",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "[18F]fluoride (eluted from QMA)",
              "amount": "0.74–1.11 GBq (approximately), eluted in 0.2 mL saline"
            },
            {
              "compound_id": "C08",
              "name": "NP2 (precursor)",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "aluminum chloride (AlCl3) in sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "3 μL (2 mM)",
              "role": "chelation_catalyst"
            },
            {
              "name": "sodium acetate buffer",
              "amount": "100 μL (0.1 M, pH 4.0)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": "200 μL"
            },
            {
              "name": "DMSO",
              "volume": "50 μL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "After heating, cooled to room temperature before purification. Ethanol solvent removed after SepPak purification; final product reconstituted in saline."
          },
          "product": {
            "compound_id": "C16",
            "name": "[18F]AlF-NP2",
            "yield": "62.76 ± 0.22% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "13.42 ± 1.25 GBq/μmol",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters), eluted with 1.5 mL ethanol; ethanol evaporated; product reconstituted in saline.",
          "notes": "Radiochemical yield, purity, and molar activity details are summarised in Table S1 (SI). Molar activity is mean ± SD (n ≥ 3)."
        }
      ]
    }
  ]
}
```

