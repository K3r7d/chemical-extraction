# Reading and playing around the paper

### Manually reading

[7:56PM 11th March 2026]:
I start to do the project. First, Sherif told me to read paper by my-self, learn how a chemical synthesis paper work so that I can write a prompt for LLM to get the information that I want to get.

[8:50PM 11th March 2026]:
After skimming and scanning some papers in dataset, it seem that most of them are about batteries. 
After reading 2 papers, I can get some conclude about it:
- Paper 1:
	- Introduce about the theory hypothesis of the compound call $V_2CT_x$ and use experiment to claim it.
	- There are a lot of variant of $V_2CT_x$ 
	- One chemical reaction is regarded in paper: $V_2C + Al \rightarrow V_2AlC$.
- Paper 2
	- They develop new cathode  ($LiNi_{1-x-y}Mn_xAl_yO_2$ or NMA) to solve high cost and scarcity issues of cobalt in traditional batteries.
	- Now there is a shorten name for the compound is NMA, which the paper 1 do not have. I think I should remind this.
	- the Primary compound is NMA-89 ($LiNi_{0.883}Mn_{0.056}Al_{0.061}O_2$).
	- The rest of paper is hard to read so I cannot understand, but it just about domain knowledge. May be do not have anything else to notice.

[6:20PM 12th March 2026]:
Now I will go to the next step is design a prompt and test it with LLM. I'm gonna test it with some simple prompt, record the chat and then asking review for my result in tomorrow when I come to the office.

### Prompting

Now start with a naive prompt
```
Act as a expert chemist, your task is extracting important information in chemical synthesis paper. Please extract following papers.
```

Answer:

>[!Gemini 3 Thinking mode]
>As an expert chemist, I have extracted the key findings, synthesis parameters, and performance metrics from the provided research papers regarding advanced battery cathode materials.
> ## Paper 1: Two-Dimensional Vanadium Carbide (MXene) for Aluminum Batteries
>
>**Title:** Two-Dimensional Vanadium Carbide (MXene) as a High Capacity Cathode Material for Rechargeable Aluminum Batteries. **Authors:** Armin VahidMohammadi, et al..
> ### 1. Material & Theoretical Framework
>
>- **Active Material:** V2​C MXene, specifically investigated as V2​CTx​ (where T represents surface functional groups like F, O, or OH).
>- **Reaction Mechanism:** The cathode discharge involves the intercalation of Al into the MXene structure: V2​C+Al→V2​AlC.
>- **Theoretical Capacity:** Calculated at **705.263 mAh g⁻¹** for bare V2​C. Functionalized versions range from **529.39** (V2​CF2​) to **551.16 mAh g⁻¹** (V2​CO2​).
>### 2. Synthesis and Structure
>
>- **Preparation:** Multilayered (ML) V2​CTx​ was produced by etching the MAX phase.
>- **Delamination:** Few-layered (FL) V2​CTx​ was achieved through intercalation with **TBAOH** (tetrabutylammonium hydroxide) followed by delamination in NMP or water.
>- **Morphology:** Delamination in water yields primarily single and bi-layer flakes.
>### 3. Key Performance & Characterization
>
>- **Experimental Capacity:** ML-V2​CTx​ showed ~90 mAh g⁻¹ , whereas TBAOH-FL-V2​CTx​ reached significantly higher first-cycle capacities (~400 mAh g⁻¹).
>- **Aluminum Intercalation:** EDS and STEM mappings confirmed a clear increase in Al content upon discharge and a decrease after charge.
>- **Rate Capability:** Demonstrates fast charging and slow discharging capabilities.
>- **Water Content:** TGA showed that even after pre-drying at 180°C, about **2.42 wt.%** water remains in the MXene powder.
>
>
>## Paper 2: High-Nickel NMA (Cobalt-Free Cathode)
>
>**Title:** High-Nickel NMA: A Cobalt-Free Alternative to NMC and NCA Cathodes for Lithium-Ion Batteries. **Authors:** Wangda Li, Steven Lee, and Arumugam Manthiram.
>### 1. Material Design
>
>- **Composition:** LiNi1−x−y​Mnx​Aly​O2​ (**NMA**) with high nickel content (89 mol%).
>- **Objective:** To eliminate cobalt, which is expensive and has a vulnerable supply chain, while maintaining the performance of NMC and NCA cathodes .
>### 2. Synthesis Parameters
>
>- **Method:** Hydroxide coprecipitation followed by lithiation calcination.
>- **Calcination:** Performed at **750 ± 10°C** for **15 hours** under flowing oxygen.
>- **Structural Integrity:** Rietveld refinement showed Li/Ni mixing of **3.0%** for NMA-89, which is comparable to Co-bearing cathodes like NMC-89 (3.3%).
>### 3. Electrochemical & Thermal Properties
>
>- **Capacity:** Reaches a specific discharge capacity of **216 mAh g⁻¹** (at C/10, 2.8-4.4 V).
>- **Operating Voltage:** NMA operates at a voltage approximately **40 mV higher** than NMC.
>- **Long-term Stability:** In pouch cells, NMA-89 retained **82% capacity after 1000 deep cycles**, significantly outperforming NMC-89 (54%) and NCA-89 (62%).
>- **Thermal Stability:** DSC analysis showed NMA has a peak exothermic temperature of **238°C**, superior to NMC (222∘C) and NCA (237∘C) at identical Ni contents.
>

