# Codex / generic-agent — sanctions-pep-screening

```yaml
screen:
  name: "..."
  dob: YYYY-MM-DD | null
  nationality: ISO-2 | null
  aliases: [...]
  threshold_high: 0.92
  threshold_medium: 0.78
  cache_dir: "./data/sanctions"

results:
  high_confidence_hits: [...]
  medium_confidence_hits: [...]
  low_confidence_hits: [...]
  negative_finding_text: "A search of <lists> on <date> did not reveal matches"
```

See `SKILL.md`.
