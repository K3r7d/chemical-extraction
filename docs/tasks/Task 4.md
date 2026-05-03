After Mahmoud give me a new SGLT paper, which have a longer contents. Now I will first check with my best prompt right now is 2.4

##### Claude_1 2.4 
```
{
  "extraction": {
    "prompt_version": "v2.4",
    "extraction_date": "2026-03-26",
    "model_name": "claude-sonnet-4-6",
    "extractor_notes": "This paper contains an extremely large compound library (>127 numbered final compounds plus hundreds of intermediates and building blocks). Full extraction of all compounds and pathways would require several thousand compound entries. This extraction covers: (1) all key lead/final compounds explicitly evaluated biologically (26–38, 46–51, 60–70, 94–102, 124–127), (2) major building block intermediates referenced in multiple pathways, (3) key reagents/alkylating agents (23a-d, 58). Many intermediate compounds (18a-h, 19a-h, 20a-p, 21a-w, 22a-q, 24a-x, 25a-g) are listed as a representative selection; full characterization of all 100+ intermediates is in SI (Tables S1-S7, S17). Mass spectrometry data in the experimental section employs nominal/observed m/z values from ESI-MS; monoisotopic masses are not explicitly calculated by the authors for most intermediates. The SI (Tables S1-S7) contains full structural and analytical data for all intermediates. Compound 64 is a prodrug (triacetylated) that is listed as a final_product since it is biologically evaluated; its deacetylated form is compound 101. Some HPLC purity values and LC-MS data were selectively reported in the paper."
  },

  "paper": {
    "title": "Design, Optimization, and Biological Evaluation of First-in-Class Triple Inhibitors of SGLT1, SGLT2, and DPP4 for Type 2 Diabetes Mellitus",
    "authors": [
      "Fernando de Souza Gama",
      "Marcos Ferreira",
      "Natanael Dante Segretti",
      "Mariana C. F. C. B. Damião",
      "Cristiano R. W. Guimarães",
      "Alessandra Mascarello",
      "Hatylas Azevedo"
    ],
    "doi": "10.1021/acs.jmedchem.5c02225",
    "journal": "Journal of Medicinal Chemistry",
    "year": 2025,
    "synthesis_scale": "lab",
    "mechanism_discussed": "synthetic",
    "method_completeness": "partial",
    "has_synthesis": true,
    "extraction_notes": "The main text contains full experimental procedures for all final products and key intermediates. Supporting Information (Tables S1-S7) contains structures of all intermediates relating to Scheme 1; Table S17 contains HPLC/LC-MS purity data. Biological IC50 data appear in Tables 1-6 (main text). Compounds 29 and 36 are noted as <95% purity and not critical to SAR. The paper does not report monoisotopic exact masses by calculation; MS data are given as observed m/z ions only. SGLT2/SGLT1 selectivity ratios are reported in Tables 1-6 for all final compounds."
  },

  "compounds": [
    {
      "id": "C01",
      "name": "canagliflozin (compound 1)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reference_compound",
      "is_newly_synthesized": false,
      "source": "commercial/literature",
      "physicochemical_properties": {
        "log_p": null,
        "other": "SGLT2/SGLT1 selectivity ratio ~250:1"
      },
      "description": "Marketed SGLT2 inhibitor used as a reference compound and comparator in biological studies."
    },
    {
      "id": "C02",
      "name": "dapagliflozin (compound 2)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reference_compound",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": "SGLT2/SGLT1 selectivity ratio ~1200:1; used as positive control in SGLT1/2 transport assays and PK comparator in all in vivo studies"
      },
      "description": "Marketed SGLT2-selective inhibitor (gliflozin) used as primary comparator in all in vitro and in vivo experiments throughout the study."
    },
    {
      "id": "C03",
      "name": "bexagliflozin (compound 3)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reference_compound",
      "is_newly_synthesized": false,
      "source": "literature",
      "physicochemical_properties": {
        "log_p": null,
        "other": "SGLT2/SGLT1 selectivity ratio ~2430:1"
      },
      "description": "Marketed SGLT2 inhibitor cited for SGLT2/SGLT1 selectivity reference."
    },
    {
      "id": "C04",
      "name": "empagliflozin (compound 4)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reference_compound",
      "is_newly_synthesized": false,
      "source": "literature",
      "physicochemical_properties": {
        "log_p": null,
        "other": "SGLT2/SGLT1 selectivity ratio ~2680:1"
      },
      "description": "Marketed SGLT2 inhibitor cited for selectivity reference and cardiovascular outcome trial context."
    },
    {
      "id": "C05",
      "name": "ertugliflozin (compound 5)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reference_compound",
      "is_newly_synthesized": false,
      "source": "literature",
      "physicochemical_properties": {
        "log_p": null,
        "other": "SGLT2/SGLT1 selectivity ratio ~2500:1; contains dioxabicyclo[3.2.1]octane ring system used as inspiration for compound 66"
      },
      "description": "Marketed SGLT2 inhibitor whose dioxabicyclo[3.2.1]octane sugar ring system inspired the design of analogue 66."
    },
    {
      "id": "C06",
      "name": "sotagliflozin (compound 6)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reference_compound",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": "SGLT2/SGLT1 selectivity ratio ~20:1; used as comparator in ZDF rat OGTT and ob/ob mouse studies"
      },
      "description": "Marketed dual SGLT1/2 inhibitor (sotagliflozin) used as comparator in in vivo glycemic control and GLP-1 studies."
    },
    {
      "id": "C07",
      "name": "licogliflozin (compound 7)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reference_compound",
      "is_newly_synthesized": false,
      "source": "literature",
      "physicochemical_properties": {
        "log_p": null,
        "other": "SGLT2/SGLT1 selectivity ratio ~40:1; contains core ethyl group adopted in present series"
      },
      "description": "Dual SGLT1/2 inhibitor providing the core ethyl substitution pattern adopted in the R1=Et series of this study."
    },
    {
      "id": "C08",
      "name": "HM41322 (compound 8)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reference_compound",
      "is_newly_synthesized": false,
      "source": "literature",
      "physicochemical_properties": {
        "log_p": null,
        "other": "SGLT2/SGLT1 selectivity ratio ~10:1; contains central indane moiety"
      },
      "description": "Dual SGLT1/2 inhibitor whose indane core motif inspired the design of analogue 102."
    },
    {
      "id": "C09",
      "name": "LX2761 (compound 9)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reference_compound",
      "is_newly_synthesized": false,
      "source": "literature",
      "physicochemical_properties": {
        "log_p": null,
        "other": "SGLT2/SGLT1 selectivity ratio ~1:1.2 (slight SGLT1 preference); cryo-EM structure bound to SGLT1 available (PDB: 7WMV)"
      },
      "description": "SGLT1-selective inhibitor whose cryo-EM structure guided linker design in this study."
    },
    {
      "id": "C10",
      "name": "mizagliflozin (compound 10)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reference_compound",
      "is_newly_synthesized": false,
      "source": "literature",
      "physicochemical_properties": {
        "log_p": null,
        "other": "SGLT1/SGLT2 selectivity ratio ~51:1 to ~300:1 (most SGLT1-selective); contains core isopropyl group"
      },
      "description": "Most SGLT1-selective inhibitor disclosed to date; its isopropyl core group inspired compound 100 in this study."
    },
    {
      "id": "C11",
      "name": "vildagliptin (compound 11)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reference_compound",
      "is_newly_synthesized": false,
      "source": "literature",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 inhibitor; known to inhibit DPP8 more potently than DPP4; contains 2-cyanopyrrolidine motif with pseudoirreversible covalent inhibition"
      },
      "description": "Marketed DPP4 inhibitor (gliptin) whose 2-cyanopyrrolidine motif was incorporated into the DPP4-targeting portion of the triple inhibitor series."
    },
    {
      "id": "C12",
      "name": "saxagliptin (compound 12)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reference_compound",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 inhibitor; contains fused cyclopropyl ring conferring reversible covalent inhibition; used as comparator in ZDF rat OGTT (1 mg/kg combined with dapagliflozin)"
      },
      "description": "Marketed DPP4 inhibitor (saxagliptin) used as comparator in combination with dapagliflozin in ZDF rat OGTT studies."
    },
    {
      "id": "C13",
      "name": "anagliptin (compound 13)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reference_compound",
      "is_newly_synthesized": false,
      "source": "literature",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 inhibitor; X-ray structure bound to human DPP4 available (PDB: 3WQH); elongated structure interacts with S2 extensive site"
      },
      "description": "DPP4 inhibitor whose crystal structure (PDB: 3WQH) guided linker design for triple inhibitors in this study."
    },
    {
      "id": "C14",
      "name": "prusogliptin (compound 14)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reference_compound",
      "is_newly_synthesized": false,
      "source": "literature",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Investigational DPP4 inhibitor; contains 4-fluorinated 2-cyanopyrrolidine"
      },
      "description": "Investigational DPP4 inhibitor whose 4-fluoro-2-cyanopyrrolidine motif informed fluorination strategy in this study."
    },
    {
      "id": "C15",
      "name": "melogliptin (compound 15)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reference_compound",
      "is_newly_synthesized": false,
      "source": "literature",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Investigational DPP4 inhibitor; contains 4-fluorinated 2-cyanopyrrolidine"
      },
      "description": "Investigational DPP4 inhibitor whose 4-fluoro-2-cyanopyrrolidine motif informed fluorination strategy in this study."
    },
    {
      "id": "C16",
      "name": "gosogliptin (compound 16)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reference_compound",
      "is_newly_synthesized": false,
      "source": "literature",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Clinical candidate DPP4 inhibitor; high oral bioavailability; contains 3,3-difluoropyrrolidine moiety; inspired compound 51 and difluoro series"
      },
      "description": "DPP4 clinical candidate whose difluoropyrrolidine moiety and 2,4-disubstituted pyrrolidine linker inspired compounds 51 and the difluoro variants."
    },
    {
      "id": "C17",
      "name": "teneligliptin (compound 17)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reference_compound",
      "is_newly_synthesized": false,
      "source": "literature",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Marketed DPP4 inhibitor; contains thiazolidine moiety and similar binding mode to anagliptin 13 at S2 extensive site"
      },
      "description": "Marketed DPP4 inhibitor (teneligliptin) whose thiazolidine moiety inspired alkylating agent 23c and analogue 46/60."
    },
    {
      "id": "C18",
      "name": "tetraacetyl dapagliflozin (compound 18a)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial or prepared from dapagliflozin",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Tetraacetyl-protected dapagliflozin derivative serving as the primary starting material for most compounds in the initial library (R1=Cl, R2=CH2OAc, R3=OAc, R4=H series)."
    },
    {
      "id": "C19",
      "name": "6-deoxy triacetyl chloro C-glycoside (compound 18b)",
      "iupac_name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{4-chloro-3-[(p-ethoxyphenyl)methyl]phenyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "LC-MS: purity 95.9%, m/z (ES) 541.0 (100%; [M(35Cl)+Na]+), 543.0 (40%; [M(37Cl)+Na]+)"
      },
      "description": "6-Deoxy C-glycoside intermediate with chloro core substituent, prepared from known dapagliflozin precursor 71; key building block for compounds 60-64, 97-98."
    },
    {
      "id": "C20",
      "name": "6-deoxy triacetyl ethyl C-glycoside (compound 18c)",
      "iupac_name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{4-ethyl-3-[(p-ethoxyphenyl)methyl]phenyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "LC-MS: m/z (ES) 535.1 ([M+Na]+); yield 80% by Suzuki-Miyaura from 18b"
      },
      "description": "6-Deoxy C-glycoside with ethyl core substituent, prepared by Suzuki-Miyaura coupling of 18b with NHC-borane 74; key building block for compounds 64, 99, 101, 124-127."
    },
    {
      "id": "C21",
      "name": "triacetyl sotagliflozin (compound 18d)",
      "iupac_name": "(2R,3S,4R,5S,6S)-4,5-Diacetoxy-6-{4-chloro-3-[(p-hydroxyphenyl)methyl]phenyl}-2-(methylthio)tetrahydro-2H-pyran-3-yl Acetate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house (prepared by acetylation of sotagliflozin 6)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Yield 99% by acetylation of compound 6 with Ac2O/pyridine/DMAP"
      },
      "description": "Triacetyl sotagliflozin, prepared by direct acetylation of sotagliflozin; key intermediate for sotagliflozin analogues 67 and 68."
    },
    {
      "id": "C22",
      "name": "4-fluoro 6-deoxy C-glycoside 18e",
      "iupac_name": "(2S,3S,4R,5R,6R)-4-Acetoxy-2-{4-chloro-3-[(p-ethoxyphenyl)methyl]phenyl}-5-fluoro-6-methyltetrahydro-2H-pyran-3-yl Acetate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "19F NMR (CDCl3): -197.0; overall yield 38% over four steps from 92"
      },
      "description": "4-Fluoro 6-deoxy C-glucoside intermediate prepared from benzyl-protected precursor 92 via triflation and TBAF-mediated fluorination with inversion at C4; key building block for compound 69."
    },
    {
      "id": "C23",
      "name": "4,4-difluoro 6-deoxy C-glycoside 18f",
      "iupac_name": "(2S,3S,4R,6R)-4-Acetoxy-2-{4-chloro-3-[(p-ethoxyphenyl)methyl]phenyl}-5,5-difluoro-6-methyltetrahydro-2H-pyran-3-yl Acetate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "19F NMR (CDCl3): -118.0 (d, J=249), -133.8 (d, J=249); overall yield 41% over three steps from 93"
      },
      "description": "4,4-Difluoro 6-deoxy C-glucoside prepared by oxidation of 92 to ketone 93 followed by BAST fluorination; key building block for compound 70."
    },
    {
      "id": "C24",
      "name": "6-methyl triacetyl C-glycoside 18g",
      "iupac_name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{3-[(p-ethoxyphenyl)methyl]-4-tolyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Yield 94% (acetylation step); prepared following Meng route to dapagliflozin from 5-bromo-2-methylbenzoic acid 103"
      },
      "description": "Methyl-core 6-deoxy C-glycoside, prepared via a 9-step sequence from 5-bromo-2-methylbenzoic acid (103) analogous to the dapagliflozin synthesis; key building block for compound 99."
    },
    {
      "id": "C25",
      "name": "isopropyl triacetyl C-glycoside 18h",
      "iupac_name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{3-[(p-ethoxyphenyl)methyl]-4-cumenyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "LC-MS: purity 85.5%, m/z (ES) 549.25 ([M+Na]+); prepared in 3 steps from 18b via Suzuki-Molander coupling then hydrogenation"
      },
      "description": "Isopropyl-core 6-deoxy C-glycoside prepared from 18b via Suzuki-Molander coupling with potassium isopropenyltrifluoroborate (27% yield) followed by hydrogenation; building block for compound 100."
    },
    {
      "id": "C26",
      "name": "phenol intermediate 19a",
      "iupac_name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-{4-chloro-3-[(p-hydroxyphenyl)methyl]phenyl}tetrahydro-2H-pyran-2-yl]methyl Acetate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house (BBr3 dealkylation of 18a)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC purity 97.0%; LC-MS purity 90.6%, m/z (ES) 566.2 (100%; [M(35Cl)+H2O]+), 568.2 (35%; [M(37Cl)+H2O]+); yield 8.80 g (93%) from 18a (9.90 g, 17.2 mmol)"
      },
      "description": "Free phenol intermediate obtained by BBr3-mediated demethylation of tetraacetyl dapagliflozin (18a); primary substrate for Mitsunobu and nucleophilic coupling reactions in the initial library."
    },
    {
      "id": "C27",
      "name": "phenol intermediate 19b",
      "iupac_name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{4-chloro-3-[(p-hydroxyphenyl)methyl]phenyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house (BBr3 dealkylation of 18b)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Yield 2.20 g (93%) from 18b (2.50 g, 4.82 mmol); white solid"
      },
      "description": "6-Deoxy free phenol intermediate from BBr3 dealkylation of 18b; primary substrate for 6-deoxy series final compounds 60-63, 97-98."
    },
    {
      "id": "C28",
      "name": "phenol intermediate 19c",
      "iupac_name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{4-ethyl-3-[(p-hydroxyphenyl)methyl]phenyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house (BBr3 dealkylation of 18c)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Yield 6.00 g (67%) from 18c (9.50 g, 18.5 mmol); white solid"
      },
      "description": "6-Deoxy ethyl-core free phenol intermediate from BBr3 dealkylation of 18c; substrate for ethyl-core series final compounds 64, 94, 95, 99, 101, 124-127."
    },
    {
      "id": "C29",
      "name": "phenol intermediate 19d",
      "iupac_name": "(2R,3S,4R,5S,6S)-4,5-Diacetoxy-6-{4-chloro-3-[(p-hydroxyphenyl)methyl]phenyl}-2-(methylthio)tetrahydro-2H-pyran-3-yl Acetate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house (BBr3 dealkylation of 18d)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Yield 0.89 g (72%) from 18d; white solid; used without further purification"
      },
      "description": "Sotagliflozin-derived free phenol intermediate; substrate for sotagliflozin analogues 67 and 68."
    },
    {
      "id": "C30",
      "name": "4-fluoro phenol intermediate 19e",
      "iupac_name": "(2S,3S,4R,5R,6R)-4-Acetoxy-2-{4-chloro-3-[(p-hydroxyphenyl)methyl]phenyl}-5-fluoro-6-methyltetrahydro-2H-pyran-3-yl Acetate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house (BBr3 dealkylation of 18e)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Yield 1.70 g (95%) from 18e (1.90 g, 3.97 mmol); 19F NMR (CDCl3): -197.0"
      },
      "description": "4-Fluoro 6-deoxy free phenol intermediate; substrate for compound 69."
    },
    {
      "id": "C31",
      "name": "4,4-difluoro phenol intermediate 19f",
      "iupac_name": "(2S,3S,4R,6R)-4-Acetoxy-2-{4-chloro-3-[(p-hydroxyphenyl)methyl]phenyl}-5,5-difluoro-6-methyltetrahydro-2H-pyran-3-yl Acetate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house (BBr3 dealkylation of 18f)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Yield 1.20 g (75%) from 18f (1.70 g, 3.42 mmol); 19F NMR (CDCl3): -118.0 (d, J=249), -133.8 (d, J=249)"
      },
      "description": "4,4-Difluoro 6-deoxy free phenol intermediate; substrate for compound 70."
    },
    {
      "id": "C32",
      "name": "methyl-core phenol intermediate 19g",
      "iupac_name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{3-[(p-hydroxyphenyl)methyl]-4-tolyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house (BBr3 dealkylation of 18g)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Yield 1.40 g (87%) from 18g (1.70 g, 3.32 mmol)"
      },
      "description": "Methyl-core 6-deoxy free phenol intermediate; substrate for compound 99."
    },
    {
      "id": "C33",
      "name": "isopropyl-core phenol intermediate 19h",
      "iupac_name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{3-[(p-hydroxyphenyl)methyl]-4-cumenyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house (BBr3 dealkylation of 18h)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Crude yield 0.40 g (94%) from 18h (0.45 g, 0.85 mmol); used without further purification"
      },
      "description": "Isopropyl-core 6-deoxy free phenol intermediate; substrate for compound 100."
    },
    {
      "id": "C34",
      "name": "gem-dimethyl C4 linker alcohol 20b",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Commercially available Boc-protected gem-dimethyl 4-aminobutanol linker precursor; used extensively in Mitsunobu couplings to install the gem-dimethyl C4 linker (priority linker identified from SAR)."
    },
    {
      "id": "C35",
      "name": "chloroacetyl-(S)-2-cyanopyrrolidine 23a",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Y=CH2, R5=CN, R6=H; N-alkylating agent for unmodified 2-cyanopyrrolidine DPP4 pharmacophore"
      },
      "description": "Chloroacetyl-(S)-2-cyanopyrrolidine N-alkylating agent used to install the DPP4-targeting 2-cyanopyrrolidine moiety in route 1 and route 2 sequences (compounds 26-34)."
    },
    {
      "id": "C36",
      "name": "chloroacetyl-(2S,4S)-4-fluoro-2-cyanopyrrolidine 23b",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Y=(S)-CHF, R5=CN, R6=H; N-alkylating agent for 4-fluoro-2-cyanopyrrolidine DPP4 pharmacophore"
      },
      "description": "N-Alkylating agent for the 4-fluorinated 2-cyanopyrrolidine DPP4 pharmacophore; used to synthesize compounds 35, 37, 38, 47, 49, 63, 97, 98, 125, 126."
    },
    {
      "id": "C37",
      "name": "chloroacetyl-(S)-4-cyano-thiazolidine 23c",
      "iupac_name": "(S)-3-(2-Chloroacetyl)-1,3-thiazolidine-4-carbonitrile",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Y=S, R5=H, R6=CN; yield 60% over 3 steps from Boc-D-thiazolidine-4-carboxylic acid 52; LC-MS: purity 90.8%, m/z 185.1 (100%; [M(35Cl)+H]+), 187.1 (30%)"
      },
      "description": "N-Alkylating agent for the thiazolidine-4-carbonitrile DPP4 pharmacophore (teneligliptin-inspired); used for compounds 46 and 60."
    },
    {
      "id": "C38",
      "name": "chloroacetyl-(S)-4,4-difluoro-2-cyanopyrrolidine 23d",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Y=CF2, R5=CN, R6=H; 4,4-difluorinated pyrrolidine inspired by gosogliptin 16"
      },
      "description": "Commercially sourced N-alkylating agent for the 4,4-difluoro-2-cyanopyrrolidine DPP4 pharmacophore; used for lead compounds 61, 64, 65, 66, 68, 94, 95, 99-102, 127."
    },
    {
      "id": "C39",
      "name": "chloroacetyl-(1S,3S,5S)-3-cyano-2-azabicyclo[3.1.0]hexane 58",
      "iupac_name": "[(1S,3S,5S)-3-Cyano-2-azabicyclo[3.1.0]hex-2-yl]acetyl Chloride",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Yield 76% from 57; saxagliptin-inspired fused cyclopropyl DPP4 pharmacophore; LC-MS purity 90.8%, m/z 185.1"
      },
      "description": "N-Alkylating agent for saxagliptin-inspired fused bicyclic DPP4 pharmacophore; prepared in 2 steps from commercially available Boc-azabicyclo[3.1.0]hexane-3-carbonitrile 56; used for compound 48 and 62."
    },
    {
      "id": "C40",
      "name": "L-hydroxyproline (compound 39)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Commercially available L-hydroxyproline used as starting material for Scheme 2 synthesis of compound 36 (gosogliptin-type linker analogue)."
    },
    {
      "id": "C41",
      "name": "Boc-hydroxyproline 40",
      "iupac_name": "(2S,4R)-1-tert-Butoxycarbonyl-4-hydroxy-2-pyrrolidinecarboxylic Acid",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Yield 1.60 g (45%) from L-hydroxyproline (2.00 g, 15.3 mmol); LC-MS purity 100%, m/z 230.1 ([M-H]-)"
      },
      "description": "Boc-protected hydroxyproline prepared by standard Boc protection of L-hydroxyproline 39 for use in Scheme 2 (compound 36) and Scheme 4 (compound 51)."
    },
    {
      "id": "C42",
      "name": "compound 26 (C2 linker triple inhibitor)",
      "iupac_name": "(S)-1-(2-{3-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylpropylamino}acetyl)-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 0.049 ± 0.008 μM; SGLT1 IC50 = 2.95 ± 2.18 μM; SGLT2 IC50 = 0.018 ± 0.006 μM; SGLT2/1 ratio = 160; LC-MS purity 99.0%, m/z 602.3 (100%; [M(35Cl)-H]-)"
      },
      "description": "First library compound with C2 gem-dimethyl linker; compromised SGLT1 potency (IC50 2.95 μM) relative to longer linker analogues."
    },
    {
      "id": "C43",
      "name": "compound 27 (gem-dimethyl C4 triple inhibitor)",
      "iupac_name": "(S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 0.016 ± 0.004 μM; SGLT1 IC50 = 0.687 ± 0.506 μM; SGLT2 IC50 = 0.0018 ± 0.0020 μM; SGLT2/1 ratio = 377; LC-MS purity 100%, m/z 616.2 (100%; [M(35Cl)+H]+); prioritized for further development based on balanced potency and in vivo PK; IV PK in fasted CD-1 mice (1 mg/kg): higher clearance than dapagliflozin; UGE ~50% of dapagliflozin over 24h in fed ICR mice"
      },
      "description": "Priority linker compound with gem-dimethyl C4 linker identified as the optimal linker from initial library screening; advanced to in vivo PK and UGE studies in mice."
    },
    {
      "id": "C44",
      "name": "compound 28 (C2 ethylene linker)",
      "iupac_name": "(S)-1-(2-{2-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]ethylamino}acetyl)-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 0.165 ± 0.032 μM; SGLT1 IC50 = 0.768 ± 0.267 μM; SGLT2 IC50 = 0.0044 ± 0.0025 μM; SGLT2/1 ratio = 177; LC-MS purity 95.9%, m/z 560.3"
      },
      "description": "C2 ethylene linker analogue; C3 linker series showed compromised DPP4 potency."
    },
    {
      "id": "C45",
      "name": "compound 29 (C3 linker)",
      "iupac_name": "(S)-1-(2-{3-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]propylamino}acetyl)-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 0.137 ± 0.043 μM; SGLT1 IC50 = 0.799 ± 0.336 μM; SGLT2 IC50 = 0.0026 ± 0.0021 μM; SGLT2/1 ratio = 302; LC-MS purity 94.6%, m/z 574.2; NOTE: <95% purity by HPLC, not critical to SAR"
      },
      "description": "C3 linker analogue; compromised DPP4 potency compared to C4 linker 27."
    },
    {
      "id": "C46",
      "name": "compound 30 (C4 linker)",
      "iupac_name": "(S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]butylamino}acetyl)-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 0.114 ± 0.066 μM; SGLT1 IC50 = 0.283 ± 0.101 μM; SGLT2 IC50 = 0.0027 ± 0.0030 μM; SGLT2/1 ratio = 105; HPLC purity 98.6%; LC-MS purity 96.9%, m/z 588.2; chemical stability concern at pH 7.5; unstable in mouse plasma"
      },
      "description": "Unsubstituted C4 linker analogue; good SGLT1 potency but stability concerns in phosphate buffer pH 7.5 and mouse plasma."
    },
    {
      "id": "C47",
      "name": "compound 32 (trans-1,3-cyclopentyl linker)",
      "iupac_name": "(S)-1-{2-[(1S,3S)-3-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclopentylamino]acetyl}-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 0.011 ± 0.003 μM; SGLT1 IC50 = 0.882 ± 0.410 μM; SGLT2 IC50 = 0.0026 ± 0.0011 μM; SGLT2/1 ratio = 428; LC-MS purity 98.9%, m/z 600.2; backup linker; IV PK in fed ICR mice showed comparable UGE to compound 27"
      },
      "description": "Trans-1,3-cyclopentyl linker analogue; excellent DPP4/SGLT2 potency but weaker SGLT1 activity; identified as backup linker after compound 27."
    },
    {
      "id": "C48",
      "name": "compound 33 (3-cyclohexyl linker)",
      "iupac_name": "(S)-1-(2-{3-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclohexylamino}acetyl)-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 0.030 ± 0.004 μM; SGLT1 IC50 = 2.31 ± 1.44 μM; SGLT2 IC50 = 0.0088 ± 0.0068 μM; SGLT2/1 ratio = 262; HPLC purity 99.6%; LC-MS purity 99.3%, m/z 614.2"
      },
      "description": "3-Cyclohexyl linker analogue with weaker SGLT1 activity."
    },
    {
      "id": "C49",
      "name": "compound 34 (4-cyclohexyl linker)",
      "iupac_name": "(S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclohexylamino}acetyl)-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 0.028 ± 0.010 μM; SGLT1 IC50 = 1.17 ± 0.46 μM; SGLT2 IC50 = 0.0032 ± 0.0017 μM; SGLT2/1 ratio = 365; HPLC purity 99.6%; LC-MS purity 100.0%, m/z 614.2; chemical stability concern at pH 7.5"
      },
      "description": "4-Cyclohexyl linker analogue; next-best SGLT1 inhibitor after linker 27 in initial screen, selected for in vivo PK study."
    },
    {
      "id": "C50",
      "name": "compound 35 (pyrrolidinyloxy linker, monofluoro)",
      "iupac_name": "(2S,4S)-1-(2-{3-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1-pyrrolidinyl}acetyl)-4-fluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 11.2 ± 0.15 μM; SGLT1 IC50 = 2.41 ± 0.75 μM; SGLT2 IC50 = 0.0074 ± 0.0033 μM; SGLT2/1 ratio = 323; LC-MS purity 99.8%, m/z 604.4; loss of DPP4 activity due to F in wrong linker position"
      },
      "description": "Pyrrolidinyloxy linker analogue with 4-fluoro DPP4 pharmacophore; essentially inactive against DPP4 (IC50 11.2 μM)."
    },
    {
      "id": "C51",
      "name": "compound 36 (gosogliptin-type linker)",
      "iupac_name": "(S)-1-{[(2S,4S)-4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-2-pyrrolidinyl]carbonyl}-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house (Scheme 2)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 20.0 ± 5.39 μM; SGLT1 IC50 = 0.646 ± 0.273 μM; SGLT2 IC50 = 0.0046 ± 0.0017 μM; SGLT2/1 ratio = 141; HPLC purity 92.0%; LC-MS purity 88.9%, m/z 572.2; NOTE: <95% purity, not critical to SAR; inactive against DPP4"
      },
      "description": "Gosogliptin-type 2,4-disubstituted pyrrolidine linker analogue; good SGLT1 activity but inactive against DPP4 (IC50 20 μM); prepared via divergent Scheme 2 route."
    },
    {
      "id": "C52",
      "name": "compound 37 (bicyclo[2.2.2]octyl linker)",
      "iupac_name": "(2S,4S)-1-(2-{5-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]bicyclo[2.2.2]oct-2-ylamino}acetyl)-4-fluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 0.0135 ± 0.0009 μM; SGLT1 IC50 = 1.64 ± 0.01 μM; SGLT2 IC50 = 0.0016 ± 0.0009 μM; SGLT2/1 ratio = 101; LC-MS purity 99.2%, m/z 658.3"
      },
      "description": "Adamantane-skeleton-inspired bicyclo[2.2.2]octyl linker analogue; good DPP4/SGLT2 but moderate SGLT1 potency."
    },
    {
      "id": "C53",
      "name": "compound 38 (1-methylcyclohexyl linker)",
      "iupac_name": "(2S,4S)-1-{2-[(1R,4R)-4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1-methylcyclohexylamino]acetyl}-4-fluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 0.0064 ± 0.0013 μM; SGLT1 IC50 = 1.610 ± 0.002 μM; SGLT2 IC50 = 0.0087 ± 0.0030 μM; SGLT2/1 ratio = 186; LC-MS purity 100.0%, m/z 646.3"
      },
      "description": "1-Methylcyclohexyl linker analogue (analogous to gem-dimethyl substitution); good DPP4/SGLT2 but moderate SGLT1 potency."
    },
    {
      "id": "C54",
      "name": "compound 46 (thiazolidine DPP4 pharmacophore)",
      "iupac_name": "(S)-3-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-1,3-thiazolidine-4-carbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 0.020 ± 0.004 μM; SGLT1 IC50 = 1.66 ± 2.18 μM; SGLT2 IC50 = 0.0049 ± 0.0067 μM; SGLT2/1 ratio = 337; HPLC purity 100.0%; LC-MS purity 100.0%, m/z 634.2; thiazolidine moiety detrimental to SGLT1 potency"
      },
      "description": "Thiazolidine DPP4 pharmacophore analogue of compound 27; detrimental effect on SGLT1 inhibition (IC50 1.66 vs 0.69 μM for parent 27)."
    },
    {
      "id": "C55",
      "name": "compound 47 (4-fluoro 2-cyanopyrrolidine, gem-dimethyl C4 linker)",
      "iupac_name": "(2S,4S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4-fluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 0.0057 ± 0.0004 μM; SGLT1 IC50 = 0.687 ± 0.316 μM; SGLT2 IC50 = 0.0016 ± 0.0026 μM; SGLT2/1 ratio = 432; HPLC purity 100.0%; LC-MS purity 99.0%, m/z 634.2; 4-fluorination marginally improved SGLT2/DPP4 without adversely affecting SGLT1"
      },
      "description": "4-Fluoro-2-cyanopyrrolidine analogue of compound 27; improved DPP4/SGLT2 potency without compromising SGLT1."
    },
    {
      "id": "C56",
      "name": "compound 48 (fused cyclopropyl DPP4 pharmacophore)",
      "iupac_name": "(1S,3S,5S)-2-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-2-azabicyclo[3.1.0]hexane-3-carbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 0.114 ± 0.029 μM; SGLT1 IC50 = 0.846 ± 0.489 μM; SGLT2 IC50 = 0.0024 ± 0.0032 μM; SGLT2/1 ratio = 347; HPLC purity 100.0%; LC-MS purity 99.6%, m/z 628.2; fused cyclopropyl ring compromised DPP4 potency ~10-fold"
      },
      "description": "Saxagliptin-inspired fused cyclopropyl DPP4 pharmacophore analogue; 10-fold loss of DPP4 potency compared to parent compound 27."
    },
    {
      "id": "C57",
      "name": "compound 49 (4-fluoro 2-cyanopyrrolidine, cyclopentyl linker)",
      "iupac_name": "(2S,4S)-1-{2-[(1S,3R)-3-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclopentylamino]acetyl}-4-fluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 0.0046 ± 0.0006 μM; SGLT1 IC50 = 0.595 ± 0.123 μM; SGLT2 IC50 = 0.0013 ± 0.0009 μM; SGLT2/1 ratio = 461; HPLC purity 99.7%; LC-MS purity 100.0%, m/z 618.2"
      },
      "description": "4-Fluoro-2-cyanopyrrolidine with trans-1,3-cyclopentyl linker; IC50 4.6 nM for SGLT2, improved over parent 32."
    },
    {
      "id": "C58",
      "name": "compound 50 (4,4-difluoro 2-cyanopyrrolidine, cyclopentyl linker)",
      "iupac_name": "(S)-1-{2-[(1S,3R)-3-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclopentylamino]acetyl}-4,4-difluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 0.016 ± 0.004 μM; SGLT1 IC50 = 1.07 ± 0.24 μM; SGLT2 IC50 = 0.0039 ± 0.0010 μM; SGLT2/1 ratio = 314; HPLC purity 95.4%; LC-MS purity 97.1%, m/z 634.0 ([M(35Cl)-H]-); difluorination beneficial for SGLT2/1 selectivity"
      },
      "description": "4,4-Difluoro-2-cyanopyrrolidine (gosogliptin-inspired) with trans-1,3-cyclopentyl linker; IC50 1.6 nM for SGLT2, best SGLT2 potency in DPP4 ligand variation series."
    },
    {
      "id": "C59",
      "name": "compound 51 (difluoropyrrolidine, gosogliptin-type linker)",
      "iupac_name": "[(2S,4R)-4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-2-pyrrolidinyl](3,3-difluoro-1-pyrrolidinyl)methanone",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house (Scheme 4)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 2.24 ± 1.12 μM; SGLT1 IC50 = 2.63 ± 0.05 μM; SGLT2 IC50 = 0.075 ± 0.015 μM; SGLT2/1 ratio = 35; HPLC purity 99.9%; LC-MS purity 99.6%, m/z 583.2; gosogliptin-inspired linker not explored further"
      },
      "description": "Difluoropyrrolidine amide analogue with gosogliptin-type 2,4-disubstituted pyrrolidine linker; improved DPP4 vs parent 36 but 4-fold weaker SGLT1; gosogliptin linker not pursued further."
    },
    {
      "id": "C60",
      "name": "compound 60 (6-deoxy, thiazolidine, first 6-deoxy lead)",
      "iupac_name": "(S)-3-(2-{4-[p-({2-Chloro-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-1,3-thiazolidine-4-carbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 32 ± 11 nM; SGLT1 IC50 = 110 ± 131 nM; SGLT2 IC50 = 1.0 ± 0.6 nM; SGLT2/1 ratio = 110; LC-MS purity 100.0%, m/z 618.3; rat IV PK (1 mg/kg): <10% plasma exposure vs dapagliflozin; UGE: 101 mg over 24h IV, 380 mg over 24h oral (10 mg/kg); OGTT in Sprague-Dawley rats: comparable antihyperglycemic to dapagliflozin at 50 mg/kg oral"
      },
      "description": "First 6-deoxy analogue with thiazolidine DPP4 pharmacophore; demonstrated proof-of-concept for glycemic control in rat OGTT despite low plasma exposure, suggesting kidney accumulation-driven efficacy."
    },
    {
      "id": "C61",
      "name": "compound 61 (6-deoxy, 4,4-difluoro, gem-dimethyl C4 — platform compound)",
      "iupac_name": "(S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 38 ± 16 nM; SGLT1 IC50 = 67 ± 45 nM; SGLT2 IC50 = 1.3 ± 1.0 nM; SGLT2/1 ratio = 52; LC-MS purity 98.1%, m/z 636.3; rat oral (10 mg/kg) UGE 1030 mg vs 3370 mg for dapagliflozin; ZDF rat OGTT: significantly superior plasma glucose vs dapagliflozin at 1h (p=0.0186) and 1.5h (p=0.0122); significantly elevated aGLP-1 vs dapagliflozin (p<0.0001); DPP4 vs DPP8 selectivity: 20-fold; DPP4 vs DPP9 selectivity: 6.0-fold; no DPP3 inhibition up to 10 μM; no GLUT1/GLUT4 inhibition up to 10 μM"
      },
      "description": "Platform compound; 6-deoxy modification with 4,4-difluoro-2-cyanopyrrolidine DPP4 pharmacophore; advanced to ZDF rat OGTT showing superior glycemic control and elevated aGLP-1 vs dapagliflozin; preferred over monofluorinated 63 for balanced properties."
    },
    {
      "id": "C62",
      "name": "compound 62 (fused cyclopropyl, 6-deoxy)",
      "iupac_name": "(1S,3S,5S)-2-(2-{4-[p-({2-Chloro-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-2-azabicyclo[3.1.0]hexane-3-carbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 596 ± 268 nM; SGLT1 IC50 = 56 ± 23 nM; SGLT2 IC50 = 1.2 ± 0.3 nM; SGLT2/1 ratio = 46; LC-MS purity 100.0%, m/z 612.3; ruled out due to 5-fold loss in DPP4 potency vs parent 48; >50% CYP2C9 inhibition at 10 μM"
      },
      "description": "Fused cyclopropyl DPP4 pharmacophore with 6-deoxy sugar; excluded from further development due to compromised DPP4 potency and CYP2C9 inhibition."
    },
    {
      "id": "C63",
      "name": "compound 63 (6-deoxy, 4-fluoro, gem-dimethyl C4)",
      "iupac_name": "(2S,4S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4-fluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 13 ± 4 nM; SGLT1 IC50 = 158 ± 285 nM; SGLT2 IC50 = 1.0 ± 0.6 nM; SGLT2/1 ratio = 158; LC-MS purity 97.2%, m/z 618.3; >50% CYP2C9 inhibition at 10 μM; rat oral UGE lower than 61"
      },
      "description": "Monofluorinated 6-deoxy analogue; very potent DPP4 inhibitor (13 nM) but higher SGLT2/1 ratio than difluorinated 61; CYP2C9 concern; 4,4-difluorination preferred for best balance."
    },
    {
      "id": "C64",
      "name": "compound 64 (prodrug, triacetylated, ethyl core)",
      "iupac_name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-(3-{[p-(4-{2-[(S)-2-cyano-4,4-difluoro-1-pyrrolidinyl]-2-oxoethylamino}-4-methylpentyloxy)phenyl]methyl}-4-ethylphenyl)-2-methyltetrahydro-2H-pyran-3-yl Acetate",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 356 ± 92 nM (triacetylated form); SGLT1 IC50 = 1290 ± 300 nM; SGLT2 IC50 = 170 ± 56 nM; SGLT2/1 ratio = 7.6; LC-MS purity 99.4%, m/z 756.3 ([M+H]+); prodrug strategy: short half-life in microsomes (≤5.5 min) reflecting rapid deacetylation in vivo; oral (10 mg/kg) in rats: UGE 2160 mg/24h vs 3370 mg for dapagliflozin; ZDF rat OGTT (30 mg/kg): significantly superior plasma glucose AUC0-3h vs dapagliflozin (p=0.0328); significantly elevated aGLP-1 vs both dapagliflozin and sotagliflozin; head-to-head vs 101 in fed ICR mice: significantly higher UGE (p=0.04); THREE development candidates (64, 99, 101) under further evaluation including IND-enabling toxicology"
      },
      "description": "Lead compound 64; triacetylated prodrug of compound 101 (R1=Et) left protected to improve bioavailability; demonstrates triple DPP4/SGLT1/SGLT2 inhibition in vivo after deacetylation; one of three clinical development candidates."
    },
    {
      "id": "C65",
      "name": "compound 65 (spiro-cyclopropyl C5, ethyl core)",
      "iupac_name": "(S)-1-(2-{4-[p-({2-Ethyl-5-[(5S,6R,7R,8S)-6,7,8-trihydroxy-4-oxa-5-spiro[2.5]octyl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house (Scheme 6)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 62 ± 52 nM; SGLT1 IC50 = 20 ± 5 nM; SGLT2 IC50 = 1.8 ± 1.1 nM; SGLT2/1 ratio = 11; LC-MS purity 98.1%, m/z 642.3; rat plasma instability concern; oral UGE very low for unclear reasons"
      },
      "description": "Spiro-cyclopropyl C5 modification of the ethyl-core analogue; potent dual SGLT1/2 inhibitor (SGLT2/1 ratio ~11) but rat plasma instability and unexpectedly poor oral UGE."
    },
    {
      "id": "C66",
      "name": "compound 66 (ertugliflozin-type bicyclic sugar, ethyl core)",
      "iupac_name": "(S)-1-(2-{4-[p-({2-Ethyl-5-[(1S,2S,3S,4R,5S)-2,3,4-trihydroxy-1-methyl-6,8-dioxabicyclo[3.2.1]oct-5-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house (Schemes S3, 7)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 40 ± 15 nM; SGLT1 IC50 = 8.6 ± 5.6 nM; SGLT2 IC50 = 1.0 ± 0.6 nM; SGLT2/1 ratio = 8.6; LC-MS purity 97.1%, m/z 658.3; most potent SGLT1 inhibitor (8.6 nM IC50); rat oral UGE 1440 mg/24h; no metabolic stability issues"
      },
      "description": "Ertugliflozin-type bicyclic sugar (C1-deoxy dioxabicyclo[3.2.1]octane) with ethyl core; most potent SGLT1 inhibitor in the series (IC50 8.6 nM); prepared via complex 10-step route (Schemes S3 and 7)."
    },
    {
      "id": "C67",
      "name": "compound 67 (sotagliflozin sugar, 4-fluoro DPP4)",
      "iupac_name": "(2S,4S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(methylthio)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4-fluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 20 ± 3 nM; SGLT1 IC50 = 18 ± 1 nM; SGLT2 IC50 = 0.5 ± 0.2 nM; SGLT2/1 ratio = 36; LC-MS purity 95.4%, m/z 650.2"
      },
      "description": "Sotagliflozin-inspired analogue (6-methylthio sugar) with 4-fluoro-2-cyanopyrrolidine; potent across all three targets but higher SGLT2 selectivity (36:1) than ethyl-core series."
    },
    {
      "id": "C68",
      "name": "compound 68 (sotagliflozin sugar, 4,4-difluoro DPP4)",
      "iupac_name": "5-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(methylthio)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-2-{2-[(S)-2-cyano-4,4-difluoro-1-pyrrolidinyl]-2-oxoethylammonio}-2-methylpentane Chloride",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 49 ± 14 nM; SGLT1 IC50 = 37 ± 25 nM; SGLT2 IC50 = 0.4 ± 0.2 nM; SGLT2/1 ratio = 84; LC-MS purity 99.2%, m/z 668.3; lower rat/human plasma and microsomal stability; not pursued further due to low oral bioavailability (undetectable in plasma after oral dosing)"
      },
      "description": "Sotagliflozin sugar with 4,4-difluoro DPP4 pharmacophore; very potent across targets but poor oral bioavailability in rats."
    },
    {
      "id": "C69",
      "name": "compound 69 (4-fluoro glucoside, monofluoro DPP4)",
      "iupac_name": "(2S,4S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-5-fluoro-3,4-dihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4-fluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 17 ± 8 nM; SGLT1 IC50 = not determined; SGLT2 IC50 = 21 ± 9 nM; SGLT2/1 ratio = not determined; LC-MS purity 99.2%, m/z 620.3; increased SGLT2 IC50 (21 nM vs 1.0 nM for 63); not pursued further"
      },
      "description": "C4-fluorinated glucoside analogue; increased SGLT2 IC50 (21 nM vs 1.0 nM for parent 63); not of further interest."
    },
    {
      "id": "C70",
      "name": "compound 70 (4,4-difluoro glucoside, monofluoro DPP4)",
      "iupac_name": "(2S,4S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,6R)-5,5-difluoro-3,4-dihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4-fluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 31 ± 16 nM; SGLT1 IC50 = not determined; SGLT2 IC50 = 88 ± 34 nM; SGLT2/1 ratio = not determined; LC-MS purity 99.7%, m/z 638.3; increased SGLT2 IC50 (88 nM); not pursued further"
      },
      "description": "C4,4-difluorinated glucoside analogue; markedly increased SGLT2 IC50 (88 nM); not of further interest."
    },
    {
      "id": "C71",
      "name": "compound 94 (spiro-cyclopropyl linker, ethyl core)",
      "iupac_name": "(S)-1-[2-(1-{3-[p-({2-Ethyl-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]propyl}cyclopropylamino)acetyl]-4,4-difluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 636 ± 188 nM; SGLT1 IC50 = 6.4 ± 0.7 nM; SGLT2 IC50 = 0.7 ± 0.1 nM; SGLT2/1 ratio = 9.8; LC-MS purity 95.9%, m/z 628.4; too much DPP4 activity lost vs required"
      },
      "description": "Spiro-cyclopropyl linker analogue in ethyl core series; excellent SGLT1/2 potency but compromised DPP4 activity (636 nM); not advanced."
    },
    {
      "id": "C72",
      "name": "compound 95 (spiro-cyclopentyl linker, ethyl core)",
      "iupac_name": "(S)-1-[2-(1-{3-[p-({2-Ethyl-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]propyl}cyclopentylamino)acetyl]-4,4-difluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 176 ± 46 nM; SGLT1 IC50 = 0.9 ± 0.0 nM; SGLT2 IC50 = 0.7 ± 0.0 nM; SGLT2/1 ratio = 1.3; LC-MS purity 98.1%, m/z 656.4; near-equal SGLT1/2 potency but more rapid in vitro metabolism than all other compounds tested; not advanced"
      },
      "description": "Spiro-cyclopentyl linker analogue; remarkable near-equal SGLT1/2 potency (SGLT2/1 ratio 1.3) but fastest in vitro metabolism in the entire series; not advanced."
    },
    {
      "id": "C73",
      "name": "compound 96 (N-methyl analogue of 61)",
      "iupac_name": "(S)-1-[2-(1-{4-[p-({2-Chloro-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutyl}-N-methylamino)acetyl]-4,4-difluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house (N-methylation of 61 with MeI)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 7880 ± 3860 nM; SGLT1 IC50 = 108 ± 21 nM; SGLT2 IC50 = 3.2 ± 0.2 nM; SGLT2/1 ratio = 34; LC-MS purity 97.9%, m/z 650.2; N-methylation abolished DPP4 activity consistent with loss of β-NH interactions with Glu205/206"
      },
      "description": "N-Methyl analogue of compound 61; DPP4 activity essentially abolished (IC50 7880 nM vs 38 nM for NH analogue 61), confirming importance of β-NH for Glu205/206 interaction."
    },
    {
      "id": "C74",
      "name": "compound 97 (trans-cyclopentyl, 6-deoxy, chloro)",
      "iupac_name": "(2S,4S)-1-{2-[(1S,3S)-3-[p-({2-Chloro-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclopentylamino]acetyl}-4-fluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 6.0 ± 0.5 nM; SGLT1 IC50 = 237 ± 128 nM; SGLT2 IC50 = 1.4 ± 0.8 nM; SGLT2/1 ratio = 167; LC-MS purity 99.5%, m/z 602.3; weaker SGLT1 than 61"
      },
      "description": "Trans-1,3-cyclopentyl linker with 6-deoxy chloro series; very potent DPP4/SGLT2 but weaker SGLT1 (237 nM) than lead 61."
    },
    {
      "id": "C75",
      "name": "compound 98 (cis-cyclohexyl, 6-deoxy, chloro)",
      "iupac_name": "(2S,4S)-1-{2-[(1R,4R)-4-[p-({2-Chloro-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclohexylamino]acetyl}-4-fluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 5.3 ± 0.7 nM; SGLT1 IC50 = 291 ± 214 nM; SGLT2 IC50 = 0.8 ± 0.2 nM; SGLT2/1 ratio = 360; LC-MS purity 100.0%, m/z 616.3; weaker SGLT1 and high SGLT2 selectivity"
      },
      "description": "Cis-1,4-cyclohexyl linker with 6-deoxy chloro series; potent DPP4/SGLT2 but weak SGLT1 (291 nM) and high SGLT2 selectivity (360:1)."
    },
    {
      "id": "C76",
      "name": "compound 99 (methyl core, 4,4-difluoro — LEAD 1)",
      "iupac_name": "(S)-1-(2-{1,1-Dimethyl-4-[p-({5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]-2-tolyl}methyl)phenoxy]butylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 58 ± 12 nM; SGLT1 IC50 = 23 ± 7 nM; SGLT2 IC50 = 0.8 ± 0.2 nM; SGLT2/1 ratio = 29; LC-MS purity 96.4%, m/z 616.4; ZDF rat OGTT (30 mg/kg): significantly superior plasma glucose AUC0-3h vs dapagliflozin (p=0.0185); significantly elevated aGLP-1 (p<0.0001); DPP4 vs DPP8 selectivity: 6.8-fold; DPP4 vs DPP9 selectivity: 2.4-fold; ob/ob mice (10 days): dose-dependent plasma glucose reduction; no significant UGE/urine volume increase unlike sotagliflozin; SAFETYscan44 at 10 μM: <50% inhibition of all 44 off-targets; THREE development candidates (64, 99, 101) under IND-enabling evaluation"
      },
      "description": "Lead compound 99; methyl-core (R1=Me) analogue with 4,4-difluoro DPP4 pharmacophore; balanced SGLT2/1 ratio (29:1); superior glycemic control and sustained aGLP-1 elevation in ZDF rats; no adverse effects in ob/ob mice; one of three clinical development candidates."
    },
    {
      "id": "C77",
      "name": "compound 100 (isopropyl core, near-equal SGLT1/2)",
      "iupac_name": "(S)-1-(2-{1,1-Dimethyl-4-[p-({5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]-2-cumenyl}methyl)phenoxy]butylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 117 ± 39 nM; SGLT1 IC50 = 1.2 ± 0.0 nM; SGLT2 IC50 = 1.0 ± 0.2 nM; SGLT2/1 ratio = 1.2; LC-MS purity 99.2%, m/z 644.4; excluded from further consideration due to less potent DPP4 (117 nM)"
      },
      "description": "Isopropyl-core analogue inspired by mizagliflozin 10; near-equal SGLT1/2 potency (ratio 1.2) as expected, but insufficient DPP4 potency (117 nM) for further development."
    },
    {
      "id": "C78",
      "name": "compound 101 (ethyl core, 4,4-difluoro — LEAD 2)",
      "iupac_name": "(S)-1-(2-{4-[p-({2-Ethyl-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 72 ± 41 nM; SGLT1 IC50 = 4.2 ± 1.1 nM; SGLT2 IC50 = 0.8 ± 0.2 nM; SGLT2/1 ratio = 5.2; LC-MS purity 96.0%, m/z 630.4; deacetylated form of prodrug 64; ZDF rat OGTT (30 mg/kg): significantly superior plasma glucose vs dapagliflozin at 0.5h (p=0.023) and 1h (p=0.019); significantly elevated aGLP-1 vs both dapagliflozin and sotagliflozin (p<0.0001); DPP4 vs DPP8 selectivity: 9.3-fold; DPP4 vs DPP9 selectivity: 2.6-fold; ob/ob mice (50 mg/kg, 10 days): significant antihyperglycemic efficacy; oral bioavailability (rat) F=4.8%; THREE development candidates (64, 99, 101) under IND-enabling evaluation"
      },
      "description": "Lead compound 101; ethyl-core 6-deoxy analogue with 4,4-difluoro DPP4 pharmacophore (deacetylated form of prodrug 64); excellent balanced SGLT1/2 inhibition (SGLT2/1 ratio 5.2) combined with potent DPP4 inhibition; one of three clinical development candidates."
    },
    {
      "id": "C79",
      "name": "compound 102 (indane core analogue)",
      "iupac_name": "(S)-1-(2-{1,1-Dimethyl-4-[p-({6-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]-4-indanyl}methyl)phenoxy]butylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house (Scheme 11)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 71 ± 49 nM; SGLT1 IC50 = 6.7 ± 3.7 nM; SGLT2 IC50 = 1.0 ± 0.4 nM; SGLT2/1 ratio = 6.7; LC-MS purity 99.8%, m/z 640.4; indane core analogous to HM41322 (8); rat oral UGE 746 mg/24h"
      },
      "description": "Indane-core analogue of compound 101, prepared via 12-step synthesis (Scheme 11) from 5-indanylamine; potent across all three targets with favorable SGLT2/1 ratio; less UGE than 101 in rats."
    },
    {
      "id": "C80",
      "name": "compound 124 (4,4-didesfluoro analogue of 101)",
      "iupac_name": "(S)-1-(2-{4-[p-({2-Ethyl-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 162 ± 53 nM; SGLT1 IC50 = 3.9 ± 1.2 nM; SGLT2 IC50 = 0.9 ± 0.2 nM; SGLT2/1 ratio = 4.6; LC-MS purity 97.7%, m/z 594.4; 2-fold lower DPP4 vs 101; oral UGE 165 mg (vs 2110 mg for 101); F=1.2%"
      },
      "description": "Unmodified 2-cyanopyrrolidine analogue of 101 (no fluorine at C4); 2-fold lower DPP4 potency; dramatically lower in vivo UGE suggesting importance of C4 fluorination for bioavailability."
    },
    {
      "id": "C81",
      "name": "compound 125 (4-monofluoro analogue of 101)",
      "iupac_name": "(2S,4S)-1-(2-{4-[p-({2-Ethyl-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4-fluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 69 ± 37 nM; SGLT1 IC50 = 3.0 ± 0.7 nM; SGLT2 IC50 = 0.4 ± 0.2 nM; SGLT2/1 ratio = 7.1; LC-MS purity 99.9%, m/z 612.4; ZDF rat OGTT (30 mg/kg): trend toward significance vs dapagliflozin (p=0.0852); >50% CYP2C9 inhibition at 10 μM; oral UGE 662 mg; F=1.0%"
      },
      "description": "Monofluorinated (4-fluoro) analogue of 101; same activity profile as parent 101 across targets; slightly better hepatocyte stability; CYP2C9 inhibition concern."
    },
    {
      "id": "C82",
      "name": "compound 126 (ethyl core, cyclopentyl linker, monofluoro)",
      "iupac_name": "(2S,4S)-1-{2-[(1S,3S)-3-[p-({2-Ethyl-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclopentylamino]acetyl}-4-fluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 17 ± 6 nM; SGLT1 IC50 = 3.4 ± 0.5 nM; SGLT2 IC50 = 0.7 ± 0.4 nM; SGLT2/1 ratio = 4.6; LC-MS purity 96.8%, m/z 612.4; 70-fold improvement in SGLT1 vs chloro analogue 97 (3.4 vs 237 nM); oral UGE indistinguishable from baseline; short oral half-life"
      },
      "description": "Ethyl-core trans-1,3-cyclopentyl linker analogue; 70-fold better SGLT1 potency than chloro analogue 97 but unexpectedly poor in vivo efficacy (UGE baseline level) due to short oral half-life."
    },
    {
      "id": "C83",
      "name": "compound 127 (ethyl core, cyclopentyl linker, 4,4-difluoro)",
      "iupac_name": "(S)-1-{2-[(1S,3S)-3-[p-({2-Ethyl-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclopentylamino]acetyl}-4,4-difluoro-2-pyrrolidinecarbonitrile",
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 IC50 = 50 ± 17 nM; SGLT1 IC50 = 3.2 ± 0.9 nM; SGLT2 IC50 = 1.0 ± 0.3 nM; SGLT2/1 ratio = 3.9; LC-MS purity 95.8%, m/z 614.3; unstable in phosphate buffer pH 6.4 and 7.5 and in rat plasma; oral UGE indistinguishable from baseline"
      },
      "description": "4,4-Difluoro analogue of 126 with cyclopentyl linker; 3-fold lower DPP4 potency vs 126; chemical lability in phosphate buffer and rat plasma; poor in vivo efficacy."
    },
    {
      "id": "C84",
      "name": "linagliptin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reference_compound",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": "DPP4 inhibitor class; high plasma clearance but strong kidney distribution; used as comparator in tissue distribution studies"
      },
      "description": "Marketed DPP4 inhibitor used as comparator in Sprague-Dawley rat tissue distribution studies to demonstrate kidney accumulation pattern."
    },
    {
      "id": "C85",
      "name": "Boc-D-thiazolidine-4-carboxylic acid (compound 52)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Commercially available starting material for preparation of thiazolidine alkylating agent 23c (Scheme 3)."
    },
    {
      "id": "C86",
      "name": "Boc-azabicyclo[3.1.0]hexane-3-carbonitrile (compound 56)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Commercially available saxagliptin-inspired bicyclic building block used as starting material for preparation of alkylating agent 58 (Scheme 3)."
    },
    {
      "id": "C87",
      "name": "isopropyl-β-D-thiogalactopyranoside (compound 85)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Commercially available carbohydrate starting material for synthesis of 4-fluoro and 4,4-difluoro C-glycoside intermediates 18e/18f (Scheme 8)."
    },
    {
      "id": "C88",
      "name": "dapagliflozin precursor 71",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "prepared as reported in patent literature (Ellsworth et al. US 6,515,117 B2)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Known intermediate in dapagliflozin synthesis accessed per patent literature; used as starting material for 6-deoxy series (Scheme 5)."
    },
    {
      "id": "C89",
      "name": "NHC-borane 74",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "known compound (Monot et al. Org. Lett. 2009)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Known N-heterocyclic carbene borane reagent used in Suzuki-Miyaura reactions to install ethyl substituent in 18c and 77 (Schemes 5, 6)."
    },
    {
      "id": "C90",
      "name": "5-indanylamine (compound 113)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Commercially available starting material for Scheme 11 synthesis of indane-core compound 102."
    },
    {
      "id": "C91",
      "name": "TBDPS-protected 4-hydroxybenzaldehyde (compound 117)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial or prepared",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "TBDPS-protected para-hydroxybenzaldehyde used in lithiation-addition step of Scheme 11 to install the diphenylmethylene core structure of compound 102."
    },
    {
      "id": "C92",
      "name": "protected 6-deoxygluconolactone 120",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house (preparation not detailed in main text)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Tribenzyloxy-protected 6-deoxygluconolactone substrate used in Scheme 11 glycosylation step for compound 102; preparation details not provided in main text."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "General Route to Phenol Intermediate 19a (BBr3 Dealkylation of 18a)",
      "target_compound_id": "C26",
      "target_compound_name": "phenol intermediate 19a",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "O-dealkylation (boron tribromide mediated)",
          "reactants": [
            {
              "compound_id": "C18",
              "name": "tetraacetyl dapagliflozin (18a)",
              "amount": "9.90 g (17.2 mmol)"
            }
          ],
          "reagents": [
            {
              "name": "boron tribromide (BBr3)",
              "amount": "10 equiv (dissolved in dry CH2Cl2)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "235 mL"
            }
          ],
          "conditions": {
            "temperature": "-70 °C initially, raised to -30 °C",
            "time": "reaction monitored by TLC/LC-MS until complete (general procedure: up to several hours)",
            "pressure": null,
            "atmosphere": "N2",
            "ph": null,
            "other": "BBr3 solution added dropwise at -70 °C; after 0.5 h temperature raised to -30 °C; after completion, poured onto ice and neutralized with sat. NaHCO3 (400 mL); aqueous layer extracted twice with CH2Cl2; combined organics washed with brine, dried over Na2SO4, filtered, concentrated"
          },
          "product": {
            "compound_id": "C26",
            "name": "phenol intermediate 19a",
            "yield": "8.80 g (93%)",
            "purity": "97.0% by HPLC; LC-MS purity 90.6%",
            "molar_activity": null,
            "characterization": ["HPLC", "LC-MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {"adduct": "[M(35Cl)+H2O]+", "mz": 566.2},
                {"adduct": "[M(37Cl)+H2O]+", "mz": 568.2}
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "trituration of crude product with EtOAc/petroleum ether (1:5, 90 mL) at 25 °C for 0.5 h; collected as white solid",
          "notes": "General procedure applies to BBr3 dealkylation of all 18a-h; individual dealkylation conditions (temperature ramp, reaction time) specified per compound in experimental section. Product characterized by NMR in main text."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "General Route 1 to Final Triple Inhibitors (exemplified by compound 27)",
      "target_compound_id": "C43",
      "target_compound_name": "compound 27",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Mitsunobu etherification",
          "reactants": [
            {
              "compound_id": "C26",
              "name": "phenol intermediate 19a",
              "amount": "170 mg (0.31 mmol)"
            },
            {
              "compound_id": "C34",
              "name": "gem-dimethyl C4 linker alcohol 20b",
              "amount": "168 mg (0.77 mmol, 2.5 equiv)"
            }
          ],
          "reagents": [
            {
              "name": "triphenylphosphine (PPh3)",
              "amount": "203 mg (0.77 mmol, 2.5 equiv)",
              "role": "other"
            },
            {
              "name": "DIAD (diisopropyl azodicarboxylate)",
              "amount": "157 mg (151 μL, 0.77 mmol, 2.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "~1.2 mL"
            }
          ],
          "conditions": {
            "temperature": "0-5 °C for DIAD addition, then 25 °C",
            "time": "20 h",
            "pressure": null,
            "atmosphere": "N2",
            "ph": null,
            "other": "DIAD added at 0-5 °C; reaction followed by TLC until complete; workup: evaporation, purification by column chromatography"
          },
          "product": {
            "compound_id": null,
            "name": "Boc-protected linker-coupled intermediate 21b",
            "yield": "168 mg (73%)",
            "purity": "LC-MS purity 94.7%",
            "molar_activity": null,
            "characterization": ["LC-MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {"adduct": "[M(35Cl)-Boc+H]+", "mz": 590.4},
                {"adduct": "[M(37Cl)-Boc+H]+", "mz": 592.0}
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica (12.5 → 17 → 22 → 100% EtOAc/petroleum ether) followed by preparative TLC (1:1 EtOAc/petroleum ether)",
          "notes": "General Mitsunobu procedure applies to all 19a-h + 20a-e and 20m-p couplings. Reactant 20b evaporated with toluene or THF/toluene for additional drying in some cases."
        },
        {
          "step_number": 2,
          "reaction_type": "Boc deprotection (TFA)",
          "reactants": [
            {
              "compound_id": null,
              "name": "Boc-protected intermediate 21b",
              "amount": "100 mg (0.13 mmol)"
            }
          ],
          "reagents": [
            {
              "name": "trifluoroacetic acid (TFA)",
              "amount": "200 μL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "2.0 mL"
            }
          ],
          "conditions": {
            "temperature": "30 °C",
            "time": "2 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "reaction monitored by TLC; concentrated under reduced pressure; coevaporated with MeCN to remove residual TFA; product isolated as TFA salt"
          },
          "product": {
            "compound_id": null,
            "name": "free amine TFA salt 22b",
            "yield": "100 mg (98%)",
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
          "purification": "coevaporation with MeCN under reduced pressure",
          "notes": "General procedure for Boc deprotection (22a-l and 22n-q) using TFA/CH2Cl2 at 15-30 °C for up to 4 h. Ratio TFA:CH2Cl2 varies from 1:4 to 1:10 v/v."
        },
        {
          "step_number": 3,
          "reaction_type": "N-alkylation",
          "reactants": [
            {
              "compound_id": null,
              "name": "free amine TFA salt 22b",
              "amount": "150 mg (0.20 mmol)"
            },
            {
              "compound_id": "C35",
              "name": "chloroacetyl-(S)-2-cyanopyrrolidine (23a)",
              "amount": "34 mg (0.20 mmol, 1.0 equiv)"
            }
          ],
          "reagents": [
            {
              "name": "K2CO3",
              "amount": "82 mg (0.59 mmol, 3.0 equiv)",
              "role": "base"
            },
            {
              "name": "NaI",
              "amount": "3.0 mg (0.02 mmol, 0.1 equiv)",
              "role": "catalyst"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "1.5 mL"
            }
          ],
          "conditions": {
            "temperature": "addition at 5 °C, reaction at 25 °C",
            "time": "24 h",
            "pressure": null,
            "atmosphere": "N2",
            "ph": null,
            "other": "after completion diluted with ~10 volumes water, extracted 3x EtOAc, washed with brine, dried Na2SO4, concentrated; crude used directly in deprotection"
          },
          "product": {
            "compound_id": null,
            "name": "acetylated triple inhibitor 24b",
            "yield": "120 mg (crude)",
            "purity": "LC-MS purity 66.7%",
            "molar_activity": null,
            "characterization": ["LC-MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {"adduct": "[M(35Cl)+H]+", "mz": 784.3},
                {"adduct": "[M(37Cl)+H]+", "mz": 786.3}
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "crude material taken to next step without purification",
          "notes": "General N-alkylation procedure (Route 1) applies to 23a-d or 58 with amines 22a-q. Yields over two steps are quoted following subsequent deprotection."
        },
        {
          "step_number": 4,
          "reaction_type": "deacetylation (Zemplén conditions)",
          "reactants": [
            {
              "compound_id": null,
              "name": "acetylated intermediate 24b",
              "amount": "120 mg (~0.15 mmol)"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "7.0 M NH3/MeOH",
              "volume": "3.0 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "6 h",
            "pressure": null,
            "atmosphere": "sealed vessel",
            "ph": null,
            "other": "volatiles removed under reduced pressure; residue coevaporated 3x with MeOH to remove NH3"
          },
          "product": {
            "compound_id": "C43",
            "name": "compound 27",
            "yield": "18.0 mg (15% over two steps from 22b)",
            "purity": "100.0% by HPLC and LC-MS",
            "molar_activity": null,
            "characterization": ["HPLC", "LC-MS", "1H NMR"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {"adduct": "[M(35Cl)+H]+", "mz": 616.2},
                {"adduct": "[M(37Cl)+H]+", "mz": 618.2}
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "preparative HPLC: Waters XBridge column (150 × 25 mm, 5 μm); mobile phase A = 10 mM NH4HCO3, B = MeCN; gradient 20-40% B over 12 min",
          "notes": "General deprotection procedure (Route 1) for compounds 26-30, 32-35, 37, 38, 46-50, 60-63, 69, 70, 97, 98. Reaction times 2.5-12 h at 10-25 °C. Isolated after preparative HPLC purification as white solids."
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Synthesis of Alkylating Agent 23c (Thiazolidine DPP4 Pharmacophore, Scheme 3)",
      "target_compound_id": "C37",
      "target_compound_name": "chloroacetyl-(S)-4-cyano-thiazolidine 23c",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "mixed anhydride amidation",
          "reactants": [
            {
              "compound_id": "C85",
              "name": "Boc-D-thiazolidine-4-carboxylic acid (52)",
              "amount": "1.00 g (4.29 mmol)"
            }
          ],
          "reagents": [
            {
              "name": "ethyl chloroformate",
              "amount": "767 mg (673 μL, 7.07 mmol, 1.65 equiv)",
              "role": "other"
            },
            {
              "name": "Et3N",
              "amount": "715 mg (984 μL, 7.07 mmol, 1.65 equiv)",
              "role": "base"
            },
            {
              "name": "NH4OH (25%)",
              "amount": "12.0 g (13.2 mL)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "7.0 mL"
            }
          ],
          "conditions": {
            "temperature": "-15 °C for ethyl chloroformate addition; -20 to -13 °C for NH4OH addition; then 25 °C",
            "time": "0.5 h at -15 °C, then 16 h at 25 °C",
            "pressure": null,
            "atmosphere": "N2",
            "ph": null,
            "other": "extracted with CH2Cl2 (2×15 mL then 2×10 mL); washed with water (3×20 mL) and brine; dried Na2SO4; purified by column chromatography"
          },
          "product": {
            "compound_id": null,
            "name": "Boc-thiazolidine-4-carboxamide 53",
            "yield": "730 mg (73%)",
            "purity": null,
            "molar_activity": null,
            "characterization": ["LC-MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {"adduct": "[M-Boc+H]+", "mz": 133.1}
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica (17 → 100% EtOAc/petroleum ether)",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "dehydration to nitrile (TFAA)",
          "reactants": [
            {
              "compound_id": null,
              "name": "Boc-thiazolidine-4-carboxamide 53",
              "amount": "730 mg (3.14 mmol)"
            }
          ],
          "reagents": [
            {
              "name": "trifluoroacetic anhydride (TFAA)",
              "amount": "990 mg (656 μL, 4.71 mmol, 1.5 equiv)",
              "role": "other"
            },
            {
              "name": "Et3N",
              "amount": "954 mg (1.31 mL, 9.43 mmol, 3.0 equiv)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "3.5 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C",
            "time": "1.5 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "diluted with water (20 mL); extracted with CH2Cl2 (15 mL then 10 mL); washed water (3×15 mL) and brine; crude used directly"
          },
          "product": {
            "compound_id": null,
            "name": "Boc-thiazolidine-4-carbonitrile 54",
            "yield": "690 mg (>100%, crude)",
            "purity": null,
            "molar_activity": null,
            "characterization": ["1H NMR"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "used directly without purification",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Boc deprotection (TsOH)",
          "reactants": [
            {
              "compound_id": null,
              "name": "Boc-thiazolidine-4-carbonitrile 54",
              "amount": "690 mg (3.22 mmol)"
            }
          ],
          "reagents": [
            {
              "name": "p-toluenesulfonic acid monohydrate",
              "amount": "919 mg (4.83 mmol, 1.5 equiv)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "MeCN",
              "volume": "4.8 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "24 h",
            "pressure": null,
            "atmosphere": "N2",
            "ph": null,
            "other": "concentrated under reduced pressure; crude brown solid used directly"
          },
          "product": {
            "compound_id": null,
            "name": "thiazolidine-4-carbonitrile tosylate salt 55",
            "yield": "1.50 g (>100%, crude)",
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
          "purification": "used without further purification",
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "N-acylation with chloroacetyl chloride",
          "reactants": [
            {
              "compound_id": null,
              "name": "thiazolidine-4-carbonitrile tosylate salt 55",
              "amount": "1.30 g (4.54 mmol)"
            }
          ],
          "reagents": [
            {
              "name": "chloroacetyl chloride",
              "amount": "513 mg (361 μL, 4.54 mmol, 1.0 equiv)",
              "role": "other"
            },
            {
              "name": "Et3N",
              "amount": "919 mg (1.26 mL, 9.08 mmol, 2.0 equiv)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "9.0 mL total (4.5 mL per solution)"
            }
          ],
          "conditions": {
            "temperature": "0 °C",
            "time": "2 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "amine/Et3N solution added dropwise to chloroacetyl chloride solution at 0 °C; diluted with water (30 mL); extracted with CH2Cl2 (5×20 mL); washed with water (20 mL) and brine (20 mL)"
          },
          "product": {
            "compound_id": "C37",
            "name": "chloroacetyl-(S)-4-cyano-thiazolidine (23c)",
            "yield": "360 mg (60% over three steps from 53)",
            "purity": null,
            "molar_activity": null,
            "characterization": ["1H NMR", "LC-MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "concentration under reduced pressure; obtained as brown solid",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "General Route 2 to Final Triple Inhibitors (exemplified by compound 99)",
      "target_compound_id": "C76",
      "target_compound_name": "compound 99",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Mitsunobu etherification",
          "reactants": [
            {
              "compound_id": "C32",
              "name": "methyl-core phenol intermediate 19g",
              "amount": "0.90 g (1.90 mmol)"
            },
            {
              "compound_id": "C34",
              "name": "gem-dimethyl C4 linker alcohol 20b",
              "amount": "1.00 g (4.80 mmol, 2.5 equiv)"
            }
          ],
          "reagents": [
            {
              "name": "PPh3",
              "amount": "1.25 g (4.80 mmol, 2.5 equiv)",
              "role": "other"
            },
            {
              "name": "DIAD",
              "amount": "0.97 g (0.90 mL, 4.80 mmol, 2.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "6.3 mL"
            }
          ],
          "conditions": {
            "temperature": "reflux",
            "time": "3 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "purified by column chromatography; characterization performed at later step"
          },
          "product": {
            "compound_id": null,
            "name": "Boc-protected intermediate 21u",
            "yield": "0.92 g (81%)",
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
          "purification": "column chromatography on silica (6.5 → 100% EtOAc/petroleum ether)",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "simultaneous Boc deprotection and sugar deacetylation (acid)",
          "reactants": [
            {
              "compound_id": null,
              "name": "Boc-protected intermediate 21u",
              "amount": "0.50 g (0.75 mmol)"
            }
          ],
          "reagents": [
            {
              "name": "4 M HCl/MeOH",
              "amount": "12.5 mL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "included in 4 M HCl/MeOH solution"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "12 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "concentrated under reduced pressure; crude yellow oil used without further purification; product isolated as HCl salt"
          },
          "product": {
            "compound_id": null,
            "name": "fully deprotected amine HCl salt 25d",
            "yield": "0.60 g (>100%, crude containing HCl salt)",
            "purity": "LC-MS purity 90.0%, m/z 444.4 ([M+H]+)",
            "molar_activity": null,
            "characterization": ["LC-MS", "1H NMR"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {"adduct": "[M+H]+", "mz": 444.4}
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "used directly without further purification",
          "notes": "Route 2 general procedure: Boc and acetyl groups removed simultaneously with excess 4 M HCl/MeOH in MeOH at 20-25 °C for 1-12 h. All intermediates isolated as HCl salts."
        },
        {
          "step_number": 3,
          "reaction_type": "N-alkylation",
          "reactants": [
            {
              "compound_id": null,
              "name": "fully deprotected amine HCl salt 25d",
              "amount": "200 mg (0.42 mmol)"
            },
            {
              "compound_id": "C38",
              "name": "chloroacetyl-4,4-difluoro-2-cyanopyrrolidine (23d)",
              "amount": "174 mg (0.83 mmol, 2.0 equiv)"
            }
          ],
          "reagents": [
            {
              "name": "K2CO3",
              "amount": "173 mg (1.25 mmol, 3.0 equiv)",
              "role": "base"
            },
            {
              "name": "NaI",
              "amount": "25 mg (0.17 mmol, 0.4 equiv)",
              "role": "catalyst"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "2.0 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "12 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "workup: diluted with ~10 volumes water, extracted 3x EtOAc, washed brine, dried Na2SO4, concentrated"
          },
          "product": {
            "compound_id": "C76",
            "name": "compound 99",
            "yield": "220 mg (44%)",
            "purity": "96.4% by LC-MS",
            "molar_activity": null,
            "characterization": ["LC-MS", "1H NMR", "13C NMR", "19F NMR"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {"adduct": "[M+H]+", "mz": 616.4}
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "preparative HPLC: Waters XBridge BEH C18 (250 × 70 mm, 10 μm); mobile phase A = 0.05% NH4OH + 10 mM NH4HCO3, B = MeCN; gradient 35-65% B over 20 min",
          "notes": "Route 2 general procedure for N-alkylation of amines 25a-g with 23a-d; same conditions as Route 1 alkylation. All compounds isolated as white solids after preparative HPLC."
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Synthesis of 6-Deoxy C-Glycoside Intermediates 18b and 18c (Scheme 5)",
      "target_compound_id": "C19",
      "target_compound_name": "6-deoxy triacetyl chloro C-glycoside (compound 18b)",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Appel reaction (iodination of primary alcohol)",
          "reactants": [
            {
              "compound_id": "C88",
              "name": "dapagliflozin precursor 71",
              "amount": "24.4 g (33.4 mmol)"
            }
          ],
          "reagents": [
            {
              "name": "PPh3",
              "amount": "11.6 g (44.4 mmol, 1.33 equiv)",
              "role": "other"
            },
            {
              "name": "imidazole",
              "amount": "2.85 g (41.9 mmol, 1.26 equiv)",
              "role": "other"
            },
            {
              "name": "I2",
              "amount": "10.5 g (41.5 mmol, 1.24 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "195 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C, then 50 °C",
            "time": "5 h",
            "pressure": null,
            "atmosphere": "N2",
            "ph": null,
            "other": "cooled to 25 °C, poured into water (200 mL), extracted with DCM (3×100 mL); washed with 0.5 M HCl (150 mL) and brine (2×80 mL); dried Na2SO4; purified by column chromatography on silica (0→2→3.3→5→100% MeOH/CH2Cl2)"
          },
          "product": {
            "compound_id": null,
            "name": "iodomethyl intermediate 72",
            "yield": "17.8 g (58%)",
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
          "purification": "column chromatography on silica",
          "notes": "Characterization performed after next step."
        },
        {
          "step_number": 2,
          "reaction_type": "acetyl protection",
          "reactants": [
            {
              "compound_id": null,
              "name": "iodomethyl intermediate 72",
              "amount": "17.8 g (32.4 mmol)"
            }
          ],
          "reagents": [
            {
              "name": "Ac2O",
              "amount": "33.1 g (30.4 mL, 324 mmol, 10 equiv)",
              "role": "other"
            },
            {
              "name": "DMAP",
              "amount": "792 mg (6.49 mmol, 0.2 equiv)",
              "role": "catalyst"
            }
          ],
          "solvents": [
            {
              "name": "pyridine",
              "volume": "124 mL"
            }
          ],
          "conditions": {
            "temperature": "0-10 °C then 25 °C",
            "time": "15 h",
            "pressure": null,
            "atmosphere": "N2",
            "ph": null,
            "other": "cooled in ice bath; water added after reaction; extracted with EtOAc; washed brine; purified by column chromatography"
          },
          "product": {
            "compound_id": null,
            "name": "triacetyl iodomethyl intermediate 73",
            "yield": "5.50 g (25%)",
            "purity": null,
            "molar_activity": null,
            "characterization": ["1H NMR"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica (0→9→11→100% EtOAc/petroleum ether)",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "hydrogenolytic deiodination",
          "reactants": [
            {
              "compound_id": null,
              "name": "triacetyl iodomethyl intermediate 73",
              "amount": "5.00 g (7.41 mmol)"
            }
          ],
          "reagents": [
            {
              "name": "wet 10% Pd/C",
              "amount": "2.00 g",
              "role": "catalyst"
            },
            {
              "name": "Et3N",
              "amount": "7.50 g (10.3 mL, 74.1 mmol, 10 equiv)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "2:1 THF/MeOH",
              "volume": "45 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "24 h",
            "pressure": null,
            "atmosphere": "H2 (1 atm)",
            "ph": null,
            "other": "filtered; concentrated; partitioned between EtOAc (300 mL) and water (150 mL); organic layer washed brine, dried Na2SO4; purified by column chromatography"
          },
          "product": {
            "compound_id": null,
            "name": "deiodinated methyl intermediate (deiodinated 18b precursor with OMe)",
            "yield": "3.70 g (96%)",
            "purity": null,
            "molar_activity": null,
            "characterization": ["1H NMR"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica (0→11→33→50→100% EtOAc/petroleum ether)",
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "anomeric reduction (Et3SiH/BF3·OEt2)",
          "reactants": [
            {
              "compound_id": null,
              "name": "deiodinated methoxy intermediate",
              "amount": "3.70 g dissolved in MeCN (26 mL)"
            }
          ],
          "reagents": [
            {
              "name": "Et3SiH",
              "amount": "2.51 g (3.44 mL, 21.6 mmol, 3.2 equiv)",
              "role": "reductant"
            },
            {
              "name": "BF3·Et2O",
              "amount": "2.30 g (2.00 mL, 16.2 mmol, 2.4 equiv)",
              "role": "other"
            },
            {
              "name": "water",
              "amount": "121 μL (6.74 mmol, 1.0 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "MeCN",
              "volume": "26 mL"
            }
          ],
          "conditions": {
            "temperature": "<15 °C for additions, then 25 °C",
            "time": "5 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "cooled in ice bath before additions; quenched with sat. NaHCO3 (100 mL); extracted with EtOAc (3×40 mL); washed brine; dried Na2SO4; triturated"
          },
          "product": {
            "compound_id": "C19",
            "name": "6-deoxy triacetyl chloro C-glycoside 18b",
            "yield": "2.90 g (83%)",
            "purity": "LC-MS purity 95.9%, m/z 541.0 (100%; [M(35Cl)+Na]+)",
            "molar_activity": null,
            "characterization": ["1H NMR", "LC-MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {"adduct": "[M(35Cl)+Na]+", "mz": 541.0},
                {"adduct": "[M(37Cl)+Na]+", "mz": 543.0}
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "trituration with 1:7 EtOAc/petroleum ether (40 mL) at 25 °C for 16 h; white solid",
          "notes": "18c (ethyl analogue) was prepared from 18b by Suzuki-Miyaura coupling with NHC-borane 74 [Pd(OAc)2 (10 mol%), RuPhos, toluene/H2O (10:1), 80 °C, 24 h] in 80% yield."
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Synthesis of Lead Compound 101 (Route 2, Ethyl Core)",
      "target_compound_id": "C78",
      "target_compound_name": "compound 101",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Mitsunobu etherification",
          "reactants": [
            {
              "compound_id": "C28",
              "name": "ethyl-core phenol intermediate 19c",
              "amount": "3.00 g (6.19 mmol)"
            },
            {
              "compound_id": "C34",
              "name": "gem-dimethyl C4 linker alcohol 20b",
              "amount": "2.69 g (12.4 mmol, 2.0 equiv)"
            }
          ],
          "reagents": [
            {
              "name": "PPh3",
              "amount": "4.06 g (15.5 mmol, 2.5 equiv)",
              "role": "other"
            },
            {
              "name": "DIAD",
              "amount": "3.13 g (3.00 mL, 15.5 mmol, 2.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "30 mL"
            }
          ],
          "conditions": {
            "temperature": "reflux",
            "time": "3 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "purified by column chromatography (5→14% EtOAc/petroleum ether); colorless oil; full characterization at later step"
          },
          "product": {
            "compound_id": null,
            "name": "Boc-protected intermediate 21m",
            "yield": "4.00 g (95%)",
            "purity": "LC-MS: m/z 706.4 (100%; [M+Na]+), 584.4 (65%; [M-Boc+H]+)",
            "molar_activity": null,
            "characterization": ["LC-MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {"adduct": "[M+Na]+", "mz": 706.4},
                {"adduct": "[M-Boc+H]+", "mz": 584.4}
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica (5→14% EtOAc/petroleum ether)",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "simultaneous Boc deprotection and sugar deacetylation (HCl/MeOH)",
          "reactants": [
            {
              "compound_id": null,
              "name": "Boc-protected intermediate 21m",
              "amount": "0.80 g (1.17 mmol)"
            }
          ],
          "reagents": [
            {
              "name": "4 M HCl/MeOH",
              "amount": "10 mL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "1.0 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "1 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "concentrated; product isolated as HCl salt"
          },
          "product": {
            "compound_id": null,
            "name": "fully deprotected amine HCl salt 25f",
            "yield": "790 mg (87%)",
            "purity": "LC-MS purity 89.7%, m/z 458.4 (100%; [M+H]+)",
            "molar_activity": null,
            "characterization": ["LC-MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {"adduct": "[M+H]+", "mz": 458.4}
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "used without further purification",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "N-alkylation (two-portion addition)",
          "reactants": [
            {
              "compound_id": null,
              "name": "amine HCl salt 25f",
              "amount": "400 mg (0.81 mmol)"
            },
            {
              "compound_id": "C38",
              "name": "chloroacetyl-4,4-difluoro-2-cyanopyrrolidine (23d)",
              "amount": "169 mg (0.81 mmol, 1.0 equiv) initial + 169 mg (0.81 mmol, 1.0 equiv) additional = 338 mg total (2.0 equiv)"
            }
          ],
          "reagents": [
            {
              "name": "K2CO3",
              "amount": "336 mg (2.43 mmol, 3.0 equiv)",
              "role": "base"
            },
            {
              "name": "NaI",
              "amount": "49 mg (0.32 mmol, 0.4 equiv)",
              "role": "catalyst"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "4.0 mL initial + 2.0 mL for second portion = 6.0 mL total"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "2 h initial + 12 h additional = 14 h total",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "first portion of 23d in DMF (4 mL) stirred 2 h; additional portion of 23d in DMF (2 mL) added dropwise and stirred further 12 h; standard workup"
          },
          "product": {
            "compound_id": "C78",
            "name": "compound 101",
            "yield": "110 mg (58%)",
            "purity": "96.0% by LC-MS",
            "molar_activity": null,
            "characterization": ["1H NMR", "13C NMR", "19F NMR", "LC-MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {"adduct": "[M+H]+", "mz": 630.4}
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "preparative HPLC: Phenomenex Gemini NX (80×40 mm, 3 μm); mobile phase A = 10 mM NH4HCO3, B = MeCN; gradient 30-60% B over 8 min; white solid",
          "notes": "Two-portion alkylating agent addition used to improve conversion. Route 2 general procedure applies to 25a-g and S2 with 23a-d."
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Synthesis of Lead Compound 99 (Route 2, Methyl Core) — see P4",
      "target_compound_id": "C76",
      "target_compound_name": "compound 99",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "see pathway P4 (steps 1-3)",
          "reactants": [],
          "reagents": [],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Pathway P4 provides the full 3-step Route 2 synthesis for compound 99 starting from phenol 19g, using Mitsunobu coupling with 20b, HCl/MeOH deprotection, and N-alkylation with 23d. Yield: 220 mg (44%). The multi-step synthesis of 19g from 5-bromo-2-methylbenzoic acid 103 is described in Scheme 9 (9 steps; key steps: acid chloride formation, Friedel-Crafts acylation with phenetole, diarylketone reduction, lithiation-gluconolactone addition, anomeric reduction, C6 tosylation/LiAlH4 reduction, acetylation, BBr3 dealkylation)."
          },
          "product": {
            "compound_id": "C76",
            "name": "compound 99",
            "yield": "220 mg (44%)",
            "purity": "96.4% by LC-MS",
            "molar_activity": null,
            "characterization": ["1H NMR", "13C NMR", "19F NMR", "LC-MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {"adduct": "[M+H]+", "mz": 616.4}
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "preparative HPLC as described in P4",
          "notes": "Full synthesis of methyl-core building block 19g (Scheme 9): 5-bromo-2-methylbenzoic acid 103 → acid chloride 104 (oxalyl chloride, 99%) → diarylketone 105 (AlCl3/phenetole, 87%) → diarylmethylene 106 (Et3SiH/BF3·OEt2, 96%) → glucosylation to 108 (n-BuLi/TMS-gluconolactone 107; MsOH/MeOH, 86%) → C-glycoside 109 (Et3SiH/BF3·OEt2, 53%) → tosylate 110 (TsCl/pyridine, 29% — low yield step) → 6-methyl product 111 (LiAlH4, 96%) → triacetate 18g (Ac2O/Et3N/DMAP, 94%) → phenol 19g (BBr3, 87%)."
        }
      ]
    },
    {
      "pathway_id": "P8",
      "pathway_name": "Synthesis of Prodrug Lead 64 (N-alkylation of amine 22m with 23d)",
      "target_compound_id": "C64",
      "target_compound_name": "compound 64 (triacetylated prodrug)",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Boc deprotection using TMSI (selective for Boc over acetates)",
          "reactants": [
            {
              "compound_id": null,
              "name": "Boc-protected intermediate 21m",
              "amount": "1.80 g (2.63 mmol)"
            }
          ],
          "reagents": [
            {
              "name": "TMSI (trimethylsilyl iodide)",
              "amount": "2.20 g (1.50 mL, 11.0 mmol, 4.2 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "MeCN",
              "volume": "120 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C",
            "time": "1.5 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "quenched with water (10 mL); extracted with EtOAc (3×20 mL); washed brine (30 mL); dried Na2SO4; purified by flash chromatography (0-35% EtOAc/petroleum ether, 35 mL/min)"
          },
          "product": {
            "compound_id": null,
            "name": "selectively Boc-deprotected amine 22m (acetates retained)",
            "yield": "1.20 g (78%)",
            "purity": "LC-MS purity 96.1%, m/z 584.3 ([M+H]+)",
            "molar_activity": null,
            "characterization": ["LC-MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {"adduct": "[M+H]+", "mz": 584.3}
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "flash column chromatography on silica (0-35% EtOAc/petroleum ether)",
          "notes": "TMSI selectively removes Boc group while leaving sugar acetates intact, enabling prodrug strategy for compound 64."
        },
        {
          "step_number": 2,
          "reaction_type": "N-alkylation",
          "reactants": [
            {
              "compound_id": null,
              "name": "selectively deprotected amine 22m",
              "amount": "510 mg (0.73 mmol)"
            },
            {
              "compound_id": "C38",
              "name": "chloroacetyl-4,4-difluoro-2-cyanopyrrolidine (23d)",
              "amount": "122 mg (0.59 mmol, 0.8 equiv)"
            }
          ],
          "reagents": [
            {
              "name": "K2CO3",
              "amount": "303 mg (2.19 mmol, 3.0 equiv)",
              "role": "base"
            },
            {
              "name": "NaI",
              "amount": "44 mg (0.29 mmol, 0.4 equiv)",
              "role": "catalyst"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "5.0 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "4 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "workup; purified by preparative HPLC"
          },
          "product": {
            "compound_id": "C64",
            "name": "compound 64 (triacetylated prodrug)",
            "yield": "125 mg (31%)",
            "purity": "99.4% by LC-MS",
            "molar_activity": null,
            "characterization": ["1H NMR", "13C NMR", "LC-MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {"adduct": "[M+H]+", "mz": 756.3}
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "preparative HPLC: Phenomenex Gemini C18 (75×40 mm, 5 μm); mobile phase A = 10 mM NH4HCO3, B = MeCN; gradient 45-75% B over 8 min; white solid",
          "notes": "Compound 64 is a prodrug; short microsomal/hepatocyte half-life (≤5.5 min) reflects rapid in vivo deacetylation to active compound 101."
        }
      ]
    },
    {
      "pathway_id": "P9",
      "pathway_name": "Synthesis of Compound 36 via Divergent Route (Scheme 2 — Gosogliptin-Type Linker)",
      "target_compound_id": "C51",
      "target_compound_name": "compound 36",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Boc protection",
          "reactants": [
            {
              "compound_id": "C40",
              "name": "L-hydroxyproline (39)",
              "amount": "2.00 g (15.3 mmol)"
            }
          ],
          "reagents": [
            {
              "name": "NaOH (1M)",
              "amount": "24 mL (1.6 equiv)",
              "role": "base"
            },
            {
              "name": "Boc2O",
              "amount": "3.99 g (4.20 mL, 18.3 mmol, 1.2 equiv)",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "2:1 water/1,4-dioxane",
              "volume": "54 mL + 6 mL dioxane for Boc2O solution"
            }
          ],
          "conditions": {
            "temperature": "0 °C initially (<10 °C); then 20 °C",
            "time": "16 h",
            "pressure": null,
            "atmosphere": "N2",
            "ph": "adjusted to pH 4 with 1 M HCl after reaction",
            "other": "concentrated to ~30 mL; extracted with EtOAc (15×100 mL); washed brine; dried Na2SO4; yellow solid"
          },
          "product": {
            "compound_id": "C41",
            "name": "Boc-hydroxyproline (40)",
            "yield": "1.60 g (45%)",
            "purity": "LC-MS purity 100.0%, m/z 230.1 ([M-H]-)",
            "molar_activity": null,
            "characterization": ["1H NMR", "LC-MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {"adduct": "[M-H]-", "mz": 230.1}
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "workup as above; yellow solid used without further purification",
          "notes": "Boc2O dissolved in 1,4-dioxane (6 mL) and added to the stirred cold reaction mixture."
        },
        {
          "step_number": 2,
          "reaction_type": "TsOH-mediated Boc deprotection of 41 to give tosylate salt 42",
          "reactants": [
            {
              "compound_id": null,
              "name": "(S)-1-Boc-2-cyanopyrrolidine (41)",
              "amount": "1.50 g (7.64 mmol)"
            }
          ],
          "reagents": [
            {
              "name": "p-toluenesulfonic acid monohydrate",
              "amount": "2.18 g (11.5 mmol, 1.5 equiv)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "MeCN",
              "volume": "7 mL"
            }
          ],
          "conditions": {
            "temperature": "20 °C",
            "time": "48 h",
            "pressure": null,
            "atmosphere": "N2",
            "ph": null,
            "other": "concentrated at 45 °C; triturated with MTBE (30 mL) for 10 min; CH2Cl2 (6 mL) added; stirred 3 h; collected by filtration; washed with MTBE; filtrate concentrated"
          },
          "product": {
            "compound_id": null,
            "name": "(S)-pyrrolidine-2-carbonitrile p-toluenesulfate (42)",
            "yield": "1.90 g (93%)",
            "purity": null,
            "molar_activity": null,
            "characterization": ["1H NMR"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "filtration and washing as described",
          "notes": "Starting material 41 is Boc-cyanopyrrolidine, commercially available or prepared."
        },
        {
          "step_number": 3,
          "reaction_type": "amide coupling (EDC/HOBt)",
          "reactants": [
            {
              "compound_id": "C41",
              "name": "Boc-hydroxyproline (40)",
              "amount": "300 mg (1.30 mmol)"
            },
            {
              "compound_id": null,
              "name": "(S)-pyrrolidine-2-carbonitrile tosylate salt (42)",
              "amount": "384 mg (1.43 mmol, 1.1 equiv)"
            }
          ],
          "reagents": [
            {
              "name": "Et3N",
              "amount": "145 mg (199 μL, 1.43 mmol, 1.1 equiv)",
              "role": "base"
            },
            {
              "name": "HOBt",
              "amount": "193 mg (1.43 mmol, 1.1 equiv)",
              "role": "coupling_reagent"
            },
            {
              "name": "EDC",
              "amount": "274 mg (1.43 mmol, 1.1 equiv)",
              "role": "coupling_reagent"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "3 mL"
            }
          ],
          "conditions": {
            "temperature": "20 °C",
            "time": "16 h",
            "pressure": null,
            "atmosphere": "N2",
            "ph": null,
            "other": "42 dissolved/suspended in CH2Cl2, Et3N added and stirred 5 min; then 40, HOBt, EDC added; quenched with sat. NaHCO3 (20 mL); extracted CH2Cl2 (15 mL + 2×10 mL); washed brine; dried Na2SO4; purified by column chromatography"
          },
          "product": {
            "compound_id": null,
            "name": "Boc-hydroxyproline-cyanopyrrolidine amide 43",
            "yield": "230 mg (57%)",
            "purity": "LC-MS purity 97.7%, m/z 210.1 ([M-Boc+H]+)",
            "molar_activity": null,
            "characterization": ["1H NMR", "LC-MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {"adduct": "[M-Boc+H]+", "mz": 210.1}
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica (0→3.33→100% MeOH/CH2Cl2)",
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "tosylation of hydroxyl group",
          "reactants": [
            {
              "compound_id": null,
              "name": "Boc-hydroxyproline-cyanopyrrolidine amide 43",
              "amount": "200 mg (0.65 mmol)"
            }
          ],
          "reagents": [
            {
              "name": "p-toluenesulfonyl chloride",
              "amount": "271 mg (1.42 mmol, 2.2 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "pyridine",
              "volume": "1.4 mL"
            }
          ],
          "conditions": {
            "temperature": "20 °C",
            "time": "20 h",
            "pressure": null,
            "atmosphere": "N2",
            "ph": null,
            "other": "diluted with water (30 mL); extracted with EtOAc (3×15 mL); washed brine; dried Na2SO4; evaporated; used crude"
          },
          "product": {
            "compound_id": null,
            "name": "tosylated linker-DPP4 pharmacophore building block 44",
            "yield": "310 mg (>100%, crude)",
            "purity": null,
            "molar_activity": null,
            "characterization": ["1H NMR"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "used without further purification",
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "nucleophilic coupling (SN2 with phenol 19a)",
          "reactants": [
            {
              "compound_id": "C26",
              "name": "phenol intermediate 19a",
              "amount": "170 mg (0.31 mmol)"
            },
            {
              "compound_id": null,
              "name": "tosylate 44",
              "amount": "287 mg (0.62 mmol, 2.0 equiv)"
            }
          ],
          "reagents": [
            {
              "name": "Cs2CO3",
              "amount": "232 mg (0.71 mmol, 2.3 equiv)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "3.4 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C then 85 °C",
            "time": "16 h at 85 °C",
            "pressure": null,
            "atmosphere": "N2",
            "ph": null,
            "other": "diluted with water (40 mL); extracted with EtOAc (15 mL + 2×10 mL); washed brine; dried Na2SO4; concentrated; used crude"
          },
          "product": {
            "compound_id": null,
            "name": "coupled intermediate 45 (Boc/acetyl protected compound 36 precursor)",
            "yield": "350 mg (>100%, crude)",
            "purity": "LC-MS: m/z 740.3 (100%; [M(35Cl)-Boc+H]+)",
            "molar_activity": null,
            "characterization": ["LC-MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {"adduct": "[M(35Cl)-Boc+H]+", "mz": 740.3}
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "used directly without purification",
          "notes": null
        },
        {
          "step_number": 6,
          "reaction_type": "Boc deprotection then sugar deacetylation (sequential)",
          "reactants": [
            {
              "compound_id": null,
              "name": "coupled intermediate 45",
              "amount": "300 mg (0.36 mmol)"
            }
          ],
          "reagents": [
            {
              "name": "TFA",
              "amount": "1.16 g (0.75 mL)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "3 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "1.5 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "concentrated; coevaporated with CH2Cl2 (3×5 mL); residual yellow oil then dissolved in 7 M NH3/MeOH (6.0 mL) and stirred at 15 °C for 7 h in sealed vessel for deacetylation; volatiles removed; coevaporated with MeOH (3×5 mL)"
          },
          "product": {
            "compound_id": "C51",
            "name": "compound 36",
            "yield": "30 mg (17% over three steps from 19a)",
            "purity": "HPLC purity 92.0%; LC-MS purity 88.9%, m/z 572.2 (100%; [M(35Cl)+H]+)",
            "molar_activity": null,
            "characterization": ["1H NMR", "HPLC", "LC-MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {"adduct": "[M(35Cl)+H]+", "mz": 572.2},
                {"adduct": "[M(37Cl)+H]+", "mz": 574.3}
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "preparative HPLC: Waters XBridge BEH C18 (100×30 mm, 10 μm); mobile phase A = 10 mM NH4HCO3, B = MeCN; gradient 10-30% B over 10 min",
          "notes": "Note: <95% HPLC purity; compound 36 not critical to SAR discussion. Three-step yield from 19a."
        }
      ]
    }
  ]
}
```

##### Evaluation
- First, I can see a pattern in compound: `log_p` is not use, and it introduce some of new information about `physicochemical_properties`. The cause is that the bias from the first paper.
- The paper have too much compound so that Claude can not extract full information.

#### Prompt optimization

Now I will optimize my prompt. First, I gonna read and collect some paper that can help me to improve my prompt.

**1. PRISM / Persona research (Hu et al., 2026 — USC)**
The PRISM authors recommend: "When you care more about alignment (safety, rules, structure-following), be specific about your requirement; if you care more about accuracy and facts, do not add anything."

**2. Chain-of-Thought + Schema Design (Instructor benchmarks, 2024)**
[Bad Schemas could break your LLM Structured Outputs - Instructor](https://python.useinstructor.com/blog/2024/09/26/bad-schemas-could-break-your-llm-structured-outputs/#chain-of-thought)
Simply adding additional fields for the model to reason about its final response improves reasoning all around.

### v3.0 Prompt.

Based on these two papers, I will remove the "You are an expert" and narrow my scope to only synthesis, the old prompt focus in all information of chemistry.

```
SYSTEM ROLE
You are a chemical synthesis extraction engine. Your sole task is to extract synthesis procedures, reaction conditions, compound preparation data, and directly related characterisation data from the academic paper provided. You do NOT extract biological assay results, pharmacological properties, computational docking scores, or biodistribution data UNLESS they appear within the experimental/synthesis section itself and pertain directly to a synthesised compound's identity or purity. This scope restriction is absolute.

Your primary obligation is fidelity to the source text over completeness of any individual field. If a value is absent, record null. Never invent, infer, or supplement with prior chemical knowledge.

---

CRITICAL RULES — read before answering

RULE 1 — SYNTHESIS SCOPE ONLY
This prompt extracts only compounds that participate in a synthesis procedure.

Include in compounds[]:
- Any compound that is a reactant, reagent, solvent source, or product in at least one synthesis step.
- Radionuclide/metal sources used directly in radiolabeling or chelation steps.
- Buffers and pH-adjustment solutions used in a synthesis or radiolabeling step.
- Catalysts, bases, and coupling reagents named with an amount in a step.

Exclude from compounds[] (out of scope):
- Compounds that appear only in biological assay sections (cell lines, receptors, antibodies).
- Reference compounds used only in competitive binding or IC50 assays with no synthetic role.
- Commercial kits, cell culture reagents, or radiopharmaceutical QC standards that are never substrates or products in a synthesis step.
- Any compound whose first and only appearance is in a figure legend describing a biological result.

RULE 2 — ARTICLE-ONLY
Extract exclusively from the provided text (main text, schemes, figures, tables, captions, experimental section). If details are in Supporting Information not provided, record null for those fields and note the SI reference in the step's notes field. Do NOT supplement with prior chemical knowledge.

RULE 3 — NULL FOR ABSENT DATA
If a field value is absent from the article, use null. Never invent plausible values.

RULE 4 — NEGATIVE CASE
If the paper contains no synthesis, return valid JSON with has_synthesis: false and all synthesis arrays empty.

RULE 5 — YIELD FORMAT
Use "N mg (N%)" when both mass and percentage are stated; "N%" when only a percentage is given. For radiochemical yields, append the RCY suffix: "89.55 ± 0.12% RCY". ONE compound per yield string — never concatenate multiple compounds into a single yield field.

RULE 6 — AMOUNTS FORMAT
Express amounts as "N unit (N unit)" for mass + moles (e.g. "6.4 mg (3 μmol)"). Use an en dash for ranges: "0.74–1.11 GBq". Never append solvent or concentration context into the amount string — those go in the solvents array or the reagent's amount field respectively.

RULE 7 — COMPOUND ID ORDERING
Assign IDs (C01, C02, C03, …) strictly by order of first appearance in the paper, reading top-to-bottom, left-to-right, section by section:
  a. Title / abstract → assigned first
  b. Introduction → next
  c. Results / Chemistry section → next
  d. Experimental section → last
  e. Within a single sentence listing multiple compounds: left to right

Rules: no skipped IDs, no reused IDs, no merged entries. New reagents/buffers/radionuclides introduced in a step receive IDs at that point in document order.

IMPORTANT for v3.0: ID assignment is restricted to in-scope compounds (Rule 1). Out-of-scope compounds are silently ignored — their absence does not create gaps because they were never assigned IDs.

RULE 8 — ROLE ASSIGNMENT
Use this decision tree in strict order:

1. Contains a radioisotope, produced in a radiolabeling step → radiolabeled_product (overrides all)
2. Sourced externally (commercial/custom), used as substrate or precursor → starting_material
3. Sourced externally, used as consumable reagent (activating agent, chelator, base, buffer, radionuclide source) → reagent
4. Synthesised in-house, sole purpose is input to a subsequent transformation (including radiolabeling) → intermediate
5. Synthesised in-house or externally, evaluated as a standalone pharmacological deliverable, no radioisotope → final_product
6. Metal, ligand, or co-ligand in a coordination context → catalyst or coligand

Key distinctions:
- A compound is intermediate ONLY if made in-house in this study. An externally synthesised precursor used in radiolabeling is starting_material, not intermediate.
- radiolabeled_product always overrides final_product. If a compound contains a radioisotope and was produced in a radiolabeling step, it is radiolabeled_product regardless of how extensively it is evaluated.

RULE 9 — is_newly_synthesized
Set to true only for compounds prepared in-house during this study. Set to false for all commercially purchased, custom-ordered, or externally synthesised compounds, regardless of whether the structure is novel.

RULE 10 — method_completeness
Choose exactly one value:
- "full" — complete procedure in main text for all in-scope compounds
- "partial" — at least one in-house procedure in main text; others in SI or unavailable
- "referenced_to_SI" — main text gives no procedural detail at all; all routes in SI only
- "none" — no synthesis reported

RULE 11 — STEP GRANULARITY
Each physically distinct operation requiring its own materials list is a separate numbered step. Indicators of a new step: different equipment, different reagents, different conditions, different vessel. Examples:
- QMA trapping and Al18F complexation are separate steps.
- pH adjustment of a radionuclide solution and the subsequent chelation reaction are separate steps.
- Solid-phase resin loading and each coupling cycle are separate steps.
- Elution from a cartridge and the subsequent reaction are separate steps.

RULE 12 — INTERMEDIATE PRODUCTS IN MULTI-STEP SEQUENCES
The product block of every step must describe what is produced by that step, even if it is a transient intermediate. For transient intermediates with no standalone compound entry, use "compound_id": null and give a descriptive name. Never recycle a reactant's compound_id as the product of the same step.

RULE 13 — REAGENT vs CONDITIONS
- The pH of the reaction mixture goes in conditions.ph.
- The concentration and pH of a reagent solution go in the reagent's amount field: "0.5 mL (0.25 M, pH 6.5)".
- Never duplicate: if a value is in the reagent amount field, do not also put it in conditions.

RULE 14 — PURITY FORMAT
Always include the analytical method: ">95% by HPLC" for non-radioactive compounds; ">95% RCP by radio-HPLC" for radiolabeled products.

RULE 15 — TEMPERATURE FORMAT
Use SI convention with a space: "95 °C", "-20 °C", "room temperature". Never "95°C".

RULE 16 — HPLC RETENTION TIME
Record as a number in minutes in product.hplc_retention_time_min. Include if reported in any characterisation section for a synthesised compound.

RULE 17 — MS DATA
Record the calculated mass exactly as stated in the paper. For large peptides where authors use average or nominal masses, note in paper.extraction_notes. Do not correct or recalculate.

RULE 18 — ONE ENTRY PER COMPOUND
Each distinct substance gets exactly one compound entry and one ID. Do not skip IDs, do not reuse them, do not merge two substances into one entry.

RULE 19 — NO CITATION ARTIFACTS
All string values must be plain prose. Strip citation tags, reference numbers, footnote markers, and retrieval-system metadata from all fields.

RULE 20 — ONE PATHWAY PER TARGET COMPOUND
Each synthesis pathway (P1, P2, …) targets exactly one compound. Never describe two distinct synthetic routes in one pathway entry using "or" / "alternatively" logic.

RULE 21 — PHYSICOCHEMICAL PROPERTIES (SYNTHESIS-SCOPED)
Record only properties that appear in the experimental/synthesis section or that directly characterise a synthesised compound's identity, purity, or radiolabeling outcome:
- Log P (if measured for a radiolabeled product as part of its characterisation)
- HPLC retention time and purity
- MS data (exact mass, observed ions)
- Molar activity (for radiolabeled products)
- Radiochemical purity (RCP)

Do NOT extract in this prompt: KD, Bmax, IC50, docking scores, tumor uptake (%ID/g), T/NT ratios, blood T½. These are biological data outside synthesis scope for v3.0.

RULE 22 — CONSISTENCY GATE (MANDATORY PRE-OUTPUT CHECK)
Before emitting the final JSON, verify each of the following and fix any failures:

  a. Every compound_id referenced in any synthesis pathway step (reactants, reagents, product.compound_id) has a matching entry in compounds[].
  b. Every target_compound_id in a pathway has a matching entry in compounds[].
  c. No two compound entries share the same id value.
  d. Compound IDs form a contiguous sequence from C01 to the highest assigned ID, with no gaps.
  e. A compound_id used as a reactant input in step N does NOT appear as product.compound_id of the same step N.
  f. For every radiolabeled_product entry, log_p is populated if the paper reports it; otherwise null.
  g. All compounds in compounds[] satisfy Rule 1 (synthesis scope). Remove any that do not.

---

EXECUTION PROTOCOL — 3 PHASES

PHASE 1 — SCAN PASS
Before filling any JSON field, perform a scan of the document and identify:
1. Which sections contain synthesis procedures (Methods, Experimental, Schemes, Chemistry section)?
2. How many synthesis pathways are described?
3. What is the set of compounds that are within synthesis scope (Rule 1)?
4. Are there Supporting Information references for procedural details not in the main text?

Record this scan summary in extraction.extractor_notes. This phase prevents extracting compounds that appear only in biology sections.

PHASE 2 — COMPOUND INVENTORY
Build the compounds[] array before filling any synthesis steps. Assign IDs in document order (Rule 7), restricted to in-scope compounds only. For each compound, resolve: role, is_newly_synthesized, source.

PHASE 3 — PATHWAY EXTRACTION
For each synthesis pathway, fill steps sequentially. Apply Rule 12 strictly (every step has a product block). Run the Consistency Gate (Rule 22) before emitting the final JSON.

---

OUTPUT SCHEMA

Return a single JSON object. Do not add any text before or after the JSON.

{
  "extraction": {
    "prompt_version": "v3.0",
    "extraction_date": "YYYY-MM-DD",
    "model_name": "string — name and version of the model used for this extraction",
    "extractor_notes": "string or null — scan-pass summary: sections identified, number of pathways, SI references, scope decisions (which compounds were excluded per Rule 1 and why), mass type notes (monoisotopic vs nominal for large peptides), any ambiguities"
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
    "extraction_notes": "string or null — paper-specific observations: unusual reporting conventions, missing SI, discrepancies in the source text, notes on average vs monoisotopic masses, note if large numbers of biological-only compounds were excluded from scope"
  },

  "compounds": [
    {
      "id": "C01",
      "name": "string",
      "iupac_name": "string or null — only if explicitly stated in the paper",
      "molecular_formula": "string or null — only if explicitly stated",
      "role": "starting_material | intermediate | reagent | catalyst | coligand | radiolabeled_product | final_product",
      "is_newly_synthesized": true,
      "source": "string or null — in-house, commercial supplier name, or vendor if stated",
      "physicochemical_properties": {
        "log_p": "string or null — radiolabeled products only, if reported in experimental section",
        "other": "string or null — synthesis-relevant properties only: HPLC retention time, purity by HPLC or radio-HPLC, molar activity, RCP; semicolon-separated"
      },
      "description": "one sentence of plain prose describing this compound's synthetic role in the study"
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
          "reaction_type": "string or null — e.g. amide coupling, reductive amination, radiolabeling, solid-phase peptide synthesis, click chemistry",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "string",
              "amount": "string or null"
            }
          ],
          "reagents": [
            {
              "compound_id": "string or null — C-ID if reagent has a compound entry; null otherwise",
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
            "purity": "string or null — include analytical method, e.g. >95% by HPLC",
            "molar_activity": "string or null — radiolabeled products only",
            "characterization": ["string — e.g. ESI-MS, HPLC, NMR, radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": "number or null",
              "formula": "string or null",
              "observed_ions": [
                {
                  "adduct": "string — e.g. [M+H]+, [M+2H]2+",
                  "mz": "number or null"
                }
              ]
            },
            "hplc_retention_time_min": "number or null"
          },
          "purification": "string or null — method (e.g. SPE, semi-prep HPLC), cartridge type or catalog number if given, elution solvent and volume, post-purification formulation steps",
          "notes": "string or null — SI references, vessel and equipment details, replication count (n=), any procedural context not captured in the structured fields above"
        }
      ]
    }
  ]
}
```

##### Claude Paper 1 
```
{
  "extraction": {
    "prompt_version": "v3.0",
    "extraction_date": "2026-03-28",
    "model_name": "claude-sonnet-4-6",
    "extractor_notes": "PHASE 1 SCAN: Synthesis procedures are found in Section 5.2 (Chemistry) of the main text and in Schemes S1–S5 of the Supporting Information (SI). Section 5.4 (Preparation of Radioligands) contains radiolabeling procedures. Two classes of synthesis are described: (1) solution-phase conjugation of PR7 with DOTA-NHS or NOTA-NHS to give DP1 and NP1, respectively (Section 5.2.1, Scheme S5, full detail in main text); (2) SPPS-based synthesis of PR7, DP2, DP3, and NP2 (Schemes S1–S4 in SI; Section 5.2.2 of main text states these were custom-synthesized externally by Nanchang Tanzhen Biotechnology Co., Ltd.). Radiolabeling of three 68Ga tracers (Section 5.4) and two 18F tracers (Section 5.4) are described in full in the main text. Total synthesis pathways identified: P1 (DP1 synthesis), P2 (NP1 synthesis), P3 ([68Ga]Ga-DP1/DP2/DP3 radiolabeling — three separate radiolabeled products but using essentially the same procedure applied to three different precursors; split into P3, P4, P5), P6 ([18F]AlF-NP1 radiolabeling), P7 ([18F]AlF-NP2 radiolabeling). PR7, DP2, DP3, NP2 syntheses are referenced to SI Schemes S1–S4 but the actual execution was by an external CRO; these are treated as starting_material/externally synthesized. SPPS reagents (Fmoc amino acids, resins, coupling reagents, piperidine, TFA, etc.) appear only in Scheme diagrams in the SI with no quantitative amounts given; they are excluded per Rule 1 because no amounts are stated for them in accessible text and they are components of externally executed synthesis. DIPEA and DMSO used in the DP1/NP1 conjugation step have amounts stated (20 µL DIPEA, 400 µL DMSO) and are in-scope. Mass type note: all masses reported are labeled 'calcd' exact masses in the experimental section and SI scheme boxes; for large peptides (MW 2100–3015 Da) these are monoisotopic exact masses as stated by the authors. Compounds excluded from scope: cell lines (MC38, B16F10, A549, HepG2), antibodies, kit reagents, Western blot reagents, transcriptomics reagents — all appear only in biological/analytical sections with no synthetic role. 1-octanol and PBS used only in log P measurement (physicochemical characterization, not synthesis) are excluded. Fetal bovine serum and CH3CN/TFA used only in stability assay are excluded."
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
    "extraction_notes": "Full procedural detail is provided in the main text for the DP1/NP1 conjugation (Section 5.2.1) and for all five radiolabeling reactions (Section 5.4). The syntheses of PR7, DP2, DP3, and NP2 are referenced to Schemes S1–S4 in the SI, but these compounds were actually custom-synthesized externally by Nanchang Tanzhen Biotechnology Co., Ltd. and are therefore classified as starting_materials with is_newly_synthesized: false. The SI Schemes show SPPS routes with Fmoc amino acid sequences, resins, and reagents, but no amounts are given for these steps. MS data are reported as exact masses (monoisotopic) as explicitly labeled 'calcd' in the paper, consistent with the molecular formulas given; this is appropriate for peptides in the 2100–3015 Da range. The paper reports a discrepancy in Table S1 vs. main text for [68Ga]Ga-DP3 log P: main text states −1.82 ± 0.03, Table S1 also states −1.82 ± 0.03 — consistent. Molar activity and RCY data are from Section 2.2 and Table S1 (SI); both sources are consistent. Large numbers of biological-only compounds (cell lines, antibodies, assay reagents) were excluded from scope per Rule 1."
  },

  "compounds": [
    {
      "id": "C01",
      "name": "PR7",
      "iupac_name": null,
      "molecular_formula": "C96H133N25O31",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesized)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.642 min; >95% pure by HPLC (mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 23% B to 43% B over 20 min, 1 mL/min)"
      },
      "description": "ROR1-targeting linear peptide scaffold (lead compound) used as the substrate for conjugation with DOTA-NHS or NOTA-NHS to produce DP1 and NP1, respectively."
    },
    {
      "id": "C02",
      "name": "DOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesized)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "N-hydroxysuccinimide ester of DOTA used as the activated chelator for conjugation to the amine of PR7 to produce DP1."
    },
    {
      "id": "C03",
      "name": "NOTA-NHS",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesized)",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "N-hydroxysuccinimide ester of NOTA used as the activated chelator for conjugation to the amine of PR7 to produce NP1."
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
      "description": "Diisopropylethylamine used as a non-nucleophilic base in the conjugation reactions for synthesis of DP1 and NP1."
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
        "other": "HPLC retention time: 11.230 min; >95% pure by HPLC (mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B to 95% B over 20 min, 1 mL/min)"
      },
      "description": "DOTA-conjugated linear ROR1-targeting peptide precursor synthesized from PR7 and DOTA-NHS, used as the precursor for 68Ga radiolabeling to produce [68Ga]Ga-DP1."
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
        "other": "HPLC retention time: 12.780 min; >95% pure by HPLC (mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B to 95% B over 20 min, 1 mL/min)"
      },
      "description": "NOTA-conjugated linear ROR1-targeting peptide precursor synthesized from PR7 and NOTA-NHS, used as the precursor for 18F AlF radiolabeling to produce [18F]AlF-NP1."
    },
    {
      "id": "C07",
      "name": "DP2",
      "iupac_name": null,
      "molecular_formula": "C122H174N32O41",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesized)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.328 min; >95% pure by HPLC (mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 23% B to 43% B over 20 min, 1 mL/min)"
      },
      "description": "DOTA-conjugated cyclic ROR1-targeting peptide precursor (custom synthesized externally) used as the substrate for 68Ga radiolabeling to produce [68Ga]Ga-DP2."
    },
    {
      "id": "C08",
      "name": "DP3",
      "iupac_name": null,
      "molecular_formula": "C133H186N32O43S3",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesized)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.404 min; >95% pure by HPLC (mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 23% B to 43% B over 20 min, 1 mL/min)"
      },
      "description": "DOTA-conjugated cyclic ROR1-targeting peptide precursor containing disulfide-cyclized architecture (custom synthesized externally) used as the substrate for 68Ga radiolabeling to produce [68Ga]Ga-DP3."
    },
    {
      "id": "C09",
      "name": "NP2",
      "iupac_name": null,
      "molecular_formula": "C118H167N31O39",
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Nanchang Tanzhen Biotechnology Co., Ltd. (custom synthesized)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC retention time: 10.620 min; >95% pure by HPLC (mobile phase: 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 23% B to 43% B over 20 min, 1 mL/min)"
      },
      "description": "NOTA-conjugated cyclic ROR1-targeting peptide precursor (custom synthesized externally) used as the substrate for 18F AlF radiolabeling to produce [18F]AlF-NP2."
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
      "description": "Gallium-68 chloride solution used as the radionuclide source for radiolabeling of DOTA-conjugated peptide precursors DP1, DP2, and DP3."
    },
    {
      "id": "C11",
      "name": "Sodium acetate solution",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Aqueous sodium acetate buffer used to adjust the pH of the 68GaCl3 solution to pH 4–4.5 prior to the 68Ga chelation radiolabeling step."
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
        "other": "RCY: 89.55 ± 0.12% RCY; RCP: 92.56 ± 0.02% by radio-HPLC; molar activity: 14.37 ± 0.97 GBq/µmol (n ≥ 3); HPLC retention time: 12.26 ± 0.03 min"
      },
      "description": "68Ga-radiolabeled DOTA-conjugated linear ROR1-targeting radiotracer produced by chelation of 68GaCl3 with precursor DP1, the primary 68Ga candidate evaluated for PET imaging."
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
        "other": "RCY: 97.67 ± 1.05% RCY; RCP: 99.45 ± 0.01% by radio-HPLC; molar activity: 20.05 ± 1.35 GBq/µmol (n ≥ 3); HPLC retention time: 11.22 ± 0.03 min"
      },
      "description": "68Ga-radiolabeled DOTA-conjugated cyclic ROR1-targeting radiotracer produced by chelation of 68GaCl3 with precursor DP2."
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
        "other": "RCY: 98.01 ± 0.97% RCY; RCP: 98.46 ± 0.05% by radio-HPLC; molar activity: 14.09 ± 2.12 GBq/µmol (n ≥ 3); HPLC retention time: 12.48 ± 0.04 min"
      },
      "description": "68Ga-radiolabeled DOTA-conjugated disulfide-cyclized ROR1-targeting radiotracer produced by chelation of 68GaCl3 with precursor DP3."
    },
    {
      "id": "C15",
      "name": "Fluoride-18 ([18F]fluoride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Cyclone 18/9 cyclotron (IBA, Belgium), Center for Molecular Imaging and Translational Medicine, Xiamen University",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Fluorine-18 produced by the 18O(p,n)18F reaction, used as the radionuclide source for AlF-mediated 18F radiolabeling of NOTA-conjugated peptide precursors NP1 and NP2."
    },
    {
      "id": "C16",
      "name": "QMA cartridge",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Quaternary methyl ammonium (QMA) solid-phase extraction cartridge used to trap and concentrate [18F]fluoride from the cyclotron target water before elution into the radiolabeling vial."
    },
    {
      "id": "C17",
      "name": "Aluminum chloride solution (AlCl3 in sodium acetate buffer)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Aluminum(III) chloride dissolved in sodium acetate buffer used as the aluminum source to form the Al18F complex in the AlF-chelation radiolabeling of NOTA-peptide precursors NP1 and NP2."
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
        "other": "RCY: 62.58 ± 0.32% RCY; RCP: 99.46 ± 0.15% by radio-HPLC; molar activity: 13.13 ± 1.71 GBq/µmol (n ≥ 3); HPLC retention time: 12.93 ± 0.01 min"
      },
      "description": "18F-radiolabeled AlF-NOTA-conjugated linear ROR1-targeting radiotracer produced by Al18F chelation with precursor NP1, the primary 18F candidate evaluated for PET imaging."
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
        "other": "RCY: 62.76 ± 0.22% RCY; RCP: 99.56 ± 0.04% by radio-HPLC; molar activity: 13.42 ± 1.25 GBq/µmol (n ≥ 3); HPLC retention time: 11.30 ± 0.01 min"
      },
      "description": "18F-radiolabeled AlF-NOTA-conjugated cyclic ROR1-targeting radiotracer produced by Al18F chelation with precursor NP2."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Synthesis of DP1 (PR7-DOTA conjugate)",
      "target_compound_id": "C05",
      "target_compound_name": "DP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide coupling (NHS ester conjugation)",
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
            "temperature": "room temperature",
            "time": "12 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "agitated in an oscillator; reaction performed in a 2 mL centrifugation tube"
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
          "purification": "Semipreparative HPLC with UV detection at 254 nm; product obtained after lyophilization",
          "notes": "Synthetic route also shown in Scheme S5 of the Supporting Information. The same reaction vessel and conditions were used in parallel for NP1 synthesis (P2) with NOTA-NHS replacing DOTA-NHS."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of NP1 (PR7-NOTA conjugate)",
      "target_compound_id": "C06",
      "target_compound_name": "NP1",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "amide coupling (NHS ester conjugation)",
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
            "temperature": "room temperature",
            "time": "12 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "agitated in an oscillator; reaction performed in a 2 mL centrifugation tube"
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
          "purification": "Semipreparative HPLC with UV detection at 254 nm; product obtained after lyophilization",
          "notes": "Synthetic route also shown in Scheme S5 of the Supporting Information."
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
              "compound_id": "C11",
              "name": "Sodium acetate (0.25 M in water, pH 6.5)",
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
          "reaction_type": "radiometal chelation (68Ga labeling)",
          "reactants": [
            {
              "compound_id": null,
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL total (from Step 1)"
            },
            {
              "compound_id": "C05",
              "name": "DP1 (precursor)",
              "amount": "50 µg (16–20 nmol, in 50 µL DMSO)"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 µL (for precursor dissolution)"
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
            "molar_activity": "14.37 ± 0.97 GBq/µmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": 12.26
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL ethanol; ethanol solvent retained (no evaporation step described for 68Ga products); final product formulated in eluate",
          "notes": "n ≥ 3 preparations. Radio-HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B to 95% B over 20 min, 1 mL/min. RCY, RCP, and molar activity also summarized in Table S1 of the Supporting Information."
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
              "compound_id": "C11",
              "name": "Sodium acetate (0.25 M in water, pH 6.5)",
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
          "reaction_type": "radiometal chelation (68Ga labeling)",
          "reactants": [
            {
              "compound_id": null,
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL total (from Step 1)"
            },
            {
              "compound_id": "C07",
              "name": "DP2 (precursor)",
              "amount": "50 µg (16–20 nmol, in 50 µL DMSO)"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 µL (for precursor dissolution)"
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
            "molar_activity": "20.05 ± 1.35 GBq/µmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": 11.22
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL ethanol",
          "notes": "n ≥ 3 preparations. Same procedure as P3 but using DP2 precursor."
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
              "compound_id": "C11",
              "name": "Sodium acetate (0.25 M in water, pH 6.5)",
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
          "reaction_type": "radiometal chelation (68Ga labeling)",
          "reactants": [
            {
              "compound_id": null,
              "name": "68GaCl3–sodium acetate solution (pH 4–4.5)",
              "amount": "1.5 mL total (from Step 1)"
            },
            {
              "compound_id": "C08",
              "name": "DP3 (precursor)",
              "amount": "50 µg (16–20 nmol, in 50 µL DMSO)"
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "50 µL (for precursor dissolution)"
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
            "molar_activity": "14.09 ± 2.12 GBq/µmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": 12.48
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL ethanol",
          "notes": "n ≥ 3 preparations. Same procedure as P3 but using DP3 precursor."
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
          "reaction_type": "solid-phase trapping of [18F]fluoride on QMA cartridge",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "Fluoride-18",
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
            "other": "fluoride-18 solution passed through preconditioned QMA cartridge"
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
          "reaction_type": "elution of [18F]fluoride from QMA cartridge",
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
            "other": "eluted into a vial pre-loaded with AlCl3 solution, acetonitrile, sodium acetate buffer, and precursor"
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride eluate in reaction vial",
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
          "notes": "Vial pre-loaded with: 3 µL of 2 mM AlCl3 in sodium acetate buffer (0.1 M, pH 4.0), 200 µL acetonitrile, 100 µL sodium acetate buffer (0.1 M, pH 4.0), and 50 µg (18–25 nmol) NP1 precursor in 50 µL DMSO."
        },
        {
          "step_number": 3,
          "reaction_type": "Al18F chelation radiolabeling",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride eluate in reaction vial (from Step 2)",
              "amount": null
            },
            {
              "compound_id": "C06",
              "name": "NP1 (precursor)",
              "amount": "50 µg (18–25 nmol, in 50 µL DMSO)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C17",
              "name": "Aluminum chloride (AlCl3) in sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "3 µL (2 mM)",
              "role": "chelation_catalyst"
            },
            {
              "compound_id": "C11",
              "name": "Sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "100 µL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": "200 µL"
            },
            {
              "name": "DMSO",
              "volume": "50 µL (for precursor dissolution)"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "cooled to room temperature after reaction"
          },
          "product": {
            "compound_id": "C18",
            "name": "[18F]AlF-NP1",
            "yield": "62.58 ± 0.32% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "13.13 ± 1.71 GBq/µmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": 12.93
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL ethanol; ethanol solvent removed; final product resolved in saline",
          "notes": "n ≥ 3 preparations. Radio-HPLC method: mobile phase 0.1% TFA in water (A) and 0.1% TFA in acetonitrile (B); 5% B to 95% B over 20 min, 1 mL/min. RCY, RCP, and molar activity also summarized in Table S1 of the Supporting Information."
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
          "reaction_type": "solid-phase trapping of [18F]fluoride on QMA cartridge",
          "reactants": [
            {
              "compound_id": "C15",
              "name": "Fluoride-18",
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
            "other": "fluoride-18 solution passed through preconditioned QMA cartridge"
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
          "reaction_type": "elution of [18F]fluoride from QMA cartridge",
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
            "other": "eluted into a vial pre-loaded with AlCl3 solution, acetonitrile, sodium acetate buffer, and precursor"
          },
          "product": {
            "compound_id": null,
            "name": "[18F]fluoride eluate in reaction vial",
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
          "notes": "Vial pre-loaded with: 3 µL of 2 mM AlCl3 in sodium acetate buffer (0.1 M, pH 4.0), 200 µL acetonitrile, 100 µL sodium acetate buffer (0.1 M, pH 4.0), and 50 µg (18–25 nmol) NP2 precursor in 50 µL DMSO."
        },
        {
          "step_number": 3,
          "reaction_type": "Al18F chelation radiolabeling",
          "reactants": [
            {
              "compound_id": null,
              "name": "[18F]fluoride eluate in reaction vial (from Step 2)",
              "amount": null
            },
            {
              "compound_id": "C09",
              "name": "NP2 (precursor)",
              "amount": "50 µg (18–25 nmol, in 50 µL DMSO)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C17",
              "name": "Aluminum chloride (AlCl3) in sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "3 µL (2 mM)",
              "role": "chelation_catalyst"
            },
            {
              "compound_id": "C11",
              "name": "Sodium acetate buffer (0.1 M, pH 4.0)",
              "amount": "100 µL",
              "role": "ph_adjuster"
            }
          ],
          "solvents": [
            {
              "name": "acetonitrile",
              "volume": "200 µL"
            },
            {
              "name": "DMSO",
              "volume": "50 µL (for precursor dissolution)"
            }
          ],
          "conditions": {
            "temperature": "100 °C",
            "time": "20 min",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "cooled to room temperature after reaction"
          },
          "product": {
            "compound_id": "C19",
            "name": "[18F]AlF-NP2",
            "yield": "62.76 ± 0.22% RCY",
            "purity": ">95% RCP by radio-HPLC",
            "molar_activity": "13.42 ± 1.25 GBq/µmol (n ≥ 3)",
            "characterization": ["radio-HPLC"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": 11.30
          },
          "purification": "SepPak C18 cartridge (WAT020515, Waters); eluted with 1.5 mL ethanol; ethanol solvent removed; final product resolved in saline",
          "notes": "n ≥ 3 preparations. Same procedure as P6 but using NP2 precursor."
        }
      ]
    }
  ]
}
```

##### Claude Paper 2 Scheme 1
```
{
  "extraction": {
    "prompt_version": "v3.0",
    "extraction_date": "2026-03-28",
    "model_name": "claude-sonnet-4-6",
    "extractor_notes": "PHASE 1 SCAN: The paper contains an extensive medicinal chemistry synthesis campaign spanning Schemes 1–9 (main text) plus Schemes S1–S4 (Supporting Information). The user requested extraction of ONE scheme only; Scheme 1 was selected as the central general synthetic route. Scheme 1 describes six transformations (steps a–f) converting acetyl-protected dapagliflozin 18a into triple inhibitor targets via: (a) BBr3 dealkylation to phenol 19a; (b) Mitsunobu or SN2 coupling of 19a with Boc-linker building blocks 20a–l to give 21a–l; (c) TFA Boc deprotection to ammonium salts 22a–l; (d) N-alkylation with alkylating agent 23a to give protected intermediates 24a–l (Route 1) or direct deprotection then N-alkylation in Route 2; (e) deacetylation of the sugar with NH3/MeOH to give final deprotected compounds 26–38, 46–50 (Route 1); (f) HCl/MeOH final acid deprotection (Route 2 only). The representative compound traced through all steps is 27 (gem-dimethyl C4 linker, first identified lead). Compound 18a is described as 'tetraacetyl dapagliflozin' and treated as a commercially sourced/known starting material (the patent literature synthesis for the dapagliflozin intermediate 71 is referenced). Compounds 20a–l are either commercially available or prepared by tosylation (general procedure in experimental); for Scheme 1 tracing, 20b (the gem-dimethyl C4 linker alcohol, commercially available) is used for compound 27. Alkylating agent 23a ((S)-2-(chloroacetyl)pyrrolidine-2-carbonitrile) is used without a synthesis being described in the main text — it is treated as a reagent of unstated source (likely commercial or from SI). Compounds 23b–d and 58 are in-house synthesized (Scheme 3 for 23c and 58) or sourced commercially (23d). Scope decisions: excluded all biological-only comparators (dapagliflozin 2, sotagliflozin 6, linagliptin, etc.) that have no synthetic role in Scheme 1. All compounds in Scheme 1 scope are included. Many compounds (26–38, 46–50) are produced via the same steps and are listed only insofar as relevant to the exemplary route to 27. SI contains full tables of intermediates (Tables S1–S7) but Scheme 1 procedure is fully described in main text for 19a, 21b, 22b, 24b, and 27."
  },

  "paper": {
    "title": "Design, Optimization, and Biological Evaluation of First-in-Class Triple Inhibitors of SGLT1, SGLT2, and DPP4 for Type 2 Diabetes Mellitus",
    "authors": [
      "Fernando de Souza Gama",
      "Marcos Ferreira",
      "Natanael Dante Segretti",
      "Mariana C. F. C. B. Damiao",
      "Cristiano R. W. Guimaraes",
      "Alessandra Mascarello",
      "Hatylas Azevedo"
    ],
    "doi": "10.1021/acs.jmedchem.5c02225",
    "journal": "Journal of Medicinal Chemistry",
    "year": 2025,
    "synthesis_scale": "lab",
    "mechanism_discussed": "synthetic",
    "method_completeness": "partial",
    "has_synthesis": true,
    "extraction_notes": "This paper contains nine numbered schemes in the main text and four in the SI. Only Scheme 1 is extracted per user instruction. Scheme 1 is a general multi-step route; specific quantities and full characterization are reported for 19a, representative Mitsunobu products (21b), Boc-deprotected amines (22b), N-alkylated intermediates (24b), and final deprotected target compounds (27). Intermediate structures for all Scheme 1 analogues are presented in Tables S1–S7 (SI, not provided). Alkylating agent 23a has no synthesis described in the main text; it is referenced by structure only and its source is not explicitly stated in the excerpted text. Yields are quoted 'over two steps' (combining N-alkylation and deacetylation) for Route 1 final compounds. All masses are consistent with small organic molecules; monoisotopic masses applicable."
  },

  "compounds": [
    {
      "id": "C01",
      "name": "Tetraacetyl dapagliflozin (18a)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Referenced as known compound derived from dapagliflozin via literature procedure",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "The fully acetyl-protected C-glycoside dapagliflozin derivative (18a) serving as the primary starting material for Scheme 1; has R1 = Cl, R2 = CH2OAc, R3 = OAc."
    },
    {
      "id": "C02",
      "name": "4-[tert-butyl(oxycarbonylamino)]-2-methyl-2-butanol linker precursor (20b)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Commercially available",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Boc-protected gem-dimethyl amino-alcohol linker building block 20b used in Mitsunobu coupling with phenol 19a to install the C4 gem-dimethyl linker."
    },
    {
      "id": "C03",
      "name": "(S)-2-(Chloroacetyl)pyrrolidine-2-carbonitrile (23a)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "Source not stated in main text",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "The chloroacetyl-2-cyanopyrrolidine alkylating agent 23a (Y = CH2, R5 = CN, R6 = H) used in Route 1 N-alkylation to install the 2-cyanopyrrolidine DPP4-targeting pharmacophore."
    },
    {
      "id": "C04",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-{4-chloro-3-[(p-hydroxyphenyl)methyl]phenyl}tetrahydro-2H-pyran-2-yl]methyl Acetate (19a)",
      "iupac_name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-{4-chloro-3-[(p-hydroxyphenyl)methyl]phenyl}tetrahydro-2H-pyran-2-yl]methyl Acetate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "In-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Purity 97.0% by HPLC; LC–MS purity 90.6%; m/z (ES) 566.2 (100%; [M(35Cl)+H2O]+), 568.2 (35%; [M(37Cl)+H2O]+)"
      },
      "description": "Free phenol intermediate 19a obtained by BBr3-mediated dealkylation of aryl ethyl ether 18a; serves as the central nucleophilic building block for linker attachment in Scheme 1."
    },
    {
      "id": "C05",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-{3-[(p-{4-[tert-butyl(oxycarbonylamino)]-4-methylpentyloxy}phenyl)methyl]-4-chlorophenyl}tetrahydro-2H-pyran-2-yl]methyl Acetate (21b)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "In-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "LC–MS purity 100.0%; m/z (ES) 634.2 (100%; [M(35Cl)−Boc+H]+), 636.2 (35%; [M(37Cl)−Boc+H]+)"
      },
      "description": "Boc-protected gem-dimethyl C4 linker-coupled Mitsunobu product 21b, bearing the acetyl-protected C-glycoside and intact Boc-amino group, produced by Mitsunobu coupling of 19a with alcohol 20b."
    },
    {
      "id": "C06",
      "name": "5-[p-({2-Chloro-5-[(2S,3S,4R,5R,6R)-3,4,5-triacetoxy-6-(acetoxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-2-methyl-2-pentanammonium Trifluoroacetate (22b)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "In-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "TFA salt of the free amine intermediate 22b obtained by TFA-mediated Boc deprotection of 21b; the unprotected amino group is required for subsequent N-alkylation."
    },
    {
      "id": "C07",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-(4-chloro-3-{[p-(4-{2-[(S)-2-cyano-1-pyrrolidinyl]-2-oxoethylamino}-4-methylpentyloxy)phenyl]methyl}phenyl)tetrahydro-2H-pyran-2-yl]methyl Acetate (24b)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "In-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "LC–MS purity 66.7%; m/z (ES) 784.3 (100%; [M(35Cl)+H]+), 786.3 (45%; [M(37Cl)+H]+)"
      },
      "description": "Sugar-acetyl-protected N-alkylated intermediate 24b bearing the 2-cyanopyrrolidine amide, produced by N-alkylation of amine 22b with chloroacetyl agent 23a; penultimate intermediate in Route 1 to compound 27."
    },
    {
      "id": "C08",
      "name": "(S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-2-pyrrolidinecarbonitrile (27)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "In-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Purity 100.0% by HPLC; LC–MS purity 100.0%; m/z (ES) 616.2 (100%; [M(35Cl)+H]+), 618.2 (40%; [M(37Cl)+H]+)"
      },
      "description": "Triple inhibitor lead compound 27, bearing the gem-dimethyl C4 linker and unprotected dapagliflozin-derived C-glycoside, obtained after NH3/MeOH deacetylation of 24b and preparative HPLC purification."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Scheme 1 — General Route to Triple SGLT1/SGLT2/DPP4 Inhibitor 27 (Route 1)",
      "target_compound_id": "C08",
      "target_compound_name": "Compound 27",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Aryl ether dealkylation (BBr3-mediated O-demethylation)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "Tetraacetyl dapagliflozin (18a)",
              "amount": "9.90 g (17.2 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Boron tribromide (BBr3)",
              "amount": "10 equiv in dry CH2Cl2",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Nitrogen (N2)",
              "amount": null,
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "Dichloromethane (CH2Cl2)",
              "volume": "235 mL total reaction volume"
            }
          ],
          "conditions": {
            "temperature": "−70 °C (addition), raised to −30 °C after 0.5 h",
            "time": "1–6 h (until complete by TLC or LC–MS)",
            "pressure": null,
            "atmosphere": "N2",
            "ph": null,
            "other": "After reaction, mixture poured onto ice, neutralized with sat. NaHCO3 (400 mL), layers separated; aqueous extracted twice with CH2Cl2; combined organics washed with brine, dried over Na2SO4, filtered, concentrated; crude purified by trituration with EtOAc/petroleum ether (1:5, 90 mL) at 25 °C for 0.5 h"
          },
          "product": {
            "compound_id": "C04",
            "name": "Phenol intermediate 19a",
            "yield": "8.80 g (93%)",
            "purity": "97.0% by HPLC",
            "molar_activity": null,
            "characterization": ["1H NMR", "HPLC", "LC–MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {
                  "adduct": "[M(35Cl)+H2O]+",
                  "mz": 566.2
                },
                {
                  "adduct": "[M(37Cl)+H2O]+",
                  "mz": 568.2
                }
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "Trituration with EtOAc/petroleum ether (1:5, 90 mL) at 25 °C for 0.5 h; obtained as white solid",
          "notes": "General procedure applies to all 18a–h analogues. Yield range across all examples: 67–95%. Scheme 1 label: step (a). Structures of all intermediates relating to Scheme 1 presented in Tables S1–S7 (SI)."
        },
        {
          "step_number": 2,
          "reaction_type": "Mitsunobu coupling (O-alkylation of phenol with Boc-amino alcohol)",
          "reactants": [
            {
              "compound_id": "C04",
              "name": "Phenol 19a",
              "amount": "170 mg (0.31 mmol)"
            },
            {
              "compound_id": "C02",
              "name": "Boc-amino alcohol 20b",
              "amount": "168 mg (0.77 mmol, 2.5 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Triphenylphosphine (PPh3)",
              "amount": "203 mg (0.77 mmol, 2.5 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Diisopropyl azodicarboxylate (DIAD)",
              "amount": "157 mg (151 μL, 0.77 mmol, 2.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "Tetrahydrofuran (THF)",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": "0–5 °C (DIAD addition), then 25 °C",
            "time": "20 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Crude purified by column chromatography on silica (12.5 → 17 → 22 → 100% EtOAc/petroleum ether) followed by preparative TLC (1:1 EtOAc/petroleum ether)"
          },
          "product": {
            "compound_id": "C05",
            "name": "Boc-protected linker intermediate 21b",
            "yield": "168 mg (73%)",
            "purity": "100.0% by LC–MS",
            "molar_activity": null,
            "characterization": ["1H NMR", "LC–MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {
                  "adduct": "[M(35Cl)−Boc+H]+",
                  "mz": 634.2
                },
                {
                  "adduct": "[M(37Cl)−Boc+H]+",
                  "mz": 636.2
                }
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "Column chromatography on silica (12.5 → 17 → 22 → 100% EtOAc/petroleum ether), followed by preparative TLC (1:1 EtOAc/petroleum ether); obtained as white solid",
          "notes": "General Mitsunobu procedure applies to alcohols 20a–n (Z = OH); alternatively, K2CO3/Cs2CO3 in DMF at 80–85 °C is used for tosylates (Z = OTs). Scheme 1 label: step (b). Yield range across all Mitsunobu examples: 57–95%."
        },
        {
          "step_number": 3,
          "reaction_type": "Boc deprotection (trifluoroacetic acid)",
          "reactants": [
            {
              "compound_id": "C05",
              "name": "Boc-protected intermediate 21b",
              "amount": "100 mg (0.13 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Trifluoroacetic acid (TFA)",
              "amount": "200 μL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "Dichloromethane (CH2Cl2)",
              "volume": "2.0 mL"
            }
          ],
          "conditions": {
            "temperature": "30 °C",
            "time": "2 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Crude material coevaporated with MeCN under reduced pressure to remove residual TFA; isolated as TFA salt"
          },
          "product": {
            "compound_id": "C06",
            "name": "Ammonium TFA salt 22b",
            "yield": "100 mg (98%)",
            "purity": null,
            "molar_activity": null,
            "characterization": ["1H NMR"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "Coevaporation with MeCN (×3) under reduced pressure; used directly in next step as crude TFA salt",
          "notes": "General Boc deprotection procedure (TFA, CH2Cl2, 15–30 °C, 1–4 h) applies to all 21a–l, 21o, 21p, 21s, 21t. Yield range: 41–100%. Scheme 1 label: step (c). All deprotected amines isolated as TFA salts."
        },
        {
          "step_number": 4,
          "reaction_type": "N-alkylation (SN2 with chloroacetyl 2-cyanopyrrolidine)",
          "reactants": [
            {
              "compound_id": "C06",
              "name": "Amine TFA salt 22b",
              "amount": "150 mg (0.20 mmol)"
            },
            {
              "compound_id": "C03",
              "name": "Alkylating agent 23a",
              "amount": "34 mg (0.20 mmol, 1.0 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Potassium carbonate (K2CO3)",
              "amount": "82 mg (0.59 mmol, 3.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": null,
              "name": "Sodium iodide (NaI)",
              "amount": "3.0 mg (0.02 mmol, 0.1 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "N,N-Dimethylformamide (DMF)",
              "volume": "1.5 mL"
            }
          ],
          "conditions": {
            "temperature": "5 °C (addition), 25 °C (reaction)",
            "time": "24 h",
            "pressure": null,
            "atmosphere": "N2",
            "ph": null,
            "other": "After reaction, diluted with ~10 volumes water, extracted three times with EtOAc; combined organics washed with brine, dried over Na2SO4, filtered, concentrated; crude taken forward without purification"
          },
          "product": {
            "compound_id": "C07",
            "name": "Sugar-protected N-alkylated intermediate 24b",
            "yield": "120 mg (crude; 66.7% LC–MS purity)",
            "purity": "66.7% by LC–MS",
            "molar_activity": null,
            "characterization": ["LC–MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {
                  "adduct": "[M(35Cl)+H]+",
                  "mz": 784.3
                },
                {
                  "adduct": "[M(37Cl)+H]+",
                  "mz": 786.3
                }
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "Crude product (yellow oil) taken forward without further purification; yield over two steps is quoted after subsequent deprotection",
          "notes": "General N-alkylation procedure (Route 1) applies to amines 22a–q and alkylating agents 23a–d or 58. Scheme 1 label: step (d). NaI used as iodide catalyst (Finkelstein activation). Overall yield range across library: 8–58% over two steps."
        },
        {
          "step_number": 5,
          "reaction_type": "Sugar deacetylation (ammonolysis with NH3/MeOH)",
          "reactants": [
            {
              "compound_id": "C07",
              "name": "Acetyl-protected intermediate 24b",
              "amount": "120 mg (0.15 mmol, crude from step 4)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Ammonia in methanol (7.0 M NH3/MeOH)",
              "amount": "3.0 mL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "Methanol (MeOH)",
              "volume": "3.0 mL (as solvent/reagent combination)"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "6 h",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "Reaction conducted in sealed vessel. Volatiles removed by evaporation under vacuum; residue coevaporated three times with MeOH (3–5 mL) to remove residual NH3. Crude product purified by preparative HPLC"
          },
          "product": {
            "compound_id": "C08",
            "name": "Triple inhibitor 27",
            "yield": "18.0 mg (15% over two steps from 22b)",
            "purity": "100.0% by HPLC and LC–MS",
            "molar_activity": null,
            "characterization": ["1H NMR", "HPLC", "LC–MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {
                  "adduct": "[M(35Cl)+H]+",
                  "mz": 616.2
                },
                {
                  "adduct": "[M(37Cl)+H]+",
                  "mz": 618.2
                }
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "Preparative HPLC (column: Waters XBridge, 150 × 25 mm, 5 μm; mobile phase: A = 10 mM NH4HCO3, B = MeCN; 20–40% B over 12 min); obtained as white solid",
          "notes": "General deprotection procedure for Route 1 final compounds 26–30, 32–35, 37, 38, 46–50, 60–63, 69, 70, 97, 98. Scheme 1 label: step (e). Yield range across analogues (two-step from 22): 4–43%. 1H NMR (400 MHz, CD3OD): δ 7.38–7.31 (m, 2H), 7.31–7.25 (m, 1H), 7.10 (d, J = 8.8, 2H), 6.81 (d, J = 8.8, 2H), 4.74 (t, J = 5.2, 1H), 4.61 (s, 1H), 4.17–3.99 (m, 3H), 3.99–3.92 (m, 2H), 3.91–3.84 (m, 1H), 3.73–3.60 (m, 2H), 3.54–3.35 (m, 6H), 3.30–3.25 (m, 1H), 2.40–1.99 (m, 4H), 1.85–1.70 (m, 2H), 1.68–1.51 (m, 2H), 1.18–1.06 (m, 6H)."
        }
      ]
    }
  ]
}
```

With the paper 2, it is too long so that Claude cannot extract full paper, I just extract the Scheme 1 in the paper.

##### Claude Paper 2 Scheme 2
```
{
  "extraction": {
    "prompt_version": "v3.0",
    "extraction_date": "2026-03-28",
    "model_name": "claude-sonnet-4-6",
    "extractor_notes": "PHASE 1 SCAN: Scheme 2 describes the synthesis of compound 36, a triple inhibitor bearing the gosogliptin-type 2,4-disubstituted pyrrolidine linker, which was inaccessible via the general route (Scheme 1) because the β-nitrogen is incorporated into the pyrrolidine ring. The scheme is fully described in the main text experimental section (pages 36–37). Seven steps are executed: (a) Boc protection of L-hydroxyproline 39 → 40; (b) TsOH-mediated Boc deprotection of 41 → 42 (pyrrolidinium salt); (c) EDC/HOBt amide coupling of 40 + 42 → 43; (d) tosylation of hydroxyl in 43 → 44; (e) SN2 O-alkylation of phenol 19a with tosylate 44 → 45; (f) TFA Boc + sugar deprotection and (g) NH3/MeOH deacetylation, reported as one combined operation → 36. Compound 19a (phenol intermediate from Scheme 1) is an in-scope intermediate carried over as a reactant in step 5. Compound 41 ((S)-1-Boc-2-cyanopyrrolidine) is introduced by name with no synthesis described; treated as commercially sourced starting material. Compound 39 (L-hydroxyproline) is a commercial amino acid. Steps (f) and (g) are performed sequentially in one operation on compound 45 and reported together as steps e–g with a combined three-step yield of 17% from 19a. The paper's yield annotation 'over three steps from 19a' spans steps (e), (f), and (g) of Scheme 2. Compounds 23d and other Scheme 3 compounds are out of scope for this extraction (Scheme 2 only). No SI references for Scheme 2 procedure — all detail in main text. Biological-only compounds excluded per Rule 1."
  },

  "paper": {
    "title": "Design, Optimization, and Biological Evaluation of First-in-Class Triple Inhibitors of SGLT1, SGLT2, and DPP4 for Type 2 Diabetes Mellitus",
    "authors": [
      "Fernando de Souza Gama",
      "Marcos Ferreira",
      "Natanael Dante Segretti",
      "Mariana C. F. C. B. Damiao",
      "Cristiano R. W. Guimaraes",
      "Alessandra Mascarello",
      "Hatylas Azevedo"
    ],
    "doi": "10.1021/acs.jmedchem.5c02225",
    "journal": "Journal of Medicinal Chemistry",
    "year": 2025,
    "synthesis_scale": "lab",
    "mechanism_discussed": "synthetic",
    "method_completeness": "full",
    "has_synthesis": true,
    "extraction_notes": "Scheme 2 only is extracted per user instruction. All steps fully described in the main text experimental section. The combined yield of 17% is quoted 'over three steps from 19a', referring to steps (e), (f), and (g) of Scheme 2; individual yields for steps (f) and (g) are not separately reported. Compound 45 crude mass (350 mg, >100% nominal yield) reflects an over-mass crude residue carried forward directly. Purity of compound 36 is 92.0% by HPLC — below the >95% threshold noted in the paper for screened compounds, and the paper explicitly flags 36 as a compound for which the purity exception applies. Masses for all compounds are reported as observed m/z (ES-MS); calculated exact masses are not stated in the paper."
  },

  "compounds": [
    {
      "id": "C01",
      "name": "L-Hydroxyproline (39)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Commercially available L-hydroxyproline used as the starting amino acid for construction of the gosogliptin-type pyrrolidine linker in Scheme 2."
    },
    {
      "id": "C02",
      "name": "(S)-1-Boc-2-cyanopyrrolidine (41)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "Commercial",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Commercially available N-Boc-protected (S)-2-cyanopyrrolidine used as the DPP4-pharmacophore building block; Boc is removed in step 2 to reveal the free amine for amide coupling."
    },
    {
      "id": "C03",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-{4-chloro-3-[(p-hydroxyphenyl)methyl]phenyl}tetrahydro-2H-pyran-2-yl]methyl Acetate (19a)",
      "iupac_name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-{4-chloro-3-[(p-hydroxyphenyl)methyl]phenyl}tetrahydro-2H-pyran-2-yl]methyl Acetate",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "In-house (prepared in Scheme 1, step a)",
      "physicochemical_properties": {
        "log_p": null,
        "other": "Purity 97.0% by HPLC; LC–MS purity 90.6%; m/z (ES) 566.2 ([M(35Cl)+H2O]+), 568.2 ([M(37Cl)+H2O]+)"
      },
      "description": "Free-phenol acetyl-protected C-glycoside intermediate 19a, prepared by BBr3 dealkylation in Scheme 1 and used here as the SGLT1/2-targeting nucleophilic component for SN2 O-alkylation with tosylate 44."
    },
    {
      "id": "C04",
      "name": "(2S,4R)-1-tert-Butoxycarbonyl-4-hydroxy-2-pyrrolidinecarboxylic Acid (40)",
      "iupac_name": "(2S,4R)-1-tert-Butoxycarbonyl-4-hydroxy-2-pyrrolidinecarboxylic Acid",
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "In-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "LC–MS purity 100.0%; m/z (ES) 230.1 ([M−H]−)"
      },
      "description": "N-Boc-protected trans-4-hydroxy-L-proline (compound 40) prepared by Boc protection of L-hydroxyproline 39; serves as the carboxylic acid component in amide coupling with pyrrolidinium salt 42."
    },
    {
      "id": "C05",
      "name": "(S)-1-Pyrrolidinium-2-carbonitrile p-Toluenesulfate (42)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "In-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Tosylate salt of (S)-pyrrolidine-2-carbonitrile (compound 42), prepared by TsOH-mediated Boc deprotection of 41; the free amine is coupled with Boc-hydroxyproline 40 in the next step."
    },
    {
      "id": "C06",
      "name": "tert-Butyl (2S,4R)-2-{[(S)-2-cyano-1-pyrrolidinyl]carbonyl}-4-hydroxy-1-pyrrolidinecarboxylate (43)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "In-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "LC–MS purity 97.7%; m/z (ES) 210.1 ([M−Boc+H]+)"
      },
      "description": "Boc-protected hydroxyprolinyl–cyanopyrrolidine amide 43, obtained by EDC/HOBt coupling of 40 and 42; the free hydroxyl at C4 is tosylated in the next step to create an electrophilic leaving group."
    },
    {
      "id": "C07",
      "name": "tert-Butyl (2S,4R)-2-{[(S)-2-Cyano-1-pyrrolidinyl]carbonyl}-4-(tosyloxy)-1-pyrrolidinecarboxylate (44)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "In-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": null
      },
      "description": "Tosylated derivative 44 of compound 43, prepared by treatment with TsCl/pyridine; acts as the activated electrophile for SN2 O-alkylation of phenol 19a."
    },
    {
      "id": "C08",
      "name": "tert-Butyl (2S,4S)-4-[p-({2-Chloro-5-[(2S,3S,4R,5R,6R)-3,4,5-triacetoxy-6-(acetoxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-2-{[(S)-2-cyano-1-pyrrolidinyl]carbonyl}-1-pyrrolidinecarboxylate (45)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "In-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "m/z (ES) 740.3 (100%; [M(35Cl)−Boc+H]+), 742.3 (40%; [M(37Cl)−Boc+H]+)"
      },
      "description": "Fully protected penultimate intermediate 45, bearing the intact C-glycoside acetates, Boc group on the pyrrolidine nitrogen, and the 2-cyanopyrrolidinyl amide; produced by Cs2CO3-mediated SN2 coupling of phenol 19a with tosylate 44."
    },
    {
      "id": "C09",
      "name": "(S)-1-{[(2S,4S)-4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-2-pyrrolidinyl]carbonyl}-2-pyrrolidinecarbonitrile (36)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "In-house",
      "physicochemical_properties": {
        "log_p": null,
        "other": "HPLC purity 92.0%; LC–MS purity 88.9%; m/z (ES) 572.2 (100%; [M(35Cl)+H]+), 574.3 (35%; [M(37Cl)+H]+)"
      },
      "description": "Triple inhibitor 36 bearing the gosogliptin-type 2,4-disubstituted pyrrolidine linker, with unmasked sugar hydroxyl groups and free pyrrolidine nitrogen; the final deprotected product obtained after combined TFA Boc removal and NH3/MeOH deacetylation of 45."
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "Scheme 2 — Gosogliptin-Type Linker Installation: Synthesis of Compound 36",
      "target_compound_id": "C09",
      "target_compound_name": "Compound 36",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "N-Boc protection of amino acid",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "L-Hydroxyproline (39)",
              "amount": "2.00 g (15.3 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "1 M NaOH",
              "amount": "24 mL (24 mmol, 1.6 equiv)",
              "role": "base"
            },
            {
              "compound_id": null,
              "name": "Di-tert-butyl dicarbonate (Boc2O)",
              "amount": "3.99 g (4.20 mL, 18.3 mmol, 1.2 equiv) in 1,4-dioxane (6 mL)",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "Water/1,4-dioxane (2:1)",
              "volume": "54 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C (addition, maintained below 10 °C), then 20 °C",
            "time": "16 h",
            "pressure": null,
            "atmosphere": "N2",
            "ph": "Adjusted to pH 4 with 1 M HCl after reaction",
            "other": "Reaction mixture concentrated to ~30 mL under reduced pressure before pH adjustment; extracted with EtOAc (15 × 100 mL); combined organics washed with brine (300 mL), dried over Na2SO4, filtered, concentrated"
          },
          "product": {
            "compound_id": "C04",
            "name": "N-Boc-trans-4-hydroxy-L-proline (40)",
            "yield": "1.60 g (45%)",
            "purity": "100.0% by LC–MS",
            "molar_activity": null,
            "characterization": ["1H NMR", "LC–MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {
                  "adduct": "[M−H]−",
                  "mz": 230.1
                }
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "No chromatographic purification stated; product isolated after aqueous workup as yellow solid",
          "notes": "Scheme 2 label: step (a). Boc2O added in 1,4-dioxane to aqueous NaOH solution of the amino acid at 0 °C."
        },
        {
          "step_number": 2,
          "reaction_type": "Boc deprotection of N-Boc pyrrolidine (acid-mediated)",
          "reactants": [
            {
              "compound_id": "C02",
              "name": "(S)-1-Boc-2-cyanopyrrolidine (41)",
              "amount": "1.50 g (7.64 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "p-Toluenesulfonic acid monohydrate (TsOH·H2O)",
              "amount": "2.18 g (11.5 mmol, 1.5 equiv)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "Acetonitrile (MeCN)",
              "volume": "7 mL"
            }
          ],
          "conditions": {
            "temperature": "20 °C",
            "time": "48 h",
            "pressure": null,
            "atmosphere": "N2",
            "ph": null,
            "other": "Concentrated under reduced pressure at 45 °C; crude triturated with MTBE (30 mL) for 10 min, then CH2Cl2 (6 mL) added; solids stirred at 20 °C for 3 h, collected by filtration, washed with MTBE; filtrate concentrated"
          },
          "product": {
            "compound_id": "C05",
            "name": "(S)-1-Pyrrolidinium-2-carbonitrile p-toluenesulfate (42)",
            "yield": "1.90 g (93%)",
            "purity": null,
            "molar_activity": null,
            "characterization": ["1H NMR"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "Trituration with MTBE then CH2Cl2; collected by filtration; obtained as white solid",
          "notes": "Scheme 2 label: step (b). Product is the p-toluenesulfonate salt of (S)-pyrrolidine-2-carbonitrile. 1H NMR (400 MHz, CD3OD): δ 7.71 (d, J = 8.2, 2H), 7.24 (d, J = 8.2, 2H), 4.69 (t, J = 7.6, 1H), 3.51–3.34 (m, 2H), 2.56–2.43 (m, 1H), 2.37 (s, 3H), 2.34–2.05 (m, 3H)."
        },
        {
          "step_number": 3,
          "reaction_type": "Amide coupling (EDC/HOBt)",
          "reactants": [
            {
              "compound_id": "C04",
              "name": "N-Boc-trans-4-hydroxy-L-proline (40)",
              "amount": "300 mg (1.30 mmol)"
            },
            {
              "compound_id": "C05",
              "name": "(S)-Pyrrolidinium-2-carbonitrile p-toluenesulfate (42)",
              "amount": "384 mg (1.43 mmol, 1.1 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "1-Hydroxybenzotriazole (HOBt)",
              "amount": "193 mg (1.43 mmol, 1.1 equiv)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": null,
              "name": "1-Ethyl-3-(3-dimethylaminopropyl)carbodiimide (EDC)",
              "amount": "274 mg (1.43 mmol, 1.1 equiv)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": null,
              "name": "Triethylamine (Et3N)",
              "amount": "145 mg (199 μL, 1.43 mmol, 1.1 equiv)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "Dichloromethane (CH2Cl2)",
              "volume": "3 mL"
            }
          ],
          "conditions": {
            "temperature": "20 °C",
            "time": "16 h",
            "pressure": null,
            "atmosphere": "N2",
            "ph": null,
            "other": "Compound 42 pre-suspended in CH2Cl2 with Et3N and stirred 5 min until dissolved before addition of 40, HOBt, and EDC; reaction quenched with sat. NaHCO3 (20 mL); extracted with CH2Cl2 (15 mL then 2 × 10 mL); combined organics washed with brine (20 mL), dried over Na2SO4, filtered, concentrated"
          },
          "product": {
            "compound_id": "C06",
            "name": "tert-Butyl (2S,4R)-2-{[(S)-2-cyano-1-pyrrolidinyl]carbonyl}-4-hydroxy-1-pyrrolidinecarboxylate (43)",
            "yield": "230 mg (57%)",
            "purity": "97.7% by LC–MS",
            "molar_activity": null,
            "characterization": ["1H NMR", "LC–MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {
                  "adduct": "[M−Boc+H]+",
                  "mz": 210.1
                }
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "Column chromatography on silica (0 → 3.33 → 100% MeOH/CH2Cl2); obtained as light yellow solid",
          "notes": "Scheme 2 label: step (c). 1H NMR (400 MHz, CDCl3): δ 4.89–4.76 (m, 1H), 4.70–4.48 (m, 2H), 3.94–3.41 (m, 4H), 2.42–2.07 (m, 6H), 2.02–1.87 (m, 1H), 1.45 (s, 9H)."
        },
        {
          "step_number": 4,
          "reaction_type": "Tosylation of secondary alcohol",
          "reactants": [
            {
              "compound_id": "C06",
              "name": "Hydroxy intermediate 43",
              "amount": "200 mg (0.65 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "p-Toluenesulfonyl chloride (TsCl)",
              "amount": "271 mg (1.42 mmol, 2.2 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "Pyridine",
              "volume": "1.4 mL"
            }
          ],
          "conditions": {
            "temperature": "20 °C",
            "time": "20 h",
            "pressure": null,
            "atmosphere": "N2",
            "ph": null,
            "other": "Diluted with water (30 mL); extracted with EtOAc (3 × 15 mL); combined organics washed with brine, dried over Na2SO4, filtered, evaporated; used in next step without further purification"
          },
          "product": {
            "compound_id": "C07",
            "name": "tert-Butyl (2S,4R)-2-{[(S)-2-Cyano-1-pyrrolidinyl]carbonyl}-4-(tosyloxy)-1-pyrrolidinecarboxylate (44)",
            "yield": "310 mg (>100%; crude, used directly)",
            "purity": null,
            "molar_activity": null,
            "characterization": ["1H NMR"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": []
            },
            "hplc_retention_time_min": null
          },
          "purification": "None; crude yellow oil taken directly to next step",
          "notes": "Scheme 2 label: step (d). Yield >100% indicates crude over-mass due to residual solvent/reagent contamination in the crude oil. 1H NMR (400 MHz, CDCl3): δ 7.85–7.75 (m, 2H), 7.44–7.33 (m, 2H), 5.14–4.90 (m, 1H), 4.87–4.71 (m, 1H), 4.57–4.46 (m, 1H), 3.93–3.49 (m, 4H), 2.48 (s, 3H), 2.44–2.07 (m, 6H), 1.40 (s, 9H)."
        },
        {
          "step_number": 5,
          "reaction_type": "O-Alkylation of phenol with tosylate (SN2)",
          "reactants": [
            {
              "compound_id": "C03",
              "name": "Phenol intermediate 19a",
              "amount": "170 mg (0.31 mmol)"
            },
            {
              "compound_id": "C07",
              "name": "Tosylate 44",
              "amount": "287 mg (0.62 mmol, 2.0 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Caesium carbonate (Cs2CO3)",
              "amount": "232 mg (0.71 mmol, 2.3 equiv)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "N,N-Dimethylformamide (DMF)",
              "volume": "3.4 mL"
            }
          ],
          "conditions": {
            "temperature": "85 °C",
            "time": "16 h",
            "pressure": null,
            "atmosphere": "N2",
            "ph": null,
            "other": "Tosylate 44 added to 19a and Cs2CO3 in DMF at 25 °C then heated to 85 °C; after reaction, water (40 mL) added, extracted with EtOAc (15 mL then 2 × 10 mL); combined organics washed with brine (20 mL), dried over Na2SO4, filtered, concentrated; crude used directly in next step"
          },
          "product": {
            "compound_id": "C08",
            "name": "Fully protected intermediate 45",
            "yield": "350 mg (crude, >100%)",
            "purity": null,
            "molar_activity": null,
            "characterization": ["LC–MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {
                  "adduct": "[M(35Cl)−Boc+H]+",
                  "mz": 740.3
                },
                {
                  "adduct": "[M(37Cl)−Boc+H]+",
                  "mz": 742.3
                }
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "None; crude yellow oil carried forward directly to final deprotection",
          "notes": "Scheme 2 label: step (e). Yield >100% reflects crude over-mass; no individual yield quoted for this step. Combined yield over steps (e), (f), and (g) is 17% from 19a."
        },
        {
          "step_number": 6,
          "reaction_type": "Simultaneous Boc deprotection (TFA) followed by sugar deacetylation (NH3/MeOH)",
          "reactants": [
            {
              "compound_id": "C08",
              "name": "Fully protected intermediate 45",
              "amount": "300 mg (0.36 mmol, crude from step 5)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Trifluoroacetic acid (TFA)",
              "amount": "1.16 g (0.75 mL)",
              "role": "acid"
            },
            {
              "compound_id": null,
              "name": "7 M Ammonia in methanol (NH3/MeOH)",
              "amount": "6.0 mL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "Dichloromethane (CH2Cl2)",
              "volume": "3 mL (TFA step)"
            },
            {
              "name": "Methanol (MeOH)",
              "volume": "Included in 7 M NH3/MeOH (6.0 mL)"
            }
          ],
          "conditions": {
            "temperature": "25 °C (TFA step); 15 °C (NH3/MeOH step)",
            "time": "1.5 h (TFA step); 7 h (NH3/MeOH step)",
            "pressure": null,
            "atmosphere": null,
            "ph": null,
            "other": "TFA step: concentrated under reduced pressure; residue coevaporated with CH2Cl2 (3 × 5 mL) to remove residual TFA. NH3/MeOH step: conducted in sealed vessel; volatiles removed under reduced pressure; residue coevaporated with MeOH (3 × 5 mL) under reduced pressure to remove excess NH3"
          },
          "product": {
            "compound_id": "C09",
            "name": "Triple inhibitor 36",
            "yield": "30 mg (17% over three steps from 19a)",
            "purity": "92.0% by HPLC; 88.9% by LC–MS",
            "molar_activity": null,
            "characterization": ["1H NMR", "HPLC", "LC–MS"],
            "ms_data": {
              "calculated_exact_mass": null,
              "formula": null,
              "observed_ions": [
                {
                  "adduct": "[M(35Cl)+H]+",
                  "mz": 572.2
                },
                {
                  "adduct": "[M(37Cl)+H]+",
                  "mz": 574.3
                }
              ]
            },
            "hplc_retention_time_min": null
          },
          "purification": "Preparative HPLC (column: Waters XBridge BEH C18, 100 × 30 mm, 10 μm; mobile phase: A = 10 mM NH4HCO3, B = MeCN; 10–30% B over 10 min); obtained as white solid",
          "notes": "Scheme 2 labels: steps (f) and (g) combined here as a single sequential operation. The paper reports the 17% yield over three steps spanning steps (e), (f), and (g) from 19a. 1H NMR (400 MHz, CD3OD): δ 7.39–7.23 (m, 3H), 7.11 (d, J = 8.5, 2H), 6.80 (d, J = 8.5, 2H), 5.03–4.97 (m, 1H), 4.38–4.24 (m, 1H), 4.14–3.95 (m, 3H), 3.91–3.82 (m, 1H), 3.79–3.56 (m, 4H), 3.50–3.34 (m, 4H), 3.34–3.23 (m, 2H), 2.70–2.50 (m, 2H), 2.48–2.37 (m, 1H), 2.20–1.88 (m, 3H). Purity of 36 is below the >95% threshold; the paper explicitly flags 36 as an exception to this criterion."
        }
      ]
    }
  ]
}
```

### V3.1

##### Prompt
```
SYSTEM ROLE
===========

You are a chemical synthesis extraction engine. Extract synthesis procedures, reaction conditions, compound preparation data, and purity/MS characterization from the academic paper provided. Do NOT extract biological assay results, pharmacological IC50 data, in vivo data, selectivity ratios, or docking scores. This scope restriction is absolute.

Your primary obligation is fidelity to the source text. If a value is absent, record null. Never invent or infer values.


RULES
=====

RULE 1 — SCOPE: SYNTHESIS ONLY

Include in compounds[]:
- Reactants, reagents, and products in at least one synthesis step
- Radionuclide/metal sources used in radiolabeling or chelation
- Buffers and pH-adjustment solutions used in a synthesis step
- Catalysts, bases, coupling reagents named with an amount

Exclude from compounds[]:
- Reference compounds (marketed drugs, known inhibitors cited for comparison only, with no synthetic role in this study) — omit entirely, do not assign IDs
- Compounds appearing only in biological assay sections
- Cell lines, antibodies, commercial kits, QC standards

RULE 2 — ARTICLE-ONLY
Extract exclusively from the provided text. If details are in Supporting Information not provided, record null and note the SI reference in the step's notes field. Do not use prior chemical knowledge.

RULE 3 — NULL FOR ABSENT DATA
Record null for any absent field. Never invent plausible values.

RULE 4 — COMPOUND ID ORDERING
Assign IDs (C01, C02, ...) strictly by order of first appearance, top-to-bottom through:
  a. Abstract
  b. Introduction
  c. Results/Chemistry
  d. Experimental
Within a sentence, assign left to right. No skipped IDs, no reused IDs. Reference compounds are excluded and never receive IDs — their absence does not create gaps.

RULE 5 — ROLE ASSIGNMENT (decision tree, strict order)
1. Contains a radioisotope, produced in a radiolabeling step → radiolabeled_product
2. Sourced externally (commercial/vendor), used as substrate or precursor → starting_material
3. Sourced externally, used as consumable reagent (base, coupling agent, buffer, radionuclide source) → reagent
4. Synthesised in-house, input to a subsequent transformation → intermediate
5. Synthesised in-house or externally, evaluated as standalone pharmacological deliverable, no radioisotope → final_product
6. Metal/ligand in a coordination context → catalyst or coligand

RULE 6 — is_newly_synthesized
true = prepared in-house in this study.
false = commercial, custom-ordered, or externally synthesised.

RULE 7 — YIELD FORMAT
"N mg (N%)" when both stated; "N%" when only percentage given. One compound per yield string.

RULE 8 — AMOUNTS FORMAT
"N unit (N unit)" e.g. "6.4 mg (3 umol)". Never append solvent or concentration into the amount string.

RULE 9 — STEP GRANULARITY
Each physically distinct operation with its own materials list = one numbered step. Different reagents, conditions, vessel, or equipment = new step. Examples:
- pH adjustment and subsequent reaction = 2 steps
- QMA trapping and Al18F complexation = 2 steps
- Each SPPS coupling cycle = separate step

RULE 10 — STEP PRODUCT BLOCK
Every step must have a product block describing what that step produces, even if transient. Use compound_id: null for transient intermediates with no standalone entry. Never recycle a reactant's ID as the product of the same step.

RULE 11 — CONDITIONS DISCIPLINE
- conditions.ph = pH of the reaction mixture only
- Reagent solution pH/concentration goes in the reagent amount field
- conditions.other = 1 sentence maximum (key workup or handling note only)
- purification = method + elution solvent only
  Examples: "column chromatography, EtOAc/hexanes gradient"
            "preparative HPLC, 10 mM NH4HCO3/MeCN"

RULE 12 — PURITY FORMAT
Always include analytical method. Examples:
- "99.0% by LC-MS"
- ">95% by HPLC"
- ">95% RCP by radio-HPLC"

RULE 13 — MS DATA (flat string)
Record MS data as a flat string in compound.ms_observed.
Example: "[M+H]+ 616.2, [M+Na]+ 638.2"
Example: "[M(35Cl)+Na]+ 541.0, [M(37Cl)+Na]+ 543.0"
Record calculated exact mass only if explicitly stated in the paper.
Do not use nested objects for MS data.

RULE 14 — ONE PATHWAY PER TARGET COMPOUND
Each pathway (P1, P2, ...) targets exactly one compound. No "or/alternatively" logic within one pathway.

RULE 15 — CONSISTENCY GATE (run before output)
a. Every compound_id in any step (reactants, reagents, product) has a matching entry in compounds[]
b. Every target_compound_id in a pathway has a matching entry in compounds[]
c. No duplicate compound IDs
d. IDs form a contiguous sequence C01 to highest assigned, no gaps
e. A reactant's compound_id is never also the product.compound_id of the same step
f. All compounds[] entries satisfy Rule 1 (no reference compounds)


EXECUTION PROTOCOL
==================

PHASE 1 — SCAN
Before filling any JSON, identify:
1. Which sections contain synthesis (Experimental, Schemes, Chemistry)?
2. How many pathways?
3. Which compounds are in-scope vs. excluded (especially reference compounds)?
4. Any SI references for missing details?
Record scan summary in extraction.extractor_notes.

PHASE 2 — COMPOUND INVENTORY
Build compounds[] in document order. Assign IDs only to in-scope compounds.
Resolve role and is_newly_synthesized for each.

PHASE 3 — PATHWAY EXTRACTION
Fill steps sequentially. Every step has a product block.
Run Consistency Gate before output.


OUTPUT SCHEMA
=============

Return a single JSON object. No text before or after the JSON.

{
  "extraction": {
    "prompt_version": "v3.1",
    "extraction_date": "YYYY-MM-DD",
    "model_name": "string",
    "extractor_notes": "string or null — scan summary: sections found, pathway count, excluded reference compounds (names only, no IDs), SI gaps, mass type notes"
  },

  "paper": {
    "title": "string",
    "authors": ["string"],
    "doi": "string or null",
    "journal": "string or null",
    "year": "integer or null",
    "synthesis_scale": "lab | preclinical | gmp | none",
    "method_completeness": "full | partial | referenced_to_SI | none",
    "has_synthesis": true,
    "extraction_notes": "string or null"
  },

  "compounds": [
    {
      "id": "C01",
      "name": "string",
      "iupac_name": "string or null — only if explicitly stated in the paper",
      "molecular_formula": "string or null — only if explicitly stated",
      "role": "starting_material | intermediate | reagent | catalyst | coligand | radiolabeled_product | final_product",
      "is_newly_synthesized": true,
      "source": "string or null — in-house / commercial / vendor name",
      "purity": "string or null — e.g. 99.0% by LC-MS",
      "ms_observed": "string or null — flat string e.g. [M+H]+ 616.2, [M(35Cl)+Na]+ 541.0",
      "ms_calculated_exact_mass": "number or null — only if explicitly stated in paper",
      "description": "one sentence describing this compound's synthetic role"
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "string",
      "target_compound_id": "string",
      "target_compound_name": "string",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "string or null",
          "reactants": [
            {
              "compound_id": "string or null",
              "name": "string",
              "amount": "string or null"
            }
          ],
          "reagents": [
            {
              "compound_id": "string or null",
              "name": "string",
              "amount": "string or null",
              "role": "coupling_reagent | base | acid | oxidant | reductant | catalyst | protecting_group_reagent | ph_adjuster | radionuclide_source | other"
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
            "atmosphere": "string or null",
            "ph": "string or null",
            "other": "string or null — 1 sentence max"
          },
          "product": {
            "compound_id": "string or null",
            "name": "string",
            "yield": "string or null",
            "purity": "string or null",
            "hplc_retention_time_min": "number or null"
          },
          "purification": "string or null — method + solvent only",
          "notes": "string or null — SI references, equipment, replication count"
        }
      ]
    }
  ]
}

```

##### Claude Paper 2
```
{
  "extraction": {
    "prompt_version": "v3.1",
    "extraction_date": "2026-03-29",
    "model_name": "claude-sonnet-4-6",
    "extractor_notes": "SCAN SUMMARY: Synthesis sections found in Schemes 1–11 (main text) plus Schemes S1–S4 (SI, not provided). Experimental Section contains detailed procedures for: (1) General dealkylation of aryl ethyl ethers 18a–h to give 19a–h; (2) Tosylation of linker alcohols to give 20f–l, 20o, 20p; (3) Mitsunobu coupling of 19a–h with alcohols 20a–e, 20m–p to give 21a–w; (4) Boc deprotection of 21-series to give 22a–q; (5) N-alkylation with 23a–d or 58 (route 1) to give 24a–x; (6) Final deprotection (NH3/MeOH) to give screening compounds 26–38, 46–50, 60–63, 69–70, 97–98; (7) Full deprotection (HCl/MeOH) of 21m,n,q,r,u–w to give 25a–g; (8) N-alkylation of 25a–g (route 2) to give final products 64, 65, 66, 67, 68, 94, 95, 99–102, 124–127; (9) Separate syntheses for 36, 51 (Scheme 2/4); (10) Alkylating agents 23c (Scheme 3) and 58 (Scheme 3); (11) Building blocks 19g (Scheme 9), 19h (Scheme 10); (12) Sugar intermediates 18b (Scheme 5), 18c (Scheme 5), 18d (direct acetylation of sotagliflozin 6), 18e and 18f (Scheme 8), 18g (Scheme 9), 18h (Scheme 10); (13) Schemes 5–8 for sugar building blocks; (14) Scheme 11 for compound 102. Pathways: P1=19a synthesis; P2–P8 cover major sugar building blocks (18b, 18c, 18d, 18e, 18f, 18g, 18h); P9=compound 36; P10=compound 51; P11=compounds 26–38 (general route 1 from 19a); P12=compounds 60–63 (route 1 from 19b/c/d); P13=compound 64; P14=compound 65 (Scheme 6); P15=compound 66 (Scheme 7); P16=compounds 67–68; P17=compounds 94–95; P18=compounds 96; P19=compounds 97–98; P20=compounds 99–101 (route 2); P21=compound 102 (Scheme 11); P22=compounds 124–127. Reference compounds excluded (no IDs assigned): canagliflozin 1, dapagliflozin 2, bexagliflozin 3, empagliflozin 4, ertugliflozin 5, sotagliflozin 6, licogliflozin 7, HM41322 8, LX2761 9, mizagliflozin 10, vildagliptin 11, saxagliptin 12, anagliptin 13, prusogliptin 14, melogliptin 15, gosogliptin 16, teneligliptin 17. SI gaps: Schemes S1–S4 not provided; Table S17 (purity data) not provided; compound 20k synthesis in Scheme S1; compound 31 route in Scheme S2; compound 79 synthesis in Scheme S3; compound 20n synthesis in Scheme S4. MS data type: ESI, [M+H]+, [M-H]-, [M+Na]+ and chlorine isotope patterns as reported. Exact masses not explicitly stated in paper. NOTE: Due to extreme compound count (100+ in-scope compounds), this extraction covers all compounds with full characterization data in the Experimental Section. Intermediates without standalone characterization (crude products taken directly to next step) are included with available data."
  },
  "paper": {
    "title": "Design, Optimization, and Biological Evaluation of First-in-Class Triple Inhibitors of SGLT1, SGLT2, and DPP4 for Type 2 Diabetes Mellitus",
    "authors": [
      "Fernando de Souza Gama",
      "Marcos Ferreira",
      "Natanael Dante Segretti",
      "Mariana C. F. C. B. Damião",
      "Cristiano R. W. Guimarães",
      "Alessandra Mascarello",
      "Hatylas Azevedo"
    ],
    "doi": "10.1021/acs.jmedchem.5c02225",
    "journal": "Journal of Medicinal Chemistry",
    "year": 2025,
    "synthesis_scale": "lab",
    "method_completeness": "partial",
    "has_synthesis": true,
    "extraction_notes": "Full experimental procedures provided for all final screening compounds and key intermediates. Some building block syntheses (20k, 79, 20n) referenced to SI Schemes S1, S3, S4. Purity data in Table S17 (SI). The paper describes two main routes (Route 1 and Route 2) to final products, with extensive use of general procedures applied to multiple substrate/reagent combinations."
  },
  "compounds": [
    {
      "id": "C01",
      "name": "tetraacetyl dapagliflozin (18a)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acetyl-protected dapagliflozin derivative used as the primary starting material for the dapagliflozin-based SGLT1/2/DPP4 inhibitor library."
    },
    {
      "id": "C02",
      "name": "BBr3",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Boron tribromide used as Lewis acid for dealkylation of aryl ethyl ethers 18a–h to give free phenols 19a–h."
    },
    {
      "id": "C03",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-{4-chloro-3-[(p-hydroxyphenyl)methyl]phenyl}tetrahydro-2H-pyran-2-yl]methyl Acetate (19a)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "97.0% by HPLC; 90.6% by LC-MS",
      "ms_observed": "[M(35Cl)+H2O]+ 566.2, [M(37Cl)+H2O]+ 568.2",
      "ms_calculated_exact_mass": null,
      "description": "Free phenol intermediate derived from 18a by BBr3 dealkylation; key branching point for linker coupling in the dapagliflozin series."
    },
    {
      "id": "C04",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{4-chloro-3-[(p-hydroxyphenyl)methyl]phenyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate (19b)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "6-Deoxy free phenol intermediate derived from 18b by BBr3 dealkylation; used in synthesis of 60–63, 97–98."
    },
    {
      "id": "C05",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{4-ethyl-3-[(p-hydroxyphenyl)methyl]phenyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate (19c)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "6-Deoxy, 4-ethyl free phenol intermediate derived from 18c by BBr3 dealkylation; used in synthesis of 64, 94, 95, 101, 125, 126, 127."
    },
    {
      "id": "C06",
      "name": "(2R,3S,4R,5S,6S)-4,5-Diacetoxy-6-{4-chloro-3-[(p-hydroxyphenyl)methyl]phenyl}-2-(methylthio)tetrahydro-2H-pyran-3-yl Acetate (19d)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Sotagliflozin-derived free phenol intermediate from BBr3 dealkylation of 18d; used in synthesis of 67–68."
    },
    {
      "id": "C07",
      "name": "(2S,3S,4R,5R,6R)-4-Acetoxy-2-{4-chloro-3-[(p-hydroxyphenyl)methyl]phenyl}-5-fluoro-6-methyltetrahydro-2H-pyran-3-yl Acetate (19e)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "4-Fluoro, 6-deoxy free phenol intermediate derived from 18e by BBr3 dealkylation; used in synthesis of 69."
    },
    {
      "id": "C08",
      "name": "(2S,3S,4R,6R)-4-Acetoxy-2-{4-chloro-3-[(p-hydroxyphenyl)methyl]phenyl}-5,5-difluoro-6-methyltetrahydro-2H-pyran-3-yl Acetate (19f)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "4,4-Difluoro, 6-deoxy free phenol intermediate derived from 18f by BBr3 dealkylation; used in synthesis of 70."
    },
    {
      "id": "C09",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{3-[(p-hydroxyphenyl)methyl]-4-tolyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate (19g)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Core methyl (R1=Me), 6-deoxy free phenol intermediate from BBr3 dealkylation of 18g; used in synthesis of 99."
    },
    {
      "id": "C10",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{3-[(p-hydroxyphenyl)methyl]-4-cumenyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate (19h)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Core isopropyl (R1=iPr), 6-deoxy free phenol intermediate from BBr3 dealkylation of 18h; used in synthesis of 100."
    },
    {
      "id": "C11",
      "name": "tert-butyl 3-methyl-3-[(N-Boc-amino)]butyl ether linker alcohol 20a",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "C2-linker Boc-amino alcohol used in Mitsunobu coupling with 19a to give 21a."
    },
    {
      "id": "C12",
      "name": "tert-butyl 4-methyl-4-[(N-Boc-amino)]pentyl ether linker alcohol 20b (4-[tert-butyl(oxycarbonylamino)]-4-methylpentan-1-ol)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Priority gem-dimethyl C4 linker alcohol used extensively in Mitsunobu coupling with 19a–h to give 21b-series; corresponds to the preferred linker in compounds 27, 47, 60–68, 94, 95, 99–102, 124–127."
    },
    {
      "id": "C13",
      "name": "2-(N-Boc-amino)ethanol (20c)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "C2 ethylene linker Boc-amino alcohol used in Mitsunobu coupling to give 21c (compound 28)."
    },
    {
      "id": "C14",
      "name": "3-(N-Boc-amino)propanol (20d)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "C3 propylene linker Boc-amino alcohol used in Mitsunobu coupling to give 21d (compound 29)."
    },
    {
      "id": "C15",
      "name": "4-(N-Boc-amino)butanol (20e)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "C4 butylene linker Boc-amino alcohol used in Mitsunobu coupling to give 21e (compound 30)."
    },
    {
      "id": "C16",
      "name": "tert-Butyl [3-(Tosyloxy)cyclopentyl]carbamate (20f)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Cyclopentyl tosylate linker prepared from tert-butyl 3-hydroxycyclopentylcarbamate; used in nucleophilic coupling with 19a to give 21f (compound 31)."
    },
    {
      "id": "C17",
      "name": "tert-Butyl [(1S,3R)-3-(Tosyloxy)cyclopentyl]carbamate (20g)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Enantiopure trans-1,3-cyclopentyl tosylate linker; used in nucleophilic coupling to give 21f (compound 32)."
    },
    {
      "id": "C18",
      "name": "tert-Butyl [3-(Tosyloxy)cyclohexyl]carbamate (20h)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "3-Cyclohexyl tosylate linker; used in nucleophilic coupling to give 21g (compound 33)."
    },
    {
      "id": "C19",
      "name": "tert-Butyl [4-(Tosyloxy)cyclohexyl]carbamate (20i)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "4-Cyclohexyl tosylate linker; used in nucleophilic coupling to give 21h (compound 34)."
    },
    {
      "id": "C20",
      "name": "tert-butyl 3-pyrrolidinyloxy carbamate 20j (3-(N-Boc-aminooxy)pyrrolidine tosylate)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Commercially available pyrrolidine tosylate linker; used in nucleophilic coupling to give 21i (compound 35)."
    },
    {
      "id": "C21",
      "name": "tert-Butyl [5-(Tosyloxy)bicyclo[2.2.2]oct-2-yl]carbamate (20k)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Bicyclo[2.2.2]octyl tosylate linker prepared from 5-hydroxybicyclo[2.2.2]oct-2-yl Boc-carbamate S3 (Scheme S1); used in coupling to give 21j (compound 37)."
    },
    {
      "id": "C22",
      "name": "tert-Butyl [(1R,4R)-1-Methyl-4-(tosyloxy)cyclohexyl]carbamate (20l)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "1-Methylcyclohexyl tosylate linker; used in nucleophilic coupling to give 21k (compound 38)."
    },
    {
      "id": "C23",
      "name": "spiro-cyclopropyl linker alcohol 20m (1-[N-Boc-amino]-1-cyclopropylmethanol-derived linker)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Spiro-cyclopropyl Boc-amino alcohol used in Mitsunobu coupling with 19c to give 21q (compound 94)."
    },
    {
      "id": "C24",
      "name": "spiro-cyclopentyl linker alcohol 20n (1-[N-Boc-amino]-1-cyclopentanemethanol-derived propyl linker)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Spiro-cyclopentyl Boc-amino alcohol prepared in four steps from N-Boc-1-amino-1-cyclopentanemethanol (Scheme S4); used in Mitsunobu coupling to give 21r (compound 95)."
    },
    {
      "id": "C25",
      "name": "tert-Butyl [(1S,3S)-3-hydroxycyclopentyl]carbamate-derived tosylate 20o",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Enantiopure (1S,3S)-trans-cyclopentyl Boc-amino alcohol used in Mitsunobu coupling with 19b and 19c to give 21s and 21w."
    },
    {
      "id": "C26",
      "name": "tert-Butyl [(1R,4R)-4-(Tosyloxy)cyclohexyl]carbamate (20p)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Trans-4-Boc-aminocyclohexanol-derived tosylate; used in nucleophilic coupling with 19b to give 21t (compound 98)."
    },
    {
      "id": "C27",
      "name": "(S)-2-Chloro-1-[(S)-2-cyanopyrrolidin-1-yl]ethan-1-one (23a); chloroacetyl-(S)-2-cyanopyrrolidine",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Alkylating agent (Y=CH2, R5=CN, R6=H) used in N-alkylation step (Route 1) to install the 2-cyanopyrrolidine DPP4 pharmacophore in compounds 26–34."
    },
    {
      "id": "C28",
      "name": "(2S,4S)-4-Fluoro-2-cyanopyrrolidine chloroacetyl alkylating agent (23b); (S)-2-chloro-1-[(2S,4S)-2-cyano-4-fluoropyrrolidin-1-yl]ethan-1-one",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "4-Fluorinated alkylating agent (Y=(S)-CHF, R5=CN, R6=H) used in N-alkylation to install 4-fluoro-2-cyanopyrrolidine DPP4 pharmacophore in compounds 35, 37, 38, 47, 49, 63, 67, 97–98, 125–126."
    },
    {
      "id": "C29",
      "name": "(S)-3-(2-Chloroacetyl)-1,3-thiazolidine-4-carbonitrile (23c)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M(35Cl)+H]+ 185.1, [M(37Cl)+H]+ 187.1",
      "ms_calculated_exact_mass": null,
      "description": "Thiazolidine-carbonitrile alkylating agent (Y=S, R5=H, R6=CN) prepared from Boc-D-thiazolidine-4-carboxylic acid 52 via amidation, TFAA dehydration, Boc removal, and chloroacetylation; used in N-alkylation to give compounds 46, 60."
    },
    {
      "id": "C30",
      "name": "(S)-2-Chloro-1-[(S)-2-cyano-4,4-difluoropyrrolidin-1-yl]ethan-1-one (23d); 4,4-difluoro-2-cyanopyrrolidine chloroacetyl alkylating agent",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "4,4-Difluorinated alkylating agent (Y=CF2, R5=CN, R6=H) commercially sourced; used to install gosogliptin-inspired difluoropyrrolidine DPP4 motif in compounds 50, 61, 62, 64, 68, 94, 95, 99–102, 124, 127."
    },
    {
      "id": "C31",
      "name": "[(1S,3S,5S)-3-Cyano-2-azabicyclo[3.1.0]hex-2-yl]acetyl Chloride (58)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "90.8% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 185.1, [M(37Cl)+H]+ 187.1",
      "ms_calculated_exact_mass": null,
      "description": "Bicyclic azabicyclo[3.1.0]hexane-carbonitrile chloroacetyl alkylating agent (saxagliptin-inspired) prepared from commercially available 56 via TFAA, TsOH deprotection, and chloroacetylation; used in N-alkylation to give compound 48, 62."
    },
    {
      "id": "C32",
      "name": "DIAD (diisopropyl azodicarboxylate)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu reagent used in coupling of phenols 19a–h with linker alcohols 20a–e, 20m–p."
    },
    {
      "id": "C33",
      "name": "DEAD (diethyl azodicarboxylate)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Alternative Mitsunobu reagent used in coupling reactions for some 21-series intermediates."
    },
    {
      "id": "C34",
      "name": "PPh3 (triphenylphosphine)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Phosphine co-reagent in Mitsunobu couplings and Appel iodinations."
    },
    {
      "id": "C35",
      "name": "K2CO3 (potassium carbonate)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Base used in nucleophilic coupling of tosylates with phenols 19a/19b and in N-alkylation steps."
    },
    {
      "id": "C36",
      "name": "Cs2CO3 (cesium carbonate)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Stronger base used in nucleophilic coupling reactions (O-alkylation) and Buchwald-Hartwig type couplings."
    },
    {
      "id": "C37",
      "name": "NaI (sodium iodide)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Finkelstein catalyst (0.1–0.4 equiv) used in N-alkylation steps to enhance reactivity of chloroacetyl alkylating agents."
    },
    {
      "id": "C38",
      "name": "TFA (trifluoroacetic acid)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Boc deprotection reagent used in CH2Cl2 for conversion of 21-series to 22-series TFA salts."
    },
    {
      "id": "C39",
      "name": "NH3/MeOH (7 M ammonia in methanol)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Deacetylation reagent used in final step of Route 1 to remove sugar acetyl protecting groups."
    },
    {
      "id": "C40",
      "name": "HCl/MeOH (4 M HCl in methanol)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Simultaneous Boc deprotection and sugar deacetylation reagent used in Route 2 to give 25a–g HCl salts."
    },
    {
      "id": "C41",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-{3-[(p-{3-[tert-butyl(oxycarbonylamino)]cyclopentyloxy}phenyl)methyl]-4-chlorophenyl}tetrahydro-2H-pyran-2-yl]methyl Acetate (21f)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "100.0% by LC-MS",
      "ms_observed": "[M(35Cl)-Boc+H]+ 632.3, [M(37Cl)-Boc+H]+ 634.3",
      "ms_calculated_exact_mass": null,
      "description": "Boc-protected coupling product of 19a with tosylate 20g; intermediate en route to compound 32."
    },
    {
      "id": "C42",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-{3-[(p-{3-[tert-butyl(oxycarbonylamino)]cyclohexyloxy}phenyl)methyl]-4-chlorophenyl}tetrahydro-2H-pyran-2-yl]methyl Acetate (21g)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "74.2% by LC-MS",
      "ms_observed": "[M(35Cl)-Boc+H]+ 646.3, [M(37Cl)-Boc+H]+ 648.3",
      "ms_calculated_exact_mass": null,
      "description": "Boc-protected coupling product of 19a with 20h; intermediate en route to compound 33."
    },
    {
      "id": "C43",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-{3-[(p-{4-[tert-butyl(oxycarbonylamino)]cyclohexyloxy}phenyl)methyl]-4-chlorophenyl}tetrahydro-2H-pyran-2-yl]methyl Acetate (21h)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M(35Cl)-Boc+H]+ 646.3, [M(37Cl)-Boc+H]+ 648.3",
      "ms_calculated_exact_mass": null,
      "description": "Boc-protected coupling product of 19a with 20i; intermediate en route to compound 34."
    },
    {
      "id": "C44",
      "name": "tert-Butyl 3-[p-({2-Chloro-5-[(2S,3S,4R,5R,6R)-3,4,5-triacetoxy-6-(acetoxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1-pyrrolidinecarboxylate (21i)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "70.2% by LC-MS",
      "ms_observed": "[M(35Cl)-Boc+H]+ 618.2, [M(37Cl)-Boc+H]+ 620.2",
      "ms_calculated_exact_mass": null,
      "description": "Boc-protected coupling product of 19a with pyrrolidine tosylate 20j; intermediate en route to compound 35."
    },
    {
      "id": "C45",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-{3-[(p-{5-[tert-butyl(oxycarbonylamino)]bicyclo[2.2.2]oct-2-yloxy}phenyl)methyl]-4-chlorophenyl}tetrahydro-2H-pyran-2-yl]methyl Acetate (21j)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M(35Cl)-Boc+H]+ 672.3, [M(37Cl)-Boc+H]+ 674.3, [M(35Cl)+Na]+ 794.3, [M(37Cl)+Na]+ 796.3",
      "ms_calculated_exact_mass": null,
      "description": "Boc-protected coupling product of 19a with bicyclooctyl tosylate 20k; intermediate en route to compound 37."
    },
    {
      "id": "C46",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-[3-({p-[(1s,4R)-4-[tert-butyl(oxycarbonylamino)]-4-methylcyclohexyloxy]phenyl}methyl)-4-chlorophenyl]tetrahydro-2H-pyran-2-yl]methyl Acetate (21k)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "59.8% by LC-MS",
      "ms_observed": "[M(35Cl)-Boc+H]+ 660.3, [M(37Cl)-Boc+H]+ 662.3",
      "ms_calculated_exact_mass": null,
      "description": "Boc-protected coupling product of 19a with 1-methylcyclohexyl tosylate 20l; intermediate en route to compound 38."
    },
    {
      "id": "C47",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-{3-[(p-{3-[tert-butyl(oxycarbonylamino)]-3-methylbutoxy}phenyl)methyl]-4-chlorophenyl}tetrahydro-2H-pyran-2-yl]methyl Acetate (21a)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "100.0% by LC-MS",
      "ms_observed": "[M(35Cl)-Boc+H]+ 634.2, [M(37Cl)-Boc+H]+ 636.2",
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu product of 19a with C2-linker alcohol 20a; intermediate en route to compound 26."
    },
    {
      "id": "C48",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-{3-[(p-{4-[tert-butyl(oxycarbonylamino)]-4-methylpentyloxy}phenyl)methyl]-4-chlorophenyl}tetrahydro-2H-pyran-2-yl]methyl Acetate (21b)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "100.0% by LC-MS",
      "ms_observed": "[M(35Cl)-Boc+H]+ 634.2, [M(37Cl)-Boc+H]+ 636.2",
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu product of 19a with gem-dimethyl C4 linker alcohol 20b; key intermediate en route to compound 27."
    },
    {
      "id": "C49",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-{3-[(p-{2-[tert-butyl(oxycarbonylamino)]ethoxy}phenyl)methyl]-4-chlorophenyl}tetrahydro-2H-pyran-2-yl]methyl Acetate (21c)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu product of 19a with C2 amino-alcohol 20c; intermediate en route to compound 28."
    },
    {
      "id": "C50",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-{3-[(p-{3-[tert-butyl(oxycarbonylamino)]propoxy}phenyl)methyl]-4-chlorophenyl}tetrahydro-2H-pyran-2-yl]methyl Acetate (21d)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu product of 19a with C3 amino-alcohol 20d; intermediate en route to compound 29."
    },
    {
      "id": "C51",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-{3-[(p-{4-[tert-butyl(oxycarbonylamino)]butoxy}phenyl)methyl]-4-chlorophenyl}tetrahydro-2H-pyran-2-yl]methyl Acetate (21e)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu product of 19a with C4 amino-alcohol 20e; intermediate en route to compound 30."
    },
    {
      "id": "C52",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{3-[(p-{4-[tert-butyl(oxycarbonylamino)]-4-methylpentyloxy}phenyl)methyl]-4-chlorophenyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate (21l)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "94.7% by LC-MS",
      "ms_observed": "[M(35Cl)-Boc+H]+ 590.4, [M(37Cl)-Boc+H]+ 592.0",
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu product of 19b (6-deoxy, Cl) with 20b; key intermediate en route to 6-deoxy compounds 60–63."
    },
    {
      "id": "C53",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{3-[(p-{4-[tert-butyl(oxycarbonylamino)]-4-methylpentyloxy}phenyl)methyl]-4-ethylphenyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate (21m)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 706.4, [M-Boc+H]+ 584.4",
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu product of 19c (6-deoxy, Et) with 20b; key intermediate en route to 64, 101, 124, 125."
    },
    {
      "id": "C54",
      "name": "(2R,3S,4R,5S,6S)-4,5-Diacetoxy-6-{3-[(p-{4-[tert-butyl(oxycarbonylamino)]-4-methylpentyloxy}phenyl)methyl]-4-chlorophenyl}-2-(methylthio)tetrahydro-2H-pyran-3-yl Acetate (21n)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu product of 19d (sotagliflozin-derived, SMe) with 20b; intermediate en route to 67–68."
    },
    {
      "id": "C55",
      "name": "(2S,3S,4R,5R,6R)-4-Acetoxy-2-{3-[(p-{4-[tert-butyl(oxycarbonylamino)]-4-methylpentyloxy}phenyl)methyl]-4-chlorophenyl}-5-fluoro-6-methyltetrahydro-2H-pyran-3-yl Acetate (21o)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "93.6% by LC-MS",
      "ms_observed": "[M(35Cl)-Boc+H]+ 550.2, [M(37Cl)-Boc+H]+ 552.2",
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu product of 19e (4-F, 6-deoxy) with 20b; intermediate en route to compound 69."
    },
    {
      "id": "C56",
      "name": "(2S,3S,4R,6R)-4-Acetoxy-2-{3-[(p-{4-[tert-butyl(oxycarbonylamino)]-4-methylpentyloxy}phenyl)methyl]-4-chlorophenyl}-5,5-difluoro-6-methyltetrahydro-2H-pyran-3-yl Acetate (21p)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu product of 19f (4,4-diF, 6-deoxy) with 20b; intermediate en route to compound 70."
    },
    {
      "id": "C57",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-(3-{[p-(3-{1-[tert-butyl(oxycarbonylamino)]cyclopropyl}propoxy)phenyl]methyl}-4-ethylphenyl)-2-methyltetrahydro-2H-pyran-3-yl Acetate (21q)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu product of 19c with spiro-cyclopropyl linker alcohol 20m; intermediate en route to compound 94."
    },
    {
      "id": "C58",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-(3-{[p-(3-{1-[tert-butyl(oxycarbonylamino)]cyclopentyl}propoxy)phenyl]methyl}-4-ethylphenyl)-2-methyltetrahydro-2H-pyran-3-yl Acetate (21r)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 732.4, [M-Boc+H]+ 610.3",
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu product of 19c with spiro-cyclopentyl linker alcohol 20n; intermediate en route to compound 95."
    },
    {
      "id": "C59",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-[3-({p-[(1S,3S)-3-[tert-butyl(oxycarbonylamino)]cyclopentyloxy]phenyl}methyl)-4-chlorophenyl]-2-methyltetrahydro-2H-pyran-3-yl Acetate (21s)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu product of 19b with enantiopure cyclopentyl alcohol 20o; intermediate en route to compound 97."
    },
    {
      "id": "C60",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{3-[(p-{4-[tert-butyl(oxycarbonylamino)]-4-methylpentyloxy}phenyl)methyl]-4-tolyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate (21u)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu product of 19g (R1=Me) with 20b; intermediate en route to compound 99."
    },
    {
      "id": "C61",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{3-[(p-{4-[tert-butyl(oxycarbonylamino)]-4-methylpentyloxy}phenyl)methyl]-4-cumenyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate (21v)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu product of 19h (R1=iPr) with 20b; intermediate en route to compound 100."
    },
    {
      "id": "C62",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-[3-({p-[(1S,3S)-3-[tert-butyl(oxycarbonylamino)]cyclopentyloxy]phenyl}methyl)-4-ethylphenyl]-2-methyltetrahydro-2H-pyran-3-yl Acetate (21w)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu product of 19c with enantiopure cyclopentyl alcohol 20o; intermediate en route to compounds 101, 126, 127."
    },
    {
      "id": "C63",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-[3-({p-[(1S,4R)-4-[tert-butyl(oxycarbonylamino)]cyclohexyloxy]phenyl}methyl)-4-chlorophenyl]-2-methyltetrahydro-2H-pyran-3-yl Acetate (21t)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M(35Cl)-Boc+H]+ 588.3, [M(37Cl)-Boc+H]+ 590.3",
      "ms_calculated_exact_mass": null,
      "description": "Nucleophilic coupling product of 19b with cyclohexyl tosylate 20p; intermediate en route to compound 98."
    },
    {
      "id": "C64",
      "name": "4-[p-({2-Chloro-5-[(2S,3S,4R,5R,6R)-3,4,5-triacetoxy-6-(acetoxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-2-methyl-2-butanammonium Trifluoroacetate (22a)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "85.9% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 634.2, [M(37Cl)+H]+ 636.2",
      "ms_calculated_exact_mass": null,
      "description": "TFA salt of free amine obtained by Boc deprotection of 21a; used in N-alkylation with 23a to give intermediate 24a en route to compound 26."
    },
    {
      "id": "C65",
      "name": "5-[p-({2-Chloro-5-[(2S,3S,4R,5R,6R)-3,4,5-triacetoxy-6-(acetoxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-2-methyl-2-pentanammonium Trifluoroacetate (22b)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "TFA salt of free amine from Boc deprotection of 21b; used in N-alkylation to give 24b, 24l, 24m, 24n (en route to 27, 46, 47, 48)."
    },
    {
      "id": "C66",
      "name": "2-[p-({2-Chloro-5-[(2S,3S,4R,5R,6R)-3,4,5-triacetoxy-6-(acetoxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]ethanammonium Trifluoroacetate (22c)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "TFA salt of C2-linker amine from Boc deprotection of 21c; en route to compound 28."
    },
    {
      "id": "C67",
      "name": "3-[p-({2-Chloro-5-[(2S,3S,4R,5R,6R)-3,4,5-triacetoxy-6-(acetoxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1-propanammonium Trifluoroacetate (22d)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "TFA salt of C3-linker amine from Boc deprotection of 21d; en route to compound 29."
    },
    {
      "id": "C68",
      "name": "4-[p-({2-Chloro-5-[(2S,3S,4R,5R,6R)-3,4,5-triacetoxy-6-(acetoxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1-butanammonium Trifluoroacetate (22e)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "TFA salt of C4-linker amine from Boc deprotection of 21e; en route to compound 30."
    },
    {
      "id": "C69",
      "name": "(1S,3S)-3-[p-({2-Chloro-5-[(2S,3S,4R,5R,6R)-3,4,5-triacetoxy-6-(acetoxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclopentanammonium Trifluoroacetate (22f)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "TFA salt of trans-cyclopentyl amine from Boc deprotection of 21f; used in N-alkylation to give 24f, 24o, 24p (en route to 32, 49, 50)."
    },
    {
      "id": "C70",
      "name": "3-[p-({2-Chloro-5-[(2S,3S,4R,5R,6R)-3,4,5-triacetoxy-6-(acetoxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclohexanammonium Trifluoroacetate (22g)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "70.3% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 646.2, [M(37Cl)+H]+ 648.2",
      "ms_calculated_exact_mass": null,
      "description": "TFA salt of 3-cyclohexyl amine from Boc deprotection of 21g; en route to compound 33."
    },
    {
      "id": "C71",
      "name": "4-[p-({2-Chloro-5-[(2S,3S,4R,5R,6R)-3,4,5-triacetoxy-6-(acetoxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclohexanammonium Trifluoroacetate (22h)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "TFA salt of 4-cyclohexyl amine from Boc deprotection of 21h; en route to compound 34."
    },
    {
      "id": "C72",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-(4-chloro-3-{[p-(3-pyrrolidinyloxy)phenyl]methyl}phenyl)tetrahydro-2H-pyran-2-yl]methyl Acetate (22i)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Free pyrrolidine amine from TFA deprotection of 21i; en route to compound 35."
    },
    {
      "id": "C73",
      "name": "{5-[p-({2-Chloro-5-[(2S,3S,4R,5R,6R)-3,4,5-triacetoxy-6-(acetoxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]bicyclo[2.2.2]oct-2-yl}-λ4-azanylium Trifluoroacetate (22j)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "94.1% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 672.3, [M(37Cl)+H]+ 674.3",
      "ms_calculated_exact_mass": null,
      "description": "TFA salt of bicyclooctyl amine from Boc deprotection of 21j; en route to compound 37."
    },
    {
      "id": "C74",
      "name": "(1R,4S)-4-[p-({2-Chloro-5-[(2S,3S,4R,5R,6R)-3,4,5-triacetoxy-6-(acetoxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1-methylcyclohexanammonium Trifluoroacetate (22k)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "TFA salt of 1-methylcyclohexyl amine from Boc deprotection of 21k; en route to compound 38."
    },
    {
      "id": "C75",
      "name": "5-[p-({2-Chloro-5-[(2S,3S,4S,5R,6R)-3,4,5-triacetoxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-2-methyl-2-pentanammonium Trifluoroacetate (22l)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "TFA salt of 6-deoxy, Cl-series free amine from Boc deprotection of 21l; used in N-alkylation to give 24q, 24r, 24s, 24t (en route to 60–63)."
    },
    {
      "id": "C76",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-(3-{[p-(4-amino-4-methylpentyloxy)phenyl]methyl}-4-ethylphenyl)-2-methyltetrahydro-2H-pyran-3-yl Acetate (22m)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "96.1% by LC-MS",
      "ms_observed": "[M+H]+ 584.3",
      "ms_calculated_exact_mass": null,
      "description": "Free amine from TMSI-mediated Boc deprotection of 21m (Et series); used in N-alkylation with 23d to give compound 64."
    },
    {
      "id": "C77",
      "name": "5-[p-({2-Chloro-5-[(2S,3S,4R,5R,6R)-3,4-diacetoxy-5-fluoro-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-2-methyl-2-pentanammonium Trifluoroacetate (22n)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "TFA salt of 4-fluoro, 6-deoxy free amine from Boc deprotection of 21o; en route to compound 69."
    },
    {
      "id": "C78",
      "name": "5-[p-({2-Chloro-5-[(2S,3S,4R,6R)-3,4-diacetoxy-5,5-difluoro-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-2-methyl-2-pentanammonium Trifluoroacetate (22o)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "TFA salt of 4,4-difluoro, 6-deoxy free amine from Boc deprotection of 21p; en route to compound 70."
    },
    {
      "id": "C79",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-[3-({p-[(1S,3S)-3-aminocyclopentyloxy]phenyl}methyl)-4-chlorophenyl]-2-methyltetrahydro-2H-pyran-3-yl Acetate (22p)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Free amine from Boc deprotection of 21s; en route to compound 97."
    },
    {
      "id": "C80",
      "name": "(1R,4S)-4-[p-({2-Chloro-5-[(2S,3S,4S,5R,6R)-3,4,5-triacetoxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclohexanammonium Trifluoroacetate (22q)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "TFA salt of cis-1,4-cyclohexyl amine from Boc deprotection of 21t; en route to compound 98."
    },
    {
      "id": "C81",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-(4-chloro-3-{[p-(3-{2-[(S)-2-cyano-1-pyrrolidinyl]-2-oxoethylamino}-3-methylbutoxy)phenyl]methyl}phenyl)tetrahydro-2H-pyran-2-yl]methyl Acetate (24a)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "81.7% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 770.3, [M(37Cl)+H]+ 772.3",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22a with 23a; penultimate protected intermediate en route to compound 26."
    },
    {
      "id": "C82",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-(4-chloro-3-{[p-(4-{2-[(S)-2-cyano-1-pyrrolidinyl]-2-oxoethylamino}-4-methylpentyloxy)phenyl]methyl}phenyl)tetrahydro-2H-pyran-2-yl]methyl Acetate (24b)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "66.7% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 784.3, [M(37Cl)+H]+ 786.3",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22b with 23a; penultimate protected intermediate en route to compound 27."
    },
    {
      "id": "C83",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-(4-chloro-3-{[p-(2-{2-[(S)-2-cyano-1-pyrrolidinyl]-2-oxoethylamino}ethoxy)phenyl]methyl}phenyl)tetrahydro-2H-pyran-2-yl]methyl Acetate (24c)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22c with 23a; penultimate protected intermediate en route to compound 28."
    },
    {
      "id": "C84",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-(4-chloro-3-{[p-(3-{2-[(S)-2-cyano-1-pyrrolidinyl]-2-oxoethylamino}propoxy)phenyl]methyl}phenyl)tetrahydro-2H-pyran-2-yl]methyl Acetate (24d)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "29.9% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 742.3, [M(37Cl)+H]+ 744.3",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22d with 23a; penultimate protected intermediate en route to compound 29."
    },
    {
      "id": "C85",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-(4-chloro-3-{[p-(4-{2-[(S)-2-cyano-1-pyrrolidinyl]-2-oxoethylamino}butoxy)phenyl]methyl}phenyl)tetrahydro-2H-pyran-2-yl]methyl Acetate (24e)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "46.5% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 756.3, [M(37Cl)+H]+ 758.3",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22e with 23a; penultimate protected intermediate en route to compound 30."
    },
    {
      "id": "C86",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-[4-chloro-3-({p-[(1S,3S)-3-{2-[(S)-2-cyano-1-pyrrolidinyl]-2-oxoethylamino}cyclopentyloxy]phenyl}methyl)phenyl]tetrahydro-2H-pyran-2-yl]methyl Acetate (24f)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M(35Cl)+H]+ 768.4, [M(37Cl)+H]+ 770.4",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22f with 23a; penultimate protected intermediate en route to compound 32."
    },
    {
      "id": "C87",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-(4-chloro-3-{[p-(3-{2-[(S)-2-cyano-1-pyrrolidinyl]-2-oxoethylamino}cyclohexyloxy)phenyl]methyl}phenyl)tetrahydro-2H-pyran-2-yl]methyl Acetate (24g)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M(35Cl)+H]+ 782.3, [M(37Cl)+H]+ 784.4",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22g with 23a; penultimate protected intermediate en route to compound 33."
    },
    {
      "id": "C88",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-(4-chloro-3-{[p-(4-{2-[(S)-2-cyano-1-pyrrolidinyl]-2-oxoethylamino}cyclohexyloxy)phenyl]methyl}phenyl)tetrahydro-2H-pyran-2-yl]methyl Acetate (24h)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "45.2% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 782.3, [M(37Cl)+H]+ 784.3",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22h with 23a; penultimate protected intermediate en route to compound 34."
    },
    {
      "id": "C89",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-(4-chloro-3-{[p-(1-{2-[(2S,4S)-2-cyano-4-fluoro-1-pyrrolidinyl]-2-oxoethyl}-3-pyrrolidinyloxy)phenyl]methyl}phenyl)tetrahydro-2H-pyran-2-yl]methyl Acetate (24i)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "37.3% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 772.4, [M(37Cl)+H]+ 774.4",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22i with 23b; penultimate protected intermediate en route to compound 35."
    },
    {
      "id": "C90",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-(4-chloro-3-{[p-(5-{2-[(2S,4S)-2-cyano-4-fluoro-1-pyrrolidinyl]-2-oxoethylamino}bicyclo[2.2.2]oct-2-yloxy)phenyl]methyl}phenyl)tetrahydro-2H-pyran-2-yl]methyl Acetate (24j)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "46.3% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 826.2, [M(37Cl)+H]+ 828.3",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22j with 23b; penultimate protected intermediate en route to compound 37."
    },
    {
      "id": "C91",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-[4-chloro-3-({p-[(1R,4R)-4-{2-[(2S,4S)-2-cyano-4-fluoro-1-pyrrolidinyl]-2-oxoethylamino}-4-methylcyclohexyloxy]phenyl}methyl)phenyl]tetrahydro-2H-pyran-2-yl]methyl Acetate (24k)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "61.7% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 814.3, [M(37Cl)+H]+ 816.3",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22k with 23b; penultimate protected intermediate en route to compound 38."
    },
    {
      "id": "C92",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-(4-chloro-3-{[p-(4-{2-[(S)-4-cyano-1,3-thiazolidin-3-yl]-2-oxoethylamino}-4-methylpentyloxy)phenyl]methyl}phenyl)tetrahydro-2H-pyran-2-yl]methyl Acetate (24l)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M(35Cl)+H]+ 802.3, [M(37Cl)+H]+ 804.3",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22b with thiazolidine alkylating agent 23c; penultimate protected intermediate en route to compound 46."
    },
    {
      "id": "C93",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-(4-chloro-3-{[p-(4-{2-[(2S,4S)-2-cyano-4-fluoro-1-pyrrolidinyl]-2-oxoethylamino}-4-methylpentyloxy)phenyl]methyl}phenyl)tetrahydro-2H-pyran-2-yl]methyl Acetate (24m)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "67.2% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 802.3, [M(37Cl)+H]+ 804.3",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22b with 23b; penultimate protected intermediate en route to compound 47."
    },
    {
      "id": "C94",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-(4-chloro-3-{[p-(4-{2-[(1S,3S,5S)-3-cyano-2-azabicyclo[3.1.0]hex-2-yl]-2-oxoethylamino}-4-methylpentyloxy)phenyl]methyl}phenyl)tetrahydro-2H-pyran-2-yl]methyl Acetate (24n)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "58.6% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 796.4, [M(37Cl)+H]+ 798.4",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22b with bicyclic alkylating agent 58; penultimate protected intermediate en route to compound 48."
    },
    {
      "id": "C95",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-[4-chloro-3-({p-[(1R,3S)-3-{2-[(2S,4S)-2-cyano-4-fluoro-1-pyrrolidinyl]-2-oxoethylamino}cyclopentyloxy]phenyl}methyl)phenyl]tetrahydro-2H-pyran-2-yl]methyl Acetate (24o)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "65.5% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 786.4, [M(37Cl)+H]+ 788.4",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22f with 23b; penultimate protected intermediate en route to compound 49."
    },
    {
      "id": "C96",
      "name": "[(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-[4-chloro-3-({p-[(1R,3S)-3-{2-[(S)-2-cyano-4,4-difluoro-1-pyrrolidinyl]-2-oxoethylamino}cyclopentyloxy]phenyl}methyl)phenyl]tetrahydro-2H-pyran-2-yl]methyl Acetate (24p)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "58.3% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 804.4, [M(37Cl)+H]+ 806.4",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22f with 23d; penultimate protected intermediate en route to compound 50."
    },
    {
      "id": "C97",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-(4-chloro-3-{[p-(4-{2-[(S)-4-cyano-1,3-thiazolidin-3-yl]-2-oxoethylamino}-4-methylpentyloxy)phenyl]methyl}phenyl)-2-methyltetrahydro-2H-pyran-3-yl Acetate (24q)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "78.5% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 744.3, [M(37Cl)+H]+ 746.3",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22l with 23c; penultimate protected intermediate en route to compound 60."
    },
    {
      "id": "C98",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-(4-chloro-3-{[p-(4-{2-[(S)-2-cyano-4,4-difluoro-1-pyrrolidinyl]-2-oxoethylamino}-4-methylpentyloxy)phenyl]methyl}phenyl)-2-methyltetrahydro-2H-pyran-3-yl Acetate (24r)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22l with 23d; penultimate protected intermediate en route to compound 61."
    },
    {
      "id": "C99",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-(4-chloro-3-{[p-(4-{2-[(1S,3S,5S)-3-cyano-2-azabicyclo[3.1.0]hex-2-yl]-2-oxoethylamino}-4-methylpentyloxy)phenyl]methyl}phenyl)-2-methyltetrahydro-2H-pyran-3-yl Acetate (24s)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "90.3% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 738.3, [M(37Cl)+H]+ 740.3",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22l with bicyclic alkylating agent 58; penultimate protected intermediate en route to compound 62."
    },
    {
      "id": "C100",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-(4-chloro-3-{[p-(4-{2-[(2S,4S)-2-cyano-4-fluoro-1-pyrrolidinyl]-2-oxoethylamino}-4-methylpentyloxy)phenyl]methyl}phenyl)-2-methyltetrahydro-2H-pyran-3-yl Acetate (24t)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "71.1% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 744.3, [M(37Cl)+H]+ 745.9",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22l with 23b; penultimate protected intermediate en route to compound 63."
    },
    {
      "id": "C101",
      "name": "(2S,3S,4R,5R,6R)-4-Acetoxy-2-(4-chloro-3-{[p-(4-{2-[(2S,4S)-2-cyano-4-fluoro-1-pyrrolidinyl]-2-oxoethylamino}-4-methylpentyloxy)phenyl]methyl}phenyl)-5-fluoro-6-methyltetrahydro-2H-pyran-3-yl Acetate (24u)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "85.2% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 704.3, [M(37Cl)+H]+ 706.3",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22n with 23b; penultimate protected intermediate en route to compound 69."
    },
    {
      "id": "C102",
      "name": "(2S,3S,4R,6R)-4-Acetoxy-2-(4-chloro-3-{[p-(4-{2-[(2S,4S)-2-cyano-4-fluoro-1-pyrrolidinyl]-2-oxoethylamino}-4-methylpentyloxy)phenyl]methyl}phenyl)-5,5-difluoro-6-methyltetrahydro-2H-pyran-3-yl Acetate (24v)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "87.7% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 722.2, [M(37Cl)+H]+ 724.2",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22o with 23b; penultimate protected intermediate en route to compound 70."
    },
    {
      "id": "C103",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-[4-chloro-3-({p-[(1S,3S)-3-{2-[(2S,4S)-2-cyano-4-fluoro-1-pyrrolidinyl]-2-oxoethylamino}cyclopentyloxy]phenyl}methyl)phenyl]-2-methyltetrahydro-2H-pyran-3-yl Acetate (24w)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "54.2% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 728.3, [M(37Cl)+H]+ 730.0",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22p with 23b; penultimate protected intermediate en route to compound 97."
    },
    {
      "id": "C104",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-[4-chloro-3-({p-[(1R,4R)-4-{2-[(2S,4S)-2-cyano-4-fluoro-1-pyrrolidinyl]-2-oxoethylamino}cyclohexyloxy]phenyl}methyl)phenyl]-2-methyltetrahydro-2H-pyran-3-yl Acetate (24x)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "83.8% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 742.3, [M(37Cl)+H]+ 743.9",
      "ms_calculated_exact_mass": null,
      "description": "N-alkylation product of 22q with 23b; penultimate protected intermediate en route to compound 98."
    },
    {
      "id": "C105",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-(3-{[p-(4-{2-[(S)-2-cyano-4,4-difluoro-1-pyrrolidinyl]-2-oxoethylamino}-4-methylpentyloxy)phenyl]methyl}-4-ethylphenyl)-2-methyltetrahydro-2H-pyran-3-yl Acetate (compound 64)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "99.4% by LC-MS",
      "ms_observed": "[M+H]+ 756.3",
      "ms_calculated_exact_mass": null,
      "description": "Triple SGLT1/SGLT2/DPP4 inhibitor screening compound (lead); triacetylated prodrug of compound 101; R1=Et, C4 gem-dimethyl linker, 4,4-difluoro-2-cyanopyrrolidine DPP4 motif."
    },
    {
      "id": "C106",
      "name": "(S)-1-(2-{3-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylpropylamino}acetyl)-2-pyrrolidinecarbonitrile (compound 26)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "99.0% by LC-MS",
      "ms_observed": "[M(35Cl)-H]- 602.3, [M(37Cl)-H]- 604.3",
      "ms_calculated_exact_mass": null,
      "description": "Triple inhibitor screening compound with C2 gem-dimethyl linker and 2-cyanopyrrolidine DPP4 motif; first library compound."
    },
    {
      "id": "C107",
      "name": "(S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-2-pyrrolidinecarbonitrile (compound 27)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "100.0% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 616.2, [M(37Cl)+H]+ 618.2",
      "ms_calculated_exact_mass": null,
      "description": "Priority early lead compound; C4 gem-dimethyl linker, 2-cyanopyrrolidine DPP4 motif; dapagliflozin-based triple inhibitor."
    },
    {
      "id": "C108",
      "name": "(S)-1-(2-{2-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]ethylamino}acetyl)-2-pyrrolidinecarbonitrile (compound 28)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "95.9% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 560.3, [M(37Cl)+H]+ 562.2",
      "ms_calculated_exact_mass": null,
      "description": "Triple inhibitor screening compound with C2 ethylene linker and 2-cyanopyrrolidine DPP4 motif."
    },
    {
      "id": "C109",
      "name": "(S)-1-(2-{3-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]propylamino}acetyl)-2-pyrrolidinecarbonitrile (compound 29)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "94.6% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 574.2, [M(37Cl)+H]+ 576.2",
      "ms_calculated_exact_mass": null,
      "description": "Triple inhibitor screening compound with C3 propylene linker and 2-cyanopyrrolidine DPP4 motif."
    },
    {
      "id": "C110",
      "name": "(S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]butylamino}acetyl)-2-pyrrolidinecarbonitrile (compound 30)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "98.6% by HPLC; 96.9% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 588.2, [M(37Cl)+H]+ 590.2",
      "ms_calculated_exact_mass": null,
      "description": "Triple inhibitor screening compound with C4 butylene linker and 2-cyanopyrrolidine DPP4 motif."
    },
    {
      "id": "C111",
      "name": "(S)-1-(2-{3-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclopentylamino}acetyl)-2-pyrrolidinecarbonitrile (compound 31)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "99.0% by HPLC; 97.5% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 600.2, [M(37Cl)+H]+ 602.2",
      "ms_calculated_exact_mass": null,
      "description": "Triple inhibitor with unspecified racemic cyclopentyl linker; prepared via Scheme S2 (route 2 variant)."
    },
    {
      "id": "C112",
      "name": "(S)-1-{2-[(1S,3S)-3-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclopentylamino]acetyl}-2-pyrrolidinecarbonitrile (compound 32)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "98.9% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 600.2, [M(37Cl)+H]+ 602.2",
      "ms_calculated_exact_mass": null,
      "description": "Triple inhibitor with trans-1,3-cyclopentyl linker (backup prioritized linker) and 2-cyanopyrrolidine DPP4 motif."
    },
    {
      "id": "C113",
      "name": "(S)-1-(2-{3-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclohexylamino}acetyl)-2-pyrrolidinecarbonitrile (compound 33)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "99.6% by HPLC; 99.3% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 614.2, [M(37Cl)+H]+ 616.2",
      "ms_calculated_exact_mass": null,
      "description": "Triple inhibitor with 3-cyclohexyl linker and 2-cyanopyrrolidine DPP4 motif."
    },
    {
      "id": "C114",
      "name": "(S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclohexylamino}acetyl)-2-pyrrolidinecarbonitrile (compound 34)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "99.6% by HPLC; 100.0% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 614.2, [M(37Cl)+H]+ 616.2",
      "ms_calculated_exact_mass": null,
      "description": "Triple inhibitor with 4-cyclohexyl linker and 2-cyanopyrrolidine DPP4 motif."
    },
    {
      "id": "C115",
      "name": "(2S,4S)-1-(2-{3-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1-pyrrolidinyl}acetyl)-4-fluoro-2-pyrrolidinecarbonitrile (compound 35)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "99.8% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 604.4, [M(37Cl)+H]+ 606.4",
      "ms_calculated_exact_mass": null,
      "description": "Triple inhibitor with pyrrolidine O-linker (gosogliptin-16-inspired) and 4-fluoro-2-cyanopyrrolidine DPP4 motif."
    },
    {
      "id": "C116",
      "name": "L-Hydroxyproline (39)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Commercial amino acid used as starting material for synthesis of Boc-hydroxyproline 40 (Scheme 2)."
    },
    {
      "id": "C117",
      "name": "(2R,4R)-1-tert-Butoxycarbonyl-4-hydroxy-2-pyrrolidinecarboxylic Acid (40)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "100.0% by LC-MS",
      "ms_observed": "[M-H]- 230.1",
      "ms_calculated_exact_mass": null,
      "description": "N-Boc hydroxyproline prepared from L-hydroxyproline 39 and Boc2O; key intermediate for Scheme 2 synthesis of compound 36."
    },
    {
      "id": "C118",
      "name": "(S)-1-Boc-2-cyanopyrrolidine (41)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Commercial Boc-protected 2-cyanopyrrolidine; deprotected with TsOH to give pyrrolidinium tosylate 42 (Scheme 2)."
    },
    {
      "id": "C119",
      "name": "(S)-1-Pyrrolidinium-2-carbonitrile P-toluenesulfate (42)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "TsOH salt of 2-cyanopyrrolidine prepared from Boc-compound 41 by acid deprotection; used in EDC/HOBt coupling with 40 to give 43."
    },
    {
      "id": "C120",
      "name": "tert-Butyl (2S,4R)-2-{[(S)-2-cyano-1-pyrrolidinyl]carbonyl}-4-hydroxy-1-pyrrolidinecarboxylate (43)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "97.7% by LC-MS",
      "ms_observed": "[M-Boc+H]+ 210.1",
      "ms_calculated_exact_mass": null,
      "description": "Amide coupling product of 40 and 42; hydroxypyrrolidine intermediate en route to compound 36 (Scheme 2)."
    },
    {
      "id": "C121",
      "name": "tert-Butyl (2S,4R)-2-{[(S)-2-Cyano-1-pyrrolidinyl]carbonyl}-4-(tosyloxy)-1-pyrrolidinecarboxylate (44)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Tosylate of 43 prepared with TsCl/pyridine; electrophilic coupling partner with 19a for synthesis of compound 36."
    },
    {
      "id": "C122",
      "name": "tert-Butyl (2S,4S)-4-[p-({2-Chloro-5-[(2S,3S,4R,5R,6R)-3,4,5-triacetoxy-6-(acetoxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-2-{[(S)-2-cyano-1-pyrrolidinyl]carbonyl}-1-pyrrolidinecarboxylate (45)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M(35Cl)-Boc+H]+ 740.3, [M(37Cl)-Boc+H]+ 742.3",
      "ms_calculated_exact_mass": null,
      "description": "Cs2CO3-mediated O-alkylation product of 19a with tosylate 44; penultimate protected intermediate en route to compound 36."
    },
    {
      "id": "C123",
      "name": "(S)-1-{[(2S,4S)-4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-2-pyrrolidinyl]carbonyl}-2-pyrrolidinecarbonitrile (compound 36)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "92.0% by HPLC; 88.9% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 572.2, [M(37Cl)+H]+ 574.3",
      "ms_calculated_exact_mass": null,
      "description": "Triple inhibitor with gosogliptin/teneligliptin-type 2,4-disubstituted pyrrolidine linker; prepared via Scheme 2."
    },
    {
      "id": "C124",
      "name": "(2S,4S)-1-(2-{5-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]bicyclo[2.2.2]oct-2-ylamino}acetyl)-4-fluoro-2-pyrrolidinecarbonitrile (compound 37)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "99.2% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 658.3, [M(37Cl)+H]+ 660.3",
      "ms_calculated_exact_mass": null,
      "description": "Triple inhibitor with bicyclo[2.2.2]octyl linker (adamantane-skeleton inspired) and 4-fluoro-2-cyanopyrrolidine DPP4 motif."
    },
    {
      "id": "C125",
      "name": "(2S,4S)-1-{2-[(1R,4R)-4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1-methylcyclohexylamino]acetyl}-4-fluoro-2-pyrrolidinecarbonitrile (compound 38)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "100.0% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 646.3, [M(37Cl)+H]+ 648.3",
      "ms_calculated_exact_mass": null,
      "description": "Triple inhibitor with 1-methylcyclohexyl linker and 4-fluoro-2-cyanopyrrolidine DPP4 motif."
    },
    {
      "id": "C126",
      "name": "Boc-D-thiazolidine-4-carboxylic acid (52)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Commercial N-Boc thiazolidine carboxylic acid; starting material for synthesis of thiazolidine alkylating agent 23c (Scheme 3)."
    },
    {
      "id": "C127",
      "name": "tert-Butyl (S)-4-Carbamoyl-1,3-thiazolidine-3-carboxylate (53)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M-Boc+H]+ 133.1",
      "ms_calculated_exact_mass": null,
      "description": "Primary amide intermediate from mixed anhydride coupling of 52 with NH4OH; en route to 23c (Scheme 3)."
    },
    {
      "id": "C128",
      "name": "tert-Butyl (S)-4-Cyano-1,3-thiazolidine-3-carboxylate (54)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "TFAA-mediated dehydration product of amide 53 to nitrile; en route to 23c (Scheme 3)."
    },
    {
      "id": "C129",
      "name": "(S)-1,3-Thiazolidin-3-ium-4-carbonitrile p-Toluenesulfonate (55)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "TsOH salt of thiazolidine carbonitrile from Boc removal of 54; used in chloroacetylation to give 23c (Scheme 3)."
    },
    {
      "id": "C130",
      "name": "ethyl chloroformate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Mixed anhydride-forming reagent used in amidation of 52 with NH4OH (Scheme 3)."
    },
    {
      "id": "C131",
      "name": "TFAA (trifluoroacetic anhydride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Dehydrating agent for amide-to-nitrile conversion and for deprotection steps in Scheme 3."
    },
    {
      "id": "C132",
      "name": "chloroacetyl chloride",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acylating agent used in final step for synthesis of alkylating agents 23c and 58."
    },
    {
      "id": "C133",
      "name": "(1S,3S,5S)-2-Azabicyclo[3.1.0]hexane-3-carbonitrile (Boc-protected) starting material (56)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Commercially available Boc-protected bicyclic azabicyclo[3.1.0]hexane building block; starting material for synthesis of alkylating agent 58 (Scheme 3)."
    },
    {
      "id": "C134",
      "name": "(1S,3S,5S)-2-Azabicyclo[3.1.0]hexan-2-ium-3-carbonitrile p-Toluenesulfonate (57)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "TsOH salt of bicyclic cyanopyrrolidine analogue from TFAA deprotection of 56 followed by TsOH treatment; used in chloroacetylation to give 58 (Scheme 3)."
    },
    {
      "id": "C135",
      "name": "3,3-Difluoropyrrolidine hydrochloride",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Commercial reagent used in EDC/HOBt amide coupling with 40 to give the alcohol intermediate en route to tosylate 59 (Scheme 4)."
    },
    {
      "id": "C136",
      "name": "tert-Butyl (2S,4R)-2-[(3,3-Difluoro-1-pyrrolidinyl)carbonyl]-4-(tosyloxy)-1-pyrrolidinecarboxylate (59)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "100.0% by LC-MS",
      "ms_observed": "[M-tBu]- 263.1, [M]- 319.1",
      "ms_calculated_exact_mass": null,
      "description": "Tosylated difluoropyrrolidine-hydroxyproline amide; preformed coupling partner containing both linker and DPP4 motif, used with 19a to give 45→compound 51 (Scheme 4)."
    },
    {
      "id": "C137",
      "name": "[(2S,4R)-4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-2-pyrrolidinyl](3,3-difluoro-1-pyrrolidinyl)methanone (compound 51)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "99.9% by HPLC; 99.6% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 583.2, [M(37Cl)+H]+ 585.3",
      "ms_calculated_exact_mass": null,
      "description": "Difluorinated gosogliptin-type linker analogue of compound 36; prepared via Scheme 4."
    },
    {
      "id": "C138",
      "name": "(3R,4S,5S,6S)-2-{4-Chloro-3-[(p-ethoxyphenyl)methyl]phenyl}-6-(iodomethyl)-2-methoxytetrahydro-4H-pyran-3,4,5-triol (72)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Appel iodination product of known intermediate 71 (dapagliflozin synthesis intermediate); en route to 6-deoxy building block 18b (Scheme 5)."
    },
    {
      "id": "C139",
      "name": "Compound 71 (dapagliflozin synthesis intermediate with 4-ethoxyphenethyl group)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Known dapagliflozin synthesis intermediate (patent literature); starting material for Scheme 5 synthesis of 6-deoxy building block 18b."
    },
    {
      "id": "C140",
      "name": "(2S,3S,4S,5R)-4,5-Diacetoxy-6-{4-chloro-3-[(p-ethoxyphenyl)methyl]phenyl}-2-(iodomethyl)-6-methoxytetrahydro-2H-pyran-3-yl Acetate (73)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Peracetylated iodo-methyl intermediate; deiodinated by hydrogenation to give 6-deoxy analogue en route to 18b (Scheme 5)."
    },
    {
      "id": "C141",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{4-chloro-3-[(p-ethoxyphenyl)methyl]phenyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate (18b)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "95.9% by LC-MS",
      "ms_observed": "[M(35Cl)+Na]+ 541.0, [M(37Cl)+Na]+ 543.0",
      "ms_calculated_exact_mass": null,
      "description": "6-Deoxy C-glucoside with Cl core and ethoxy protecting group; key building block for 6-deoxy series (Scheme 5); dealkylated to 19b."
    },
    {
      "id": "C142",
      "name": "N-heterocyclic carbene borane 74 (triisopropylphosphine borane of 4-ethylphenyl boronate)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Known NHC-borane coupling partner (Monot et al. 2009); used in Suzuki-Miyaura coupling with 18b to directly produce 18c (Scheme 5)."
    },
    {
      "id": "C143",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{3-[(p-ethoxyphenyl)methyl]-4-ethylphenyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate (18c)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M+Na]+ 535.1",
      "ms_calculated_exact_mass": null,
      "description": "6-Deoxy C-glucoside with Et core group; Suzuki-Miyaura coupling product of 18b with NHC-borane 74 (Scheme 5); dealkylated to 19c."
    },
    {
      "id": "C144",
      "name": "Pd(OAc)2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "catalyst",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Palladium acetate catalyst used in Suzuki-Miyaura couplings (Schemes 5, 6, 10)."
    },
    {
      "id": "C145",
      "name": "RuPhos (2-dicyclohexylphosphino-2',6'-diisopropoxybiphenyl)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "catalyst",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Buchwald phosphine ligand for Pd-catalyzed Suzuki cross-coupling reactions."
    },
    {
      "id": "C146",
      "name": "(2R,3S,4R,5S,6S)-4,5-Diacetoxy-6-{4-chloro-3-[(p-hydroxyphenyl)methyl]phenyl}-2-(methylthio)tetrahydro-2H-pyran-3-yl Acetate (18d); triacetyl sotagliflozin",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Triacetyl sotagliflozin prepared by direct acetylation of sotagliflozin 6 (commercially sourced reference compound) with Ac2O/pyridine/DMAP; used to give 19d after BBr3 dealkylation."
    },
    {
      "id": "C147",
      "name": "(2S,3R,4R,5S,6S)-2-{4-Chloro-3-[(p-ethoxyphenyl)methyl]phenyl}-6-(iodomethyl)tetrahydro-4H-pyran-3,4,5-triol (75)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Appel iodination product of dapagliflozin 2 (commercially sourced); starting point for Scheme 6 (spiro-cyclopropyl analogue 65)."
    },
    {
      "id": "C148",
      "name": "dapagliflozin 2",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Commercially sourced dapagliflozin used directly as substrate for iodination (Scheme 6) and acetylation (18d preparation)."
    },
    {
      "id": "C149",
      "name": "(5S,6R,7R,8S)-5-{4-Chloro-3-[(p-ethoxyphenyl)methyl]phenyl}-4-oxa-6,7,8-spiro[2.5]octanetriol (76)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Spiro-cyclopropyl intermediate obtained from 75 by NaOMe-mediated elimination and Simmons-Smith cyclopropanation (Scheme 6)."
    },
    {
      "id": "C150",
      "name": "(5S,6S,7R,8S)-6,7-Diacetoxy-5-{4-ethyl-3-[(p-hydroxyphenyl)methyl]phenyl}-4-oxa-8-spiro[2.5]octyl Acetate (77)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Peracetylated free phenol spiro-cyclopropyl intermediate with Et core; key intermediate for compound 65 (Scheme 6)."
    },
    {
      "id": "C151",
      "name": "(5S,6S,7R,8S)-6,7-Diacetoxy-5-{3-[(p-{4-[tert-butyl(oxycarbonylamino)]-4-methylpentyloxy}phenyl)methyl]-4-ethylphenyl}-4-oxa-8-spiro[2.5]octyl Acetate (78)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "81.9% by LC-MS",
      "ms_observed": "[M-BocNH]+ 579.1",
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu coupling product of 77 with 20b; Boc-protected penultimate intermediate en route to compound 65 (Scheme 6)."
    },
    {
      "id": "C152",
      "name": "(S)-1-(2-{4-[p-({2-Ethyl-5-[(5S,6R,7R,8S)-6,7,8-trihydroxy-4-oxa-5-spiro[2.5]octyl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile (compound 65)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "98.1% by LC-MS",
      "ms_observed": "[M+H]+ 642.3",
      "ms_calculated_exact_mass": null,
      "description": "Triple inhibitor with spiro-cyclopropyl C5 modification, Et core, C4 gem-dimethyl linker, and 4,4-difluoro-2-cyanopyrrolidine DPP4 motif (Scheme 6)."
    },
    {
      "id": "C153",
      "name": "Compound 79 (allyloxy ertugliflozin analogue with p-ethoxyphenyl group)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Initial allyl-protected bicyclic ertugliflozin analogue with p-ethoxy distal ring; synthesis referenced to Scheme S3."
    },
    {
      "id": "C154",
      "name": "[(2S,3S,4R)-2,3,4-Triacetoxy-5-{4-chloro-3-[(p-hydroxyphenyl)methyl]phenyl}-6,8-dioxabicyclo[3.2.1]oct-1-yl]methyl Acetate (80)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M(35Cl)-H]- 575.1, [M(37Cl)-H]- 577.1",
      "ms_calculated_exact_mass": null,
      "description": "Pd(PPh3)4/1,3-dimethylbarbituric acid allyl deprotection product of 79 after peracetylation; free phenol ertugliflozin analogue (Scheme 7)."
    },
    {
      "id": "C155",
      "name": "4-[p-({2-Chloro-5-[(2S,3S,4R)-2,3,4-trihydroxy-1-(hydroxymethyl)-6,8-dioxabicyclo[3.2.1]oct-5-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutyl 2-Methyl-2-propanecarbamate (81)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M(35Cl)-Boc+H]+ 676.3, [M(37Cl)-Boc+H]+ 678.2",
      "ms_calculated_exact_mass": null,
      "description": "Mitsunobu coupling product of 80 with 20b followed by LiOH deacetylation; Boc-protected intermediate (Scheme 7)."
    },
    {
      "id": "C156",
      "name": "4-[p-({2-Chloro-5-[(2S,3S,4R)-2,3,4-trihydroxy-1-methyl-6,8-dioxabicyclo[3.2.1]oct-5-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutyl 2-Methyl-2-propanecarbamate (82)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M(35Cl)-Boc+H]+ 492.1, [M(37Cl)-Boc+H]+ 494.1",
      "ms_calculated_exact_mass": null,
      "description": "6-Deoxy ertugliflozin analogue obtained by iodination/hydrogenation of 81; Boc-protected intermediate (Scheme 7)."
    },
    {
      "id": "C157",
      "name": "vinylboronic acid pinacol ester",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Boronate ester used in Suzuki-Miyaura coupling with aryl chloride 82 (SPhos Pd G3 catalyst) to install vinyl group en route to ethyl group (Scheme 7)."
    },
    {
      "id": "C158",
      "name": "SPhos Pd G3 (third-generation Buchwald palladium precatalyst)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "catalyst",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Palladium precatalyst used in Suzuki-Miyaura coupling of aryl chloride 82 with vinylboronic acid pinacol ester (Scheme 7)."
    },
    {
      "id": "C159",
      "name": "4-[p-({2-Ethyl-5-[(2S,3S,4R)-2,3,4-trihydroxy-1-methyl-6,8-dioxabicyclo[3.2.1]oct-5-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutyl 2-Methyl-2-propanecarbamate (83)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Suzuki-Miyaura/hydrogenation product installing Et group on 82; Boc-protected intermediate en route to compound 66 (Scheme 7)."
    },
    {
      "id": "C160",
      "name": "5-[p-({2-Ethyl-5-[(2S,3S,4R)-2,3,4-trihydroxy-1-methyl-6,8-dioxabicyclo[3.2.1]oct-5-yl]phenyl}methyl)phenoxy]-2-methyl-2-pentanammonium Chloride (84)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "HCl salt of free amine from 4M HCl/dioxane deprotection of 83; used in N-alkylation with 23d to give compound 66 (Scheme 7)."
    },
    {
      "id": "C161",
      "name": "(S)-1-(2-{4-[p-({2-Ethyl-5-[(1S,2S,3S,4R,5S)-2,3,4-trihydroxy-1-methyl-6,8-dioxabicyclo[3.2.1]oct-5-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile (compound 66)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "97.1% by LC-MS",
      "ms_observed": "[M+H]+ 658.3",
      "ms_calculated_exact_mass": null,
      "description": "Triple inhibitor incorporating dioxabicyclo[3.2.1]octane ring (ertugliflozin-like) with C1-deoxy modification, Et core, C4 gem-dimethyl linker, and 4,4-difluoro-2-cyanopyrrolidine motif (Scheme 7)."
    },
    {
      "id": "C162",
      "name": "isopropyl-β-D-thiogalactopyranoside (85)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Commercial thioglycoside starting material for Scheme 8 synthesis of 4-fluoro and 4,4-difluoro C-glucoside building blocks 18e and 18f."
    },
    {
      "id": "C163",
      "name": "(4aR,6S,7R,8R,8aR)-6-(Isopropylthio)-2-phenyl-1,3,5-trioxahexahydro-7H-naphthalene-7,8-diol (86)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Benzylidene-protected thiogalactopyranoside intermediate from 85 and dimethoxybenzaldehyde (Scheme 8)."
    },
    {
      "id": "C164",
      "name": "(4aR,6S,7R,8S,8aS)-7,8-Bis(benzyloxy)-6-(isopropylthio)-2-Phenyl-1,3,5-trioxahexahydro-2H-naphthalene (87)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Dibenzylated benzylidene intermediate from NaH/BnBr protection of 86 (Scheme 8)."
    },
    {
      "id": "C165",
      "name": "(4aR,7R,8S,8aS)-7,8-Bis(benzyloxy)-2-Phenyl-1,3,5-trioxahexahydro-6H-naphthalen-6-one (88)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Lactone intermediate from NBS-mediated hydrolysis of isopropylthio group and Ac2O/DMSO oxidation of 87 (Scheme 8)."
    },
    {
      "id": "C166",
      "name": "4-bromo-2-ethoxyphenyl boronate/aryl bromide 89",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Aryl bromide reagent used in lithium-halogen exchange and addition to lactone 88 (Scheme 8); provides the diarylmethylene core."
    },
    {
      "id": "C167",
      "name": "(4aR,7R,8S,8aS)-7,8-Bis(benzyloxy)-6-{4-chloro-3-[(p-ethoxyphenyl)methyl]phenyl}-2-Phenyl-1,3,5-trioxahexahydro-6H-naphthalen-6-ol (90)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Lithiation/addition product of 89 to lactone 88; anomeric alcohol intermediate (Scheme 8)."
    },
    {
      "id": "C168",
      "name": "(2R,3S,4S,5S,6S)-4,5-Bis(benzyloxy)-6-{4-chloro-3-[(p-ethoxyphenyl)methyl]phenyl}-2-(hydroxymethyl)tetrahydro-2H-pyran-3-ol (91)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Et3SiH/BF3·OEt2 reduction of anomeric OH in 90 with concomitant benzylidene removal; key C-glucoside intermediate (Scheme 8)."
    },
    {
      "id": "C169",
      "name": "(2R,3S,4S,5S,6S)-4,5-Bis(benzyloxy)-6-{4-chloro-3-[(p-ethoxyphenyl)methyl]phenyl}-2-methyltetrahydro-2H-pyran-3-ol (92)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "6-Deoxy C-glucoside from selective tosylation/LiAlH4 reduction of 91; branching point for 18e and 18f synthesis (Scheme 8)."
    },
    {
      "id": "C170",
      "name": "(2S,3S,4R,5R,6R)-4-Acetoxy-2-{4-chloro-3-[(p-ethoxyphenyl)methyl]phenyl}-5-fluoro-6-methyltetrahydro-2H-pyran-3-yl Acetate (18e)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "4-Fluoro, 6-deoxy C-glucoside building block; prepared from 92 via triflation, TBAF fluorination, Bn removal (EtSH/BF3·OEt2), and acetylation (Scheme 8); dealkylated to 19e."
    },
    {
      "id": "C171",
      "name": "(2R,4R,5S,6S)-4,5-Bis(benzyloxy)-6-{4-chloro-3-[(p-ethoxyphenyl)methyl]phenyl}-2-methyltetrahydro-2H-pyran-3-one (93)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "IBX oxidation product of 92 at C4; ketone intermediate for BAST fluorination to give 4,4-difluoro derivative (Scheme 8)."
    },
    {
      "id": "C172",
      "name": "(2S,3S,4R,6R)-4-Acetoxy-2-{4-chloro-3-[(p-ethoxyphenyl)methyl]phenyl}-5,5-difluoro-6-methyltetrahydro-2H-pyran-3-yl Acetate (18f)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "4,4-Difluoro, 6-deoxy C-glucoside building block; prepared from 93 via BAST difluorination, Bn removal, and acetylation (Scheme 8); dealkylated to 19f."
    },
    {
      "id": "C173",
      "name": "bis(2-methoxyethyl)aminosulfur trifluoride (BAST)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fluorinating agent for geminal difluorination of ketone 93 (Scheme 8)."
    },
    {
      "id": "C174",
      "name": "TBAF (tetrabutylammonium fluoride)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "reagent",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Fluoride source for nucleophilic fluorination with inversion at C4 of triflate intermediate from 92 (Scheme 8); also used for TBDPS deprotection in Scheme 11."
    },
    {
      "id": "C175",
      "name": "5-bromo-2-methylbenzoic acid (103)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Commercial starting material for synthesis of core methyl (R1=Me) dapagliflozin analogue 18g via acid chloride/Friedel-Crafts/reduction sequence (Scheme 9)."
    },
    {
      "id": "C176",
      "name": "4-Bromo-2-toluoyl Chloride (104)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Acid chloride from 103 with oxalyl chloride/DMF; used in Friedel-Crafts acylation (Scheme 9)."
    },
    {
      "id": "C177",
      "name": "phenetole (ethoxybenzene)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Aromatic coupling partner in AlCl3-mediated Friedel-Crafts acylation with acid chloride 104 (Scheme 9)."
    },
    {
      "id": "C178",
      "name": "(5-Bromo-2-tolyl)(p-ethoxyphenyl)methanone (105)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Friedel-Crafts ketone product of 104 with phenetole; reduced to diphenylmethylene 106 (Scheme 9)."
    },
    {
      "id": "C179",
      "name": "4-Bromo-2-[(p-ethoxyphenyl)methyl]toluene (106)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Et3SiH/BF3·OEt2 reduction product of ketone 105; key diphenylmethylene intermediate for lithiation/glucosylation (Scheme 9)."
    },
    {
      "id": "C180",
      "name": "silyl-protected gluconolactone 107",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "TMS-protected D-gluconolactone electrophile; reacted with lithiated 106 then MsOH/MeOH to give methyl glycoside 108 (Scheme 9)."
    },
    {
      "id": "C181",
      "name": "(3R,4S,5S,6R)-2-{3-[(p-Ethoxyphenyl)methyl]-4-tolyl}-6-(hydroxymethyl)-2-methoxytetrahydro-4H-pyran-3,4,5-triol (108)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Methyl glycoside intermediate from n-BuLi lithiation of 106, reaction with 107, and MsOH/MeOH treatment (Scheme 9)."
    },
    {
      "id": "C182",
      "name": "(2R,3S,4R,5R,6S)-6-{3-[(p-Ethoxyphenyl)methyl]-4-tolyl}-2-(hydroxymethyl)tetrahydro-4H-pyran-3,4,5-triol (109)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Et3SiH/BF3·OEt2 reduction of anomeric methoxy group of 108; dapagliflozin methyl analogue (Scheme 9)."
    },
    {
      "id": "C183",
      "name": "(2R,3S,4R,5R,6S)-6-{3-[(p-Ethoxyphenyl)methyl]-4-tolyl}-2-[(tosyloxy)methyl]tetrahydro-4H-pyran-3,4,5-triol (110)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Primary alcohol tosylate of 109; selective 6-O-tosylation for C6-deoxygenation (Scheme 9)."
    },
    {
      "id": "C184",
      "name": "(2R,3S,4S,5R,6S)-6-{3-[(p-Ethoxyphenyl)methyl]-4-tolyl}-2-methyltetrahydro-4H-pyran-3,4,5-triol (111)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "LiAlH4 reduction product of tosylate 110; 6-deoxy dapagliflozin methyl analogue (Scheme 9)."
    },
    {
      "id": "C185",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{3-[(p-ethoxyphenyl)methyl]-4-tolyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate (18g)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Peracetylated 6-deoxy C-glucoside with methyl core group; dealkylated with BBr3 to give 19g (Scheme 9)."
    },
    {
      "id": "C186",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{3-[(p-ethoxyphenyl)methyl]-4-isopropenylphenyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate (112)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Suzuki-Molander coupling product of 18b with potassium isopropenyltrifluoroborate; isopropenyl intermediate en route to isopropyl building block 18h (Scheme 10)."
    },
    {
      "id": "C187",
      "name": "potassium isopropenyltrifluoroborate",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Potassium organotrifluoroborate used in Suzuki-Molander coupling with 18b (Scheme 10)."
    },
    {
      "id": "C188",
      "name": "(2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{3-[(p-ethoxyphenyl)methyl]-4-cumenyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate (18h)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "85.5% by LC-MS",
      "ms_observed": "[M+Na]+ 549.25",
      "ms_calculated_exact_mass": null,
      "description": "Isopropyl core C-glucoside from Pd/C hydrogenation of 112; dealkylated to 19h (Scheme 10)."
    },
    {
      "id": "C189",
      "name": "(S)-3-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-1,3-thiazolidine-4-carbonitrile (compound 46)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "100.0% by HPLC; 100.0% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 634.2, [M(37Cl)+H]+ 636.2",
      "ms_calculated_exact_mass": null,
      "description": "Triple inhibitor with thiazolidine-carbonitrile (teneligliptin-17-inspired) DPP4 motif and C4 gem-dimethyl linker."
    },
    {
      "id": "C190",
      "name": "(2S,4S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4-fluoro-2-pyrrolidinecarbonitrile (compound 47)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "100.0% by HPLC; 99.0% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 634.2, [M(37Cl)+H]+ 636.2",
      "ms_calculated_exact_mass": null,
      "description": "4-Fluorinated DPP4 pharmacophore analogue of compound 27; C4 gem-dimethyl linker."
    },
    {
      "id": "C191",
      "name": "(1S,3S,5S)-2-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-2-azabicyclo[3.1.0]hexane-3-carbonitrile (compound 48)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "100.0% by HPLC; 99.6% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 628.2, [M(37Cl)+H]+ 630.2",
      "ms_calculated_exact_mass": null,
      "description": "Bicyclic azabicyclo[3.1.0]hexane-carbonitrile (saxagliptin-12-inspired) DPP4 motif analogue of compound 27; C4 gem-dimethyl linker."
    },
    {
      "id": "C192",
      "name": "(2S,4S)-1-{2-[(1S,3R)-3-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclopentylamino]acetyl}-4-fluoro-2-pyrrolidinecarbonitrile (compound 49)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "99.7% by HPLC; 100.0% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 618.2, [M(37Cl)+H]+ 620.2",
      "ms_calculated_exact_mass": null,
      "description": "4-Fluoro DPP4 motif with trans-1,3-cyclopentyl linker; analogue of compound 32."
    },
    {
      "id": "C193",
      "name": "(S)-1-{2-[(1S,3R)-3-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclopentylamino]acetyl}-4,4-difluoro-2-pyrrolidinecarbonitrile (compound 50)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "95.4% by HPLC; 97.1% by LC-MS",
      "ms_observed": "[M(35Cl)-H]- 634.0, [M(37Cl)-H]- 636.1",
      "ms_calculated_exact_mass": null,
      "description": "4,4-Difluoro DPP4 motif with trans-1,3-cyclopentyl linker; most potent SGLT2 inhibitor in linker/DPP4 variation screen."
    },
    {
      "id": "C194",
      "name": "(S)-3-(2-{4-[p-({2-Chloro-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-1,3-thiazolidine-4-carbonitrile (compound 60)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "100.0% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 618.3, [M(37Cl)+H]+ 620.3",
      "ms_calculated_exact_mass": null,
      "description": "6-Deoxy, thiazolidine-carbonitrile DPP4 motif triple inhibitor; first 6-deoxy screening compound."
    },
    {
      "id": "C195",
      "name": "(S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile (compound 61)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "98.1% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 636.3, [M(37Cl)+H]+ 638.3",
      "ms_calculated_exact_mass": null,
      "description": "Key platform compound; 6-deoxy, 4,4-difluoro-2-cyanopyrrolidine DPP4 motif; priority lead for further optimization."
    },
    {
      "id": "C196",
      "name": "(1S,3S,5S)-2-(2-{4-[p-({2-Chloro-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-2-azabicyclo[3.1.0]hexane-3-carbonitrile (compound 62)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "100.0% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 612.3, [M(37Cl)+H]+ 614.3",
      "ms_calculated_exact_mass": null,
      "description": "6-Deoxy, bicyclic saxagliptin-inspired DPP4 motif triple inhibitor; fused cyclopropyl motif ruled out due to DPP4 activity loss."
    },
    {
      "id": "C197",
      "name": "(2S,4S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4-fluoro-2-pyrrolidinecarbonitrile (compound 63)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "97.2% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 618.3, [M(37Cl)+H]+ 620.3",
      "ms_calculated_exact_mass": null,
      "description": "6-Deoxy, 4-fluoro-2-cyanopyrrolidine DPP4 motif triple inhibitor; monofluorinated analogue."
    },
    {
      "id": "C198",
      "name": "(2S,4S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-5-fluoro-3,4-dihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4-fluoro-2-pyrrolidinecarbonitrile (compound 69)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "99.2% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 620.3, [M(37Cl)+H]+ 622.3",
      "ms_calculated_exact_mass": null,
      "description": "4-Fluoro C-glucoside analogue (monofluorinated at C4 of sugar); not pursued further."
    },
    {
      "id": "C199",
      "name": "(2S,4S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,6R)-5,5-difluoro-3,4-dihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4-fluoro-2-pyrrolidinecarbonitrile (compound 70)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "99.7% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 638.3, [M(37Cl)+H]+ 640.3",
      "ms_calculated_exact_mass": null,
      "description": "4,4-Difluoro C-glucoside analogue; not pursued further due to reduced SGLT2 potency."
    },
    {
      "id": "C200",
      "name": "1-{3-[p-({2-Ethyl-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]propyl}cyclopropanammonium Chloride (25a)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "92.1% by LC-MS",
      "ms_observed": "[M+H]+ 456.2",
      "ms_calculated_exact_mass": null,
      "description": "HCl salt of fully deprotected amine (Route 2) from 21q by HCl/MeOH deprotection; used in N-alkylation with 23d to give compound 94."
    },
    {
      "id": "C201",
      "name": "1-{3-[p-({2-Ethyl-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]propyl}cyclopentanammonium Chloride (25b)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "77.6% by LC-MS",
      "ms_observed": "[M+H]+ 484.3",
      "ms_calculated_exact_mass": null,
      "description": "HCl salt of fully deprotected amine (Route 2) from 21r; used in N-alkylation with 23d to give compound 95."
    },
    {
      "id": "C202",
      "name": "5-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(methylthio)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-2-methyl-2-pentanammonium Chloride (25c)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "93.3% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 496.3, [M(37Cl)+H]+ 498.2",
      "ms_calculated_exact_mass": null,
      "description": "HCl salt of sotagliflozin-derived free amine (Route 2) from TFA deprotection of 21n followed by HCl/MeOH; used in N-alkylation to give compounds 67–68."
    },
    {
      "id": "C203",
      "name": "2-Methyl-5-[p-({5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]-2-tolyl}methyl)phenoxy]-2-pentanammonium Chloride (25d)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "90.0% by LC-MS",
      "ms_observed": "[M+H]+ 444.4",
      "ms_calculated_exact_mass": null,
      "description": "HCl salt of fully deprotected methyl-core amine (Route 2) from 21u; used in N-alkylation with 23d to give compound 99."
    },
    {
      "id": "C204",
      "name": "2-Methyl-5-[p-({5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]-2-cumenyl}methyl)phenoxy]-2-pentanammonium Chloride (25e)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "HCl salt of fully deprotected isopropyl-core amine (Route 2) from 21v; used in N-alkylation with 23d to give compound 100."
    },
    {
      "id": "C205",
      "name": "5-[p-({2-Ethyl-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-2-methyl-2-pentanammonium Chloride (25f)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "89.7% by LC-MS",
      "ms_observed": "[M+Na]+ 480.4, [M+H]+ 458.4",
      "ms_calculated_exact_mass": null,
      "description": "HCl salt of fully deprotected ethyl-core amine (Route 2) from 21m; used in N-alkylation to give compounds 64 (via 22m), 101, 124, 125."
    },
    {
      "id": "C206",
      "name": "(1S,3S)-3-[p-({2-Ethyl-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclopentanammonium Chloride (25g)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "HCl salt of fully deprotected ethyl-core, cyclopentyl-linker amine (Route 2) from 21w; used in N-alkylation to give compounds 101, 126, 127."
    },
    {
      "id": "C207",
      "name": "(2S,4S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(methylthio)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4-fluoro-2-pyrrolidinecarbonitrile (compound 67)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "95.4% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 650.2, [M(37Cl)+H]+ 652.2",
      "ms_calculated_exact_mass": null,
      "description": "Sotagliflozin-6-inspired analogue (5-SMe sugar modification) with 4-fluoro-2-cyanopyrrolidine DPP4 motif."
    },
    {
      "id": "C208",
      "name": "5-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(methylthio)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-2-{2-[(S)-2-cyano-4,4-difluoro-1-pyrrolidinyl]-2-oxoethylammonio}-2-methylpentane Chloride (compound 68)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "99.2% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 668.3, [M(37Cl)+H]+ 670.2",
      "ms_calculated_exact_mass": null,
      "description": "Sotagliflozin-6-inspired analogue with 4,4-difluoro-2-cyanopyrrolidine DPP4 motif; higher SGLT2 selectivity."
    },
    {
      "id": "C209",
      "name": "(S)-1-[2-(1-{3-[p-({2-Ethyl-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]propyl}cyclopropylamino)acetyl]-4,4-difluoro-2-pyrrolidinecarbonitrile (compound 94)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "95.9% by LC-MS",
      "ms_observed": "[M+H]+ 628.4",
      "ms_calculated_exact_mass": null,
      "description": "Spiro-cyclopropyl gem-dimethyl linker replacement analogue with Et core and 4,4-difluoro DPP4 motif; sacrificed DPP4 activity."
    },
    {
      "id": "C210",
      "name": "(S)-1-[2-(1-{3-[p-({2-Ethyl-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]propyl}cyclopentylamino)acetyl]-4,4-difluoro-2-pyrrolidinecarbonitrile (compound 95)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "98.1% by LC-MS",
      "ms_observed": "[M+H]+ 656.4",
      "ms_calculated_exact_mass": null,
      "description": "Spiro-cyclopentyl gem-dimethyl linker replacement analogue with Et core; potent SGLT1/2 dual inhibitor but poor in vitro metabolism."
    },
    {
      "id": "C211",
      "name": "(S)-1-[2-({4-[p-({2-Chloro-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutyl}-N-methylamino)acetyl]-4,4-difluoro-2-pyrrolidinecarbonitrile (compound 96)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "97.9% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 650.2, [M(37Cl)+H]+ 652.3",
      "ms_calculated_exact_mass": null,
      "description": "N-Methyl analogue of compound 61; prepared by direct methylation of 61 with MeI/K2CO3; essentially inactive against DPP4."
    },
    {
      "id": "C212",
      "name": "(2S,4S)-1-{2-[(1S,3S)-3-[p-({2-Chloro-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclopentylamino]acetyl}-4-fluoro-2-pyrrolidinecarbonitrile (compound 97)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "99.5% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 602.3, [M(37Cl)+H]+ 604.3",
      "ms_calculated_exact_mass": null,
      "description": "6-Deoxy, trans-1,3-cyclopentyl linker, 4-fluoro-2-cyanopyrrolidine DPP4 motif (Cl core); weaker SGLT1 activity than 61."
    },
    {
      "id": "C213",
      "name": "(2S,4S)-1-{2-[(1R,4R)-4-[p-({2-Chloro-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclohexylamino]acetyl}-4-fluoro-2-pyrrolidinecarbonitrile (compound 98)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "100.0% by LC-MS",
      "ms_observed": "[M(35Cl)+H]+ 616.3, [M(37Cl)+H]+ 618.3",
      "ms_calculated_exact_mass": null,
      "description": "6-Deoxy, cis-1,4-cyclohexyl linker, 4-fluoro-2-cyanopyrrolidine DPP4 motif (Cl core); high SGLT2 selectivity."
    },
    {
      "id": "C214",
      "name": "(S)-1-(2-{1,1-Dimethyl-4-[p-({5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]-2-tolyl}methyl)phenoxy]butylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile (compound 99)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "96.4% by LC-MS",
      "ms_observed": "[M+H]+ 616.4",
      "ms_calculated_exact_mass": null,
      "description": "Lead compound; R1=Me (canagliflozin-1-inspired), 6-deoxy, C4 gem-dimethyl linker, 4,4-difluoro-2-cyanopyrrolidine DPP4 motif."
    },
    {
      "id": "C215",
      "name": "(S)-1-(2-{1,1-Dimethyl-4-[p-({5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]-2-cumenyl}methyl)phenoxy]butylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile (compound 100)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "99.2% by LC-MS",
      "ms_observed": "[M+H]+ 644.4",
      "ms_calculated_exact_mass": null,
      "description": "R1=iPr (mizagliflozin-10-inspired), 6-deoxy, C4 gem-dimethyl linker, 4,4-difluoro DPP4 motif; near-equal SGLT1/2 potency."
    },
    {
      "id": "C216",
      "name": "(S)-1-(2-{4-[p-({2-Ethyl-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile (compound 101)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "96.0% by LC-MS",
      "ms_observed": "[M+H]+ 630.4",
      "ms_calculated_exact_mass": null,
      "description": "Lead compound; R1=Et (licogliflozin-7-inspired), 6-deoxy, C4 gem-dimethyl linker, 4,4-difluoro-2-cyanopyrrolidine DPP4 motif; deacetylated form of 64."
    },
    {
      "id": "C217",
      "name": "5-Indanylamine (113)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Commercial 5-aminoindane; starting material for synthesis of compound 102 bearing HM41322-8-inspired indane core (Scheme 11)."
    },
    {
      "id": "C218",
      "name": "6-Bromo-5-indanylamine (114)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M(79Br)+H]+ 212.1, [M(81Br)+H]+ 214.2",
      "ms_calculated_exact_mass": null,
      "description": "NBS-mediated selective bromination of 5-indanylamine 113 at C6 (Scheme 11)."
    },
    {
      "id": "C219",
      "name": "6-Bromo-4-iodo-5-indanylamine (115)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "95.7% by LC-MS",
      "ms_observed": "[M(79Br)+H]+ 337.9, [M(81Br)+H]+ 339.9",
      "ms_calculated_exact_mass": null,
      "description": "NIS/AcOH iodination of 114 at C4 to give diiodinated precursor for deamination (Scheme 11)."
    },
    {
      "id": "C220",
      "name": "6-Bromo-4-iodoindane (116)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Deamination product of 115 via NaNO2/H2SO4/EtOH reductive Sandmeyer; lithiation substrate for diphenylmethanol synthesis (Scheme 11)."
    },
    {
      "id": "C221",
      "name": "p-TBDPS-oxy-benzaldehyde (117)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "TBDPS-protected 4-hydroxybenzaldehyde; aldehyde electrophile for lithiation/addition from 116 (Scheme 11)."
    },
    {
      "id": "C222",
      "name": "(6-Bromo-4-indanyl){p-[tert-butylbis(phenyl)siloxy]phenyl}methanol (118)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": "[M(79Br)-OH]+ 539.1, [M(81Br)-OH]+ 339.9",
      "ms_calculated_exact_mass": null,
      "description": "n-BuLi lithiation of 116 and addition to aldehyde 117; diphenylmethanol intermediate (Scheme 11)."
    },
    {
      "id": "C223",
      "name": "{p-[(6-Bromo-4-indanyl)methyl]phenoxy}-tert-butylbis(phenyl)silane (119)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Et3SiH/BF3·OEt2 reduction of alcohol 118 to diphenylmethylene; brominated indane core intermediate (Scheme 11)."
    },
    {
      "id": "C224",
      "name": "protected 6-deoxygluconolactone substrate 120",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "starting_material",
      "is_newly_synthesized": false,
      "source": "commercial",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Tri-O-benzyl-6-deoxy-D-gluconolactone electrophile; used in lithiation/addition with lithiated 119 (Scheme 11)."
    },
    {
      "id": "C225",
      "name": "tert-Butylbis(phenyl)[p-({6-[(2S,3S,4S,5R,6R)-3,4,5-Tris(benzyloxy)-6-methyltetrahydro-2H-pyran-2-yl]-4-indanyl}methyl)phenoxy]silane (121)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "Glycosylation product of lithiated 119 with protected gluconolactone 120 followed by Et3SiH/BF3·OEt2 anomeric reduction; TBDPS-protected indane C-glucoside (Scheme 11)."
    },
    {
      "id": "C226",
      "name": "tert-Butyl {1,1-Dimethyl-4-[p-({6-[(2S,3S,4S,5R,6R)-3,4,5-tris(benzyloxy)-6-methyltetrahydro-2H-pyran-2-yl]-4-indanyl}methyl)phenoxy]butyl}carbamate (122)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": null,
      "ms_observed": null,
      "ms_calculated_exact_mass": null,
      "description": "TBAF desilylation of 121 followed by Mitsunobu coupling with 20b; Boc-protected, tri-Bn-protected intermediate (Scheme 11)."
    },
    {
      "id": "C227",
      "name": "1,1-Dimethyl-4-[p-({6-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]-4-indanyl}methyl)phenoxy]butyl 2-Methyl-2-propanecarbamate (123)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "intermediate",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "83.4% by LC-MS",
      "ms_observed": "[M+Na]+ 592.4",
      "ms_calculated_exact_mass": null,
      "description": "High-pressure Pd(OH)2/Pd/C hydrogenation product of 122 to remove Bn groups; Boc-protected indane-glucoside intermediate en route to compound 102 (Scheme 11)."
    },
    {
      "id": "C228",
      "name": "(S)-1-(2-{1,1-Dimethyl-4-[p-({6-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]-4-indanyl}methyl)phenoxy]butylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile (compound 102)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "99.8% by LC-MS",
      "ms_observed": "[M-H]- 640.4",
      "ms_calculated_exact_mass": null,
      "description": "Triple inhibitor with fused indane core (HM41322-8-inspired), 6-deoxy C-glucoside, C4 gem-dimethyl linker, 4,4-difluoro-2-cyanopyrrolidine DPP4 motif (Scheme 11)."
    },
    {
      "id": "C229",
      "name": "(S)-1-(2-{4-[p-({2-Ethyl-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-2-pyrrolidinecarbonitrile (compound 124)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "97.7% by LC-MS",
      "ms_observed": "[M+H]+ 594.4",
      "ms_calculated_exact_mass": null,
      "description": "4,4-Didesfluoro analogue of compound 101; unsubstituted 2-cyanopyrrolidine DPP4 motif; 2-fold lower DPP4 potency than 101."
    },
    {
      "id": "C230",
      "name": "(2S,4S)-1-(2-{4-[p-({2-Ethyl-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4-fluoro-2-pyrrolidinecarbonitrile (compound 125)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "99.9% by LC-MS",
      "ms_observed": "[M+H]+ 612.4",
      "ms_calculated_exact_mass": null,
      "description": "4-Monofluoro analogue of compound 101; same activity profile, modestly improved hepatocyte stability."
    },
    {
      "id": "C231",
      "name": "(2S,4S)-1-{2-[(1S,3S)-3-[p-({2-Ethyl-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclopentylamino]acetyl}-4-fluoro-2-pyrrolidinecarbonitrile (compound 126)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "96.8% by LC-MS",
      "ms_observed": "[M+H]+ 612.4",
      "ms_calculated_exact_mass": null,
      "description": "Et core, trans-1,3-cyclopentyl linker, 4-fluoro DPP4 motif; dramatically improved SGLT1 potency vs Cl analogue 97 (SGLT2/1 ratio 4.6)."
    },
    {
      "id": "C232",
      "name": "(S)-1-{2-[(1S,3S)-3-[p-({2-Ethyl-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]cyclopentylamino]acetyl}-4,4-difluoro-2-pyrrolidinecarbonitrile (compound 127)",
      "iupac_name": null,
      "molecular_formula": null,
      "role": "final_product",
      "is_newly_synthesized": true,
      "source": "in-house",
      "purity": "95.8% by LC-MS",
      "ms_observed": "[M+H]+ 614.3",
      "ms_calculated_exact_mass": null,
      "description": "Et core, trans-1,3-cyclopentyl linker, 4,4-difluoro DPP4 motif; chemically labile in phosphate buffer and rat plasma."
    }
  ],
  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "General Dealkylation of Aryl Ethyl Ethers (18a→19a)",
      "target_compound_id": "C03",
      "target_compound_name": "19a: [(2R,3R,4R,5S,6S)-3,4,5-Triacetoxy-6-{4-chloro-3-[(p-hydroxyphenyl)methyl]phenyl}tetrahydro-2H-pyran-2-yl]methyl Acetate",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "O-dealkylation (Lewis acid mediated aryl ether cleavage)",
          "reactants": [
            {
              "compound_id": "C01",
              "name": "tetraacetyl dapagliflozin (18a)",
              "amount": "9.90 g (17.2 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "BBr3 (10 equiv) in dry CH2Cl2",
              "amount": "10 equiv",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2 (dry)",
              "volume": "235 mL"
            }
          ],
          "conditions": {
            "temperature": "-70 °C, then warmed to -30 °C",
            "time": "1–6 h total",
            "atmosphere": "N2",
            "ph": null,
            "other": "Reaction poured onto ice, neutralized with sat. NaHCO3 (400 mL), organic layers washed with brine, dried over Na2SO4."
          },
          "product": {
            "compound_id": "C03",
            "name": "19a",
            "yield": "8.80 g (93%)",
            "purity": "97.0% by HPLC; 90.6% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "trituration with EtOAc/petroleum ether (1:5, 90 mL) at 25 °C for 0.5 h",
          "notes": "General procedure applies to 18a–h; individual volumes and purification methods differ per substrate."
        }
      ]
    },
    {
      "pathway_id": "P2",
      "pathway_name": "Synthesis of 6-Deoxy C-Glucoside Building Block 18b (Scheme 5)",
      "target_compound_id": "C141",
      "target_compound_name": "18b: (2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{4-chloro-3-[(p-ethoxyphenyl)methyl]phenyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Appel iodination (primary alcohol to iodide)",
          "reactants": [
            {
              "compound_id": "C139",
              "name": "Compound 71 (dapagliflozin synthesis intermediate)",
              "amount": "24.4 g (33.4 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C34",
              "name": "PPh3",
              "amount": "11.6 g (44.4 mmol, 1.33 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "imidazole",
              "amount": "2.85 g (41.9 mmol, 1.26 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "I2",
              "amount": "10.5 g (41.5 mmol, 1.24 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "195 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C then 50 °C",
            "time": "5 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Worked up with water, DCM, 0.5 M HCl, brine; purified by column chromatography."
          },
          "product": {
            "compound_id": "C138",
            "name": "72 (iodomethyl intermediate)",
            "yield": "17.8 g (58%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 0→5% MeOH/CH2Cl2",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Acetylation (sugar hydroxyl protection)",
          "reactants": [
            {
              "compound_id": "C138",
              "name": "72",
              "amount": "17.8 g (32.4 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Ac2O",
              "amount": "33.1 g (30.4 mL, 324 mmol, 10 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "DMAP",
              "amount": "792 mg (6.49 mmol, 0.2 equiv)",
              "role": "catalyst"
            }
          ],
          "solvents": [
            {
              "name": "pyridine",
              "volume": "124 mL"
            }
          ],
          "conditions": {
            "temperature": "0–10 °C then 25 °C",
            "time": "15 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Quenched with water, extracted with EtOAc; purified by column chromatography."
          },
          "product": {
            "compound_id": "C140",
            "name": "73 (iodoacetatetetremer)",
            "yield": "5.50 g (25%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 0→11% EtOAc/petroleum ether",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Hydrogenolytic deiodination",
          "reactants": [
            {
              "compound_id": "C140",
              "name": "73",
              "amount": "5.00 g (7.41 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "wet 10% Pd/C",
              "amount": "2.00 g",
              "role": "catalyst"
            },
            {
              "compound_id": null,
              "name": "Et3N",
              "amount": "7.50 g (10.3 mL, 74.1 mmol, 10 equiv)",
              "role": "base"
            },
            {
              "compound_id": null,
              "name": "H2 (1 atm)",
              "amount": null,
              "role": "reductant"
            }
          ],
          "solvents": [
            {
              "name": "2:1 THF/MeOH",
              "volume": "45 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "24 h",
            "atmosphere": "H2 (1 atm)",
            "ph": null,
            "other": "Filtered, concentrated; partitioned between EtOAc and water; purified by column chromatography."
          },
          "product": {
            "compound_id": null,
            "name": "deiodinated intermediate (6-methoxy C-glucoside triacetate)",
            "yield": "3.70 g (96%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 0→50% EtOAc/petroleum ether",
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "Anomeric reduction (methoxy to H via Et3SiH/BF3·OEt2)",
          "reactants": [
            {
              "compound_id": null,
              "name": "deiodinated intermediate (6-methoxy triacetate)",
              "amount": "3.70 g (~6.74 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "water",
              "amount": "121 μL (6.74 mmol, 1.0 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Et3SiH",
              "amount": "2.51 g (3.44 mL, 21.6 mmol, 3.2 equiv)",
              "role": "reductant"
            },
            {
              "compound_id": null,
              "name": "BF3·Et2O",
              "amount": "2.30 g (2.00 mL, 16.2 mmol, 2.4 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "MeCN",
              "volume": "26 mL"
            }
          ],
          "conditions": {
            "temperature": "<15 °C then 25 °C",
            "time": "5 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with sat. NaHCO3; extracted with EtOAc; triturated with 1:7 EtOAc/petroleum ether."
          },
          "product": {
            "compound_id": "C141",
            "name": "18b",
            "yield": "2.90 g (83%)",
            "purity": "95.9% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "trituration with 1:7 EtOAc/petroleum ether (40 mL) at 25 °C for 16 h",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P3",
      "pathway_name": "Synthesis of 6-Deoxy, Ethyl-Core Building Block 18c (Scheme 5)",
      "target_compound_id": "C143",
      "target_compound_name": "18c: (2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{3-[(p-ethoxyphenyl)methyl]-4-ethylphenyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Suzuki-Miyaura cross-coupling (NHC-borane)",
          "reactants": [
            {
              "compound_id": "C141",
              "name": "18b",
              "amount": "12.0 g (23.1 mmol)"
            },
            {
              "compound_id": "C142",
              "name": "NHC-borane 74",
              "amount": "16.9 g (34.7 mmol, 1.5 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C144",
              "name": "Pd(OAc)2",
              "amount": "882 mg (3.93 mmol, 0.17 equiv)",
              "role": "catalyst"
            },
            {
              "compound_id": "C145",
              "name": "RuPhos",
              "amount": "3.45 g (7.40 mmol, 0.32 equiv)",
              "role": "catalyst"
            }
          ],
          "solvents": [
            {
              "name": "10:1 toluene/water",
              "volume": "154 mL"
            }
          ],
          "conditions": {
            "temperature": "80 °C",
            "time": "24 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Degassed and N2-purged three times; water added after reaction; extracted with EtOAc."
          },
          "product": {
            "compound_id": "C143",
            "name": "18c",
            "yield": "9.50 g (80%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 5→12.5% EtOAc/petroleum ether",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P4",
      "pathway_name": "Synthesis of Triacetyl Sotagliflozin (18d)",
      "target_compound_id": "C146",
      "target_compound_name": "18d: (2R,3S,4R,5S,6S)-4,5-Diacetoxy-6-{4-chloro-3-[(p-hydroxyphenyl)methyl]phenyl}-2-(methylthio)tetrahydro-2H-pyran-3-yl Acetate",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Acetylation of sotagliflozin",
          "reactants": [
            {
              "compound_id": "C148",
              "name": "sotagliflozin 6",
              "amount": "2.80 g (6.59 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Ac2O",
              "amount": "8.07 g (7.41 mL, 79.0 mmol, 12 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "pyridine",
              "amount": "6.25 g (6.38 mL, 79.0 mmol, 12 equiv)",
              "role": "base"
            },
            {
              "compound_id": null,
              "name": "DMAP",
              "amount": "64 mg (0.53 mmol, 0.08 equiv)",
              "role": "catalyst"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "56 mL"
            }
          ],
          "conditions": {
            "temperature": "20 °C",
            "time": "1 h",
            "atmosphere": null,
            "ph": null,
            "other": "Concentrated under reduced pressure; diluted with MTBE; washed with 1 M HCl, sat. NaHCO3, brine."
          },
          "product": {
            "compound_id": "C146",
            "name": "18d",
            "yield": "3.60 g (99%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none; used without further purification",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P5",
      "pathway_name": "Synthesis of 4-Fluoro, 6-Deoxy C-Glucoside Building Block 18e (Scheme 8)",
      "target_compound_id": "C170",
      "target_compound_name": "18e: (2S,3S,4R,5R,6R)-4-Acetoxy-2-{4-chloro-3-[(p-ethoxyphenyl)methyl]phenyl}-5-fluoro-6-methyltetrahydro-2H-pyran-3-yl Acetate",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Benzylidene protection of isopropyl thiogalactopyranoside",
          "reactants": [
            {
              "compound_id": "C162",
              "name": "isopropyl-β-D-thiogalactopyranoside (85)",
              "amount": "49.8 g (209 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "benzaldehyde dimethyl acetal",
              "amount": "51.1 g (50.6 mL, 335 mmol, 1.6 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "TsOH·H2O",
              "amount": "3.99 g (20.9 mmol, 0.1 equiv)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "300 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "2 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Quenched with Et3N; worked up with water/EtOAc; triturated with MTBE."
          },
          "product": {
            "compound_id": "C163",
            "name": "86 (benzylidene protected)",
            "yield": "54.0 g (79%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "trituration with MTBE (300 mL)",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Benzyl protection of remaining hydroxyls",
          "reactants": [
            {
              "compound_id": "C163",
              "name": "86",
              "amount": "54.0 g (165 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "NaH (60% dispersion in mineral oil)",
              "amount": "19.9 g (496 mmol, 3.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": null,
              "name": "BnBr",
              "amount": "84.9 g (59.0 mL, 496 mmol, 3.0 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "1080 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C then 25 °C",
            "time": "0.5 h (NaH) then 16 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with sat. NH4Cl at 0 °C; concentrated; partitioned between EtOAc and brine; triturated with diisopropyl ether."
          },
          "product": {
            "compound_id": "C164",
            "name": "87",
            "yield": "79.0 g (94%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "trituration with diisopropyl ether (1 L)",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "NBS-mediated hydrolysis of isopropylthio group to hemiacetal",
          "reactants": [
            {
              "compound_id": "C164",
              "name": "87",
              "amount": "26.3 g (51.9 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "NBS",
              "amount": "8.78 g (49.3 mmol, 0.95 equiv)",
              "role": "oxidant"
            }
          ],
          "solvents": [
            {
              "name": "9:1 acetone/water",
              "volume": "330 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "5 min",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with sat. NaHCO3; extracted with EtOAc; pooled from three batches."
          },
          "product": {
            "compound_id": null,
            "name": "hemiacetal intermediate",
            "yield": "45.0 g (64%; pooled)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 9→100% EtOAc/petroleum ether",
          "notes": "Three batches pooled."
        },
        {
          "step_number": 4,
          "reaction_type": "Ac2O/DMSO oxidation of hemiacetal to lactone",
          "reactants": [
            {
              "compound_id": null,
              "name": "hemiacetal intermediate",
              "amount": "40.0 g (89.2 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Ac2O",
              "amount": "64 mL",
              "role": "oxidant"
            }
          ],
          "solvents": [
            {
              "name": "DMSO",
              "volume": "128 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "16 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with water at 0–10 °C; extracted with EtOAc; purified by chromatography."
          },
          "product": {
            "compound_id": "C165",
            "name": "88 (lactone)",
            "yield": "32.0 g (80%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 9→33% EtOAc/petroleum ether",
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "Lithium-halogen exchange and addition to lactone",
          "reactants": [
            {
              "compound_id": "C165",
              "name": "88",
              "amount": "18.0 g (40.3 mmol)"
            },
            {
              "compound_id": "C166",
              "name": "aryl bromide 89",
              "amount": "19.7 g (60.5 mmol, 1.5 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "n-BuLi (2.5 M)",
              "amount": "24.2 mL (1.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "210 mL total"
            }
          ],
          "conditions": {
            "temperature": "-65 to -60 °C",
            "time": "2.5 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Quenched with sat. NH4Cl at 0 °C; extracted with EtOAc; pooled from two batches."
          },
          "product": {
            "compound_id": "C167",
            "name": "90 (anomeric alcohol)",
            "yield": "49.0 g (88%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 9→100% EtOAc/petroleum ether",
          "notes": null
        },
        {
          "step_number": 6,
          "reaction_type": "Anomeric reduction with Et3SiH/BF3·OEt2 (concomitant benzylidene removal)",
          "reactants": [
            {
              "compound_id": "C167",
              "name": "90",
              "amount": "25.2 g (36.3 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Et3SiH",
              "amount": "12.7 g (17.4 mL, 109 mmol, 3.0 equiv)",
              "role": "reductant"
            },
            {
              "compound_id": null,
              "name": "BF3·Et2O",
              "amount": "15.5 g (13.5 mL, 109 mmol, 3.0 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "151 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C",
            "time": "1 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Quenched with water; extracted with EtOAc; purified by chromatography."
          },
          "product": {
            "compound_id": "C168",
            "name": "91 (C-glucoside diol)",
            "yield": "13.0 g (61%)",
            "purity": null,
            "hpl_retention_time_min": null
          },
          "purification": "column chromatography on silica, 9→100% EtOAc/petroleum ether",
          "notes": null
        },
        {
          "step_number": 7,
          "reaction_type": "Selective tosylation of primary alcohol then LiAlH4 reduction (C6-deoxygenation)",
          "reactants": [
            {
              "compound_id": "C168",
              "name": "91",
              "amount": "13.0 g (22.1 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "p-toluenesulfonyl chloride",
              "amount": "7.57 g (39.7 mmol, 1.8 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "pyridine",
              "volume": "78 mL"
            }
          ],
          "conditions": {
            "temperature": "-20 °C then 30 °C",
            "time": "16 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Quenched with water at 0 °C; washed with sat. NaHCO3 and brine."
          },
          "product": {
            "compound_id": null,
            "name": "primary tosylate intermediate",
            "yield": "11.4 g (70%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 9→100% EtOAc/petroleum ether",
          "notes": null
        },
        {
          "step_number": 8,
          "reaction_type": "LiAlH4 reduction of tosylate",
          "reactants": [
            {
              "compound_id": null,
              "name": "primary tosylate intermediate",
              "amount": "17.2 g (23.1 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "LiAlH4",
              "amount": "3.51 g (92.6 mmol, 4.0 equiv)",
              "role": "reductant"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "134 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C then 65 °C",
            "time": "2.5 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched at 0 °C with water/NaOH; filtered over Na2SO4; purified by chromatography."
          },
          "product": {
            "compound_id": "C169",
            "name": "92 (6-deoxy C-glucoside with Bn protecting groups)",
            "yield": "10.2 g (77%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 4→100% EtOAc/petroleum ether",
          "notes": null
        },
        {
          "step_number": 9,
          "reaction_type": "Triflation of C4-OH then TBAF fluorination (inversion)",
          "reactants": [
            {
              "compound_id": "C169",
              "name": "92",
              "amount": "6.0 g (10.5 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Tf2O",
              "amount": "5.91 g (3.45 mL, 20.9 mmol, 2.0 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C174",
              "name": "TBAF (1 M in THF)",
              "amount": "104.6 mL (10 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2/pyridine then THF",
              "volume": "60 mL + 24 mL pyridine; then 44.3 mL THF"
            }
          ],
          "conditions": {
            "temperature": "-15 °C then 15 °C (triflation); 15 °C (fluorination)",
            "time": "1.25 h (triflation); 16 h (fluorination)",
            "atmosphere": "N2",
            "ph": null,
            "other": "Triflation product concentrated; fluorination quenched with water; Bn removal with EtSH/BF3·OEt2."
          },
          "product": {
            "compound_id": null,
            "name": "4-fluoro, 6-deoxy, Bn-protected intermediate",
            "yield": "3.50 g (58% over two steps from 92)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 1→3.33% EtOAc/petroleum ether",
          "notes": null
        },
        {
          "step_number": 10,
          "reaction_type": "Benzyl group removal (EtSH/BF3·OEt2) and acetylation",
          "reactants": [
            {
              "compound_id": null,
              "name": "4-fluoro, 6-deoxy, Bn-protected intermediate",
              "amount": "3.50 g (6.08 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "EtSH",
              "amount": "38.2 g (45.5 mL, 615 mmol, 101 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "BF3·Et2O",
              "amount": "26.2 g (22.8 mL, 184 mmol, 30.3 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Ac2O",
              "amount": "3.72 g (3.42 mL, 36.5 mmol, 6.0 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "DMAP",
              "amount": "74 mg (0.61 mmol, 0.1 equiv)",
              "role": "catalyst"
            }
          ],
          "solvents": [
            {
              "name": "neat EtSH/BF3·Et2O then pyridine",
              "volume": "19 mL pyridine for acetylation"
            }
          ],
          "conditions": {
            "temperature": "25 °C (Bn removal); 25 °C, 16 h (acetylation)",
            "time": "3 h (Bn removal); 16 h (acetylation)",
            "atmosphere": null,
            "ph": null,
            "other": "Poured into sat. NaHCO3 after Bn removal; purified by column chromatography."
          },
          "product": {
            "compound_id": "C170",
            "name": "18e",
            "yield": "1.90 g (65% over two steps; 38% over four steps from 92)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 1→3.33% EtOAc/petroleum ether",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P6",
      "pathway_name": "Synthesis of 4,4-Difluoro, 6-Deoxy C-Glucoside Building Block 18f (Scheme 8)",
      "target_compound_id": "C172",
      "target_compound_name": "18f: (2S,3S,4R,6R)-4-Acetoxy-2-{4-chloro-3-[(p-ethoxyphenyl)methyl]phenyl}-5,5-difluoro-6-methyltetrahydro-2H-pyran-3-yl Acetate",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "IBX oxidation of C4-OH to ketone",
          "reactants": [
            {
              "compound_id": "C169",
              "name": "92",
              "amount": "5.50 g (9.60 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "IBX",
              "amount": "3.22 g (11.5 mmol, 1.2 equiv)",
              "role": "oxidant"
            }
          ],
          "solvents": [
            {
              "name": "MeCN",
              "volume": "33 mL"
            }
          ],
          "conditions": {
            "temperature": "80 °C",
            "time": "2 h",
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to RT; filtered; filtrate concentrated."
          },
          "product": {
            "compound_id": "C171",
            "name": "93 (ketone)",
            "yield": "4.80 g (88%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "BAST gem-difluorination",
          "reactants": [
            {
              "compound_id": "C171",
              "name": "93",
              "amount": "4.80 g (8.40 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C173",
              "name": "BAST (bis(2-methoxyethyl)aminosulfur trifluoride)",
              "amount": "6.32 g (6.26 mL, 28.6 mmol, 3.4 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "30 mL"
            }
          ],
          "conditions": {
            "temperature": "15 °C",
            "time": "16 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with sat. NaHCO3; extracted with EtOAc."
          },
          "product": {
            "compound_id": null,
            "name": "4,4-difluoro, 6-deoxy, Bn-protected intermediate",
            "yield": "2.80 g (56%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 0→9% EtOAc/petroleum ether",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Benzyl group removal (EtSH/BF3·OEt2) and acetylation",
          "reactants": [
            {
              "compound_id": null,
              "name": "4,4-difluoro, 6-deoxy, Bn-protected intermediate",
              "amount": "2.80 g (4.72 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "EtSH",
              "amount": "30.6 g (36.4 mL, 492 mmol, 104 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "BF3·Et2O",
              "amount": "22.5 g (19.6 mL, 158 mmol, 33.6 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Ac2O",
              "amount": "2.89 g (2.65 mL, 28.3 mmol, 6.0 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "DMAP",
              "amount": "58 mg (0.047 mmol, 0.1 equiv)",
              "role": "catalyst"
            }
          ],
          "solvents": [
            {
              "name": "neat EtSH/BF3 then pyridine",
              "volume": "19 mL pyridine"
            }
          ],
          "conditions": {
            "temperature": "25 °C (Bn removal); 25 °C (acetylation)",
            "time": "3 h; 16 h",
            "atmosphere": null,
            "ph": null,
            "other": "Poured into sat. NaHCO3 after Bn removal; extracted with EtOAc."
          },
          "product": {
            "compound_id": "C172",
            "name": "18f",
            "yield": "1.70 g (72% over two steps; 41% over three steps from 93)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 1→9% EtOAc/petroleum ether",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P7",
      "pathway_name": "Synthesis of Core Methyl Building Block 18g/19g (Scheme 9)",
      "target_compound_id": "C09",
      "target_compound_name": "19g: (2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{3-[(p-hydroxyphenyl)methyl]-4-tolyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Acid chloride formation",
          "reactants": [
            {
              "compound_id": "C175",
              "name": "5-bromo-2-methylbenzoic acid (103)",
              "amount": "65.0 g (302 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "oxalyl chloride",
              "amount": "46.0 g (31.7 mL, 363 mmol, 1.2 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "DMF (cat.)",
              "amount": "1.10 g (1.16 mL, 15.1 mmol, 0.05 equiv)",
              "role": "catalyst"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2 (anhydrous)",
              "volume": "325 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C then 25 °C",
            "time": "3 h",
            "atmosphere": "Ar",
            "ph": null,
            "other": "Concentrated under reduced pressure."
          },
          "product": {
            "compound_id": "C176",
            "name": "104 (acid chloride)",
            "yield": "70.0 g (99%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Friedel-Crafts acylation",
          "reactants": [
            {
              "compound_id": "C176",
              "name": "104",
              "amount": "70.0 g (300 mmol)"
            },
            {
              "compound_id": "C177",
              "name": "phenetole",
              "amount": "40.3 g (41.7 mL, 330 mmol, 1.1 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "AlCl3",
              "amount": "48.0 g (360 mmol, 1.2 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "454 mL total"
            }
          ],
          "conditions": {
            "temperature": "0 → 25 °C",
            "time": "1 h",
            "atmosphere": null,
            "ph": null,
            "other": "Poured into water at 0 °C; organic layer separated; triturated with petroleum ether."
          },
          "product": {
            "compound_id": "C178",
            "name": "105 (ketone)",
            "yield": "83.5 g (87%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "trituration with petroleum ether",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Et3SiH/BF3·OEt2 reduction of ketone to diarylmethylene",
          "reactants": [
            {
              "compound_id": "C178",
              "name": "105",
              "amount": "63.0 g (197 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Et3SiH",
              "amount": "103 g (142 mL, 888 mmol, 4.5 equiv)",
              "role": "reductant"
            },
            {
              "compound_id": null,
              "name": "BF3·Et2O",
              "amount": "98.0 g (85.0 mL, 691 mmol, 3.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CHCl3/MeCN (2:1 approx.)",
              "volume": "435 mL total"
            }
          ],
          "conditions": {
            "temperature": "0–10 °C then 30 °C",
            "time": "1 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Quenched with sat. NaHCO3; extracted with CH2Cl2; purified by column chromatography."
          },
          "product": {
            "compound_id": "C179",
            "name": "106 (diarylmethylene)",
            "yield": "57.7 g (96%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, petroleum ether",
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "n-BuLi lithiation/glucosylation, then MsOH/MeOH O-methylation",
          "reactants": [
            {
              "compound_id": "C179",
              "name": "106",
              "amount": "66.0 g (216 mmol)"
            },
            {
              "compound_id": "C180",
              "name": "silyl-protected gluconolactone 107",
              "amount": "131 g (281 mmol, 1.3 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "n-BuLi (2.5 M)",
              "amount": "104 mL (1.2 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "MsOH",
              "amount": "47.8 g (35.5 mL, 497 mmol, 2.3 equiv)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "4:1 toluene/THF then MeOH",
              "volume": "660 mL toluene/THF; 330 mL MeOH"
            }
          ],
          "conditions": {
            "temperature": "-70 to -60 °C (lithiation); -70 °C → 25 °C then add MsOH; 25 °C, 16 h",
            "time": "2 h lithiation; 16 h reaction with MsOH",
            "atmosphere": null,
            "ph": null,
            "other": "Adjusted to pH 9 with i-Pr2NEt; concentrated; column chromatography."
          },
          "product": {
            "compound_id": "C181",
            "name": "108 (methyl glycoside)",
            "yield": "97.3 g (86%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 1.67→100% MeOH/CH2Cl2",
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "Anomeric methoxy reduction (Et3SiH/BF3·OEt2)",
          "reactants": [
            {
              "compound_id": "C181",
              "name": "108",
              "amount": "96.0 g (229 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Et3SiH",
              "amount": "120 g (165 mL, 1.03 mol, 4.5 equiv)",
              "role": "reductant"
            },
            {
              "compound_id": null,
              "name": "BF3·Et2O",
              "amount": "114 g (98.7 mL, 803 mmol, 3.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CHCl3/MeCN",
              "volume": "662 mL total"
            }
          ],
          "conditions": {
            "temperature": "0–10 °C then 30 °C",
            "time": "1 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Quenched with sat. NaHCO3; extracted with DCM."
          },
          "product": {
            "compound_id": "C182",
            "name": "109 (methyl dapagliflozin analogue)",
            "yield": "47.0 g (53%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly",
          "notes": null
        },
        {
          "step_number": 6,
          "reaction_type": "Selective 6-O-tosylation",
          "reactants": [
            {
              "compound_id": "C182",
              "name": "109",
              "amount": "32.5 g (83.7 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "p-toluenesulfonyl chloride",
              "amount": "15.9 g (83.7 mmol, 1.0 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "pyridine",
              "volume": "163 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C then 30 °C",
            "time": "16 h",
            "atmosphere": null,
            "ph": null,
            "other": "Diluted with water; extracted with EtOAc; washed with 1 M HCl."
          },
          "product": {
            "compound_id": "C183",
            "name": "110 (primary tosylate)",
            "yield": "13.0 g (29%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 5→100% EtOAc/petroleum ether",
          "notes": "Low yield due to low selectivity of tosylation step."
        },
        {
          "step_number": 7,
          "reaction_type": "LiAlH4 reduction of primary tosylate (C6-deoxygenation)",
          "reactants": [
            {
              "compound_id": "C183",
              "name": "110",
              "amount": "9.2 g (16.9 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "LiAlH4 (2.5 M in THF)",
              "amount": "17 mL (2.5 equiv)",
              "role": "reductant"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "84 mL"
            }
          ],
          "conditions": {
            "temperature": "20 °C then 65 °C",
            "time": "2.5 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Quenched with water/NaOH/water; Na2SO4 added; filtered."
          },
          "product": {
            "compound_id": "C184",
            "name": "111 (6-deoxy diol)",
            "yield": "7.15 g (96%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly",
          "notes": null
        },
        {
          "step_number": 8,
          "reaction_type": "Peracetylation",
          "reactants": [
            {
              "compound_id": "C184",
              "name": "111",
              "amount": "9.60 g (25.8 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Ac2O",
              "amount": "15.8 g (15.0 mL, 154 mmol, 6.0 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Et3N",
              "amount": "20.9 g (28.0 mL, 206 mmol, 8.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": null,
              "name": "DMAP",
              "amount": "315 mg (2.58 mmol, 0.10 equiv)",
              "role": "catalyst"
            }
          ],
          "solvents": [
            {
              "name": "MeCN",
              "volume": "58 mL"
            }
          ],
          "conditions": {
            "temperature": "35 °C",
            "time": "9 h",
            "atmosphere": null,
            "ph": null,
            "other": "Diluted with water at 5–10 °C; extracted with EtOAc."
          },
          "product": {
            "compound_id": "C185",
            "name": "18g",
            "yield": "12.1 g (94%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly in BBr3 dealkylation to give 19g",
          "notes": null
        },
        {
          "step_number": 9,
          "reaction_type": "O-dealkylation (aryl ethyl ether to phenol)",
          "reactants": [
            {
              "compound_id": "C185",
              "name": "18g",
              "amount": "1.70 g (3.32 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "BBr3 (10 equiv) in dry CH2Cl2",
              "amount": "10 equiv",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "20 mL"
            }
          ],
          "conditions": {
            "temperature": "-70 °C then -30 °C",
            "time": "4.5 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "General dealkylation procedure; poured onto ice; neutralized with sat. NaHCO3."
          },
          "product": {
            "compound_id": "C09",
            "name": "19g",
            "yield": "1.40 g (87%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 5→50% EtOAc/petroleum ether",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P8",
      "pathway_name": "Synthesis of Core Isopropyl Building Block 18h/19h (Scheme 10)",
      "target_compound_id": "C10",
      "target_compound_name": "19h: (2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-{3-[(p-hydroxyphenyl)methyl]-4-cumenyl}-2-methyltetrahydro-2H-pyran-3-yl Acetate",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Suzuki-Molander coupling (Ar-Cl + potassium isopropenyltrifluoroborate)",
          "reactants": [
            {
              "compound_id": "C141",
              "name": "18b",
              "amount": "1.80 g (3.47 mmol)"
            },
            {
              "compound_id": "C187",
              "name": "potassium isopropenyltrifluoroborate",
              "amount": "615 mg (4.16 mmol, 1.2 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C144",
              "name": "Pd(OAc)2",
              "amount": "389 mg (1.73 mmol, 0.5 equiv)",
              "role": "catalyst"
            },
            {
              "compound_id": "C145",
              "name": "RuPhos",
              "amount": "142 mg (0.35 mmol, 0.1 equiv)",
              "role": "catalyst"
            },
            {
              "compound_id": null,
              "name": "K2CO3",
              "amount": "1.44 g (10.4 mmol, 3.0 equiv)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "1,4-dioxane/water (6:1)",
              "volume": "14 mL"
            }
          ],
          "conditions": {
            "temperature": "90 °C",
            "time": "12 h",
            "atmosphere": null,
            "ph": null,
            "other": "Cooled to RT; diluted with MeCN; filtered; concentrated."
          },
          "product": {
            "compound_id": "C186",
            "name": "112 (isopropenyl intermediate)",
            "yield": "0.50 g (27%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Pd/C hydrogenation (isopropenyl to isopropyl)",
          "reactants": [
            {
              "compound_id": "C186",
              "name": "112",
              "amount": "0.50 g (0.95 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "5% Pd/C",
              "amount": "202 mg",
              "role": "catalyst"
            },
            {
              "compound_id": null,
              "name": "H2",
              "amount": null,
              "role": "reductant"
            }
          ],
          "solvents": [
            {
              "name": "EtOH",
              "volume": "3.2 mL"
            }
          ],
          "conditions": {
            "temperature": "20 °C",
            "time": "3 h",
            "atmosphere": "H2",
            "ph": null,
            "other": "Degassed; filtered; concentrated."
          },
          "product": {
            "compound_id": "C188",
            "name": "18h",
            "yield": "0.45 g (90%)",
            "purity": "85.5% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly in BBr3 dealkylation to give 19h",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "O-dealkylation (aryl ethyl ether to phenol)",
          "reactants": [
            {
              "compound_id": "C188",
              "name": "18h",
              "amount": "0.45 g (0.85 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C02",
              "name": "BBr3 (10 equiv)",
              "amount": "10 equiv",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "3 mL"
            }
          ],
          "conditions": {
            "temperature": "-70 °C then -40 °C",
            "time": "2 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "General dealkylation workup; crude used directly."
          },
          "product": {
            "compound_id": "C10",
            "name": "19h",
            "yield": "0.40 g (94%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none; crude used in next step",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P9",
      "pathway_name": "Synthesis of Alkylating Agent 23c (Scheme 3)",
      "target_compound_id": "C29",
      "target_compound_name": "23c: (S)-3-(2-Chloroacetyl)-1,3-thiazolidine-4-carbonitrile",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Mixed anhydride amidation",
          "reactants": [
            {
              "compound_id": "C126",
              "name": "Boc-D-thiazolidine-4-carboxylic acid (52)",
              "amount": "1.00 g (4.29 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C130",
              "name": "ethyl chloroformate",
              "amount": "767 mg (673 μL, 7.07 mmol, 1.65 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Et3N",
              "amount": "715 mg (984 μL, 7.07 mmol, 1.65 equiv)",
              "role": "base"
            },
            {
              "compound_id": null,
              "name": "NH4OH (25%)",
              "amount": "12.0 g (13.2 mL)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "7.0 mL"
            }
          ],
          "conditions": {
            "temperature": "-15 °C (addition); -20 to -13 °C (NH4OH addition); 25 °C",
            "time": "0.5 h at -15 °C; 16 h at 25 °C",
            "atmosphere": "N2",
            "ph": null,
            "other": "Extracted with CH2Cl2; washed with water and brine; column chromatography."
          },
          "product": {
            "compound_id": "C127",
            "name": "53 (Boc-thiazolidine amide)",
            "yield": "730 mg (73%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 17→100% EtOAc/petroleum ether",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Amide dehydration to nitrile (TFAA)",
          "reactants": [
            {
              "compound_id": "C127",
              "name": "53",
              "amount": "730 mg (3.14 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C131",
              "name": "TFAA",
              "amount": "990 mg (656 μL, 4.71 mmol, 1.5 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Et3N",
              "amount": "954 mg (1.31 mL, 9.43 mmol, 3.0 equiv)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "THF (dry)",
              "volume": "3.5 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C",
            "time": "1.5 h",
            "atmosphere": null,
            "ph": null,
            "other": "Diluted with water; extracted with CH2Cl2; washed."
          },
          "product": {
            "compound_id": "C128",
            "name": "54 (Boc-thiazolidine nitrile)",
            "yield": "690 mg (>100%, crude)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Boc deprotection with TsOH",
          "reactants": [
            {
              "compound_id": "C128",
              "name": "54",
              "amount": "690 mg (3.22 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "TsOH·H2O",
              "amount": "919 mg (4.83 mmol, 1.5 equiv)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "MeCN",
              "volume": "4.8 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "24 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Concentrated; used directly."
          },
          "product": {
            "compound_id": "C129",
            "name": "55 (TsOH salt)",
            "yield": "1.50 g (>100%, crude)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly",
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "N-chloroacetylation",
          "reactants": [
            {
              "compound_id": "C129",
              "name": "55",
              "amount": "1.30 g (4.54 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C132",
              "name": "chloroacetyl chloride",
              "amount": "513 mg (361 μL, 4.54 mmol, 1.0 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Et3N",
              "amount": "919 mg (1.26 mL, 9.08 mmol, 2.0 equiv)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "9.0 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C",
            "time": "2 h",
            "atmosphere": null,
            "ph": null,
            "other": "Diluted with water; extracted with CH2Cl2; washed with water and brine."
          },
          "product": {
            "compound_id": "C29",
            "name": "23c",
            "yield": "360 mg (60% over three steps from 53)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none reported",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P10",
      "pathway_name": "Synthesis of Bicyclic Alkylating Agent 58 (Scheme 3)",
      "target_compound_id": "C31",
      "target_compound_name": "58: [(1S,3S,5S)-3-Cyano-2-azabicyclo[3.1.0]hex-2-yl]acetyl Chloride",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Boc removal with TFAA then TsOH Boc deprotection",
          "reactants": [
            {
              "compound_id": "C133",
              "name": "Boc-protected bicyclic compound 56",
              "amount": "2.50 g (11.1 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C131",
              "name": "TFAA",
              "amount": "9.28 g (6.15 mL, 44.2 mmol, 4.0 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "TsOH·H2O",
              "amount": "5.02 g (26.4 mmol, 2.5 equiv)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "pyridine (17 mL) then MeCN (14 mL)",
              "volume": "31 mL total"
            }
          ],
          "conditions": {
            "temperature": "-10 °C then 25 °C (TFAA step); 25 °C (TsOH step)",
            "time": "16 h (TFAA); 16 h (TsOH)",
            "atmosphere": null,
            "ph": null,
            "other": "TFAA step: diluted with water; extracted with EtOAc; washed. TsOH step: concentrated; triturated with cold EtOAc."
          },
          "product": {
            "compound_id": "C134",
            "name": "57 (TsOH salt)",
            "yield": "2.60 g (88%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "trituration with cold EtOAc (50 mL) at -30 °C for 1.5 h",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "N-chloroacetylation",
          "reactants": [
            {
              "compound_id": "C134",
              "name": "57",
              "amount": "2.60 g (9.27 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C132",
              "name": "chloroacetyl chloride",
              "amount": "3.14 g (2.21 mL, 27.8 mmol, 3.0 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Et3N",
              "amount": "9.38 g (12.9 mL, 92.7 mmol, 10 equiv)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "18 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C then 25 °C",
            "time": "4 h",
            "atmosphere": null,
            "ph": null,
            "other": "Diluted with CH2Cl2; washed with water and brine; dried; purified by column chromatography."
          },
          "product": {
            "compound_id": "C31",
            "name": "58",
            "yield": "1.30 g (76%)",
            "purity": "90.8% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 2% MeOH/CH2Cl2 then 11→20% EtOAc/petroleum ether",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P11",
      "pathway_name": "Synthesis of Tosylate Linker 59 and Compound 51 (Scheme 4)",
      "target_compound_id": "C137",
      "target_compound_name": "Compound 51: [(2S,4R)-4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-2-pyrrolidinyl](3,3-difluoro-1-pyrrolidinyl)methanone",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "EDC/HOBt amide coupling of 3,3-difluoropyrrolidine with Boc-hydroxyproline 40",
          "reactants": [
            {
              "compound_id": "C117",
              "name": "40 (Boc-hydroxyproline)",
              "amount": "300 mg (1.30 mmol)"
            },
            {
              "compound_id": "C135",
              "name": "3,3-difluoropyrrolidine hydrochloride",
              "amount": "205 mg (1.43 mmol, 1.1 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "HOBt",
              "amount": "193 mg (1.43 mmol, 1.1 equiv)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": null,
              "name": "EDC",
              "amount": "274 mg (1.43 mmol, 1.1 equiv)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": null,
              "name": "Et3N",
              "amount": "145 mg (199 μL, 1.43 mmol, 1.1 equiv)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "3 mL"
            }
          ],
          "conditions": {
            "temperature": "20 °C",
            "time": "16 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Quenched with sat. NaHCO3; extracted with CH2Cl2; purified by column chromatography."
          },
          "product": {
            "compound_id": null,
            "name": "difluoropyrrolidine amide alcohol intermediate",
            "yield": "360 mg (87%)",
            "purity": "100.0% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 2.5→100% MeOH/CH2Cl2",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Tosylation of hydroxyl",
          "reactants": [
            {
              "compound_id": null,
              "name": "difluoropyrrolidine amide alcohol intermediate",
              "amount": "200 mg (0.62 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "p-toluenesulfonyl chloride",
              "amount": "262 mg (1.37 mmol, 2.20 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "pyridine",
              "volume": "1.4 mL"
            }
          ],
          "conditions": {
            "temperature": "20 °C",
            "time": "16 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Diluted with water; extracted with EtOAc; washed with brine."
          },
          "product": {
            "compound_id": "C136",
            "name": "59",
            "yield": "280 mg (95%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Cs2CO3-mediated O-alkylation (19a with tosylate 59)",
          "reactants": [
            {
              "compound_id": "C03",
              "name": "19a",
              "amount": "170 mg (0.31 mmol)"
            },
            {
              "compound_id": "C136",
              "name": "59",
              "amount": "367 mg (0.77 mmol, 2.5 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C36",
              "name": "Cs2CO3",
              "amount": "232 mg (0.71 mmol, 2.3 equiv)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF (dry)",
              "volume": "2.5 mL"
            }
          ],
          "conditions": {
            "temperature": "85 °C",
            "time": "16 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Diluted with water; extracted with EtOAc; used directly."
          },
          "product": {
            "compound_id": null,
            "name": "fully protected intermediate for 51",
            "yield": "450 mg (crude)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly",
          "notes": "LC-MS: m/z [M(35Cl)-Boc+H]+ 751.3"
        },
        {
          "step_number": 4,
          "reaction_type": "TFA Boc deprotection",
          "reactants": [
            {
              "compound_id": null,
              "name": "fully protected intermediate for 51",
              "amount": "400 mg (0.47 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C38",
              "name": "TFA",
              "amount": "1.54 g (1.00 mL)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "4 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "3 h",
            "atmosphere": null,
            "ph": null,
            "other": "Concentrated; coevaporated with CH2Cl2 to remove TFA."
          },
          "product": {
            "compound_id": null,
            "name": "Boc-deprotected intermediate, acetyl-protected sugar",
            "yield": "crude",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly",
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "NH3/MeOH sugar deacetylation",
          "reactants": [
            {
              "compound_id": null,
              "name": "Boc-deprotected intermediate (acetylated)",
              "amount": "crude"
            }
          ],
          "reagents": [
            {
              "compound_id": "C39",
              "name": "7 M NH3/MeOH",
              "amount": "10 mL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "MeOH (included in NH3/MeOH)",
              "volume": "10 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "4 h",
            "atmosphere": null,
            "ph": null,
            "other": "Sealed bottle; volatiles removed under vacuum; coevaporated with MeOH."
          },
          "product": {
            "compound_id": "C137",
            "name": "compound 51",
            "yield": "40 mg (25% over three steps from 19a)",
            "purity": "99.9% by HPLC; 99.6% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "preparative HPLC: Waters XBridge OBD C18, 150×40 mm, 10 μm; A=10 mM NH4HCO3, B=MeCN; 15–45% B over 8 min",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P12",
      "pathway_name": "Synthesis of Compound 36 (Gosogliptin-Linker, Scheme 2)",
      "target_compound_id": "C123",
      "target_compound_name": "Compound 36: (S)-1-{[(2S,4S)-4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-2-pyrrolidinyl]carbonyl}-2-pyrrolidinecarbonitrile",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Boc protection of L-hydroxyproline",
          "reactants": [
            {
              "compound_id": "C116",
              "name": "L-hydroxyproline (39)",
              "amount": "2.00 g (15.3 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "1 M NaOH",
              "amount": "24 mL (1.6 equiv)",
              "role": "base"
            },
            {
              "compound_id": null,
              "name": "Boc2O",
              "amount": "3.99 g (4.20 mL, 18.3 mmol, 1.2 equiv)",
              "role": "protecting_group_reagent"
            }
          ],
          "solvents": [
            {
              "name": "2:1 water/1,4-dioxane",
              "volume": "60 mL"
            }
          ],
          "conditions": {
            "temperature": "<10 °C then 20 °C",
            "time": "16 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Concentrated; adjusted to pH 4 with 1 M HCl; extracted with EtOAc (15×100 mL); dried; concentrated."
          },
          "product": {
            "compound_id": "C117",
            "name": "40 (Boc-hydroxyproline)",
            "yield": "1.60 g (45%)",
            "purity": "100.0% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "Boc deprotection of 41 to give 2-cyanopyrrolidinium TsOH salt 42",
          "reactants": [
            {
              "compound_id": "C118",
              "name": "(S)-1-Boc-2-cyanopyrrolidine (41)",
              "amount": "1.50 g (7.64 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "TsOH·H2O",
              "amount": "2.18 g (11.5 mmol, 1.5 equiv)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "MeCN",
              "volume": "7 mL"
            }
          ],
          "conditions": {
            "temperature": "20 °C",
            "time": "48 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Concentrated; triturated with MTBE/CH2Cl2; filtered; washed with MTBE."
          },
          "product": {
            "compound_id": "C119",
            "name": "42 (pyrrolidinium TsOH salt)",
            "yield": "1.90 g (93%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "trituration with MTBE then CH2Cl2",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "EDC/HOBt amide coupling (40 + 42)",
          "reactants": [
            {
              "compound_id": "C117",
              "name": "40",
              "amount": "300 mg (1.30 mmol)"
            },
            {
              "compound_id": "C119",
              "name": "42",
              "amount": "384 mg (1.43 mmol, 1.1 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Et3N",
              "amount": "145 mg (199 μL, 1.43 mmol, 1.1 equiv)",
              "role": "base"
            },
            {
              "compound_id": null,
              "name": "HOBt",
              "amount": "193 mg (1.43 mmol, 1.1 equiv)",
              "role": "coupling_reagent"
            },
            {
              "compound_id": null,
              "name": "EDC",
              "amount": "274 mg (1.43 mmol, 1.1 equiv)",
              "role": "coupling_reagent"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "3 mL"
            }
          ],
          "conditions": {
            "temperature": "20 °C",
            "time": "16 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Quenched with sat. NaHCO3; extracted with CH2Cl2; purified by column chromatography."
          },
          "product": {
            "compound_id": "C120",
            "name": "43",
            "yield": "230 mg (57%)",
            "purity": "97.7% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 0→100% MeOH/CH2Cl2",
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "Tosylation",
          "reactants": [
            {
              "compound_id": "C120",
              "name": "43",
              "amount": "200 mg (0.65 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "p-toluenesulfonyl chloride",
              "amount": "271 mg (1.42 mmol, 2.2 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "pyridine",
              "volume": "1.4 mL"
            }
          ],
          "conditions": {
            "temperature": "20 °C",
            "time": "20 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Diluted with water; extracted with EtOAc; evaporated."
          },
          "product": {
            "compound_id": "C121",
            "name": "44",
            "yield": "310 mg (>100%, crude)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly",
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "Cs2CO3-mediated O-alkylation (19a with tosylate 44)",
          "reactants": [
            {
              "compound_id": "C03",
              "name": "19a",
              "amount": "170 mg (0.31 mmol)"
            },
            {
              "compound_id": "C121",
              "name": "44",
              "amount": "287 mg (0.62 mmol, 2.0 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C36",
              "name": "Cs2CO3",
              "amount": "232 mg (0.71 mmol, 2.3 equiv)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "DMF (dry)",
              "volume": "3.4 mL"
            }
          ],
          "conditions": {
            "temperature": "85 °C",
            "time": "16 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Water added; extracted with EtOAc; used directly."
          },
          "product": {
            "compound_id": "C122",
            "name": "45",
            "yield": "350 mg (>100%, crude)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly",
          "notes": "LC-MS: m/z [M(35Cl)-Boc+H]+ 740.3"
        },
        {
          "step_number": 6,
          "reaction_type": "TFA Boc deprotection",
          "reactants": [
            {
              "compound_id": "C122",
              "name": "45",
              "amount": "300 mg (0.36 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C38",
              "name": "TFA",
              "amount": "1.16 g (0.75 mL)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "3 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "1.5 h",
            "atmosphere": null,
            "ph": null,
            "other": "Concentrated; coevaporated with CH2Cl2."
          },
          "product": {
            "compound_id": null,
            "name": "Boc-deprotected, acetylated intermediate",
            "yield": "300 mg (crude)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none",
          "notes": null
        },
        {
          "step_number": 7,
          "reaction_type": "NH3/MeOH sugar deacetylation",
          "reactants": [
            {
              "compound_id": null,
              "name": "Boc-deprotected acetylated intermediate",
              "amount": "300 mg crude"
            }
          ],
          "reagents": [
            {
              "compound_id": "C39",
              "name": "7 M NH3/MeOH",
              "amount": "6.0 mL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "MeOH (included in NH3/MeOH)",
              "volume": "6.0 mL"
            }
          ],
          "conditions": {
            "temperature": "15 °C",
            "time": "7 h",
            "atmosphere": null,
            "ph": null,
            "other": "Sealed vessel; volatiles removed; coevaporated with MeOH."
          },
          "product": {
            "compound_id": "C123",
            "name": "compound 36",
            "yield": "30 mg (17% over three steps from 19a)",
            "purity": "92.0% by HPLC; 88.9% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "preparative HPLC: Waters XBridge BEH C18, 100×30 mm, 10 μm; A=10 mM NH4HCO3, B=MeCN; 10–30% B over 10 min",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P13",
      "pathway_name": "General Route 1: Synthesis of Dapagliflozin-Series Compounds 26–35, 37–38, 46–50 (exemplified by compound 27)",
      "target_compound_id": "C107",
      "target_compound_name": "Compound 27: (S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(hydroxymethyl)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-2-pyrrolidinecarbonitrile",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Mitsunobu coupling (19a + 20b)",
          "reactants": [
            {
              "compound_id": "C03",
              "name": "19a",
              "amount": "170 mg (0.31 mmol)"
            },
            {
              "compound_id": "C12",
              "name": "20b (gem-dimethyl C4 Boc-amino alcohol)",
              "amount": "168 mg (0.77 mmol, 2.5 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C34",
              "name": "PPh3",
              "amount": "203 mg (0.77 mmol, 2.5 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C32",
              "name": "DIAD",
              "amount": "157 mg (151 μL, 0.77 mmol, 2.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF (dry)",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": "0–5 °C (DIAD addition) then 25 °C",
            "time": "20 h",
            "atmosphere": "N2",
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C48",
            "name": "21b",
            "yield": "168 mg (73%)",
            "purity": "100.0% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica (12.5→22% EtOAc/petroleum ether) then preparative TLC (1:1 EtOAc/petroleum ether)",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "TFA Boc deprotection",
          "reactants": [
            {
              "compound_id": "C48",
              "name": "21b",
              "amount": "100 mg (0.13 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C38",
              "name": "TFA",
              "amount": "200 μL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "2.0 mL"
            }
          ],
          "conditions": {
            "temperature": "30 °C",
            "time": "2 h",
            "atmosphere": null,
            "ph": null,
            "other": "Crude coevaporated with MeCN."
          },
          "product": {
            "compound_id": "C65",
            "name": "22b (TFA salt)",
            "yield": "100 mg (98%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "N-alkylation with chloroacetyl-cyanopyrrolidine 23a",
          "reactants": [
            {
              "compound_id": "C65",
              "name": "22b (TFA salt)",
              "amount": "150 mg (0.20 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C27",
              "name": "23a",
              "amount": "34 mg (0.20 mmol, 1.0 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C35",
              "name": "K2CO3",
              "amount": "82 mg (0.59 mmol, 3.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C37",
              "name": "NaI",
              "amount": "3.0 mg (0.02 mmol, 0.1 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "1.5 mL"
            }
          ],
          "conditions": {
            "temperature": "5 °C (addition) then 25 °C",
            "time": "24 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Diluted with water; extracted with EtOAc; used directly."
          },
          "product": {
            "compound_id": "C82",
            "name": "24b (crude)",
            "yield": "120 mg (crude)",
            "purity": "66.7% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly",
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "NH3/MeOH sugar deacetylation",
          "reactants": [
            {
              "compound_id": "C82",
              "name": "24b (crude)",
              "amount": "120 mg (0.15 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C39",
              "name": "7 M NH3/MeOH",
              "amount": "3.0 mL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "MeOH (in NH3/MeOH)",
              "volume": "3.0 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "6 h",
            "atmosphere": null,
            "ph": null,
            "other": "Sealed vessel; volatiles removed; coevaporated with MeOH."
          },
          "product": {
            "compound_id": "C107",
            "name": "compound 27",
            "yield": "18.0 mg (15% over two steps from 22b)",
            "purity": "100.0% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "preparative HPLC: Waters XBridge, 150×25 mm, 5 μm; A=10 mM NH4HCO3, B=MeCN; 20–40% B over 12 min",
          "notes": "General route applies analogously to all other Route 1 compounds (26–35, 37–38, 46–50); specific reagents and amounts vary per compound."
        }
      ]
    },
    {
      "pathway_id": "P14",
      "pathway_name": "General Route 1: Synthesis of 6-Deoxy Compounds 60–63 (exemplified by compound 61)",
      "target_compound_id": "C195",
      "target_compound_name": "Compound 61: (S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Mitsunobu coupling (19b + 20b)",
          "reactants": [
            {
              "compound_id": "C04",
              "name": "19b",
              "amount": "200 mg (0.41 mmol)"
            },
            {
              "compound_id": "C12",
              "name": "20b",
              "amount": "443 mg (2.04 mmol, 5.0 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C34",
              "name": "PPh3",
              "amount": "267 mg (1.02 mmol, 2.5 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C32",
              "name": "DIAD",
              "amount": "206 mg (198 μL, 1.02 mmol, 2.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF (dry)",
              "volume": "2 mL"
            }
          ],
          "conditions": {
            "temperature": "15 °C",
            "time": "16 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Evaporated with toluene/THF for drying before reaction."
          },
          "product": {
            "compound_id": "C52",
            "name": "21l",
            "yield": "200 mg (71%)",
            "purity": "94.7% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica (12.5→100% EtOAc/petroleum ether) then preparative HPLC (Phenomenex Gemini NX, 150×30 mm; A=10 mM NH4HCO3, B=MeCN; 50–80% B over 8 min)",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "TFA Boc deprotection",
          "reactants": [
            {
              "compound_id": "C52",
              "name": "21l",
              "amount": "816 mg (1.16 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C38",
              "name": "TFA",
              "amount": "500 μL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "2.0 mL"
            }
          ],
          "conditions": {
            "temperature": "15 °C",
            "time": "1 h",
            "atmosphere": null,
            "ph": null,
            "other": "Crude 22l used directly."
          },
          "product": {
            "compound_id": "C75",
            "name": "22l (TFA salt)",
            "yield": "crude",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "N-alkylation with 23d",
          "reactants": [
            {
              "compound_id": "C75",
              "name": "22l (TFA salt)",
              "amount": "816 mg (1.16 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C30",
              "name": "23d (4,4-difluoro-2-cyanopyrrolidine chloroacetyl)",
              "amount": "254 mg (1.22 mmol, 1.05 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C35",
              "name": "K2CO3",
              "amount": "481 mg (3.48 mmol, 3.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C37",
              "name": "NaI",
              "amount": "70 mg (0.46 mmol, 0.4 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "2 mL"
            }
          ],
          "conditions": {
            "temperature": "15 °C",
            "time": "16 h",
            "atmosphere": null,
            "ph": null,
            "other": "Workup gave crude 24r."
          },
          "product": {
            "compound_id": "C98",
            "name": "24r (crude)",
            "yield": "800 mg (crude)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly",
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "NH3/MeOH sugar deacetylation",
          "reactants": [
            {
              "compound_id": "C98",
              "name": "24r (crude)",
              "amount": "1.00 g (~1.31 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C39",
              "name": "7 M NH3/MeOH",
              "amount": "18 mL",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "MeOH (in NH3/MeOH)",
              "volume": "18 mL"
            }
          ],
          "conditions": {
            "temperature": "15 °C",
            "time": "7 h",
            "atmosphere": null,
            "ph": null,
            "other": "Sealed vessel; volatiles removed."
          },
          "product": {
            "compound_id": "C195",
            "name": "compound 61",
            "yield": "200 mg (22% over two steps from 22l)",
            "purity": "98.1% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "preparative HPLC: Phenomenex Gemini NX, 80×40 mm, 3 μm; A=10 mM NH4HCO3, B=MeCN; 25–55% B over 8 min",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P15",
      "pathway_name": "General Route 2: Synthesis of Compound 64 (Triacetylated Prodrug)",
      "target_compound_id": "C105",
      "target_compound_name": "Compound 64: (2R,3R,4S,5S,6S)-4,5-Diacetoxy-6-(3-{[p-(4-{2-[(S)-2-cyano-4,4-difluoro-1-pyrrolidinyl]-2-oxoethylamino}-4-methylpentyloxy)phenyl]methyl}-4-ethylphenyl)-2-methyltetrahydro-2H-pyran-3-yl Acetate",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "TMSI-mediated Boc deprotection of 21m",
          "reactants": [
            {
              "compound_id": "C53",
              "name": "21m",
              "amount": "1.80 g (2.63 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "TMSI (trimethylsilyl iodide)",
              "amount": "2.20 g (1.50 mL, 11.0 mmol, 4.2 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "MeCN",
              "volume": "120 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C",
            "time": "1.5 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with water; extracted with EtOAc; purified by flash column."
          },
          "product": {
            "compound_id": "C76",
            "name": "22m",
            "yield": "1.20 g (78%)",
            "purity": "96.1% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "flash column chromatography on silica, 0–35% EtOAc/petroleum ether",
          "notes": "TMSI used instead of TFA because TFA would also remove sugar acetates."
        },
        {
          "step_number": 2,
          "reaction_type": "N-alkylation with 23d (no final deacetylation)",
          "reactants": [
            {
              "compound_id": "C76",
              "name": "22m",
              "amount": "510 mg (0.73 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C30",
              "name": "23d",
              "amount": "122 mg (0.59 mmol, 0.8 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C35",
              "name": "K2CO3",
              "amount": "303 mg (2.19 mmol, 3.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C37",
              "name": "NaI",
              "amount": "44 mg (0.29 mmol, 0.4 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "5.0 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "4 h",
            "atmosphere": null,
            "ph": null,
            "other": "Standard workup; no final deacetylation (sugar acetates retained as prodrug)."
          },
          "product": {
            "compound_id": "C105",
            "name": "compound 64 (triacetylated prodrug)",
            "yield": "125 mg (31%)",
            "purity": "99.4% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "preparative HPLC: Phenomenex Gemini C18, 75×40 mm, 5 μm; A=10 mM NH4HCO3, B=MeCN; 45–75% B over 8 min",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P16",
      "pathway_name": "General Route 2: Synthesis of Compound 99 (Core Methyl Lead)",
      "target_compound_id": "C214",
      "target_compound_name": "Compound 99: (S)-1-(2-{1,1-Dimethyl-4-[p-({5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]-2-tolyl}methyl)phenoxy]butylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Mitsunobu coupling (19g + 20b)",
          "reactants": [
            {
              "compound_id": "C09",
              "name": "19g",
              "amount": "0.90 g (1.90 mmol)"
            },
            {
              "compound_id": "C12",
              "name": "20b",
              "amount": "1.00 g (4.80 mmol, 2.5 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C34",
              "name": "PPh3",
              "amount": "1.25 g (4.80 mmol, 2.5 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C32",
              "name": "DIAD",
              "amount": "0.97 g (0.90 mL, 4.80 mmol, 2.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "6.3 mL"
            }
          ],
          "conditions": {
            "temperature": "reflux",
            "time": "3 h",
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C60",
            "name": "21u",
            "yield": "0.92 g (81%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 6.5→100% EtOAc/petroleum ether",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "HCl/MeOH dual deprotection (Boc removal + sugar deacetylation)",
          "reactants": [
            {
              "compound_id": "C60",
              "name": "21u",
              "amount": "0.50 g (0.75 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C40",
              "name": "4 M HCl/MeOH",
              "amount": "12.5 mL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "included in HCl/MeOH"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "12 h",
            "atmosphere": null,
            "ph": null,
            "other": "Concentrated; used directly as HCl salt 25d."
          },
          "product": {
            "compound_id": "C203",
            "name": "25d (HCl salt)",
            "yield": "0.60 g (>100%, crude)",
            "purity": "90.0% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "N-alkylation with 23d",
          "reactants": [
            {
              "compound_id": "C203",
              "name": "25d (HCl salt)",
              "amount": "200 mg (0.42 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C30",
              "name": "23d",
              "amount": "174 mg (0.83 mmol, 2.0 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C35",
              "name": "K2CO3",
              "amount": "173 mg (1.25 mmol, 3.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C37",
              "name": "NaI",
              "amount": "25 mg (0.17 mmol, 0.4 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "2.0 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "12 h",
            "atmosphere": null,
            "ph": null,
            "other": "Standard workup."
          },
          "product": {
            "compound_id": "C214",
            "name": "compound 99",
            "yield": "220 mg (44%)",
            "purity": "96.4% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "preparative HPLC: Waters XBridge BEH C18, 250×70 mm, 10 μm; A=0.05% NH4OH+10 mM NH4HCO3, B=MeCN; 35–65% B over 20 min",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P17",
      "pathway_name": "General Route 2: Synthesis of Compound 101 (Lead Compound, Et-Core)",
      "target_compound_id": "C216",
      "target_compound_name": "Compound 101: (S)-1-(2-{4-[p-({2-Ethyl-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Mitsunobu coupling (19c + 20b)",
          "reactants": [
            {
              "compound_id": "C05",
              "name": "19c",
              "amount": "3.00 g (6.19 mmol)"
            },
            {
              "compound_id": "C12",
              "name": "20b",
              "amount": "2.69 g (12.4 mmol, 2.0 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C34",
              "name": "PPh3",
              "amount": "4.06 g (15.5 mmol, 2.5 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C32",
              "name": "DIAD",
              "amount": "3.13 g (3.00 mL, 15.5 mmol, 2.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "30 mL"
            }
          ],
          "conditions": {
            "temperature": "reflux",
            "time": "3 h",
            "atmosphere": null,
            "ph": null,
            "other": null
          },
          "product": {
            "compound_id": "C53",
            "name": "21m",
            "yield": "4.00 g (95%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 5→14% EtOAc/petroleum ether",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "HCl/MeOH dual deprotection",
          "reactants": [
            {
              "compound_id": "C53",
              "name": "21m",
              "amount": "0.80 g (1.17 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C40",
              "name": "4 M HCl/MeOH",
              "amount": "10 mL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "1.0 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "1 h",
            "atmosphere": null,
            "ph": null,
            "other": "Concentrated; 25f used directly."
          },
          "product": {
            "compound_id": "C205",
            "name": "25f (HCl salt)",
            "yield": "790 mg (87%)",
            "purity": "89.7% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "none",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "N-alkylation with 23d (two-portion addition)",
          "reactants": [
            {
              "compound_id": "C205",
              "name": "25f (HCl salt)",
              "amount": "400 mg (0.81 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C30",
              "name": "23d (two portions: 169 mg + 169 mg = 1.0+1.0 equiv each)",
              "amount": "338 mg total (1.62 mmol, 2.0 equiv total)",
              "role": "other"
            },
            {
              "compound_id": "C35",
              "name": "K2CO3",
              "amount": "336 mg (2.43 mmol, 3.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C37",
              "name": "NaI",
              "amount": "49 mg (0.32 mmol, 0.4 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "6.0 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "2 h (first portion) + 12 h (second portion)",
            "atmosphere": null,
            "ph": null,
            "other": "Second portion of 23d added after 2 h; standard workup."
          },
          "product": {
            "compound_id": "C216",
            "name": "compound 101",
            "yield": "110 mg (58%)",
            "purity": "96.0% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "preparative HPLC: Phenomenex Gemini NX, 80×40 mm, 3 μm; A=10 mM NH4HCO3, B=MeCN; 30–60% B over 8 min",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P18",
      "pathway_name": "Synthesis of Compound 102 with Indane Core (Scheme 11)",
      "target_compound_id": "C228",
      "target_compound_name": "Compound 102: (S)-1-(2-{1,1-Dimethyl-4-[p-({6-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]-4-indanyl}methyl)phenoxy]butylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "NBS selective bromination of 5-indanylamine at C6",
          "reactants": [
            {
              "compound_id": "C217",
              "name": "5-indanylamine (113)",
              "amount": "45.0 g (338 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "NBS",
              "amount": "54.1 g (304 mmol, 0.9 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "NMP",
              "volume": "450 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C",
            "time": "1.5 h",
            "atmosphere": null,
            "ph": null,
            "other": "Diluted with water; extracted with EtOAc; washed with brine; purified by column chromatography."
          },
          "product": {
            "compound_id": "C218",
            "name": "114 (6-bromo-5-aminoindane)",
            "yield": "45.0 g (63%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, petroleum ether",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "NIS iodination at C4",
          "reactants": [
            {
              "compound_id": "C218",
              "name": "114",
              "amount": "45.0 g (212 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "N-iodosuccinimide (NIS)",
              "amount": "57.3 g (255 mmol, 1.2 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "AcOH",
              "volume": "450 mL"
            }
          ],
          "conditions": {
            "temperature": "20 °C",
            "time": "12 h",
            "atmosphere": null,
            "ph": null,
            "other": "Diluted with water; extracted with CH2Cl2; washed with brine; purified."
          },
          "product": {
            "compound_id": "C219",
            "name": "115 (6-bromo-4-iodo-5-aminoindane)",
            "yield": "52.8 g (74%)",
            "purity": "95.7% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, petroleum ether",
          "notes": null
        },
        {
          "step_number": 3,
          "reaction_type": "Diazotization and reductive deamination (Sandmeyer-type)",
          "reactants": [
            {
              "compound_id": "C219",
              "name": "115",
              "amount": "23.9 g (70.7 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "NaNO2",
              "amount": "9.76 g (141 mmol, 2.0 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "H2SO4",
              "amount": "190 mL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "EtOH/H2O (10:1)",
              "volume": "528 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C then 20 °C",
            "time": "2 h at 0 °C; 10 h at 20 °C",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with water; extracted with CH2Cl2; purified by column chromatography."
          },
          "product": {
            "compound_id": "C220",
            "name": "116 (6-bromo-4-iodoindane)",
            "yield": "28.9 g (63%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, petroleum ether",
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "n-BuLi lithiation of 116 and addition to TBDPS-benzaldehyde 117",
          "reactants": [
            {
              "compound_id": "C220",
              "name": "116",
              "amount": "19.0 g (58.8 mmol)"
            },
            {
              "compound_id": "C221",
              "name": "TBDPS-benzaldehyde 117",
              "amount": "25.5 g (70.7 mmol, 1.2 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "n-BuLi (2.5 M)",
              "amount": "28.2 mL (1.2 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "285 mL"
            }
          ],
          "conditions": {
            "temperature": "-60 °C (lithiation and addition); warmed to 20 °C",
            "time": "1 h (lithiation); 11 h at 20 °C",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with sat. NH4Cl; extracted with CH2Cl2; purified by column chromatography."
          },
          "product": {
            "compound_id": "C222",
            "name": "118 (diphenylmethanol)",
            "yield": "22.9 g (67%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 0→5% EtOAc/petroleum ether",
          "notes": null
        },
        {
          "step_number": 5,
          "reaction_type": "Et3SiH/BF3·OEt2 reduction of alcohol to diphenylmethylene",
          "reactants": [
            {
              "compound_id": "C222",
              "name": "118",
              "amount": "10.0 g (17.9 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Et3SiH",
              "amount": "2.40 g (3.29 mL, 20.6 mmol, 1.15 equiv)",
              "role": "reductant"
            },
            {
              "compound_id": null,
              "name": "BF3·Et2O",
              "amount": "2.55 g (2.21 mL, 17.9 mmol, 1.0 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "MeCN",
              "volume": "100 mL"
            }
          ],
          "conditions": {
            "temperature": "-20 °C then 0 °C",
            "time": "1.5 h then 0.5 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with water; extracted with CH2Cl2; purified by column chromatography."
          },
          "product": {
            "compound_id": "C223",
            "name": "119 (brominated indane core)",
            "yield": "6.20 g (63%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 0→1% EtOAc/petroleum ether",
          "notes": null
        },
        {
          "step_number": 6,
          "reaction_type": "n-BuLi lithiation of 119 and glycosylation with 6-deoxygluconolactone 120",
          "reactants": [
            {
              "compound_id": "C223",
              "name": "119",
              "amount": "1.0 g (1.85 mmol)"
            },
            {
              "compound_id": "C224",
              "name": "protected 6-deoxygluconolactone 120",
              "amount": "639 mg (1.48 mmol, 0.8 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "n-BuLi (2.50 M)",
              "amount": "739 μL (1.0 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Et3SiH",
              "amount": "649 mg (892 μL, 5.59 mmol, 2.5 equiv)",
              "role": "reductant"
            },
            {
              "compound_id": null,
              "name": "BF3·Et2O",
              "amount": "476 mg (412 μL, 3.35 mmol, 1.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "10 mL; then CH2Cl2 (80 mL each) for reduction"
            }
          ],
          "conditions": {
            "temperature": "-70 °C (lithiation/addition); Et3SiH/BF3 step at -70→0 °C",
            "time": "1 h (lithiation); 2 h (glycosylation); 2 h (anomeric reduction)",
            "atmosphere": null,
            "ph": null,
            "other": "Two batches; anomeric reduction quenched with water; purified by column chromatography."
          },
          "product": {
            "compound_id": "C225",
            "name": "121 (TBDPS/Bn-protected C-glucoside)",
            "yield": "3.40 g combined (75%; 44% over two steps from 119)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 0→1% EtOAc/petroleum ether",
          "notes": "Two parallel batches combined."
        },
        {
          "step_number": 7,
          "reaction_type": "TBAF desilylation then Mitsunobu coupling with 20b",
          "reactants": [
            {
              "compound_id": "C225",
              "name": "121",
              "amount": "1.70 g (1.93 mmol)"
            },
            {
              "compound_id": "C12",
              "name": "20b",
              "amount": "529 mg (2.43 mmol, 1.2 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C174",
              "name": "TBAF (1.0 M in THF)",
              "amount": "2.42 mL (1.25 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C34",
              "name": "PPh3",
              "amount": "585 mg (2.23 mmol, 1.1 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C32",
              "name": "DIAD",
              "amount": "492 mg (427 μL, 2.43 mmol, 1.2 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "51 mL (TBAF) + 13 mL (Mitsunobu)"
            }
          ],
          "conditions": {
            "temperature": "0 °C then 20 °C (TBAF); 70 °C (Mitsunobu)",
            "time": "0.5 h (TBAF); 3 h (Mitsunobu)",
            "atmosphere": null,
            "ph": null,
            "other": "TBAF step: quenched with water; extracted with EtOAc; phenol intermediate taken directly to Mitsunobu."
          },
          "product": {
            "compound_id": "C226",
            "name": "122",
            "yield": "1.20 g (67%; 60% over two steps from 121)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 1→5% EtOAc/petroleum ether",
          "notes": null
        },
        {
          "step_number": 8,
          "reaction_type": "High-pressure Pd(OH)2/Pd/C hydrogenation to remove Bn groups",
          "reactants": [
            {
              "compound_id": "C226",
              "name": "122",
              "amount": "1.20 g (1.43 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Pd(OH)2",
              "amount": "400 mg",
              "role": "catalyst"
            },
            {
              "compound_id": null,
              "name": "Pd/C (10%)",
              "amount": "400 mg",
              "role": "catalyst"
            },
            {
              "compound_id": null,
              "name": "H2 (3.4 atm)",
              "amount": null,
              "role": "reductant"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "200 mL"
            }
          ],
          "conditions": {
            "temperature": "80 °C",
            "time": "12 h",
            "atmosphere": "H2 (3.4 atm, sealed tube)",
            "ph": null,
            "other": "Filtered; concentrated; purified by column chromatography."
          },
          "product": {
            "compound_id": "C227",
            "name": "123",
            "yield": "0.59 g (70%)",
            "purity": "83.4% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 9→50% EtOAc/petroleum ether",
          "notes": null
        },
        {
          "step_number": 9,
          "reaction_type": "HCl/MeOH Boc deprotection",
          "reactants": [
            {
              "compound_id": "C227",
              "name": "123",
              "amount": "0.59 g (1.04 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C40",
              "name": "4 M HCl/MeOH",
              "amount": "7.37 mL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "3.62 mL"
            }
          ],
          "conditions": {
            "temperature": "20 °C",
            "time": "2 h",
            "atmosphere": null,
            "ph": null,
            "other": "Concentrated; coevaporated with MeCN."
          },
          "product": {
            "compound_id": null,
            "name": "HCl salt of Boc-deprotected 123",
            "yield": "0.55 g (crude)",
            "purity": "96.6% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly",
          "notes": null
        },
        {
          "step_number": 10,
          "reaction_type": "N-alkylation with 23d",
          "reactants": [
            {
              "compound_id": null,
              "name": "HCl salt of deprotected 123",
              "amount": "0.50 g (0.99 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C30",
              "name": "23d",
              "amount": "309 mg (1.48 mmol, 1.5 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C35",
              "name": "K2CO3",
              "amount": "410 mg (2.96 mmol, 3.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C37",
              "name": "NaI",
              "amount": "59 mg (0.40 mmol, 0.4 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "10 mL"
            }
          ],
          "conditions": {
            "temperature": "50 °C",
            "time": "3 h",
            "atmosphere": null,
            "ph": null,
            "other": "Reaction mixture filtered; filtrate purified by preparative HPLC."
          },
          "product": {
            "compound_id": "C228",
            "name": "compound 102",
            "yield": "399 mg (63%; 60% over 2 steps from 123)",
            "purity": "99.8% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "preparative HPLC: Phenomenex Gemini C18, 75×40 mm, 3 μm; A=10 mM NH4HCO3, B=MeCN; 20–50% B over 8 min",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P19",
      "pathway_name": "Synthesis of Compound 96 (N-Methyl Analogue of 61)",
      "target_compound_id": "C211",
      "target_compound_name": "Compound 96: (S)-1-[2-({4-[p-({2-Chloro-5-[(2S,3R,4S,5S,6R)-3,4,5-trihydroxy-6-methyltetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutyl}-N-methylamino)acetyl]-4,4-difluoro-2-pyrrolidinecarbonitrile",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Selective N-methylation of compound 61",
          "reactants": [
            {
              "compound_id": "C195",
              "name": "compound 61",
              "amount": "0.16 g (0.25 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "K2CO3",
              "amount": "173 mg (1.26 mmol, 5.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": null,
              "name": "iodomethane",
              "amount": "36 mg (16 μL, 0.25 mmol, 1.0 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "1.0 mL"
            }
          ],
          "conditions": {
            "temperature": "20 °C",
            "time": "2 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with NH4OH and sat. NH4Cl; extracted with EtOAc; washed with brine."
          },
          "product": {
            "compound_id": "C211",
            "name": "compound 96",
            "yield": "25 mg (15%)",
            "purity": "97.9% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "preparative HPLC: Waters Xbridge BEH C18, 100×25 mm, 10 μm; A=10 mM NH4HCO3, B=MeCN; 40–70% B over 8 min",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P20",
      "pathway_name": "Synthesis of Sotagliflozin-Inspired Compounds 67 and 68 (Route 2)",
      "target_compound_id": "C207",
      "target_compound_name": "Compound 67: (2S,4S)-1-(2-{4-[p-({2-Chloro-5-[(2S,3R,4R,5S,6R)-3,4,5-trihydroxy-6-(methylthio)tetrahydro-2H-pyran-2-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4-fluoro-2-pyrrolidinecarbonitrile",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "TFA Boc deprotection of 21n, then HCl/MeOH deacetylation",
          "reactants": [
            {
              "compound_id": "C54",
              "name": "21n",
              "amount": "1.20 g (1.66 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C38",
              "name": "TFA",
              "amount": "6.16 g (4.0 mL)",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "15 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "1 h (TFA); then 12 h (HCl/MeOH on portion)",
            "atmosphere": null,
            "ph": null,
            "other": "First concentrated to yellow oil; a portion (0.60 g) taken for HCl/MeOH deprotection."
          },
          "product": {
            "compound_id": "C202",
            "name": "25c (HCl salt)",
            "yield": "0.31 g (92%)",
            "purity": "93.3% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "none",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "N-alkylation with 23b to give compound 67",
          "reactants": [
            {
              "compound_id": "C202",
              "name": "25c (HCl salt)",
              "amount": "70 mg (0.14 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C28",
              "name": "23b",
              "amount": "32 mg (0.17 mmol, 1.2 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C35",
              "name": "K2CO3",
              "amount": "98 mg (0.71 mmol, 5.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C37",
              "name": "NaI",
              "amount": "21 mg (0.14 mmol, 1.0 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "1.0 mL"
            }
          ],
          "conditions": {
            "temperature": "25 °C",
            "time": "12 h",
            "atmosphere": null,
            "ph": null,
            "other": "Reaction mixture filtered; concentrated; purified by preparative HPLC."
          },
          "product": {
            "compound_id": "C207",
            "name": "compound 67",
            "yield": "28 mg (30%)",
            "purity": "95.4% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "preparative HPLC: Phenomenex Luna C18, 100×40 mm, 5 μm; A=0.04% HCl in H2O, B=MeCN; 40–80% B over 8 min",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P21",
      "pathway_name": "Synthesis of Compound 65 (Spiro-Cyclopropyl, Scheme 6)",
      "target_compound_id": "C152",
      "target_compound_name": "Compound 65: (S)-1-(2-{4-[p-({2-Ethyl-5-[(5S,6R,7R,8S)-6,7,8-trihydroxy-4-oxa-5-spiro[2.5]octyl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Appel iodination of dapagliflozin 2 primary alcohol",
          "reactants": [
            {
              "compound_id": "C148",
              "name": "dapagliflozin 2",
              "amount": "60 g (147 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C34",
              "name": "PPh3",
              "amount": "61.5 g (235 mmol, 1.6 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "imidazole",
              "amount": "15.0 g (220 mmol, 1.5 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "I2",
              "amount": "55.8 g (220 mmol, 1.5 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "600 mL"
            }
          ],
          "conditions": {
            "temperature": "50 °C",
            "time": "18 h",
            "atmosphere": null,
            "ph": null,
            "other": "Diluted with water; extracted with EtOAc; purified by column chromatography."
          },
          "product": {
            "compound_id": "C147",
            "name": "75 (iodomethyl dapagliflozin)",
            "yield": "51 g (67%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 0→100% EtOAc/petroleum ether",
          "notes": null
        },
        {
          "step_number": 2,
          "reaction_type": "NaOMe-mediated β-elimination to alkene",
          "reactants": [
            {
              "compound_id": "C147",
              "name": "75",
              "amount": "51 g (98.3 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "NaOMe",
              "amount": "53.1 g (983 mmol, 10 equiv)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "MeOH",
              "volume": "500 mL"
            }
          ],
          "conditions": {
            "temperature": "65 °C",
            "time": "18 h",
            "atmosphere": null,
            "ph": null,
            "other": "Diluted with water; extracted with EtOAc; purified by column chromatography."
          },
          "product": {
            "compound_id": null,
            "name": "alkene intermediate (76 precursor)",
            "yield": "26 g (45%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 0→100% EtOAc/petroleum ether",
          "notes": "An aliquot of 3.50 g taken for Simmons-Smith."
        },
        {
          "step_number": 3,
          "reaction_type": "Simmons-Smith cyclopropanation",
          "reactants": [
            {
              "compound_id": null,
              "name": "alkene intermediate",
              "amount": "3.50 g (8.95 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "CH2I2",
              "amount": "19.2 g (5.78 mL, 71.6 mmol, 8.0 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "ZnEt2 (2.0 M in hexane)",
              "amount": "35.8 mL (8.0 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "CH2Cl2",
              "volume": "70 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C then 20 °C",
            "time": "12 h",
            "atmosphere": null,
            "ph": null,
            "other": "Quenched with water; extracted with EtOAc; preparative HPLC/trituration."
          },
          "product": {
            "compound_id": "C149",
            "name": "76 (spiro-cyclopropyl triol)",
            "yield": "1.32 g (36%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "preparative HPLC: Waters XBridge, 150×25 mm, 5 μm; A=10 mM NH4HCO3, B=MeCN; 40–70% B then trituration with 1:10 EtOAc/petroleum ether",
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "Suzuki-Miyaura coupling (Ar-Cl to Ar-Et via NHC-borane 74)",
          "reactants": [
            {
              "compound_id": "C149",
              "name": "76",
              "amount": "500 mg (1.23 mmol)"
            },
            {
              "compound_id": "C142",
              "name": "NHC-borane 74",
              "amount": "781 mg (1.61 mmol, 1.3 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C144",
              "name": "Pd(OAc)2",
              "amount": "55 mg (0.25 mmol, 0.2 equiv)",
              "role": "catalyst"
            },
            {
              "compound_id": "C145",
              "name": "RuPhos",
              "amount": "230 mg (0.49 mmol, 0.4 equiv)",
              "role": "catalyst"
            }
          ],
          "solvents": [
            {
              "name": "10:1 toluene/water",
              "volume": "11 mL"
            }
          ],
          "conditions": {
            "temperature": "80 °C",
            "time": "12 h",
            "atmosphere": "N2",
            "ph": null,
            "other": "Sealed tube; quenched with water; extracted with EtOAc."
          },
          "product": {
            "compound_id": null,
            "name": "Suzuki cross-coupling product (Et-group installed, phenol unmasked)",
            "yield": "2.50 g (70%; from combined batches)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 1→100% EtOAc/petroleum ether",
          "notes": "Multiple parallel reactions combined."
        },
        {
          "step_number": 5,
          "reaction_type": "Ac2O acetylation (sugar triol protection) then BBr3 phenol deprotection",
          "reactants": [
            {
              "compound_id": null,
              "name": "Suzuki coupling product",
              "amount": "1.00 g (2.50 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Ac2O",
              "amount": "1.02 g (0.94 mL, 10.0 mmol, 4.0 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "DIPEA",
              "amount": "1.30 g (1.75 mL, 10.0 mmol, 4.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": null,
              "name": "DMAP",
              "amount": "31 mg (0.25 mmol, 0.1 equiv)",
              "role": "catalyst"
            },
            {
              "compound_id": "C02",
              "name": "BBr3 (2.0 M in CH2Cl2)",
              "amount": "11.1 mL (10 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "toluene (acetylation); CH2Cl2 (dealkylation)",
              "volume": "10 mL + 23 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C then 20 °C (acetylation); -60 to -20 °C (BBr3)",
            "time": "3 h (acetylation); 3 h (BBr3)",
            "atmosphere": "N2",
            "ph": null,
            "other": "Acetylation: quenched with water; extracted with EtOAc. BBr3: quenched with water; extracted with CH2Cl2."
          },
          "product": {
            "compound_id": "C150",
            "name": "77",
            "yield": "300 mg (27%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "preparative TLC (1:3 EtOAc/petroleum ether)",
          "notes": null
        },
        {
          "step_number": 6,
          "reaction_type": "Mitsunobu coupling (77 + 20b)",
          "reactants": [
            {
              "compound_id": "C150",
              "name": "77",
              "amount": "50.0 mg (0.10 mmol)"
            },
            {
              "compound_id": "C12",
              "name": "20b",
              "amount": "87.5 mg (0.40 mmol, 4.0 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C32",
              "name": "DIAD",
              "amount": "82 mg (78 μL, 0.40 mmol, 4.0 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C34",
              "name": "PPh3",
              "amount": "106 mg (0.40 mmol, 4.0 equiv)",
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
            "temperature": "70 °C",
            "time": "3 h",
            "atmosphere": "N2 (sealed tube)",
            "ph": null,
            "other": "Quenched with water; extracted; six parallel reactions combined and purified."
          },
          "product": {
            "compound_id": "C151",
            "name": "78",
            "yield": "280 mg (63%)",
            "purity": "81.9% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "preparative TLC (1:3 EtOAc/petroleum ether)",
          "notes": "Six parallel reactions combined."
        },
        {
          "step_number": 7,
          "reaction_type": "HCl/MeOH simultaneous Boc removal and sugar deacetylation, then N-alkylation",
          "reactants": [
            {
              "compound_id": "C151",
              "name": "78",
              "amount": "140 mg (0.20 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C40",
              "name": "4 M HCl/MeOH",
              "amount": "40 mL",
              "role": "acid"
            },
            {
              "compound_id": "C30",
              "name": "23d",
              "amount": "124 mg (0.59 mmol, 1.50 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C35",
              "name": "K2CO3",
              "amount": "164 mg (1.19 mmol, 3.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C37",
              "name": "NaI",
              "amount": "24 mg (0.16 mmol, 0.4 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "MeOH (deprotection); DMF (alkylation)",
              "volume": "7 mL + 4.0 mL"
            }
          ],
          "conditions": {
            "temperature": "20 °C (deprotection); 25 °C (alkylation)",
            "time": "12 h (deprotection); 12 h (alkylation)",
            "atmosphere": null,
            "ph": null,
            "other": "Deprotection: concentrated; coevaporated. Alkylation: diluted with CH2Cl2; purified by column chromatography."
          },
          "product": {
            "compound_id": "C152",
            "name": "compound 65",
            "yield": "58 mg (45% over two steps from 78)",
            "purity": "98.1% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 2→5% MeOH/CH2Cl2",
          "notes": null
        }
      ]
    },
    {
      "pathway_id": "P22",
      "pathway_name": "Synthesis of Ertugliflozin Analogue Compound 66 (Scheme 7)",
      "target_compound_id": "C161",
      "target_compound_name": "Compound 66: (S)-1-(2-{4-[p-({2-Ethyl-5-[(1S,2S,3S,4R,5S)-2,3,4-trihydroxy-1-methyl-6,8-dioxabicyclo[3.2.1]oct-5-yl]phenyl}methyl)phenoxy]-1,1-dimethylbutylamino}acetyl)-4,4-difluoro-2-pyrrolidinecarbonitrile",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "Acetylation and allyl deprotection of compound 79",
          "reactants": [
            {
              "compound_id": "C153",
              "name": "compound 79 (allyloxy ertugliflozin analogue)",
              "amount": "2.0 g (4.46 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "Ac2O",
              "amount": "2.27 g (2.09 mL, 22.3 mmol, 5.0 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "DIEA",
              "amount": "4.03 g (5.43 mL, 31.2 mmol, 7.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": null,
              "name": "DMAP",
              "amount": "190 mg (1.56 mmol, 0.35 equiv)",
              "role": "catalyst"
            },
            {
              "compound_id": null,
              "name": "1,3-dimethylbarbituric acid",
              "amount": "2.53 g (16.2 mmol, 10 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "Pd(PPh3)4",
              "amount": "561 mg (0.49 mmol, 0.3 equiv)",
              "role": "catalyst"
            }
          ],
          "solvents": [
            {
              "name": "THF (acetylation and allyl removal)",
              "volume": "10 mL each step"
            }
          ],
          "conditions": {
            "temperature": "0 °C then 1 h (acetylation); 90 °C then 1 h (allyl removal)",
            "time": "1 h each",
            "atmosphere": null,
            "ph": null,
            "other": "Three batches pooled after allyl removal; purified by column chromatography."
          },
          "product": {
            "compound_id": "C154",
            "name": "80 (phenol, acetylated bicyclic ertugliflozin analogue)",
            "yield": "2.5 g (81%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 0→100% EtOAc/petroleum ether",
          "notes": "Three batches from acetylation combined before allyl deprotection."
        },
        {
          "step_number": 2,
          "reaction_type": "Mitsunobu coupling (80 + 20b)",
          "reactants": [
            {
              "compound_id": "C154",
              "name": "80",
              "amount": "500 mg (0.87 mmol)"
            },
            {
              "compound_id": "C12",
              "name": "20b",
              "amount": "376 mg (1.73 mmol, 2.0 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C32",
              "name": "DIAD",
              "amount": "351 mg (336 μL, 1.73 mmol, 2.0 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C34",
              "name": "PPh3",
              "amount": "455 mg (1.73 mmol, 2.0 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "THF",
              "volume": "5 mL"
            }
          ],
          "conditions": {
            "temperature": "70 °C",
            "time": "1 h (sealed tube)",
            "atmosphere": null,
            "ph": null,
            "other": "Diluted with water; extracted with EtOAc; five batches pooled."
          },
          "product": {
            "compound_id": "C155",
            "name": "81 (Mitsunobu product)",
            "yield": "3.1 g (86%) from combined batches",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 0→100% EtOAc/petroleum ether",
          "notes": "Five parallel reactions pooled."
        },
        {
          "step_number": 3,
          "reaction_type": "LiOH deacetylation of sugar",
          "reactants": [
            {
              "compound_id": "C155",
              "name": "81",
              "amount": "2.00 g (2.58 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": null,
              "name": "LiOH·H2O",
              "amount": "216 mg (5.15 mmol, 2.0 equiv)",
              "role": "base"
            }
          ],
          "solvents": [
            {
              "name": "2:3:1 THF/MeOH/H2O",
              "volume": "30 mL"
            }
          ],
          "conditions": {
            "temperature": "0 °C",
            "time": "1 h",
            "atmosphere": null,
            "ph": null,
            "other": "Diluted with water; extracted with EtOAc; used directly."
          },
          "product": {
            "compound_id": null,
            "name": "LiOH-deacetylated 81 (triol product)",
            "yield": "1.50 g (85%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "none; used directly",
          "notes": null
        },
        {
          "step_number": 4,
          "reaction_type": "Iodination/hydrogenation (C6-deoxygenation sequence)",
          "reactants": [
            {
              "compound_id": null,
              "name": "triol intermediate from 81 deacetylation",
              "amount": "500 mg (0.82 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C34",
              "name": "PPh3",
              "amount": "539 mg (2.06 mmol, 2.5 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "imidazole",
              "amount": "279 mg (4.11 mmol, 5.0 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "I2",
              "amount": "521 mg (2.06 mmol, 2.5 equiv)",
              "role": "other"
            },
            {
              "compound_id": null,
              "name": "10% Pd/C",
              "amount": "500 mg",
              "role": "catalyst"
            },
            {
              "compound_id": null,
              "name": "Et3N",
              "amount": "338 mg (465 μL, 3.34 mmol, 3.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": null,
              "name": "H2 (1 atm)",
              "amount": null,
              "role": "reductant"
            }
          ],
          "solvents": [
            {
              "name": "toluene (iodination); MeOH (hydrogenation)",
              "volume": "10 mL + 10 mL"
            }
          ],
          "conditions": {
            "temperature": "80 °C (iodination); 20 °C (hydrogenation)",
            "time": "2 h (iodination); 2 h (hydrogenation)",
            "atmosphere": "H2 (1 atm, hydrogenation)",
            "ph": null,
            "other": "Iodination: quenched with sat. NaHSO3; column chromatography. Hydrogenation: filtered; concentrated."
          },
          "product": {
            "compound_id": "C156",
            "name": "82 (6-deoxy ertugliflozin-Cl analogue)",
            "yield": "0.50 g total (76% hydrogenation; 49% iodination)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica (iodination step), 0→100% EtOAc/petroleum ether",
          "notes": "Additional runs provided total 0.80 g of iodide for hydrogenation."
        },
        {
          "step_number": 5,
          "reaction_type": "Suzuki-Miyaura with vinylboronic acid pinacol ester (SPhos Pd G3), then hydrogenation",
          "reactants": [
            {
              "compound_id": "C156",
              "name": "82",
              "amount": "250 mg (0.42 mmol)"
            },
            {
              "compound_id": "C157",
              "name": "vinylboronic acid pinacol ester",
              "amount": "325 mg (358 μL, 2.11 mmol, 5.0 equiv)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C158",
              "name": "SPhos Pd G3",
              "amount": "132 mg (0.17 mmol, 0.4 equiv)",
              "role": "catalyst"
            },
            {
              "compound_id": null,
              "name": "K3PO4",
              "amount": "448 mg (2.11 mmol, 5.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": null,
              "name": "10% Pd/C",
              "amount": "50 mg",
              "role": "catalyst"
            },
            {
              "compound_id": null,
              "name": "H2 (1 atm)",
              "amount": null,
              "role": "reductant"
            }
          ],
          "solvents": [
            {
              "name": "4:1 1,4-dioxane/H2O (coupling); MeOH (hydrogenation)",
              "volume": "5 mL + 5 mL"
            }
          ],
          "conditions": {
            "temperature": "150 °C microwave, 1 h (coupling); 20 °C, 1 h (hydrogenation)",
            "time": "1 h each",
            "atmosphere": "microwave irradiation (coupling); H2 1 atm (hydrogenation)",
            "ph": null,
            "other": "Two batches combined; purified by column chromatography."
          },
          "product": {
            "compound_id": "C159",
            "name": "83 (Et-group installed)",
            "yield": "200 mg (66% hydrogenation; 61% coupling)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "column chromatography on silica, 0→100% EtOAc/petroleum ether",
          "notes": "Two parallel coupling batches combined."
        },
        {
          "step_number": 6,
          "reaction_type": "HCl/dioxane Boc deprotection",
          "reactants": [
            {
              "compound_id": "C159",
              "name": "83",
              "amount": "200 mg (0.34 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C40",
              "name": "4 M HCl/1,4-dioxane",
              "amount": "3 mL",
              "role": "acid"
            }
          ],
          "solvents": [
            {
              "name": "1,4-dioxane",
              "volume": "3 mL"
            }
          ],
          "conditions": {
            "temperature": "20 °C",
            "time": "2 h",
            "atmosphere": null,
            "ph": null,
            "other": "Volatiles removed; partitioned between water and EtOAc; aqueous concentrated; triturated with EtOAc."
          },
          "product": {
            "compound_id": "C160",
            "name": "84 (HCl salt)",
            "yield": "120 mg (67%)",
            "purity": null,
            "hplc_retention_time_min": null
          },
          "purification": "trituration with EtOAc",
          "notes": null
        },
        {
          "step_number": 7,
          "reaction_type": "N-alkylation with 23d",
          "reactants": [
            {
              "compound_id": "C160",
              "name": "84 (HCl salt)",
              "amount": "120 mg (0.23 mmol)"
            }
          ],
          "reagents": [
            {
              "compound_id": "C30",
              "name": "23d",
              "amount": "58 mg (0.28 mmol, 1.2 equiv)",
              "role": "other"
            },
            {
              "compound_id": "C35",
              "name": "K2CO3",
              "amount": "95 mg (0.69 mmol, 3.0 equiv)",
              "role": "base"
            },
            {
              "compound_id": "C37",
              "name": "NaI",
              "amount": "14 mg (0.09 mmol, 0.4 equiv)",
              "role": "other"
            }
          ],
          "solvents": [
            {
              "name": "DMF",
              "volume": "2 mL"
            }
          ],
          "conditions": {
            "temperature": "50 °C",
            "time": "6 h",
            "atmosphere": null,
            "ph": null,
            "other": "Diluted with water; extracted with EtOAc; washed with brine; purified by preparative HPLC."
          },
          "product": {
            "compound_id": "C161",
            "name": "compound 66",
            "yield": "60 mg (40%)",
            "purity": "97.1% by LC-MS",
            "hplc_retention_time_min": null
          },
          "purification": "preparative HPLC: WePure Biotech XP tC18, 150×40 mm, 7 μm; A=10 mM NH4HCO3, B=MeCN; 30–70% B over 8 min",
          "notes": null
        }
      ]
    }
  ]
}
```

##### Verification
Based on a careful review of the provided sources, **the pasted extraction is NOT correct and contains several major hallucinations and misattributions.** While much of the metadata and earlier synthetic steps are accurate, the extraction fabricates specific experimental details and structural-activity relationship (SAR) data that do not exist in the provided text.

Here are the specific hallucinations and errors in the extraction:

1. Fabricated Synthetic Procedures (Pathways P16 & P17)

The extractor fabricated the reagent masses, equivalents, and yields for the final steps of compounds **99** and **101**. The specific experimental procedures for these final steps are omitted from the provided source text, so the model extrapolated or hallucinated them.

- **Pathway P17 (Compound 101):** The extraction claims a reaction using "400 mg (0.81 mmol) of 25f", "336 mg of K2CO3", "49 mg of NaI", and "yield 110 mg (58%)". **This is a hallucination.** The extractor lifted these exact numbers from the synthesis of **Compound 125** (found in the text of image ) and falsely applied them to Compound 101, merely swapping out the alkylating agent in the text to make it fit.
- **Pathway P16 (Compound 99):** The extraction fabricates a reaction using "200 mg (0.42 mmol) of 25d", "173 mg of K2CO3", "25 mg of NaI", and a "yield of 220 mg (44%)". There is no such procedure or yield for compound 99 in the provided text.

2. Incorrect Yield Data (Pathway P19)

- **Pathway P19 (Compound 96):** The extraction claims the synthesis of Compound 96 resulted in a "yield 25 mg (15%)". However, the actual source text for Compound 96 (found in the text of image ) states that the yield is **"30 mg, 17%"**.

3. Hallucinated SAR & Biological Data in Compound Descriptions

The extraction includes specific biological conclusions in the descriptions of several final products. While these might be accurate to the broader (unprovided) full paper, they are **not supported by the provided source text** (which lacks the in vitro SGLT/DPP4 IC50 tables for these specific compounds).

- **C231 (Compound 126):** Claims it has an "SGLT2/1 ratio 4.6". This number does not appear anywhere in the source text.
- **C229 (Compound 124):** Claims it has "2-fold lower DPP4 potency than 101". This is not stated in the sources.
- **C215 (Compound 100):** Claims it has "near-equal SGLT1/2 potency". This is not stated in the sources.
- **C211 (Compound 96):** Claims it is "essentially inactive against DPP4". This is not stated in the sources.
- **C209 (Compound 94):** Claims the synthesis "sacrificed DPP4 activity". This is not stated in the sources.

**Conclusion:** To fix this extraction, the hallucinated SAR commentary in the "description" fields must be removed, and the synthetic steps for Compounds 99 and 101 (Pathways 16 & 17) must be marked as "Not provided in text" rather than filled with fabricated parameters.

#### Gap Evaluation: v3.1 and v2.4 vs. Full Paper Content

##### Missing Compounds

|Compound|Name|Source Location|In v2.4|In v3.1|Gap Type|
|---|---|---|---|---|---|
|S1|Methyl 5-oxobicyclo[2.2.2]octane-2-carboxylate|SI Scheme S1|No|No|Missing in both|
|S2|5-Oxobicyclo[2.2.2]oct-2-yl 2-methyl-2-propanecarbamate|SI Scheme S1|No|No|Missing in both|
|S3|5-Hydroxybicyclo[2.2.2]oct-2-yl 2-methyl-2-propanecarbamate|SI Scheme S1|No|No|Missing in both|
|20k|tert-Butyl [5-(Tosyloxy)bicyclo[2.2.2]oct-2-yl]carbamate|SI Scheme S1 + main text|Partial (no pathway)|Partial (no pathway)|Pathway missing in both|
|S4|Partially deacetylated O-alkylation product of 19a + 20f|SI Scheme S2|No|No|Missing in both|
|S5|3-[p-(dapagliflozin-yl)phenoxy]cyclopentanammonium TFA|SI Scheme S2|No|No|Missing in both|
|S6|2-[(p-Hydroxyphenyl)methyl]-4-bromo-1-chlorobenzene|SI Scheme S3|No|No|Missing in both|
|S7|2-{[p-(Allyloxy)phenyl]methyl}-4-bromo-1-chlorobenzene|SI Scheme S3|No|No|Missing in both|
|S8|TMS-protected D-gluconolactone (used in S3 route)|SI Scheme S3|No|No|Missing in both|
|S9|Allyloxy C-glycoside methyl glycoside|SI Scheme S3|No|No|Missing in both|
|S10|TMS-protected allyloxy C-glycoside primary alcohol|SI Scheme S3|No|No|Missing in both|
|S11|TMS-protected allyloxy C-glycoside aldehyde|SI Scheme S3|No|No|Missing in both|
|S12|Allyloxy bis(hydroxymethyl) C-glycoside|SI Scheme S3|No|No|Missing in both|
|79|Allyloxy dioxabicyclo[3.2.1]octane triol|SI Scheme S3 + main text|Partial (entry only, no pathway)|Partial (entry only, no pathway)|Pathway missing in both|
|S13|N-Boc-1-amino-1-cyclopentanemethanol|SI Scheme S4|No|No|Missing in both|
|S14|1-Formylcyclopentyl 2-methyl-2-propanecarbamate|SI Scheme S4|No|No|Missing in both|
|S15|Methyl 3-{1-[tert-butyl(oxycarbonylamino)]cyclopentyl}propionate|SI Scheme S4|No|No|Missing in both|
|20n|1-(3-Hydroxypropyl)cyclopentyl 2-methyl-2-propanecarbamate|SI Scheme S4|Partial (entry only)|Partial (entry only)|Pathway missing in both|

---

##### Section 2 — Missing Synthesis Pathways

|Pathway|Target Compound|Steps|Key Reactions|In v2.4|In v3.1|Notes|
|---|---|---|---|---|---|---|
|Scheme S1|20k (bicyclooctyl tosylate linker)|4|LiOH hydrolysis → Curtius rearrangement (DPPA/t-BuOH) → NaBH4 reduction → TsCl tosylation|No|No|Full procedure in SI p. S2–S3. Both versions list 20k as a compound entry but give no synthetic route.|
|Scheme S2|Compound 31 (via S4 → S5)|4|Cs2CO3 O-alkylation of 19a + 20f → NH3/MeOH deprotection → TFA Boc removal → N-alkylation with 23a|No|No|Full procedure in SI p. S3–S4. Compound 31 appears as a final product in both extractions but the modified route via S4/S5 is absent.|
|Scheme S3|79 (allyloxy ertugliflozin precursor)|8|Allyl O-protection → n-BuLi glucosylation (S8) → MsOH methylation → TMSCl silylation → Na2CO3 desilylation → Py·SO3 oxidation → NaOEt/paraformaldehyde → TFA cyclisation|No|No|Full procedure in SI p. S5–S6 with amounts and yields for all 8 steps. Largest single gap in both extractions.|
|Scheme S4|20n (spiro-cyclopentyl linker)|4|IBX oxidation of S13 → HWE olefination (triethyl phosphonoacetate/NaH) → Pd/C hydrogenation → LiBH4 ester reduction|No|No|Full procedure in SI p. S7. Both versions list 20n as a compound entry but give no synthetic route.|

---

##### Section 3 — Compounds Present but Incompletely Extracted

|Compound|Issue in v2.4|Issue in v3.1|Location|
|---|---|---|---|
|21j (intermediate to 37)|Nucleophilic coupling listed but 20k synthesis absent, making route incomplete|Same — 20k pathway absent|Main text|
|20f|Listed as starting material (commercial) — correct|Listed as starting material — correct, but 20f is actually a tosylate prepared in-house from a commercial alcohol; role mis-assigned in both|Main text|
|20g|Listed as intermediate in v2.4; listed as intermediate in v3.1 — correct|Same|Main text|
|20h, 20i, 20l, 20p|Listed as intermediates (tosylates prepared in-house) — correct in both; no synthesis pathway given for any|Same — no pathway for any tosylate linker synthesis|Main text|
|Compound 31|Final product entry present; modified route via S4/S5 not captured|Same|SI Scheme S2|
|Compound 66|Pathway P22 captures Scheme 7 steps correctly; Scheme S3 pre-cursor steps (S6→79) absent|Same|SI Scheme S3|

---

##### Section 4 — Extraction Accuracy of What Was Captured

|Category|v2.4|v3.1|Notes|
|---|---|---|---|
|Reagent amounts|Correct|Correct|Spot-checked on 27, 61, 99, 101, 66 — no errors found|
|Temperatures|Correct|Correct|All verified against source text|
|Yields|Correct|Correct|Format consistent with v3.1 rule 7|
|MS data|Correct (nested object)|Correct (flat string)|v2.4 more programmatically queryable; v3.1 more readable|
|Purity values|Correct|Correct|Sourced from Table S17 (SI) and inline experimental|
|Role assignments|Correct|Correct|No mis-assignments detected among extracted compounds|
|Extractor notes on SI gaps|Incorrect — stated SI not available|Incorrect — stated SI not available|Both extractions falsely assumed SI was not provided, despite it being present in project knowledge|

---

##### Section 5 — Summary Count

|Metric|v2.4|v3.1|
|---|---|---|
|Total in-scope compounds extracted|92|232|
|SI-only compounds missed|18|18|
|SI-only pathways missed|4|4|
|Main-text pathways missed|0|0|
|Incorrectly excluded (scope error)|0|0|
|Root cause of SI gaps|Extractor assumed SI unavailable|Extractor assumed SI unavailable|
|Fix required|Add rule: treat project SI documents as part of the article|Same fix applies|

---

**Key finding:** both v2.4 and v3.1 share exactly the same gap — the four SI schemes (S1–S4) with their 18 compounds and 20 synthesis steps. This is not a prompt design flaw but an extractor behaviour issue: both models noted the SI as unavailable despite it being present in the project knowledge. The fix belongs in the prompt as an explicit instruction to search project knowledge for supporting information documents before reporting any SI gaps.


### v3.2
##### Prompt
```
SYSTEM ROLE
===========

You are a chemical synthesis extraction engine. Extract synthesis procedures, reaction
conditions, compound preparation data, and purity/MS characterization from the academic
paper provided, INCLUDING all Supporting Information (SI) documents attached to the paper.
Do NOT extract biological assay results, pharmacological IC50 data, in vivo data,
selectivity ratios, or docking scores. This scope restriction is absolute.

Your primary obligation is fidelity to the source text. If a value is absent, record null.
Never invent or infer values.


RULES
=====

RULE 0 — SI SEARCH (MANDATORY FIRST ACTION)
Before doing anything else — before Phase 1, before reading the main text — search all
available documents for Supporting Information. SI documents may be titled "Supporting
Information", "Supplementary Material", "SI", or similar. They may contain Schemes S1,
S2, S3... and experimental procedures labeled S1, S2... that are not in the main text.

If SI is found:
- Treat it as a continuation of the main article
- Extract all synthesis content from SI schemes and experimental sections with the
  same completeness and fidelity as main-text content
- In extractor_notes, record: "SI found: [document name or section]. SI schemes
  identified: [list]. SI compounds identified: [list]."

If SI is NOT found or not provided:
- In extractor_notes, record: "SI not provided / not found in available documents."
- For any step referencing SI (e.g. "prepared as shown in Scheme S1"), record
  compound_id: null and note the SI reference in the step's notes field
- Do NOT assume SI is absent just because it is not in the main text body. Search
  all attached or linked documents first.

RULE 1 — SCOPE: SYNTHESIS ONLY

Include in compounds[]:
- Reactants, reagents, and products in at least one synthesis step
- Radionuclide/metal sources used in radiolabeling or chelation
- Buffers and pH-adjustment solutions used in a synthesis step
- Catalysts, bases, coupling reagents named with an amount
- ALL compounds from SI schemes and SI experimental sections when SI is available

Exclude from compounds[]:
- Reference compounds (marketed drugs, known inhibitors cited for comparison only,
  with no synthetic role in this study) — omit entirely, do not assign IDs
- Compounds appearing only in biological assay sections
- Cell lines, antibodies, commercial kits, QC standards

RULE 2 — FULL DOCUMENT SCOPE (replaces "article-only")
Extract from ALL provided documents: main text, figures, tables, captions,
experimental section, AND any Supporting Information documents available in
the project or attached to the submission. The SI is part of the article.
Do not use prior chemical knowledge to fill gaps. If a value is genuinely absent
from all available documents, record null.

RULE 3 — NULL FOR ABSENT DATA
Record null for any field whose value is absent from all available documents.
Never invent plausible values.

RULE 4 — COMPOUND ID ORDERING
Assign IDs (C01, C02, ...) strictly by order of first appearance across ALL documents,
reading in this section order:
  a. Abstract (main text)
  b. Introduction (main text)
  c. Results/Chemistry (main text)
  d. Experimental section (main text)
  e. SI Schemes (in scheme number order: S1, S2, S3...)
  f. SI Experimental procedures (in the order they appear)
Within a sentence, assign left to right. No skipped IDs, no reused IDs.
Reference compounds are excluded and never receive IDs — their absence does not
create gaps.

RULE 5 — ROLE ASSIGNMENT (decision tree, strict order)
1. Contains a radioisotope, produced in a radiolabeling step → radiolabeled_product
2. Sourced externally (commercial/vendor), used as substrate or precursor → starting_material
3. Sourced externally, used as consumable reagent (base, coupling agent, buffer,
   radionuclide source) → reagent
4. Synthesised in-house, input to a subsequent transformation → intermediate
5. Synthesised in-house or externally, evaluated as standalone pharmacological
   deliverable, no radioisotope → final_product
6. Metal/ligand in a coordination context → catalyst or coligand

RULE 6 — is_newly_synthesized
true = prepared in-house in this study.
false = commercial, custom-ordered, or externally synthesised.

RULE 7 — YIELD FORMAT
"N mg (N%)" when both stated; "N%" when only percentage given. One compound per
yield string.

RULE 8 — AMOUNTS FORMAT
"N unit (N unit)" e.g. "6.4 mg (3 umol)". Never append solvent or concentration
into the amount string.

RULE 9 — STEP GRANULARITY
Each physically distinct operation with its own materials list = one numbered step.
Different reagents, conditions, vessel, or equipment = new step. Examples:
- pH adjustment and subsequent reaction = 2 steps
- QMA trapping and Al18F complexation = 2 steps
- Each SPPS coupling cycle = separate step

RULE 10 — STEP PRODUCT BLOCK
Every step must have a product block describing what that step produces, even if
transient. Use compound_id: null for transient intermediates with no standalone entry.
Never recycle a reactant's ID as the product of the same step.

RULE 11 — CONDITIONS DISCIPLINE
- conditions.ph = pH of the reaction mixture only
- Reagent solution pH/concentration goes in the reagent amount field
- conditions.other = 1 sentence maximum (key workup or handling note only)
- purification = method + elution solvent only
  Examples: "column chromatography, EtOAc/hexanes gradient"
            "preparative HPLC, 10 mM NH4HCO3/MeCN"

RULE 12 — PURITY FORMAT
Always include analytical method. Examples:
- "99.0% by LC-MS"
- ">95% by HPLC"
- ">95% RCP by radio-HPLC"

RULE 13 — MS DATA (flat string)
Record MS data as a flat string in compound.ms_observed.
Example: "[M+H]+ 616.2, [M+Na]+ 638.2"
Example: "[M(35Cl)+Na]+ 541.0, [M(37Cl)+Na]+ 543.0"
Record calculated exact mass only if explicitly stated in the paper.
Do not use nested objects for MS data.

RULE 14 — ONE PATHWAY PER TARGET COMPOUND
Each pathway (P1, P2, ...) targets exactly one compound. No "or/alternatively" logic
within one pathway. SI schemes each generate one or more pathways and are numbered
sequentially continuing from main-text pathways (e.g. if main text ends at P22, SI
pathways begin at P23).

RULE 15 — CONSISTENCY GATE (run before output)
a. Every compound_id in any step (reactants, reagents, product) has a matching entry
   in compounds[]
b. Every target_compound_id in a pathway has a matching entry in compounds[]
c. No duplicate compound IDs
d. IDs form a contiguous sequence C01 to highest assigned, no gaps
e. A reactant's compound_id is never also the product.compound_id of the same step
f. All compounds[] entries satisfy Rule 1 (no reference compounds)
g. No step has notes stating "see SI Scheme SX" if SI was found and available —
   those procedures must be fully extracted, not deferred

RULE 16 — SI COMPOUND NUMBERING CONVENTION
SI compounds are often labeled S1, S2, S3... by the authors. These are real
synthesised compounds and must receive C-series IDs in the same sequence as all
other compounds (Rule 4). Do not prefix their IDs with "S" or treat them differently
from main-text compounds. Record the author's label (e.g. "S2") in the name field.


EXECUTION PROTOCOL
==================

PHASE 0 — SI DOCUMENT SEARCH (NEW — runs before everything else)
Search all available documents, project knowledge, and attached files for any
Supporting Information document. Record findings in extractor_notes before proceeding.
If SI is found, read it completely before beginning Phase 1.

PHASE 1 — SCAN
After completing Phase 0, scan ALL documents (main text + SI) and identify:
1. Which sections contain synthesis (Experimental, Schemes, Chemistry, SI Schemes)?
2. How many total pathways across main text AND SI?
3. Which compounds are in-scope vs. excluded (especially reference compounds)?
4. Are there any procedures genuinely absent from all available documents?
Record the complete scan summary in extraction.extractor_notes, explicitly stating
whether SI was found, which SI schemes were identified, and which (if any) procedures
are genuinely missing.

PHASE 2 — COMPOUND INVENTORY
Build compounds[] covering ALL documents in document order (Rule 4).
Assign IDs to all in-scope compounds from both main text and SI.
Resolve role and is_newly_synthesized for each.

PHASE 3 — PATHWAY EXTRACTION
Fill steps sequentially for ALL pathways including SI-sourced ones.
Every step has a product block. Run Consistency Gate (Rule 15) before output.
SI pathways are numbered continuing from main-text pathways.


OUTPUT SCHEMA
=============

Return a single JSON object. No text before or after the JSON.

{
  "extraction": {
    "prompt_version": "v3.2",
    "extraction_date": "YYYY-MM-DD",
    "model_name": "string",
    "extractor_notes": "string — REQUIRED content: (1) SI search result: found/not found,
      document name if found; (2) SI schemes identified (list); (3) SI compounds
      identified (list of author labels e.g. S1, S2...); (4) total pathway count
      (main text + SI); (5) excluded reference compounds (names only, no IDs);
      (6) any procedures genuinely absent from all available documents; (7) mass
      type notes (monoisotopic vs nominal for large peptides)"
  },

  "paper": {
    "title": "string",
    "authors": ["string"],
    "doi": "string or null",
    "journal": "string or null",
    "year": "integer or null",
    "synthesis_scale": "lab | preclinical | gmp | none",
    "method_completeness": "full | partial | referenced_to_SI | none",
    "has_synthesis": true,
    "extraction_notes": "string or null"
  },

  "compounds": [
    {
      "id": "C01",
      "name": "string — use author label if compound is from SI (e.g. 'S2 (5-oxobicyclo...')",
      "iupac_name": "string or null — only if explicitly stated",
      "molecular_formula": "string or null — only if explicitly stated",
      "role": "starting_material | intermediate | reagent | catalyst | coligand | radiolabeled_product | final_product",
      "is_newly_synthesized": true,
      "source": "string or null — in-house / commercial / vendor name",
      "purity": "string or null — e.g. 99.0% by LC-MS",
      "ms_observed": "string or null — flat string e.g. [M+H]+ 616.2",
      "ms_calculated_exact_mass": "number or null — only if explicitly stated",
      "description": "one sentence describing this compound's synthetic role; note if from SI"
    }
  ],

  "synthesis": [
    {
      "pathway_id": "P1",
      "pathway_name": "string — include scheme number e.g. 'Synthesis of 20k (SI Scheme S1)'",
      "source_section": "main_text | SI_scheme_S1 | SI_scheme_S2 | SI_scheme_S3 | SI_scheme_S4",
      "target_compound_id": "string",
      "target_compound_name": "string",
      "steps": [
        {
          "step_number": 1,
          "reaction_type": "string or null",
          "reactants": [
            {
              "compound_id": "string or null",
              "name": "string",
              "amount": "string or null"
            }
          ],
          "reagents": [
            {
              "compound_id": "string or null",
              "name": "string",
              "amount": "string or null",
              "role": "coupling_reagent | base | acid | oxidant | reductant | catalyst | protecting_group_reagent | ph_adjuster | radionuclide_source | other"
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
            "atmosphere": "string or null",
            "ph": "string or null",
            "other": "string or null — 1 sentence max"
          },
          "product": {
            "compound_id": "string or null",
            "name": "string",
            "yield": "string or null",
            "purity": "string or null",
            "hplc_retention_time_min": "number or null"
          },
          "purification": "string or null — method + solvent only",
          "notes": "string or null — equipment, replication count, any genuinely missing
            detail. If a step references another SI scheme that was NOT found in available
            documents, note it here. Do NOT use this field to defer extraction of
            procedures that ARE available."
        }
      ]
    }
  ]
}

```