[6:36PM 12th March 2026]:
Now I come up with more tailored prompt with detailed JSON format to observe what will happen.
```
Act as a expert chemist and information extraction specialist. Your task is extracting important information in chemical synthesis paper. Your task is to extract chemical synthesis pathways from academic papers with high precision and structure them as valid JSON. Return a JSON object following this exact schema:

{
	"paper": 
	{
	    "title": "string",
	    "authors": ["string"],
	    "doi": "string or null",
	    "journal": "string or null",
	    "year": "integer or null"
	},
	"compounds": 
	[
	    {
			"name": "string",
		    "iupac_name": "string or null",
		    "description": "string"
	    }
	],
	"synthesis": 
	[
		{
		    "pathway_id": "string",
		    "target_compound": "string",
			"reactants":
			[
				{
					"name": "string",
					"amount": "string or null"
				}
			],
			"reagents": 
			[
				{
					"name": "string",
					"amount": "string or null"
				}
			],
			"solvents": 
			[
				{
					"name": "string",
					"amount": "string or null"
				}
			],
			"product": "string"
		}
	]
}
```

I think I need some help from ChatGPT to get a better JSON because I just use my general chemistry knowledge to write this prompt. 

After a while, I get the final prompt:
```
Act as a expert chemist and information extraction specialist. Your task is extracting important information in chemical synthesis paper. Your task is to extract chemical synthesis pathways from academic papers with high precision and structure them as valid JSON. Return a JSON object following this exact schema:

{
	"paper": 
	{
	    "title": "string",
	    "authors": ["string"],
	    "doi": "string or null",
	    "journal": "string or null",
	    "year": "integer or null"
	},
	"compounds": 
	[
	    {
			"name": "string",
		    "iupac_name": "string or null",
		    "description": "short description of the compound role (e.g., starting material, intermediate, catalyst, product)"
	    }
	],

	"synthesis": 
	[
		{
		    "pathway_id": "string",
		    "target_compound": "string",
		    "steps": 
		    [
		        {
			        "step_number": "integer",
			        "reactants":
			        [
			            {
					        "name": "string",
				            "amount": "string or null"
			            }
			        ],
			        "reagents": 
			        [
				        {
				            "name": "string",
					        "amount": "string or null"
			            }
			        ],
			        "solvents": 
			        [
			            {
					        "name": "string",
				            "volume": "string or null"
			            }
					],
			        "conditions": 
			        {
			            "temperature": "string or null",
			            "time": "string or null",
			            "pressure": "string or null",
			            "atmosphere": "string or null",
			            "other": "string or null"
			        },
					"product": 
					{
			            "name": "string",
			            "yield": "string or null"
			        },
			        "notes": "string or null"
			    }
		    ]
		}
	]
}
```

