# Codex / generic-agent — crosswalk-matrix

```yaml
project: <id>
last_updated: YYYY-MM-DD
rows: [{rq_id, question}]
columns: [{source_id, source_label}]
cells:
  - rq_id, source_id, value: MA-001 | gap | NR | WIP | orphan
progress:
  populated: <int>
  gaps: <int>
  wip: <int>
  nr: <int>
  orphaned: <int>
prioritised_open_gaps: [{rq_id, source_id, priority, rationale}]
```

See `SKILL.md`.
