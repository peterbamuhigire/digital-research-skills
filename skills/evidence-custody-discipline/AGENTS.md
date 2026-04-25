# Codex / generic-agent — evidence-custody-discipline

```yaml
chain_of_custody:
  case_id: "..."
  evidence_id: "..."
  description: "..."
  collected_at: <iso8601>
  collected_by: "..."
  transfers:
    - timestamp: <iso8601>
      from_party: "..."
      to_party: "..."
      location: "..."
      purpose: collection | transport | analysis | storage | court
      sealed_container: bool
      seal_id: "..."
  integrity_verified: bool
```

See `SKILL.md`.
