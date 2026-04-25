# Codex / generic-agent — adverse-media-investigation

```yaml
search:
  subject_name: "..."
  aliases: [...]
  identifiers: [year, employer, location, ...]
  engines: [google_cse, serpapi, brave]
  categories: [financial_crime, regulatory, criminal, litigation, reputational]
  languages: [en, sw, fr, ar, ...]
results:
  high_confidence: [...]   # ≥50% identifiers matched
  medium_confidence: [...]
  low_confidence: [...]    # likely false positive
  multi_source_corroborated: bool
```

See `SKILL.md`.
