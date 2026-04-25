# Codex / generic-agent — tudor-twelve-point-evaluation

```yaml
source_id: <id>
scores:
  recency: 0..3
  relevancy: 0..3
  authority: 0..3
  completeness: 0..3
  accuracy: 0..3
  clarity: 0..3
  verifiability: 0..3
  statistical_validity: 0..3
  internal_consistency: 0..3
  external_consistency: 0..3
  context: 0..3
  comparative_quality: 0..3
  # optional financial:
  understandability: 0..3
  reliability_faithfulness: 0..3
  comparability: 0..3
total: <int>
threshold_action: promote | use_with_caveats | quote_selectively | flag
notes_per_criterion: {recency: "...", ...}
```

See `SKILL.md`.
