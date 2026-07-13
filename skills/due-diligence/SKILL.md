---
name: due-diligence
description: Use when conducting lawful corporate, financial, sanctions, regulatory, ownership, or background-check due diligence that needs an auditable finding trail and CARA resolution; use osint-investigation for broader open-source inquiry without a diligence decision.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Due Diligence

Single entry skill for corporate, financial, sanctions, regulatory, and background-check diligence. For broader open-source investigations, load `osint-investigation`. For licensed-PI workflows, load `pi-investigation`.

Diligence conclusions are high-stakes judgments. Run `critical-reasoning-and-argument` before classifying a red flag, resolving an allegation, weighing a pattern, or recommending proceed / conditions / decline / escalate.

## Workflow router

| Diligence goal | Load |
|---|---|
| Run the standard 3-phase DD investigation (planning → collection → analysis → reporting) | `references/dd-framework-hetherington.md` |
| Architect the final DD report (CARA framework: Context, Allegations, Resolutions, Actions) | `references/dd-report-architecture.md` |
| Trace beneficial ownership and pierce the corporate veil | `references/corporate-veil.md` |
| Screen for sanctions, PEPs, watchlists | `references/sanctions-pep-screening.md` |
| Find the right registry / regulator / public record per jurisdiction | `references/jurisdictional-registry-atlas.md` |
| Map the regulatory landscape that governs a target | `references/regulatory-landscape-mapping.md` |
| Run a background check on an individual (employment, education, criminal, civil) | `references/background-check-workflow.md` |

## CRAWL methodology (universal — Hetherington)

Detail in `references/dd-framework-hetherington.md`. The engine's default DD process:

1. **C — Collect** the publicly available record (registries, sanctions lists, courts, regulators, media).
2. **R — Review** for red flags (sanctions, litigation, regulatory action, adverse media, ownership opacity).
3. **A — Analyse** the patterns across the file (consistency, timeline, motive, capacity).
4. **W — Weigh** the evidence by source tier and triangulation.
5. **L — Log** every finding with source, date, tier, confidence — the audit trail.

## CARA report architecture

Detail in `references/dd-report-architecture.md`. Every formal DD report uses:

- **C — Context** — who is the subject, what is the engagement, what is the scope.
- **A — Allegations / findings** — every red flag, named clearly, sourced precisely.
- **R — Resolutions** — for each allegation: refuted / partially substantiated / substantiated / unresolved, with evidence.
- **A — Actions** — recommendations: proceed / proceed with conditions / decline / escalate.

## Mandatory pairings

- **`source-evaluation`** — every claim in a DD report rides the 5-tier ladder + Burke/Tudor/Silverman audits.
- **`critical-reasoning-and-argument`** — every allegation, pattern, CARA resolution, and recommendation must pass an argument map, countercase, inference audit, and certainty calibration.
- **`web-scraping-foundations`** — when collection automates registry pulls.
- **`report-and-proposal-craft`** — for the formal report container (front matter, exec summary, three-way discipline).

## Reference index

| Reference | Load when |
|---|---|
| `references/dd-framework-hetherington.md` | Every DD engagement — CRAWL phases, planning, collection, analysis |
| `references/dd-report-architecture.md` | Producing a formal DD report — CARA structure, evidence ladders, recommendation discipline |
| `references/corporate-veil.md` | Beneficial-ownership tracing, shell-company patterns, jurisdictional opacity, UBO discovery |
| `references/sanctions-pep-screening.md` | Sanctions / PEP / watchlist screening — list inventory, fuzzy match discipline, adverse-hit handling |
| `references/jurisdictional-registry-atlas.md` | Per-jurisdiction map of company registry, beneficial-ownership registry, court records, regulator portals (East Africa + global) |
| `references/regulatory-landscape-mapping.md` | Mapping the regulators / standards / licences that govern a target's operations |
| `references/background-check-workflow.md` | Individual background checks — employment, education, professional licence, criminal, civil, identity |

## Universal output rule

Every finding in a DD artifact carries:

- Source URL or document ID (with archive snapshot).
- Source tier (1–5).
- Date accessed (UTC).
- Confidence (high / medium / low).
- Triangulation status (single-source / multi-source / contested).
- Evidence-ladder verdict (CARA-Resolved category).

A finding without those fields does not ship.

## Universal anti-patterns

- "No adverse hits" without naming the lists checked, the date, and the match algorithm.
- Sanctions / PEP screening on name-only without DOB / nationality / aliases.
- Confusing "no record" with "no registry exists in that jurisdiction."
- Ownership trace stopped at the first nominee or trust without flagging.
- Report that pretends to certainty where the file is contested or thin.
- Mixing legal advice with diligence findings (the engine reports facts; counsel interprets).
- Single-source adverse-media item treated as proven misconduct.
- Reusing a sanctions screen >30 days old without re-running.
- Background-check claims about criminal history without authorisation framework declared.
- Skipping the audit log; CRAWL's L is non-negotiable.

## Universal ship gate

