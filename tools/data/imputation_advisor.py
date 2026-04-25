"""Imputation method advisor.

Walker: imputation method depends on (1) missingness rate, (2) missingness
mechanism (MCAR / MAR / MNAR), (3) correlation with other columns, (4)
temporal ordering presence.

This advisor recommends a method without committing to it — caller decides.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal, Optional


ImputationMethod = Literal[
    "drop", "scalar", "mean", "median", "mode", "group_mean",
    "ffill", "bfill", "interpolate", "knn", "iterative",
]


@dataclass(slots=True)
class ImputationAdvice:
    column: str
    null_rate: float
    recommended_method: ImputationMethod
    rationale: str
    alternatives: list[ImputationMethod]


def advise_imputation(
    df: Any, column: str, *,
    has_temporal_index: bool = False,
    correlated_columns: Optional[list[str]] = None,
    drop_threshold: float = 0.50,
    knn_min_correlation: float = 0.3,
) -> ImputationAdvice:
    """Recommend an imputation method for a column.

    has_temporal_index: True if rows are time-ordered → ffill/interpolate viable.
    correlated_columns: list of cols with strong correlation → KNN/iterative viable.
    """
    import pandas as pd

    s = df[column]
    n = len(s)
    null_rate = float(s.isna().sum() / n) if n else 0.0

    # Decision tree
    if null_rate >= drop_threshold:
        return ImputationAdvice(
            column=column,
            null_rate=null_rate,
            recommended_method="drop",
            rationale=f"{null_rate:.0%} null — too sparse to impute reliably; drop column or rows",
            alternatives=[],
        )

    if null_rate == 0:
        return ImputationAdvice(
            column=column,
            null_rate=0.0,
            recommended_method="scalar",
            rationale="no nulls — no imputation needed",
            alternatives=[],
        )

    # Time-series first
    if has_temporal_index:
        if pd.api.types.is_numeric_dtype(s):
            return ImputationAdvice(
                column=column, null_rate=null_rate,
                recommended_method="interpolate",
                rationale="numeric + temporal index — linear interpolation most accurate",
                alternatives=["ffill", "bfill", "knn"],
            )
        return ImputationAdvice(
            column=column, null_rate=null_rate,
            recommended_method="ffill",
            rationale="categorical + temporal index — forward-fill from prior valid value",
            alternatives=["bfill", "mode"],
        )

    # KNN / iterative when correlations exist
    if correlated_columns and len(correlated_columns) >= 2:
        return ImputationAdvice(
            column=column, null_rate=null_rate,
            recommended_method="knn",
            rationale=(
                f"correlated with {len(correlated_columns)} other columns "
                f"(threshold {knn_min_correlation}) — KNN imputation preserves multivariate structure"
            ),
            alternatives=["iterative", "group_mean", "median"],
        )

    # Numeric with skew → median, otherwise mean
    if pd.api.types.is_numeric_dtype(s):
        try:
            skew = abs(float(s.skew()))
            if skew > 1.0:
                return ImputationAdvice(
                    column=column, null_rate=null_rate,
                    recommended_method="median",
                    rationale=f"numeric with skew={skew:.2f} (>1) — median robust to outliers",
                    alternatives=["mean", "knn"],
                )
        except Exception:
            pass
        return ImputationAdvice(
            column=column, null_rate=null_rate,
            recommended_method="mean",
            rationale="numeric, approximately symmetric — mean acceptable",
            alternatives=["median", "knn"],
        )

    # Categorical
    return ImputationAdvice(
        column=column, null_rate=null_rate,
        recommended_method="mode",
        rationale="categorical — mode (most frequent value) is the standard",
        alternatives=["scalar", "drop"],
    )
