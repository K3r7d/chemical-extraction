"""Shared validator types + JSON Schema check.

Validators never raise — they return lists of `Issue`. Callers decide whether
to hard-fail. This keeps validation composable and lets us run all checks in
one pass for richer error reporting.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Any

from jsonschema import Draft202012Validator

from ..schema import SCHEMA_V3_4


class Severity(StrEnum):
    ERROR = "error"
    WARNING = "warning"


@dataclass(frozen=True)
class Issue:
    code: str
    severity: Severity
    message: str
    path: str = ""

    def __str__(self) -> str:
        loc = f" at {self.path}" if self.path else ""
        return f"[{self.severity.value}] {self.code}{loc}: {self.message}"


def check_schema(extraction: dict[str, Any]) -> list[Issue]:
    """Validate against v3.4 JSON Schema. Schema violations are always errors."""
    validator = Draft202012Validator(SCHEMA_V3_4)
    issues: list[Issue] = []
    for err in validator.iter_errors(extraction):
        path = "/".join(str(p) for p in err.absolute_path)
        issues.append(
            Issue(
                code="schema_violation",
                severity=Severity.ERROR,
                message=err.message,
                path=path,
            )
        )
    return issues


def validate_extraction(extraction: dict[str, Any]) -> list[Issue]:
    """Run all validators and return aggregated issues.

    Order matters: schema first (without valid shape, the others can't run safely).
    """
    issues = check_schema(extraction)
    if any(i.severity is Severity.ERROR for i in issues):
        return issues  # don't run downstream checks against malformed input

    # Late imports avoid a circular at module-load time.
    from .ms_arithmetic import check_ms_arithmetic
    from .rule_15 import check_rule_15

    issues.extend(check_rule_15(extraction))
    issues.extend(check_ms_arithmetic(extraction))
    return issues
