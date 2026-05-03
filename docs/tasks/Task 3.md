# Testing Reproducible of Prompt

#### v2.1prompt

##### Attempt 1
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
##### Attempt 2
```
{
  "meta": {
    "prompt_version": "v2.1",
    "extraction_date": "2026-03-17",
    "has_synthesis": true,
    "synthesis_scale": "preclinical",
    "mechanism_discussed": "synthetic",
    "method_completeness": "partial",
    "extraction_notes": "Full synthetic routes for all five precursors (DP1, DP2, DP3, NP1, NP2) are referenced to Schemes S1–S5 in Supporting Information, which are not included in the provided input. Only the synthesis of DP1 and NP1 is described in the main text (Section 5.2.1). PR7, DP2, DP3, and NP2 were custom-synthesized externally (Nanchang Tanzhen Biotechnology Co., Ltd.) with no in-house synthetic details provided. Radiolabeling procedures for all five radiotracers are fully described in Section 5.4. Radiochemical characteristics (RCY, molar activity, RCP) are summarized in Table S1 (SI); summary values are given in Section 2.2 of the main text and have been captured here. MS data for DP2, DP3, and NP2 appear in the experimental section following Section 5.2.2, extracted as written."
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
        "other": "KD = 1.57 × 10−9 M (ROR1 binding); HPLC retention time: 10.642 min; >95% pure by HPLC"
      },
      "description": "ROR1-targeting lead peptide used as the starting scaffold for chelator conjugation to generate DP1 and NP1, and as a blocking agent in cell uptake and in vivo competition assays."
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
      "description": "NHS ester-activated DOTA chelator used for conjugation to PR7 to produce the 68Ga-precursor DP1."
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
      "description": "NHS ester-activated NOTA chelator used for conjugation to PR7 to produce the 18F/Al-precursor NP1."
    },
    {
      "id": "C04",
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
      "description": "Organic base (N,N-diisopropylethylamine) used to facilitate NHS ester conjugation of DOTA-NHS or NOTA-NHS to PR7."
    },
    {
      "id": "C05",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 11.230 min; >95% pure by HPLC; used as precursor for [68Ga]Ga-DP1 radiolabeling"
      },
      "description": "DOTA-conjugated linear ROR1-targeting peptide derived from PR7, serving as the precursor for 68Ga radiolabeling to yield [68Ga]Ga-DP1."
    },
    {
      "id": "C06",
      "name": "NP1",
      "iupac_name": null,
      "molecular_formula": "C108H152N28O36",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 12.780 min; >95% pure by HPLC; used as precursor for [18F]AlF-NP1 radiolabeling"
      },
      "description": "NOTA-conjugated linear ROR1-targeting peptide derived from PR7, serving as the precursor for Al18F radiolabeling to yield [18F]AlF-NP1."
    },
    {
      "id": "C07",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.328 min; >95% pure by HPLC; used as precursor for [68Ga]Ga-DP2 radiolabeling"
      },
      "description": "DOTA-conjugated cyclic ROR1-targeting peptide (custom synthesized) serving as precursor for 68Ga radiolabeling to yield [68Ga]Ga-DP2."
    },
    {
      "id": "C08",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.404 min; >95% pure by HPLC; used as precursor for [68Ga]Ga-DP3 radiolabeling"
      },
      "description": "DOTA-conjugated cyclic ROR1-targeting peptide (custom synthesized) serving as precursor for 68Ga radiolabeling to yield [68Ga]Ga-DP3."
    },
    {
      "id": "C09",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.620 min; >95% pure by HPLC; used as precursor for [18F]AlF-NP2 radiolabeling"
      },
      "description": "NOTA-conjugated cyclic ROR1-targeting peptide (custom synthesized) serving as precursor for Al18F radiolabeling to yield [18F]AlF-NP2."
    },
    {
      "id": "C10",
      "name": "68GaCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "ITM (68Ge–68Ga generator)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Gallium-68 chloride radionuclide source obtained from a 68Ge–68Ga generator, used for radiolabeling of DOTA-peptide precursors DP1, DP2, and DP3."
    },
    {
      "id": "C11",
      "name": "[18F]fluoride",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Cyclone 18/9 cyclotron, Center for Molecular Imaging and Translational Medicine, Xiamen University",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Produced via 18O(p,n)18F reaction"
      },
      "description": "Fluorine-18 radionuclide source produced by cyclotron, trapped on a QMA cartridge and used for Al18F radiolabeling of NOTA-peptide precursors NP1 and NP2."
    },
    {
      "id": "C12",
      "name": "AlCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Aluminum chloride chelation catalyst providing Al3+ ions to form the Al18F complex incorporated into the NOTA chelator of NP1 and NP2 during radiolabeling."
    },
    {
      "id": "C13",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.19 ± 0.05",
        "other": "KD = 74.9 nM (MC38 cells); blood elimination T1/2 = 7.62 min; tumor uptake: 1.41 ± 0.08% ID/g at 30 min p.i., 0.94 ± 0.07% ID/g at 60 min p.i."
      },
      "description": "68Ga-labeled DOTA-conjugated linear ROR1-targeting peptide, the lead radiotracer demonstrating the highest MC38 cell uptake among 68Ga-labeled probes and selected for detailed in vivo evaluation."
    },
    {
      "id": "C14",
      "name": "[68Ga]Ga-DP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.53 ± 0.04",
        "other": "KD = 154.9 nM (MC38 cells)"
      },
      "description": "68Ga-labeled DOTA-conjugated cyclic ROR1-targeting peptide evaluated by PET imaging in MC38 tumor-bearing mice, showing comparable tumor uptake to [68Ga]Ga-DP1 but significant kidney accumulation."
    },
    {
      "id": "C15",
      "name": "[68Ga]Ga-DP3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−1.82 ± 0.03",
        "other": "KD = 213.4 nM (MC38 cells)"
      },
      "description": "68Ga-labeled DOTA-conjugated cyclic ROR1-targeting peptide with the highest lipophilicity among the five probes, showing the lowest tumor uptake in MC38 PET imaging studies."
    },
    {
      "id": "C16",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.10 ± 0.04",
        "other": "KD = 141.7 nM (MC38 cells); blood elimination T1/2 = 19.32 min; tumor uptake: 2.89 ± 0.07% ID/g at 30 min p.i., 1.32 ± 0.14% ID/g at 60 min p.i.; ~4% intact probe detectable in urine at 0.5 h p.i., almost none at 1 h p.i."
      },
      "description": "18F-labeled Al18F-NOTA-conjugated linear ROR1-targeting peptide identified as the lead 18F radiotracer, demonstrating the highest MC38 cell uptake and excellent tumor targeting across multiple tumor models."
    },
    {
      "id": "C17",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.54 ± 0.04",
        "other": "KD = 212.1 nM (MC38 cells)"
      },
      "description": "18F-labeled Al18F-NOTA-conjugated cyclic ROR1-targeting peptide showing significantly lower MC38 cell uptake than [18F]AlF-NP1 and pronounced renal radioactivity."
    },
    {
      "id": "C18",
      "name": "sodium acetate buffer (0.25 M, pH 6.5)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate solution used to adjust the pH of the 68GaCl3 solution to pH 4–4.5 prior to 68Ga radiolabeling reactions."
    },
    {
      "id": "C19",
      "name": "sodium acetate buffer (0.1 M, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate buffer used as the reaction medium and for dissolving AlCl3 in the Al18F radiolabeling procedure for NP1 and NP2."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Chelator conjugation — DP1",
      "target_compound_id": "C05",
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
            "other": "Reaction performed in a 2 mL centrifugation tube agitated in an oscillator"
          },
          "product": {
            "compound_id": "C05",
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
          "purification": "Semipreparative HPLC with UV detection at 254 nm; product obtained after lyophilization. HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min at 1 mL/min flow rate.",
          "notes": "DP1 and NP1 were prepared in the same reaction setup run in parallel (one with DOTA-NHS, one with NOTA-NHS). Full synthetic route referenced to Scheme S1 in Supporting Information."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Chelator conjugation — NP1",
      "target_compound_id": "C06",
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
            "other": "Reaction performed in a 2 mL centrifugation tube agitated in an oscillator"
          },
          "product": {
            "compound_id": "C06",
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
          "purification": "Semipreparative HPLC with UV detection at 254 nm; product obtained after lyophilization. HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min at 1 mL/min flow rate.",
          "notes": "NP1 and DP1 were prepared in the same reaction setup run in parallel. Full synthetic route referenced to Scheme S4 in Supporting Information."
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
          "notes": "PR7, DP2, DP3, and NP2 were custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. No synthetic details are provided in the paper. HPLC method for purity analysis: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 23% B gradient to 43% B over 20 min at 1 mL/min flow rate. Full synthetic routes referenced to Schemes S2, S3, S5 in Supporting Information."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Custom synthesis — DP2",
      "target_compound_id": "C07",
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
            "compound_id": "C07",
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
          "notes": "Custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. No synthetic details provided. Full synthetic route in Scheme S2, SI."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Custom synthesis — DP3",
      "target_compound_id": "C08",
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
            "compound_id": "C08",
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
          "notes": "Custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. No synthetic details provided. Full synthetic route in Scheme S3, SI."
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Custom synthesis — NP2",
      "target_compound_id": "C09",
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
            "compound_id": "C09",
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
          "notes": "Custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. No synthetic details provided. Full synthetic route in Scheme S5, SI."
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Radiolabeling (68Ga) — [68Ga]Ga-DP1",
      "target_compound_id": "C13",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": "68GaCl3 diluted with sodium acetate solution to adjust pH to 4–4.5"
          },
          "product": {
            "compound_id": "C10",
            "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
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
          "notes": "This pH-adjusted 68GaCl3 solution is transferred to the precursor vial for chelation in Step 2."
        },
        {
          "step_number": 2,
          "reaction_type": "68Ga chelation",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL"
            },
            {
              "compound_id": "C05",
              "name": "DP1",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "other": "Cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C13",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters), eluted with 1.5 mL ethanol. Radio-HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B at 20 min at 1 mL/min flow rate.",
          "notes": "RCY and molar activity are mean values (n ≥ 3); full radiochemical characteristics in Table S1, SI. Precursor dissolved in 50 μL DMSO placed in a vial prior to addition of pH-adjusted 68GaCl3 solution."
        }
      ]
    },
    {
      "pathway_id": "P8",
      "pathway_name": "Radiolabeling (68Ga) — [68Ga]Ga-DP2",
      "target_compound_id": "C14",
      "target_compound_name": "[68Ga]Ga-DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": "68GaCl3 diluted with sodium acetate solution to adjust pH to 4–4.5"
          },
          "product": {
            "compound_id": "C10",
            "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
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
              "compound_id": "C10",
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL"
            },
            {
              "compound_id": "C07",
              "name": "DP2",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "other": "Cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C14",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters), eluted with 1.5 mL ethanol. Radio-HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B at 20 min at 1 mL/min flow rate.",
          "notes": "RCY and molar activity are mean values (n ≥ 3); full radiochemical characteristics in Table S1, SI."
        }
      ]
    },
    {
      "pathway_id": "P9",
      "pathway_name": "Radiolabeling (68Ga) — [68Ga]Ga-DP3",
      "target_compound_id": "C15",
      "target_compound_name": "[68Ga]Ga-DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": "68GaCl3 diluted with sodium acetate solution to adjust pH to 4–4.5"
          },
          "product": {
            "compound_id": "C10",
            "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
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
              "compound_id": "C10",
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL"
            },
            {
              "compound_id": "C08",
              "name": "DP3",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "other": "Cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C15",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters), eluted with 1.5 mL ethanol. Radio-HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B at 20 min at 1 mL/min flow rate.",
          "notes": "RCY and molar activity are mean values (n ≥ 3); full radiochemical characteristics in Table S1, SI."
        }
      ]
    },
    {
      "pathway_id": "P10",
      "pathway_name": "Radiolabeling (Al18F) — [18F]AlF-NP1",
      "target_compound_id": "C16",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "QMA trapping",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "[18F]fluoride",
              "amount": "0.74–1.11 GBq"
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
            "other": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water before trapping"
          },
          "product": {
            "compound_id": "C11",
            "name": "[18F]fluoride on QMA cartridge",
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
          "notes": "[18F]fluoride trapped on preconditioned QMA cartridge prior to elution into the reaction vial in Step 2."
        },
        {
          "step_number": 2,
          "reaction_type": "Al18F complexation",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "[18F]fluoride (eluted from QMA)",
              "amount": "0.2 mL saline eluate"
            },
            {
              "compound_id": "C06",
              "name": "NP1",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "AlCl3 in sodium acetate buffer (0.1 M, pH 4.0), 2 mM",
              "amount": "3 μL",
              "role": "chelation_catalyst"
            },
            {
              "name": "sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "100 μL",
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
            "other": "Cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C16",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters), eluted with 1.5 mL ethanol; ethanol solvent removed; final product reconstituted in saline. Radio-HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B at 20 min at 1 mL/min flow rate.",
          "notes": "RCY and molar activity are mean values (n ≥ 3); full radiochemical characteristics in Table S1, SI. Precursor dissolved in 50 μL DMSO."
        }
      ]
    },
    {
      "pathway_id": "P11",
      "pathway_name": "Radiolabeling (Al18F) — [18F]AlF-NP2",
      "target_compound_id": "C17",
      "target_compound_name": "[18F]AlF-NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "QMA trapping",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "[18F]fluoride",
              "amount": "0.74–1.11 GBq"
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
            "other": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water before trapping"
          },
          "product": {
            "compound_id": "C11",
            "name": "[18F]fluoride on QMA cartridge",
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
              "compound_id": "C11",
              "name": "[18F]fluoride (eluted from QMA)",
              "amount": "0.2 mL saline eluate"
            },
            {
              "compound_id": "C09",
              "name": "NP2",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "AlCl3 in sodium acetate buffer (0.1 M, pH 4.0), 2 mM",
              "amount": "3 μL",
              "role": "chelation_catalyst"
            },
            {
              "name": "sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "100 μL",
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
            "other": "Cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C17",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters), eluted with 1.5 mL ethanol; ethanol solvent removed; final product reconstituted in saline. Radio-HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B at 20 min at 1 mL/min flow rate.",
          "notes": "RCY and molar activity are mean values (n ≥ 3); full radiochemical characteristics in Table S1, SI. Precursor dissolved in 50 μL DMSO."
        }
      ]
    }
  ]
}
```


##### Attempt 3
```
{
  "meta": {
    "prompt_version": "v2.1",
    "extraction_date": "2026-03-17",
    "has_synthesis": true,
    "synthesis_scale": "preclinical",
    "mechanism_discussed": "synthetic",
    "method_completeness": "partial",
    "extraction_notes": "Detailed synthetic routes for DP1 and NP1 are provided in the main text (Section 5.2.1). Synthetic routes for PR7, DP2, DP3, and NP2 are referenced to Schemes S1–S5 in the Supporting Information and are not reproduced in the main text; these compounds were custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. Radiolabeling procedures are fully described in Section 5.4. Radiochemical characteristics summary (RCYs, molar activities, purity) is provided in Table S1 of the SI; numerical values are also stated in the main text body (Section 2.2). MS data for DP2, DP3, and NP2 are reported in the main text (page 26057) with calculated exact masses given as nominal/average values rather than monoisotopic masses — recorded as stated. Log P values reported for radiolabeled products only."
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
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "KD = 1.57 × 10−9 M (affinity for ROR1); docking score −8.8 kcal/mol; HPLC retention time 10.642 min"
      },
      "description": "PR7 is the parent ROR1-targeting peptide lead compound used as the starting material for chelator conjugation to generate DP1, NP1, and as a blocking agent in competition assays."
    },
    {
      "id": "C02",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "DOTA-NHS ester is the activated chelator reagent used to conjugate the DOTA macrocycle to PR7 via NHS ester coupling to produce the 68Ga-labelable precursor DP1."
    },
    {
      "id": "C03",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "NOTA-NHS ester is the activated chelator reagent used to conjugate the NOTA macrocycle to PR7 via NHS ester coupling to produce the 18F/Al-labelable precursor NP1."
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
        "other": "HPLC retention time 11.230 min; docking score −9.1 kcal/mol; purity >95% by HPLC"
      },
      "description": "DP1 is the DOTA-conjugated linear peptide precursor derived from PR7, serving as the chelator-bearing precursor for 68Ga radiolabeling to produce [68Ga]Ga-DP1."
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
        "other": "HPLC retention time 12.780 min; docking score −8.3 kcal/mol; purity >95% by HPLC"
      },
      "description": "NP1 is the NOTA-conjugated linear peptide precursor derived from PR7, serving as the chelator-bearing precursor for Al18F radiolabeling to produce [18F]AlF-NP1."
    },
    {
      "id": "C06",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "intermediate",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time 10.328 min; docking score −7.7 kcal/mol; purity >95% by HPLC"
      },
      "description": "DP2 is a cyclic peptide DOTA-conjugated precursor custom synthesized for 68Ga radiolabeling to produce [68Ga]Ga-DP2."
    },
    {
      "id": "C07",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "intermediate",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time 10.404 min; docking score −7.9 kcal/mol; purity >95% by HPLC"
      },
      "description": "DP3 is a cyclic peptide DOTA-conjugated precursor custom synthesized for 68Ga radiolabeling to produce [68Ga]Ga-DP3."
    },
    {
      "id": "C08",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "intermediate",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time 10.620 min; docking score −7.6 kcal/mol; purity >95% by HPLC"
      },
      "description": "NP2 is a cyclic peptide NOTA-conjugated precursor custom synthesized for Al18F radiolabeling to produce [18F]AlF-NP2."
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
      "description": "68GaCl3 is the gallium-68 radionuclide source eluted from a 68Ge/68Ga generator and used for radiolabeling DOTA-conjugated peptide precursors DP1, DP2, and DP3."
    },
    {
      "id": "C10",
      "name": "[18F]fluoride",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "in-house (produced via 18O(p,n)18F reaction by Cyclone 18/9, IBA, Belgium, at Center for Molecular Imaging and Translational Medicine, Xiamen University)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Fluoride-18 is the positron-emitting radionuclide source produced by cyclotron and used for Al18F complexation radiolabeling of NOTA-bearing precursors NP1 and NP2."
    },
    {
      "id": "C11",
      "name": "AlCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Aluminum chloride serves as the chelation catalyst in the Al18F labeling strategy, providing the Al3+ ion that bridges NOTA and 18F to form the [AlF]2+ complex within the NOTA chelator."
    },
    {
      "id": "C12",
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
      "description": "N,N-Diisopropylethylamine (DIPEA) is used as an organic base to facilitate NHS ester conjugation of DOTA-NHS or NOTA-NHS to PR7."
    },
    {
      "id": "C13",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.19 ± 0.05",
        "other": "KD = 74.9 nM (MC38 cells); blood T1/2 = 7.62 min; tumor uptake 1.41 ± 0.08% ID/g at 30 min p.i.; purity >95% RCP by radio-HPLC"
      },
      "description": "[68Ga]Ga-DP1 is the 68Ga-labeled DOTA-linear peptide radiotracer targeting ROR1, identified as one of the two lead imaging agents with favorable tumor uptake and target-to-nontarget ratios across multiple tumor models."
    },
    {
      "id": "C14",
      "name": "[68Ga]Ga-DP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.53 ± 0.04",
        "other": "KD = 154.9 nM (MC38 cells); purity >95% RCP by radio-HPLC"
      },
      "description": "[68Ga]Ga-DP2 is the 68Ga-labeled DOTA-cyclic peptide radiotracer targeting ROR1, demonstrating tumor uptake comparable to [68Ga]Ga-DP1 but with significant kidney accumulation."
    },
    {
      "id": "C15",
      "name": "[68Ga]Ga-DP3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−1.82 ± 0.03",
        "other": "KD = 213.4 nM (MC38 cells); purity >95% RCP by radio-HPLC"
      },
      "description": "[68Ga]Ga-DP3 is the 68Ga-labeled DOTA-cyclic peptide radiotracer targeting ROR1, showing significantly lower tumor uptake and pronounced renal radioactivity compared with [68Ga]Ga-DP1."
    },
    {
      "id": "C16",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.10 ± 0.04",
        "other": "KD = 141.7 nM (MC38 cells); blood T1/2 = 19.32 min; tumor uptake 2.89 ± 0.07% ID/g at 30 min p.i.; purity >95% RCP by radio-HPLC"
      },
      "description": "[18F]AlF-NP1 is the Al18F-labeled NOTA-linear peptide radiotracer targeting ROR1, identified as one of the two lead imaging agents with excellent tumor targeting, favorable pharmacokinetics, and renal clearance."
    },
    {
      "id": "C17",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.54 ± 0.04",
        "other": "KD = 212.1 nM (MC38 cells); purity >95% RCP by radio-HPLC"
      },
      "description": "[18F]AlF-NP2 is the Al18F-labeled NOTA-cyclic peptide radiotracer targeting ROR1, showing significantly lower tumor uptake and high kidney accumulation compared with [18F]AlF-NP1."
    },
    {
      "id": "C18",
      "name": "sodium acetate buffer (pH 6.5)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate buffer at pH 6.5 is used to adjust the pH of the 68GaCl3 solution prior to radiolabeling of DOTA-conjugated precursors."
    },
    {
      "id": "C19",
      "name": "sodium acetate buffer (pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate buffer at pH 4.0 is used as the reaction medium for the Al18F complexation radiolabeling of NOTA-conjugated precursors NP1 and NP2."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Chelator conjugation — DP1 (DOTA-NHS coupling to PR7)",
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
            "other": null
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
          "purification": "Semipreparative HPLC with UV detection at 254 nm; product obtained after lyophilization. HPLC mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "Reaction performed in a 2 mL centrifugation tube agitated in an oscillator. DP1 and NP1 were synthesized in the same reaction setup using DOTA-NHS and NOTA-NHS respectively."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Chelator conjugation — NP1 (NOTA-NHS coupling to PR7)",
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
            "other": null
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
          "purification": "Semipreparative HPLC with UV detection at 254 nm; product obtained after lyophilization. HPLC mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "Reaction performed in a 2 mL centrifugation tube agitated in an oscillator. Same reaction setup as DP1 synthesis but using NOTA-NHS in place of DOTA-NHS."
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
          "notes": "PR7, DP2, DP3, and NP2 were custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. Synthetic routes are described in Schemes S1–S5 in the Supporting Information, which are not reproduced in the main text. HPLC method for characterization: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 23% B to 43% B over 20 min, flow rate 1 mL/min."
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
          "notes": "Custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. Synthetic route in Schemes S1–S5, SI. HPLC method: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 23% B to 43% B over 20 min, flow rate 1 mL/min."
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
          "notes": "Custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. Synthetic route in Schemes S1–S5, SI. HPLC method: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 23% B to 43% B over 20 min, flow rate 1 mL/min."
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
          "notes": "Custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. Synthetic route in Schemes S1–S5, SI. HPLC method: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 23% B to 43% B over 20 min, flow rate 1 mL/min. Only [M+2H]2+ ion is reported in the paper for NP2."
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Radiolabeling (68Ga) — [68Ga]Ga-DP1",
      "target_compound_id": "C13",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3 solution",
          "reactants": [
            {
              "compound_id": "C09",
              "name": "68GaCl3",
              "amount": "1 mL (0.74–1.11 GBq in 0.1 M HCl)"
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
            "compound_id": "C09",
            "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
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
          "notes": "The pH-adjusted 68GaCl3 solution is immediately transferred to the vial containing the precursor for chelation in Step 2."
        },
        {
          "step_number": 2,
          "reaction_type": "68Ga chelation",
          "reactants": [
            {
              "compound_id": "C09",
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL"
            },
            {
              "compound_id": "C04",
              "name": "DP1",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "other": "Cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C13",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters) eluted with 1.5 mL ethanol. Radio-HPLC analysis: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "Radiochemical characteristics (RCY, molar activity, RCP) summarized in Table S1, SI; values also stated in main text Section 2.2. n ≥ 3 for molar activity determination. No post-purification solvent removal or reconstitution step is described for 68Ga products."
        }
      ]
    },
    {
      "pathway_id": "P8",
      "pathway_name": "Radiolabeling (68Ga) — [68Ga]Ga-DP2",
      "target_compound_id": "C14",
      "target_compound_name": "[68Ga]Ga-DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3 solution",
          "reactants": [
            {
              "compound_id": "C09",
              "name": "68GaCl3",
              "amount": "1 mL (0.74–1.11 GBq in 0.1 M HCl)"
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
            "compound_id": "C09",
            "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
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
              "compound_id": "C09",
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL"
            },
            {
              "compound_id": "C06",
              "name": "DP2",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "other": "Cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C14",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters) eluted with 1.5 mL ethanol. Radio-HPLC analysis: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "n ≥ 3 for molar activity determination. Radiochemical characteristics also in Table S1, SI."
        }
      ]
    },
    {
      "pathway_id": "P9",
      "pathway_name": "Radiolabeling (68Ga) — [68Ga]Ga-DP3",
      "target_compound_id": "C15",
      "target_compound_name": "[68Ga]Ga-DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3 solution",
          "reactants": [
            {
              "compound_id": "C09",
              "name": "68GaCl3",
              "amount": "1 mL (0.74–1.11 GBq in 0.1 M HCl)"
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
            "compound_id": "C09",
            "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
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
              "compound_id": "C09",
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL"
            },
            {
              "compound_id": "C07",
              "name": "DP3",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "other": "Cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C15",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters) eluted with 1.5 mL ethanol. Radio-HPLC analysis: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "n ≥ 3 for molar activity determination. Radiochemical characteristics also in Table S1, SI."
        }
      ]
    },
    {
      "pathway_id": "P10",
      "pathway_name": "Radiolabeling (Al18F) — [18F]AlF-NP1",
      "target_compound_id": "C16",
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
            "other": null
          },
          "product": {
            "compound_id": "C10",
            "name": "[18F]fluoride on QMA cartridge",
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
          "notes": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water before trapping."
        },
        {
          "step_number": 2,
          "reaction_type": "Al18F complexation",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "[18F]fluoride (eluted from QMA)",
              "amount": "0.2 mL saline eluate"
            },
            {
              "compound_id": "C05",
              "name": "NP1",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "aluminum chloride (AlCl3)",
              "amount": "3 μL (2 mM in sodium acetate buffer, 0.1 M, pH 4.0)",
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
            "other": "Cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C16",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters) eluted with 1.5 mL ethanol. Ethanol solvent removed after purification; final product reconstituted in saline. Radio-HPLC analysis: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "n ≥ 3 for molar activity determination. Radiochemical characteristics also in Table S1, SI."
        }
      ]
    },
    {
      "pathway_id": "P11",
      "pathway_name": "Radiolabeling (Al18F) — [18F]AlF-NP2",
      "target_compound_id": "C17",
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
            "other": null
          },
          "product": {
            "compound_id": "C10",
            "name": "[18F]fluoride on QMA cartridge",
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
          "notes": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water before trapping."
        },
        {
          "step_number": 2,
          "reaction_type": "Al18F complexation",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "[18F]fluoride (eluted from QMA)",
              "amount": "0.2 mL saline eluate"
            },
            {
              "compound_id": "C08",
              "name": "NP2",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "aluminum chloride (AlCl3)",
              "amount": "3 μL (2 mM in sodium acetate buffer, 0.1 M, pH 4.0)",
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
            "other": "Cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C17",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters) eluted with 1.5 mL ethanol. Ethanol solvent removed after purification; final product reconstituted in saline. Radio-HPLC analysis: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "n ≥ 3 for molar activity determination. Radiochemical characteristics also in Table S1, SI."
        }
      ]
    }
  ]
}
```

