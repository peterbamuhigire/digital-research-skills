"""Multi-method outlier panel — univariate + multivariate + time-series.

Walker's discipline: outliers are not errors by default. Distinguish
*implausible* from *unusual*. The panel gives the analyst multiple
perspectives instead of a single threshold.

Methods:
- IQR (univariate, robust)
- Z-score (univariate, normality-assumption)
- Isolation Forest (multivariate, no distributional assumption)
- Cook's distance (regression-influence; opt-in)
- Period-over-period delta (time-series)
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal, Optional


OutlierMethod = Literal["iqr", "zscore", "isolation_forest", "cooks_distance", "period_delta"]


@dataclass(slots=True)
class OutlierReport:
    method: OutlierMethod
    n_total: int
    n_flagged: int
    flagged_indices: list[int]
    threshold_used: dict[str, float] = field(default_factory=dict)
    notes: str = ""


def detect_outliers_iqr(
    series: Any, *, multiplier: float = 1.5,
) -> OutlierReport:
    """Univariate IQR. Robust to non-normality. Walker's default."""
    import pandas as pd
    s = pd.Series(series).dropna()
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr = q3 - q1
    lo = q1 - multiplier * iqr
    hi = q3 + multiplier * iqr
    flagged = s[(s < lo) | (s > hi)].index.tolist()
    return OutlierReport(
        method="iqr",
        n_total=len(s),
        n_flagged=len(flagged),
        flagged_indices=[int(i) for i in flagged],
        threshold_used={"lo": float(lo), "hi": float(hi), "multiplier": multiplier},
        notes=f"IQR = {iqr:.3f}; flag if outside [{lo:.3f}, {hi:.3f}]",
    )


def detect_outliers_zscore(
    series: Any, *, threshold: float = 3.0,
) -> OutlierReport:
    """Univariate z-score. Assumes approximate normality."""
    import pandas as pd
    s = pd.Series(series).dropna()
    if s.std() == 0:
        return OutlierReport(method="zscore", n_total=len(s), n_flagged=0,
                             flagged_indices=[], notes="zero std — cannot compute z")
    z = (s - s.mean()) / s.std()
    flagged = s[z.abs() > threshold].index.tolist()
    return OutlierReport(
        method="zscore",
        n_total=len(s),
        n_flagged=len(flagged),
        flagged_indices=[int(i) for i in flagged],
        threshold_used={"abs_z": threshold},
        notes=f"z-threshold ±{threshold}; assumes normality (check skew/kurt first)",
    )


def detect_outliers_isolation_forest(
    df: Any, *, contamination: float = 0.05, random_state: int = 42,
) -> OutlierReport:
    """Multivariate. Lazy-imports sklearn."""
    from sklearn.ensemble import IsolationForest
    from sklearn.preprocessing import StandardScaler
    import pandas as pd
    import numpy as np

    numeric = df.select_dtypes(include="number").dropna()
    if numeric.empty:
        return OutlierReport(method="isolation_forest", n_total=0, n_flagged=0,
                             flagged_indices=[], notes="no numeric columns")

    X = StandardScaler().fit_transform(numeric)
    model = IsolationForest(contamination=contamination, random_state=random_state)
    pred = model.fit_predict(X)
    flagged_mask = pred == -1
    flagged = numeric.index[flagged_mask].tolist()
    return OutlierReport(
        method="isolation_forest",
        n_total=len(numeric),
        n_flagged=int(flagged_mask.sum()),
        flagged_indices=[int(i) for i in flagged],
        threshold_used={"contamination": contamination, "random_state": random_state},
        notes="multivariate; standardised features; IF score < 0 → outlier",
    )


def detect_outliers(
    df_or_series: Any, *,
    methods: list[OutlierMethod] = ["iqr"],
    column: Optional[str] = None,
    **kwargs,
) -> dict[OutlierMethod, OutlierReport]:
    """Run a panel of outlier methods.

    df_or_series: pass a DataFrame for multivariate methods (isolation_forest);
                   pass a Series (or DataFrame + column) for univariate.
    """
    import pandas as pd

    out: dict[OutlierMethod, OutlierReport] = {}

    # Resolve series for univariate methods
    if isinstance(df_or_series, pd.DataFrame) and column:
        series = df_or_series[column]
    elif isinstance(df_or_series, pd.Series):
        series = df_or_series
    else:
        series = None

    if "iqr" in methods and series is not None:
        out["iqr"] = detect_outliers_iqr(series, **{k: v for k, v in kwargs.items() if k in ("multiplier",)})
    if "zscore" in methods and series is not None:
        out["zscore"] = detect_outliers_zscore(series, **{k: v for k, v in kwargs.items() if k in ("threshold",)})
    if "isolation_forest" in methods and isinstance(df_or_series, pd.DataFrame):
        out["isolation_forest"] = detect_outliers_isolation_forest(
            df_or_series,
            **{k: v for k, v in kwargs.items() if k in ("contamination", "random_state")},
        )

    return out
