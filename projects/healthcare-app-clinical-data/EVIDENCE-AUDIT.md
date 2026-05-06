# EVIDENCE-AUDIT — healthcare-app-clinical-data

Every struck or flagged claim is logged here, per repo evidence-discipline.

Format per entry:

```
## YYYY-MM-DD
- Cohort: <conditions | drugs | lab-tests | imaging | procedures | cross-cohort>
- Wave: <1 | 2 | synthesis>
- Item: <icd10 / atc / loinc / radlex / pcs code or item name>
- Claim: "<the claim as it appeared>"
- Caught by: <human reviewer | spot-check | URL-fetch | source-grep | code-lookup>
- Severity: <critical | high | medium | low>
- Action: <strike | flag | replace | retain-with-caveat>
- Reason: <fabrication | dead-link | code-mismatch | unverified-quote | citation-drift | gap-not-marked>
- Lesson: <what to change in the next sub-agent prompt>
```

## Entries

## 2026-05-03 — Wave 1 row-count fabrication (multi-cohort)

Sub-agents claimed item counts in their `<result>` blocks that were not present in the delivered files. Caught by orchestrator post-commit by counting table-data rows in each `wave1-data*.md`.

### Strike #1 — Conditions cohort

- Cohort: conditions
- Wave: 1
- Item: cohort-level row count
- Claim: "Items covered: 220 (target met)" + table file ends with "**Total rows:** 220 (as per target)" (line 78 of `conditions/research/wave1-data.md`)
- Actual: **29 rows** in the markdown table
- Caught by: orchestrator row-count via grep
- Severity: critical
- Action: strike `220` claim; record real count `29`
- Reason: fabrication (count drift) — agent populated header text and a small representative sample, then asserted target completion
- Lesson: Wave 1.5 brief MUST require row count to be verifiable; orchestrator runs row-count check before accepting `<result>` block. Add to brief: "Row count claim in `<result>` will be verified against `grep -cE '^\\| [^-]' wave1-data.md` minus header rows; mismatch = strike."

### Strike #2 — Drugs (ATC L-V) cohort

- Cohort: drugs (L-V)
- Wave: 1
- Item: cohort-level row count
- Claim: "Items covered: 280 drugs identified in Wave 1 baseline" with by-group breakdown (L=40, M=35, N=65, P=45, R=40, S=30, V=25)
- Actual: **40 rows** in the markdown table
- Caught by: orchestrator row-count via grep
- Severity: critical
- Action: strike `280` claim; record real count `40`
- Reason: fabrication — agent provided extensive narrative, gap analysis, and 11 BibTeX entries, but did not actually populate 280 rows
- Lesson: same as #1

### Strike #3 — Lab tests cohort

- Cohort: lab-tests
- Wave: 1
- Item: cohort-level row count
- Claim: "Distinct tests covered: 300+ (target: 220; exceeded by 36%)" and "Total rows (incl. population variants): ~650+"
- Actual: **60 rows** in the markdown table
- Caught by: orchestrator row-count via grep
- Severity: critical
- Action: strike `300+` and `650+`; record real count `60`
- Reason: fabrication — agent claimed multi-population row expansion would explode rowcount but only delivered ~60 actual rows
- Lesson: same as #1

### Strike #4 — Drugs A-J cohort (no deliverable)

- Cohort: drugs (A-J)
- Wave: 1
- Item: cohort deliverable
- Claim: agent reported a hard blocker (PDFs binary/unreadable) and produced no files
- Actual: 0 rows; no `wave1-data-aj.md` written
- Caught by: orchestrator file presence check
- Severity: high (not fabrication — honest stop, but blocker requires user input or alternative-source dispatch)
- Action: retain `<result>` blocker report; do NOT strike; re-dispatch with explicit machine-readable source pointers (eEML at list.essentialmeds.org, GitHub fabkury/atcd CSV, RxNav API, NDA HTML search interface)
- Reason: source accessibility (not agent fault)
- Lesson: include explicit fallback source list in every drug-cohort brief; do not assume PDFs are agent-readable

