# Codex / generic-agent guidance — gap-analysis

Output a structured gap-list per research file:

```yaml
gaps:
  - dimension: geographic | cohort | source-type | time | language | vulnerable-group | quantitative | triangulation | quotes
    kind: search | structural | scope
    description: "..."
    proposed_fix: "..."
    priority: high | medium | low
```

See `SKILL.md` for canonical rules.