Now let test it with Gemini Thinking mode one more time.

Paper 1
```
{
  "paper": {
    "title": "Two-Dimensional Vanadium Carbide (MXene) as a High Capacity Cathode Material for Rechargeable Aluminum Batteries",
    "authors": [
      "Armin VahidMohammadi",
      "Ali Hadjikhani",
      "Sina Shahbazmohamadi",
      "Majid Beidaghi"
    ],
    "doi": null,
    "journal": "ACS Nano",
    "year": 2026
  },
  "compounds": [
    {
      "name": "V2AlC",
      "iupac_name": null,
      "description": "Parent MAX phase starting material"
    },
    {
      "name": "V2CTx",
      "iupac_name": null,
      "description": "Multilayered (ML) MXene product and electrode active material"
    },
    {
      "name": "TBAOH",
      "iupac_name": "tetrabutylammonium hydroxide",
      "description": "Intercalating agent used for delamination"
    },
    {
      "name": "TBAOH-FL-V2CTx",
      "iupac_name": null,
      "description": "Few-layered (FL) or delaminated MXene product"
    },
    {
      "name": "NMP",
      "iupac_name": "N-Methyl-2-pyrrolidone",
      "description": "Solvent used for delamination"
    },
    {
      "name": "Aluminum",
      "iupac_name": null,
      "description": "Anode and current collector material"
    }
  ],
  "synthesis": [
    {
      "pathway_id": "V2CTx_Synthesis_and_Delamination",
      "target_compound": "TBAOH-FL-V2CTx",
      "steps": [
        {
          "step_number": 1,
          "reactants": [
            {
              "name": "V2AlC",
              "amount": null
            }
          ],
          "reagents": [
            {
              "name": "Etchant (HF based - implied)",
              "amount": null
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "other": "Etching process to remove Al from MAX phase"
          },
          "product": {
            "name": "ML-V2CTx",
            "yield": null
          },
          "notes": "Multilayered vanadium carbide MXene is formed after etching. Some residual Al may remain in unreacted MAX particles[cite: 66]."
        },
        {
          "step_number": 2,
          "reactants": [
            {
              "name": "ML-V2CTx",
              "amount": null
            }
          ],
          "reagents": [
            {
              "name": "TBAOH",
              "amount": null
            }
          ],
          "solvents": [],
          "conditions": {
            "temperature": null,
            "time": "4 h",
            "pressure": null,
            "atmosphere": null,
            "other": "Intercalation"
          },
          "product": {
            "name": "TBAOH-intercalated V2CTx",
            "yield": null
          },
          "notes": "Intercalation increases the c-lattice parameter as shown by XRD[cite: 347]."
        },
        {
          "step_number": 3,
          "reactants": [
            {
              "name": "TBAOH-intercalated V2CTx",
              "amount": null
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "NMP",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "other": "High speed stirring"
          },
          "product": {
            "name": "TBAOH-FL-V2CTx (in NMP)",
            "yield": null
          },
          "notes": "Results in bi- or few-layered flakes[cite: 90]."
        },
        {
          "step_number": 4,
          "reactants": [
            {
              "name": "TBAOH-intercalated V2CTx",
              "amount": null
            }
          ],
          "reagents": [],
          "solvents": [
            {
              "name": "Water",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": null,
            "time": null,
            "pressure": null,
            "atmosphere": null,
            "other": "Direct delamination"
          },
          "product": {
            "name": "TBAOH-FL-V2CTx (in Water)",
            "yield": null
          },
          "notes": "Results in single and bi-layer flakes[cite: 90]. Used to produce freestanding paper via vacuum filtration[cite: 334]."
        }
      ]
    }
  ]
}
```