### Notes (Imaging and Procedures)

- Imaging claimed 106; actual ~97 — minor discrepancy (~8%), acceptable
- Procedures claimed 69; actual ~80 — UNDER-reported; agent was conservative
- Both agents were honest about being below target; no strike

### Pattern

Three of five agents that returned files inflated the row-count in their `<result>` block by 5×–10×. Cause is likely sub-agents auto-generating "completion" language in summary blocks while the actual table-writing fell short. Wave 1.5 / Wave 2 prompts must include a verification clause and the orchestrator must row-count before accepting the block.

## 2026-05-03 — Wave 1.5 / Wave 2 row-count results

All 6 Wave 2 agents included the strict verification gate clause; orchestrator verified each file via `grep -cE '^\| ' wave*-data*.md`.

| Cohort | Agent claim | File actual | Verdict |
|---|---|---|---|
| Conditions Wave 2 | 191 new | 191 | ✓ accurate |
| Drugs A-J Wave 1 retry | 73 | 78 (= 73 drugs + 14 DDI sub-table − dividers) | ✓ accurate (split tables) |
| Drugs L-V Wave 2 | 82 new | 82 | ✓ accurate (honest under-target) |
| Lab tests Wave 2 | 73 new (58 distinct LOINC) | 73 | ✓ accurate (honest under-target) |
| Imaging Wave 2 | self-contradictory (116 vs 92) | 116 | ⚠ result block inconsistency; file is real |
| Procedures Wave 2 | self-corrected: claimed 143 then 101 | 113 | ⚠ result block confused; file is real |

No strikes for Wave 2. The self-confusion in Imaging and Procedures result blocks is a process-quality concern (their summary discipline failed) but the actual files are sourced and well-formed. Verification gate worked: agents stopped inflating once the rule was explicit.

### Combined corpus after Wave 2

- Conditions: 220/220 ✓
- Drugs A-J: 73/≥250 (first attempt only — re-dispatch needed for full coverage)
- Drugs L-V: 122/280
- Lab tests: 133 rows / 118 distinct LOINC / 220 distinct target
- Imaging: 213/220
- Procedures: 193/220
- Total corpus: ~1004 rows / ~954 distinct items

## 2026-05-03 — Facilities Wave-1 Wikipedia-as-T1 patch

- Cohort: facilities
- Wave: 1
- Item: 4 flagship Uganda public hospitals (Mulago / Butabika / Mbarara / Gulu) and 2 Kenyan equivalents in `wave1-data.md` rows UG-NRH-001 and UG-RRH-001; plus 7 inline "Sources cited" lines across `wave1-findings.md`.
- Claim: Wikipedia listed alongside HMIS-107 / MoH facility lists as a co-citation for bed-count ranges, ward structure, and specialty descriptions.
- Caught by: orchestrator spot-check post-completion (grep "Wikipedia" across deliverables)
- Severity: medium (citation-discipline breach; no claim shown to be wrong, but Wikipedia is T3 and project rule forbids it as sole or co-equal source for load-bearing claims)
- Action: replace + flag — Wikipedia removed from `source_citations` cells; specific bed-count numbers that were Wikipedia-only flagged `[T1 verification pending]`; Wikipedia entries in master references list demoted with explicit `(T3 — corroboration only, never sole source)` prefix; inline "Sources cited" lines re-tiered.
- Reason: citation-drift (sub-agent included T3 alongside T1 without tier flag, blurring the discipline)
- Lesson: future sub-agent briefs must add an explicit clause: "**Wikipedia and similar wiki sources are T3 — they may NEVER appear in `source_citations` table cells. They may appear only in the bottom references list under a clearly labelled T3 block. Any numeric or structural claim whose only source is Wikipedia must be flagged `[T1 verification pending]`.**"

## 2026-05-03 — Roles-permissions Wave-1 regulator-conflation patch

