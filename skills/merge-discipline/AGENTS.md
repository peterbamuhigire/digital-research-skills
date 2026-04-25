# Codex / generic-agent — merge-discipline

```yaml
merge:
  on: [...]
  how: inner | left | right | outer
  validate: one_to_one | one_to_many | many_to_one | many_to_many
  indicator: true
  audit_report:
    left_only: <int>
    right_only: <int>
    both: <int>
    fan_out_factor: <float>
    warnings: [...]
  thresholds:
    max_left_only_rate: 0.10
    max_fan_out: 1.5
```

See `SKILL.md`.
