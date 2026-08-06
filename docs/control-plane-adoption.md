# Control-plane adoption

This engine adopts the shared ten-engine contract from
`C:\wamp64\www\skills-web-dev\docs\engine-control-plane.md`. Digital
research remains the source of truth for source evaluation, currentness,
OSINT, standards checks, benchmarking, evidence grading, and citation audit.

## Local roles and commands

| Role | Responsibility | Required output |
|---|---|---|
| Research planner | Define the decision, claims, populations, jurisdictions, and search plan. | Research plan and claim map. |
| Source verifier | Check identity, authority, date, method, access, and claim support. | Source register. |
| Evidence grader | Grade strength, uncertainty, conflict, and freshness. | Evidence grades and caveats. |
| Citation auditor | Reconcile claims, citations, quotations, links, and output references. | Citation-audit report. |

Route thin commands `research-plan`, `source-audit`, `synthesis`, and
`citation-audit` to canonical research workflows. The deterministic
`scripts/validate_source_currency.py` adapter enforces currentness metadata
before time-sensitive claims are released. Sub-agents receive the
engine's evidence-discipline clause and return sourced findings, not invented
facts or unsupported synthesis.

## Hook and release contract

- `preflight` records question, cutoff date, jurisdiction, source access,
  sensitivity, and output standard.
- `context` loads project evidence register, prior claims, source dates,
  exclusions, and unresolved contradictions before searching.
- `before_write` checks claim provenance, quote limits, currentness, identity,
  and uncertainty before a finding enters the report.
- `after_write` runs source, currency, claim-map, citation, and anti-slop
  checks and records the evidence grade.
- `release` requires source register, currency check, claim map, citation
  audit, uncertainty statement, and independent review where risk warrants.
- `stop` preserves search state, inaccessible sources, unresolved conflicts,
  stale claims, and the next research owner.

No source, date, citation, or verification result is PASS merely because an
agent reports confidence. Missing evidence is `NOT ASSESSED` and blocks the
affected conclusion.
