# PROJECT-STATUS — healthcare-app-clinical-data

**Last updated:** 2026-05-03 (Project completed through Phase 5: critical reasoning notes, consumables linkages, 7 cohort DOCX reports, 7 grouped XLSX data sheets, updated cross-cohort master DOCX, manifest, context files, and registry gate files generated.)

This is the multi-session resumption anchor. On a new session: read this first, find the last completed task in the table, resume from the next.

## Phase tracker

| Phase | Conditions | Drugs (A–J) | Drugs (L–V) | Lab tests | Imaging | Procedures | Cross-cohort |
|---|---|---|---|---|---|---|---|
| 0 — Scaffold | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 1 — Wave 1 research | 220/220 ✓ | 268/250 ✓ (W1+W3+W4+W5) | 304/280 ✓ (W1+W2+W3+W4+W5) | 296 rows / ~257 distinct LOINC ✓ | 255/220 ✓ | 254/220 ✓ | n/a |
| Cohort 6 — Consumables | n/a | n/a | n/a | n/a | n/a | n/a | 327/300 ✓ (W1+W2) |
| Cohort 7 — Standard forms | n/a | n/a | n/a | n/a | n/a | n/a | 45 forms/tools found in local corpus ✓ (W1) |
| 2 — QA loop | pending | pending | pending | pending | pending | pending | n/a |
| 3 — Wave 2 gap-fill | pending | pending | pending | pending | pending | pending | n/a |
| 4 — Critical reasoning | complete | complete | complete | complete | complete | complete | complete |
| 5 — Deliverable assembly | complete | complete | complete | complete | complete | complete | complete |

Status values: `pending` / `in progress` / `complete` / `blocked: <reason>`.

The drugs cohort is dispatched as two parallel sub-agents (ATC A–J and ATC L–V) but merged for Phase 5 deliverables.

The Standard Forms cohort is a local-corpus extraction, not yet a complete national HMIS catalogue. It documents every concrete form/tool found in `_context/book-derived-recommendations.md`, `_context/sources-cache/uganda-hiv-2016.md`, `_context/sources-cache/uganda-hmis-107.md`, and `_context/sources-cache/uganda-idsr.md`; rows that need current MoH toolset verification are marked as gaps.

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


## Phase 5 completion note

- Generated outputs on 2026-05-03 under `05-output/clinical-data-deliverables/` with copies in `export/`.
- Cohort row counts parsed for export: conditions: 220, drugs: 488, lab-tests: 220, imaging: 50, procedures: 222, consumables: 257, standard-forms: 45.
- Generated cohort reports include Section 1 standards and enforcing bodies per `_context/standards-and-bodies.md`.
- Standard Forms cohort is included as a local-corpus form/tool inventory and remains bounded by the available cached sources.

## Phase 6 — Tenant-setup cohorts (added 2026-05-03)

Goal: ship 7 reusable data packs so a new healthcare tenant can be configured in minutes by selecting country, facility type, and operating model.

**Scope decisions (user-confirmed 2026-05-03):**
- Country pack: full pack for **Uganda + Kenya only**; other 7 countries stubbed (header row + flagged `[STUB]`).
- Tenant blueprints: **6 canonical** v1 blueprints (small clinic, HC III, HC IV, general hospital, standalone lab, standalone pharmacy). Specialist/maternity/ART/dental/NGO blueprints deferred.

**Execution order (sequential — cross-references require coherent vocabulary):**

