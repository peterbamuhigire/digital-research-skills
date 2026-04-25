# Codex / generic-agent — anomaly-detection

```yaml
panel:
  methods: [iqr, zscore, isolation_forest, cooks_distance, period_delta, stl_residual]
  univariate_column: "..."
  multivariate_columns: [...]
  parameters:
    iqr_multiplier: 1.5
    zscore_threshold: 3.0
    isolation_contamination: 0.05
results:
  per_method: {method, n_flagged, flagged_indices, threshold_used}
  consensus_indices: [...]   # flagged by ≥2 methods
```

See `SKILL.md`.