##### Attempt 4
```
{
  "meta": {
    "prompt_version": "v2.1",
    "extraction_date": "2026-03-17",
    "has_synthesis": true,
    "synthesis_scale": "preclinical",
    "mechanism_discussed": "synthetic",
    "method_completeness": "partial",
    "extraction_notes": "Full synthetic routes for DP1, DP2, DP3, NP1, and NP2 are stated to be in Schemes S1–S5 (Supporting Information), which are not provided in this input. Section 5.2.1 gives in-house synthesis details for DP1 and NP1 only. PR7, DP2, DP3, and NP2 are noted as custom-synthesized externally (Nanchang Tanzhen Biotechnology Co., Ltd.); DOTA-NHS and NOTA-NHS are also from this vendor. Radiolabeling details for all five radiotracers are fully described in Section 5.4. ESI-MS data for all precursors are present in the main text. Radiochemical characteristics (RCY, molar activity, RCP) are summarized as text values; Table S1 referenced for full tabular data. Log P values are reported for all five radiotracers."
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
        "other": "KD = 1.57 × 10−9 M (affinity for ROR1); docking score −8.8 kcal/mol"
      },
      "description": "PR7 is the parent ROR1-targeting peptide used as the lead scaffold for all subsequent chelator-conjugated and cyclic peptide derivatives in this study."
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
      "description": "DOTA-NHS ester is the activated chelator reagent used to conjugate the macrocyclic DOTA chelator to the PR7 peptide amine to produce DP1."
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
      "description": "NOTA-NHS ester is the activated chelator reagent used to conjugate the macrocyclic NOTA chelator to the PR7 peptide amine to produce NP1."
    },
    {
      "id": "C04",
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
      "description": "N,N-Diisopropylethylamine (DIPEA) serves as an organic base to neutralize acid generated during NHS ester conjugation reactions producing DP1 and NP1."
    },
    {
      "id": "C05",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Docking score −9.1 kcal/mol; KD = 74.9 nM (MC38 cells)"
      },
      "description": "DP1 is the linear DOTA-conjugated PR7 peptide precursor used for 68Ga radiolabeling to generate [68Ga]Ga-DP1 for ROR1-targeted PET imaging."
    },
    {
      "id": "C06",
      "name": "NP1",
      "iupac_name": null,
      "molecular_formula": "C108H152N28O36",
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Docking score −8.3 kcal/mol; KD = 141.7 nM (MC38 cells)"
      },
      "description": "NP1 is the linear NOTA-conjugated PR7 peptide precursor used for Al18F radiolabeling to generate [18F]AlF-NP1 for ROR1-targeted PET imaging."
    },
    {
      "id": "C07",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Docking score −7.7 kcal/mol; KD = 154.9 nM (MC38 cells); HPLC retention time 10.328 min"
      },
      "description": "DP2 is a cyclic DOTA-conjugated ROR1-targeting peptide precursor custom-synthesized externally and used for 68Ga radiolabeling."
    },
    {
      "id": "C08",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Docking score −7.9 kcal/mol; KD = 213.4 nM (MC38 cells); HPLC retention time 10.404 min"
      },
      "description": "DP3 is a cyclic DOTA-conjugated ROR1-targeting peptide precursor custom-synthesized externally and used for 68Ga radiolabeling."
    },
    {
      "id": "C09",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Docking score −7.6 kcal/mol; KD = 212.1 nM (MC38 cells); HPLC retention time 10.620 min"
      },
      "description": "NP2 is a cyclic NOTA-conjugated ROR1-targeting peptide precursor custom-synthesized externally and used for Al18F radiolabeling."
    },
    {
      "id": "C10",
      "name": "68GaCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "ITM (68Ge–68Ga generator)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "68GaCl3 eluted from a 68Ge–68Ga generator serves as the radionuclide source for radiolabeling of DOTA-conjugated peptide precursors DP1, DP2, and DP3."
    },
    {
      "id": "C11",
      "name": "[18F]fluoride",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Center for Molecular Imaging and Translational Medicine, Xiamen University (Cyclone 18/9, IBA)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "[18F]fluoride produced by the 18O(p,n)18F reaction is the radionuclide source used in Al18F complexation for labeling of NOTA-conjugated peptide precursors NP1 and NP2."
    },
    {
      "id": "C12",
      "name": "AlCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Aluminum chloride (AlCl3) serves as the chelation catalyst providing Al3+ ions for Al18F complexation during radiolabeling of NOTA-conjugated precursors NP1 and NP2."
    },
    {
      "id": "C13",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.19 ± 0.05",
        "other": "Blood elimination half-life T1/2 = 7.62 min; MC38 tumor uptake 1.41 ± 0.08% ID/g at 30 min p.i., 0.94 ± 0.07% ID/g at 60 min p.i."
      },
      "description": "[68Ga]Ga-DP1 is the 68Ga-radiolabeled form of the linear DOTA-peptide DP1, serving as the primary 68Ga-labeled ROR1-targeted PET radiotracer evaluated in preclinical tumor models."
    },
    {
      "id": "C14",
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
      "description": "[68Ga]Ga-DP2 is the 68Ga-radiolabeled cyclic DOTA-peptide used as a comparative ROR1-targeted PET radiotracer in MC38 tumor-bearing mouse models."
    },
    {
      "id": "C15",
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
      "description": "[68Ga]Ga-DP3 is the 68Ga-radiolabeled cyclic DOTA-peptide evaluated as a comparative ROR1-targeted PET radiotracer, showing the lowest tumor uptake among the 68Ga series."
    },
    {
      "id": "C16",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.10 ± 0.04",
        "other": "Blood elimination half-life T1/2 = 19.32 min; MC38 tumor uptake 2.89 ± 0.07% ID/g at 30 min p.i., 1.32 ± 0.14% ID/g at 60 min p.i."
      },
      "description": "[18F]AlF-NP1 is the Al18F-radiolabeled linear NOTA-peptide NP1 and serves as the primary 18F-labeled ROR1-targeted PET radiotracer, demonstrating the highest cell uptake and favorable preclinical imaging performance."
    },
    {
      "id": "C17",
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
      "description": "[18F]AlF-NP2 is the Al18F-radiolabeled cyclic NOTA-peptide NP2 evaluated as a comparative 18F-labeled ROR1-targeted PET radiotracer, showing lower tumor uptake and higher renal accumulation than [18F]AlF-NP1."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Chelator conjugation — DP1",
      "target_compound_id": "C05",
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
            "other": null
          },
          "product": {
            "compound_id": "C05",
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
          "purification": "Semipreparative HPLC with UV detection at 254 nm; product obtained after lyophilization. HPLC mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "Reaction performed in a 2 mL centrifugation tube agitated in an oscillator. Full synthetic route stated to be in Scheme S1 (Supporting Information)."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Chelator conjugation — NP1",
      "target_compound_id": "C06",
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
            "other": null
          },
          "product": {
            "compound_id": "C06",
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
          "purification": "Semipreparative HPLC with UV detection at 254 nm; product obtained after lyophilization. HPLC mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "Reaction performed in the same 2 mL centrifugation tube setup as DP1; DP1 and NP1 were prepared in parallel from the same PR7 batch. Full synthetic route stated to be in Scheme S2 (Supporting Information, implied)."
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
          "notes": "PR7, DP2, DP3, and NP2 were all custom-synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. No synthetic details are provided in the main text or accessible Supporting Information for this input. HPLC method for these four compounds: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 23% B gradient to 43% B over 20 min, flow rate 1 mL/min. Full synthetic routes stated to be in Schemes S1–S5 (Supporting Information)."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Custom synthesis — DP2",
      "target_compound_id": "C07",
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
            "compound_id": "C07",
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
          "notes": "Custom-synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. No synthetic details provided in this input. Full synthetic route in Supporting Information (Schemes S1–S5)."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Custom synthesis — DP3",
      "target_compound_id": "C08",
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
            "compound_id": "C08",
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
          "notes": "Custom-synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. No synthetic details provided in this input. Full synthetic route in Supporting Information (Schemes S1–S5)."
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Custom synthesis — NP2",
      "target_compound_id": "C09",
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
            "compound_id": "C09",
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
          "notes": "Custom-synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. No synthetic details provided in this input. Full synthetic route in Supporting Information (Schemes S1–S5)."
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Radiolabeling (68Ga) — [68Ga]Ga-DP1",
      "target_compound_id": "C13",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3 solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3",
              "amount": "0.74–1.11 GBq in 0.1 M HCl, 1 mL"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate solution",
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
            "ph": "4–4.5 (final solution pH)",
            "other": null
          },
          "product": {
            "compound_id": "C10",
            "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
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
          "notes": "pH-adjusted 68GaCl3 solution immediately transferred to vial containing peptide precursor for chelation step."
        },
        {
          "step_number": 2,
          "reaction_type": "68Ga chelation",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL total"
            },
            {
              "compound_id": "C05",
              "name": "DP1",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "other": "Cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C13",
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
          "purification": "SepPak C18 cartridges (WAT020515, Waters); eluent 1.5 mL ethanol. Radiochemical yield, purity, and molar activity determined by radio-HPLC. HPLC method: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "n ≥ 3 for molar activity determination. Stability confirmed >90% RCP after 2 h in saline and fetal bovine serum (Figures S18–S22, SI). Full radiochemical characteristics in Table S1 (SI)."
        }
      ]
    },
    {
      "pathway_id": "P8",
      "pathway_name": "Radiolabeling (68Ga) — [68Ga]Ga-DP2",
      "target_compound_id": "C14",
      "target_compound_name": "[68Ga]Ga-DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3 solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3",
              "amount": "0.74–1.11 GBq in 0.1 M HCl, 1 mL"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate solution",
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
            "ph": "4–4.5 (final solution pH)",
            "other": null
          },
          "product": {
            "compound_id": "C10",
            "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
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
              "compound_id": "C10",
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL total"
            },
            {
              "compound_id": "C07",
              "name": "DP2",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "other": "Cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C14",
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
          "purification": "SepPak C18 cartridges (WAT020515, Waters); eluent 1.5 mL ethanol. Radio-HPLC method: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "n ≥ 3 for molar activity. Stability >90% RCP after 2 h. Full data in Table S1 (SI)."
        }
      ]
    },
    {
      "pathway_id": "P9",
      "pathway_name": "Radiolabeling (68Ga) — [68Ga]Ga-DP3",
      "target_compound_id": "C15",
      "target_compound_name": "[68Ga]Ga-DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3 solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3",
              "amount": "0.74–1.11 GBq in 0.1 M HCl, 1 mL"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate solution",
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
            "ph": "4–4.5 (final solution pH)",
            "other": null
          },
          "product": {
            "compound_id": "C10",
            "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
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
              "compound_id": "C10",
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL total"
            },
            {
              "compound_id": "C08",
              "name": "DP3",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "other": "Cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C15",
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
          "purification": "SepPak C18 cartridges (WAT020515, Waters); eluent 1.5 mL ethanol. Radio-HPLC method: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "n ≥ 3 for molar activity. Stability >90% RCP after 2 h. Full data in Table S1 (SI)."
        }
      ]
    },
    {
      "pathway_id": "P10",
      "pathway_name": "Radiolabeling (Al18F) — [18F]AlF-NP1",
      "target_compound_id": "C16",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "QMA trapping",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "[18F]fluoride",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline (preconditioning wash)",
              "volume": "10 mL"
            },
            {
              "name": "pure water (preconditioning wash)",
              "volume": "10 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C11",
            "name": "[18F]fluoride (trapped on QMA cartridge)",
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
          "notes": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water prior to trapping."
        },
        {
          "step_number": 2,
          "reaction_type": "Al18F complexation",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "[18F]fluoride (eluted from QMA)",
              "amount": "0.2 mL saline eluate"
            },
            {
              "compound_id": "C06",
              "name": "NP1",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "AlCl3 in sodium acetate buffer",
              "amount": "3 μL (2 mM AlCl3 in 0.1 M sodium acetate, pH 4.0)",
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
            "ph": "4.0",
            "other": "Cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C16",
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
          "purification": "SepPak C18 cartridges (WAT020515, Waters); eluent 1.5 mL ethanol. Ethanol solvent removed; final product reconstituted in saline. Radio-HPLC method: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "n ≥ 3 for molar activity. Metabolic stability assessed in urine of normal mice: approximately 4% intact probe at 0.5 h p.i., essentially none at 1 h p.i. (Figures S23–S24, SI). Stability >90% RCP after 2 h in saline and serum. Full data in Table S1 (SI)."
        }
      ]
    },
    {
      "pathway_id": "P11",
      "pathway_name": "Radiolabeling (Al18F) — [18F]AlF-NP2",
      "target_compound_id": "C17",
      "target_compound_name": "[18F]AlF-NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "QMA trapping",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "[18F]fluoride",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline (preconditioning wash)",
              "volume": "10 mL"
            },
            {
              "name": "pure water (preconditioning wash)",
              "volume": "10 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C11",
            "name": "[18F]fluoride (trapped on QMA cartridge)",
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
          "notes": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water prior to trapping."
        },
        {
          "step_number": 2,
          "reaction_type": "Al18F complexation",
          "reactants": [
            {
              "compound_id": "C11",
              "name": "[18F]fluoride (eluted from QMA)",
              "amount": "0.2 mL saline eluate"
            },
            {
              "compound_id": "C09",
              "name": "NP2",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "AlCl3 in sodium acetate buffer",
              "amount": "3 μL (2 mM AlCl3 in 0.1 M sodium acetate, pH 4.0)",
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
            "ph": "4.0",
            "other": "Cooled to room temperature before purification"
          },
          "product": {
            "compound_id": "C17",
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
          "purification": "SepPak C18 cartridges (WAT020515, Waters); eluent 1.5 mL ethanol. Ethanol solvent removed; final product reconstituted in saline. Radio-HPLC method: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "n ≥ 3 for molar activity. Stability >90% RCP after 2 h. Full data in Table S1 (SI)."
        }
      ]
    }
  ]
}
```



#### v2.2 prompt
```
SYSTEM ROLE
You are an expert chemist and scientific information extraction specialist with deep knowledge of organic, medicinal, and radiochemical synthesis. Your task is to extract chemical synthesis information from the academic paper provided below with maximum precision.

---

CRITICAL EXTRACTION RULES — read before answering

1. ARTICLE-ONLY
Extract exclusively from the version of the paper provided to you (main text, schemes, figures, experimental section). If the paper references Supporting Information for details not present in your input, record null for those fields and note the SI reference in the step's "notes" field. Do NOT supplement with prior chemical knowledge.

2. NOT REPORTED
If a field's value is absent from the article, use null — never invent plausible values.

3. NEGATIVE CASE
If the paper contains NO synthesis, still return valid JSON with has_synthesis: false and all synthesis arrays empty.

4. YIELD FORMAT
Use "N mg (N%)" when both mass and percentage are stated; "N%" when only a percentage is given. For radiochemical yields, append the RCY suffix: "89.55 ± 0.12% RCY". ONE compound per yield string — never concatenate multiple compounds into a single yield field.

5. AMOUNTS FORMAT
Express amounts as "N unit (N unit)" for mass + moles (e.g. "6.4 mg (3 μmol)"). Use an en dash for ranges: "0.74–1.11 GBq". Never append solvent or concentration context into the amount string — those go in the solvents array or reagents list respectively.

6. COMPOUND ENTRIES — what to include
Include ALL compounds: final products, intermediates, catalysts, radiolabeled derivatives, and any named reagent that plays a defined mechanistic role. Specific inclusion rules:

- Radionuclide sources (e.g. 68GaCl3, [18F]fluoride, [64Cu]Cl2) always get their own compound entry.
- Inorganic reagents with a defined mechanistic role (e.g. AlCl3 in AlF radiolabeling, SnCl2 as a reductant) always get their own compound entry.
- Organic bases or activating agents named with an amount in a synthesis step (e.g. DIPEA, HATU, PyBOP) get their own compound entry.
- Buffer solutions: create one compound entry per distinct pH/concentration combination if each plays a mechanistically distinct role. Do not merge two buffers at different pH values into one entry.
- Pure solvents used only for dissolution or elution (e.g. DMSO, MeCN, EtOH, DCM) do NOT need compound entries — record them only in the solvents array of each step.

7. ROLE ASSIGNMENT — use these definitions exactly

Assign one role per compound. When in doubt, apply this decision tree in order:

- Is it a radiolabeled product (contains a radioisotope, produced in a radiolabeling step)? → radiolabeled_product
- Is it sourced externally (commercial supplier, custom order, vendor synthesis) and used directly as a substrate or precursor with no in-house chemical transformation? → starting_material
- Is it sourced externally and used as a consumable reagent (activating agent, chelator, base, buffer, radionuclide source)? → reagent
- Is it synthesised in-house and its sole purpose is to serve as input to a subsequent transformation (including radiolabeling)? → intermediate
- Is it synthesised in-house or externally and presented as a standalone biologically or pharmacologically evaluated deliverable? → final_product
- Is it used as a positive or negative control, reference standard, or blocking agent? → reference_compound
- Is it a metal, ligand, or co-ligand in a coordination or organometallic context? → catalyst or coligand as appropriate

Key distinctions:
- A compound is intermediate only if it was made in-house in this study. An externally synthesised compound used as a radiolabeling precursor is starting_material, not intermediate.
- A compound is final_product only if the paper evaluates it as a standalone deliverable. A chelator-peptide conjugate whose sole purpose is radiolabeling is intermediate, not final_product, even if it is characterised by HPLC and MS.

8. is_newly_synthesized
Set to true only for compounds prepared in-house during this study. Set to false for all commercially purchased, custom-ordered, or externally synthesised compounds, regardless of whether the structure is novel.

9. method_completeness
Choose exactly one value:
- "full" — complete procedure is in the main text for all compounds and steps
- "partial" — at least one in-house procedure appears in the main text; others are in SI or unavailable
- "referenced_to_SI" — main text gives no procedural detail at all; all routes are in SI only
- "none" — no synthesis is reported

If the main text contains an explicit in-house synthesis procedure for even one compound, use "partial", not "referenced_to_SI".

10. STEP GRANULARITY
Each physically distinct operation that requires its own materials list is a separate numbered step, even if the paper narrates them in one paragraph. Indicators: different equipment, different reagents, different conditions, different vessel. Examples: solid-phase resin loading and coupling are separate steps; QMA trapping and Al18F complexation are separate steps; pH adjustment of a radionuclide solution and the subsequent chelation reaction are separate steps.

11. INTERMEDIATE PRODUCTS IN MULTI-STEP SEQUENCES
The product block of every step must describe what is produced by that step — even if it is a transient intermediate (e.g. a pH-adjusted radionuclide solution, a resin-bound peptide after a single coupling). For transient intermediates that have no independent compound entry, use "compound_id": null and give a descriptive name. Never recycle the compound_id of an input to describe the output of the same step.

12. REAGENT vs CONDITIONS — where concentration and pH go
- The pH of the reaction mixture goes in conditions.ph.
- The concentration and pH of a reagent solution (e.g. a buffer added to the reaction) go in the reagent's amount field: "0.5 mL (0.25 M, pH 6.5)".
- Never duplicate: if a value is in the reagent amount field, do not also put it in conditions.

13. PURITY FORMAT
Always include the analytical method: ">95% by HPLC" for non-radioactive compounds; ">95% RCP by radio-HPLC" for radiolabeled products.

14. TEMPERATURE FORMAT
Use SI convention with a space: "95 °C", "-20 °C", "room temperature". Never "95°C".

15. HPLC RETENTION TIME
Record as a number in minutes in product.hplc_retention_time_min. If a retention time is reported only in a characterisation table and not in a synthesis yield statement, still record it in the synthesis step product block for that compound.

16. MS DATA — monoisotopic vs nominal mass
Record the calculated mass exactly as stated in the paper. For large peptides, authors sometimes report nominal or average masses rather than monoisotopic masses. When this is evident (e.g. the stated mass matches the average molecular weight rather than the monoisotopic mass), note it in meta.extraction_notes. Do not correct or recalculate.

17. ONE ENTRY PER COMPOUND
Each distinct substance gets exactly one compound entry and one ID. Assign IDs (C01, C02, ...) in the order compounds first appear in the paper. Do not skip IDs, do not reuse them, do not merge two substances into one entry.

18. NO CITATION ARTIFACTS
All string values must be plain prose. Strip citation tags, reference numbers, footnote markers, and retrieval-system metadata from all fields.

19. ONE PATHWAY PER TARGET COMPOUND
Each synthesis pathway (P1, P2, ...) targets exactly one compound. Never describe two distinct synthetic routes in one pathway entry using "or" / "alternatively" logic.

---

OUTPUT SCHEMA

Return a single JSON object. Do not add any text before or after the JSON.

{
  "meta": {
    "prompt_version": "v2.2",
    "extraction_date": "YYYY-MM-DD",
    "has_synthesis": true,
    "synthesis_scale": "lab | preclinical | gmp | none",
    "mechanism_discussed": "synthetic | biological_only | none",
    "method_completeness": "full | partial | referenced_to_SI | none",
    "extraction_notes": "string or null"
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
      "name": "string",
      "iupac_name": "string or null — only if explicitly stated in the paper",
      "molecular_formula": "string or null — only if explicitly stated",
      "role": "starting_material | intermediate | reagent | catalyst | coligand | radiolabeled_product | final_product | reference_compound",
      "is_newly_synthesized": true,
      "source": "string or null — in-house, commercial, or vendor name if stated",
      "physicochemical_properties": {
        "log_p": "string or null",
        "other": "string or null"
      },
      "description": "one sentence of plain prose describing this compound's function in the study"
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "string",
      "target_compound_id": "C01",
      "target_compound_name": "string",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "string or null",
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
              "role": "coupling_reagent | base | acid | oxidant | reductant | catalyst | protecting_group_reagent | ph_adjuster | radionuclide_source | chelation_catalyst | other"
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
            "ph": "string or null — pH of the reaction mixture only",
            "other": "string or null — stirring mode, post-reaction cooling, special handling; vessel and equipment details go in notes"
          },
          "product": {
            "compound_id": "string or null — C-ID if the compound has an entry; null for transient intermediates",
            "name": "string",
            "yield": "string or null",
            "purity": "string or null",
            "molar_activity": "string or null — radiolabeled products only",
            "characterization": ["ESI-MS", "HPLC"],
            "ms_data": {
              "calculated_exact_mass": "number or null",
              "formula": "string or null",
              "observed_ions": [
                {
                  "adduct": "string",
                  "mz": "number or null"
                }
              ]
            },
            "hplc_retention_time_min": "number or null"
          },
          "purification": "string or null — method, catalog number if given, elution solvent and volume, post-purification formulation steps",
          "notes": "string or null — SI references, vessel and equipment details, n value for replicates, any procedural context not captured above"
        }
      ]
    }
  ]
}
```

##### ChatGPT_1
```
{
  "meta": {
    "prompt_version": "v2.2",
    "extraction_date": "2026-03-18",
    "has_synthesis": true,
    "synthesis_scale": "preclinical",
    "mechanism_discussed": "none",
    "method_completeness": "partial",
    "extraction_notes": "Detailed synthetic routes for several peptide precursors (DP2, DP3, NP2, PR7) are stated to be in Supporting Information only. Radiochemical yields are reported as averages without mass values. No HPLC retention times are reported for radiolabeled products."
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
      "source": "custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "A peptide scaffold used as the starting material for conjugation to chelators to form radiolabeling precursors."
    },
    {
      "id": "C02",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "An activated chelator used to conjugate with PR7 to form DOTA-containing peptide precursor DP1."
    },
    {
      "id": "C03",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "An activated chelator used to conjugate with PR7 to form NOTA-containing peptide precursor NP1."
    },
    {
      "id": "C04",
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
      "description": "A base used to facilitate amide coupling between PR7 and NHS-activated chelators."
    },
    {
      "id": "C05",
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
      "description": "A DOTA-conjugated peptide precursor used for radiolabeling with gallium-68."
    },
    {
      "id": "C06",
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
      "description": "A NOTA-conjugated peptide precursor used for radiolabeling with fluorine-18 via AlF chemistry."
    },
    {
      "id": "C07",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "A peptide-based precursor used for radiolabeling with gallium-68."
    },
    {
      "id": "C08",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "A peptide-based precursor used for radiolabeling with gallium-68."
    },
    {
      "id": "C09",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "A peptide-based precursor used for radiolabeling with fluorine-18 via AlF chemistry."
    },
    {
      "id": "C10",
      "name": "68GaCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "68Ge−68Ga generator (ITM)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "The radionuclide source used for labeling peptide precursors with gallium-68."
    },
    {
      "id": "C11",
      "name": "Sodium acetate buffer (0.25 M, pH 6.5)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "A buffer used to adjust the pH of the gallium-68 solution prior to chelation."
    },
    {
      "id": "C12",
      "name": "Fluoride-18",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "cyclotron production",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "The radionuclide source used for aluminum fluoride radiolabeling of peptide precursors."
    },
    {
      "id": "C13",
      "name": "Aluminum chloride",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "A reagent used to form the Al18F complex during fluorine-18 radiolabeling."
    },
    {
      "id": "C14",
      "name": "Sodium acetate buffer (0.1 M, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "A buffer used in the Al18F radiolabeling reaction mixture to maintain acidic conditions."
    },
    {
      "id": "C15",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "A gallium-68 labeled peptide used as a PET imaging probe targeting ROR1."
    },
    {
      "id": "C16",
      "name": "[68Ga]Ga-DP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "A gallium-68 labeled peptide used as a PET imaging probe targeting ROR1."
    },
    {
      "id": "C17",
      "name": "[68Ga]Ga-DP3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "A gallium-68 labeled peptide used as a PET imaging probe targeting ROR1."
    },
    {
      "id": "C18",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "A fluorine-18 labeled peptide prepared via AlF chemistry for PET imaging of ROR1."
    },
    {
      "id": "C19",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "A fluorine-18 labeled peptide prepared via AlF chemistry for PET imaging of ROR1."
    }
  ],
  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of DP1",
      "target_compound_id": "C05",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide coupling",
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
            "compound_id": "C05",
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
                  "adduct": "[M + 2H]2+",
                  "mz": 1260.54
                },
                {
                  "adduct": "[M + 3H]3+",
                  "mz": 840.68
                }
              ]
            },
            "hplc_retention_time_min": 11.23
          },
          "purification": "semipreparative HPLC followed by lyophilization",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of NP1",
      "target_compound_id": "C06",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide coupling",
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
            "compound_id": "C06",
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
                  "adduct": "[M + 2H]2+",
                  "mz": 1210.22
                },
                {
                  "adduct": "[M + 3H]3+",
                  "mz": 807.0
                }
              ]
            },
            "hplc_retention_time_min": 12.78
          },
          "purification": "semipreparative HPLC followed by lyophilization",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Radiolabeling of gallium-68 peptides",
      "target_compound_id": "C15",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3",
              "amount": "0.74–1.11 GBq"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate buffer (0.25 M, pH 6.5)",
              "amount": "0.5 mL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "pH-adjusted 68Ga solution",
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
          "reaction_type": "radiometal chelation",
          "reactants": [
            {
              "compound_id": "C05",
              "name": "DP1",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "other": null
          },
          "product": {
            "compound_id": "C15",
            "name": "[68Ga]Ga-DP1",
            "yield": "89.55 ± 0.12% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "14.37 ± 0.97 GBq/μmol",
            "characterization": [
              "HPLC"
            ],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge purification with 1.5 mL ethanol as eluent",
          "notes": "Same procedure applied to DP2 and DP3 to yield [68Ga]Ga-DP2 and [68Ga]Ga-DP3 with RCYs of 97.67 ± 1.05% and 98.01 ± 0.97%, respectively"
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Radiolabeling of fluorine-18 peptides via AlF chemistry",
      "target_compound_id": "C18",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "radionuclide trapping and elution",
          "reactants": [
            {
              "compound_id": "C12",
              "name": "Fluoride-18",
              "amount": "0.74–1.11 GBq"
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
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "trapped on QMA cartridge and eluted"
          },
          "product": {
            "compound_id": null,
            "name": "eluted fluoride-18 solution",
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
          "notes": "QMA cartridge preconditioned with saline and water"
        },
        {
          "step_number": 2,
          "reaction_type": "Al18F complexation and chelation",
          "reactants": [
            {
              "compound_id": "C06",
              "name": "NP1",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "aluminum chloride",
              "amount": "3 μL (2 mM in sodium acetate buffer)",
              "role": "chelation_catalyst"
            },
            {
              "name": "sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "100 μL",
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
            "other": null
          },
          "product": {
            "compound_id": "C18",
            "name": "[18F]AlF-NP1",
            "yield": "62.58 ± 0.32% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "13.13 ± 1.71 GBq/μmol",
            "characterization": [
              "HPLC"
            ],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge purification with 1.5 mL ethanol followed by solvent removal and formulation in saline",
          "notes": "Same procedure applied to NP2 to yield [18F]AlF-NP2 with RCY of 62.76 ± 0.22%"
        }
      ]
    }
  ]
}
```

##### Gemini_1
```
{
  "meta": {
    "prompt_version": "v2.2",
    "extraction_date": "2026-03-18",
    "has_synthesis": true,
    "synthesis_scale": "preclinical",
    "mechanism_discussed": "none",
    "method_completeness": "partial",
    "extraction_notes": "Synthesis routes for PR7, DP2, DP3, and NP2 are noted as custom-synthesized by a vendor (Nanchang Tanzhen Biotechnology) and detailed only in Supporting Information. Calculated masses reported in the text for peptides appear to be monoisotopic. Log P values provided are for the radiolabeled derivatives."
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
        "other": "retention time: 10.642 min"
      },
      "description": "A ROR1-targeted peptide lead compound used as the scaffold for further chemical modifications."
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
      "description": "An activated ester chelator used for coupling the DOTA group to the peptide."
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
      "description": "An activated ester chelator used for coupling the NOTA group to the peptide."
    },
    {
      "id": "C04",
      "name": "DIPEA",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial supplier",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "An organic base used in the peptide conjugation reaction."
    },
    {
      "id": "C05",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "retention time: 11.230 min"
      },
      "description": "A linear peptide conjugate of PR7 and DOTA synthesized in-house."
    },
    {
      "id": "C06",
      "name": "NP1",
      "iupac_name": null,
      "molecular_formula": "C108H152N28O36",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "retention time: 12.780 min"
      },
      "description": "A linear peptide conjugate of PR7 and NOTA synthesized in-house."
    },
    {
      "id": "C07",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": "retention time: 10.328 min"
      },
      "description": "A custom-synthesized cyclic peptide-DOTA conjugate precursor."
    },
    {
      "id": "C08",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": "retention time: 10.404 min"
      },
      "description": "A custom-synthesized cyclic peptide-DOTA conjugate precursor with a specific linker."
    },
    {
      "id": "C09",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd.",
      "physicochemical_properties": {
        "log_p": null,
        "other": "retention time: 10.620 min"
      },
      "description": "A custom-synthesized cyclic peptide-NOTA conjugate precursor."
    },
    {
      "id": "C10",
      "name": "68GaCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "ITM 68Ge-68Ga generator",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "The radionuclide source used for Gallium-68 labeling of DOTA-conjugated peptides."
    },
    {
      "id": "C11",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "-2.19 ± 0.05",
        "other": "stability >90% RCP in saline and FBS after 2 h"
      },
      "description": "A 68Ga-labeled linear peptide probe for PET imaging of ROR1 expression."
    },
    {
      "id": "C12",
      "name": "[68Ga]Ga-DP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "-2.53 ± 0.04",
        "other": null
      },
      "description": "A 68Ga-labeled cyclic peptide probe targeting ROR1."
    },
    {
      "id": "C13",
      "name": "[68Ga]Ga-DP3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "-1.82 ± 0.03",
        "other": null
      },
      "description": "A 68Ga-labeled cyclic peptide probe with a cysteine-based linker targeting ROR1."
    },
    {
      "id": "C14",
      "name": "[18F]fluoride",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Cyclone 18/9 cyclotron",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "The radionuclide source used for Fluorine-18 labeling via the AlF method."
    },
    {
      "id": "C15",
      "name": "AlCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial supplier",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Used to form the [Al18F]2+ complex for radiolabeling NOTA-conjugated peptides."
    },
    {
      "id": "C16",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "-2.10 ± 0.04",
        "other": "rapid metabolic degradation in urine observed"
      },
      "description": "An 18F-labeled linear peptide probe for PET imaging of ROR1 expression."
    },
    {
      "id": "C17",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "-2.54 ± 0.04",
        "other": null
      },
      "description": "An 18F-labeled cyclic peptide probe targeting ROR1."
    },
    {
      "id": "C18",
      "name": "sodium acetate buffer (0.25 M, pH 6.5)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Buffer used to adjust the pH of the 68Ga solution for radiolabeling."
    },
    {
      "id": "C19",
      "name": "sodium acetate buffer (0.1 M, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": null,
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Buffer used to maintain the acidic pH required for AlF complexation."
    }
  ],
  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of DP1",
      "target_compound_id": "C05",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amine acylation",
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
          "purification": "semipreparative HPLC with UV detection at 254 nm; obtained after lyophilization",
          "notes": "Purification method details found in Experimental Section 5.2.1."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of NP1",
      "target_compound_id": "C06",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amine acylation",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 μmol)"
            }
          ],
          "reagents": [
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
            "compound_id": "C06",
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
          "purification": "semipreparative HPLC with UV detection at 254 nm; obtained after lyophilization",
          "notes": "Purification method details found in Experimental Section 5.2.1."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "68Ga Radiolabeling of DP1",
      "target_compound_id": "C11",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3",
              "amount": "1 mL (0.74–1.11 GBq in 0.1 M HCl)"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate buffer (0.25 M, pH 6.5)",
              "amount": "0.5 mL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": "room temperature",
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4.0–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "pH-adjusted 68GaCl3 solution",
            "yield": null,
            "purity": null,
            "molar_activity": null,
            "characterization": [],
            "ms_data": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "complexation",
          "reactants": [
            {
              "compound_id": null,
              "name": "pH-adjusted 68GaCl3 solution",
              "amount": null
            },
            {
              "compound_id": "C05",
              "name": "DP1",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "ph": "4.0–4.5",
            "other": "cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C11",
            "name": "[68Ga]Ga-DP1",
            "yield": "89.55 ± 0.12% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "14.37 ± 0.97 GBq/μmol",
            "characterization": [
              "HPLC"
            ],
            "ms_data": null,
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge elution with 1.5 mL ethanol; final resolution in saline",
          "notes": "n ≥ 3 for molar activity."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "18F Radiolabeling of NP1",
      "target_compound_id": "C16",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "radionuclide processing",
          "reactants": [
            {
              "compound_id": "C14",
              "name": "[18F]fluoride",
              "amount": "0.74–1.11 GBq"
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
            "temperature": "room temperature",
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "trapped on preconditioned QMA cartridge and eluted"
          },
          "product": {
            "compound_id": null,
            "name": "eluted [18F]fluoride",
            "yield": null,
            "purity": null,
            "molar_activity": null,
            "characterization": [],
            "ms_data": null,
            "hplc_retention_time_min": null
          },
          "purification": null,
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "complexation",
          "reactants": [
            {
              "compound_id": null,
              "name": "eluted [18F]fluoride",
              "amount": "0.2 mL"
            },
            {
              "compound_id": "C06",
              "name": "NP1",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "AlCl3",
              "amount": "3 μL (2 mM in 0.1 M NaOAc buffer, pH 4.0)",
              "role": "chelation_catalyst"
            },
            {
              "name": "sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "100 μL",
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
            "ph": "4.0",
            "other": "cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C16",
            "name": "[18F]AlF-NP1",
            "yield": "62.58 ± 0.32% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "13.13 ± 1.71 GBq/μmol",
            "characterization": [
              "HPLC"
            ],
            "ms_data": null,
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge elution with 1.5 mL ethanol; final resolution in saline after solvent removal",
          "notes": "n ≥ 3 for molar activity."
        }
      ]
    }
  ]
}
```