Paper 2
```
{
  "paper": {
    "title": "High-Nickel NMA: A Cobalt-Free Alternative to NMC and NCA Cathodes for Lithium-Ion Batteries",
    "authors": [
      "Wangda Li",
      "Steven Lee",
      "Arumugam Manthiram"
    ],
    "doi": "10.1002/adma.202002718",
    "journal": "Advanced Materials",
    "year": 2020
  },
  "compounds": [
    {
      "name": "NiSO4·6H2O",
      "iupac_name": "Nickel(II) sulfate hexahydrate",
      "description": "Starting material for the hydroxide precursor."
    },
    {
      "name": "MnSO4·H2O",
      "iupac_name": "Manganese(II) sulfate monohydrate",
      "description": "Starting material for the hydroxide precursor."
    },
    {
      "name": "Al(NO3)3·9H2O",
      "iupac_name": "Aluminum nitrate nonahydrate",
      "description": "Starting material for the hydroxide precursor."
    },
    {
      "name": "KOH",
      "iupac_name": "Potassium hydroxide",
      "description": "Precipitating reagent used to maintain pH."
    },
    {
      "name": "Ammonium hydroxide",
      "iupac_name": "Azane;hydrate",
      "description": "Chelating agent used during coprecipitation."
    },
    {
      "name": "LiOH·H2O",
      "iupac_name": "Lithium hydroxide monohydrate",
      "description": "Lithium source for the final calcination step."
    },
    {
      "name": "Ni0.883Mn0.056Al0.061(OH)2",
      "iupac_name": null,
      "description": "Mixed-metal hydroxide precursor intermediate."
    },
    {
      "name": "NMA-89",
      "iupac_name": "Lithium Nickel Manganese Aluminum Oxide (LiNi0.883Mn0.056Al0.061O2)",
      "description": "Final cobalt-free cathode product."
    }
  ],
  "synthesis": [
    {
      "pathway_id": "NMA_89_Synthesis",
      "target_compound": "NMA-89",
      "steps": [
        {
          "step_number": 1,
          "reactants": [
            {
              "name": "NiSO4·6H2O",
              "amount": "molar ratio 0.883"
            },
            {
              "name": "MnSO4·H2O",
              "amount": "molar ratio 0.056"
            },
            {
              "name": "Al(NO3)3·9H2O",
              "amount": "molar ratio 0.061"
            }
          ],
          "reagents": [
            {
              "name": "KOH",
              "amount": "to maintain pH 11.25"
            },
            {
              "name": "Ammonium hydroxide",
              "amount": null
            }
          ],
          "solvents": [
            {
              "name": "Deionized water",
              "volume": null
            }
          ],
          "conditions": {
            "temperature": "50 °C",
            "time": null,
            "pressure": "Ambient",
            "atmosphere": "Nitrogen",
            "other": "pH controlled at 11.25 ± 0.25 in a 10 L tank reactor"
          },
          "product": {
            "name": "Ni0.883Mn0.056Al0.061(OH)2",
            "yield": null
          },
          "notes": "Hydroxide coprecipitation process followed by washing, filtering, and drying."
        },
        {
          "step_number": 2,
          "reactants": [
            {
              "name": "Ni0.883Mn0.056Al0.061(OH)2",
              "amount": "1 molar part"
            },
            {
              "name": "LiOH·H2O",
              "amount": "1.01 molar ratio"
            }
          ],
          "reagents": [],
          "solvents": [],
          "conditions": {
            "temperature": "750 ± 10 °C",
            "time": "15 h",
            "pressure": "Ambient",
            "atmosphere": "Flowing oxygen",
            "other": "Solid-state calcination"
          },
          "product": {
            "name": "NMA-89",
            "yield": null
          },
          "notes": "The precursor and LiOH were mixed based on TGA weight-loss results prior to lithiation calcination."
        }
      ]
    }
  ]
}
```

We can get some observation from these two 'naive' and 'tailor' version of prompt:
- Neither answer shows significant hallucinations. Both models correctly mapped data points to the respective papers.
- The JSON format is superior for **technical extraction**. It can capture small detail of engineering part in paper that missed from naive prompt.


