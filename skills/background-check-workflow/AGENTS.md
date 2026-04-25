# Codex / generic-agent — background-check-workflow

```yaml
intake:
  purpose: employment | partner | dd | dating
  disclosure_release_signed: bool
  permissible_purpose: "..."  # FCRA §604
  depth: 5y_2emp | 10y_3emp | 15y_full
sweep:
  public_records: [civil, liens, judgments, divorces, criminal, ucc, bankruptcy, property]
  federal_courts: [district, tax, bankruptcy]
  regulatory: [sec, ftc, fcc, sos, dmv, ag, licensing, comptroller]
report:
  interim: bool
  final: bool
  credibility_per_finding: bool
  adverse_action_notice_required: bool
```

See `SKILL.md`.
