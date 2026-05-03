# PROJECT-STATUS — healthcare-app-clinical-data

**Last updated:** 2026-05-03 (Phase 1 returned — 5 of 6 agents produced files; 3 cohorts had row-count fabrication strikes; Drugs A-J blocked on PDF source extraction; Phase 2 QA paused pending user sign-off)

This is the multi-session resumption anchor. On a new session: read this first, find the last completed task in the table, resume from the next.

## Phase tracker

| Phase | Conditions | Drugs (A–J) | Drugs (L–V) | Lab tests | Imaging | Procedures | Cross-cohort |
|---|---|---|---|---|---|---|---|
| 0 — Scaffold | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 1 — Wave 1 research | partial 29/220 (count strike) | blocked: PDF extraction | partial 40/280 (count strike) | partial 60/650 (count strike) | partial 97/220 | partial 80/220 | n/a |
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

## Phase 0 addendum — book-derived recommendations (2026-05-03)

A research agent studied five health-informatics textbooks (Coiera 3e; HIS-Progress; HIS-RP; Systems Perspective 2e; Multidisciplinary). Findings saved at `_context/book-derived-recommendations.md`. **All Wave 1 sub-agent briefs must reference this file.**

Material data-model changes from the addendum (apply when drafting Wave 1 briefs — design doc §4 is now superseded for these columns):

- **Conditions:** add `snomed_ct_concept_id`, `snomed_ct_description_id`, `icd11_candidate_code`, `granularity_caveat`, `coding_rule`
- **Drugs:** add `atc_ddd_value`, `atc_ddd_unit`, `rxnorm_rxcui`, `lasa_tallman_form`, structured DDI sub-table; do NOT use a free-text interactions column
- **Lab:** PHII-19 columns enforced (specimen type/container/volume_min, TAT routine/stat, critical low/high, interferences, delta-check); reference ranges split into population-keyed row variants rather than single column with sub-fields; add `snomed_ct_concept`
- **Imaging:** add `dicom_sr_template_ref`, `radlex_anatomy_id`, `radlex_finding_id`; convert `key_measurements` to structured array `[{name, loinc_id, units}, …]`
- **Procedures:** ICHI promoted to primary, ICD-10-PCS secondary (column rename — `ichi_code` is now the lead, `icd10_pcs_code` is now secondary)
- **Universal:** `code_system_version`, `code_accessed_date`, `level_of_care_min`, `cadre_min`, `connectivity_tolerance`, `paper_form_equivalent`

Wave 1 sub-agent briefs must include the 7 additional clauses listed in `_context/book-derived-recommendations.md` §6.

## Decisions log

- 2026-05-03 — Approach approved by client (internal team). 5 cohorts, drugs cohort split A–J / L–V for Wave 1 dispatch. Geography: Uganda + Kenya + Tanzania. Ranking: IHME GBD. Coding standards per cohort (ICD-10 / ATC / LOINC / RadLex / ICD-10-PCS + CDT).

## Open methodology notes

1. Uganda EMHSLU edition will be cited in report; drugs that may have moved on/off since flagged.
2. Per-drug NDA register verification capped at ~200 highest-priority drugs for tractability; the rest cited from EMHSLU listings.
3. East African lab reference ranges used where published; Tietz/Western fallback marked `[reference range from Western source — local validation pending]`.
4. ICD-10-PCS as primary procedure code with WHO ICHI as secondary.
5. CDT codes used with attribution; licensing constraint flagged for app team's commercial rollout.
