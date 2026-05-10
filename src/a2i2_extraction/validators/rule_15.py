"""Rule 15 consistency gate (a-g) from v3.4 prompt.

Runs as programmatic checks rather than as LLM self-check.
"""

from __future__ import annotations

import re
from typing import Any

from .schema import Issue, Severity

_C_ID = re.compile(r"^C(\d+)$")


def _collect_referenced_ids(extraction: dict[str, Any]) -> set[str]:
    refs: set[str] = set()
    for pathway in extraction.get("synthesis", []):
        if tid := pathway.get("target_compound_id"):
            refs.add(tid)
        for step in pathway.get("steps", []):
            for entry in (
                *step.get("reactants", []),
                *step.get("reagents", []),
                step.get("product", {}),
            ):
                if cid := entry.get("compound_id"):
                    refs.add(cid)
    return refs


def check_rule_15(extraction: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    compounds = extraction.get("compounds", [])
    declared_ids = [c["id"] for c in compounds]
    declared_set = set(declared_ids)

    # (a) every referenced compound_id has a compounds[] entry
    referenced = _collect_referenced_ids(extraction)
    for ref in sorted(referenced):
        if ref not in declared_set:
            issues.append(
                Issue(
                    code="rule15_a_dangling_reference",
                    severity=Severity.ERROR,
                    message=f"compound_id '{ref}' referenced but not in compounds[]",
                )
            )

    # (b) every target_compound_id has a compounds[] entry — covered by (a)
    # but we still want a distinct code for clearer reporting.
    for pathway in extraction.get("synthesis", []):
        tid = pathway.get("target_compound_id")
        if tid and tid not in declared_set:
            issues.append(
                Issue(
                    code="rule15_b_target_missing",
                    severity=Severity.ERROR,
                    message=f"pathway {pathway.get('pathway_id')} targets undeclared {tid}",
                )
            )

    # (c) no duplicate IDs; IDs contiguous from C01
    seen: set[str] = set()
    duplicates = [cid for cid in declared_ids if cid in seen or seen.add(cid)]  # type: ignore[func-returns-value]
    for cid in duplicates:
        issues.append(
            Issue(
                code="rule15_c_duplicate_id",
                severity=Severity.ERROR,
                message=f"duplicate compound id {cid}",
            )
        )
    nums = sorted(int(m.group(1)) for cid in declared_ids if (m := _C_ID.match(cid)))
    if nums and nums != list(range(1, len(nums) + 1)):
        issues.append(
            Issue(
                code="rule15_c_noncontiguous_ids",
                severity=Severity.ERROR,
                message=f"compound IDs not contiguous from C01: got {nums}",
            )
        )

    # (d) reactant is never also the product of the same step
    for pathway in extraction.get("synthesis", []):
        for step in pathway.get("steps", []):
            product_id = (step.get("product") or {}).get("compound_id")
            if not product_id:
                continue
            for r in step.get("reactants", []):
                if r.get("compound_id") == product_id:
                    issues.append(
                        Issue(
                            code="rule15_d_reactant_is_product",
                            severity=Severity.ERROR,
                            message=(
                                f"step {step.get('step_number')} of "
                                f"{pathway.get('pathway_id')}: reactant {product_id} "
                                "is also the product"
                            ),
                        )
                    )

    # (e) no step defers to an SI scheme that IS available — requires knowledge
    # of which SI schemes were actually parsed, so we only flag the surface
    # pattern (a step with no reagents/products + a deferral note).
    for pathway in extraction.get("synthesis", []):
        for step in pathway.get("steps", []):
            note = (step.get("notes") or "").lower()
            if "see si" in note and step.get("reagents") and step.get("product"):
                issues.append(
                    Issue(
                        code="rule15_e_si_deferral_with_data",
                        severity=Severity.WARNING,
                        message=(
                            f"step {step.get('step_number')} of "
                            f"{pathway.get('pathway_id')} both defers to SI and "
                            "carries data — consolidate or remove the deferral"
                        ),
                    )
                )

    # (f) final_product purity is null or from explicit individual measurement —
    # we can only check structural shape: if role=final_product and purity has
    # a value, it must contain an analytical method per Rule 12.
    method_re = re.compile(r"\b(LC-?MS|HPLC|RCP|GC|NMR)\b", re.IGNORECASE)
    for c in compounds:
        if (
            c["role"] == "final_product"
            and c.get("purity")
            and not method_re.search(c["purity"])
        ):
            issues.append(
                Issue(
                    code="rule15_f_purity_missing_method",
                    severity=Severity.WARNING,
                    message=(
                        f"final_product {c['id']} purity '{c['purity']}' "
                        "does not name an analytical method (Rule 12)"
                    ),
                )
            )

    # (g) no SPPS pathway contains more than one iterative-coupling step (Rule 9A)
    for pathway in extraction.get("synthesis", []):
        spps_count = sum(
            1
            for s in pathway.get("steps", [])
            if "iterative" in (s.get("reaction_type") or "").lower()
            and "sppr" not in (s.get("reaction_type") or "").lower()
        )
        if spps_count > 1:
            issues.append(
                Issue(
                    code="rule15_g_multiple_iterative_couplings",
                    severity=Severity.ERROR,
                    message=(
                        f"pathway {pathway.get('pathway_id')} has {spps_count} "
                        "iterative-coupling steps; Rule 9A allows at most one"
                    ),
                )
            )

    return issues