- [ ] Engagement scope written; jurisdictions named; cut-off date stated.
- [ ] CRAWL phases logged.
- [ ] Sanctions / PEP screen run within 30 days; algorithm and lists named.
- [ ] Registry hits captured with hit-link, date, screenshot or scrape archive.
- [ ] UBO trace pursued to the natural person or to a flagged opacity barrier.
- [ ] Adverse-media items each tier-evaluated and triangulated where required.
- [ ] CARA verdicts (refuted / partial / substantiated / unresolved) per allegation.
- [ ] Critical-reasoning gate passed for red flags, patterns, CARA resolutions, and recommendations.
- [ ] Recommendations specific (proceed / conditions / decline / escalate).
- [ ] Engine-level guardrail (`source-evaluation/references/evidence-discipline.md`) run.
- [ ] No legal advice; counsel boundary respected.
- [ ] Report container conforms to `report-and-proposal-craft` formal-report standards.

## Companion skills

<!-- dual-compat-start -->
## Use When

Use for lawful diligence supporting proceed, conditions, decline, or escalation decisions.

## Do Not Use When

Use `osint-investigation` for broad inquiry without a diligence subject and decision; do not use for unlawful surveillance or legal advice.

## Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Subject identifiers, scope, jurisdictions, cut-off date, authority | Client and engagement record | Stop collection |
| Registry, sanctions, court, regulator, media evidence | Verified primary and secondary sources | Mark `no source found` or unresolved; do not clear the subject |

## Diligence Core Method

1. Confirm lawful authority, identifiers, scope, jurisdictions, and decision.
2. Collect and log sources under CRAWL with provenance and cut-off dates.
3. Resolve identity matches before treating any hit as relevant.
4. Analyse each allegation, countercase, and evidence limit; stop on unsafe attribution.
5. Issue CARA findings and actions with unresolved gaps visible.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Diligence report and evidence log | Authorised decision-maker | Each finding has subject match, source trail, confidence, resolution, and action |

## Diligence Evidence Guidance

The search log, source captures, identity-resolution record, ownership trace, allegation matrix, and CARA report form the diligence evidence.

## Diligence Capability Notes

Default to lawful public-record review. Private-data access, contacting subjects, surveillance, paid searches, publication, or adverse action requires explicit authority and applicable legal review.

## Degraded Mode

Fallback when registries, matches, or screens are unavailable: keep them unresolved, return a scoped partial result, mark checks `not assessed`, and never convert absence of evidence into clearance.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| Identity match is ambiguous | Hold and seek discriminators | False positive |
| Evidence is contested or single-source | Mark unresolved and triangulate | Defamatory overstatement |
| Opacity blocks ownership trace | Report the barrier | False beneficial-owner claim |

## Quality Standards

Every finding is lawful, attributable, identity-resolved, source-tiered, time-bounded, and proportionate to the evidence.

## Diligence Pitfalls

- Treating a name match as identity; resolve identifiers.
- Equating no hit with clearance; state coverage.
- Presenting an allegation as fact; apply CARA.
- Stopping at a nominee; trace or flag opacity.
- Recommending legal conclusions; preserve counsel boundary.

## Worked Example

An adverse-media name match without a second identifier remains unresolved and cannot support a decline recommendation by itself.

## References

- [CRAWL framework](references/dd-framework-hetherington.md)
- [CARA report architecture](references/dd-report-architecture.md)
- [Sanctions and PEP screening](references/sanctions-pep-screening.md)
<!-- dual-compat-end -->

## Workflow

1. Confirm lawful authority, identifiers, scope, jurisdictions, decision, and cut-off date.
2. Collect and log public-record evidence with provenance and coverage.
3. Stop when identity is ambiguous, attribution is unsafe, or a required source cannot be assessed.
4. Recover by seeking discriminating identifiers, triangulating the claim, or preserving an unresolved finding.
5. Resolve findings through CARA and issue proportionate actions with gaps visible.

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Search log, identity record, ownership trace, allegation matrix, and CARA report | Authorised decision-maker and reviewer | Every finding is identity-resolved, sourced, time-bounded, confidence-rated, and actionable |

## Capability Contract

Minimum capability is read-only access to lawful public records and authorised identifiers. Private-data access, contact, surveillance, spending, publication, or adverse action requires explicit authorisation and legal review.

## Anti-Patterns

- Treating a name match as identity. **Fix:** resolve discriminating identifiers.
- Equating no hit with clearance. **Fix:** state lists, dates, and coverage.
- Presenting an allegation as fact. **Fix:** apply CARA resolution.
- Stopping at a nominee. **Fix:** trace ownership or flag opacity.
- Recommending legal conclusions. **Fix:** preserve the counsel boundary.

## Companion skills

- `source-evaluation` — mandatory pairing.
- `critical-reasoning-and-argument` — mandatory for allegation resolution, red-flag weighting, pattern analysis, and action recommendation.
- `osint-investigation` — when DD requires broader open-source recon.
- `pi-investigation` — when licensed-PI evidence collection is needed.
- `web-scraping-foundations` — for registry automation.
- `report-and-proposal-craft` — for the report container.