| # | Cohort | Status | Folder |
|---|---|---|---|
| 1 | Tenant blueprints | Wave-1 complete (6 canonical blueprints × 14 cols, all references checked against sibling cohorts) — clean | `tenant-blueprints/` |
| 2 | Facilities / org master | Wave-1 complete (28 rows × 22 cols) — Wikipedia-citation patch applied | `facilities/` |
| 3 | Roles / cadres / permissions | Wave-1 complete (18 rows × 23 cols) — regulator-conflation patch applied | `roles-permissions/` |
| 4 | Workflows / care pathways | Wave-1 complete (18 rows × 17 cols) — Schedule A/B/C residual patch applied | `workflows/` |
| 5 | Country packs (UG + KE) | Wave-1 complete (2 full + 7 stubs × 24 cols) — Wikipedia-in-cell patch applied | `country-packs/` |
| 6 | Billing / tariffs / insurance | Wave-1 complete (58 charge-items + 16 payer mappings) — clean (no patch needed) | `billing-tariffs/` |
| 7 | Reporting / KPI library | Wave-1 complete (55 indicators × 19 cols across 16 domains) — clean (no patch needed) | `reporting-kpis/` |

Note on order: **blueprints depends on the other 6**, so Wave-1 for blueprints will produce a draft schema + 6 shells with placeholders, then a Wave-2 fill-in once cohorts 2–7 have data. Cohorts 2–7 can run in their listed sequence.

**Definition of done per cohort** (per user spec): markdown data table, Word report (with §1 Standards & Bodies), Excel workbook with populated data, gaps marked explicitly, cross-links to existing clinical cohorts, manifest entry, engine validation passes.

## Phase 6 — Wave-1 completion summary (2026-05-03)

All 7 tenant-setup cohorts have Wave-1 markdown data + findings deliverables. Patches applied where evidence-discipline breaches were found (logged in `EVIDENCE-AUDIT.md`). Cross-cohort synthesis appended to `00-cross-cohort-master.md`.

**Per-cohort row counts (verified by orchestrator):**
- facilities: 28 rows
- roles-permissions: 18 rows
- workflows: 18 rows
- country-packs: 9 rows (UG+KE full; 7 stubbed)
- billing-tariffs: 58 charge-items + 16 payer mappings
- reporting-kpis: 55 indicators across 16 domains
- tenant-blueprints: 6 canonical blueprints (integration cohort)

**Discipline patches applied this phase (logged in EVIDENCE-AUDIT.md):**
1. Facilities — Wikipedia stripped from 4 flagship-hospital `source_citations` cells; bed-counts flagged `[T1 verification pending]`.
2. Roles-permissions — 8 cells corrected for regulator conflation (UMDPC ≠ clinical officers; PSU ≠ registration council; AHPC for lab + clinical-officer + radiographer cadres); medical-officer prescribing scope cleaned of "NDA Class A/B/C" misuse.
3. Workflows — 4 residual "Class A/B/C" prescribing references in WF-RX-001 patched.
4. Country-packs — Wikipedia stripped from 9 source_citations cells (one per country row).
5. Billing-tariffs — clean (no patch needed).
6. Reporting-KPIs — clean (no patch needed).
7. Tenant-blueprints — clean (orchestrator-assembled integration cohort).

**Deliverables NOT yet produced (Phase-6 next-session work):**
1. Wave-2 gap-fill — known gaps documented per cohort findings file (Mulago bed counts, Uganda enrolled-nurse / radiographer scope, NDA prescriber-schedule, Kenya clinical-guideline cache, PNFP tariffs, SHA specialist tariffs, 7 stub-country full packs, 15 form-cohort gaps in reporting-kpis, 4 deferred specialty blueprints).
2. DOCX / XLSX assembly for the 7 Phase-6 cohorts — `scripts/generate_healthcare_app_clinical_data_outputs.py` needs extension. Each cohort's Word report must carry §1 Standards & Bodies per the standing rule.
3. Critical-reasoning pass over the 7 Phase-6 cohorts — `skills/critical-reasoning-and-argument` not yet applied.
4. Updated cross-cohort master DOCX with Phase-6 sections.
5. Engine validation across the 7 new cohort folders.

**Resumption anchor:** read `00-cross-cohort-master.md` "Phase 6 — Tenant-setup synthesis" section and the per-cohort `wave1-findings.md` files for context, then start with whichever of the 5 deferred work items above the user prioritises.
