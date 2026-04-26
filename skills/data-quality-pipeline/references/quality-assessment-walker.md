# Data quality assessment — the four axes

The user's specification: every dataset must be assessed for **completeness, usefulness, reliability, relevance** before the engine uses it. This skill enforces that gate.

## The four axes

### 1. Completeness
- Cell-level complete rate (`1 - null_count / total_cells`)
- Row-level complete rate (`1 - rows_with_any_null / total_rows`)
- Walker's discipline: `df.isnull().sum(axis=0)` for column-wise, `df.isnull().sum(axis=1).value_counts()` for row-wise profile

**Threshold**: 0.7 default for production research; 0.5 for exploratory.

### 2. Usefulness
- Required columns present (caller specifies which columns the research question needs)
- Sample size sufficient (≥30 for any inferential analysis; ≥100 for stratified analysis)
- Granularity matches the question (per-day vs per-month vs per-year)
- Column count reasonable (not 2 columns; not 500 columns of unknown noise)

**Threshold**: 0.7 default. Below 0.7 → escalate to operator with a list of missing capabilities.

### 3. Reliability
Walker's five sub-axes collapsed:
- **Accuracy** — verifiable against external truth (recompute from source)
- **Consistency** — internal logical checks (cross-field implications)
- **Validity** — type/range/format conformity
- **Uniqueness** — no duplicate records on natural keys
- **Timeliness** — data fresh enough for the question

The internal-signal score uses: duplicate-row rate, dtype-suspect column count, average IQR-outlier rate. External-truth verification (best) requires caller to supply a trusted reference.

**Threshold**: 0.7 default. Below 0.7 → run Walker's diagnostic battery before using.

### 4. Relevance
- Geographic scope match (does the dataset cover the target jurisdictions?)
- Time-range match (does it cover the target window?)
- Topic match (do column names suggest the dataset speaks to the question?)

**Threshold**: 0.7 default. Below 0.7 → caller likely retrieved the wrong dataset.

## Standard usage

```python
from tools.data import score_data_quality, profile_dataframe
import pandas as pd

df = pd.read_parquet("projects/<id>/data/dataset.parquet")

# Profile first — Walker + Chen probes
profile = profile_dataframe(df, source_path="dataset.parquet")
profile.to_json("projects/<id>/data/profile.json")

# Then score against the research question
dq = score_data_quality(
    df,
    research_topic="rental housing Uganda",
    required_columns=["region", "rent_amount", "household_size", "year"],
    expected_geographic_scope=["UG"],
    expected_time_range=("2020-01-01", "2025-12-31"),
    geographic_column="country_iso",
    time_column="survey_date",
)

if not dq.passes(threshold=0.7):
    # Escalate to operator — do NOT proceed to analysis
    print(f"DQ FAIL — composite {dq.composite:.2f}")
    print(f"  completeness {dq.completeness.score:.2f}: {dq.completeness.blockers}")
    print(f"  usefulness   {dq.usefulness.score:.2f}: {dq.usefulness.blockers}")
    print(f"  reliability  {dq.reliability.score:.2f}: {dq.reliability.blockers}")
    print(f"  relevance    {dq.relevance.score:.2f}: {dq.relevance.blockers}")
```

## Decision rules

- **Always profile + score before analysing.** No exceptions.
- **Document the score** in the project's `<cohort>/research/sources.md`.
- **If composite < 0.7**, either:
  - Find a different dataset
  - Limit the research question to what the data supports
  - Disclose the limitation explicitly in the final report
- **The score is a starting point.** Walker: outliers may be real, missingness may be informative. Use the score to direct attention, not to auto-reject.

## Outputs that travel with the dataset

```
projects/<id>/data/dataset.parquet
projects/<id>/data/dataset.profile.json   # ProfileReport
projects/<id>/data/dataset.dq.json        # DataQualityScore
projects/<id>/data/dataset.manifest.json  # SHA-256, source URL, license, retrieval date
```

These four files together are the dataset's **provenance packet**. Every figure / table / claim that uses the dataset cites it and links to the packet.

## Anti-patterns

- Analysing before profiling
- Trusting `read_csv`'s dtype inference (pass `dtype=`, `na_values=`, `parse_dates=` explicitly)
- Treating null counts as the only completeness signal (row-level matters)
- Computing reliability without checking duplicates first
- Skipping relevance scoring (the most-cited dataset isn't always the right one)
- Over-relying on internal-signal reliability (verify against external source where possible)

## See also

- `tools/data/dq_score.py`, `tools/data/profiler.py` — implementation
- `dataset-discovery-and-analysis` — upstream (retrieval)
- `data-cleaning-pandas` — what to do when DQ score is low
- `tidy-data-craft` — Wickham violation detection
- `merge-discipline` — when joining multiple datasets
- `evidence-discipline` — engine-wide rule
