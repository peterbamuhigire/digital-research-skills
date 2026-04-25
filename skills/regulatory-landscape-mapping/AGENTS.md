# Codex / generic-agent guidance — regulatory-landscape-mapping

Output structured per-jurisdiction:

```yaml
jurisdiction: KE | UG | TZ | RW | BI | SS
constitutional: [{article, content, source_url}]
statute: [{name, year, status, key_provisions, source_url}]
subsidiary: [{name, parent_statute, source_url}]
case_law: [{citation, year, ratio, source_url}]
enforcement:
  regulator: "..."
  recent_actions: [...]
  enforcement_gap: "..."
```

See `SKILL.md`.