##### Claude_1:
```
{
  "meta": {
    "prompt_version": "v2.2",
    "extraction_date": "2026-03-18",
    "has_synthesis": true,
    "synthesis_scale": "preclinical",
    "mechanism_discussed": "synthetic",
    "method_completeness": "partial",
    "extraction_notes": "Detailed synthetic routes for DP2, DP3, NP2, and PR7 are described as custom syntheses by an external vendor (Nanchang Tanzhen Biotechnology Co., Ltd.) and are not reported in-house; only HPLC retention times and ESI-MS data are provided in the main text for these compounds. Full synthetic schemes (Schemes S1–S5) are in Supporting Information and not available in the provided text. Radiochemical yields and molar activities are reported as mean ± SD (n ≥ 3) as stated in Table S1 (SI); summary values are given in the main text. Calculated exact masses for DP2 (2743.2514) and DP3 (3015.2514) appear to be nominal/average masses rather than monoisotopic masses given their size and the number of decimal places reported; noted accordingly. The [18F]fluoride trapping step on QMA and subsequent AlF chelation are treated as two separate steps per Step Granularity rules."
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
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.642 min; >95% purity by HPLC"
      },
      "description": "ROR1-targeting linear peptide lead compound with high affinity (KD = 1.57 × 10−9 M) and exceptional internalization efficiency, used as the starting scaffold for chelator conjugation to produce DP1 and NP1, and also used as a blocking agent in competition studies."
    },
    {
      "id": "C02",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "N-hydroxysuccinimide ester of DOTA chelator used as the activated coupling reagent for conjugation to PR7 to produce DP1."
    },
    {
      "id": "C03",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "N-hydroxysuccinimide ester of NOTA chelator used as the activated coupling reagent for conjugation to PR7 to produce NP1."
    },
    {
      "id": "C04",
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
      "description": "Hindered organic base (N,N-diisopropylethylamine) used to facilitate the NHS-ester amide coupling reactions for synthesis of DP1 and NP1."
    },
    {
      "id": "C05",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "-2.19 ± 0.05",
        "other": "HPLC retention time: 11.230 min; >95% purity by HPLC"
      },
      "description": "DOTA-conjugated linear ROR1-targeting peptide precursor derived from PR7, synthesised in-house and used as the radiolabeling precursor for preparation of [68Ga]Ga-DP1."
    },
    {
      "id": "C06",
      "name": "NP1",
      "iupac_name": null,
      "molecular_formula": "C108H152N28O36",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "-2.10 ± 0.04",
        "other": "HPLC retention time: 12.780 min; >95% purity by HPLC"
      },
      "description": "NOTA-conjugated linear ROR1-targeting peptide precursor derived from PR7, synthesised in-house and used as the radiolabeling precursor for preparation of [18F]AlF-NP1."
    },
    {
      "id": "C07",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": "-2.53 ± 0.04",
        "other": "HPLC retention time: 10.328 min; >95% purity by HPLC"
      },
      "description": "DOTA-conjugated cyclic ROR1-targeting peptide precursor (cyclic variant of PR7 scaffold) custom synthesised externally and used as the radiolabeling precursor for [68Ga]Ga-DP2."
    },
    {
      "id": "C08",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": "-1.82 ± 0.03",
        "other": "HPLC retention time: 10.404 min; >95% purity by HPLC"
      },
      "description": "DOTA-conjugated cyclic ROR1-targeting peptide precursor containing disulfide linkage(s), custom synthesised externally and used as the radiolabeling precursor for [68Ga]Ga-DP3."
    },
    {
      "id": "C09",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": "-2.54 ± 0.04",
        "other": "HPLC retention time: 10.620 min; >95% purity by HPLC"
      },
      "description": "NOTA-conjugated cyclic ROR1-targeting peptide precursor custom synthesised externally and used as the radiolabeling precursor for [18F]AlF-NP2."
    },
    {
      "id": "C10",
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
      "description": "Gallium-68 chloride radionuclide source eluted from the 68Ge–68Ga generator in 0.1 M HCl, used as the radiolabeling agent for 68Ga-DOTA chelation to produce [68Ga]Ga-DP1, [68Ga]Ga-DP2, and [68Ga]Ga-DP3."
    },
    {
      "id": "C11",
      "name": "sodium acetate buffer (0.25 M, pH 6.5)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate solution used to dilute and adjust the pH of the 68GaCl3 solution to pH 4–4.5 prior to radiolabeling with DOTA-peptide precursors."
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
        "log_p": "-2.19 ± 0.05",
        "other": null
      },
      "description": "68Ga-radiolabeled DOTA-conjugated linear ROR1-targeting peptide, the lead 68Ga radiotracer evaluated for PET imaging of ROR1 expression in multiple tumor-bearing mouse models."
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
        "log_p": "-2.53 ± 0.04",
        "other": null
      },
      "description": "68Ga-radiolabeled DOTA-conjugated cyclic ROR1-targeting peptide radiotracer evaluated by PET imaging in MC38 tumor-bearing mice."
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
        "log_p": "-1.82 ± 0.03",
        "other": null
      },
      "description": "68Ga-radiolabeled DOTA-conjugated cyclic ROR1-targeting peptide radiotracer evaluated by PET imaging in MC38 tumor-bearing mice."
    },
    {
      "id": "C15",
      "name": "[18F]fluoride",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "produced in-house via 18O(p,n)18F reaction on Cyclone 18/9 cyclotron (IBA, Belgium), Center for Molecular Imaging and Translational Medicine, Xiamen University",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Fluorine-18 radionuclide source produced by proton bombardment of 18O-enriched water, used as the radiolabeling agent for AlF-NOTA chelation to produce [18F]AlF-NP1 and [18F]AlF-NP2."
    },
    {
      "id": "C16",
	      "name": "aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, 0.1 M sodium acetate, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Aluminum(III) chloride solution providing Al3+ ions as the bridging metal for AlF-NOTA radiolabeling, enabling 18F incorporation into NOTA-peptide precursors via aluminum fluoride chelation."
    },
    {
      "id": "C17",
      "name": "sodium acetate buffer (0.1 M, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate buffer used to provide the reaction medium for AlF-NOTA radiolabeling of NP1 and NP2."
    },
    {
      "id": "C18",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "-2.10 ± 0.04",
        "other": null
      },
      "description": "18F-labeled aluminum fluoride NOTA-conjugated linear ROR1-targeting peptide, the lead 18F radiotracer demonstrating excellent tumor targeting and favorable pharmacokinetics for PET imaging of ROR1 expression."
    },
    {
      "id": "C19",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "-2.54 ± 0.04",
        "other": null
      },
      "description": "18F-labeled aluminum fluoride NOTA-conjugated cyclic ROR1-targeting peptide radiotracer evaluated in parallel with [18F]AlF-NP1, showing lower tumor uptake and higher renal accumulation."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of DP1 (DOTA-PR7 conjugate)",
      "target_compound_id": "C05",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling",
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
            "other": "agitation in an oscillator"
          },
          "product": {
            "compound_id": "C05",
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
                  "adduct": "[M + 2H]2+",
                  "mz": 1260.54
                },
                {
                  "adduct": "[M + 3H]3+",
                  "mz": 840.68
                }
              ]
            },
            "hplc_retention_time_min": 11.230
          },
          "purification": "Semipreparative HPLC with UV detection at 254 nm; lyophilization after collection. Mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "Reaction performed in a 2 mL centrifugation tube. DP1 and NP1 were prepared in the same reaction setup using DOTA-NHS or NOTA-NHS respectively; these are recorded as separate pathways per extraction rules."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of NP1 (NOTA-PR7 conjugate)",
      "target_compound_id": "C06",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 μmol)"
            }
          ],
          "reagents": [
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
            "other": "agitation in an oscillator"
          },
          "product": {
            "compound_id": "C06",
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
                  "adduct": "[M + 2H]2+",
                  "mz": 1210.22
                },
                {
                  "adduct": "[M + 3H]3+",
                  "mz": 807.00
                }
              ]
            },
            "hplc_retention_time_min": 12.780
          },
          "purification": "Semipreparative HPLC with UV detection at 254 nm; lyophilization after collection. Mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "Reaction performed in a 2 mL centrifugation tube. Performed in the same experimental setup as DP1 synthesis, substituting NOTA-NHS for DOTA-NHS."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP1",
      "target_compound_id": "C12",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
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
          "notes": "Resulting pH 4–4.5 solution was immediately transferred to the vial containing the precursor."
        },
        {
          "step_number": 2,
          "reaction_type": "radiometal chelation (68Ga-DOTA complexation)",
          "reactants": [
            {
              "compound_id": null,
              "name": "68GaCl3–sodium acetate solution at pH 4–4.5",
              "amount": "1.5 mL"
            },
            {
              "compound_id": "C05",
              "name": "DP1",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "other": "cooled to room temperature after reaction"
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol. Radio-HPLC analysis: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "n ≥ 3 replicates. Precursor dissolved in 50 μL DMSO prior to transfer. RCY and molar activity values from Table S1 (SI) as summarised in the main text."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP2",
      "target_compound_id": "C13",
      "target_compound_name": "[68Ga]Ga-DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
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
          "reaction_type": "radiometal chelation (68Ga-DOTA complexation)",
          "reactants": [
            {
              "compound_id": null,
              "name": "68GaCl3–sodium acetate solution at pH 4–4.5",
              "amount": "1.5 mL"
            },
            {
              "compound_id": "C07",
              "name": "DP2",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "other": "cooled to room temperature after reaction"
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol. Radio-HPLC analysis: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "n ≥ 3 replicates. Precursor dissolved in 50 μL DMSO prior to transfer."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP3",
      "target_compound_id": "C14",
      "target_compound_name": "[68Ga]Ga-DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
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
          "reaction_type": "radiometal chelation (68Ga-DOTA complexation)",
          "reactants": [
            {
              "compound_id": null,
              "name": "68GaCl3–sodium acetate solution at pH 4–4.5",
              "amount": "1.5 mL"
            },
            {
              "compound_id": "C08",
              "name": "DP3",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "other": "cooled to room temperature after reaction"
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol. Radio-HPLC analysis: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "n ≥ 3 replicates. Precursor dissolved in 50 μL DMSO prior to transfer."
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Radiolabeling of [18F]AlF-NP1",
      "target_compound_id": "C18",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "18F trapping on QMA cartridge and elution",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "[18F]fluoride",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline (for QMA preconditioning)",
              "volume": "10 mL"
            },
            {
              "name": "pure water (for QMA preconditioning)",
              "volume": "10 mL"
            },
            {
              "name": "saline (elution)",
              "volume": "0.2 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride eluate in saline",
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
          "notes": "QMA cartridge preconditioned sequentially with 10 mL saline then 10 mL pure water before trapping."
        },
        {
          "step_number": 2,
          "reaction_type": "AlF-NOTA radiolabeling (18F aluminum fluoride chelation)",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride eluate in saline",
              "amount": "0.2 mL"
            },
            {
              "compound_id": "C06",
              "name": "NP1",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, 0.1 M, pH 4.0)",
              "amount": "3 μL",
              "role": "chelation_catalyst"
            },
            {
              "name": "sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "100 μL",
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
            "other": "cooled to room temperature after reaction; ethanol solvent removed after purification; final product resolved in saline"
          },
          "product": {
            "compound_id": "C18",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol. Ethanol solvent removed; final product resolved in saline. Radio-HPLC analysis: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "n ≥ 3 replicates. Precursor dissolved in 50 μL DMSO. All components combined in one vial prior to heating."
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Radiolabeling of [18F]AlF-NP2",
      "target_compound_id": "C19",
      "target_compound_name": "[18F]AlF-NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "18F trapping on QMA cartridge and elution",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "[18F]fluoride",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline (for QMA preconditioning)",
              "volume": "10 mL"
            },
            {
              "name": "pure water (for QMA preconditioning)",
              "volume": "10 mL"
            },
            {
              "name": "saline (elution)",
              "volume": "0.2 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride eluate in saline",
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
          "notes": "QMA cartridge preconditioned sequentially with 10 mL saline then 10 mL pure water before trapping."
        },
        {
          "step_number": 2,
          "reaction_type": "AlF-NOTA radiolabeling (18F aluminum fluoride chelation)",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride eluate in saline",
              "amount": "0.2 mL"
            },
            {
              "compound_id": "C09",
              "name": "NP2",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, 0.1 M, pH 4.0)",
              "amount": "3 μL",
              "role": "chelation_catalyst"
            },
            {
              "name": "sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "100 μL",
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
            "other": "cooled to room temperature after reaction; ethanol solvent removed after purification; final product resolved in saline"
          },
          "product": {
            "compound_id": "C19",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol. Ethanol solvent removed; final product resolved in saline. Radio-HPLC analysis: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min, flow rate 1 mL/min.",
          "notes": "n ≥ 3 replicates. Precursor dissolved in 50 μL DMSO. Identical procedure to [18F]AlF-NP1 radiolabeling but using NP2 precursor."
        }
      ]
    }
  ]
}
```

##### Claude_2
```
{
  "meta": {
    "prompt_version": "v2.2",
    "extraction_date": "2026-03-19",
    "has_synthesis": true,
    "synthesis_scale": "preclinical",
    "mechanism_discussed": "synthetic",
    "method_completeness": "partial",
    "extraction_notes": "Detailed synthetic routes for DP1 and NP1 are provided in the main text (Section 5.2.1). Synthetic routes for PR7, DP2, DP3, and NP2 are described only as custom-synthesized externally (Section 5.2.2), with detailed routes in Schemes S1-S5 (Supporting Information not provided). Radiolabeling procedures for all five radiotracers are fully described in Section 5.4. MS data for DP2, DP3, and NP2 include calculated masses that appear to be average/nominal masses rather than monoisotopic masses (e.g., DP2 calcd 2743.2514 and DP3 calcd 3015.2514 are given to 4 decimal places but the values match average MW more closely for large peptides). RCY and molar activity values are from Table S1 as summarized in the main text. HPLC retention times for the radiotracers are not reported in the main text. Log P values are reported for radiolabeled products only."
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
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "KD = 1.57 × 10−9 M for ROR1; docking score −8.8 kcal/mol"
      },
      "description": "ROR1-targeting lead peptide used as a starting material for conjugation with DOTA-NHS or NOTA-NHS to produce DP1 and NP1, and also used as a blocking agent in cell uptake, PET imaging, and autoradiography competition experiments."
    },
    {
      "id": "C02",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "N-hydroxysuccinimide ester of DOTA used as an activated chelator reagent for conjugation to PR7 to produce the DP1 precursor."
    },
    {
      "id": "C03",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "N-hydroxysuccinimide ester of NOTA used as an activated chelator reagent for conjugation to PR7 to produce the NP1 precursor."
    },
    {
      "id": "C04",
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
      "description": "N,N-diisopropylethylamine used as a base in the coupling reaction between PR7 and DOTA-NHS or NOTA-NHS."
    },
    {
      "id": "C05",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Docking score −9.1 kcal/mol; HPLC retention time 11.230 min; purity >95% by HPLC"
      },
      "description": "DOTA-conjugated linear PR7 peptide precursor synthesized in-house by coupling PR7 with DOTA-NHS, serving as the radiolabeling precursor for [68Ga]Ga-DP1."
    },
    {
      "id": "C06",
      "name": "NP1",
      "iupac_name": null,
      "molecular_formula": "C108H152N28O36",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Docking score −8.3 kcal/mol; HPLC retention time 12.780 min; purity >95% by HPLC"
      },
      "description": "NOTA-conjugated linear PR7 peptide precursor synthesized in-house by coupling PR7 with NOTA-NHS, serving as the radiolabeling precursor for [18F]AlF-NP1."
    },
    {
      "id": "C07",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Docking score −7.7 kcal/mol; HPLC retention time 10.328 min; purity >95% by HPLC"
      },
      "description": "Cyclic DOTA-conjugated peptide precursor custom synthesized externally, used as the radiolabeling precursor for [68Ga]Ga-DP2."
    },
    {
      "id": "C08",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Docking score −7.9 kcal/mol; HPLC retention time 10.404 min; purity >95% by HPLC"
      },
      "description": "Cyclic DOTA-conjugated peptide precursor custom synthesized externally, used as the radiolabeling precursor for [68Ga]Ga-DP3."
    },
    {
      "id": "C09",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Docking score −7.6 kcal/mol; HPLC retention time 10.620 min; purity >95% by HPLC"
      },
      "description": "Cyclic NOTA-conjugated peptide precursor custom synthesized externally, used as the radiolabeling precursor for [18F]AlF-NP2."
    },
    {
      "id": "C10",
      "name": "68GaCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "68Ge-68Ga generator (ITM)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Gallium-68 trichloride eluted from a 68Ge/68Ga generator and used as the radionuclide source for 68Ga-labeling of DOTA-peptide precursors DP1, DP2, and DP3."
    },
    {
      "id": "C11",
      "name": "sodium acetate buffer (0.25 M, pH 6.5)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate solution used to adjust the pH of the 68GaCl3 solution to pH 4–4.5 prior to addition to the DOTA-peptide precursor for 68Ga radiolabeling."
    },
    {
      "id": "C12",
      "name": "[18F]fluoride",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "cyclotron-produced via 18O(p,n)18F reaction, Cyclone 18/9 (IBA), Center for Molecular Imaging and Translational Medicine, Xiamen University",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Fluoride-18 produced by cyclotron and used as the radionuclide source for AlF-based 18F-labeling of NOTA-peptide precursors NP1 and NP2."
    },
    {
      "id": "C13",
      "name": "aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, 0.1 M sodium acetate, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Aluminum chloride solution in sodium acetate buffer serving as the aluminum source for Al18F chelation with NOTA-peptide precursors in the AlF radiolabeling method."
    },
    {
      "id": "C14",
      "name": "sodium acetate buffer (0.1 M, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate buffer used as reaction medium in the AlF radiolabeling of NOTA-peptide precursors NP1 and NP2."
    },
    {
      "id": "C15",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.19 ± 0.05",
        "other": "KD = 74.9 nM; molar activity 14.37 ± 0.97 GBq/μmol; RCP >90%; blood T1/2 = 7.62 min"
      },
      "description": "68Ga-labeled DOTA-linear PR7 peptide radiotracer, the primary 68Ga candidate evaluated by PET imaging for ROR1 expression in multiple tumor models."
    },
    {
      "id": "C16",
      "name": "[68Ga]Ga-DP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.53 ± 0.04",
        "other": "KD = 154.9 nM; molar activity 20.05 ± 1.35 GBq/μmol; RCP >90%"
      },
      "description": "68Ga-labeled DOTA-cyclic peptide radiotracer evaluated by PET imaging for ROR1 targeting, showing comparable tumor uptake to [68Ga]Ga-DP1 but higher renal accumulation."
    },
    {
      "id": "C17",
      "name": "[68Ga]Ga-DP3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−1.82 ± 0.03",
        "other": "KD = 213.4 nM; molar activity 14.09 ± 2.12 GBq/μmol; RCP >90%"
      },
      "description": "68Ga-labeled DOTA-cyclic peptide radiotracer evaluated by PET imaging for ROR1 targeting, showing lower tumor uptake compared to [68Ga]Ga-DP1 and [68Ga]Ga-DP2."
    },
    {
      "id": "C18",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.10 ± 0.04",
        "other": "KD = 141.7 nM; molar activity 13.13 ± 1.71 GBq/μmol; RCP >90%; blood T1/2 = 19.32 min"
      },
      "description": "18F-labeled AlF-NOTA-linear PR7 peptide radiotracer, a primary candidate evaluated by PET imaging for ROR1 expression in multiple tumor models, demonstrating excellent tumor targeting and renal clearance."
    },
    {
      "id": "C19",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.54 ± 0.04",
        "other": "KD = 212.1 nM; molar activity 13.42 ± 1.25 GBq/μmol; RCP >90%"
      },
      "description": "18F-labeled AlF-NOTA-cyclic peptide radiotracer evaluated for ROR1 targeting, showing lower tumor uptake and higher renal accumulation compared to [18F]AlF-NP1."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of DP1 (DOTA-PR7 conjugate)",
      "target_compound_id": "C05",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling",
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
            "compound_id": "C05",
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
                  "adduct": "[M + 2H]2+",
                  "mz": 1260.54
                },
                {
                  "adduct": "[M + 3H]3+",
                  "mz": 840.68
                }
              ]
            },
            "hplc_retention_time_min": 11.230
          },
          "purification": "Semipreparative HPLC with UV detection at 254 nm; mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min, flow rate 1 mL/min; product obtained after lyophilization",
          "notes": "Reaction performed in a 2 mL centrifugation tube. DP1 and NP1 were synthesized in the same experimental procedure using the same batch of PR7 with either DOTA-NHS or NOTA-NHS."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of NP1 (NOTA-PR7 conjugate)",
      "target_compound_id": "C06",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling",
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
            "compound_id": "C06",
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
                  "adduct": "[M + 2H]2+",
                  "mz": 1210.22
                },
                {
                  "adduct": "[M + 3H]3+",
                  "mz": 807.00
                }
              ]
            },
            "hplc_retention_time_min": 12.780
          },
          "purification": "Semipreparative HPLC with UV detection at 254 nm; mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min, flow rate 1 mL/min; product obtained after lyophilization",
          "notes": "Reaction performed in a 2 mL centrifugation tube. NP1 and DP1 were synthesized in the same experimental procedure using the same batch of PR7 with either NOTA-NHS or DOTA-NHS."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP1",
      "target_compound_id": "C15",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "pH-adjusted 68GaCl3–sodium acetate solution (pH 4–4.5)",
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
          "notes": "The diluted and pH-adjusted 68GaCl3 solution was then transferred to the vial containing the precursor."
        },
        {
          "step_number": 2,
          "reaction_type": "radiometal chelation (68Ga complexation with DOTA)",
          "reactants": [
            {
              "compound_id": null,
              "name": "pH-adjusted 68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL"
            },
            {
              "compound_id": "C05",
              "name": "DP1 precursor",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "other": "cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C15",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluent: 1.5 mL ethanol; after purification ethanol solvent removed and final product resolved in saline",
          "notes": "n ≥ 3 replicates. Radio-HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B at 20 min, flow rate 1 mL/min. RCY, RCP, and molar activity values are from Table S1 as summarized in the main text."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP2",
      "target_compound_id": "C16",
      "target_compound_name": "[68Ga]Ga-DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "pH-adjusted 68GaCl3–sodium acetate solution (pH 4–4.5)",
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
          "reaction_type": "radiometal chelation (68Ga complexation with DOTA)",
          "reactants": [
            {
              "compound_id": null,
              "name": "pH-adjusted 68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL"
            },
            {
              "compound_id": "C07",
              "name": "DP2 precursor",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "other": "cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C16",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluent: 1.5 mL ethanol; after purification ethanol solvent removed and final product resolved in saline",
          "notes": "n ≥ 3 replicates. Same radio-HPLC method as [68Ga]Ga-DP1."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP3",
      "target_compound_id": "C17",
      "target_compound_name": "[68Ga]Ga-DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "pH-adjusted 68GaCl3–sodium acetate solution (pH 4–4.5)",
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
          "reaction_type": "radiometal chelation (68Ga complexation with DOTA)",
          "reactants": [
            {
              "compound_id": null,
              "name": "pH-adjusted 68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL"
            },
            {
              "compound_id": "C08",
              "name": "DP3 precursor",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "other": "cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C17",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluent: 1.5 mL ethanol; after purification ethanol solvent removed and final product resolved in saline",
          "notes": "n ≥ 3 replicates. Same radio-HPLC method as [68Ga]Ga-DP1."
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Radiolabeling of [18F]AlF-NP1",
      "target_compound_id": "C18",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "[18F]fluoride trapping on QMA cartridge",
          "reactants": [
            {
              "compound_id": "C12",
              "name": "[18F]fluoride",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline",
              "volume": "10 mL (preconditioning)"
            },
            {
              "name": "pure water",
              "volume": "10 mL (preconditioning)"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
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
          "notes": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water prior to trapping."
        },
        {
          "step_number": 2,
          "reaction_type": "[18F]fluoride elution from QMA cartridge",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride trapped on QMA cartridge",
              "amount": null
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
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride in saline eluate",
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
          "notes": "Saline eluate collected into a reaction vial pre-loaded with AlCl3 solution, acetonitrile, sodium acetate buffer, and the NP1 precursor."
        },
        {
          "step_number": 3,
          "reaction_type": "Al18F complexation with NOTA-peptide (AlF radiolabeling)",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride in saline eluate",
              "amount": "0.2 mL"
            },
            {
              "compound_id": "C06",
              "name": "NP1 precursor",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, 0.1 M sodium acetate, pH 4.0)",
              "amount": "3 μL",
              "role": "chelation_catalyst"
            },
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
              "volume": "50 μL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C18",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluent: 1.5 mL ethanol; ethanol solvent removed after purification and final product resolved in saline",
          "notes": "n ≥ 3 replicates. Radio-HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B at 20 min, flow rate 1 mL/min."
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Radiolabeling of [18F]AlF-NP2",
      "target_compound_id": "C19",
      "target_compound_name": "[18F]AlF-NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "[18F]fluoride trapping on QMA cartridge",
          "reactants": [
            {
              "compound_id": "C12",
              "name": "[18F]fluoride",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline",
              "volume": "10 mL (preconditioning)"
            },
            {
              "name": "pure water",
              "volume": "10 mL (preconditioning)"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
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
          "notes": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water prior to trapping."
        },
        {
          "step_number": 2,
          "reaction_type": "[18F]fluoride elution from QMA cartridge",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride trapped on QMA cartridge",
              "amount": null
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
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride in saline eluate",
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
          "step_number": 3,
          "reaction_type": "Al18F complexation with NOTA-peptide (AlF radiolabeling)",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride in saline eluate",
              "amount": "0.2 mL"
            },
            {
              "compound_id": "C09",
              "name": "NP2 precursor",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, 0.1 M sodium acetate, pH 4.0)",
              "amount": "3 μL",
              "role": "chelation_catalyst"
            },
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
              "volume": "50 μL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C19",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluent: 1.5 mL ethanol; ethanol solvent removed after purification and final product resolved in saline",
          "notes": "n ≥ 3 replicates. Same radio-HPLC method as [18F]AlF-NP1."
        }
      ]
    }
  ]
}
```
##### Claude 3
```
{
  "meta": {
    "prompt_version": "v2.2",
    "extraction_date": "2026-03-19",
    "has_synthesis": true,
    "synthesis_scale": "preclinical",
    "mechanism_discussed": "synthetic",
    "method_completeness": "partial",
    "extraction_notes": "Detailed synthetic routes for DP1 and NP1 are provided in the main text (Section 5.2.1). Synthetic routes for PR7, DP2, DP3, and NP2 are stated to be in Schemes S1-S5 (Supporting Information); only HPLC retention times and ESI-MS data for these compounds appear in the main text (Section 5.2.2). Radiolabeling procedures for all five radiotracers are fully described in Section 5.4. The calculated exact masses for DP2 (2743.2514) and DP3 (3015.2514) appear to be average/nominal masses given their large peptide size rather than monoisotopic masses — recorded as stated. The molecular formula for PR7 (C96H133N25O31, calc. 2131.96) also appears to reflect a nominal/average mass. RCY values are reported as mean ± SD (n ≥ 3). Molar activity values are reported as mean ± SD (n ≥ 3). Log P values reported as mean ± SD."
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
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "ROR1-targeting linear peptide used as the lead scaffold and starting material for conjugation to DOTA-NHS or NOTA-NHS to produce DP1 and NP1; also used as a blocking agent in cell and in vivo competition assays."
    },
    {
      "id": "C02",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "NHS ester-activated DOTA chelator used as a coupling reagent to conjugate DOTA to PR7, yielding the 68Ga-labeling precursor DP1."
    },
    {
      "id": "C03",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "NHS ester-activated NOTA chelator used as a coupling reagent to conjugate NOTA to PR7, yielding the 18F-AlF-labeling precursor NP1."
    },
    {
      "id": "C04",
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
      "description": "Organic base added to the conjugation reaction to facilitate NHS ester coupling of DOTA-NHS or NOTA-NHS to PR7."
    },
    {
      "id": "C05",
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
      "description": "DOTA-conjugated linear ROR1-targeting peptide precursor synthesized in-house by coupling DOTA-NHS to PR7; serves as the chelator-peptide precursor for 68Ga radiolabeling to produce [68Ga]Ga-DP1."
    },
    {
      "id": "C06",
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
      "description": "NOTA-conjugated linear ROR1-targeting peptide precursor synthesized in-house by coupling NOTA-NHS to PR7; serves as the chelator-peptide precursor for 18F-AlF radiolabeling to produce [18F]AlF-NP1."
    },
    {
      "id": "C07",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "DOTA-conjugated cyclic ROR1-targeting peptide precursor custom-synthesized externally; serves as the precursor for 68Ga radiolabeling to produce [68Ga]Ga-DP2."
    },
    {
      "id": "C08",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "DOTA-conjugated cyclic ROR1-targeting peptide precursor custom-synthesized externally; serves as the precursor for 68Ga radiolabeling to produce [68Ga]Ga-DP3."
    },
    {
      "id": "C09",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "NOTA-conjugated cyclic ROR1-targeting peptide precursor custom-synthesized externally; serves as the precursor for 18F-AlF radiolabeling to produce [18F]AlF-NP2."
    },
    {
      "id": "C10",
      "name": "68GaCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "68Ge-68Ga generator (ITM)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Gallium-68 chloride radionuclide source obtained from a 68Ge/68Ga generator; used as the radiometal source for 68Ga labeling of DOTA-peptide precursors DP1, DP2, and DP3."
    },
    {
      "id": "C11",
      "name": "Sodium acetate buffer (0.25 M, pH 6.5)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate solution used to dilute and adjust the pH of the 68GaCl3 solution to pH 4–4.5 prior to the 68Ga chelation reaction."
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
        "log_p": "-2.19 ± 0.05",
        "other": null
      },
      "description": "68Ga-radiolabeled DOTA-conjugated linear ROR1-targeting peptide; a lead PET radiotracer evaluated extensively in vitro and in vivo for ROR1-targeted tumor imaging."
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
        "log_p": "-2.53 ± 0.04",
        "other": null
      },
      "description": "68Ga-radiolabeled DOTA-conjugated cyclic ROR1-targeting peptide evaluated by PET imaging in MC38 tumor-bearing mice."
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
        "log_p": "-1.82 ± 0.03",
        "other": null
      },
      "description": "68Ga-radiolabeled DOTA-conjugated cyclic ROR1-targeting peptide evaluated by PET imaging; showed lower tumor uptake than [68Ga]Ga-DP1."
    },
    {
      "id": "C15",
      "name": "[18F]fluoride",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Cyclone 18/9 cyclotron (IBA, Belgium), Center for Molecular Imaging and Translational Medicine, Xiamen University",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Fluorine-18 radionuclide produced via 18O(p,n)18F reaction; used as the radiofluorine source for 18F-AlF labeling of NOTA-peptide precursors NP1 and NP2."
    },
    {
      "id": "C16",
      "name": "Aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, 0.1 M sodium acetate, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Aluminum(III) chloride solution serving as the metal co-reagent that bridges 18F fluoride to the NOTA chelator in the Al18F radiolabeling of NP1 and NP2."
    },
    {
      "id": "C17",
      "name": "Sodium acetate buffer (0.1 M, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate buffer used as the reaction medium component during the 18F-AlF radiolabeling step to maintain appropriate pH conditions for Al18F-NOTA chelation."
    },
    {
      "id": "C18",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "-2.10 ± 0.04",
        "other": null
      },
      "description": "18F-labeled Al18F-NOTA-conjugated linear ROR1-targeting peptide; a lead PET radiotracer demonstrating excellent tumor targeting, renal clearance, and favorable biodistribution in multiple tumor models."
    },
    {
      "id": "C19",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "-2.54 ± 0.04",
        "other": null
      },
      "description": "18F-labeled Al18F-NOTA-conjugated cyclic ROR1-targeting peptide evaluated by PET imaging; showed lower tumor uptake and higher renal accumulation compared with [18F]AlF-NP1."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of DP1 (DOTA-PR7 conjugate)",
      "target_compound_id": "C05",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling",
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
            "other": "Agitated in an oscillator"
          },
          "product": {
            "compound_id": "C05",
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
          "purification": "Semipreparative HPLC with UV detection at 254 nm; followed by lyophilization. HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min; flow rate 1 mL/min.",
          "notes": "Reaction performed in a 2 mL centrifugation tube. DP1 and NP1 were synthesized in parallel in the same reaction setup using either DOTA-NHS or NOTA-NHS."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of NP1 (NOTA-PR7 conjugate)",
      "target_compound_id": "C06",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 μmol)"
            }
          ],
          "reagents": [
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
            "other": "Agitated in an oscillator"
          },
          "product": {
            "compound_id": "C06",
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
          "purification": "Semipreparative HPLC with UV detection at 254 nm; followed by lyophilization. HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min; flow rate 1 mL/min.",
          "notes": "Reaction performed in a 2 mL centrifugation tube. NP1 and DP1 were synthesized in parallel in the same reaction setup."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Characterization of externally synthesized precursors (PR7, DP2, DP3, NP2)",
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
          "notes": "PR7 was custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. Synthetic route described in Scheme S1 (Supporting Information). HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 23% B to 43% B over 20 min; flow rate 1 mL/min."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Characterization of externally synthesized precursor DP2",
      "target_compound_id": "C07",
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
            "compound_id": "C07",
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
          "notes": "DP2 was custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. Synthetic route described in Scheme S2 (Supporting Information). HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 23% B to 43% B over 20 min; flow rate 1 mL/min."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Characterization of externally synthesized precursor DP3",
      "target_compound_id": "C08",
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
            "compound_id": "C08",
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
          "notes": "DP3 was custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. Synthetic route described in Scheme S3 (Supporting Information). HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 23% B to 43% B over 20 min; flow rate 1 mL/min."
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Characterization of externally synthesized precursor NP2",
      "target_compound_id": "C09",
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
            "compound_id": "C09",
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
          "notes": "NP2 was custom synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. Synthetic route described in Scheme S5 (Supporting Information). HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 23% B to 43% B over 20 min; flow rate 1 mL/min."
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP1",
      "target_compound_id": "C12",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3",
              "amount": "1 mL (0.74–1.11 GBq in 0.1 M HCl)"
            }
          ],
          "reagents": [
            {
              "name": "Sodium acetate buffer",
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
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "pH-adjusted 68GaCl3–sodium acetate solution",
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
          "reaction_type": "Radiometal chelation (68Ga labeling)",
          "reactants": [
            {
              "compound_id": null,
              "name": "pH-adjusted 68GaCl3–sodium acetate solution",
              "amount": "1.5 mL (transferred from step 1)"
            },
            {
              "compound_id": "C05",
              "name": "DP1 (precursor)",
              "amount": "50 μg (16–20 nmol) in 50 μL DMSO"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 μL (used to dissolve precursor)"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to room temperature after reaction"
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL ethanol. After ethanol removal, final product dissolved in saline.",
          "notes": "RCY and molar activity reported as mean ± SD (n ≥ 3). Radio-HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min; flow rate 1 mL/min. Stability >90% RCP after 2 h in saline and fetal bovine serum."
        }
      ]
    },
    {
      "pathway_id": "P8",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP2",
      "target_compound_id": "C13",
      "target_compound_name": "[68Ga]Ga-DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3",
              "amount": "1 mL (0.74–1.11 GBq in 0.1 M HCl)"
            }
          ],
          "reagents": [
            {
              "name": "Sodium acetate buffer",
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
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "pH-adjusted 68GaCl3–sodium acetate solution",
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
          "reaction_type": "Radiometal chelation (68Ga labeling)",
          "reactants": [
            {
              "compound_id": null,
              "name": "pH-adjusted 68GaCl3–sodium acetate solution",
              "amount": "1.5 mL (transferred from step 1)"
            },
            {
              "compound_id": "C07",
              "name": "DP2 (precursor)",
              "amount": "50 μg (16–20 nmol) in 50 μL DMSO"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 μL (used to dissolve precursor)"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to room temperature after reaction"
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL ethanol. After ethanol removal, final product dissolved in saline.",
          "notes": "RCY and molar activity reported as mean ± SD (n ≥ 3). Stability >90% RCP after 2 h in saline and fetal bovine serum."
        }
      ]
    },
    {
      "pathway_id": "P9",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP3",
      "target_compound_id": "C14",
      "target_compound_name": "[68Ga]Ga-DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3",
              "amount": "1 mL (0.74–1.11 GBq in 0.1 M HCl)"
            }
          ],
          "reagents": [
            {
              "name": "Sodium acetate buffer",
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
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "pH-adjusted 68GaCl3–sodium acetate solution",
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
          "reaction_type": "Radiometal chelation (68Ga labeling)",
          "reactants": [
            {
              "compound_id": null,
              "name": "pH-adjusted 68GaCl3–sodium acetate solution",
              "amount": "1.5 mL (transferred from step 1)"
            },
            {
              "compound_id": "C08",
              "name": "DP3 (precursor)",
              "amount": "50 μg (16–20 nmol) in 50 μL DMSO"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 μL (used to dissolve precursor)"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to room temperature after reaction"
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL ethanol. After ethanol removal, final product dissolved in saline.",
          "notes": "RCY and molar activity reported as mean ± SD (n ≥ 3). Stability >90% RCP after 2 h in saline and fetal bovine serum."
        }
      ]
    },
    {
      "pathway_id": "P10",
      "pathway_name": "Radiolabeling of [18F]AlF-NP1",
      "target_compound_id": "C18",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Solid-phase [18F]fluoride trapping on QMA cartridge",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "[18F]fluoride",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "Saline (cartridge preconditioning)",
              "volume": "10 mL"
            },
            {
              "name": "Pure water (cartridge preconditioning)",
              "volume": "10 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water before trapping"
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
          "reaction_type": "Elution of [18F]fluoride and Al18F-NOTA chelation radiolabeling",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride trapped on QMA cartridge",
              "amount": "from step 1"
            },
            {
              "compound_id": "C06",
              "name": "NP1 (precursor)",
              "amount": "50 μg (18–25 nmol) in 50 μL DMSO"
            }
          ],
          "reagents": [
            {
              "name": "Aluminum chloride (AlCl3) in sodium acetate buffer",
              "amount": "3 μL (2 mM AlCl3 in 0.1 M sodium acetate buffer, pH 4.0)",
              "role": "chelation_catalyst"
            },
            {
              "name": "Sodium acetate buffer",
              "amount": "100 μL (0.1 M, pH 4.0)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "Saline (for elution of [18F]fluoride from QMA)",
              "volume": "0.2 mL"
            },
            {
              "name": "Acetonitrile",
              "volume": "200 μL"
            },
            {
              "name": "DMSO (precursor dissolution)",
              "volume": "50 μL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to room temperature after reaction"
          },
          "product": {
            "compound_id": "C18",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL ethanol. Ethanol solvent removed; final product dissolved in saline.",
          "notes": "RCY and molar activity reported as mean ± SD (n ≥ 3). Radio-HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min; flow rate 1 mL/min. Stability >90% RCP after 2 h in saline and fetal bovine serum. Approximately 4% intact probe detectable in urine at 0.5 h p.i.; almost none at 1 h p.i."
        }
      ]
    },
    {
      "pathway_id": "P11",
      "pathway_name": "Radiolabeling of [18F]AlF-NP2",
      "target_compound_id": "C19",
      "target_compound_name": "[18F]AlF-NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Solid-phase [18F]fluoride trapping on QMA cartridge",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "[18F]fluoride",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "Saline (cartridge preconditioning)",
              "volume": "10 mL"
            },
            {
              "name": "Pure water (cartridge preconditioning)",
              "volume": "10 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water before trapping"
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
          "reaction_type": "Elution of [18F]fluoride and Al18F-NOTA chelation radiolabeling",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride trapped on QMA cartridge",
              "amount": "from step 1"
            },
            {
              "compound_id": "C09",
              "name": "NP2 (precursor)",
              "amount": "50 μg (18–25 nmol) in 50 μL DMSO"
            }
          ],
          "reagents": [
            {
              "name": "Aluminum chloride (AlCl3) in sodium acetate buffer",
              "amount": "3 μL (2 mM AlCl3 in 0.1 M sodium acetate buffer, pH 4.0)",
              "role": "chelation_catalyst"
            },
            {
              "name": "Sodium acetate buffer",
              "amount": "100 μL (0.1 M, pH 4.0)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "Saline (for elution of [18F]fluoride from QMA)",
              "volume": "0.2 mL"
            },
            {
              "name": "Acetonitrile",
              "volume": "200 μL"
            },
            {
              "name": "DMSO (precursor dissolution)",
              "volume": "50 μL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to room temperature after reaction"
          },
          "product": {
            "compound_id": "C19",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL ethanol. Ethanol solvent removed; final product dissolved in saline.",
          "notes": "RCY and molar activity reported as mean ± SD (n ≥ 3). Stability >90% RCP after 2 h in saline and fetal bovine serum."
        }
      ]
    }
  ]
}
```





