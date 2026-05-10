"""JSON Schema (draft 2020-12) for v3.4 extraction output.

Mirrors the OUTPUT SCHEMA block in docs/prompts/Prompt versions.md (v3.4).
Hard-fail on any structural deviation.
"""

ROLE_ENUM = [
    "starting_material",
    "intermediate",
    "reagent",
    "catalyst",
    "coligand",
    "radiolabeled_product",
    "final_product",
]

REAGENT_ROLE_ENUM = [
    "coupling_reagent",
    "base",
    "acid",
    "oxidant",
    "reductant",
    "catalyst",
    "protecting_group_reagent",
    "ph_adjuster",
    "radionuclide_source",
    "other",
]

SCHEMA_V3_4: dict = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "v3.4 chemical synthesis extraction",
    "type": "object",
    "required": ["extraction", "paper", "compounds", "synthesis"],
    "additionalProperties": False,
    "properties": {
        "extraction": {
            "type": "object",
            "required": ["prompt_version", "extraction_date", "model_name", "extractor_notes"],
            "additionalProperties": False,
            "properties": {
                "prompt_version": {"type": "string"},
                "extraction_date": {"type": "string", "pattern": r"^\d{4}-\d{2}-\d{2}$"},
                "model_name": {"type": "string"},
                "extractor_notes": {"type": "string"},
            },
        },
        "paper": {
            "type": "object",
            "required": [
                "title",
                "authors",
                "doi",
                "journal",
                "year",
                "synthesis_scale",
                "method_completeness",
                "has_synthesis",
                "extraction_notes",
            ],
            "additionalProperties": False,
            "properties": {
                "title": {"type": "string"},
                "authors": {"type": "array", "items": {"type": "string"}},
                "doi": {"type": ["string", "null"]},
                "journal": {"type": ["string", "null"]},
                "year": {"type": ["integer", "null"]},
                "synthesis_scale": {"enum": ["lab", "preclinical", "gmp", "none"]},
                "method_completeness": {
                    "enum": ["full", "partial", "referenced_to_SI", "none"]
                },
                "has_synthesis": {"type": "boolean"},
                "extraction_notes": {"type": ["string", "null"]},
            },
        },
        "compounds": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "id",
                    "name",
                    "iupac_name",
                    "molecular_formula",
                    "role",
                    "is_newly_synthesized",
                    "source",
                    "purity",
                    "ms_observed",
                    "ms_calculated_exact_mass",
                    "description",
                ],
                "additionalProperties": False,
                "properties": {
                    "id": {"type": "string", "pattern": r"^C\d{2,}$"},
                    "name": {"type": "string"},
                    "iupac_name": {"type": ["string", "null"]},
                    "molecular_formula": {"type": ["string", "null"]},
                    "role": {"enum": ROLE_ENUM},
                    "is_newly_synthesized": {"type": "boolean"},
                    "source": {"type": ["string", "null"]},
                    "purity": {"type": ["string", "null"]},
                    "ms_observed": {"type": ["string", "null"]},
                    "ms_calculated_exact_mass": {"type": ["number", "null"]},
                    "description": {"type": "string"},
                },
            },
        },
        "synthesis": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "pathway_id",
                    "pathway_name",
                    "source_section",
                    "target_compound_id",
                    "target_compound_name",
                    "steps",
                ],
                "additionalProperties": False,
                "properties": {
                    "pathway_id": {"type": "string", "pattern": r"^P\d+$"},
                    "pathway_name": {"type": "string"},
                    "source_section": {"type": "string"},
                    "target_compound_id": {"type": "string"},
                    "target_compound_name": {"type": "string"},
                    "steps": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": [
                                "step_number",
                                "reaction_type",
                                "reactants",
                                "reagents",
                                "solvents",
                                "conditions",
                                "product",
                                "purification",
                                "notes",
                            ],
                            "additionalProperties": False,
                            "properties": {
                                "step_number": {"type": "integer", "minimum": 1},
                                "reaction_type": {"type": ["string", "null"]},
                                "reactants": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "required": ["compound_id", "name", "amount"],
                                        "additionalProperties": False,
                                        "properties": {
                                            "compound_id": {"type": ["string", "null"]},
                                            "name": {"type": "string"},
                                            "amount": {"type": ["string", "null"]},
                                        },
                                    },
                                },
                                "reagents": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "required": [
                                            "compound_id",
                                            "name",
                                            "amount",
                                            "role",
                                        ],
                                        "additionalProperties": False,
                                        "properties": {
                                            "compound_id": {"type": ["string", "null"]},
                                            "name": {"type": "string"},
                                            "amount": {"type": ["string", "null"]},
                                            "role": {"enum": REAGENT_ROLE_ENUM},
                                        },
                                    },
                                },
                                "solvents": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "required": ["name", "volume"],
                                        "additionalProperties": False,
                                        "properties": {
                                            "name": {"type": "string"},
                                            "volume": {"type": ["string", "null"]},
                                        },
                                    },
                                },
                                "conditions": {
                                    "type": "object",
                                    "required": [
                                        "temperature",
                                        "time",
                                        "atmosphere",
                                        "ph",
                                        "other",
                                    ],
                                    "additionalProperties": False,
                                    "properties": {
                                        "temperature": {"type": ["string", "null"]},
                                        "time": {"type": ["string", "null"]},
                                        "atmosphere": {"type": ["string", "null"]},
                                        "ph": {"type": ["string", "null"]},
                                        "other": {"type": ["string", "null"]},
                                    },
                                },
                                "product": {
                                    "type": "object",
                                    "required": [
                                        "compound_id",
                                        "name",
                                        "yield",
                                        "purity",
                                        "hplc_retention_time_min",
                                    ],
                                    "additionalProperties": False,
                                    "properties": {
                                        "compound_id": {"type": ["string", "null"]},
                                        "name": {"type": "string"},
                                        "yield": {"type": ["string", "null"]},
                                        "purity": {"type": ["string", "null"]},
                                        "hplc_retention_time_min": {
                                            "type": ["number", "null"]
                                        },
                                    },
                                },
                                "purification": {"type": ["string", "null"]},
                                "notes": {"type": ["string", "null"]},
                            },
                        },
                    },
                },
            },
        },
    },
}
