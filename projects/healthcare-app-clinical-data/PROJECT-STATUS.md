# PROJECT-STATUS — healthcare-app-clinical-data

**Last updated:** 2026-05-03 (Phase 0 in progress)

This is the multi-session resumption anchor. On a new session: read this first, find the last completed task in the table, resume from the next.

## Phase tracker

| Phase | Conditions | Drugs (A–J) | Drugs (L–V) | Lab tests | Imaging | Procedures | Cross-cohort |
|---|---|---|---|---|---|---|---|
| 0 — Scaffold | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 1 — Wave 1 research | pending | pending | pending | pending | pending | pending | n/a |
| 2 — QA loop | pending | pending | pending | pending | pending | pending | n/a |
| 3 — Wave 2 gap-fill | pending | pending | pending | pending | pending | pending | n/a |
| 4 — Critical reasoning | pending | pending | pending | pending | pending | pending | pending |
| 5 — Deliverable assembly | pending | pending (merged) | pending (merged) | pending | pending | pending | pending |

Status values: `pending` / `in progress` / `complete` / `blocked: <reason>`.

The drugs cohort is dispatched as two parallel sub-agents (ATC A–J and ATC L–V) but merged for Phase 5 deliverables.

## Phase 0 sub-tasks

- [x] 0.1 Directory tree
- [x] 0.2 README.md
- [x] 0.3 CLAUDE.md
- [x] 0.4 PROJECT-STATUS.md (this file)
- [x] 0.5 EVIDENCE-AUDIT.md
- [x] 0.6 _context/coding-standards-master.md
- [x] 0.7 _context/source-tiers.md, geographic-scope.md, exclusions.md, client-brief.md
- [x] 0.8 _registry/sources.bib
- [x] 0.9 Commit Phase 0

**Phase 0 complete 2026-05-03. Ready for Phase 1 — Wave 1 dispatch.**

## Decisions log

- 2026-05-03 — Approach approved by client (internal team). 5 cohorts, drugs cohort split A–J / L–V for Wave 1 dispatch. Geography: Uganda + Kenya + Tanzania. Ranking: IHME GBD. Coding standards per cohort (ICD-10 / ATC / LOINC / RadLex / ICD-10-PCS + CDT).

## Open methodology notes

1. Uganda EMHSLU edition will be cited in report; drugs that may have moved on/off since flagged.
2. Per-drug NDA register verification capped at ~200 highest-priority drugs for tractability; the rest cited from EMHSLU listings.
3. East African lab reference ranges used where published; Tietz/Western fallback marked `[reference range from Western source — local validation pending]`.
4. ICD-10-PCS as primary procedure code with WHO ICHI as secondary.
5. CDT codes used with attribution; licensing constraint flagged for app team's commercial rollout.