I have report the performance of version 2.1 and 2.2 at [[Prompt 2.1 and 2.2 Evaluation]]. Now from it I will conduct another 2.3 version prompt. This time to test that does trying to reinforce prompt can lead to consistency over time or I will need to find another approach.
#### v2.3 prompt

```
SYSTEM ROLE
You are an expert chemist and scientific information extraction specialist with deep knowledge of organic, medicinal, and radiochemical synthesis. Your task is to extract chemical synthesis information from the academic paper provided below with maximum precision.

---

CRITICAL EXTRACTION RULES — read before answering

1. ARTICLE-ONLY
Extract exclusively from the version of the paper provided to you (main text, schemes, figures, experimental section). If the paper references Supporting Information for details not present in your input, record null for those fields and note the SI reference in the step's "notes" field. Do NOT supplement with prior chemical knowledge.

2. NOT REPORTED
If a field's value is absent from the article, use null — never invent plausible values.

3. NEGATIVE CASE
If the paper contains NO synthesis, still return valid JSON with has_synthesis: false and all synthesis arrays empty.

4. YIELD FORMAT
Use "N mg (N%)" when both mass and percentage are stated; "N%" when only a percentage is given. For radiochemical yields, append the RCY suffix: "89.55 ± 0.12% RCY". ONE compound per yield string — never concatenate multiple compounds into a single yield field.

5. AMOUNTS FORMAT
Express amounts as "N unit (N unit)" for mass + moles (e.g. "6.4 mg (3 μmol)"). Use an en dash for ranges: "0.74–1.11 GBq". Never append solvent or concentration context into the amount string — those go in the solvents array or reagents list respectively.

6. COMPOUND ENTRIES — what to include
Include ALL compounds: final products, intermediates, catalysts, radiolabeled derivatives, and any named reagent that plays a defined mechanistic role. Specific inclusion rules:

- Radionuclide sources (e.g. 68GaCl3, [18F]fluoride, [64Cu]Cl2) always get their own compound entry.
- Inorganic reagents with a defined mechanistic role (e.g. AlCl3 in AlF radiolabeling, SnCl2 as a reductant) always get their own compound entry.
- Organic bases or activating agents named with an amount in a synthesis step (e.g. DIPEA, HATU, PyBOP) get their own compound entry.
- Buffer solutions: create one compound entry per distinct pH/concentration combination if each plays a mechanistically distinct role. Do not merge two buffers at different pH values into one entry.
- Pure solvents used only for dissolution or elution (e.g. DMSO, MeCN, EtOH, DCM) do NOT need compound entries — record them only in the solvents array of each step.

7. ROLE ASSIGNMENT — use these definitions exactly

Assign one role per compound. When in doubt, apply this decision tree in order:

- Is it a radiolabeled product (contains a radioisotope, produced in a radiolabeling step)? → radiolabeled_product. This takes priority over final_product even if the compound is biologically evaluated.
- Is it sourced externally (commercial supplier, custom order, vendor synthesis) and used directly as a substrate or precursor with no in-house chemical transformation? → starting_material
- Is it sourced externally and used as a consumable reagent (activating agent, chelator, base, buffer, radionuclide source)? → reagent
- Is it synthesised in-house and its sole purpose is to serve as input to a subsequent transformation (including radiolabeling)? → intermediate
- Is it synthesised in-house or externally and presented as a standalone biologically or pharmacologically evaluated deliverable, and does NOT contain a radioisotope? → final_product
- Is it used as a positive or negative control, reference standard, or blocking agent? → reference_compound
- Is it a metal, ligand, or co-ligand in a coordination or organometallic context? → catalyst or coligand as appropriate

Key distinctions:
- A compound is intermediate ONLY if it was made in-house in this study. An externally synthesised compound used as a radiolabeling precursor is starting_material, not intermediate, even if it is novel in structure.
- A compound is final_product only if the paper evaluates it as a standalone deliverable AND it does not contain a radioisotope. A chelator-peptide conjugate whose sole purpose is radiolabeling is intermediate, not final_product, even if it is characterised by HPLC and MS.
- radiolabeled_product always overrides final_product. If a compound contains a radioisotope and was produced in a radiolabeling step, it is radiolabeled_product regardless of how extensively it is evaluated.

8. is_newly_synthesized
Set to true only for compounds prepared in-house during this study. Set to false for all commercially purchased, custom-ordered, or externally synthesised compounds, regardless of whether the structure is novel.

9. method_completeness
Choose exactly one value:
- "full" — complete procedure is in the main text for all compounds and steps
- "partial" — at least one in-house procedure appears in the main text; others are in SI or unavailable
- "referenced_to_SI" — main text gives no procedural detail at all; all routes are in SI only
- "none" — no synthesis is reported

If the main text contains an explicit in-house synthesis procedure for even one compound, use "partial", not "referenced_to_SI".

10. STEP GRANULARITY
Each physically distinct operation that requires its own materials list is a separate numbered step, even if the paper narrates them in one paragraph. Indicators: different equipment, different reagents, different conditions, different vessel. Examples:
- Solid-phase resin loading and coupling are separate steps.
- QMA trapping and Al18F complexation are separate steps.
- pH adjustment of a radionuclide solution and the subsequent chelation reaction are separate steps.
- Elution of a trapped species from a cartridge and the subsequent reaction are separate steps.

11. INTERMEDIATE PRODUCTS IN MULTI-STEP SEQUENCES
The product block of every step must describe what is produced by that step — even if it is a transient intermediate (e.g. a pH-adjusted radionuclide solution, a resin-bound peptide after a single coupling). For transient intermediates that have no independent compound entry, use "compound_id": null and give a descriptive name. Never recycle the compound_id of an input to describe the output of the same step. Example: if C09 is the 68GaCl3 starting reagent, the pH-adjusted solution produced in Step 1 must use "compound_id": null, not "compound_id": "C09".

12. REAGENT vs CONDITIONS — where concentration and pH go
- The pH of the reaction mixture goes in conditions.ph.
- The concentration and pH of a reagent solution (e.g. a buffer added to the reaction) go in the reagent's amount field: "0.5 mL (0.25 M, pH 6.5)".
- Never duplicate: if a value is in the reagent amount field, do not also put it in conditions.

13. PURITY FORMAT
Always include the analytical method: ">95% by HPLC" for non-radioactive compounds; ">95% RCP by radio-HPLC" for radiolabeled products.

14. TEMPERATURE FORMAT
Use SI convention with a space: "95 °C", "-20 °C", "room temperature". Never "95°C".

15. HPLC RETENTION TIME
Record as a number in minutes in product.hplc_retention_time_min. If a retention time is reported only in a characterisation table and not in a synthesis yield statement, still record it in the synthesis step product block for that compound.

16. MS DATA — monoisotopic vs nominal mass
Record the calculated mass exactly as stated in the paper. For large peptides, authors sometimes report nominal or average masses rather than monoisotopic masses. When this is evident (e.g. the stated mass matches the average molecular weight rather than the monoisotopic mass), note it in paper.extraction_notes. Do not correct or recalculate.

17. ONE ENTRY PER COMPOUND
Each distinct substance gets exactly one compound entry and one ID. Assign IDs (C01, C02, ...) in the order compounds first appear in the paper. Do not skip IDs, do not reuse them, do not merge two substances into one entry.

18. NO CITATION ARTIFACTS
All string values must be plain prose. Strip citation tags, reference numbers, footnote markers, and retrieval-system metadata from all fields.

19. ONE PATHWAY PER TARGET COMPOUND
Each synthesis pathway (P1, P2, ...) targets exactly one compound. Never describe two distinct synthetic routes in one pathway entry using "or" / "alternatively" logic.

20. LOG P AND PHYSICOCHEMICAL PROPERTIES — source-of-truth rule
Record a physicochemical property (log P, KD, T½, etc.) only in the compound entry for the exact species in which it was measured. Never transfer a value from a radiolabeled product to its unlabeled precursor or vice versa, even if they share the same peptide backbone. If the paper does not explicitly state a log P for the unlabeled precursor, set log_p: null for that precursor.

---

OUTPUT SCHEMA

Return a single JSON object. Do not add any text before or after the JSON.

{
  "extraction": {
    "prompt_version": "v2.3",
    "extraction_date": "YYYY-MM-DD",
    "model_name": "string — name and version of the model used for this extraction",
    "extractor_notes": "string or null — notes about the extraction process, ambiguities encountered, SI references that were unavailable, and any caveats about mass type (monoisotopic vs nominal) for large peptides"
  },

  "paper": {
    "title": "string",
    "authors": ["string"],
    "doi": "string or null",
    "journal": "string or null",
    "year": "integer or null",
    "synthesis_scale": "lab | preclinical | gmp | none",
    "mechanism_discussed": "synthetic | biological_only | none",
    "method_completeness": "full | partial | referenced_to_SI | none",
    "has_synthesis": true,
    "extraction_notes": "string or null — paper-specific observations: unusual reporting conventions, missing SI, discrepancies in the source text"
  },

  "compounds": [
    {
      "id": "C01",
      "name": "string",
      "iupac_name": "string or null — only if explicitly stated in the paper",
      "molecular_formula": "string or null — only if explicitly stated",
      "role": "starting_material | intermediate | reagent | catalyst | coligand | radiolabeled_product | final_product | reference_compound",
      "is_newly_synthesized": true,
      "source": "string or null — in-house, commercial, or vendor name if stated",
      "physicochemical_properties": {
        "log_p": "string or null — only if explicitly reported for THIS compound in the paper",
        "other": "string or null"
      },
      "description": "one sentence of plain prose describing this compound's function in the study"
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "string",
      "target_compound_id": "C01",
      "target_compound_name": "string",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "string or null",
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
              "role": "coupling_reagent | base | acid | oxidant | reductant | catalyst | protecting_group_reagent | ph_adjuster | radionuclide_source | chelation_catalyst | other"
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
            "ph": "string or null — pH of the reaction mixture only",
            "other": "string or null — stirring mode, post-reaction cooling, special handling; vessel and equipment details go in notes"
          },
          "product": {
            "compound_id": "string or null — C-ID if the compound has an entry; null for transient intermediates",
            "name": "string",
            "yield": "string or null",
            "purity": "string or null",
            "molar_activity": "string or null — radiolabeled products only",
            "characterization": ["ESI-MS", "HPLC"],
            "ms_data": {
              "calculated_exact_mass": "number or null",
              "formula": "string or null",
              "observed_ions": [
                {
                  "adduct": "string",
                  "mz": "number or null"
                }
              ]
            },
            "hplc_retention_time_min": "number or null"
          },
          "purification": "string or null — method, catalog number if given, elution solvent and volume, post-purification formulation steps",
          "notes": "string or null — SI references, vessel and equipment details, n value for replicates, any procedural context not captured above"
        }
      ]
    }
  ]
}

```

##### Claude 1
```
{
  "extraction": {
    "prompt_version": "v2.3",
    "extraction_date": "2026-03-20",
    "model_name": "claude-sonnet-4-6",
    "extractor_notes": "Detailed synthetic routes for all five precursors (DP1, DP2, DP3, NP1, NP2) are referenced to Schemes S1–S5 in the Supporting Information, which is not available in this input. Only the synthesis of DP1 and NP1 has a partial procedure in the main text (Section 5.2.1). PR7, DP2, DP3, and NP2 were custom synthesized externally (Nanchang Tanzhen Biotechnology Co., Ltd.) with no in-house procedure reported. Radiolabeling procedures for all five radiotracers are given in Section 5.4 with sufficient detail to extract steps. MS calculated masses for large peptides (PR7, DP1, DP2, DP3, NP1, NP2) appear to be average/nominal masses rather than monoisotopic masses, consistent with their high molecular weights (>2100 Da); the paper does not explicitly state which mass type is reported, but the values match average molecular weights. Radiochemical yield (RCY) data and molar activity data for all five radiotracers are summarized in Table S1 (SI); values cited in the main text Section 2.2 are used here. HPLC retention times for radiotracers are not reported in the main text; only precursor retention times are given. Log P values are reported only for the five radiolabeled products. KD values are reported for the five radiolabeled products from saturation binding assays. The QMA cartridge trapping step and elution for [18F]AlF labeling are treated as separate steps per the extraction rules."
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
    "mechanism_discussed": "synthetic",
    "method_completeness": "partial",
    "has_synthesis": true,
    "extraction_notes": "Synthetic routes for DP1 and NP1 are partially described in the main text (Section 5.2.1); all other precursor routes are in Schemes S1–S5 (SI only). Radiolabeling procedures are fully described in the main text (Section 5.4). MS calculated masses for all peptide precursors are likely average masses given the high molecular weights; the paper does not clarify mass type. RCY values and molar activities are stated in the main text (Section 2.2) as means ± SD with n ≥ 3. Radiochemical purity stated as >90% in main text and >95% by radio-HPLC in Section 5.4; the more specific value from Section 5.4 is used for radiolabeled products."
  },

  "compounds": [
    {
      "id": "C01",
      "name": "PR7",
      "iupac_name": null,
      "molecular_formula": "C96H133N25O31",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "KD = 1.57 × 10−9 M (reported from prior literature, ref 38); HPLC retention time: 10.642 min; >95% pure by HPLC"
      },
      "description": "ROR1-targeting lead peptide used as the starting material for conjugation with DOTA-NHS or NOTA-NHS to produce DP1 and NP1, and as a blocking agent in cell and in vivo competition assays."
    },
    {
      "id": "C02",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "N-hydroxysuccinimide ester of DOTA used as the chelator-activating reagent for conjugation to PR7 to produce DP1."
    },
    {
      "id": "C03",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "N-hydroxysuccinimide ester of NOTA used as the chelator-activating reagent for conjugation to PR7 to produce NP1."
    },
    {
      "id": "C04",
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
      "description": "Diisopropylethylamine used as an organic base to facilitate NHS ester conjugation of PR7 with DOTA-NHS or NOTA-NHS."
    },
    {
      "id": "C05",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 11.230 min; >95% pure by HPLC; ESI-MS calcd 2518.14 (average mass); Bmax = 22158 (saturation binding, MC38 cells)"
      },
      "description": "DOTA-conjugated linear ROR1-targeting peptide precursor synthesized in-house from PR7 and DOTA-NHS, used as the radiolabeling precursor for [68Ga]Ga-DP1."
    },
    {
      "id": "C06",
      "name": "NP1",
      "iupac_name": null,
      "molecular_formula": "C108H152N28O36",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 12.780 min; >95% pure by HPLC; ESI-MS calcd 2417.09 (average mass); Bmax = 31406 (saturation binding, MC38 cells)"
      },
      "description": "NOTA-conjugated linear ROR1-targeting peptide precursor synthesized in-house from PR7 and NOTA-NHS, used as the radiolabeling precursor for [18F]AlF-NP1."
    },
    {
      "id": "C07",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.328 min; >95% pure by HPLC; ESI-MS calcd 2743.2514 (average mass); Bmax = 31268 (saturation binding, MC38 cells)"
      },
      "description": "Cyclic DOTA-peptide precursor custom synthesized externally, used as the radiolabeling precursor for [68Ga]Ga-DP2."
    },
    {
      "id": "C08",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.404 min; >95% pure by HPLC; ESI-MS calcd 3015.2514 (average mass); Bmax = 47017 (saturation binding, MC38 cells)"
      },
      "description": "Cyclic DOTA-peptide precursor (containing disulfide or thioether bridges based on sulfur content) custom synthesized externally, used as the radiolabeling precursor for [68Ga]Ga-DP3."
    },
    {
      "id": "C09",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.620 min; >95% pure by HPLC; ESI-MS calcd 2642.20 (average mass); Bmax = 22986 (saturation binding, MC38 cells)"
      },
      "description": "Cyclic NOTA-peptide precursor custom synthesized externally, used as the radiolabeling precursor for [18F]AlF-NP2."
    },
    {
      "id": "C10",
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
      "description": "Gallium-68 trichloride radionuclide source obtained from a 68Ge/68Ga generator, used for radiolabeling of DOTA-peptide precursors DP1, DP2, and DP3."
    },
    {
      "id": "C11",
      "name": "Sodium acetate buffer (0.25 M, pH 6.5)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Aqueous sodium acetate buffer used to adjust the pH of the 68GaCl3 solution to pH 4–4.5 prior to radiolabeling of DOTA-peptide precursors."
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
        "other": "KD = 74.9 nM (saturation binding, MC38 cells); blood elimination T1/2 = 7.62 min; RCY = 89.55 ± 0.12% RCY; molar activity = 14.37 ± 0.97 GBq/μmol; RCP >95% by radio-HPLC"
      },
      "description": "68Ga-labeled DOTA-linear peptide radiotracer targeting ROR1, evaluated by PET imaging and biodistribution in multiple tumor-bearing mouse models."
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
        "other": "KD = 154.9 nM (saturation binding, MC38 cells); RCY = 97.67 ± 1.05% RCY; molar activity = 20.05 ± 1.35 GBq/μmol; RCP >95% by radio-HPLC"
      },
      "description": "68Ga-labeled DOTA-cyclic peptide radiotracer targeting ROR1, evaluated by PET imaging in MC38 tumor-bearing mice."
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
        "other": "KD = 213.4 nM (saturation binding, MC38 cells); RCY = 98.01 ± 0.97% RCY; molar activity = 14.09 ± 2.12 GBq/μmol; RCP >95% by radio-HPLC"
      },
      "description": "68Ga-labeled DOTA-cyclic peptide radiotracer (highest lipophilicity among the five probes) targeting ROR1, showing the lowest tumor uptake in PET imaging."
    },
    {
      "id": "C15",
      "name": "Fluoride-18 ([18F]fluoride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Cyclone 18/9 cyclotron, Center for Molecular Imaging and Translational Medicine, Xiamen University (18O(p,n)18F reaction)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Fluorine-18 radionuclide produced by cyclotron, used as the radiolabeling source for AlF-based 18F labeling of NOTA-peptide precursors NP1 and NP2."
    },
    {
      "id": "C16",
      "name": "QMA cartridge (preconditioned)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Quaternary methyl ammonium (QMA) anion-exchange cartridge preconditioned with saline and water, used to trap [18F]fluoride from the cyclotron target water prior to AlF radiolabeling."
    },
    {
      "id": "C17",
      "name": "Aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, 0.1 M sodium acetate, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Aluminum chloride solution used as the aluminum source to form the Al18F complex with trapped [18F]fluoride for subsequent chelation with NOTA-peptide precursors."
    },
    {
      "id": "C18",
      "name": "Sodium acetate buffer (0.1 M, pH 4.0) — for AlF labeling",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate buffer at pH 4.0 used as the reaction medium component in the AlF radiolabeling step for [18F]AlF-NP1 and [18F]AlF-NP2."
    },
    {
      "id": "C19",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.10 ± 0.04",
        "other": "KD = 141.7 nM (saturation binding, MC38 cells); blood elimination T1/2 = 19.32 min; RCY = 62.58 ± 0.32% RCY; molar activity = 13.13 ± 1.71 GBq/μmol; RCP >95% by radio-HPLC; ~4% intact probe detectable in urine at 0.5 h p.i., essentially none at 1 h p.i."
      },
      "description": "18F-labeled Al18F-NOTA-linear peptide radiotracer targeting ROR1, demonstrating the best overall PET imaging performance among the five probes across multiple tumor models."
    },
    {
      "id": "C20",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.54 ± 0.04",
        "other": "KD = 212.1 nM (saturation binding, MC38 cells); RCY = 62.76 ± 0.22% RCY; molar activity = 13.42 ± 1.25 GBq/μmol; RCP >95% by radio-HPLC"
      },
      "description": "18F-labeled Al18F-NOTA-cyclic peptide radiotracer targeting ROR1, showing the lowest cell uptake among the five probes and significant kidney accumulation."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of DP1 (DOTA-PR7 conjugate)",
      "target_compound_id": "C05",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling (chelator conjugation)",
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
            "other": "Agitated in an oscillator"
          },
          "product": {
            "compound_id": "C05",
            "name": "DP1 (crude reaction mixture)",
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
          "notes": "Reaction performed in a 2 mL centrifugation tube."
        },
        {
          "step_number": 2,
          "reaction_type": "Semipreparative HPLC purification and lyophilization",
          "reactants": [
            {
              "compound_id": "C05",
              "name": "DP1 (crude reaction mixture)",
              "amount": null
            }
          ],
          "reagents": [],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "UV detection at 254 nm; followed by lyophilization"
          },
          "product": {
            "compound_id": "C05",
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
            "hplc_retention_time_min": 11.23
          },
          "purification": "Semipreparative HPLC with UV detection at 254 nm; mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min; flow rate 1 mL/min. Product obtained after lyophilization.",
          "notes": "HPLC method used for both purification and purity analysis. Calculated mass is likely an average mass given the high molecular weight of the peptide."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of NP1 (NOTA-PR7 conjugate)",
      "target_compound_id": "C06",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling (chelator conjugation)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 μmol)"
            }
          ],
          "reagents": [
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
            "other": "Agitated in an oscillator"
          },
          "product": {
            "compound_id": "C06",
            "name": "NP1 (crude reaction mixture)",
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
          "notes": "Reaction performed in a 2 mL centrifugation tube. Run concurrently with DP1 synthesis using NOTA-NHS in place of DOTA-NHS."
        },
        {
          "step_number": 2,
          "reaction_type": "Semipreparative HPLC purification and lyophilization",
          "reactants": [
            {
              "compound_id": "C06",
              "name": "NP1 (crude reaction mixture)",
              "amount": null
            }
          ],
          "reagents": [],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "UV detection at 254 nm; followed by lyophilization"
          },
          "product": {
            "compound_id": "C06",
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
            "hplc_retention_time_min": 12.78
          },
          "purification": "Semipreparative HPLC with UV detection at 254 nm; mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min; flow rate 1 mL/min. Product obtained after lyophilization.",
          "notes": "Calculated mass is likely an average mass given the high molecular weight of the peptide."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP1",
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
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "Sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL (0.25 M, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
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
          "reaction_type": "68Ga radiolabeling (chelation)",
          "reactants": [
            {
              "compound_id": null,
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL total"
            },
            {
              "compound_id": "C05",
              "name": "DP1",
              "amount": "50 μg (16–20 nmol) in 50 μL DMSO"
            }
          ],
          "reagents": [],
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
            "other": "Cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C12",
            "name": "[68Ga]Ga-DP1 (crude)",
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
          "notes": "Precursor transferred to a vial before addition of the pH-adjusted 68GaCl3 solution."
        },
        {
          "step_number": 3,
          "reaction_type": "SPE purification and formulation",
          "reactants": [
            {
              "compound_id": "C12",
              "name": "[68Ga]Ga-DP1 (crude)",
              "amount": null
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "Ethanol",
              "volume": "1.5 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL ethanol. Radio-HPLC analysis: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min; flow rate 1 mL/min.",
          "notes": "RCY and molar activity are means ± SD, n ≥ 3. Same purification protocol applied to [68Ga]Ga-DP2 and [68Ga]Ga-DP3."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP2",
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
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "Sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL (0.25 M, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
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
          "reaction_type": "68Ga radiolabeling (chelation)",
          "reactants": [
            {
              "compound_id": null,
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL total"
            },
            {
              "compound_id": "C07",
              "name": "DP2",
              "amount": "50 μg (16–20 nmol) in 50 μL DMSO"
            }
          ],
          "reagents": [],
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
            "other": "Cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C13",
            "name": "[68Ga]Ga-DP2 (crude)",
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
          "step_number": 3,
          "reaction_type": "SPE purification and formulation",
          "reactants": [
            {
              "compound_id": "C13",
              "name": "[68Ga]Ga-DP2 (crude)",
              "amount": null
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "Ethanol",
              "volume": "1.5 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL ethanol. Radio-HPLC analysis: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min; flow rate 1 mL/min.",
          "notes": "RCY and molar activity are means ± SD, n ≥ 3."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP3",
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
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "Sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL (0.25 M, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
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
          "reaction_type": "68Ga radiolabeling (chelation)",
          "reactants": [
            {
              "compound_id": null,
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL total"
            },
            {
              "compound_id": "C08",
              "name": "DP3",
              "amount": "50 μg (16–20 nmol) in 50 μL DMSO"
            }
          ],
          "reagents": [],
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
            "other": "Cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C14",
            "name": "[68Ga]Ga-DP3 (crude)",
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
          "step_number": 3,
          "reaction_type": "SPE purification and formulation",
          "reactants": [
            {
              "compound_id": "C14",
              "name": "[68Ga]Ga-DP3 (crude)",
              "amount": null
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "Ethanol",
              "volume": "1.5 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL ethanol. Radio-HPLC analysis: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min; flow rate 1 mL/min.",
          "notes": "RCY and molar activity are means ± SD, n ≥ 3."
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Radiolabeling of [18F]AlF-NP1",
      "target_compound_id": "C19",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "QMA cartridge trapping of [18F]fluoride",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "Fluoride-18 ([18F]fluoride) in cyclotron target water",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [
            {
              "compound_id": "C16",
              "name": "QMA cartridge (preconditioned with 10 mL saline, then 10 mL pure water)",
              "amount": null,
              "role": "other"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "QMA cartridge preconditioned with 10 mL saline followed by 10 mL pure water"
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
          "reaction_type": "Elution of [18F]fluoride from QMA cartridge into AlCl3/precursor vial",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride trapped on QMA cartridge",
              "amount": null
            }
          ],
          "reagents": [
            {
              "name": "Saline (eluent)",
              "amount": "0.2 mL",
              "role": "other"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Eluted directly into a vial containing AlCl3 solution, acetonitrile, sodium acetate buffer, and precursor"
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride in AlCl3/precursor reaction mixture",
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
          "notes": "The vial receiving the eluate already contains 3 μL of 2 mM AlCl3 in sodium acetate buffer (0.1 M, pH 4.0), 200 μL acetonitrile, 100 μL sodium acetate buffer (0.1 M, pH 4.0), and the precursor in DMSO."
        },
        {
          "step_number": 3,
          "reaction_type": "Al18F chelation with NOTA-peptide (radiolabeling)",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride in AlCl3/precursor reaction mixture",
              "amount": null
            },
            {
              "compound_id": "C06",
              "name": "NP1",
              "amount": "50 μg (18–25 nmol) in 50 μL DMSO"
            }
          ],
          "reagents": [
            {
              "name": "AlCl3 in sodium acetate buffer (2 mM, 0.1 M sodium acetate, pH 4.0)",
              "amount": "3 μL (2 mM, 0.1 M sodium acetate, pH 4.0)",
              "role": "chelation_catalyst"
            },
            {
              "name": "Sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "100 μL (0.1 M, pH 4.0)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "Acetonitrile",
              "volume": "200 μL"
            },
            {
              "name": "DMSO",
              "volume": "50 μL"
            },
            {
              "name": "Saline",
              "volume": "0.2 mL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to room temperature after incubation"
          },
          "product": {
            "compound_id": "C19",
            "name": "[18F]AlF-NP1 (crude)",
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
          "notes": "The reaction pH is set by the sodium acetate buffer components; the saline eluate from the QMA (0.2 mL) carries the [18F]fluoride into the vial."
        },
        {
          "step_number": 4,
          "reaction_type": "SPE purification, solvent removal, and formulation",
          "reactants": [
            {
              "compound_id": "C19",
              "name": "[18F]AlF-NP1 (crude)",
              "amount": null
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "Ethanol",
              "volume": "1.5 mL"
            },
            {
              "name": "Saline",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Ethanol solvent removed after SPE elution; final product dissolved in saline"
          },
          "product": {
            "compound_id": "C19",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL ethanol. Ethanol removed under appropriate conditions; product redissolved in saline. Radio-HPLC analysis: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min; flow rate 1 mL/min.",
          "notes": "RCY and molar activity are means ± SD, n ≥ 3. Method for ethanol removal not specified in the main text."
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Radiolabeling of [18F]AlF-NP2",
      "target_compound_id": "C20",
      "target_compound_name": "[18F]AlF-NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "QMA cartridge trapping of [18F]fluoride",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "Fluoride-18 ([18F]fluoride) in cyclotron target water",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [
            {
              "compound_id": "C16",
              "name": "QMA cartridge (preconditioned with 10 mL saline, then 10 mL pure water)",
              "amount": null,
              "role": "other"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "QMA cartridge preconditioned with 10 mL saline followed by 10 mL pure water"
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
          "reaction_type": "Elution of [18F]fluoride from QMA cartridge into AlCl3/precursor vial",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride trapped on QMA cartridge",
              "amount": null
            }
          ],
          "reagents": [
            {
              "name": "Saline (eluent)",
              "amount": "0.2 mL",
              "role": "other"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Eluted directly into a vial containing AlCl3 solution, acetonitrile, sodium acetate buffer, and precursor"
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride in AlCl3/NP2 precursor reaction mixture",
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
          "step_number": 3,
          "reaction_type": "Al18F chelation with NOTA-cyclic peptide (radiolabeling)",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride in AlCl3/NP2 precursor reaction mixture",
              "amount": null
            },
            {
              "compound_id": "C09",
              "name": "NP2",
              "amount": "50 μg (18–25 nmol) in 50 μL DMSO"
            }
          ],
          "reagents": [
            {
              "name": "AlCl3 in sodium acetate buffer (2 mM, 0.1 M sodium acetate, pH 4.0)",
              "amount": "3 μL (2 mM, 0.1 M sodium acetate, pH 4.0)",
              "role": "chelation_catalyst"
            },
            {
              "name": "Sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "100 μL (0.1 M, pH 4.0)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "Acetonitrile",
              "volume": "200 μL"
            },
            {
              "name": "DMSO",
              "volume": "50 μL"
            },
            {
              "name": "Saline",
              "volume": "0.2 mL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to room temperature after incubation"
          },
          "product": {
            "compound_id": "C20",
            "name": "[18F]AlF-NP2 (crude)",
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
          "step_number": 4,
          "reaction_type": "SPE purification, solvent removal, and formulation",
          "reactants": [
            {
              "compound_id": "C20",
              "name": "[18F]AlF-NP2 (crude)",
              "amount": null
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "Ethanol",
              "volume": "1.5 mL"
            },
            {
              "name": "Saline",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Ethanol solvent removed after SPE elution; final product dissolved in saline"
          },
          "product": {
            "compound_id": "C20",
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
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL ethanol. Ethanol removed; product redissolved in saline. Radio-HPLC analysis: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min; flow rate 1 mL/min.",
          "notes": "RCY and molar activity are means ± SD, n ≥ 3. Method for ethanol removal not specified in the main text."
        }
      ]
    }
  ]
}
```

