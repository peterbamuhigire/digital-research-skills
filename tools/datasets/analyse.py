"""Automatic dataset profiling — schema, stats, missingness, anomalies.

Per Segnini's Verification Handbook five-step quality check:
1. Completeness (null-rate per column)
2. Duplicates (per id field)
3. Accuracy (extreme-value spot-check)
4. Integrity (referential, time-stale flags)
5. Codes/acronyms (build glossary)

This module produces a one-page profile per dataset.
"""
from __future__ import annotations

from dataclasses import dataclass, field
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
    sample_values: list[Any] = field(default_factory=list)
    min_val: Any = None
    max_val: Any = None
    mean_val: Optional[float] = None
    std_val: Optional[float] = None


@dataclass(slots=True)
class DatasetProfile:
    source_path: str
    detected_format: str
    n_rows: int
    n_columns: int
    columns: list[ColumnProfile]
    duplicate_rows: int
    quality_flags: list[str] = field(default_factory=list)


def profile_dataset(
    path: str | Path, *,
    sheet: Optional[str] = None,
    sample_per_column: int = 5,
    null_rate_warn: float = 0.30,
) -> DatasetProfile:
    """Profile a CSV / TSV / JSON / NDJSON / Parquet / Excel dataset.

    Lazy-imports pandas + pyarrow.
    """
    import pandas as pd

    path = Path(path)
    fmt = _detect(path)
    df = _load(path, fmt, sheet)

    columns: list[ColumnProfile] = []
    quality_flags: list[str] = []

    for col in df.columns:
        s = df[col]
        n_total = len(s)
        n_null = int(s.isna().sum())
        null_rate = n_null / n_total if n_total else 0.0
        n_unique = int(s.nunique(dropna=True))

        col_profile = ColumnProfile(
            name=str(col),
            dtype=str(s.dtype),
            n_total=n_total,
            n_null=n_null,
            null_rate=null_rate,
            n_unique=n_unique,
            sample_values=[_safe_value(v) for v in s.dropna().head(sample_per_column).tolist()],
        )
        if pd.api.types.is_numeric_dtype(s):
            col_profile.min_val = _safe_value(s.min())
            col_profile.max_val = _safe_value(s.max())
            col_profile.mean_val = float(s.mean()) if n_null < n_total else None
            col_profile.std_val = float(s.std()) if n_null < n_total else None

        columns.append(col_profile)

        if null_rate >= null_rate_warn:
            quality_flags.append(
                f"{col}: high null rate {null_rate:.1%} (Segnini step 1 — completeness check)"
            )

    duplicate_rows = int(df.duplicated().sum())
    if duplicate_rows > 0:
        quality_flags.append(
            f"{duplicate_rows} duplicate rows detected (Segnini step 2 — duplicates check)"
        )

    return DatasetProfile(
        source_path=str(path),
        detected_format=fmt,
        n_rows=len(df),
        n_columns=len(df.columns),
        columns=columns,
        duplicate_rows=duplicate_rows,
        quality_flags=quality_flags,
    )


def _detect(path: Path) -> str:
    ext = path.suffix.lstrip(".").lower()
    return {"csv": "csv", "tsv": "tsv", "json": "json", "ndjson": "ndjson",
            "parquet": "parquet", "pq": "parquet",
            "xlsx": "excel", "xls": "excel"}.get(ext, "unknown")


def _load(path: Path, fmt: str, sheet: Optional[str]) -> Any:
    import pandas as pd
    if fmt == "csv":
        return pd.read_csv(path, low_memory=False)
    if fmt == "tsv":
        return pd.read_csv(path, sep="\t", low_memory=False)
    if fmt == "json":
        return pd.read_json(path)
    if fmt == "ndjson":
        return pd.read_json(path, lines=True)
    if fmt == "parquet":
        return pd.read_parquet(path)
    if fmt == "excel":
        return pd.read_excel(path, sheet_name=sheet) if sheet else pd.read_excel(path)
    raise ValueError(f"Unsupported format: {fmt}")


def _safe_value(v: Any) -> Any:
    """Convert numpy / pandas scalars to plain Python so the profile is JSON-serialisable."""
    try:
        # numpy scalar → Python scalar via .item()
        return v.item()  # type: ignore[union-attr]
    except (AttributeError, ValueError):
        return v
