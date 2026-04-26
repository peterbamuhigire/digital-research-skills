---
name: data-quality-pipeline
description: Use when handling any tabular data the engine consumes — raw → encoding repair → tidy check → cleaning → outlier panel → merge audit → four-axis quality score → manifest. Carries the engine's data-discipline pipeline as one entry skill with six references (Walker quality, Wickham tidy, Chen merge, encoding-and-unicode, anomaly panel, cleaning recipes). Pair with dataset-discovery-and-analysis when the data still needs to be found.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
  priority: critical
---

# Data Quality Pipeline

Single entry skill for any tabular data passing through the engine. Detail in `references/`; SKILL.md is the orchestrator. For finding datasets in the first place, load `dataset-discovery-and-analysis`.

## The pipeline (run in this order)

```
raw bytes
   ↓ (1) encoding repair      → references/encoding-and-unicode.md
clean text bytes
   ↓ (2) tidy check          → references/tidy-data-craft.md
tidy DataFrame
   ↓ (3) clean               → references/cleaning-pandas.md
clean DataFrame
   ↓ (4) outlier panel       → references/anomaly-detection.md
flagged DataFrame
   ↓ (5) merge audit         → references/merge-discipline.md   (only if joining)
merged DataFrame
   ↓ (6) quality score       → references/quality-assessment-walker.md
DataQualityScore + manifest
   ↓ (7) ship gate
output Parquet + manifest
```

Skipping a step produces silent data quality failures downstream.

## Reference index

| Stage | Reference | What it does |
|---|---|---|
| 1. Encoding repair | `references/encoding-and-unicode.md` | charset-normalizer + ftfy + BOM strip; runs before any pandas read |
| 2. Tidy check | `references/tidy-data-craft.md` | Wickham violation linter (columns_are_values / multiple_vars_per_column / vars_split_rows_cols) |
| 3. Cleaning | `references/cleaning-pandas.md` | Walker + Chen recipe library — types, missing values, duplicates, normalisation |
| 4. Anomaly detection | `references/anomaly-detection.md` | IQR + z-score + Isolation Forest panel; skew-aware method selection |
| 5. Merge audit | `references/merge-discipline.md` | Walker checkmerge + Chen `validate=` cardinality; mandatory before any join |
| 6. Quality score | `references/quality-assessment-walker.md` | Four-axis composite (completeness · usefulness · reliability · relevance), default weights (0.25, 0.25, 0.30, 0.20), `passes(threshold=0.7)` gate |
| Cross-cutting | `tools/data/profiler.py` | Profile DataFrame: dtypes, distributions, cardinality, skew/kurt hints |

## The four-axis quality score (engine's gate)

Every dataset that ships carries a score with these axes:

| Axis | Default weight | What it measures |
|---|---|---|
| **Completeness** | 0.25 | Missing-value rate per column; required-column presence |
| **Usefulness** | 0.25 | Required columns present; cardinality fit; type validity |
| **Reliability** | 0.30 | Source tier (`source-evaluation`) + provenance + duplicate rate |
| **Relevance** | 0.20 | Match to research topic, geographic scope, time range |

Composite score: weighted sum. Default ship gate: composite ≥ 0.70. Lower thresholds require explicit override and reason.

## The provenance packet (required output per dataset)

Every dataset that survives the pipeline produces:

```
projects/<id>/data/dataset.parquet           # the cleaned data
projects/<id>/data/dataset.profile.json      # profile (dtypes, distributions, cardinality)
projects/<id>/data/dataset.dq.json           # four-axis quality score
projects/<id>/data/dataset.manifest.json     # provenance: source, fetched_at, encoding,
                                              # cleaning_steps_applied, tidy_violations_fixed,
                                              # outliers_flagged, merge_audit, dq_score
```

Without the manifest, the data is not shippable.

## The non-negotiable rules

1. **Encoding first.** No `pd.read_csv` before `references/encoding-and-unicode.md` has run. Default `encoding='utf-8-sig'`.
2. **Tidy before analysis.** Load `references/tidy-data-craft.md`; lint for the three Wickham violations; fix them.
3. **`validate=` on every merge.** Load `references/merge-discipline.md`. Default `validate='one_to_one'` or `'one_to_many'` — never default-merge.
4. **Outlier panel, not single test.** Load `references/anomaly-detection.md`. IQR for skewed; z-score for normal; Isolation Forest for high-dimensional. Consensus across 2+ methods before flag.
5. **Score before ship.** Load `references/quality-assessment-walker.md`. Composite ≥ 0.70 default; sub-axis ≥ 0.50 each.
6. **Manifest always.** No dataset ships without the provenance packet.

## Universal anti-patterns

- `pd.read_csv` with no encoding repair → silent BOM-corruption of first column header.
- Cleaning before checking tidiness → fixing rows that should not exist as separate rows.
- Default `pd.merge` → silent fan-out duplication in many-to-many joins.
- Single-method outlier detection → either too strict (z-score on skewed) or too loose (IQR on multimodal).
- Quality score reported as one number without sub-axes → hides which axis failed.
- Cleaning step that drops rows without logging the reason → unrecoverable data loss.
- Manifest written by hand → drifts from actual processing.
- Reporting `n_rows` without `n_duplicates_removed`, `n_outliers_flagged`, `n_merge_orphans`.

## Universal ship gate

- [ ] Encoding repaired; manifest records detected encoding and BOM-stripped flag.
- [ ] Tidy check passed; violations fixed or flagged.
- [ ] Cleaning steps logged in manifest with input/output row counts.
- [ ] Outlier panel run; consensus flags exported.
- [ ] Every merge ran with `validate=`; orphan rate within threshold; fan-out factor sane.
- [ ] Four-axis score computed; composite ≥ 0.70 (or override declared with reason).
- [ ] Provenance packet written: parquet + profile.json + dq.json + manifest.json.
- [ ] Pair with `source-evaluation` reliability tier (mandatory).

## Companion skills

- `dataset-discovery-and-analysis` — find the data before this pipeline runs.
- `source-evaluation` — reliability axis depends on this.
- `web-scraping-foundations` — when the data has to be scraped.
- `research-orchestration` — when the data is feeding a research project.
- `report-and-proposal-craft`, `academic-writing` — when the data feeds a written artifact.