##### Claude_2
```
{
  "extraction": {
    "prompt_version": "v2.3",
    "extraction_date": "2026-03-20",
    "model_name": "claude-sonnet-4-6",
    "extractor_notes": "Full synthesis procedures for DP1 and NP1 are provided in the main text (Section 5.2.1) and radiolabeling procedures for all five radiotracers are in Section 5.4. Synthesis routes for PR7, DP2, DP3, and NP2 are referenced to Schemes S1–S5 in Supporting Information, which is unavailable; these compounds are custom-synthesized by Nanchang Tanzhen Biotechnology Co., Ltd. and treated as starting_material per the rules. MS data for large peptides (PR7, DP1, DP2, DP3, NP1, NP2) appear to be nominal/average masses rather than monoisotopic masses based on the magnitudes and the authors' use of 'calcd for' without specifying monoisotopic; the stated calculated masses match average molecular weights. This is noted per Rule 16. Radiochemical yields, molar activities, and log P values are reported in the main text for all five radiotracers; Table S1 is referenced for full radiochemical characteristics but the SI is unavailable. HPLC retention times for radiotracers are not reported in the main text. No HPLC retention times are given for radiolabeled products. The 68GaCl3 pH-adjustment step and the subsequent chelation step are treated as two separate steps per Rule 10. The QMA trapping, elution, and AlF chelation steps for 18F labeling are separated into distinct steps."
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
    "mechanism_discussed": "synthetic",
    "method_completeness": "partial",
    "has_synthesis": true,
    "extraction_notes": "Synthetic routes for precursors DP2, DP3, NP2, and PR7 are described only in Supporting Information Schemes S1–S5, which are unavailable in the provided input. Full in-house procedures are available in the main text only for DP1, NP1 (Section 5.2.1), and for all five radiolabeling reactions (Section 5.4). Calculated masses for all peptides appear to be average (not monoisotopic) masses based on comparison with molecular formulas; e.g., C96H133N25O31 for PR7 gives an average MW of ~2132 Da, consistent with the stated 2131.96. The paper reports DP2 calculated mass as 2743.2514 and DP3 as 3015.2514 with an unusual number of decimal places, which may reflect a different calculation convention. Radiochemical purity for all radioligands is stated as >95% by radio-HPLC (main text Section 5.4); the >90% figure cited elsewhere refers to in-process quality. The final purified products have >95% RCP."
  },

  "compounds": [
    {
      "id": "C01",
      "name": "PR7",
      "iupac_name": null,
      "molecular_formula": "C96H133N25O31",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "KD = 1.57 × 10−9 M (ROR1 binding); docking score −8.8 kcal/mol; HPLC retention time 10.642 min (0.1% TFA/water to 0.1% TFA/MeCN, 23–43% B over 20 min, 1 mL/min); purity >95% by HPLC"
      },
      "description": "Lead ROR1-targeting linear peptide used as the parent scaffold for chelator conjugation and as a blocking agent in cell uptake and in vivo competition assays."
    },
    {
      "id": "C02",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "N-hydroxysuccinimide ester of DOTA used as an activated chelator for conjugation to the primary amine of PR7 to yield DP1."
    },
    {
      "id": "C03",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "N-hydroxysuccinimide ester of NOTA used as an activated chelator for conjugation to the primary amine of PR7 to yield NP1."
    },
    {
      "id": "C04",
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
      "description": "Hindered organic base added to the conjugation reaction to facilitate NHS-ester amide coupling of DOTA-NHS or NOTA-NHS to PR7."
    },
    {
      "id": "C05",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time 11.230 min (0.1% TFA/water to 0.1% TFA/MeCN, 5–95% B over 20 min, 1 mL/min); purity >95% by HPLC; docking score −9.1 kcal/mol; KD = 74.9 nM (MC38 saturation binding)"
      },
      "description": "DOTA-conjugated linear PR7 peptide precursor used for 68Ga radiolabeling to produce [68Ga]Ga-DP1."
    },
    {
      "id": "C06",
      "name": "NP1",
      "iupac_name": null,
      "molecular_formula": "C108H152N28O36",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time 12.780 min (0.1% TFA/water to 0.1% TFA/MeCN, 5–95% B over 20 min, 1 mL/min); purity >95% by HPLC; docking score −8.3 kcal/mol; KD = 141.7 nM (MC38 saturation binding)"
      },
      "description": "NOTA-conjugated linear PR7 peptide precursor used for Al18F radiolabeling to produce [18F]AlF-NP1."
    },
    {
      "id": "C07",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time 10.328 min (0.1% TFA/water to 0.1% TFA/MeCN, 23–43% B over 20 min, 1 mL/min); purity >95% by HPLC; docking score −7.7 kcal/mol; KD = 154.9 nM (MC38 saturation binding)"
      },
      "description": "Custom-synthesised DOTA-cyclic peptide precursor used for 68Ga radiolabeling to produce [68Ga]Ga-DP2."
    },
    {
      "id": "C08",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time 10.404 min (0.1% TFA/water to 0.1% TFA/MeCN, 23–43% B over 20 min, 1 mL/min); purity >95% by HPLC; docking score −7.9 kcal/mol; KD = 213.4 nM (MC38 saturation binding)"
      },
      "description": "Custom-synthesised DOTA-cyclic peptide precursor (incorporating disulfide-bridged cysteine residues) used for 68Ga radiolabeling to produce [68Ga]Ga-DP3."
    },
    {
      "id": "C09",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time 10.620 min (0.1% TFA/water to 0.1% TFA/MeCN, 23–43% B over 20 min, 1 mL/min); purity >95% by HPLC; docking score −7.6 kcal/mol; KD = 212.1 nM (MC38 saturation binding)"
      },
      "description": "Custom-synthesised NOTA-cyclic peptide precursor used for Al18F radiolabeling to produce [18F]AlF-NP2."
    },
    {
      "id": "C10",
      "name": "68GaCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "ITM (68Ge–68Ga generator)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "supplied in 0.1 M HCl"
      },
      "description": "Gallium-68 chloride radionuclide source eluted from a 68Ge–68Ga generator and used for radiometal chelation with DOTA-peptide precursors."
    },
    {
      "id": "C11",
      "name": "Sodium acetate buffer (0.25 M, pH 6.5)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate buffer used to adjust the pH of the 68GaCl3 solution to pH 4–4.5 prior to radiolabeling with DOTA-peptide precursors."
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
        "other": "RCY 89.55 ± 0.12%; molar activity 14.37 ± 0.97 GBq/μmol (n ≥ 3); RCP >95% by radio-HPLC; stability >90% RCP after 2 h in saline and FBS; blood T1/2 = 7.62 min; KD = 74.9 nM (MC38); tumor uptake 1.41 ± 0.08% ID/g at 30 min p.i., 0.94 ± 0.07% ID/g at 60 min p.i."
      },
      "description": "68Ga-radiolabeled DOTA-linear PR7 peptide conjugate and the primary 68Ga PET radiotracer evaluated for ROR1-targeted PET imaging."
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
        "other": "RCY 97.67 ± 1.05%; molar activity 20.05 ± 1.35 GBq/μmol (n ≥ 3); RCP >95% by radio-HPLC; stability >90% RCP after 2 h in saline and FBS; KD = 154.9 nM (MC38)"
      },
      "description": "68Ga-radiolabeled DOTA-cyclic peptide DP2 conjugate evaluated as a ROR1-targeted PET radiotracer."
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
        "other": "RCY 98.01 ± 0.97%; molar activity 14.09 ± 2.12 GBq/μmol (n ≥ 3); RCP >95% by radio-HPLC; stability >90% RCP after 2 h in saline and FBS; KD = 213.4 nM (MC38)"
      },
      "description": "68Ga-radiolabeled DOTA-cyclic peptide DP3 conjugate evaluated as a ROR1-targeted PET radiotracer."
    },
    {
      "id": "C15",
      "name": "Fluoride-18 ([18F]fluoride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Center for Molecular Imaging and Translational Medicine, Xiamen University (Cyclone 18/9, IBA, Belgium; 18O(p,n)18F reaction)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Fluorine-18 radionuclide produced by proton bombardment of 18O-enriched water and used as the radiofluoride source for Al18F chelation radiolabeling."
    },
    {
      "id": "C16",
      "name": "Aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, 0.1 M sodium acetate, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Aluminum(III) chloride chelation catalyst dissolved in sodium acetate buffer, used to form the Al18F complex with NOTA-peptide precursors in the Al18F radiolabeling strategy."
    },
    {
      "id": "C17",
      "name": "Sodium acetate buffer (0.1 M, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate buffer used to adjust the reaction medium pH to 4.0 in the Al18F radiolabeling of NOTA-peptide precursors."
    },
    {
      "id": "C18",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.10 ± 0.04",
        "other": "RCY 62.58 ± 0.32%; molar activity 13.13 ± 1.71 GBq/μmol (n ≥ 3); RCP >95% by radio-HPLC; stability >90% RCP after 2 h in saline and FBS; approximately 4% intact at 0.5 h p.i. in urine of normal mice, nearly undetectable at 1 h p.i.; blood T1/2 = 19.32 min; KD = 141.7 nM (MC38); tumor uptake 2.89 ± 0.07% ID/g at 30 min p.i., 1.32 ± 0.14% ID/g at 60 min p.i."
      },
      "description": "Al18F-radiolabeled NOTA-linear PR7 peptide conjugate and the primary 18F PET radiotracer evaluated for ROR1-targeted PET imaging across multiple tumor models."
    },
    {
      "id": "C19",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.54 ± 0.04",
        "other": "RCY 62.76 ± 0.22%; molar activity 13.42 ± 1.25 GBq/μmol (n ≥ 3); RCP >95% by radio-HPLC; stability >90% RCP after 2 h in saline and FBS; KD = 212.1 nM (MC38)"
      },
      "description": "Al18F-radiolabeled NOTA-cyclic peptide NP2 conjugate evaluated as a ROR1-targeted PET radiotracer."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of DP1 (DOTA-PR7 conjugate)",
      "target_compound_id": "C05",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling",
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
            "other": "agitation in an oscillator; reaction performed in a 2 mL centrifugation tube"
          },
          "product": {
            "compound_id": "C05",
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
          "purification": "Semipreparative HPLC with UV detection at 254 nm; mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B), 5% B gradient to 95% B over 20 min, flow rate 1 mL/min; product obtained after lyophilization",
          "notes": "DP1 and NP1 were synthesised in the same reaction setup run in parallel with DOTA-NHS and NOTA-NHS respectively; both are described under Section 5.2.1. Calculated mass likely average mass, not monoisotopic."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of NP1 (NOTA-PR7 conjugate)",
      "target_compound_id": "C06",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 μmol)"
            }
          ],
          "reagents": [
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
            "other": "agitation in an oscillator; reaction performed in a 2 mL centrifugation tube"
          },
          "product": {
            "compound_id": "C06",
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
          "purification": "Semipreparative HPLC with UV detection at 254 nm; mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B), 5% B gradient to 95% B over 20 min, flow rate 1 mL/min; product obtained after lyophilization",
          "notes": "Synthesised in parallel with DP1 as described in Section 5.2.1. Calculated mass likely average mass, not monoisotopic."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP1",
      "target_compound_id": "C12",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "Sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL (0.25 M, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "pH-adjusted 68GaCl3–sodium acetate solution",
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
          "notes": "Final pH of the 68GaCl3–sodium acetate mixture is 4–4.5 after dilution. Solution then transferred to the vial containing the precursor."
        },
        {
          "step_number": 2,
          "reaction_type": "Radiometal chelation (68Ga complexation with DOTA-peptide)",
          "reactants": [
            {
              "compound_id": "C05",
              "name": "DP1",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "pH-adjusted 68GaCl3–sodium acetate solution",
              "amount": "1.5 mL (0.74–1.11 GBq, pH 4–4.5)",
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
            "other": "cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C12",
            "name": "[68Ga]Ga-DP1",
            "yield": "89.55 ± 0.12% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "14.37 ± 0.97 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol; ethanol solvent removed; final product resolved in saline",
          "notes": "Precursor dissolved in 50 μL DMSO in the reaction vial prior to addition of the radionuclide solution. RCY, RCP, and molar activity determined by radio-HPLC (0.1% TFA/water to 0.1% TFA/MeCN, 5–95% B over 20 min, 1 mL/min). n ≥ 3 replicates. Full radiochemical characteristics also summarized in Table S1 (SI unavailable)."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP2",
      "target_compound_id": "C13",
      "target_compound_name": "[68Ga]Ga-DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "Sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL (0.25 M, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "pH-adjusted 68GaCl3–sodium acetate solution",
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
          "reaction_type": "Radiometal chelation (68Ga complexation with DOTA-peptide)",
          "reactants": [
            {
              "compound_id": "C07",
              "name": "DP2",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "pH-adjusted 68GaCl3–sodium acetate solution",
              "amount": "1.5 mL (0.74–1.11 GBq, pH 4–4.5)",
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
            "other": "cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C13",
            "name": "[68Ga]Ga-DP2",
            "yield": "97.67 ± 1.05% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "20.05 ± 1.35 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol; ethanol solvent removed; final product resolved in saline",
          "notes": "Precursor dissolved in 50 μL DMSO. Procedure identical to [68Ga]Ga-DP1 except precursor. n ≥ 3 replicates."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP3",
      "target_compound_id": "C14",
      "target_compound_name": "[68Ga]Ga-DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "Sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL (0.25 M, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "pH-adjusted 68GaCl3–sodium acetate solution",
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
          "reaction_type": "Radiometal chelation (68Ga complexation with DOTA-peptide)",
          "reactants": [
            {
              "compound_id": "C08",
              "name": "DP3",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "pH-adjusted 68GaCl3–sodium acetate solution",
              "amount": "1.5 mL (0.74–1.11 GBq, pH 4–4.5)",
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
            "other": "cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C14",
            "name": "[68Ga]Ga-DP3",
            "yield": "98.01 ± 0.97% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "14.09 ± 2.12 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol; ethanol solvent removed; final product resolved in saline",
          "notes": "Precursor dissolved in 50 μL DMSO. Procedure identical to [68Ga]Ga-DP1 except precursor. n ≥ 3 replicates."
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Radiolabeling of [18F]AlF-NP1",
      "target_compound_id": "C18",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "[18F]fluoride trapping on QMA cartridge",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "Fluoride-18",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline (for preconditioning)",
              "volume": "10 mL"
            },
            {
              "name": "pure water (for preconditioning)",
              "volume": "10 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water prior to trapping"
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
          "notes": "QMA cartridge used as solid-phase trap for [18F]fluoride prior to elution and labeling."
        },
        {
          "step_number": 2,
          "reaction_type": "[18F]fluoride elution from QMA cartridge",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride trapped on QMA cartridge",
              "amount": null
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
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "eluted directly into the reaction vial containing AlCl3 solution, acetonitrile, sodium acetate buffer, and precursor"
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride in saline eluate",
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
          "notes": "Elution performed directly into the reaction vial to initiate Al18F complexation and labeling in a single vessel."
        },
        {
          "step_number": 3,
          "reaction_type": "Al18F chelation and NOTA-peptide radiolabeling",
          "reactants": [
            {
              "compound_id": "C06",
              "name": "NP1",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "[18F]fluoride in saline eluate",
              "amount": "0.2 mL saline eluate (approximately 0.74–1.11 GBq)",
              "role": "radionuclide_source"
            },
            {
              "name": "Aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, 0.1 M, pH 4.0)",
              "amount": "3 μL (2 mM AlCl3 in 0.1 M sodium acetate, pH 4.0)",
              "role": "chelation_catalyst"
            },
            {
              "name": "Sodium acetate buffer (0.1 M, pH 4.0)",
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
            "other": "cooled to room temperature after heating; precursor dissolved in 50 μL DMSO"
          },
          "product": {
            "compound_id": "C18",
            "name": "[18F]AlF-NP1",
            "yield": "62.58 ± 0.32% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "13.13 ± 1.71 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol; ethanol solvent removed; final product resolved in saline",
          "notes": "RCY, RCP, and molar activity determined by radio-HPLC (0.1% TFA/water to 0.1% TFA/MeCN, 5–95% B over 20 min, 1 mL/min). n ≥ 3 replicates. Full radiochemical characteristics in Table S1 (SI unavailable)."
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Radiolabeling of [18F]AlF-NP2",
      "target_compound_id": "C19",
      "target_compound_name": "[18F]AlF-NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "[18F]fluoride trapping on QMA cartridge",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "Fluoride-18",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline (for preconditioning)",
              "volume": "10 mL"
            },
            {
              "name": "pure water (for preconditioning)",
              "volume": "10 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water prior to trapping"
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
          "reaction_type": "[18F]fluoride elution from QMA cartridge",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride trapped on QMA cartridge",
              "amount": null
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
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "eluted into reaction vial containing AlCl3 solution, acetonitrile, sodium acetate buffer, and precursor"
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride in saline eluate",
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
          "step_number": 3,
          "reaction_type": "Al18F chelation and NOTA-peptide radiolabeling",
          "reactants": [
            {
              "compound_id": "C09",
              "name": "NP2",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "[18F]fluoride in saline eluate",
              "amount": "0.2 mL saline eluate (approximately 0.74–1.11 GBq)",
              "role": "radionuclide_source"
            },
            {
              "name": "Aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, 0.1 M, pH 4.0)",
              "amount": "3 μL (2 mM AlCl3 in 0.1 M sodium acetate, pH 4.0)",
              "role": "chelation_catalyst"
            },
            {
              "name": "Sodium acetate buffer (0.1 M, pH 4.0)",
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
            "other": "cooled to room temperature after heating; precursor dissolved in 50 μL DMSO"
          },
          "product": {
            "compound_id": "C19",
            "name": "[18F]AlF-NP2",
            "yield": "62.76 ± 0.22% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "13.42 ± 1.25 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol; ethanol solvent removed; final product resolved in saline",
          "notes": "Procedure identical to [18F]AlF-NP1 except precursor NP2 used in place of NP1. n ≥ 3 replicates."
        }
      ]
    }
  ]
}
```

##### Claude 3
```
{
  "extraction": {
    "prompt_version": "v2.3",
    "extraction_date": "2026-03-20",
    "model_name": "claude-sonnet-4-6",
    "extractor_notes": "Detailed synthesis routes (Schemes S1–S5) are in the Supporting Information and were not available for extraction. Only Section 5.2.1 (synthesis of DP1 and NP1 in-house) and Section 5.4 (radiolabeling of all five radiotracers) are described in the main text with full procedural detail; all other precursor syntheses are referenced to SI. The method_completeness is therefore 'partial'. Molecular formulas for DP2, DP3, NP2, and all radiotracers are either directly stated or derivable from the MS data lines in the paper; the calculated masses for DP2 (2743.2514) and DP3 (3015.2514) appear to be nominal/average masses rather than monoisotopic masses based on their significant figures and the size of the peptides — this is noted as per Rule 16. The calculated mass for PR7 (2131.96), DP2 (2743.2514), DP3 (3015.2514), and NP2 (2642.20) are reported as stated without correction. Log P values are only recorded for the radiolabeled products, as the paper explicitly states these values for the radiotracers only. KD values from saturation binding assays are recorded under physicochemical_properties of the respective radiolabeled products. Blood elimination half-lives (T1/2) are also recorded for [68Ga]Ga-DP1 and [18F]AlF-NP1 only, as these are the only ones reported. RCY values are taken from Section 2.2 (n ≥ 3). Molar activities are from Section 2.2."
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
    "mechanism_discussed": "synthetic",
    "method_completeness": "partial",
    "has_synthesis": true,
    "extraction_notes": "Detailed synthetic routes for PR7, DP2, DP3, and NP2 (Schemes S1–S5) are in the Supporting Information only; Section 5.2.2 confirms these were custom-synthesized externally by Nanchang Tanzhen Biotechnology Co., Ltd. and provides only HPLC retention times and ESI-MS data for characterization. The calculated masses for DP2 (2743.2514) and DP3 (3015.2514) appear to be average/nominal masses based on their four-decimal reporting and the large peptide size — the paper does not clarify this. Radiochemical characteristics (RCYs, molar activities, RCP) are summarized in Table S1; the main text quotes these values directly. All five radiotracers were purified by SepPak C18 cartridges. The paper states radiochemical purity >90% in the text (Section 2.2) but >95% by radio-HPLC in Section 5.4; both values are noted."
  },

  "compounds": [
    {
      "id": "C01",
      "name": "PR7",
      "iupac_name": null,
      "molecular_formula": "C96H133N25O31",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "KD = 1.57 × 10−9 M (reported from prior literature, reference 38); HPLC retention time: 10.642 min"
      },
      "description": "ROR1-targeting linear peptide lead compound used as the starting scaffold for the design of DP1, DP2, DP3, NP1, and NP2 precursors, and used as a blocking agent in cell uptake and PET imaging competition studies."
    },
    {
      "id": "C02",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "N-hydroxysuccinimide ester of DOTA chelator used as the coupling reagent for conjugation to PR7 to produce the precursor DP1."
    },
    {
      "id": "C03",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "N-hydroxysuccinimide ester of NOTA chelator used as the coupling reagent for conjugation to PR7 to produce the precursor NP1."
    },
    {
      "id": "C04",
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
      "description": "N,N-diisopropylethylamine used as a base in the conjugation reactions to produce DP1 and NP1."
    },
    {
      "id": "C05",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 11.230 min; purity >95% by HPLC; docking score with ROR1: −9.1 kcal/mol; KD: 74.9 nM (from saturation binding assay with [68Ga]Ga-DP1 in MC38 cells)"
      },
      "description": "DOTA-conjugated linear ROR1-targeting peptide precursor (P1+R3 scaffold) synthesized by coupling PR7 with DOTA-NHS; serves as the radiolabeling precursor for [68Ga]Ga-DP1."
    },
    {
      "id": "C06",
      "name": "NP1",
      "iupac_name": null,
      "molecular_formula": "C108H152N28O36",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 12.780 min; purity >95% by HPLC; docking score with ROR1: −8.3 kcal/mol; KD: 141.7 nM (from saturation binding assay with [18F]AlF-NP1 in MC38 cells)"
      },
      "description": "NOTA-conjugated linear ROR1-targeting peptide precursor (P1+R2 scaffold) synthesized by coupling PR7 with NOTA-NHS; serves as the radiolabeling precursor for [18F]AlF-NP1."
    },
    {
      "id": "C07",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.328 min; purity >95% by HPLC; docking score with ROR1: −7.7 kcal/mol; KD: 154.9 nM (from saturation binding assay with [68Ga]Ga-DP2)"
      },
      "description": "DOTA-conjugated cyclic ROR1-targeting peptide precursor (P2+L1+R3 scaffold) custom-synthesized externally; serves as the radiolabeling precursor for [68Ga]Ga-DP2."
    },
    {
      "id": "C08",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.404 min; purity >95% by HPLC; docking score with ROR1: −7.9 kcal/mol; KD: 213.4 nM (from saturation binding assay with [68Ga]Ga-DP3)"
      },
      "description": "DOTA-conjugated cyclic ROR1-targeting peptide precursor (P2+L2+R3 scaffold) custom-synthesized externally; serves as the radiolabeling precursor for [68Ga]Ga-DP3."
    },
    {
      "id": "C09",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.620 min; purity >95% by HPLC; KD: 212.1 nM (from saturation binding assay with [18F]AlF-NP2)"
      },
      "description": "NOTA-conjugated cyclic ROR1-targeting peptide precursor (P2+L1+R2 scaffold) custom-synthesized externally; serves as the radiolabeling precursor for [18F]AlF-NP2."
    },
    {
      "id": "C10",
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
      "description": "Gallium-68 trichloride in 0.1 M HCl obtained from the 68Ge–68Ga generator; used as the radionuclide source for 68Ga-labeling of DP1, DP2, and DP3 precursors."
    },
    {
      "id": "C11",
      "name": "Sodium acetate buffer (pH 6.5, 0.25 M)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Aqueous sodium acetate buffer at 0.25 M and pH 6.5 used to dilute and adjust the pH of the 68GaCl3 solution prior to the 68Ga-labeling reactions."
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
        "other": "KD: 74.9 nM (MC38 saturation binding); Bmax: 22158 CPM; blood elimination T1/2: 7.62 min; tumor uptake 1.41 ± 0.08% ID/g at 30 min p.i., 0.94 ± 0.07% ID/g at 60 min p.i. in MC38 model; tumor-to-muscle ratio 2.47 ± 0.07 at 60 min p.i.; RCP >90% (text) / >95% by radio-HPLC (Section 5.4)"
      },
      "description": "68Ga-labeled DOTA-conjugated linear ROR1-targeting radiotracer produced by complexation of 68GaCl3 with DP1; evaluated as a PET imaging agent across multiple tumor models."
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
        "other": "KD: 154.9 nM (MC38 saturation binding); Bmax: 31268 CPM; RCP >90% (text) / >95% by radio-HPLC (Section 5.4)"
      },
      "description": "68Ga-labeled DOTA-conjugated cyclic ROR1-targeting radiotracer produced by complexation of 68GaCl3 with DP2; evaluated as a PET imaging agent in MC38 tumor-bearing mice."
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
        "other": "KD: 213.4 nM (MC38 saturation binding); Bmax: 47017 CPM; RCP >90% (text) / >95% by radio-HPLC (Section 5.4)"
      },
      "description": "68Ga-labeled DOTA-conjugated cyclic ROR1-targeting radiotracer produced by complexation of 68GaCl3 with DP3; evaluated as a PET imaging agent in MC38 tumor-bearing mice."
    },
    {
      "id": "C15",
      "name": "Fluoride-18 ([18F]fluoride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "produced by Cyclone 18/9 (IBA, Belgium) at the Center for Molecular Imaging and Translational Medicine, Xiamen University via 18O(p,n)18F reaction",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Fluorine-18 fluoride used as the radionuclide source for Al18F-labeling of NP1 and NP2 precursors via the AlF chelation method."
    },
    {
      "id": "C16",
      "name": "Aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Aluminum chloride solution at 2 mM in sodium acetate buffer (0.1 M, pH 4.0) used as the aluminum source for the Al18F chelation labeling of NP1 and NP2."
    },
    {
      "id": "C17",
      "name": "Sodium acetate buffer (pH 4.0, 0.1 M)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Aqueous sodium acetate buffer at 0.1 M and pH 4.0 used in the Al18F-labeling reaction mixture for [18F]AlF-NP1 and [18F]AlF-NP2 preparation."
    },
    {
      "id": "C18",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.10 ± 0.04",
        "other": "KD: 141.7 nM (MC38 saturation binding); Bmax: 31406 CPM; blood elimination T1/2: 19.32 min; tumor uptake 2.89 ± 0.07% ID/g at 30 min p.i., 1.32 ± 0.14% ID/g at 60 min p.i. in MC38 model; tumor-to-muscle ratio 2.62 ± 0.06 at 60 min p.i.; metabolic stability: ~4% intact at 0.5 h p.i. in urine, almost none at 1 h p.i.; RCP >90% (text) / >95% by radio-HPLC (Section 5.4)"
      },
      "description": "18F-labeled Al18F-NOTA-conjugated linear ROR1-targeting radiotracer produced by Al18F chelation labeling of NP1; evaluated as the lead 18F-labeled PET imaging agent across multiple tumor models including autoradiography."
    },
    {
      "id": "C19",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.54 ± 0.04",
        "other": "KD: 212.1 nM (MC38 saturation binding); Bmax: 22986 CPM; RCP >90% (text) / >95% by radio-HPLC (Section 5.4)"
      },
      "description": "18F-labeled Al18F-NOTA-conjugated cyclic ROR1-targeting radiotracer produced by Al18F chelation labeling of NP2; evaluated as a PET imaging agent in MC38 tumor-bearing mice."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of DP1 (DOTA-PR7 conjugate)",
      "target_compound_id": "C05",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling (chelator conjugation)",
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
            "other": "Mixture agitated in an oscillator"
          },
          "product": {
            "compound_id": "C05",
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
                  "adduct": "[M + 2H]2+",
                  "mz": 1260.54
                },
                {
                  "adduct": "[M + 3H]3+",
                  "mz": 840.68
                }
              ]
            },
            "hplc_retention_time_min": 11.230
          },
          "purification": "Semipreparative HPLC with UV detection at 254 nm; mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min; flow rate 1 mL/min; product obtained after lyophilization",
          "notes": "Reaction performed in a 2 mL centrifugation tube. HPLC method for purity analysis: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min; flow rate 1 mL/min. DP1 and NP1 were synthesized in parallel in the same procedure."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of NP1 (NOTA-PR7 conjugate)",
      "target_compound_id": "C06",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling (chelator conjugation)",
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
            "other": "Mixture agitated in an oscillator"
          },
          "product": {
            "compound_id": "C06",
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
                  "adduct": "[M + 2H]2+",
                  "mz": 1210.22
                },
                {
                  "adduct": "[M + 3H]3+",
                  "mz": 807.00
                }
              ]
            },
            "hplc_retention_time_min": 12.780
          },
          "purification": "Semipreparative HPLC with UV detection at 254 nm; mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); gradient 5% B to 95% B over 20 min; flow rate 1 mL/min; product obtained after lyophilization",
          "notes": "Reaction performed in a 2 mL centrifugation tube. DP1 and NP1 were synthesized in parallel in the same procedure. HPLC method for purity analysis: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min; flow rate 1 mL/min."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP1",
      "target_compound_id": "C12",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "Sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL (0.25 M, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
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
          "notes": "The pH-adjusted 68GaCl3 solution was then transferred to the vial containing the precursor for the chelation step."
        },
        {
          "step_number": 2,
          "reaction_type": "Radiometal chelation (68Ga complexation)",
          "reactants": [
            {
              "compound_id": null,
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL total volume from Step 1"
            },
            {
              "compound_id": "C05",
              "name": "DP1 (precursor)",
              "amount": "50 μg (16–20 nmol, in 50 μL DMSO)"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 μL (for precursor dissolution)"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C12",
            "name": "[68Ga]Ga-DP1",
            "yield": "89.55 ± 0.12% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "14.37 ± 0.97 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL of ethanol. HPLC method for QC: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min; flow rate 1 mL/min.",
          "notes": "Reaction performed in a vial. n ≥ 3 replicates for RCY and molar activity determination. RCY and molar activity values are from Section 2.2; radiochemical purity >90% stated in main text, >95% stated in Section 5.4."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP2",
      "target_compound_id": "C13",
      "target_compound_name": "[68Ga]Ga-DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "Sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL (0.25 M, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
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
          "reaction_type": "Radiometal chelation (68Ga complexation)",
          "reactants": [
            {
              "compound_id": null,
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL total from Step 1"
            },
            {
              "compound_id": "C07",
              "name": "DP2 (precursor)",
              "amount": "50 μg (16–20 nmol, in 50 μL DMSO)"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 μL (for precursor dissolution)"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C13",
            "name": "[68Ga]Ga-DP2",
            "yield": "97.67 ± 1.05% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "20.05 ± 1.35 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL of ethanol. HPLC method for QC: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min; flow rate 1 mL/min.",
          "notes": "n ≥ 3 replicates for RCY and molar activity. Same general procedure as [68Ga]Ga-DP1."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP3",
      "target_compound_id": "C14",
      "target_compound_name": "[68Ga]Ga-DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C10",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "Sodium acetate (0.25 M in water, pH 6.5)",
              "amount": "0.5 mL (0.25 M, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
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
          "reaction_type": "Radiometal chelation (68Ga complexation)",
          "reactants": [
            {
              "compound_id": null,
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL total from Step 1"
            },
            {
              "compound_id": "C08",
              "name": "DP3 (precursor)",
              "amount": "50 μg (16–20 nmol, in 50 μL DMSO)"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 μL (for precursor dissolution)"
            }
          ],
          "conditions": {
            "temperature": "95 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C14",
            "name": "[68Ga]Ga-DP3",
            "yield": "98.01 ± 0.97% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "14.09 ± 2.12 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL of ethanol. HPLC method for QC: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min; flow rate 1 mL/min.",
          "notes": "n ≥ 3 replicates for RCY and molar activity. Same general procedure as [68Ga]Ga-DP1."
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Radiolabeling of [18F]AlF-NP1",
      "target_compound_id": "C18",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "18F trapping on QMA cartridge",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "Fluoride-18 ([18F]fluoride)",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline",
              "volume": "10 mL (for QMA preconditioning)"
            },
            {
              "name": "pure water",
              "volume": "10 mL (for QMA preconditioning)"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
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
          "notes": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water prior to trapping."
        },
        {
          "step_number": 2,
          "reaction_type": "Elution of trapped [18F]fluoride",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride trapped on QMA cartridge",
              "amount": null
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
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride in saline eluate",
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
          "notes": "Eluate collected directly into the reaction vial containing AlCl3 and other reagents for the labeling step."
        },
        {
          "step_number": 3,
          "reaction_type": "Al18F chelation radiolabeling",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride in saline eluate",
              "amount": "0.2 mL saline eluate"
            },
            {
              "compound_id": "C06",
              "name": "NP1 (precursor)",
              "amount": "50 μg (18–25 nmol, in 50 μL DMSO)"
            }
          ],
          "reagents": [
            {
              "name": "Aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, 0.1 M, pH 4.0)",
              "amount": "3 μL (2 mM, pH 4.0)",
              "role": "chelation_catalyst"
            },
            {
              "name": "Sodium acetate buffer (0.1 M, pH 4.0)",
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
              "volume": "50 μL (for precursor dissolution)"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to room temperature after heating; ethanol solvent removed after purification; final product redissolved in saline"
          },
          "product": {
            "compound_id": "C18",
            "name": "[18F]AlF-NP1",
            "yield": "62.58 ± 0.32% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "13.13 ± 1.71 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL of ethanol; ethanol removed; final product resolved in saline. HPLC method for QC: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min; flow rate 1 mL/min.",
          "notes": "n ≥ 3 replicates for RCY and molar activity. The reaction vial receives the saline eluate from Step 2 plus all other reagents listed."
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Radiolabeling of [18F]AlF-NP2",
      "target_compound_id": "C19",
      "target_compound_name": "[18F]AlF-NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "18F trapping on QMA cartridge",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "Fluoride-18 ([18F]fluoride)",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline",
              "volume": "10 mL (for QMA preconditioning)"
            },
            {
              "name": "pure water",
              "volume": "10 mL (for QMA preconditioning)"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
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
          "notes": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water."
        },
        {
          "step_number": 2,
          "reaction_type": "Elution of trapped [18F]fluoride",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride trapped on QMA cartridge",
              "amount": null
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
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride in saline eluate",
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
          "step_number": 3,
          "reaction_type": "Al18F chelation radiolabeling",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride in saline eluate",
              "amount": "0.2 mL saline eluate"
            },
            {
              "compound_id": "C09",
              "name": "NP2 (precursor)",
              "amount": "50 μg (18–25 nmol, in 50 μL DMSO)"
            }
          ],
          "reagents": [
            {
              "name": "Aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, 0.1 M, pH 4.0)",
              "amount": "3 μL (2 mM, pH 4.0)",
              "role": "chelation_catalyst"
            },
            {
              "name": "Sodium acetate buffer (0.1 M, pH 4.0)",
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
              "volume": "50 μL (for precursor dissolution)"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to room temperature after heating; ethanol solvent removed after purification; final product redissolved in saline"
          },
          "product": {
            "compound_id": "C19",
            "name": "[18F]AlF-NP2",
            "yield": "62.76 ± 0.22% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "13.42 ± 1.25 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL of ethanol; ethanol removed; final product resolved in saline. HPLC method for QC: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min; flow rate 1 mL/min.",
          "notes": "n ≥ 3 replicates for RCY and molar activity. Same general procedure as [18F]AlF-NP1."
        }
      ]
    }
  ]
}
```