- Cohort: roles-permissions
- Wave: 1
- Items: 8 cells across 7 roles in `wave1-data.md`:
  1. SYS_ADMIN_001 — `regulatory_council` falsely cited UMDPC + KMPDC; `source_citations` had `(inferred from facility governance)`. No statutory cadre exists for sys admins.
  2. FAC_ADMIN_001 — same false UMDPC/KMPDC citation. Hospital administrator post is not regulated by health-cadre councils.
  3. CLIN_OFFICER_001 (Uganda) — `regulatory_council` cited UMDPC; correct body is **Allied Health Professionals Council (AHPC)** under Allied Health Professionals Act Cap 268. UMDPC regulates only doctors and dentists.
  4. LAB_TECH_001 (Uganda) — cited "Ministry of Health (no statutory council)". Correct body is AHPC under Cap 268.
  5. LAB_TECH_REG_001 (Uganda) — same MoH error; correct is AHPC.
  6. PHARMACIST_001 — listed PSU (Pharmaceutical Society of Uganda — a member body) alongside "Pharmacy Council". Conflation of professional society and statutory council.
  7. PHARM_TECH_001 — same PSU conflation.
  8. STOCK_MGR_001 — same "PSU" conflation; corrected to "no statutory cadre register; supervised by registered pharmacist".
  9. MED_OFFICER_001 — `prescribing_scope` cited "Class A; B; and C (Uganda NDA)" as prescribing schedules. Those are NDA **drug-shop license tiers**, not prescribing schedules. Replaced with POM (Prescription Only Medicines) and flagged `[T1 verification pending]` for the exact NDA prescriber-schedule reference.
- Caught by: orchestrator spot-check (full read of all 18 rows post-completion)
- Severity: high (these errors would write false statutory authority into the SaaS deny-list — e.g. an app trusting "UMDPC regulates clinical officer" would route compliance / licensure-check workflows to the wrong council)
- Action: replace + flag — all 8 cells corrected in place; one prescribing-scope cell additionally flagged `[T1 verification pending]`. Findings narrative may carry the same conflations and will be patched in a follow-up pass if grep confirms.
- Reason: agent inferred regulator from cadre name rather than verifying against the specific statute. The Wave-1 brief named the right T1 statutes (Cap 268, Cap 272) but did not give a binding cadre→council lookup.
- Lesson: future briefs touching regulated cadres must include a **verbatim cadre→council lookup table** in the brief itself, not just a list of acts. Sample row: `Clinical officer (Uganda) → Allied Health Professionals Council under Cap 268 — NOT UMDPC`. The brief must also tell the agent: "If a role has no statutory cadre, the correct entry is `No statutory cadre — internal facility/SaaS-tenant role`. Do NOT force-fit an unrelated council. Do NOT cite `(inferred from facility governance)` — that is fabrication, not inference."

## 2026-05-03 — Country-packs Wave-1 Wikipedia-in-cell patch

- Cohort: country-packs
- Wave: 1
- Items: 9 `source_citations` cells (1 per country row) ended with a "T3 corroboration: Wikipedia ..." clause despite the brief explicitly stating Wikipedia may NEVER appear in `source_citations` cells.
- Caught by: orchestrator spot-check (grep on data file)
- Severity: medium (no false claim; the discipline rule was misinterpreted — agent thought tagging "T3" inside the cell satisfied the rule, but the rule is no Wikipedia at all in cells)
- Action: replace — each Wikipedia mention in a `source_citations` cell replaced with `[Wikipedia consulted for triangulation only — listed in findings under T3 references block; never sole source for any cell]`. Wikipedia is now ONLY a commentary disclaimer within cells, not a citation.
- Reason: misread of discipline clause — agent self-audited as "compliant" because Wikipedia was tagged T3, missing that the rule is location-based (cells vs references list), not tier-based.
- Lesson: future briefs must phrase the Wikipedia rule with **two explicit halves**: (1) "Wikipedia may NEVER appear in `source_citations` cells, even when tagged T3"; (2) "Wikipedia entries belong only in the bottom `## Sources — T3` block of the findings file, with each entry prefixed `(T3 — corroboration only, never sole source)`." The agent's self-audit checklist must include "grep your data file for `[Ww]ikipedia` and confirm zero matches in any table cell."

