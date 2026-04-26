# Codex / generic-agent — reports-proposals-craft

```yaml
report_or_proposal:
  type: report | proposal | hybrid
  purpose_statement:
    reader: "..."
    decision: "..."
    because_document_shows: "..."
    next_action: "..."
    deadline: "YYYY-MM-DD"
  audience_grid:
    decider: {name, must_see, likely_objection}
    influencer: {...}
    blocker: {...}
    user: {...}
    gatekeeper: {...}
  recommendations:
    - {text, owner, deadline, cost}
  scqa: {situation, complication, question, answer}
  ship_gate: {standalone_summary, lead_on_p1, claims_sourced, ...}
```

See `SKILL.md`.