##### Evaluation 
**Issues resolved vs v2.1/v2.2**

Every known problem is fixed. C1 (DP1/NP1 as `intermediate`) now passes universally, ending the 67% pattern from both prior versions. C2, C5, C6, and C7 — which were the biggest regressions or persistent failures — all reach 100%. C3 and C4 regressions introduced by v2.2 are corrected.

---

**Inconsistencies across the three v2.3 runs**

These are not hallucinations against the paper, but genuine disagreements between runs that show unresolved ambiguity in the prompt:

**Compound ID numbering for [18F]AlF-NP1.** Claude 1 assigns it `C19`, Claude 2 assigns it `C18`, Claude 3 assigns it `C18`. Claude 1's numbering is off because it created two separate compound entries for the two sodium acetate buffers (C17 = 0.1M pH 4.0 buffer, C18 = a second buffer entry), pushing [18F]AlF-NP1 to C19 and [18F]AlF-NP2 to C20. The other two runs merged buffer handling differently. This is a schema-level ambiguity about whether AlCl₃ solution and acetate buffer constitute one compound or two — the prompt rule on "dual buffer entries" (C6) is interpreted inconsistently here.

**Pathway target_compound_id for [18F]AlF-NP1 (P6).** Claude 1 and Claude 3 assign the target as `C19` and `C18` respectively (correct within their own schemes), but Claude 2 assigns `C18` which in its own numbering is the compound `[18F]AlF-NP1` — consistent. However the pathway P6 in Claude 2 lists target `C18` but the compound list shows `[18F]AlF-NP1` as `C18`, while [18F]AlF-NP2 is `C19`. So Claude 2's internal cross-references are self-consistent but differ from Claudes 1 and 3.

**Physicochemical properties placement for KD values.** All three runs record KD for radiolabeled products, but Claude 1 additionally reports `Bmax` values in the precursor compounds (e.g., `Bmax = 22158` for DP1), while Claude 2 does not include Bmax for precursors at all, and Claude 3 includes Bmax only in the radiolabeled product entries. The paper reports KD and Bmax from saturation binding assays conducted with the radiolabeled probes on cells — technically these values characterize the _radiotracer-receptor interaction_, not the precursor. Claude 3's approach is most correct; Claude 1's attribution of Bmax to the unlabeled precursor is a semantic misattribution.

**HPLC gradient for externally synthesized precursors.** Claude 2 correctly records two distinct HPLC gradients: 5–95% B for DP1/NP1 (main text section 5.2.1) and 23–43% B for PR7/DP2/DP3/NP2 (section 5.2.2). Claude 1 and Claude 3 also capture this, but Claude 1's precursor HPLC detail in `physicochemical_properties` is less explicit about which gradient applies to which compound.

---

**Genuine hallucinations / errors against the paper**

One clear instance: Claude 1's extractor_notes state the QMA cartridge trapping step uses "approximately 0.74–1.11 GBq" — this is copied from the 68Ga section of the paper; the [18F] source activity is not explicitly stated as the same range in Section 5.4. The paper says "approximately 0.74–1.11 GBq" for the 68Ga procedure but for [18F]AlF labeling it simply says "fluoride-18 (approximately 0.74–1.11 GBq)" — so all three runs actually reproduce this correctly. No outright hallucination here.

A softer error: Claude 3's `extractor_notes` mention "P1+R3 scaffold" for DP1 and "P1+R2 scaffold" for NP1. These scaffold labels come from Figure 2 in the paper (PR7: P₁+R₁; NP1: P₁+R₂; DP1: P₁+R₃), so Claude 3 is correctly reading the figure. However Claude 1 and Claude 2 do not include this detail, showing that Claude 3 drew on information the others omitted — this is enrichment, not hallucination, but it shows variable completeness.

---

**Summary**

