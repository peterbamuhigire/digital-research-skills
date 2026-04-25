# Codex / generic-agent guidance — cross-cohort-synthesis

Output a synthesis matrix:

```yaml
shared_pains:
  - pain: "Deposit theft"
    cohorts: [students, tenants]
    mechanism_match: identical | similar | symbolic
    evidence_strength: high

cascades:
  - source_pain: "HELB delay"
    source_cohort: students
    target_pain: "Cashflow crisis"
    target_cohort: hostel-owners
    mechanism: "..."

contradictions:
  - claim_a: "..."
    claim_a_source: "..."
    claim_b: "..."
    claim_b_source: "..."
    resolution: pending | tier-preferred | segment-split
```

See `SKILL.md`.
