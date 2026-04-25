"""Lightweight DataFrame profiler.

Combines Walker's custom probes (gettots / getmissings / makefreqs / getcnts /
getdistprops) into a single artefact. Emits both a Python object and a JSON
file for embedding in research outputs.

Heavier alternatives (ydata-profiling, sweetviz, D-Tale) are great for
exploration; this is the engine's lean operational profile that sits next to
every cached dataset.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Optional


@dataclass(slots=True)
class ColumnProfile:
    name: str
    dtype: str
    n_total: int
    n_null: int
    null_rate: float
    n_unique: int
    sample_values: list[Any]
    # Numeric only
    min_val: Any = None
    max_val: Any = None
    mean_val: Optional[float] = None
    std_val: Optional[float] = None
    skew_val: Optional[float] = None
    kurt_val: Optional[float] = None
    # Top frequencies
    top_values: list[tuple[Any, int]] = field(default_factory=list)
    # Suspected anomalies / hints
    hints: list[str] = field(default_factory=list)


@dataclass(slots=True)
class ProfileReport:
    source_path: str
    n_rows: int
    n_columns: int
    duplicate_rows: int
    column_drift: list[str]  # columns whose name suggests drift across versions
    columns: list[ColumnProfile] = field(default_factory=list)
    quality_flags: list[str] = field(default_factory=list)

    def to_json(self, path: str | Path) -> Path:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        # asdict + json (with default=str for non-serialisable scalars)
        path.write_text(json.dumps(asdict(self), indent=2, default=str), encoding="utf-8")
        return path


def profile_dataframe(
    df: Any, *,
    source_path: str = "<in-memory>",
    sample_per_column: int = 5,
    top_values_per_column: int = 5,
    null_rate_warn: float = 0.30,
    high_cardinality_threshold: float = 0.95,  # n_unique / n_total
) -> ProfileReport:
    """Produce a profile report for a pandas DataFrame.

    Walker's discipline + Chen's hint patterns combined.
    """
    import pandas as pd

    columns: list[ColumnProfile] = []
    quality_flags: list[str] = []
    n_rows = len(df)

    for col in df.columns:
        s = df[col]
        n_null = int(s.isna().sum())
        null_rate = n_null / n_rows if n_rows else 0.0
        n_unique = int(s.nunique(dropna=True))

        cp = ColumnProfile(
            name=str(col),
            dtype=str(s.dtype),
            n_total=n_rows,
            n_null=n_null,
            null_rate=null_rate,
            n_unique=n_unique,
            sample_values=[_safe(v) for v in s.dropna().head(sample_per_column).tolist()],
        )

        # Numeric stats
        if pd.api.types.is_numeric_dtype(s) and n_unique > 0:
            cp.min_val = _safe(s.min())
            cp.max_val = _safe(s.max())
            cp.mean_val = float(s.mean()) if n_null < n_rows else None
            cp.std_val = float(s.std()) if n_null < n_rows else None
            try:
                cp.skew_val = float(s.skew())
                cp.kurt_val = float(s.kurtosis())
            except Exception:
                pass
            # Skew/kurt hints (Walker — Ch. 4)
            if cp.skew_val is not None and abs(cp.skew_val) > 1:
                cp.hints.append(f"skew={cp.skew_val:.2f} — non-normal; prefer IQR over z-score for outliers")
            if cp.kurt_val is not None and cp.kurt_val > 3:
                cp.hints.append(f"kurtosis={cp.kurt_val:.2f} — fat tails; check for top-coding")

        # Top frequencies (categorical / low-cardinality)
        if not pd.api.types.is_numeric_dtype(s) or n_unique < 50:
            try:
                vc = s.value_counts(dropna=False).head(top_values_per_column)
                cp.top_values = [(_safe(k), int(v)) for k, v in vc.items()]
            except Exception:
                pass

        # Cardinality hint — high-cardinality object column should be category
        if not pd.api.types.is_numeric_dtype(s):
            cardinality_ratio = n_unique / n_rows if n_rows else 0.0
            if cardinality_ratio < 0.05 and n_unique > 1:
                cp.hints.append(f"low-cardinality object column ({n_unique} levels) — consider .astype('category')")
            if cardinality_ratio > high_cardinality_threshold:
                cp.hints.append("almost unique — likely an ID column; do not use as feature")

        # Datetime hint — object column that looks parseable
        if str(s.dtype) == "object":
            sample_str = s.dropna().astype(str).head(3).tolist()
            if any(_looks_datetime(v) for v in sample_str):
                cp.hints.append("object column looks datetime — use pd.to_datetime(..., errors='coerce')")

        # Float column with NaN that may be int — Chen's Int64 hint
        if str(s.dtype).startswith("float") and n_null > 0:
            try:
                non_null = s.dropna()
                if (non_null == non_null.astype(int)).all():
                    cp.hints.append("float column with NaN but all integer values — consider Int64 (nullable int)")
            except Exception:
                pass

        # Quality flag
        if null_rate >= null_rate_warn:
            quality_flags.append(f"{col}: {null_rate:.1%} null — completeness gate")

        columns.append(cp)

    # Duplicates
    dup_rows = int(df.duplicated().sum())
    if dup_rows:
        quality_flags.append(f"{dup_rows} duplicate rows — Walker: drop_duplicates required before counting")

    # Column drift hints
    drift = _column_drift_hints(list(df.columns))

    return ProfileReport(
        source_path=source_path,
        n_rows=n_rows,
        n_columns=len(df.columns),
        duplicate_rows=dup_rows,
        column_drift=drift,
        columns=columns,
        quality_flags=quality_flags,
    )


def _safe(v: Any) -> Any:
    try:
        return v.item()  # numpy → Python scalar
    except (AttributeError, ValueError):
        return v


def _looks_datetime(s: str) -> bool:
    if not isinstance(s, str):
        return False
    s = s.strip()
    if len(s) < 6 or len(s) > 30:
        return False
    digits = sum(1 for c in s if c.isdigit())
    seps = sum(1 for c in s if c in "/-:T. ")
    return digits >= 4 and seps >= 1


def _column_drift_hints(cols: list[str]) -> list[str]:
    """Heuristic: columns with leading/trailing whitespace, mixed case, or
    Unicode lookalikes — common in periodic data dumps."""
    drift: list[str] = []
    for c in cols:
        if not isinstance(c, str):
            continue
        if c != c.strip():
            drift.append(f"'{c}' has surrounding whitespace")
        if any(ch in c for ch in (" ", "–", "—")):
            drift.append(f"'{c}' contains non-ASCII spaces / dashes")
    return drift