v2.3 fully resolves all seven tracked failure modes and eliminates both regressions introduced by v2.2. The remaining problems are subtler: compound ID numbering is non-deterministic (prompt doesn't enforce a canonical ordering rule), Bmax attribution is ambiguous (should it go with the radiotracer or the precursor?), and completeness of figure-derived data varies across runs. None of these are hallucinations against the paper — they are genuine ambiguities that a v2.4 prompt would need to resolve with explicit rules.

#### v2.4 Prompt
```
SYSTEM ROLE
You are an expert chemist and scientific information extraction specialist with deep knowledge of organic, medicinal, and radiochemical synthesis. Your task is to extract chemical synthesis information from the academic paper provided below with maximum precision.

---

CRITICAL EXTRACTION RULES — read before answering

1. ARTICLE-ONLY
Extract exclusively from the version of the paper provided to you (main text, schemes, figures, tables, captions, experimental section). If the paper references Supporting Information for details not present in your input, record null for those fields and note the SI reference in the step's "notes" field. Do NOT supplement with prior chemical knowledge. Data visible in figures, tables, or captions (e.g. KD, Bmax from a binding curve figure, docking scores from a figure panel) must be extracted exactly as if they appeared in the main text — figure-derived data is not optional.

2. NOT REPORTED
If a field's value is absent from the article, use null — never invent plausible values.

3. NEGATIVE CASE
If the paper contains NO synthesis, still return valid JSON with has_synthesis: false and all synthesis arrays empty.

4. YIELD FORMAT
Use "N mg (N%)" when both mass and percentage are stated; "N%" when only a percentage is given. For radiochemical yields, append the RCY suffix: "89.55 ± 0.12% RCY". ONE compound per yield string — never concatenate multiple compounds into a single yield field.

5. AMOUNTS FORMAT
Express amounts as "N unit (N unit)" for mass + moles (e.g. "6.4 mg (3 μmol)"). Use an en dash for ranges: "0.74–1.11 GBq". Never append solvent or concentration context into the amount string — those go in the solvents array or reagents list respectively.

6. COMPOUND ENTRIES — what to include
Include ALL compounds: final products, intermediates, catalysts, radiolabeled derivatives, and any named reagent that plays a defined mechanistic role. Specific inclusion rules:

- Radionuclide sources (e.g. 68GaCl3, [18F]fluoride, [64Cu]Cl2) always get their own compound entry.
- Inorganic reagents with a defined mechanistic role (e.g. AlCl3 in AlF radiolabeling, SnCl2 as a reductant) always get their own compound entry.
- Organic bases or activating agents named with an amount in a synthesis step (e.g. DIPEA, HATU, PyBOP) get their own compound entry.
- Buffer solutions: create one compound entry per distinct pH/concentration combination if each plays a mechanistically distinct role. Do not merge two buffers at different pH values into one entry. Two sodium acetate buffers at different pH values (e.g. pH 6.5 and pH 4.0) are two separate compound entries even if they appear in the same paper.
- Pure solvents used only for dissolution or elution (e.g. DMSO, MeCN, EtOH, DCM) do NOT need compound entries — record them only in the solvents array of each step.
- Solid-phase cartridges and other consumables (e.g. QMA cartridge, SepPak C18) used purely as hardware/purification media do NOT need compound entries — record them only in the purification or notes field of the relevant step.

7. COMPOUND ID ORDERING — deterministic assignment
Assign IDs (C01, C02, C03, ...) strictly by order of first appearance in the paper, reading top to bottom, left to right, section by section in document order. Apply this canonical order:

  a. Compounds first mentioned in the title or abstract → assigned first.
  b. Compounds first mentioned in the Introduction → next.
  c. Compounds first mentioned in the Results/Chemistry section → next, in the order they appear.
  d. Compounds first mentioned in the Experimental section → next, in the order they appear.
  e. Within a single sentence listing multiple compounds, assign IDs left to right.

Rules:
- Do not skip IDs. If C03 is assigned, the next new compound must be C04.
- Do not reuse IDs.
- Do not merge two substances into one entry.
- Reagents, buffers, and radionuclide sources that are introduced for the first time in a reaction step are assigned IDs at that point in document order — after all product/precursor compounds already described earlier in the paper.
- When two buffers at different pH values first appear in the same sentence or paragraph, assign the lower ID to the buffer mentioned first (left to right in the sentence).

8. ROLE ASSIGNMENT — use these definitions exactly

Assign one role per compound. When in doubt, apply this decision tree in order:

- Is it a radiolabeled product (contains a radioisotope, produced in a radiolabeling step)? → radiolabeled_product. This takes priority over final_product even if the compound is biologically evaluated.
- Is it sourced externally (commercial supplier, custom order, vendor synthesis) and used directly as a substrate or precursor with no in-house chemical transformation? → starting_material
- Is it sourced externally and used as a consumable reagent (activating agent, chelator, base, buffer, radionuclide source)? → reagent
- Is it synthesised in-house and its sole purpose is to serve as input to a subsequent transformation (including radiolabeling)? → intermediate
- Is it synthesised in-house or externally and presented as a standalone biologically or pharmacologically evaluated deliverable, and does NOT contain a radioisotope? → final_product
- Is it used as a positive or negative control, reference standard, or blocking agent? → reference_compound
- Is it a metal, ligand, or co-ligand in a coordination or organometallic context? → catalyst or coligand as appropriate

Key distinctions:
- A compound is intermediate ONLY if it was made in-house in this study. An externally synthesised compound used as a radiolabeling precursor is starting_material, not intermediate, even if it is structurally novel.
- A compound is final_product only if the paper evaluates it as a standalone deliverable AND it does not contain a radioisotope. A chelator-peptide conjugate whose sole purpose is radiolabeling is intermediate (if made in-house) or starting_material (if sourced externally), not final_product, even if characterised by HPLC and MS.
- radiolabeled_product always overrides final_product. If a compound contains a radioisotope and was produced in a radiolabeling step, it is radiolabeled_product regardless of how extensively it is evaluated.

9. is_newly_synthesized
Set to true only for compounds prepared in-house during this study. Set to false for all commercially purchased, custom-ordered, or externally synthesised compounds, regardless of whether the structure is novel.

10. method_completeness
Choose exactly one value:
- "full" — complete procedure is in the main text for all compounds and steps
- "partial" — at least one in-house procedure appears in the main text; others are in SI or unavailable
- "referenced_to_SI" — main text gives no procedural detail at all; all routes are in SI only
- "none" — no synthesis is reported

If the main text contains an explicit in-house synthesis procedure for even one compound, use "partial", not "referenced_to_SI".

11. STEP GRANULARITY
Each physically distinct operation that requires its own materials list is a separate numbered step, even if the paper narrates them in one paragraph. Indicators: different equipment, different reagents, different conditions, different vessel. Examples:
- Solid-phase resin loading and coupling are separate steps.
- QMA trapping and Al18F complexation are separate steps.
- pH adjustment of a radionuclide solution and the subsequent chelation reaction are separate steps.
- Elution of a trapped species from a cartridge and the subsequent reaction are separate steps.

12. INTERMEDIATE PRODUCTS IN MULTI-STEP SEQUENCES
The product block of every step must describe what is produced by that step — even if it is a transient intermediate (e.g. a pH-adjusted radionuclide solution, a resin-bound peptide after a single coupling). For transient intermediates that have no independent compound entry, use "compound_id": null and give a descriptive name. Never recycle the compound_id of an input to describe the output of the same step. Example: if C09 is the 68GaCl3 starting reagent, the pH-adjusted solution produced in Step 1 must use "compound_id": null, not "compound_id": "C09".

13. REAGENT vs CONDITIONS — where concentration and pH go
- The pH of the reaction mixture goes in conditions.ph.
- The concentration and pH of a reagent solution (e.g. a buffer added to the reaction) go in the reagent's amount field: "0.5 mL (0.25 M, pH 6.5)".
- Never duplicate: if a value is in the reagent amount field, do not also put it in conditions.

14. PURITY FORMAT
Always include the analytical method: ">95% by HPLC" for non-radioactive compounds; ">95% RCP by radio-HPLC" for radiolabeled products.

15. TEMPERATURE FORMAT
Use SI convention with a space: "95 °C", "-20 °C", "room temperature". Never "95°C".

16. HPLC RETENTION TIME
Record as a number in minutes in product.hplc_retention_time_min. If a retention time is reported only in a characterisation section and not in a synthesis yield statement, still record it in the synthesis step product block for that compound.

17. MS DATA — monoisotopic vs nominal mass
Record the calculated mass exactly as stated in the paper. For large peptides, authors sometimes report nominal or average masses rather than monoisotopic masses. When this is evident (e.g. the stated mass matches the average molecular weight rather than the monoisotopic mass), note it in paper.extraction_notes. Do not correct or recalculate.

18. ONE ENTRY PER COMPOUND
Each distinct substance gets exactly one compound entry and one ID. Assign IDs in the deterministic order defined in Rule 7. Do not skip IDs, do not reuse them, do not merge two substances into one entry.

19. NO CITATION ARTIFACTS
All string values must be plain prose. Strip citation tags, reference numbers, footnote markers, and retrieval-system metadata from all fields.

20. ONE PATHWAY PER TARGET COMPOUND
Each synthesis pathway (P1, P2, ...) targets exactly one compound. Never describe two distinct synthetic routes in one pathway entry using "or" / "alternatively" logic.

21. PHYSICOCHEMICAL PROPERTIES — source-of-truth and completeness rules

  a. SPECIES ATTRIBUTION: Record a physicochemical property only in the compound entry for the exact species in which it was measured or reported. Apply this strictly:
     - log P: measured on the radiolabeled product (in octanol/PBS with radioactivity counting) → record only in the radiolabeled_product entry. Set log_p: null for all unlabeled precursors unless the paper explicitly reports a separate log P measurement for that precursor.
     - KD (binding affinity): measured using the radiolabeled product in a saturation binding assay → record only in the radiolabeled_product entry. Do not copy KD to the unlabeled precursor.
     - Bmax (receptor density/binding capacity): measured alongside KD in the same saturation binding assay → record only in the radiolabeled_product entry, in the same "other" field as KD. Never assign Bmax to an unlabeled precursor compound.
     - Docking scores: computed for the unlabeled precursor or parent peptide structure → record in the precursor/parent compound entry. Do not copy docking scores to the radiolabeled product unless the paper states the docked structure includes the radiometal.
     - Blood elimination T½: measured in vivo using the radiolabeled product → record only in the radiolabeled_product entry.

  b. COMPLETENESS: Extract ALL physicochemical properties reported for a compound, including data that appears only in figures, figure captions, or summary tables. Do not omit values because they appear in a figure rather than a table or in-text paragraph. Specifically:
     - KD and Bmax values from saturation binding curve figures must be extracted.
     - Docking scores from molecular docking figure panels must be extracted.
     - Tumor uptake (% ID/g), T/NT ratios, and biodistribution data should be noted in the "other" field if reported quantitatively.

  c. FORMAT: Record KD, Bmax, docking scores, and other numeric properties in the "other" string field of physicochemical_properties, separated by semicolons. Example: "KD = 74.9 nM (saturation binding, MC38 cells); Bmax = 22158 CPM; blood T½ = 7.62 min; tumor uptake 1.41 ± 0.08% ID/g at 30 min p.i. (MC38 model)".

22. CONSISTENCY SELF-CHECK — before returning your JSON
After completing extraction, perform these cross-reference checks and fix any failures before outputting:

  a. Every compound_id referenced in any synthesis pathway step (reactants, reagents, product.compound_id) must have a matching entry in the compounds array.
  b. Every target_compound_id in a pathway must have a matching entry in the compounds array.
  c. No two compound entries may share the same id value.
  d. Compound IDs must form a contiguous sequence: if the highest ID is CXX, all IDs from C01 to CXX must be present with no gaps.
  e. A compound_id used as a reactant input in step N must not also appear as the product.compound_id of step N (no input = output within the same step).
  f. For every radiolabeled_product entry, log_p must be populated if the paper reports it; for every non-radiolabeled compound, log_p must be null unless the paper explicitly reports it for that compound.
  g. Docking scores reported for unlabeled precursors must appear in those precursor entries, not in radiolabeled_product entries.

---

OUTPUT SCHEMA

Return a single JSON object. Do not add any text before or after the JSON.

{
  "extraction": {
    "prompt_version": "v2.4",
    "extraction_date": "YYYY-MM-DD",
    "model_name": "string — name and version of the model used for this extraction",
    "extractor_notes": "string or null — notes about the extraction process, ambiguities encountered, SI references that were unavailable, and any caveats about mass type (monoisotopic vs nominal) for large peptides"
  },

  "paper": {
    "title": "string",
    "authors": ["string"],
    "doi": "string or null",
    "journal": "string or null",
    "year": "integer or null",
    "synthesis_scale": "lab | preclinical | gmp | none",
    "mechanism_discussed": "synthetic | biological_only | none",
    "method_completeness": "full | partial | referenced_to_SI | none",
    "has_synthesis": true,
    "extraction_notes": "string or null — paper-specific observations: unusual reporting conventions, missing SI, discrepancies in the source text, notes on average vs monoisotopic masses"
  },

  "compounds": [
    {
      "id": "C01",
      "name": "string",
      "iupac_name": "string or null — only if explicitly stated in the paper",
      "molecular_formula": "string or null — only if explicitly stated",
      "role": "starting_material | intermediate | reagent | catalyst | coligand | radiolabeled_product | final_product | reference_compound",
      "is_newly_synthesized": true,
      "source": "string or null — in-house, commercial, or vendor name if stated",
      "physicochemical_properties": {
        "log_p": "string or null — only if explicitly reported for THIS compound in the paper; null for all non-radiolabeled compounds unless the paper states it directly",
        "other": "string or null — all other reported properties: KD, Bmax, docking scores, T½, HPLC retention time, tumor uptake, T/NT ratios, purity; semicolon-separated"
      },
      "description": "one sentence of plain prose describing this compound's function in the study"
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "string",
      "target_compound_id": "C01",
      "target_compound_name": "string",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "string or null",
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
              "role": "coupling_reagent | base | acid | oxidant | reductant | catalyst | protecting_group_reagent | ph_adjuster | radionuclide_source | chelation_catalyst | other"
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
            "ph": "string or null — pH of the reaction mixture only; not the pH of a specific reagent solution",
            "other": "string or null — stirring mode, post-reaction cooling, special handling; vessel and equipment details go in notes"
          },
          "product": {
            "compound_id": "string or null — C-ID if the compound has an entry; null for transient intermediates with no compound entry",
            "name": "string",
            "yield": "string or null",
            "purity": "string or null",
            "molar_activity": "string or null — radiolabeled products only",
            "characterization": ["ESI-MS", "HPLC"],
            "ms_data": {
              "calculated_exact_mass": "number or null",
              "formula": "string or null",
              "observed_ions": [
                {
                  "adduct": "string",
                  "mz": "number or null"
                }
              ]
            },
            "hplc_retention_time_min": "number or null"
          },
          "purification": "string or null — method, catalog number if given, elution solvent and volume, post-purification formulation steps",
          "notes": "string or null — SI references, vessel and equipment details, n value for replicates, any procedural context not captured above"
        }
      ]
    }
  ]
}

```

##### Claude_1
```
{
  "extraction": {
    "prompt_version": "v2.4",
    "extraction_date": "2026-03-20",
    "model_name": "claude-sonnet-4-6",
    "extractor_notes": "Detailed synthetic routes for all five precursors (DP1, DP2, DP3, NP1, NP2) are in Schemes S1–S5 of the Supporting Information, which was not provided. Only the in-house synthesis of DP1 and NP1 (Section 5.2.1) and the radiolabeling procedures (Section 5.4) are described in the main text. PR7, DP2, DP3, and NP2 were custom-synthesized externally. Radiochemical characteristics (Table S1) are in SI; however, RCY and molar activity values for all five radiotracers are explicitly stated in the main text (Section 2.2). Bmax values are extracted from Figure 4G (table inset within the figure). Molecular masses for these large peptides are reported by the authors as calculated exact masses (ESI-MS calcd); for DP2 (2743.2514) and DP3 (3015.2514), the trailing '.2514' appears to be a copy/paste artifact in the paper where the two values share the same decimal portion, suggesting possible nominal or average mass reporting — noted but values recorded as stated. All docking scores are from Figure 3B. Blood T1/2 values are from Figure S29 (referenced in main text Section 2.6). The paper reports that radiochemical purities of all radioligands are >95% by radio-HPLC (Section 5.4), overriding the earlier >90% stability statement which refers to stability samples, not freshly prepared product. Compound ID assignment follows document order: abstract/title first mention order is [68Ga]Ga-DP1, [18F]AlF-NP1 (abstract); then in Section 2.2 the precursors DP1, DP2, DP3, NP1, NP2 and their radiotracers are introduced; PR7 appears first in introduction context but as a lead compound reference (ref 38); Section 5.1 introduces PR7, DP2, DP3, NP2, DOTA-NHS, NOTA-NHS as externally sourced; Section 5.2.1 introduces DIPEA; Section 5.4 introduces 68GaCl3, sodium acetate buffer pH 6.5, AlCl3, sodium acetate buffer pH 4.0. The five precursors are first collectively named in Section 2.2; individual structures shown in Figure 2. For ID ordering I assign: PR7 first (mentioned first by name in abstract as parent scaffold context, and first in the precursor list of Section 2.2 reading order), then DP1, DP2, DP3, NP1, NP2, then their radiotracers in the order listed in Section 2.2, then reagents in order of appearance in experimental."
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
    "mechanism_discussed": "synthetic",
    "method_completeness": "partial",
    "has_synthesis": true,
    "extraction_notes": "Complete synthetic routes for all five precursors are in Schemes S1–S5 (SI not provided). In-house synthesis is described only for DP1 and NP1 in the main text (Section 5.2.1). PR7, DP2, DP3, and NP2 were custom-synthesized externally. Radiolabeling procedures for all five radiotracers are fully described in Section 5.4. The calculated exact masses for DP2 (2743.2514) and DP3 (3015.2514) both end in '.2514', which may be a typographical artifact in the paper; values are recorded as printed. These large peptides likely have average masses reported rather than strict monoisotopic masses."
  },

  "compounds": [
    {
      "id": "C01",
      "name": "PR7",
      "iupac_name": null,
      "molecular_formula": "C96H133N25O31",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time 10.642 min (0.1% TFA/water to 0.1% TFA/MeCN, 23% B to 43% B over 20 min, 1 mL/min); purity >95% by HPLC; ESI-MS calcd 2131.96, found [M+2H]2+ = 1067.47; docking score (AutoDock 4.2.6, ROR1 PDB: 6BA5) = −8.8 kcal/mol; binding sites: D27, N29, S72, R70, N51, T56, S55, E82, R81, V16, T344; KD (referenced) = 1.57 × 10−9 M (from prior literature ref 38)"
      },
      "description": "Parent ROR1-targeting peptide lead compound used as the precursor scaffold for modification and as a blocking agent in cell uptake and in vivo competition assays."
    },
    {
      "id": "C02",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time 11.230 min (0.1% TFA/water to 0.1% TFA/MeCN, 5% B to 95% B over 20 min, 1 mL/min); purity >95% by HPLC; ESI-MS calcd 2518.14, found [M+2H]2+ = 1260.54, [M+3H]3+ = 840.68; yield 4.2 mg (55.6%); docking score (AutoDock 4.2.6, ROR1 PDB: 6BA5) = −9.1 kcal/mol; binding sites: K369, Q368, N29, S72, D30, S52, S55, W57, Q80, E82, T346, T344, P342, Y341, R81; forms 15 hydrogen bonds with ROR1"
      },
      "description": "DOTA-conjugated linear peptide precursor derived from PR7, synthesized in-house and used as the radiolabeling precursor for [68Ga]Ga-DP1."
    },
    {
      "id": "C03",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time 10.328 min (0.1% TFA/water to 0.1% TFA/MeCN, 23% B to 43% B over 20 min, 1 mL/min); purity >95% by HPLC; ESI-MS calcd 2743.2514, found [M+2H]2+ = 1373.07, [M+3H]3+ = 915.72; docking score (AutoDock 4.2.6, ROR1 PDB: 6BA5) = −7.7 kcal/mol; binding sites: E82, Q80, R81, W57, S55, R99, N95, E379, D31, Y99, Y100, L355, N338, N356; forms 14 hydrogen bonds with ROR1"
      },
      "description": "DOTA-conjugated cyclic peptide precursor derived from PR7, custom-synthesized externally and used as the radiolabeling precursor for [68Ga]Ga-DP2."
    },
    {
      "id": "C04",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time 10.404 min (0.1% TFA/water to 0.1% TFA/MeCN, 23% B to 43% B over 20 min, 1 mL/min); purity >95% by HPLC; ESI-MS calcd 3015.2514, found [M+2H]2+ = 1509.05, [M+3H]3+ = 1006.39; docking score (AutoDock 4.2.6, ROR1 PDB: 6BA5) = −7.9 kcal/mol; binding sites: N95, Y96, Y99, S55, N51, E379, P342, S339, N338; forms 9 hydrogen bonds with ROR1"
      },
      "description": "DOTA-conjugated cyclic peptide precursor derived from PR7, custom-synthesized externally and used as the radiolabeling precursor for [68Ga]Ga-DP3."
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
        "other": "HPLC retention time 12.780 min (0.1% TFA/water to 0.1% TFA/MeCN, 5% B to 95% B over 20 min, 1 mL/min); purity >95% by HPLC; ESI-MS calcd 2417.09, found [M+2H]2+ = 1210.22, [M+3H]3+ = 807.00; yield 3.9 mg (54%); docking score (AutoDock 4.2.6, ROR1 PDB: 6BA5) = −8.3 kcal/mol; binding sites: S115, D76, G17, R70, T71, T73, S52, S55, N51, E379, K382, T344, T346"
      },
      "description": "NOTA-conjugated linear peptide precursor derived from PR7, synthesized in-house and used as the radiolabeling precursor for [18F]AlF-NP1."
    },
    {
      "id": "C06",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time 10.620 min (0.1% TFA/water to 0.1% TFA/MeCN, 23% B to 43% B over 20 min, 1 mL/min); purity >95% by HPLC; ESI-MS calcd 2642.20, found [M+2H]2+ = 1322.56; docking score (AutoDock 4.2.6, ROR1 PDB: 6BA5) = −7.6 kcal/mol; binding sites: N95, D31, Y99, Y100, D378, E379, P342, T344, Q340, N338, L355, N356"
      },
      "description": "NOTA-conjugated cyclic peptide precursor derived from PR7, custom-synthesized externally and used as the radiolabeling precursor for [18F]AlF-NP2."
    },
    {
      "id": "C07",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.19 ± 0.05 (1-octanol/PBS pH 7.4, radioactivity counting, n = 3)",
        "other": "RCY 89.55 ± 0.12%; radiochemical purity >95% by radio-HPLC; molar activity 14.37 ± 0.97 GBq/μmol (n ≥ 3); stability >90% RCP after 2 h in saline and fetal bovine serum; KD = 74.9 nM (saturation binding assay, MC38 cells); Bmax = 22158 CPM (saturation binding, MC38 cells); MC38 cell uptake 7.26 ± 0.49% (30 min); blood T1/2 = 7.62 min; tumor uptake (MC38) 1.41 ± 0.08% ID/g at 30 min p.i., 0.94 ± 0.07% ID/g at 60 min p.i.; kidney uptake 27.90 ± 4.36% ID/g at 30 min p.i., 20.91 ± 1.43% ID/g at 60 min p.i.; tumor-to-muscle ratio 2.47 ± 0.07 at 60 min p.i."
      },
      "description": "68Ga-labeled DOTA-DP1 radiotracer used for PET imaging of ROR1 expression in multiple tumor-bearing mouse models."
    },
    {
      "id": "C08",
      "name": "[68Ga]Ga-DP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.53 ± 0.04 (1-octanol/PBS pH 7.4, radioactivity counting, n = 3)",
        "other": "RCY 97.67 ± 1.05%; radiochemical purity >95% by radio-HPLC; molar activity 20.05 ± 1.35 GBq/μmol (n ≥ 3); stability >90% RCP after 2 h in saline and fetal bovine serum; KD = 154.9 nM (saturation binding assay, MC38 cells); Bmax = 31268 CPM (saturation binding, MC38 cells); MC38 cell uptake 2.50 ± 0.36% (30 min)"
      },
      "description": "68Ga-labeled DOTA-DP2 radiotracer evaluated by PET imaging in MC38 tumor-bearing mice for ROR1 targeting."
    },
    {
      "id": "C09",
      "name": "[68Ga]Ga-DP3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−1.82 ± 0.03 (1-octanol/PBS pH 7.4, radioactivity counting, n = 3)",
        "other": "RCY 98.01 ± 0.97%; radiochemical purity >95% by radio-HPLC; molar activity 14.09 ± 2.12 GBq/μmol (n ≥ 3); stability >90% RCP after 2 h in saline and fetal bovine serum; KD = 213.4 nM (saturation binding assay, MC38 cells); Bmax = 47017 CPM (saturation binding, MC38 cells); MC38 cell uptake 1.07 ± 0.07% (30 min); MC38 tumor uptake 0.31 ± 0.05% ID/g at 30 min p.i."
      },
      "description": "68Ga-labeled DOTA-DP3 radiotracer evaluated by PET imaging in MC38 tumor-bearing mice; showed the lowest tumor uptake among the 68Ga-labeled series."
    },
    {
      "id": "C10",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.10 ± 0.04 (1-octanol/PBS pH 7.4, radioactivity counting, n = 3)",
        "other": "RCY 62.58 ± 0.32%; radiochemical purity >95% by radio-HPLC; molar activity 13.13 ± 1.71 GBq/μmol (n ≥ 3); stability >90% RCP after 2 h in saline and fetal bovine serum; metabolic stability: ~4% intact probe detectable in urine at 0.5 h p.i., almost none at 1 h p.i. (radio-HPLC); KD = 141.7 nM (saturation binding assay, MC38 cells); Bmax = 31406 CPM (saturation binding, MC38 cells); MC38 cell uptake 10.30 ± 1.40% (30 min); blood T1/2 = 19.32 min; tumor uptake (MC38) 2.89 ± 0.07% ID/g at 30 min p.i., 1.32 ± 0.14% ID/g at 60 min p.i.; kidney uptake 27.27 ± 2.99% ID/g at 30 min p.i., 17.74 ± 4.53% ID/g at 60 min p.i.; tumor-to-muscle ratio 2.62 ± 0.06 at 60 min p.i.; autoradiography confirmed specific uptake in B16F10 lung metastasis sections, blockable by PR7"
      },
      "description": "18F-labeled AlF-NOTA-NP1 radiotracer identified as a lead probe for ROR1 PET imaging, demonstrating the highest MC38 cell uptake and favorable tumor-to-background ratios in multiple tumor models."
    },
    {
      "id": "C11",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.54 ± 0.04 (1-octanol/PBS pH 7.4, radioactivity counting, n = 3)",
        "other": "RCY 62.76 ± 0.22%; radiochemical purity >95% by radio-HPLC; molar activity 13.42 ± 1.25 GBq/μmol (n ≥ 3); stability >90% RCP after 2 h in saline and fetal bovine serum; KD = 212.1 nM (saturation binding assay, MC38 cells); Bmax = 22986 CPM (saturation binding, MC38 cells); MC38 cell uptake 0.68 ± 0.04% (30 min)"
      },
      "description": "18F-labeled AlF-NOTA-NP2 radiotracer evaluated alongside [18F]AlF-NP1; showed significantly lower MC38 cell uptake and was not prioritized for further study."
    },
    {
      "id": "C12",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "NHS ester-activated DOTA chelator used for conjugation to the amine of PR7 to produce DP1."
    },
    {
      "id": "C13",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "NHS ester-activated NOTA chelator used for conjugation to the amine of PR7 to produce NP1."
    },
    {
      "id": "C14",
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
      "description": "Hindered organic base (N,N-diisopropylethylamine) used to facilitate NHS ester coupling of DOTA-NHS or NOTA-NHS to PR7."
    },
    {
      "id": "C15",
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
      "description": "Gallium-68 trichloride eluted from a 68Ge/68Ga generator, used as the radionuclide source for 68Ga-labeling of DP1, DP2, and DP3."
    },
    {
      "id": "C16",
      "name": "Sodium acetate buffer (0.25 M, pH 6.5)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "in-house preparation",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate aqueous buffer at pH 6.5 used to dilute the 68GaCl3 solution in 0.1 M HCl and adjust the pH to 4–4.5 prior to labeling."
    },
    {
      "id": "C17",
      "name": "Fluoride-18 ([18F]fluoride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Center for Molecular Imaging and Translational Medicine, Xiamen University (cyclotron-produced via 18O(p,n)18F, Cyclone 18/9, IBA)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Cyclotron-produced fluoride-18 used as the radionuclide source for AlF-radiolabeling of NP1 and NP2."
    },
    {
      "id": "C18",
      "name": "Aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, 0.1 M sodium acetate, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Aluminum chloride solution in sodium acetate buffer at pH 4.0, serving as the aluminum source and chelation catalyst for Al18F complexation with the NOTA chelator."
    },
    {
      "id": "C19",
      "name": "Sodium acetate buffer (0.1 M, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "in-house preparation",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate aqueous buffer at pH 4.0 added to the AlF-radiolabeling reaction mixture to maintain acidic conditions for Al18F-NOTA complexation."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of DP1 (DOTA-PR7 conjugate)",
      "target_compound_id": "C02",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 μmol)"
            },
            {
              "compound_id": "C12",
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
            "other": "Agitated in an oscillator; reaction carried out in a 2 mL centrifugation tube"
          },
          "product": {
            "compound_id": "C02",
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
          "purification": "Semipreparative HPLC with UV detection at 254 nm; lyophilization after collection",
          "notes": "DP1 and NP1 are prepared in the same reaction mixture by using DOTA-NHS and NOTA-NHS respectively in parallel reactions (Section 5.2.1). HPLC method: 0.1% TFA in water (A) and 0.1% TFA in MeCN (B); 5% B to 95% B over 20 min, flow rate 1 mL/min."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of NP1 (NOTA-PR7 conjugate)",
      "target_compound_id": "C05",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 μmol)"
            },
            {
              "compound_id": "C13",
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
            "other": "Agitated in an oscillator; reaction carried out in a 2 mL centrifugation tube"
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
          "purification": "Semipreparative HPLC with UV detection at 254 nm; lyophilization after collection",
          "notes": "NP1 is prepared under identical conditions to DP1 but using NOTA-NHS instead of DOTA-NHS (Section 5.2.1). HPLC method: 0.1% TFA in water (A) and 0.1% TFA in MeCN (B); 5% B to 95% B over 20 min, flow rate 1 mL/min."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "68Ga-radiolabeling of DP1 to give [68Ga]Ga-DP1",
      "target_compound_id": "C07",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "Sodium acetate buffer (0.25 M, pH 6.5)",
              "amount": "0.5 mL (0.25 M, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "pH-adjusted 68GaCl3–sodium acetate solution (pH 4–4.5)",
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
          "notes": "The 68GaCl3 solution in 0.1 M HCl is diluted with sodium acetate buffer to adjust pH to 4–4.5 before transfer to the precursor vial."
        },
        {
          "step_number": 2,
          "reaction_type": "Radiometal chelation (68Ga-DOTA complexation)",
          "reactants": [
            {
              "compound_id": "C02",
              "name": "DP1",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "pH-adjusted 68GaCl3–sodium acetate solution",
              "amount": "1.5 mL (transferred from Step 1)",
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
            "other": "Cooled to room temperature after reaction"
          },
          "product": {
            "compound_id": "C07",
            "name": "[68Ga]Ga-DP1",
            "yield": "89.55 ± 0.12% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "14.37 ± 0.97 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol. After ethanol removal, the final product was resolved in saline.",
          "notes": "Radiochemical yield, radiochemical purity, and molar activity determined by radio-HPLC (Dionex UltiMate 3000, Thermo Scientific; radio-scanner MSFC100220, Eckert & Ziegler). HPLC method: 0.1% TFA/water (A) and 0.1% TFA/MeCN (B); 5% B to 95% B over 20 min, 1 mL/min. n ≥ 3 replicates."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "68Ga-radiolabeling of DP2 to give [68Ga]Ga-DP2",
      "target_compound_id": "C08",
      "target_compound_name": "[68Ga]Ga-DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "Sodium acetate buffer (0.25 M, pH 6.5)",
              "amount": "0.5 mL (0.25 M, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "pH-adjusted 68GaCl3–sodium acetate solution (pH 4–4.5)",
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
          "notes": "Identical procedure to P3 Step 1."
        },
        {
          "step_number": 2,
          "reaction_type": "Radiometal chelation (68Ga-DOTA complexation)",
          "reactants": [
            {
              "compound_id": "C03",
              "name": "DP2",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "pH-adjusted 68GaCl3–sodium acetate solution",
              "amount": "1.5 mL (transferred from Step 1)",
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
            "other": "Cooled to room temperature after reaction"
          },
          "product": {
            "compound_id": "C08",
            "name": "[68Ga]Ga-DP2",
            "yield": "97.67 ± 1.05% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "20.05 ± 1.35 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol. After ethanol removal, the final product was resolved in saline.",
          "notes": "n ≥ 3 replicates."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "68Ga-radiolabeling of DP3 to give [68Ga]Ga-DP3",
      "target_compound_id": "C09",
      "target_compound_name": "[68Ga]Ga-DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            }
          ],
          "reagents": [
            {
              "name": "Sodium acetate buffer (0.25 M, pH 6.5)",
              "amount": "0.5 mL (0.25 M, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "pH-adjusted 68GaCl3–sodium acetate solution (pH 4–4.5)",
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
          "notes": "Identical procedure to P3 Step 1."
        },
        {
          "step_number": 2,
          "reaction_type": "Radiometal chelation (68Ga-DOTA complexation)",
          "reactants": [
            {
              "compound_id": "C04",
              "name": "DP3",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "pH-adjusted 68GaCl3–sodium acetate solution",
              "amount": "1.5 mL (transferred from Step 1)",
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
            "other": "Cooled to room temperature after reaction"
          },
          "product": {
            "compound_id": "C09",
            "name": "[68Ga]Ga-DP3",
            "yield": "98.01 ± 0.97% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "14.09 ± 2.12 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol. After ethanol removal, the final product was resolved in saline.",
          "notes": "n ≥ 3 replicates."
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "18F AlF-radiolabeling of NP1 to give [18F]AlF-NP1",
      "target_compound_id": "C10",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Ion trapping of [18F]fluoride on QMA cartridge and elution",
          "reactants": [
            {
              "compound_id": "C17",
              "name": "[18F]fluoride",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline (for elution)",
              "volume": "0.2 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride eluate in 0.2 mL saline",
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
          "notes": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water before trapping. [18F]fluoride is trapped and then eluted with 0.2 mL saline into the labeling vial."
        },
        {
          "step_number": 2,
          "reaction_type": "Al18F-NOTA chelation radiolabeling",
          "reactants": [
            {
              "compound_id": "C05",
              "name": "NP1",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "[18F]fluoride eluate in saline",
              "amount": "0.2 mL",
              "role": "radionuclide_source"
            },
            {
              "name": "Aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, 0.1 M, pH 4.0)",
              "amount": "3 μL (2 mM AlCl3, 0.1 M sodium acetate, pH 4.0)",
              "role": "chelation_catalyst"
            },
            {
              "name": "Sodium acetate buffer (0.1 M, pH 4.0)",
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
            "other": "Cooled to room temperature after reaction"
          },
          "product": {
            "compound_id": "C10",
            "name": "[18F]AlF-NP1",
            "yield": "62.58 ± 0.32% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "13.13 ± 1.71 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol. Ethanol solvent removed; final product resolved in saline.",
          "notes": "n ≥ 3 replicates. HPLC method: 0.1% TFA/water (A) and 0.1% TFA/MeCN (B); 5% B to 95% B over 20 min, 1 mL/min."
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "18F AlF-radiolabeling of NP2 to give [18F]AlF-NP2",
      "target_compound_id": "C11",
      "target_compound_name": "[18F]AlF-NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Ion trapping of [18F]fluoride on QMA cartridge and elution",
          "reactants": [
            {
              "compound_id": "C17",
              "name": "[18F]fluoride",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline (for elution)",
              "volume": "0.2 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride eluate in 0.2 mL saline",
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
          "notes": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water before trapping. [18F]fluoride is trapped and then eluted with 0.2 mL saline into the labeling vial."
        },
        {
          "step_number": 2,
          "reaction_type": "Al18F-NOTA chelation radiolabeling",
          "reactants": [
            {
              "compound_id": "C06",
              "name": "NP2",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "[18F]fluoride eluate in saline",
              "amount": "0.2 mL",
              "role": "radionuclide_source"
            },
            {
              "name": "Aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, 0.1 M, pH 4.0)",
              "amount": "3 μL (2 mM AlCl3, 0.1 M sodium acetate, pH 4.0)",
              "role": "chelation_catalyst"
            },
            {
              "name": "Sodium acetate buffer (0.1 M, pH 4.0)",
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
            "other": "Cooled to room temperature after reaction"
          },
          "product": {
            "compound_id": "C11",
            "name": "[18F]AlF-NP2",
            "yield": "62.76 ± 0.22% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "13.42 ± 1.25 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol. Ethanol solvent removed; final product resolved in saline.",
          "notes": "n ≥ 3 replicates. Identical procedure to P6 Step 2 except using NP2 as the precursor."
        }
      ]
    }
  ]
}
```

##### Claude_2
```
{
  "extraction": {
    "prompt_version": "v2.4",
    "extraction_date": "2026-03-20",
    "model_name": "claude-sonnet-4-6",
    "extractor_notes": "Detailed synthetic routes for all five precursors (DP1, DP2, DP3, NP1, NP2) are described as being in Schemes S1–S5 (Supporting Information). Only the synthesis of DP1 and NP1 has a full procedural description in the main text (Section 5.2.1). PR7, DP2, DP3, and NP2 are stated to be custom synthesised externally (Nanchang Tanzhen Biotechnology Co., Ltd.) and are therefore starting_materials. Radiolabeling procedures for all five radiotracers are provided in the main text (Section 5.4). MS data for all precursors are reported in Section 5.2 of the main text. Calculated masses for DP2, DP3, and NP2 appear to be nominal/average masses rather than monoisotopic masses based on the decimal values stated (e.g., DP2: 2743.2514; DP3: 3015.2514; NP2: 2642.20); this is common for large peptides and is noted but not corrected. KD and Bmax values are extracted from Figure 4G as required by Rule 21b. Docking scores are extracted from Figure 3B / main text Section 2.3 and assigned to the unlabeled precursor entries per Rule 21a. Log P values are assigned only to radiolabeled_product entries as measured with radioactivity counting. Blood T1/2 values are assigned only to the respective radiolabeled_product entries. The paper uses 'RCY' for radiochemical yield and 'RCP' for radiochemical purity. The Bmax values in Figure 4G are reported in CPM units. No 3H+ ion is reported for NP2 (only [M+2H]2+ = 1322.56). AlCl3 is included as a compound entry per Rule 6. DIPEA is included as a compound entry per Rule 6. DOTA-NHS and NOTA-NHS are external reagents used in the in-house coupling step and are therefore starting_materials. Sodium acetate buffers at pH 6.5 (for 68Ga labeling) and pH 4.0 (for 18F/AlF labeling) are assigned separate compound entries per Rule 6. 68GaCl3 and [18F]fluoride are assigned compound entries per Rule 6. Two separate radiolabeling pathways are defined: P3 for 68Ga-labeled series and P4 for 18F/AlF-labeled series; however, since each pathway must target exactly one compound (Rule 20), P3 targets [68Ga]Ga-DP1 (the first listed 68Ga radiotracer) and the procedure for DP2 and DP3 is noted as sharing the same protocol in P3 notes. Similarly P4 targets [18F]AlF-NP1. The paper notes that [68Ga]Ga-DP2 and [68Ga]Ga-DP3 use identical radiolabeling conditions to [68Ga]Ga-DP1 differing only in precursor. Per Rule 20, separate pathways P5 and P6 cover [68Ga]Ga-DP2 and [68Ga]Ga-DP3 respectively, and P7 covers [18F]AlF-NP2, using the same step structure with different precursors. PR7 KD of 1.57e-9 M is reported in the Discussion section (Section 3) as a literature value from ref 38, not measured in this study — it is nonetheless recorded in PR7's physicochemical_properties.other as externally reported."
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
    "mechanism_discussed": "synthetic",
    "method_completeness": "partial",
    "has_synthesis": true,
    "extraction_notes": "Detailed synthetic routes for DP2, DP3, NP2, and PR7 are in Supporting Information (Schemes S1–S5); main text gives only MS and HPLC characterization data for these externally synthesised compounds. Full in-house synthesis procedure is provided in the main text only for DP1 and NP1 (Section 5.2.1) and for all five radiolabeling reactions (Section 5.4). Radiochemical characteristics including RCYs, molar activities, and RCP values for all five radiotracers are summarised in Table S1 (Supporting Information); the main text quotes these values in Section 2.2. Calculated masses for DP2 (2743.2514), DP3 (3015.2514), and NP2 (2642.20) are likely nominal or average masses given the large peptide sizes; stated exactly as written in the paper without correction."
  },

  "compounds": [
    {
      "id": "C01",
      "name": "PR7",
      "iupac_name": null,
      "molecular_formula": "C96H133N25O31",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "ESI-MS calcd 2131.96; [M+2H]2+ = 1067.47; HPLC retention time 10.642 min; purity >95% by HPLC; KD = 1.57 × 10−9 M (reported from ref 38, not measured in this study); docking score −8.8 kcal/mol (AutoDock 4.2.6, ROR1 PDB: 6BA5); binding sites D27, N29, S72, R70, N51, T56, S55, E82, R81, V16, T344"
      },
      "description": "ROR1-targeting linear peptide lead compound selected for its moderate molecular weight, excellent binding affinity, and exceptional internalization efficiency; used as the parent scaffold for derivatization to DP1–3 and NP1–2, and as a blocking agent in cell uptake and PET imaging competition assays."
    },
    {
      "id": "C02",
      "name": "DP1",
      "iupac_name": null,
      "molecular_formula": "C112H159N29O38",
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "ESI-MS calcd 2518.14; [M+2H]2+ = 1260.54, [M+3H]3+ = 840.68; HPLC retention time 11.230 min; purity >95% by HPLC; docking score −9.1 kcal/mol (AutoDock 4.2.6, ROR1 PDB: 6BA5); binding sites K369, Q368, N29, S72, D30, S52, S55, W57, Q80, E82, T346, T344, P342, Y341, R81; forms 15 hydrogen bonds with ROR1"
      },
      "description": "DOTA-conjugated linear peptide precursor derived from PR7, synthesised in-house by coupling DOTA-NHS to PR7 in DMSO with DIPEA; serves as the radiolabeling precursor for [68Ga]Ga-DP1."
    },
    {
      "id": "C03",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "ESI-MS calcd 2743.2514 (likely nominal/average mass); [M+2H]2+ = 1373.07, [M+3H]3+ = 915.72; HPLC retention time 10.328 min; purity >95% by HPLC; docking score −7.7 kcal/mol (AutoDock 4.2.6, ROR1 PDB: 6BA5); binding sites E82, Q80, R81, W57, S55, R99, N95, E379, D31, Y99, Y100, L355, N338, N356; forms 14 hydrogen bonds with ROR1"
      },
      "description": "DOTA-conjugated cyclic peptide precursor (P2+L1+R3 architecture) custom synthesised externally; serves as the radiolabeling precursor for [68Ga]Ga-DP2."
    },
    {
      "id": "C04",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "ESI-MS calcd 3015.2514 (likely nominal/average mass); [M+2H]2+ = 1509.05, [M+3H]3+ = 1006.39; HPLC retention time 10.404 min; purity >95% by HPLC; docking score −7.9 kcal/mol (AutoDock 4.2.6, ROR1 PDB: 6BA5); binding sites N95, Y96, Y99, S55, N51, E379, P342, S339, N338; forms 9 hydrogen bonds with ROR1"
      },
      "description": "DOTA-conjugated cyclic peptide precursor (P2+L2+R3 architecture) custom synthesised externally; serves as the radiolabeling precursor for [68Ga]Ga-DP3."
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
        "other": "ESI-MS calcd 2417.09; [M+2H]2+ = 1210.22, [M+3H]3+ = 807.00; HPLC retention time 12.780 min; purity >95% by HPLC; docking score −8.3 kcal/mol (AutoDock 4.2.6, ROR1 PDB: 6BA5); binding sites S115, D76, G17, R70, T71, T73, S52, S55, N51, E379, K382, T344, T346"
      },
      "description": "NOTA-conjugated linear peptide precursor derived from PR7, synthesised in-house by coupling NOTA-NHS to PR7 in DMSO with DIPEA; serves as the radiolabeling precursor for [18F]AlF-NP1."
    },
    {
      "id": "C06",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "ESI-MS calcd 2642.20 (likely nominal/average mass); [M+2H]2+ = 1322.56; HPLC retention time 10.620 min; purity >95% by HPLC; docking score −7.6 kcal/mol (AutoDock 4.2.6, ROR1 PDB: 6BA5); binding sites N95, D31, Y99, Y100, D378, E379, P342, T344, Q340, N338, L355, N356"
      },
      "description": "NOTA-conjugated cyclic peptide precursor (P2+L1+R2 architecture) custom synthesised externally; serves as the radiolabeling precursor for [18F]AlF-NP2."
    },
    {
      "id": "C07",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.19 ± 0.05 (octanol/PBS, pH 7.4, radioactivity counting)",
        "other": "RCY 89.55 ± 0.12% RCY (n ≥ 3); RCP >95% by radio-HPLC; molar activity 14.37 ± 0.97 GBq/μmol (n ≥ 3); stability >90% RCP after 2 h in saline and fetal bovine serum; KD = 74.9 nM (saturation binding assay, MC38 cells); Bmax = 22158 CPM (MC38 cells); blood T1/2 = 7.62 min; MC38 tumor uptake 1.41 ± 0.08% ID/g at 30 min p.i. and 0.94 ± 0.07% ID/g at 60 min p.i.; kidney uptake 27.90 ± 4.36% ID/g at 30 min p.i., 20.91 ± 1.43% ID/g at 60 min p.i.; tumor-to-muscle ratio 2.47 ± 0.07 at 60 min p.i."
      },
      "description": "68Ga-labeled DOTA-DP1 radiotracer prepared by heating DP1 precursor with 68GaCl3 in sodium acetate buffer; evaluated by PET imaging across multiple tumor models and shown to have excellent ROR1 targeting and favorable pharmacokinetics."
    },
    {
      "id": "C08",
      "name": "[68Ga]Ga-DP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.53 ± 0.04 (octanol/PBS, pH 7.4, radioactivity counting)",
        "other": "RCY 97.67 ± 1.05% RCY (n ≥ 3); RCP >95% by radio-HPLC; molar activity 20.05 ± 1.35 GBq/μmol (n ≥ 3); stability >90% RCP after 2 h in saline and fetal bovine serum; KD = 154.9 nM (saturation binding assay, MC38 cells); Bmax = 31268 CPM (MC38 cells); MC38 tumor uptake 0.52 ± 0.11% ID/g at 30 min p.i."
      },
      "description": "68Ga-labeled DOTA-DP2 cyclic peptide radiotracer prepared by heating DP2 precursor with 68GaCl3 in sodium acetate buffer; exhibited significant kidney accumulation limiting diagnostic utility."
    },
    {
      "id": "C09",
      "name": "[68Ga]Ga-DP3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−1.82 ± 0.03 (octanol/PBS, pH 7.4, radioactivity counting)",
        "other": "RCY 98.01 ± 0.97% RCY (n ≥ 3); RCP >95% by radio-HPLC; molar activity 14.09 ± 2.12 GBq/μmol (n ≥ 3); stability >90% RCP after 2 h in saline and fetal bovine serum; KD = 213.4 nM (saturation binding assay, MC38 cells); Bmax = 47017 CPM (MC38 cells); MC38 tumor uptake 0.31 ± 0.05% ID/g at 30 min p.i."
      },
      "description": "68Ga-labeled DOTA-DP3 cyclic peptide radiotracer prepared by heating DP3 precursor with 68GaCl3 in sodium acetate buffer; showed the lowest tumor uptake among the 68Ga series due to fewer hydrogen bonds with ROR1."
    },
    {
      "id": "C10",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.10 ± 0.04 (octanol/PBS, pH 7.4, radioactivity counting)",
        "other": "RCY 62.58 ± 0.32% RCY (n ≥ 3); RCP >95% by radio-HPLC; molar activity 13.13 ± 1.71 GBq/μmol (n ≥ 3); stability >90% RCP after 2 h in saline and fetal bovine serum; metabolic stability: approximately 4% intact probe in urine at 0.5 h p.i., almost none at 1 h p.i. in normal mice; KD = 141.7 nM (saturation binding assay, MC38 cells); Bmax = 31406 CPM (MC38 cells); blood T1/2 = 19.32 min; MC38 tumor uptake 2.89 ± 0.07% ID/g at 30 min p.i. and 1.32 ± 0.14% ID/g at 60 min p.i.; kidney uptake 27.27 ± 2.99% ID/g at 30 min p.i., 17.74 ± 4.53% ID/g at 60 min p.i.; tumor-to-muscle ratio 2.62 ± 0.06 at 60 min p.i."
      },
      "description": "18F-labeled AlF-NOTA-NP1 radiotracer prepared by trapping [18F]fluoride on QMA, eluting into AlCl3/NOTA-NP1 solution, and heating; demonstrated excellent ROR1 tumor targeting, favorable pharmacokinetics with renal clearance, and superior performance in multiple tumor models."
    },
    {
      "id": "C11",
      "name": "[18F]AlF-NP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "−2.54 ± 0.04 (octanol/PBS, pH 7.4, radioactivity counting)",
        "other": "RCY 62.76 ± 0.22% RCY (n ≥ 3); RCP >95% by radio-HPLC; molar activity 13.42 ± 1.25 GBq/μmol (n ≥ 3); stability >90% RCP after 2 h in saline and fetal bovine serum; KD = 212.1 nM (saturation binding assay, MC38 cells); Bmax = 22986 CPM (MC38 cells)"
      },
      "description": "18F-labeled AlF-NOTA-NP2 cyclic peptide radiotracer prepared by the AlF chelation method; showed lower tumor uptake and significant kidney accumulation compared to [18F]AlF-NP1."
    },
    {
      "id": "C12",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "N-hydroxysuccinimide ester of DOTA used as an activated chelator for conjugation to the primary amine of PR7 to yield the DP1 precursor."
    },
    {
      "id": "C13",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "N-hydroxysuccinimide ester of NOTA used as an activated chelator for conjugation to the primary amine of PR7 to yield the NP1 precursor."
    },
    {
      "id": "C14",
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
      "description": "N,N-Diisopropylethylamine used as an organic base to facilitate NHS ester coupling reactions in the synthesis of DP1 and NP1."
    },
    {
      "id": "C15",
      "name": "68GaCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "68Ge-68Ga generator (ITM)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Gallium-68 trichloride eluted from a 68Ge/68Ga generator in 0.1 M HCl; used as the radionuclide source for 68Ga-labeling of DP1, DP2, and DP3 precursors."
    },
    {
      "id": "C16",
      "name": "Sodium acetate buffer pH 6.5",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial/in-house preparation",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate solution at 0.25 M in water at pH 6.5 used to adjust the pH of the 68GaCl3 solution to pH 4–4.5 prior to 68Ga-labeling reactions."
    },
    {
      "id": "C17",
      "name": "[18F]fluoride",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "produced in-house via 18O(p,n)18F reaction by Cyclone 18/9 (IBA, Belgium) at the Center for Molecular Imaging and Translational Medicine of Xiamen University",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Fluorine-18 fluoride ion produced by cyclotron bombardment of 18O-enriched water; trapped on a QMA cartridge and eluted with saline as the radionuclide source for AlF-labeling of NP1 and NP2."
    },
    {
      "id": "C18",
      "name": "Aluminum chloride (AlCl3)",
      "iupac_name": null,
      "molecular_formula": "AlCl3",
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Aluminum chloride at 2 mM in sodium acetate buffer (pH 4.0) used as the aluminum source to form the Al18F complex with [18F]fluoride prior to chelation by NOTA-peptide precursors."
    },
    {
      "id": "C19",
      "name": "Sodium acetate buffer pH 4.0",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial/in-house preparation",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate buffer at 0.1 M and pH 4.0 used as the reaction medium for AlF-chelation radiolabeling of NOTA-peptide precursors with [18F]fluoride and AlCl3."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of DP1",
      "target_compound_id": "C02",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 μmol)"
            },
            {
              "compound_id": "C12",
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
            "other": "agitated in an oscillator; reaction performed in a 2 mL centrifugation tube"
          },
          "product": {
            "compound_id": "C02",
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
          "purification": "Semipreparative HPLC with UV detection at 254 nm; mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min at 1 mL/min; followed by lyophilization",
          "notes": "DP1 and NP1 are synthesised in the same reaction setup (parallel reactions in separate vials using DOTA-NHS and NOTA-NHS respectively). Full synthetic routes in Schemes S1 and S4 (Supporting Information)."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of NP1",
      "target_compound_id": "C05",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "PR7",
              "amount": "6.4 mg (3 μmol)"
            },
            {
              "compound_id": "C13",
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
            "other": "agitated in an oscillator; reaction performed in a 2 mL centrifugation tube"
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
          "purification": "Semipreparative HPLC with UV detection at 254 nm; mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min at 1 mL/min; followed by lyophilization",
          "notes": "Synthesised in parallel with DP1 under identical conditions using NOTA-NHS instead of DOTA-NHS. Full synthetic route in Scheme S4 (Supporting Information)."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP1",
      "target_compound_id": "C07",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3 with sodium acetate buffer",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            },
            {
              "compound_id": "C16",
              "name": "Sodium acetate buffer pH 6.5",
              "amount": "0.5 mL (0.25 M, pH 6.5)"
            }
          ],
          "reagents": [],
          "solvents": [],
          "conditions": {
            "temperature": "room temperature",
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
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
          "notes": "The pH of the mixed solution is adjusted to 4–4.5 by diluting 1 mL 68GaCl3 (in 0.1 M HCl) with 0.5 mL sodium acetate buffer (0.25 M, pH 6.5)."
        },
        {
          "step_number": 2,
          "reaction_type": "Radiometal chelation (68Ga-DOTA complexation)",
          "reactants": [
            {
              "compound_id": null,
              "name": "68GaCl3–sodium acetate solution at pH 4–4.5",
              "amount": "1.5 mL (0.74–1.11 GBq)"
            },
            {
              "compound_id": "C02",
              "name": "DP1 precursor",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "other": "Cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C07",
            "name": "[68Ga]Ga-DP1",
            "yield": "89.55 ± 0.12% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "14.37 ± 0.97 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol; ethanol solvent removed; product resolved in saline",
          "notes": "Radio-HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min at 1 mL/min. n ≥ 3 replicates. Same protocol used for [68Ga]Ga-DP2 and [68Ga]Ga-DP3 with DP2 and DP3 substituted as precursor respectively."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP2",
      "target_compound_id": "C08",
      "target_compound_name": "[68Ga]Ga-DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3 with sodium acetate buffer",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            },
            {
              "compound_id": "C16",
              "name": "Sodium acetate buffer pH 6.5",
              "amount": "0.5 mL (0.25 M, pH 6.5)"
            }
          ],
          "reagents": [],
          "solvents": [],
          "conditions": {
            "temperature": "room temperature",
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
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
          "reaction_type": "Radiometal chelation (68Ga-DOTA complexation)",
          "reactants": [
            {
              "compound_id": null,
              "name": "68GaCl3–sodium acetate solution at pH 4–4.5",
              "amount": "1.5 mL (0.74–1.11 GBq)"
            },
            {
              "compound_id": "C03",
              "name": "DP2 precursor",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "other": "Cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C08",
            "name": "[68Ga]Ga-DP2",
            "yield": "97.67 ± 1.05% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "20.05 ± 1.35 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol; ethanol solvent removed; product resolved in saline",
          "notes": "Identical protocol to [68Ga]Ga-DP1 radiolabeling with DP2 substituted as precursor."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP3",
      "target_compound_id": "C09",
      "target_compound_name": "[68Ga]Ga-DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of 68GaCl3 with sodium acetate buffer",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "68GaCl3 in 0.1 M HCl",
              "amount": "1 mL (0.74–1.11 GBq)"
            },
            {
              "compound_id": "C16",
              "name": "Sodium acetate buffer pH 6.5",
              "amount": "0.5 mL (0.25 M, pH 6.5)"
            }
          ],
          "reagents": [],
          "solvents": [],
          "conditions": {
            "temperature": "room temperature",
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
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
          "reaction_type": "Radiometal chelation (68Ga-DOTA complexation)",
          "reactants": [
            {
              "compound_id": null,
              "name": "68GaCl3–sodium acetate solution at pH 4–4.5",
              "amount": "1.5 mL (0.74–1.11 GBq)"
            },
            {
              "compound_id": "C04",
              "name": "DP3 precursor",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [],
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
            "other": "Cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C09",
            "name": "[68Ga]Ga-DP3",
            "yield": "98.01 ± 0.97% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "14.09 ± 2.12 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol; ethanol solvent removed; product resolved in saline",
          "notes": "Identical protocol to [68Ga]Ga-DP1 radiolabeling with DP3 substituted as precursor."
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Radiolabeling of [18F]AlF-NP1",
      "target_compound_id": "C10",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Solid-phase trapping of [18F]fluoride on QMA cartridge",
          "reactants": [
            {
              "compound_id": "C17",
              "name": "[18F]fluoride",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline (10 mL for conditioning)",
              "volume": "10 mL"
            },
            {
              "name": "pure water (10 mL for conditioning)",
              "volume": "10 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water prior to trapping"
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
          "notes": "QMA cartridge used as a solid-phase anion exchange concentrator for [18F]fluoride."
        },
        {
          "step_number": 2,
          "reaction_type": "Elution of [18F]fluoride from QMA and preparation of reaction mixture",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride trapped on QMA cartridge",
              "amount": null
            }
          ],
          "reagents": [
            {
              "name": "AlCl3 in sodium acetate buffer",
              "amount": "3 μL (2 mM AlCl3 in 0.1 M sodium acetate, pH 4.0)",
              "role": "chelation_catalyst"
            },
            {
              "name": "Sodium acetate buffer pH 4.0",
              "amount": "100 μL (0.1 M, pH 4.0)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "saline",
              "volume": "0.2 mL"
            },
            {
              "name": "acetonitrile",
              "volume": "200 μL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Eluted with 0.2 mL saline into reaction vial; reaction vial contains AlCl3 solution, acetonitrile, sodium acetate buffer, and precursor"
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride–AlCl3–NP1 reaction mixture",
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
          "notes": "The reaction vial contains 3 μL of 2 mM AlCl3 in sodium acetate buffer (0.1 M, pH 4.0), 200 μL acetonitrile, 100 μL sodium acetate buffer (0.1 M, pH 4.0), and 50 μg (18–25 nmol) NP1 precursor in 50 μL DMSO; [18F]fluoride eluted in 0.2 mL saline directly into this vial."
        },
        {
          "step_number": 3,
          "reaction_type": "AlF18F chelation by NOTA (radiolabeling)",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride–AlCl3–NP1 reaction mixture",
              "amount": null
            },
            {
              "compound_id": "C05",
              "name": "NP1 precursor",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C18",
              "name": "AlCl3",
              "amount": "3 μL (2 mM in sodium acetate buffer, pH 4.0)",
              "role": "chelation_catalyst"
            },
            {
              "compound_id": "C19",
              "name": "Sodium acetate buffer pH 4.0",
              "amount": "100 μL (0.1 M, pH 4.0)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 μL"
            },
            {
              "name": "acetonitrile",
              "volume": "200 μL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C10",
            "name": "[18F]AlF-NP1",
            "yield": "62.58 ± 0.32% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "13.13 ± 1.71 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol; ethanol solvent removed; product resolved in saline",
          "notes": "Radio-HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B gradient to 95% B over 20 min at 1 mL/min. n ≥ 3 replicates."
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Radiolabeling of [18F]AlF-NP2",
      "target_compound_id": "C11",
      "target_compound_name": "[18F]AlF-NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Solid-phase trapping of [18F]fluoride on QMA cartridge",
          "reactants": [
            {
              "compound_id": "C17",
              "name": "[18F]fluoride",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline (10 mL for conditioning)",
              "volume": "10 mL"
            },
            {
              "name": "pure water (10 mL for conditioning)",
              "volume": "10 mL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water prior to trapping"
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
          "reaction_type": "Elution of [18F]fluoride from QMA and preparation of reaction mixture",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride trapped on QMA cartridge",
              "amount": null
            }
          ],
          "reagents": [
            {
              "name": "AlCl3 in sodium acetate buffer",
              "amount": "3 μL (2 mM AlCl3 in 0.1 M sodium acetate, pH 4.0)",
              "role": "chelation_catalyst"
            },
            {
              "name": "Sodium acetate buffer pH 4.0",
              "amount": "100 μL (0.1 M, pH 4.0)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "saline",
              "volume": "0.2 mL"
            },
            {
              "name": "acetonitrile",
              "volume": "200 μL"
            }
          ],
          "conditions": {
            "temperature": "room temperature",
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Eluted with 0.2 mL saline into reaction vial containing AlCl3, acetonitrile, sodium acetate buffer, and NP2 precursor"
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride–AlCl3–NP2 reaction mixture",
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
          "step_number": 3,
          "reaction_type": "AlF18F chelation by NOTA (radiolabeling)",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride–AlCl3–NP2 reaction mixture",
              "amount": null
            },
            {
              "compound_id": "C06",
              "name": "NP2 precursor",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C18",
              "name": "AlCl3",
              "amount": "3 μL (2 mM in sodium acetate buffer, pH 4.0)",
              "role": "chelation_catalyst"
            },
            {
              "compound_id": "C19",
              "name": "Sodium acetate buffer pH 4.0",
              "amount": "100 μL (0.1 M, pH 4.0)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 μL"
            },
            {
              "name": "acetonitrile",
              "volume": "200 μL"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C11",
            "name": "[18F]AlF-NP2",
            "yield": "62.76 ± 0.22% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "13.42 ± 1.25 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); elution with 1.5 mL ethanol; ethanol solvent removed; product resolved in saline",
          "notes": "Identical protocol to [18F]AlF-NP1 radiolabeling with NP2 substituted as precursor. n ≥ 3 replicates."
        }
      ]
    }
  ]
}
```

##### Claude 3
```
{
  "extraction": {
    "prompt_version": "v2.4",
    "extraction_date": "2025-12-28",
    "model_name": "claude-sonnet-4-6",
    "extractor_notes": "Detailed synthetic routes for all five precursors (DP1, DP2, DP3, NP1, NP2) are described as being in Schemes S1–S5 (Supporting Information), which are not present in the provided document. Only the synthesis of DP1 and NP1 is described in the main text (Section 5.2.1). PR7, DP2, DP3, and NP2 were custom synthesized externally and their synthesis routes are not in the main text. Radiochemical characteristics (RCY, molar activity, RCP) for all five radiotracers are stated to be summarized in Table S1; the main text provides summary values for RCY and molar activity. The MS data for large peptides (e.g., DP2, DP3, NP1, NP2, PR7) appear to use nominal/average masses rather than monoisotopic masses based on the molecular weights reported (e.g., DP2 calcd 2743.2514 vs expected monoisotopic ~2742). Bmax values are extracted from Figure 4G as they appear in a figure panel table. Two distinct sodium acetate buffer solutions are used in the radiolabeling procedures: one at pH 6.5 (0.25 M) for 68Ga labeling and one at pH 4.0 (0.1 M) for 18F/AlF labeling — these are assigned separate compound entries. AlCl3 solution is used as a chelation catalyst in the AlF labeling and receives its own entry."
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
    "mechanism_discussed": "synthetic",
    "method_completeness": "partial",
    "has_synthesis": true,
    "extraction_notes": "Synthetic routes for DP1 and NP1 are fully described in the main text (Section 5.2.1). All other precursor syntheses (PR7, DP2, DP3, NP2) were performed by an external vendor (Nanchang Tanzhen Biotechnology Co., Ltd.) and no in-house synthetic route is provided. Radiolabeling procedures for all five radiotracers are fully described in Section 5.4. MS data for large peptides may use average/nominal masses rather than monoisotopic masses; the reported calculated masses for DP1 (2518.14), NP1 (2417.09), PR7 (2131.96), DP2 (2743.2514), DP3 (3015.2514), and NP2 (2642.20) are recorded exactly as stated. Bmax values (CPM) extracted from Figure 4G panel. KD values reported as point estimates in text (74.9, 154.9, 213.4, 141.7, 212.1 nM) without error bars in the main text narrative."
  },

  "compounds": [
    {
      "id": "C01",
      "name": "[18F]AlF-NP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "-2.10 ± 0.04",
        "other": "RCY = 62.58 ± 0.32% RCY; RCP >90%; molar activity = 13.13 ± 1.71 GBq/μmol (n ≥ 3); stability in saline and serum >90% RCP after 2 h; metabolic stability: ~4% intact probe detectable in urine at 0.5 h p.i., almost no intact probe at 1 h p.i.; KD = 141.7 nM (saturation binding, MC38 cells); Bmax = 31406 CPM (saturation binding, MC38 cells); blood T½ = 19.32 min; MC38 tumor uptake = 1.41 ± 0.08% ID/g at 30 min p.i. (biodistribution) — NOTE: the 1.41 value is attributed to [68Ga]Ga-DP1 in the biodistribution section; [18F]AlF-NP1 MC38 tumor uptake = 2.89 ± 0.07% ID/g at 30 min p.i. and 1.32 ± 0.14% ID/g at 60 min p.i.; kidney uptake = 27.27 ± 2.99% ID/g at 30 min p.i. and 17.74 ± 4.53% ID/g at 60 min p.i.; tumor-to-muscle ratio = 2.62 ± 0.06 at 60 min p.i.; MC38 cell uptake = 10.30 ± 1.40% total activity at 30 min; docking score not applicable (radiometal-labeled product); HPLC RCP >95% by radio-HPLC"
      },
      "description": "18F-labeled aluminum fluoride chelate of the NOTA-conjugated linear peptide NP1, developed as a ROR1-targeted PET radiotracer with excellent tumor uptake, favorable pharmacokinetics, and renal clearance."
    },
    {
      "id": "C02",
      "name": "[68Ga]Ga-DP1",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "-2.19 ± 0.05",
        "other": "RCY = 89.55 ± 0.12% RCY; RCP >90%; molar activity = 14.37 ± 0.97 GBq/μmol (n ≥ 3); stability in saline and serum >90% RCP after 2 h; KD = 74.9 nM (saturation binding, MC38 cells); Bmax = 22158 CPM (saturation binding, MC38 cells); blood T½ = 7.62 min; MC38 tumor uptake = 1.41 ± 0.08% ID/g at 30 min p.i. and 0.94 ± 0.07% ID/g at 60 min p.i. (biodistribution); kidney uptake = 27.90 ± 4.36% ID/g at 30 min p.i. and 20.91 ± 1.43% ID/g at 60 min p.i.; tumor-to-muscle ratio = 2.47 ± 0.07 at 60 min p.i.; PET MC38 tumor uptake = 0.65 ± 0.13% ID/g at 30 min p.i.; MC38 cell uptake = 7.26 ± 0.49% total activity at 30 min; HPLC RCP >95% by radio-HPLC"
      },
      "description": "68Ga-labeled DOTA chelate of the linear peptide DP1, serving as a ROR1-targeted PET radiotracer with high tumor uptake in MC38 models and favorable target-to-background ratios."
    },
    {
      "id": "C03",
      "name": "PR7",
      "iupac_name": null,
      "molecular_formula": "C96H133N25O31",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "ESI-MS calcd 2131.96 (nominal/average mass); found [M+2H]2+ = 1067.47; HPLC retention time = 10.642 min; purity >95% by HPLC (mobile phase: 0.1% TFA in water/0.1% TFA in MeCN, 23% B to 43% B over 20 min, 1 mL/min); molecular docking score = -8.8 kcal/mol (AutoDock 4.2.6, ROR1 PDB: 6BA5); binding sites: D27, N29, S72, R70, N51, T56, S55, E82, R81, V16, T344; KD (as lead compound from prior literature) = 1.57 × 10-9 M"
      },
      "description": "Lead ROR1-targeting peptide (PR7) used as the parent scaffold for derivatization and as a blocking agent in cell uptake, PET imaging, and autoradiography experiments."
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
        "other": "ESI-MS calcd 2518.14 (nominal/average mass); found [M+2H]2+ = 1260.54, [M+3H]3+ = 840.68; HPLC retention time = 11.230 min; purity >95% by HPLC (mobile phase: 0.1% TFA in water/0.1% TFA in MeCN, 5% B to 95% B over 20 min, 1 mL/min); yield = 4.2 mg (55.6%); molecular docking score = -9.1 kcal/mol (AutoDock 4.2.6, ROR1 PDB: 6BA5); binding sites: K369, Q368, N29, S72, D30, S52, S55, W57, Q80, E82, T346, T344, P342, Y341, R81; forms 15 hydrogen bonds with ROR1"
      },
      "description": "DOTA-conjugated linear peptide precursor derived from PR7 by NHS ester coupling, synthesized in-house and used as the radiolabeling precursor for [68Ga]Ga-DP1."
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
        "other": "ESI-MS calcd 2417.09 (nominal/average mass); found [M+2H]2+ = 1210.22, [M+3H]3+ = 807.00; HPLC retention time = 12.780 min; purity >95% by HPLC (mobile phase: 0.1% TFA in water/0.1% TFA in MeCN, 5% B to 95% B over 20 min, 1 mL/min); yield = 3.9 mg (54%); molecular docking score = -8.3 kcal/mol (AutoDock 4.2.6, ROR1 PDB: 6BA5); binding sites: S115, D76, G17, R70, T71, T73, S52, S55, N51, E379, K382, T344, T346"
      },
      "description": "NOTA-conjugated linear peptide precursor derived from PR7 by NHS ester coupling, synthesized in-house and used as the radiolabeling precursor for [18F]AlF-NP1."
    },
    {
      "id": "C06",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "ESI-MS calcd 2743.2514 (nominal/average mass); found [M+2H]2+ = 1373.07, [M+3H]3+ = 915.72; HPLC retention time = 10.328 min; purity >95% by HPLC (mobile phase: 0.1% TFA in water/0.1% TFA in MeCN, 23% B to 43% B over 20 min, 1 mL/min); molecular docking score = -7.7 kcal/mol (AutoDock 4.2.6, ROR1 PDB: 6BA5); binding sites: E82, Q80, R81, W57, S55, R99, N95, E379, D31, Y99, Y100, L355, N338, N356; forms 14 hydrogen bonds with ROR1"
      },
      "description": "DOTA-conjugated cyclic peptide precursor (P2+L1+R3 architecture) custom-synthesized externally and used as the radiolabeling precursor for [68Ga]Ga-DP2."
    },
    {
      "id": "C07",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "ESI-MS calcd 3015.2514 (nominal/average mass); found [M+2H]2+ = 1509.05, [M+3H]3+ = 1006.39; HPLC retention time = 10.404 min; purity >95% by HPLC (mobile phase: 0.1% TFA in water/0.1% TFA in MeCN, 23% B to 43% B over 20 min, 1 mL/min); molecular docking score = -7.9 kcal/mol (AutoDock 4.2.6, ROR1 PDB: 6BA5); binding sites: N95, Y96, Y99, S55, N51, E379, P342, S339, N338; forms only 9 hydrogen bonds with ROR1"
      },
      "description": "DOTA-conjugated cyclic peptide precursor (P2+L2+R3 architecture, contains disulfide bridges) custom-synthesized externally and used as the radiolabeling precursor for [68Ga]Ga-DP3."
    },
    {
      "id": "C08",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "ESI-MS calcd 2642.20 (nominal/average mass); found [M+2H]2+ = 1322.56; HPLC retention time = 10.620 min; purity >95% by HPLC (mobile phase: 0.1% TFA in water/0.1% TFA in MeCN, 23% B to 43% B over 20 min, 1 mL/min); molecular docking score = -7.6 kcal/mol (AutoDock 4.2.6, ROR1 PDB: 6BA5); binding sites: N95, D31, Y99, Y100, D378, E379, P342, T344, Q340, N338, L355, N356"
      },
      "description": "NOTA-conjugated cyclic peptide precursor (P2+L1+R2 architecture) custom-synthesized externally and used as the radiolabeling precursor for [18F]AlF-NP2."
    },
    {
      "id": "C09",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "N-hydroxysuccinimide ester of DOTA used as an activated chelator for conjugation to the amine group of PR7 to produce DP1."
    },
    {
      "id": "C10",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesis)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "N-hydroxysuccinimide ester of NOTA used as an activated chelator for conjugation to the amine group of PR7 to produce NP1."
    },
    {
      "id": "C11",
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
      "description": "Hindered organic base (N,N-diisopropylethylamine) used to facilitate NHS ester coupling of DOTA-NHS or NOTA-NHS to PR7."
    },
    {
      "id": "C12",
      "name": "68GaCl3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "68Ge-68Ga generator (ITM)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "supplied in 0.1 M HCl; activity range 0.74–1.11 GBq per batch"
      },
      "description": "Gallium-68 trichloride radionuclide source eluted from a 68Ge/68Ga generator and used for radiolabeling of DOTA-conjugated peptide precursors."
    },
    {
      "id": "C13",
      "name": "sodium acetate buffer (0.25 M, pH 6.5)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate buffer at pH 6.5 used to dilute and adjust the pH of the 68GaCl3 solution prior to 68Ga radiolabeling of DOTA-peptide precursors."
    },
    {
      "id": "C14",
      "name": "[68Ga]Ga-DP2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "-2.53 ± 0.04",
        "other": "RCY = 97.67 ± 1.05% RCY; RCP >90%; molar activity = 20.05 ± 1.35 GBq/μmol (n ≥ 3); stability in saline and serum >90% RCP after 2 h; KD = 154.9 nM (saturation binding, MC38 cells); Bmax = 31268 CPM (saturation binding, MC38 cells); PET MC38 tumor uptake = 0.52 ± 0.11% ID/g at 30 min p.i.; MC38 cell uptake = 2.50 ± 0.36% total activity at 30 min; HPLC RCP >95% by radio-HPLC"
      },
      "description": "68Ga-labeled DOTA chelate of the cyclic peptide DP2, evaluated as a ROR1-targeted PET radiotracer with comparable tumor uptake to [68Ga]Ga-DP1 but higher kidney accumulation."
    },
    {
      "id": "C15",
      "name": "[68Ga]Ga-DP3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "radiolabeled_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": "-1.82 ± 0.03",
        "other": "RCY = 98.01 ± 0.97% RCY; RCP >90%; molar activity = 14.09 ± 2.12 GBq/μmol (n ≥ 3); stability in saline and serum >90% RCP after 2 h; KD = 213.4 nM (saturation binding, MC38 cells); Bmax = 47017 CPM (saturation binding, MC38 cells); PET MC38 tumor uptake = 0.31 ± 0.05% ID/g at 30 min p.i.; MC38 cell uptake = 1.07 ± 0.07% total activity at 30 min; HPLC RCP >95% by radio-HPLC"
      },
      "description": "68Ga-labeled DOTA chelate of the cyclic peptide DP3, evaluated as a ROR1-targeted PET radiotracer with lower tumor uptake and higher lipophilicity compared to [68Ga]Ga-DP1."
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
        "log_p": "-2.54 ± 0.04",
        "other": "RCY = 62.76 ± 0.22% RCY; RCP >90%; molar activity = 13.42 ± 1.25 GBq/μmol (n ≥ 3); stability in saline and serum >90% RCP after 2 h; KD = 212.1 nM (saturation binding, MC38 cells); Bmax = 22986 CPM (saturation binding, MC38 cells); MC38 cell uptake = 0.68 ± 0.04% total activity at 30 min; HPLC RCP >95% by radio-HPLC"
      },
      "description": "18F-labeled aluminum fluoride chelate of the NOTA-conjugated cyclic peptide NP2, evaluated as a ROR1-targeted PET radiotracer with lower tumor uptake and pronounced renal accumulation compared to [18F]AlF-NP1."
    },
    {
      "id": "C17",
      "name": "fluoride-18 ([18F]fluoride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "in-house cyclotron production; Cyclone 18/9 (IBA), Center for Molecular Imaging and Translational Medicine, Xiamen University",
      "physicochemical_properties": {
        "log_p": null,
        "other": "produced via 18O(p,n)18F reaction; activity approximately 0.74–1.11 GBq per batch; initially trapped on QMA cartridge, eluted with 0.2 mL saline"
      },
      "description": "Cyclotron-produced fluoride-18 radionuclide source used for AlF-based 18F-radiolabeling of NOTA-conjugated peptide precursors."
    },
    {
      "id": "C18",
      "name": "aluminum chloride (AlCl3) solution in sodium acetate buffer (2 mM, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Aluminum chloride solution used as the aluminum(III) source for forming the Al18F complex during AlF-based radiolabeling of NOTA-conjugated peptides."
    },
    {
      "id": "C19",
      "name": "sodium acetate buffer (0.1 M, pH 4.0)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Sodium acetate buffer at pH 4.0 used both as the solvent for the AlCl3 solution and as an additional buffer component in the reaction vial for AlF-based 18F-radiolabeling."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of DP1 (DOTA-PR7 conjugate)",
      "target_compound_id": "C04",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling",
          "reactants": [
            {
              "compound_id": "C03",
              "name": "PR7",
              "amount": "6.4 mg (3 μmol)"
            },
            {
              "compound_id": "C09",
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
            "other": "agitated in oscillator; vessel: 2 mL centrifugation tube"
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
          "purification": "Semipreparative HPLC with UV detection at 254 nm; lyophilization after collection",
          "notes": "DP1 and NP1 were synthesized in the same reaction setup in parallel (separate reaction tubes, one with DOTA-NHS and one with NOTA-NHS). HPLC method: 0.1% TFA in water (A) / 0.1% TFA in MeCN (B); 5% B to 95% B over 20 min, 1 mL/min. Calculated mass may be nominal/average rather than monoisotopic for this large peptide."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of NP1 (NOTA-PR7 conjugate)",
      "target_compound_id": "C05",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NHS ester amide coupling",
          "reactants": [
            {
              "compound_id": "C03",
              "name": "PR7",
              "amount": "6.4 mg (3 μmol)"
            },
            {
              "compound_id": "C10",
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
            "other": "agitated in oscillator; vessel: 2 mL centrifugation tube"
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
          "purification": "Semipreparative HPLC with UV detection at 254 nm; lyophilization after collection",
          "notes": "NP1 synthesized in parallel with DP1 in a separate reaction tube under identical conditions, using NOTA-NHS instead of DOTA-NHS. HPLC method: 0.1% TFA in water (A) / 0.1% TFA in MeCN (B); 5% B to 95% B over 20 min, 1 mL/min. Calculated mass may be nominal/average rather than monoisotopic for this large peptide."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP1",
      "target_compound_id": "C02",
      "target_compound_name": "[68Ga]Ga-DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C12",
              "name": "68GaCl3",
              "amount": "1 mL (0.74–1.11 GBq in 0.1 M HCl)"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate buffer (0.25 M, pH 6.5)",
              "amount": "0.5 mL (0.25 M, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": "68GaCl3 diluted with sodium acetate buffer to achieve pH 4–4.5"
          },
          "product": {
            "compound_id": null,
            "name": "pH-adjusted 68GaCl3–sodium acetate solution",
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
          "notes": "Total volume after mixing: 1.5 mL; resulting pH of 68GaCl3–sodium acetate solution is 4–4.5."
        },
        {
          "step_number": 2,
          "reaction_type": "Radiometal chelation (68Ga DOTA complexation)",
          "reactants": [
            {
              "compound_id": "C04",
              "name": "DP1 (precursor)",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "pH-adjusted 68GaCl3–sodium acetate solution (from Step 1)",
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
            "other": "precursor dissolved in 50 μL DMSO in reaction vial; cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C02",
            "name": "[68Ga]Ga-DP1",
            "yield": "89.55 ± 0.12% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "14.37 ± 0.97 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluent: 1.5 mL ethanol; final product resolved in saline after ethanol removal",
          "notes": "HPLC method for RCP analysis: 0.1% TFA in water (A) / 0.1% TFA in MeCN (B); 5% B to 95% B over 20 min, 1 mL/min. RCY and molar activity reported as mean ± SD, n ≥ 3. Radiochemical characteristics detailed in Table S1 (SI)."
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP2",
      "target_compound_id": "C14",
      "target_compound_name": "[68Ga]Ga-DP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C12",
              "name": "68GaCl3",
              "amount": "1 mL (0.74–1.11 GBq in 0.1 M HCl)"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate buffer (0.25 M, pH 6.5)",
              "amount": "0.5 mL (0.25 M, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": "68GaCl3 diluted with sodium acetate buffer to achieve pH 4–4.5"
          },
          "product": {
            "compound_id": null,
            "name": "pH-adjusted 68GaCl3–sodium acetate solution",
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
          "notes": "Same pH adjustment procedure as for [68Ga]Ga-DP1 and [68Ga]Ga-DP3."
        },
        {
          "step_number": 2,
          "reaction_type": "Radiometal chelation (68Ga DOTA complexation)",
          "reactants": [
            {
              "compound_id": "C06",
              "name": "DP2 (precursor)",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "pH-adjusted 68GaCl3–sodium acetate solution (from Step 1)",
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
            "other": "precursor dissolved in 50 μL DMSO in reaction vial; cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C14",
            "name": "[68Ga]Ga-DP2",
            "yield": "97.67 ± 1.05% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "20.05 ± 1.35 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluent: 1.5 mL ethanol; final product resolved in saline after ethanol removal",
          "notes": "Same radiolabeling procedure as [68Ga]Ga-DP1 except precursor is DP2. Radiochemical characteristics detailed in Table S1 (SI)."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Radiolabeling of [68Ga]Ga-DP3",
      "target_compound_id": "C15",
      "target_compound_name": "[68Ga]Ga-DP3",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "pH adjustment of radionuclide solution",
          "reactants": [
            {
              "compound_id": "C12",
              "name": "68GaCl3",
              "amount": "1 mL (0.74–1.11 GBq in 0.1 M HCl)"
            }
          ],
          "reagents": [
            {
              "name": "sodium acetate buffer (0.25 M, pH 6.5)",
              "amount": "0.5 mL (0.25 M, pH 6.5)",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": "4–4.5",
            "other": "68GaCl3 diluted with sodium acetate buffer to achieve pH 4–4.5"
          },
          "product": {
            "compound_id": null,
            "name": "pH-adjusted 68GaCl3–sodium acetate solution",
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
          "notes": "Same pH adjustment procedure as for [68Ga]Ga-DP1 and [68Ga]Ga-DP2."
        },
        {
          "step_number": 2,
          "reaction_type": "Radiometal chelation (68Ga DOTA complexation)",
          "reactants": [
            {
              "compound_id": "C07",
              "name": "DP3 (precursor)",
              "amount": "50 μg (16–20 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "pH-adjusted 68GaCl3–sodium acetate solution (from Step 1)",
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
            "other": "precursor dissolved in 50 μL DMSO in reaction vial; cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C15",
            "name": "[68Ga]Ga-DP3",
            "yield": "98.01 ± 0.97% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "14.09 ± 2.12 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluent: 1.5 mL ethanol; final product resolved in saline after ethanol removal",
          "notes": "Same radiolabeling procedure as [68Ga]Ga-DP1 except precursor is DP3. Radiochemical characteristics detailed in Table S1 (SI)."
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Radiolabeling of [18F]AlF-NP1",
      "target_compound_id": "C01",
      "target_compound_name": "[18F]AlF-NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "QMA cartridge trapping and elution of [18F]fluoride",
          "reactants": [
            {
              "compound_id": "C17",
              "name": "fluoride-18",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline (for cartridge preconditioning)",
              "volume": "10 mL"
            },
            {
              "name": "pure water (for cartridge preconditioning)",
              "volume": "10 mL"
            },
            {
              "name": "saline (for elution)",
              "volume": "0.2 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water; [18F]fluoride trapped on cartridge then eluted with 0.2 mL saline into reaction vial"
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride eluate in saline",
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
          "notes": "QMA cartridge used as a solid-phase ion-exchange trap for 18F concentration and solvent exchange."
        },
        {
          "step_number": 2,
          "reaction_type": "AlF complexation and NOTA chelation (18F radiolabeling)",
          "reactants": [
            {
              "compound_id": "C05",
              "name": "NP1 (precursor)",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "[18F]fluoride eluate in saline (from Step 1)",
              "amount": "0.2 mL",
              "role": "radionuclide_source"
            },
            {
              "name": "aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, pH 4.0)",
              "amount": "3 μL (2 mM, pH 4.0)",
              "role": "chelation_catalyst"
            },
            {
              "name": "sodium acetate buffer (0.1 M, pH 4.0)",
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
            "other": "precursor dissolved in 50 μL DMSO; all components added to reaction vial; cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C01",
            "name": "[18F]AlF-NP1",
            "yield": "62.58 ± 0.32% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "13.13 ± 1.71 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluent: 1.5 mL ethanol; ethanol removed; final product resolved in saline",
          "notes": "Reaction vial contents at time of heating: [18F]fluoride eluate (0.2 mL saline), AlCl3 solution (3 μL), acetonitrile (200 μL), sodium acetate buffer (100 μL, 0.1 M, pH 4.0), and NP1 precursor (50 μL DMSO). HPLC method for RCP analysis: 0.1% TFA in water (A) / 0.1% TFA in MeCN (B); 5% B to 95% B over 20 min, 1 mL/min. Radiochemical characteristics detailed in Table S1 (SI). n ≥ 3."
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Radiolabeling of [18F]AlF-NP2",
      "target_compound_id": "C16",
      "target_compound_name": "[18F]AlF-NP2",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "QMA cartridge trapping and elution of [18F]fluoride",
          "reactants": [
            {
              "compound_id": "C17",
              "name": "fluoride-18",
              "amount": "approximately 0.74–1.11 GBq"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "saline (for cartridge preconditioning)",
              "volume": "10 mL"
            },
            {
              "name": "pure water (for cartridge preconditioning)",
              "volume": "10 mL"
            },
            {
              "name": "saline (for elution)",
              "volume": "0.2 mL"
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "QMA cartridge preconditioned with 10 mL saline then 10 mL pure water; [18F]fluoride trapped on cartridge then eluted with 0.2 mL saline into reaction vial"
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride eluate in saline",
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
          "notes": "Identical to Step 1 of P6."
        },
        {
          "step_number": 2,
          "reaction_type": "AlF complexation and NOTA chelation (18F radiolabeling)",
          "reactants": [
            {
              "compound_id": "C08",
              "name": "NP2 (precursor)",
              "amount": "50 μg (18–25 nmol)"
            }
          ],
          "reagents": [
            {
              "name": "[18F]fluoride eluate in saline (from Step 1)",
              "amount": "0.2 mL",
              "role": "radionuclide_source"
            },
            {
              "name": "aluminum chloride (AlCl3) in sodium acetate buffer (2 mM, pH 4.0)",
              "amount": "3 μL (2 mM, pH 4.0)",
              "role": "chelation_catalyst"
            },
            {
              "name": "sodium acetate buffer (0.1 M, pH 4.0)",
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
            "other": "precursor dissolved in 50 μL DMSO; all components added to reaction vial; cooled to room temperature after heating"
          },
          "product": {
            "compound_id": "C16",
            "name": "[18F]AlF-NP2",
            "yield": "62.76 ± 0.22% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "13.42 ± 1.25 GBq/μmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluent: 1.5 mL ethanol; ethanol removed; final product resolved in saline",
          "notes": "Same radiolabeling procedure as [18F]AlF-NP1 except precursor is NP2. Radiochemical characteristics detailed in Table S1 (SI). n ≥ 3."
        }
      ]
    }
  ]
}
```


### Evaluation

##### v2.1 — 4 Claude Runs

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

##### v2.2 — 3 Claude Runs

**Prompt features added:** Explicit role decision tree, `method_completeness` enum, step granularity guidance (pH adjustment ≠ chelation), buffer deduplication rule.

| Failure                      | Pass rate  | Change vs v2.1                                                           |
| ---------------------------- | ---------- | ------------------------------------------------------------------------ |
| C1 — DP1/NP1 role            | 3/3 (100%) | Full resolution                                                          |
| C2 — External precursor role | 3/3 (100%) | Full resolution                                                          |
| C3 — Log P attribution       | 1/3 (33%)  | Regression: new phrasing caused log P to be copied via backbone matching |
| C4 — KD/Bmax attribution     | 1/3 (33%)  | Minor improvement but still majority failure                             |
| C5 — Docking scores          | 1/3 (33%)  | Now extracted; misattributed in two runs                                 |
| C6 — Buffer merge            | 2/3 (67%)  | Improved                                                                 |
| C7 — Step granularity        | 3/3 (100%) | Full resolution                                                          |

**Overall v2.2 Claude pass rate:** 14/18 tracked checks = **78%**

**Qualitative observations:**

- The role decision tree correctly used the in-house vs. vendor distinction that Section 5.1 and 5.2 make explicit. All three runs correctly identified DP1/NP1 as in-house (Section 5.2.1) and DP2/DP3/NP2 as external (Section 5.2.2).
- C7 was fully resolved. All runs correctly emitted separate pH adjustment and chelation steps, reflecting the "and then transferred" language in Section 5.4.
- C3 regression: The v2.2 prompt introduced log P attribution rules that some runs interpreted as applying to the "peptide backbone," leading them to record log P values on DP1 or NP1. The paper's Section 5.6 is unambiguous that only the five radiolabeled compounds were measured, but the prompt phrasing left room for backbone-transfer inference.
- C4 persisted: The binding assay section (2.4) lists KD values for the radiolabeled tracers by name, but v2.2 Claude still sometimes transferred KD to the precursors that share the same peptide sequence.
- C5 newly tracked: Docking scores appear in Section 2.3 and Figure 3B, attributed to PR7, DP1, DP2, DP3, NP1, NP2 — all unlabeled. Two runs incorrectly placed some of these on the corresponding radiolabeled products.

---

##### v2.3 — 3 Claude Runs

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

##### v2.4 — 3 Claude Runs

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

##### Aggregate Claude Performance

Pass Rates by Failure Mode Across Versions

| Failure               | v2.1 (n=4) | v2.2 (n=3) | v2.3 (n=3) | v2.4 (n=3) |
| --------------------- | ---------- | ---------- | ---------- | ---------- |
| C1 — DP1/NP1 role     | 50%        | 100%       | 100%       | 100%       |
| C2 — External role    | 75%        | 100%       | 100%       | 100%       |
| C3 — Log P            | 25%        | 33%        | 100%       | 100%       |
| C4 — KD/Bmax          | 0%         | 33%        | 67%        | 100%       |
| C5 — Docking scores   | N/A        | 33%        | 100%       | 100%       |
| C6 — Buffer merge     | 50%        | 67%        | 100%       | 100%       |
| C7 — Step granularity | 25%        | 100%       | 100%       | 100%       |
| **Overall**           | **38%**    | **78%**    | **95%**    | **100%**   |