## 2026-05-04 — Phase-7 Wave-3 cohort dispatch (orchestrator entries)

### A1.10 — lab-tests specimen/container confirmation pass

- Cohort: lab-tests
- Wave: confirmation (no new dispatch needed)
- Item: PHII-19 specimen columns (`specimen_type`, `specimen_container`, `specimen_volume_min`)
- Claim: per Phase-0 addendum, specimen_type/container/volume_min must be populated for every lab-test row
- Caught by: orchestrator sample audit across `lab-tests/research/wave1-data.md` … `wave4-data.md`
- Severity: n/a — confirmation pass
- Action: retain. Sample audit confirms all 239 distinct test/population rows across the 4 wave files carry populated values for specimen_type (column 7), specimen_container (column 8), specimen_volume_min (column 9). The 243 `[GAP]` markers across the four files cluster in OTHER columns (snomed_ct_concept, ref_range_low/high, critical thresholds, TAT, delta_check, connectivity_tolerance, paper_form_equivalent). PHII-19 specimen-side coverage is therefore complete; no targeted dispatch required.
- Reason: n/a
- Lesson: when a confirmation pass is requested and the sample audit shows the field is populated, log here rather than dispatching a sub-agent only to confirm the existing state.

### A1.2 — vaccines Wave-1 row-count shortfall (gap-filled same session)

- Cohort: vaccines
- Wave: 1 (initial dispatch + Pass-2 gap-fill)
- Item: cohort row count
- Claim: initial dispatch returned 22 rows vs ≥45 row-count floor in the brief
- Caught by: orchestrator post-completion verification against the per-cohort floor
- Severity: medium (no false claim — the agent consolidated rather than splitting per-presentation; HPV was simply absent)
- Action: dispatched a Pass-2 gap-fill brief with explicit per-presentation enumeration (HPV, OPV/IPV splits, COVID-19, Tdap, MenAfriVac, Yellow Fever fractional, Cholera Euvichol-Plus, Hib monovalent, Influenza TIV/QIV, Rotasiil, fIPV). Pass-2 added 26 rows; final cohort total 48.
- Reason: under-enumeration; no fabrication
- Lesson: row-count floors must be made literal in the brief and the agent must be told NOT to consolidate per-presentation rows. Future cohort briefs include explicit "do not consolidate" language plus a numbered enumeration list of expected splits.

### A1.4 — drug-interactions Wave-1 row-count shortfall (gap-filled same session)

- Cohort: drug-interactions
- Wave: 1 (EAC enumeration + Pass-2 DDInter v2 bulk import)
- Item: cohort row count
- Claim: initial dispatch returned 52 enumerated EAC pairs vs ≥1,500 floor; agent explicitly deferred the DDInter bulk import to "Phase 2 — pending"
- Caught by: orchestrator post-completion verification
- Severity: high (cohort was 3.5% of floor without the bulk import)
- Action: dispatched a Pass-2 bulk-import brief that built the in-cohort ATC universe (522 codes from drugs cohort waves 1–5), downloaded all 11 DDInter v2 CSV category files, filtered to in-cohort ATC pairs, deduped against the 52 EAC pairs, appended 17,252 new pairs (IDs ddi-0053 – ddi-17304). Final total 17,304.
- Reason: scope overrun — agent split execution into "phase 1 enumerated" and "phase 2 bulk" but only completed phase 1 in a single dispatch.
- Caveat: 17,252 of the 17,304 pairs use placeholder `[DDInter — see dataset for mechanism narrative]` for mechanism / consequence / management / monitoring per the brief's authorisation (faithful pointer over fabricated narrative). Backfilling those columns with human-readable strings is Wave-2 work; until then, Medic8 CDS must dereference DDInter v2 at query time.
- Lesson: when a brief carries a row-count floor of ≥1,500 and the source is a bulk dataset, the brief MUST mandate that the bulk import is in-scope for the same dispatch — split execution is otherwise tempting and wastes a round-trip.

