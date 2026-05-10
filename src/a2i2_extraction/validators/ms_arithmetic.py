"""MS arithmetic check: RDKit exact mass vs ms_calculated_exact_mass.

Tolerance is 0.01 Da (per architecture_v2.md §7.2 item i).
A mismatch is a WARNING, not an ERROR — sometimes papers report nominal mass
or include adduct/charge; we surface the discrepancy without rejecting.
"""

from __future__ import annotations

from typing import Any

from rdkit.Chem.Descriptors import ExactMolWt
from rdkit.Chem.rdmolfiles import MolFromSmiles

from .schema import Issue, Severity

_TOLERANCE_DA = 0.01


def _exact_mass_from_formula(formula: str) -> float | None:
    """Compute monoisotopic exact mass from a Hill-system formula string.

    RDKit doesn't have a direct formula→mass call, so we parse element counts
    and sum atomic monoisotopic masses from a small built-in table.
    """
    import re

    # Use the same monoisotopic masses RDKit uses internally.
    # Limited to elements common in medchem; extend as we hit gaps.
    monoisotopic = {
        "H": 1.007825,
        "C": 12.000000,
        "N": 14.003074,
        "O": 15.994915,
        "F": 18.998403,
        "P": 30.973762,
        "S": 31.972071,
        "Cl": 34.968853,
        "Br": 78.918337,
        "I": 126.904473,
        "Si": 27.976927,
        "B": 11.009305,
        "Na": 22.989770,
        "K": 38.963707,
        # Common radioisotopes encountered in tracer chemistry — note these
        # are monoisotopic for the LABELED isotope, not the natural-abundance one.
        # We treat "F" in formulas as natural F (18.998403); 18F vs 19F is a
        # name-level distinction the LLM should make in the compound name.
    }

    pattern = re.compile(r"([A-Z][a-z]?)(\d*)")
    total = 0.0
    pos = 0
    formula = formula.strip()
    while pos < len(formula):
        m = pattern.match(formula, pos)
        if not m or m.end() == pos:
            return None
        elem = m.group(1)
        count = int(m.group(2)) if m.group(2) else 1
        if elem not in monoisotopic:
            return None  # unknown element → can't compute, skip silently
        total += monoisotopic[elem] * count
        pos = m.end()
    return total


def check_ms_arithmetic(extraction: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    for c in extraction.get("compounds", []):
        formula = c.get("molecular_formula")
        reported = c.get("ms_calculated_exact_mass")
        if not formula or reported is None:
            continue
        computed = _exact_mass_from_formula(formula)
        if computed is None:
            continue  # element outside our table; not a hard fail
        if abs(computed - reported) > _TOLERANCE_DA:
            issues.append(
                Issue(
                    code="ms_arithmetic_mismatch",
                    severity=Severity.WARNING,
                    message=(
                        f"compound {c['id']}: formula {formula} → exact mass "
                        f"{computed:.4f}, but ms_calculated_exact_mass = {reported}"
                    ),
                    path=f"compounds/{c['id']}",
                )
            )
    return issues


def exact_mass_for_smiles(smiles: str) -> float | None:
    """Helper for downstream use (compound reference table validation)."""
    mol = MolFromSmiles(smiles)
    return ExactMolWt(mol) if mol is not None else None
