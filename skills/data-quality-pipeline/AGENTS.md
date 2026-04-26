# Codex / generic-agent — data-quality-pipeline

```yaml
data_pipeline:
  source: "..."
  fetched_at: "YYYY-MM-DDTHH:MMZ"
  encoding:
    detected: "..."
    confidence: 0.0-1.0
    bom_stripped: bool
    final: utf-8
  tidy_check:
    columns_are_values: bool
    multiple_vars_per_column: bool
    vars_split_rows_cols: bool
    fixes_applied: [...]
  cleaning:
    steps: [type_coerce, missing_value_strategy, duplicate_drop, normalize, ...]
    rows_in: <int>
    rows_out: <int>
    rows_dropped_with_reason: [...]
  outlier_panel:
    methods: [iqr, zscore, isolation_forest]
    consensus_flagged: <int>
  merge_audit:
    validate: one_to_one | one_to_many | many_to_one | many_to_many
    fan_out_factor: <float>
    orphan_rate: <float>
  dq_score:
    completeness: 0.0-1.0
    usefulness: 0.0-1.0
    reliability: 0.0-1.0
    relevance: 0.0-1.0
    composite: 0.0-1.0
    weights: [0.25, 0.25, 0.30, 0.20]
    passes: bool
  manifest_written: bool
```

See `SKILL.md`.
