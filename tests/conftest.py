"""Shared fixtures.

`sample_extraction` returns a minimally valid v3.4 dict — tests mutate it to
exercise individual failure modes rather than re-building the whole shape.
"""

from __future__ import annotations

from copy import deepcopy

import pytest


@pytest.fixture
def sample_extraction() -> dict:
    return deepcopy(_SAMPLE)


_SAMPLE: dict = {
    "extraction": {
        "prompt_version": "v3.4",
        "extraction_date": "2026-05-03",
        "model_name": "test/dummy-1B",
        "extractor_notes": "test fixture",
    },
    "paper": {
        "title": "Synthetic study",
        "authors": ["A. Test"],
        "doi": None,
        "journal": None,
        "year": 2026,
        "synthesis_scale": "lab",
        "method_completeness": "full",
        "has_synthesis": True,
        "extraction_notes": None,
    },
    "compounds": [
        {
            "id": "C01",
            "name": "starting acid",
            "iupac_name": None,
            "molecular_formula": "C7H6O2",
            "role": "starting_material",
            "is_newly_synthesized": False,
            "source": "Sigma",
            "purity": None,
            "ms_observed": None,
            "ms_calculated_exact_mass": 122.0368,
            "description": "benzoic acid; commercial.",
        },
        {
            "id": "C02",
            "name": "amine",
            "iupac_name": None,
            "molecular_formula": "C6H7N",
            "role": "starting_material",
            "is_newly_synthesized": False,
            "source": "Sigma",
            "purity": None,
            "ms_observed": None,
            "ms_calculated_exact_mass": 93.0578,
            "description": "aniline; commercial.",
        },
        {
            "id": "C03",
            "name": "amide product",
            "iupac_name": None,
            "molecular_formula": "C13H11NO",
            "role": "final_product",
            "is_newly_synthesized": True,
            "source": None,
            "purity": "99.0% by HPLC",
            "ms_observed": "[M+H]+ 198.09",
            "ms_calculated_exact_mass": 197.0841,
            "description": "N-phenylbenzamide product.",
        },
    ],
    "synthesis": [
        {
            "pathway_id": "P1",
            "pathway_name": "amide product",
            "source_section": "main_text",
            "target_compound_id": "C03",
            "target_compound_name": "amide product",
            "steps": [
                {
                    "step_number": 1,
                    "reaction_type": "amide coupling",
                    "reactants": [
                        {"compound_id": "C01", "name": "benzoic acid", "amount": "100 mg"},
                        {"compound_id": "C02", "name": "aniline", "amount": "76 mg"},
                    ],
                    "reagents": [
                        {
                            "compound_id": None,
                            "name": "HATU",
                            "amount": "311 mg",
                            "role": "coupling_reagent",
                        },
                        {
                            "compound_id": None,
                            "name": "DIPEA",
                            "amount": "286 µL",
                            "role": "base",
                        },
                    ],
                    "solvents": [{"name": "DMF", "volume": "5 mL"}],
                    "conditions": {
                        "temperature": "rt",
                        "time": "12 h",
                        "atmosphere": "N2",
                        "ph": None,
                        "other": None,
                    },
                    "product": {
                        "compound_id": "C03",
                        "name": "N-phenylbenzamide",
                        "yield": "150 mg (93%)",
                        "purity": "99.0% by HPLC",
                        "hplc_retention_time_min": 8.4,
                    },
                    "purification": "silica column, hexane/EtOAc",
                    "notes": None,
                }
            ],
        }
    ],
}