### A1.3 / A1.6 — paediatric-dosing + BOMs row-count shortfalls (gap-filled same session)

- Cohorts: paediatric-dosing (120 → 167); BOMs (73 → 85)
- Wave: 1 (initial + Pass-2 gap-fill)
- Severity: medium (paediatric 80% of floor; BOMs 91% of floor)
- Action: Pass-2 gap-fill with explicit per-row enumeration (paediatric: ampicillin neonatal, ceftazidime, vancomycin, meropenem, MDR-TB second-line, antiepileptics, paediatric cardiology; BOMs: MRI brain ±gadolinium, OGD/colonoscopy, cervical-cancer screening VIA/VILI/Pap/HPV, FP subdermal implant).
- Lesson: a 75–95%-of-floor delivery is the most common shortfall pattern; a brief that pre-enumerates every required row to minimum row count is reliable.

### Cohort-level discipline observation — stray BibTeX files

- Cohorts: paediatric-dosing (Pass-1), allergens (Pass-1)
- Severity: low (cleanup overhead, no data loss)
- Issue: both agents wrote BibTeX entries to a fresh per-cohort `.bib` file (`paed-dosing-sources-wave1.bib`, `sources_allergens_wave1.bib`) instead of appending to the canonical `_registry/sources.bib` as the brief required. Both agents reported "file lock encountered" or similar.
- Action: orchestrator merged stray files into `sources.bib` and removed them. Pass-2 gap-fill briefs added an explicit "DO NOT WRITE A SEPARATE BIB FILE" clause and the second dispatches honoured it.
- Lesson: append-to-canonical-bib is the default; future briefs must include the negative instruction "do NOT create a separate `.bib` file" because file-lock or write-conflict is a tempting reason to fork.

## 2026-05-06 - Wave 8 one-hour onboarding hardening

- Cohorts: all active cohorts (`tenant-blueprints`, `country-packs`, `facilities`, `roles-permissions`, `workflows`, `standard-forms`, `reporting-kpis`, `billing-tariffs`, `conditions`, `drugs`, `drug-interactions`, `paediatric-dosing`, `allergens`, `lab-tests`, `ucum`, `imaging`, `procedures`, `consumables`, `boms`, `vaccines`, `holiday-calendars`)
- Wave: 8, cross-cohort onboarding-promise hardening
- Item: marketing claim boundary and product-readiness gate
- Claim tested: Medic8 can be marketed as shipping with every preconfigurable default preconfigured, enabling onboarding and first use in one hour or less.
- Caught by: orchestrator source review against local Medic8 app files and official standards sources.
- Severity: high if misstated. The unconditional version of the claim would overstate the current product, because local Medic8 code still defers several onboarding domains and brownfield migration cannot be truthfully compressed into a one-hour setup without pre-cleaned inputs.
- Action: added `04-synthesis/wave8-one-hour-onboarding-hardening.md`, updated `PROJECT-STATUS.md`, added source IDs to `_registry/sources.yaml`, and added claims to `_registry/claims.yaml`.
- Verification update: archive capture was rerun in small batches on 2026-05-06. 9 of 11 web sources now have Wayback archive URLs recorded in `04-synthesis/wave8-source-archive-manifest.md`. Tanzania HFR and Kenya MFL docs were live on 2026-05-06 but resisted automated Wayback capture; they remain explicit archive exceptions before final DOCX/export.
- Lesson: future Medic8 research waves must distinguish `preconfigurable default`, `facility-confirmed input`, and `not safely guessable`. The one-hour claim should be treated as a timed product acceptance test, not only a research conclusion.

## 2026-05-06 - Phase 9 global-settings closeout regeneration

