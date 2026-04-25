# Codex / generic-agent — skip-tracing-craft

```yaml
skip:
  type: unintentional | intentional | marital | criminal
  identifiers_known: [name, dob, ssn_last4, dl, address, phone, employer]
  permissible_purpose: "..."  # FCRA / DPPA / GLBA
  database_chain:
    - in_house
    - public_records
    - court_dockets
    - corporate_registry
    - commercial_db
    - interview_chain
  found_address: "..." | null
  confidence: high | medium | low
```

See `SKILL.md`.
