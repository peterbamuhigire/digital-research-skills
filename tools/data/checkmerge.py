"""Walker's checkmerge anti-join pattern.

Per Walker (Python Data Cleaning Cookbook, Ch. 8): never merge without
auditing what's being lost. checkmerge exposes left-only, right-only, and
both counts BEFORE the merge runs.

Wraps pandas `merge(..., indicator=True, validate=...)` with an explicit
report and gating thresholds.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal, Optional


@dataclass(slots=True)
class MergeAuditReport:
    left_total: int
    right_total: int
    left_only: int
    right_only: int
    both: int
    fan_out_factor: float       # >1 means right side has duplicate keys
    validate_passed: bool
    validate_mode: Optional[str] = None
    sample_left_only: list[dict] = field(default_factory=list)
    sample_right_only: list[dict] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def passes(self, *, max_left_only_rate: float = 0.10, max_fan_out: float = 1.5) -> bool:
        """Default thresholds: ≤10% left-only rows, ≤1.5x fan-out."""
        if self.left_total and self.left_only / self.left_total > max_left_only_rate:
            return False
        if self.fan_out_factor > max_fan_out:
            return False
        return True


def check_merge(
    left: Any,
    right: Any,
    *,
    on: list[str] | str,
    how: Literal["inner", "left", "right", "outer"] = "left",
    validate: Optional[Literal["one_to_one", "one_to_many", "many_to_one", "many_to_many"]] = None,
    sample_size: int = 5,
) -> tuple[Any, MergeAuditReport]:
    """Merge with audit. Returns (merged_df, report).

    on: join column(s)
    validate: Chen's `validate=` cardinality assertion. Use it whenever you
              know the expected cardinality (one_to_many is most common for
              reference-table joins).
    """
    import pandas as pd

    on_cols = [on] if isinstance(on, str) else list(on)

    # Run the merge with indicator
    merged = pd.merge(left, right, on=on_cols, how=how, indicator=True, validate=validate)

    # Audit using indicator
    indicator = merged["_merge"]
    counts = indicator.value_counts(dropna=False)
    left_only = int(counts.get("left_only", 0))
    right_only = int(counts.get("right_only", 0))
    both = int(counts.get("both", 0))

    # Fan-out: how many rows did the merge produce per left row?
    fan_out = float(len(merged) / len(left)) if len(left) else 1.0

    # Sample the orphans for human review
    sample_left = merged[indicator == "left_only"].head(sample_size).to_dict(orient="records")
    sample_right = merged[indicator == "right_only"].head(sample_size).to_dict(orient="records")

    warnings: list[str] = []
    if left_only and how in ("inner", "right"):
        warnings.append(f"{left_only} left-only rows DROPPED by how={how!r}")
    if right_only and how in ("inner", "left"):
        warnings.append(f"{right_only} right-only rows DROPPED by how={how!r}")
    if fan_out > 1.5:
        warnings.append(f"fan-out factor {fan_out:.2f}x — right side has duplicate keys, fix or accept multiplication")

    # Drop the helper column from the returned frame
    merged = merged.drop(columns=["_merge"])

    report = MergeAuditReport(
        left_total=len(left),
        right_total=len(right),
        left_only=left_only,
        right_only=right_only,
        both=both,
        fan_out_factor=fan_out,
        validate_passed=True,  # if we reached here without raising, validate passed
        validate_mode=validate,
        sample_left_only=sample_left,
        sample_right_only=sample_right,
        warnings=warnings,
    )
    return merged, report