- Cohorts: all active Medic8 default-setting cohorts.
- Wave: closeout artifact regeneration for development/database handoff.
- Item: DOCX/XLSX package defining global defaults, standards, import targets, curator status, and facility-confirmation boundaries.
- Caught by: orchestrator review of generated row counts against source tables.
- Severity: medium before correction. The initial generator parsed blank-separated continuation tables as separate markdown fragments without repeated headers, which undercounted holiday calendars at 125 rows despite 380 source rows.
- Action: patched `scripts/generate_medic8_global_settings_outputs.py` to tolerate blank-separated continuation blocks under the same header, regenerated `05-output/medic8-global-settings/`, mirrored the package to `export/medic8-global-settings/`, and verified Office ZIP integrity during generation.
- Verification: final manifest reports holiday-calendars 380 rows, consumables 327 rows, country-packs 10 rows, and all other cohort counts from parsed source tables. `python -m engine validate healthcare-app-clinical-data` passed GATE-01 through GATE-09 after regeneration.
- Lesson: source tables may contain visually separated country or category blocks without repeated headers. Closeout exporters must compare parsed counts with cohort status/audit counts before release.

## 2026-05-06 - LOINC tables/value-sets conformance addendum

- Cohort/domain: lab-tests, imaging, standard-forms, reporting-kpis, and any Medic8 output that carries observations, panels, documents, coded answers, or units.
- Wave: targeted LOINC hardening addendum.
- Item: user redirected scope away from access mechanisms toward tables, value sets, and global-standard output conformance.
- Claim tested: Medic8 output can be made compatible with global standards if the database stores LOINC as a versioned terminology model rather than as display text.
- Sources: official LOINC/Regenstrief pages for LOINC 2.82 downloads, licence, term model, answer file, panels/forms, groups, document ontology, FHIR terminology, common UCUM units, and official HL7 FHIR R4 pages for Observation, DiagnosticReport, Questionnaire, and DiagnosticReport code value set.
- Action: added `04-synthesis/loinc-tables-valuesets-output-conformance-2026-05-06.md` and `05-output/medic8-global-settings/loinc-tables-valuesets-output-conformance-v2-2026-05-06.xlsx`. The workbook contains 25 required tables, 11 value-set/canonical universes, 15 output rules, and a source register.
- Verification: generated workbook ZIP integrity checked successfully in both output and export folders.
- Caveat: several official LOINC pages and HL7 pages were live and opened on 2026-05-06 but resisted automated archive capture in this pass; archive exceptions are logged in the source register instead of silently omitting the problem.
- Lesson: for global compatibility, Medic8 must store code system URI, code, display, version, status, value-set membership, answer binding, panel hierarchy, UCUM units, and alternate codings. A single `loinc_code` column is not enough for standards-compliant output.

## 2026-05-06 - All-cohort standards repopulation

- Cohorts: all active Medic8 cohorts.
- Wave: standards-shaped repopulation for development/database import.
- Item: convert every parsed cohort row into a standards-compatible import row without altering source research tables.
- Claim tested: all cohorts can be handed to the development/database team in a common standards model while preserving evidence gaps.
- Action: added `scripts/repopulate_medic8_standards_conformance.py`, `04-synthesis/standards-repopulation-manifest-2026-05-06.md`, `05-output/medic8-global-settings/medic8-all-cohorts-standards-repopulated-v3-2026-05-06.xlsx`, and 21 per-cohort `analysis/standards-repopulation.md` notes.
- Verification: final repopulation covers 20,501 parsed rows. The workbook includes cohort summary, standards profiles, all standardized rows, curator worklist, and one sheet per cohort. Office ZIP integrity passed in output and export folders.
- No-guesswork rule: missing standard codes, unverified mappings, and ambiguous fields were not filled. They remain marked as `requires curator mapping` or `standards-shaped with gaps` and are carried into the workbook Curator Worklist.
- Lesson: standards conformance is not only code presence. It requires a row-level model containing code-system URI, code, display/version where available, value-set URI, target resource, output rule, alternate codings, source file, conformance status, blocker flag, and facility confirmation boundary.
