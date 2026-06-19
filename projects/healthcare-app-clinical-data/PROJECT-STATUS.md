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

## Phase 7 — Wave-3 cohorts for automated onboarding (added 2026-05-04)

Goal: commission 7 new research cohorts + extend country-packs + confirm specimen/container coverage so the automated-onboarding pipeline (designed in `docs/plans/2026-05-04-automated-onboarding-design.md`) has the full seed corpus it needs.

**Driver:** every catalogue Medic8's onboarding pipeline seeds must have a research cohort producing both a Word document explaining it in detail AND an Excel sheet of all the seed values (user instruction 2026-05-04).

**Sequencing decision (user-confirmed 2026-05-04):**
- A1.1 scaffold all 7 folders first (done in this session — README.md per cohort).
- A1.2 vaccines dispatched as foreground validation cohort.
- A1.3–A1.9 fanned out in parallel (background) once vaccines brief shape verified.
- A1.10 specimen/container confirmation pass.

| # | Cohort | Status | Folder |
|---|---|---|---|
| 1 | Vaccines (ATC J07, EPI schedules, MDVP, AEFI Brighton) | Wave-1 complete (48 rows incl. Pass-2 gap-fill: HPV, OPV/IPV splits, COVID-19, Tdap, MenAfriVac, Yellow Fever fractional) | `vaccines/` |
| 2 | BOMs (default kits per service / lab / imaging / vaccine / pack) | Wave-1 complete (85 BOMs / 433 line items incl. Pass-2 gap-fill: MRI, endoscopy, cervical-screening, FP-implant) | `boms/` |
| 3 | Drug-drug interactions (≥1,500 EAC + DDInter bulk) | Wave-1 complete (17,304 pairs: 52 EAC enumerated + 17,252 DDInter v2 bulk filtered to in-cohort ATCs) | `drug-interactions/` |
| 4 | Allergens (RxNorm + SNOMED + food/environmental) | Wave-1 complete (62 allergens × 11 cols) | `allergens/` |
| 5 | Paediatric dosing (WHO Children's Formulary + EMLc) | Wave-1 complete (167 dosing rules incl. Pass-2 gap-fill: ampicillin, MDR-TB, neonatal antiepileptics, paediatric cardiology) | `paediatric-dosing/` |
| 6 | UCUM units of measure (canonical + conversions) | Wave-1 complete (95 UOMs + 72 conversion edges; 0 cross-cohort orphans) | `ucum/` |
| 7 | Holiday calendars (UG/KE/TZ/RW/CD/NG, 5-year window) | Wave-1 complete (380 holiday rows × 6 countries × 5 years) | `holiday-calendars/` |
| ext | Country-packs full extension (TZ/RW/CD/NG) | in progress (4 parallel sub-agents dispatched 2026-05-04) | `country-packs/` |
| confirm | Specimen/container coverage in lab-tests | confirmed: PHII-19 specimen_type/container/volume_min populated across all 4 wave files (sample audit 2026-05-04); see EVIDENCE-AUDIT.md | `lab-tests/` |

**Definition of done per cohort:** Wave-1 markdown data + findings, gap-marked, sources-tiered, cross-links to existing cohorts noted, EVIDENCE-AUDIT.md updated for any discipline patches. Word/Excel deliverables follow in Phase 8 (enriched-report extension of `scripts/generate_healthcare_app_clinical_data_outputs.py`).

**Resumption anchor for Phase 7:** read this section + `docs/plans/2026-05-04-automated-onboarding-plan.md` Section A1, then dispatch sub-agents per the Phase A task numbering.

## Phase 7 — Wave-3 completion summary (2026-05-04)

All 7 new cohorts at or above Wave-1 floor. `_registry/sources.bib` grew from 2,262 → ~3,300 lines (~1,030 new lines / ~150 BibTeX entries across all cohorts). Country-packs extension (A1.9) launched as 4 parallel sub-agents — TZ/RW/CD/NG full packs being appended to `country-packs/research/wave1-data.md`.

**Self-audit results (orchestrator spot-check 2026-05-04):**
- Wikipedia discipline: zero hits in any data table cell across all 7 cohorts (the only `wikipedia` strings in the corpus are inside self-audit checklist text in vaccines/data, drug-interactions/data; both in meta-footer not citations).
- BibTeX append: enforced; two cohorts (paediatric-dosing pass-1, allergens pass-1) initially wrote stray `.bib` files which were merged into `sources.bib` by the orchestrator and removed.
- Two row-count shortfalls flagged and gap-filled in same session: vaccines (22→48), drug-interactions (52→17,304), paediatric-dosing (120→167), BOMs (73→85).

**Drug-interactions caveat:** 17,252 of the 17,304 pairs use placeholder text `[DDInter — see dataset for mechanism narrative]` for mechanism / consequence / management / monitoring columns. This is per-brief — the agent was authorised to use faithful dataset pointers rather than fabricate narratives. Backfilling these to human-readable strings is Wave-2 work; until then, Medic8 CDS must dereference DDInter v2 at query time.
## Phase 8 - One-hour onboarding promise hardening (added 2026-05-06)

**Goal:** harden every cohort against the Medic8 marketing promise that a supported facility can be onboarded and start using the product in one hour or less, with every preconfigurable default already preconfigured.

**Output added:** `04-synthesis/wave8-one-hour-onboarding-hardening.md`

**Conclusion:** conditional yes, not unconditional. The claim is defensible only for a pre-qualified facility that has supplied non-guessable inputs before kickoff, selects a supported country pack and tenant blueprint, and accepts Medic8 starter catalogues with review-level edits. It is not defensible for brownfield migration, uncleansed opening balances, unresolved licence evidence, unsupplied staff lists, missing bank/payment details, or custom insurer tariffs.

**Main app-facing blocker found from `C:\wamp64\www\Medic8`:**
- Current onboarding code registers steps 1, 2, 3, 5, 6, 7, 8, 13, 15, and 17.
- Steps 4, 9, 10, 11, 12, 14, 16, 18, and 19 remain deferred in `src/Onboarding/Services/Steps/StepRegistry.php`.
- Therefore, the research corpus is strong enough to support the promise, but the promise is not product-proven until a provisioner/importer covers the deferred domains or the screens ship.

**All-cohort hardening requirement:** convert the corpus from research artifacts into importable setup defaults:
- `tenant-blueprints`: machine-readable setup scripts.
- `country-packs`: fail-closed country selectors for stubs.
- `facilities`, `roles-permissions`, `workflows`: direct wizard/importer mappings.
- clinical cohorts (`conditions`, `drugs`, `lab-tests`, `imaging`, `procedures`, `consumables`, `boms`, `vaccines`, `allergens`, `paediatric-dosing`, `drug-interactions`, `ucum`): blueprint-specific starter subsets plus go-live blocker checks.
- operational cohorts (`billing-tariffs`, `standard-forms`, `reporting-kpis`, `holiday-calendars`): preloaded defaults plus explicit facility-confirmation fields.

**Verification update:** archive capture was rerun in small batches on 2026-05-06. 9 of 11 web sources now have Wayback archive URLs recorded in `04-synthesis/wave8-source-archive-manifest.md`. Tanzania HFR and Kenya MFL docs were live on 2026-05-06 but resisted automated Wayback capture; they remain explicit final-export exceptions.

**Next work:** build or specify the Medic8 provisioning runner, then run timer-based acceptance tests for all six canonical blueprints.

## Phase 9 - Closeout deliverables for development/database handoff (added 2026-05-06)

**Output family:** `05-output/medic8-global-settings/`

**Purpose:** regenerate Word and Excel artifacts as a v2 closeout package that clearly defines global defaults, standards, import targets, facility-confirmation boundaries, curator worklists, and source/gap discipline for Medic8 development and database teams.

**Artifacts:** per-cohort DOCX/XLSX files for all active cohorts, plus `medic8-global-defaults-master-v2-2026-05-06.docx`, `medic8-global-defaults-import-workbook-v2-2026-05-06.xlsx`, and `manifest.md`.

**Handoff rule:** these files define staging/default candidates. Development must preserve source/gap fields, fail closed for stubs/placeholders, and require curator sign-off before production activation.

**Regeneration verification (2026-05-06):** regenerated after parser hardening for blank-separated continuation tables. Final package includes 45 DOCX/XLSX/manifest files in `05-output/medic8-global-settings/` and mirrored in `export/medic8-global-settings/`. Holiday calendars now parse all 380 source rows; consumables now parse 327 source rows. `python -m engine validate healthcare-app-clinical-data` passes GATE-01 through GATE-09.

**LOINC table/value-set addendum (2026-05-06):** added `04-synthesis/loinc-tables-valuesets-output-conformance-2026-05-06.md` and `05-output/medic8-global-settings/loinc-tables-valuesets-output-conformance-v2-2026-05-06.xlsx` for database-team use. This narrower addendum intentionally excludes access mechanisms and focuses on importable tables, value sets, and output conformance rules: 25 required tables, 11 value-set/canonical universes, and 15 acceptance rules for FHIR/HL7-compatible observation, panel, document, answer, unit, and diagnostic-report output.

**All-cohort standards repopulation (2026-05-06):** added `04-synthesis/standards-repopulation-manifest-2026-05-06.md` and `05-output/medic8-global-settings/medic8-all-cohorts-standards-repopulated-v3-2026-05-06.xlsx`. The workbook repopulates all 20,501 parsed cohort rows into a standards-shaped import model with primary code system URI, primary code, value-set URI, FHIR/resource target, output rule, alternate coding JSON, source file, conformance status, blocker flag, and facility-confirmation boundary. Source research tables were not overwritten; any row without enough evidence remains flagged for curator mapping.

## Phase 10 - v3 implementation package from implementation-team brief (added 2026-05-06)

**Canonical brief:** `01-initiation/medic8-global-defaults-v3-brief.md`

**Output family:** `05-output/medic8-global-settings-v3/`, mirrored to `export/medic8-global-settings-v3/`

**Purpose:** implement the v3 deliverable contract without breaking the v2 workbook layout. The package adds v3 columns/sheets/artifacts, machine-readable worklists, fixtures, translations worklist, cross-reference scan, change log, and acceptance report.

**Artifacts generated:** 141 files total in both output and export trees, including:
- 21 existing-cohort DOCX files and 21 existing-cohort XLSX files named `medic8-global-defaults-<cohort>-v3-2026-05-06.*`
- 21 `curator-worklist-<cohort>-v3-2026-05-06.json` files
- 12 new-cohort skeleton XLSX files for cohorts 22-33
- `cross-references.json`
- 60 synthetic fixture JSON files under `fixtures/`
- `translations/translation-worklist-v3-2026-05-06.json`
- `change-log-v2-to-v3-2026-05-06.md`
- `change-log-v2-to-v3-2026-05-06.xlsx`
- `acceptance-report-v3-2026-05-06.md`
- `manifest-v3-2026-05-06.md`

**Implemented transformations:** v3 generator adds non-breaking columns, DDI narrative-quality scoring, row-level curator priorities, roles `Permission Grant Matrix`, source/version/licence placeholder columns, per-cohort curator JSON, cross-reference scan, synthetic blueprint fixtures, translation worklist, and v2-to-v3 change log.

**Acceptance result:** Office ZIP integrity PASS; schema generation PASS; no-guesswork gate PASS. P0 curator queue FAIL by design until source verification clears 800 source-blocked P0 rows. Cross-reference resolution FAIL until unresolved reference tokens are mapped or corrected. `python -m engine validate healthcare-app-clinical-data` passes GATE-01 through GATE-09.

**No-guesswork rule:** v3 artifacts intentionally retain `[P0 GAP - v3 source verification required]` / `[GAP - v3 research required]` where the implementation brief asks for legal, clinical, tariff, licence, translation, or external standard facts not already supported by the source corpus.

### Phase 10 P0 overlay integration update (2026-05-06)

**Sub-agent wave:** completed P0 research sessions for country-packs, drug-interactions, drugs, imaging, lab-tests, billing-tariffs, and roles-permissions. Outputs were embedded into the v3 package as source-backed workbook overlay sheets; keyed rows were promoted only where row keys or country codes matched safely.

**Regenerated output:** `scripts/generate_medic8_v3_artifacts.py` now emits 142 files in `05-output/medic8-global-settings-v3/` and mirrors 142 files to `export/medic8-global-settings-v3/`. The transfer archive is `export/medic8-global-settings-v3-2026-05-06.zip`.

**Integrated P0 evidence:** 31 source-backed research sheets embedded. Promoted rows: drug-interactions 6, imaging 50, drugs 63, billing-tariffs 62 new tariff rows, country-packs 10 country activation overlays. Roles-permissions includes the 28-role x 50-permission `Permission Grant Matrix`.

**Acceptance result after overlay integration:** Office ZIP integrity PASS; schema generation PASS; P0 research overlay integration PASS; no-guesswork gate PASS. P0 curator queue remains FAIL with 904 source-blocked items and cross-reference resolution remains FAIL with 3,189 unresolved reference tokens. This is the correct fail-closed handoff state: implementation can build import, schema, curator, and acceptance-test tooling from the artifacts, but Medic8 must not activate unresolved P0 rows as go-live global settings.

**Validation:** `python -m engine validate healthcare-app-clinical-data` passes GATE-01 through GATE-09 after the integrated rebuild.
