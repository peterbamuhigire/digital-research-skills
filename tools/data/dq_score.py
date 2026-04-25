"""Four-axis data-quality score.

The user-named axes for the knowledge-production engine:

  Completeness — null rate, row-complete rate (Walker)
  Usefulness   — granularity, time-coverage, key-presence vs research need
  Reliability  — Walker's accuracy + consistency + validity + uniqueness + timeliness
                 (collapsed into one reliability composite)
  Relevance    — topic match, geographic/temporal scope match vs research need

The score is interpretable: each axis is 0.0-1.0 with explicit drivers.
Caller decides thresholds; the engine never silently uses a low-score dataset.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass(slots=True)
class AxisScore:
    score: float                # 0.0 - 1.0
    drivers: list[str] = field(default_factory=list)
    blockers: list[str] = field(default_factory=list)  # things that cap the score
    notes: str = ""


@dataclass(slots=True)
class DataQualityScore:
    completeness: AxisScore
    usefulness: AxisScore
    reliability: AxisScore
    relevance: AxisScore
    composite: float            # weighted average

    def passes(self, *, threshold: float = 0.7) -> bool:
        """All four axes must clear the threshold."""
        return all(a.score >= threshold for a in (
            self.completeness, self.usefulness, self.reliability, self.relevance,
        ))


def score_data_quality(
    df: Any, *,
    research_topic: Optional[str] = None,
    required_columns: Optional[list[str]] = None,
    expected_geographic_scope: Optional[list[str]] = None,
    expected_time_range: Optional[tuple[str, str]] = None,
    geographic_column: Optional[str] = None,
    time_column: Optional[str] = None,
    weights: tuple[float, float, float, float] = (0.25, 0.25, 0.30, 0.20),
) -> DataQualityScore:
    """Score a DataFrame against the four-axis framework.

    research_topic / required_columns / scope hints inform usefulness + relevance;
    pass them whenever the engine has them.
    """
    import pandas as pd

    completeness = _score_completeness(df)
    usefulness = _score_usefulness(df, required_columns)
    reliability = _score_reliability(df)
    relevance = _score_relevance(
        df, research_topic, expected_geographic_scope, expected_time_range,
        geographic_column, time_column,
    )

    w_c, w_u, w_re, w_rel = weights
    composite = (
        w_c * completeness.score
        + w_u * usefulness.score
        + w_re * reliability.score
        + w_rel * relevance.score
    )

    return DataQualityScore(
        completeness=completeness,
        usefulness=usefulness,
        reliability=reliability,
        relevance=relevance,
        composite=composite,
    )


def _score_completeness(df: Any) -> AxisScore:
    import pandas as pd
    n = len(df)
    if not n:
        return AxisScore(score=0.0, blockers=["empty dataframe"])

    cell_complete = 1 - (df.isna().sum().sum() / (n * len(df.columns)))
    row_complete = 1 - (df.isna().any(axis=1).sum() / n)
    score = (cell_complete + row_complete) / 2

    drivers: list[str] = [
        f"cell-level complete rate {cell_complete:.1%}",
        f"row-level complete rate {row_complete:.1%}",
    ]
    blockers: list[str] = []
    if row_complete < 0.5:
        blockers.append(f"only {row_complete:.0%} rows fully populated")

    return AxisScore(score=score, drivers=drivers, blockers=blockers)


def _score_usefulness(df: Any, required_columns: Optional[list[str]]) -> AxisScore:
    drivers: list[str] = []
    blockers: list[str] = []
    factors: list[float] = []

    # 1. Required columns present
    if required_columns:
        present = [c for c in required_columns if c in df.columns]
        ratio = len(present) / len(required_columns)
        factors.append(ratio)
        drivers.append(f"{len(present)}/{len(required_columns)} required columns present")
        if ratio < 1.0:
            missing = [c for c in required_columns if c not in df.columns]
            blockers.append(f"missing required columns: {missing}")

    # 2. Granularity — n_rows is enough for analysis?
    if len(df) < 30:
        factors.append(0.3)
        blockers.append(f"only {len(df)} rows — usually too few for inferential analysis")
    elif len(df) < 100:
        factors.append(0.6)
        drivers.append(f"{len(df)} rows — limited statistical power")
    else:
        factors.append(1.0)
        drivers.append(f"{len(df)} rows — sufficient sample size")

    # 3. Column count — too few = limited; absurdly many = likely noise
    n_cols = len(df.columns)
    if n_cols < 2:
        factors.append(0.2)
        blockers.append(f"only {n_cols} columns")
    elif n_cols > 200:
        factors.append(0.6)
        drivers.append(f"{n_cols} columns — high-dimensional; feature selection needed")
    else:
        factors.append(1.0)

    score = sum(factors) / len(factors) if factors else 0.0
    return AxisScore(score=score, drivers=drivers, blockers=blockers)


def _score_reliability(df: Any) -> AxisScore:
    """Walker's accuracy + consistency + validity + uniqueness + timeliness.
    Heuristic without external truth — uses internal signals only."""
    import pandas as pd

    drivers: list[str] = []
    blockers: list[str] = []
    factors: list[float] = []

    # 1. Duplicate row rate
    dup_rate = float(df.duplicated().sum()) / max(len(df), 1)
    factors.append(1.0 - dup_rate)
    if dup_rate > 0.05:
        blockers.append(f"{dup_rate:.1%} duplicate rows")
    else:
        drivers.append(f"duplicates {dup_rate:.1%}")

    # 2. Type validity — columns where dtype suggests bad parsing
    suspect_cols = 0
    for col in df.columns:
        s = df[col]
        if str(s.dtype) == "object":
            # Object column with mostly numeric values is a parse problem
            sample = s.dropna().astype(str).head(20)
            if len(sample) and (sample.str.match(r"^-?\d+\.?\d*$").mean() > 0.7):
                suspect_cols += 1
    type_score = 1.0 - (suspect_cols / max(len(df.columns), 1))
    factors.append(type_score)
    if suspect_cols:
        blockers.append(f"{suspect_cols} columns appear numeric but are object dtype")

    # 3. Outlier rate (univariate IQR proxy on numeric columns)
    numeric = df.select_dtypes(include="number")
    if not numeric.empty:
        outlier_rates = []
        for col in numeric.columns:
            s = numeric[col].dropna()
            if len(s) < 4:
                continue
            q1, q3 = s.quantile(0.25), s.quantile(0.75)
            iqr = q3 - q1
            if iqr == 0:
                continue
            lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
            outlier_rate = ((s < lo) | (s > hi)).mean()
            outlier_rates.append(outlier_rate)
        if outlier_rates:
            avg_outlier = sum(outlier_rates) / len(outlier_rates)
            factors.append(1.0 - min(avg_outlier * 5, 1.0))  # scale
            drivers.append(f"avg IQR-outlier rate {avg_outlier:.1%}")

    score = sum(factors) / len(factors) if factors else 0.5
    return AxisScore(score=score, drivers=drivers, blockers=blockers,
                     notes="Reliability is internal-signal only; verify against external sources where possible.")


def _score_relevance(
    df: Any,
    topic: Optional[str],
    geo_scope: Optional[list[str]],
    time_range: Optional[tuple[str, str]],
    geo_col: Optional[str],
    time_col: Optional[str],
) -> AxisScore:
    drivers: list[str] = []
    blockers: list[str] = []
    factors: list[float] = []

    # Geographic scope match
    if geo_scope and geo_col and geo_col in df.columns:
        try:
            present = set(str(v).upper() for v in df[geo_col].dropna().unique())
            wanted = set(s.upper() for s in geo_scope)
            covered = wanted & present
            ratio = len(covered) / len(wanted) if wanted else 0
            factors.append(ratio)
            drivers.append(f"{len(covered)}/{len(wanted)} target jurisdictions present")
            if ratio < 1.0:
                missing = sorted(wanted - present)
                blockers.append(f"missing jurisdictions: {missing}")
        except Exception:
            pass

    # Time-range match
    if time_range and time_col and time_col in df.columns:
        try:
            import pandas as pd
            ts = pd.to_datetime(df[time_col], errors="coerce")
            if ts.notna().any():
                start = pd.to_datetime(time_range[0])
                end = pd.to_datetime(time_range[1])
                in_range = ts.between(start, end).mean()
                factors.append(float(in_range))
                drivers.append(f"{in_range:.1%} of rows in target time window")
        except Exception:
            pass

    # Topic match — keyword presence in column names (cheap proxy)
    if topic:
        keywords = [k.lower() for k in topic.split() if len(k) > 3]
        if keywords:
            cols_lower = " ".join(str(c).lower() for c in df.columns)
            matches = sum(1 for kw in keywords if kw in cols_lower)
            ratio = matches / len(keywords)
            factors.append(ratio)
            drivers.append(f"{matches}/{len(keywords)} topic keywords match column names")

    if not factors:
        # No filters provided — caller didn't tell us what relevance means.
        return AxisScore(score=0.5, drivers=["no relevance hints provided"], blockers=[],
                         notes="Pass research_topic / geographic_scope / time_range to score relevance properly.")

    score = sum(factors) / len(factors)
    return AxisScore(score=score, drivers=drivers, blockers=blockers)
