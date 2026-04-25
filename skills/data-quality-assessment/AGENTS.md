# Codex / generic-agent — data-quality-assessment

```yaml
score:
  completeness: {score, drivers, blockers}
  usefulness:   {score, drivers, blockers}
  reliability:  {score, drivers, blockers}
  relevance:    {score, drivers, blockers}
  composite:    <float 0-1>
  passes_threshold: bool
  threshold: 0.70
gate:
  on_fail: escalate | block_analysis | proceed_with_disclosure
```

See `SKILL.md`.
