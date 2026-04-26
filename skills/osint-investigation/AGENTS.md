# Codex / generic-agent — osint-investigation

```yaml
osint:
  goal: "..."
  deliverable: profile | chronology | adverse_media | skip_trace | stakeholder_map
  legal_purpose: "..."
  cycle: {plan, collect, analyse, disseminate}
  claims:
    - {text, source_ref, tier, archived_at, confidence, verification_notes}
  refusal_check:
    no_state_intel: true
    no_doxxing: true
    no_minors_unauth: true
    no_pretexting: true
    no_tos_violating_scrape: true
  triangulation_log: [...]
```

See `SKILL.md`.
