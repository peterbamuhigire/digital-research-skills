# Kick-Start Prompt — healthcare-app-clinical-data

> **Paste this entire file as the first message in a fresh Claude Code session pointed at `C:\Users\Peter\Documents\Claude Projects\digital-research-engine`.**

---

You are picking up an in-flight research orchestration project. Phase 0 (scaffold + book-derived recommendations) is complete and committed. Your job is to execute Phase 1 (Wave 1 research dispatch) and Phase 2 (QA loop), then stop and report back.

## What this project is

A clinical reference data corpus for a Uganda-targeted healthcare management app. Five cohorts, each delivered as a Word `.docx` report + Excel `.xlsx` data sheet:

| # | Cohort | Min items | Coding standards |
|---|---|---|---|
| 1 | Conditions / diagnoses | 220 (target; ≥200 after QA strikes) | ICD-10 primary; SNOMED CT + ICD-11 candidate as bridge columns |
| 2 | Drugs (full Uganda EMHSLU + WHO EML) | ~700 | ATC primary; RxNorm bridge; INN + 4 locally-registered brands |
| 3 | Lab tests | 220 | LOINC primary; SNOMED CT bridge; PHII-19 LIS columns |
| 4 | Imaging | 220 | LOINC + RadLex; DICOM SR template references |
| 5 | Procedures (incl. dental) | 220 | **ICHI primary**, ICD-10-PCS secondary, CDT for dental |

**Geography:** Uganda primary; Kenya + Tanzania for triangulation.
**Ranking basis:** IHME GBD 2021 + WHO country profiles (DALYs / mortality).
**Population:** all-ages merged with `population` column.
**Hard exclusions:** veterinary, traditional/herbal, cardiothoracic surgery, neurosurgery, transplant.
**Hard inclusions:** dental procedures.

## Read these files first, in this order

1. `CLAUDE.md` (repo root) — engine-wide invariants
2. `skills/source-evaluation/SKILL.md` and `references/evidence-discipline.md` — the verbatim hard-constraint clause goes in every sub-agent brief
3. `projects/healthcare-app-clinical-data/CLAUDE.md` — project invariants
4. `projects/healthcare-app-clinical-data/PROJECT-STATUS.md` — wave tracker; current state
5. `projects/healthcare-app-clinical-data/README.md`
6. `projects/healthcare-app-clinical-data/_context/coding-standards-master.md` — explains every standard used
7. `projects/healthcare-app-clinical-data/_context/source-tiers.md` — T1/T2/T3 per cohort
8. `projects/healthcare-app-clinical-data/_context/geographic-scope.md`
9. `projects/healthcare-app-clinical-data/_context/exclusions.md`
10. `projects/healthcare-app-clinical-data/_context/client-brief.md`
11. **`projects/healthcare-app-clinical-data/_context/book-derived-recommendations.md`** — material data-model changes derived from health-informatics textbooks. **Apply these when drafting Wave 1 briefs.** They supersede the design doc's §4 column lists where they conflict.
12. `projects/healthcare-app-clinical-data/_registry/sources.bib` — starter T1 citations
13. `docs/plans/2026-05-03-healthcare-clinical-data-design.md` — full design (Sections 1–10)
14. `docs/plans/2026-05-03-healthcare-clinical-data-plan.md` — phased implementation plan

## What to do

### Step 1 — Verify scaffold

Run `git log --oneline -5` to confirm the most recent commits include "Scaffold healthcare-app-clinical-data project (Phase 0)". List `projects/healthcare-app-clinical-data/` to confirm 5 cohort dirs, `_context/`, `_registry/`, `export/`. If anything is missing, stop and report.

### Step 2 — Draft the master Wave 1 sub-agent brief template

Compose a self-contained briefing (sub-agents do not see your conversation history). The brief MUST include:

1. **Goal block** — cohort, target item count, deliverable shape (the two output files)
2. **Scope** — Uganda primary, Kenya + Tanzania triangulation; population scope; hard exclusions verbatim from `_context/exclusions.md`
3. **Coding standards used** — link to `_context/coding-standards-master.md` (sub-agent should read it)
4. **Data-model columns** — the full column list for the cohort, **as updated by `_context/book-derived-recommendations.md`** (not the design doc's original §4). For example, the Procedures column list now leads with `ichi_code` not `icd10_pcs_code`. The Lab cohort uses population-keyed row variants. Drugs has structured DDI, ATC-DDD, RxNorm bridge, LASA/tall-man.
5. **Source tiers** — T1/T2/T3 from `_context/source-tiers.md`; instruction "T1 must be cited where applicable; T2 may corroborate; T3 never sole source"
6. **Verbatim hard-constraint clause** from `skills/source-evaluation/references/evidence-discipline.md` (the exact 7-bullet block beginning with "HARD CONSTRAINT — NO HALLUCINATION")
7. **Seven additional clauses from `_context/book-derived-recommendations.md` §6** — version capture, granularity caveat, ATC-DDD + RxNorm, PHII-19, ICHI primary, paediatric separation, level-of-care + cadre
8. **Output paths** — `<cohort>/research/wave1-findings.md` (narrative + categorisation) and `<cohort>/research/wave1-data.md` (markdown table matching the data model)
9. **Gap-marking rule** — "any field without a sourced answer must be marked `[GAP — no source found]`. Do not fabricate."
10. **Bibliography rule** — agent appends new sources to `_registry/sources.bib` with access date
11. **Required `<result>` block content** — items covered, gap-marks, sources used by tier, blockers

Save this template internally; it will be specialised per cohort with the cohort-specific column list.

### Step 3 — Dispatch Wave 1 (six parallel agents in background)

In a single message, dispatch six `Agent` calls with `subagent_type: content-marketing:search-specialist` (fallback `general-purpose`) and `run_in_background: true`:

1. **Conditions** — target 220 items, ICD-10 primary
2. **Drugs (ATC A–J)** — Alimentary, Blood, Cardio, Dermatologicals, GU/sex hormones, Systemic hormones, Antiinfectives. Aim to cover all relevant Uganda EMHSLU drugs falling in these ATC level-1 groups
3. **Drugs (ATC L–V)** — Antineoplastics, Musculoskeletal, Nervous, Antiparasitics, Respiratory, Sensory, Various
4. **Lab tests** — target 220 items, LOINC + PHII-19 columns
5. **Imaging** — target 220 items, LOINC + RadLex + DICOM SR references
6. **Procedures** — target 220 items, ICHI primary, ICD-10-PCS secondary, CDT for dental

Update `PROJECT-STATUS.md` Phase 1 row to `in progress` for each dispatched cohort.

### Step 4 — Monitor and process completions

You will receive notifications as each background agent completes. **Do not poll.** When a `<result>` arrives:

1. Record completion in `PROJECT-STATUS.md`
2. Read the `<result>` block only — do NOT shell-tail the output markdown files (they overflow context). The full files are committed to the project for Phase 5 to use directly.
3. Note any blockers, gap counts, source-tier breakdown
4. Once all 6 are returned, commit: `git add -f projects/healthcare-app-clinical-data/ && git commit -m "Wave 1 research returned for all 5 cohorts"`

### Step 5 — Phase 2 QA loop (one cohort at a time, sequential)

For each cohort, run the 7-step QA from `docs/plans/2026-05-03-healthcare-clinical-data-plan.md` Phase 2:

1. Read the cohort's `wave1-data.md` and `wave1-findings.md` (use `Read` tool, not Bash)
2. Spot-check 10% of items via `WebFetch` — pick random rows, verify cited URL contents match
3. Verify 20 random codes against the official authority for that cohort's primary standard (LOINC website, WHO ICD-10 browser, etc.)
4. Verify every regulation/registration claim where claimed (NDA / PPB / TMDA registrations) — accept `[unverified — agent could not access register]` markings as valid; do not silently strike them
5. Run completeness check — does the cohort hit minimum after struck items? Are categories balanced?
6. Strike-and-log: anything failing verification → row removed from `wave1-data.md`; entry to `EVIDENCE-AUDIT.md` per the format in that file
7. Compute Wave 2 gap-fill brief — list of specific items / fields / sources for the next wave

After each cohort: commit `EVIDENCE-AUDIT.md` and `PROJECT-STATUS.md` updates. Move to next cohort.

### Step 6 — Stop and report

After Phase 2 completes for all 5 cohorts (the drugs cohort = both A–J and L–V agents merged), STOP. Update `PROJECT-STATUS.md` final state. Report back to the user with:

- Phase 1 completion summary (items per cohort, gap-mark counts, source tier breakdown)
- Phase 2 strike summary (rows struck per cohort, top reasons, items below minimum)
- Wave 2 gap-fill briefs ready for dispatch
- Any blockers needing user input before proceeding to Phase 3

Do **not** dispatch Phase 3 (Wave 2 gap-fill) without user sign-off on the Wave 2 briefs.

## Process discipline

- Use the `Skill` tool to invoke `superpowers:using-superpowers` first. Then invoke skills as they apply (`superpowers:subagent-driven-development` is appropriate for this work).
- Track progress with TaskCreate / TaskUpdate.
- The `projects/` directory is gitignored — use `git add -f projects/healthcare-app-clinical-data/` to stage. Local commits only; **never push** projects/ to remote.
- Today's date for file headers and commits: **2026-05-03** (or whatever the current date is when the new session runs — check the system reminder).
- The orchestrator never reads sub-agent output files via Bash tail / cat. Only the `<result>` block. Files are read with the `Read` tool, in chunks, when QA needs them.
- The verbatim hard-constraint anti-hallucination clause is non-negotiable in every brief. Without it, sub-agents will fabricate. Verify it is present before dispatch.
- Append, do not overwrite, when handling Wave 2.

## Phase 0 deliverables already in place (do not recreate)

- `projects/healthcare-app-clinical-data/README.md`
- `projects/healthcare-app-clinical-data/CLAUDE.md`
- `projects/healthcare-app-clinical-data/PROJECT-STATUS.md`
- `projects/healthcare-app-clinical-data/EVIDENCE-AUDIT.md`
- `projects/healthcare-app-clinical-data/_context/` (5 files)
- `projects/healthcare-app-clinical-data/_registry/sources.bib`
- 5 cohort directories with empty `research/`, `analysis/`, `opportunities/` subfolders
- `docs/plans/2026-05-03-healthcare-clinical-data-design.md`
- `docs/plans/2026-05-03-healthcare-clinical-data-plan.md`

## Begin

Start with Step 1.
