"""Wickham tidy-data violation detector.

Per Chen + Wickham:
  1. Each variable in a column
  2. Each observation in a row
  3. Each observational unit in a table

This linter detects three common violations and suggests the fix.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class TidyViolation:
    kind: str         # "columns_are_values" | "multiple_vars_per_column" | "vars_split_rows_cols"
    columns: list[str]
    suggested_fix: str
    severity: str = "warn"   # "warn" | "block"


def tidy_check(df: Any) -> list[TidyViolation]:
    """Return any tidy-data violations detected in the DataFrame."""
    violations: list[TidyViolation] = []

    cols = list(df.columns)

    # 1. Columns-are-values: many similarly-shaped column names
    #    e.g. "2018", "2019", "2020", "2021" or "Q1_sales", "Q2_sales", ...
    if len(cols) > 4:
        # Detect numeric-looking column names
        year_cols = [c for c in cols if isinstance(c, str) and c.isdigit() and 1900 < int(c) < 2100]
        if len(year_cols) >= 3:
            violations.append(TidyViolation(
                kind="columns_are_values",
                columns=year_cols,
                suggested_fix=(
                    f"{len(year_cols)} year-like columns. "
                    f"Run: df.melt(id_vars=[<keys>], value_vars={year_cols!r}, "
                    "var_name='year', value_name='value')"
                ),
            ))

        # Detect repeated prefix patterns: "Q1_sales", "Q2_sales", ...
        prefixes: dict[str, list[str]] = {}
        for c in cols:
            if isinstance(c, str) and "_" in c:
                head = c.split("_", 1)[0]
                prefixes.setdefault(head, []).append(c)
        for head, group in prefixes.items():
            if len(group) >= 3:
                violations.append(TidyViolation(
                    kind="columns_are_values",
                    columns=group,
                    suggested_fix=(
                        f"{len(group)} columns share prefix '{head}'. "
                        "Likely a category encoded in column names. "
                        f"Run: df.melt(id_vars=[<keys>], value_vars={group!r})"
                    ),
                ))

    # 2. Multiple variables per column: cell contains separator like "_" / "/"
    #    Inspect string columns
    import pandas as pd
    for col in cols:
        s = df[col]
        if str(s.dtype) != "object":
            continue
        sample = s.dropna().astype(str).head(50)
        if len(sample) < 5:
            continue
        # Heuristic: many cells have a single separator
        for sep in ("_", "/", ":", " - "):
            sep_count = sample.str.contains(sep, regex=False).mean()
            if sep_count > 0.7:
                violations.append(TidyViolation(
                    kind="multiple_vars_per_column",
                    columns=[col],
                    suggested_fix=(
                        f"Column '{col}' values look like 'a{sep}b' pairs ({sep_count:.0%} of cells). "
                        f"Run: df[['{col}_1', '{col}_2']] = df['{col}'].str.split('{sep}', n=1, expand=True)"
                    ),
                ))
                break

    # 3. Variables split across rows-and-columns:
    #    Heuristic — DataFrame has both wide structure AND a column that looks
    #    like it's selecting which "type" the row holds (e.g. element=tmin/tmax)
    type_like_cols = [c for c in cols if isinstance(c, str) and c.lower() in (
        "type", "kind", "variable", "var", "metric", "measure", "element"
    )]
    if type_like_cols:
        violations.append(TidyViolation(
            kind="vars_split_rows_cols",
            columns=type_like_cols + [c for c in cols if c not in type_like_cols],
            suggested_fix=(
                f"Column(s) {type_like_cols} look like pivot-encoded variable types. "
                f"Run: df.pivot_table(index=[<keys>], columns={type_like_cols[0]!r}, values=<value-col>)"
            ),
            severity="warn",
        ))

    return violations
