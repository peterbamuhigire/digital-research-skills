# Healthcare App Clinical Data Corpus — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Produce five sourced clinical-data cohorts (conditions, drugs, lab tests, imaging, procedures) for a Uganda-focused healthcare management app, each delivered as a `.docx` report + `.xlsx` data sheet, plus a cross-cohort master doc.

**Architecture:** Multi-wave research orchestration. Orchestrator (this session) scaffolds the project, dispatches parallel research sub-agents per cohort, runs QA loops with WebFetch verification, then assembles deliverables via document-generation skills. Project lives under `projects/healthcare-app-clinical-data/`. Append-only writes; every struck claim logged in `EVIDENCE-AUDIT.md`.

**Tech Stack / skills used:** `Agent` tool (sub-agent dispatch), `WebFetch` (verification), `source-evaluation` skill (evidence discipline), `gap-analysis`, `critical-reasoning-and-argument`, `cross-cohort-synthesis`, `professional-word-output`, `document-skills:xlsx`. No code is written; "tests" here are evidence-verification gates.

**Reference:** Design doc → `docs/plans/2026-05-03-healthcare-clinical-data-design.md`. Project CLAUDE.md governs all sub-agent dispatch. The verbatim hard-constraint clause from `skills/source-evaluation/references/evidence-discipline.md` MUST appear in every sub-agent brief.

---

## Phase 0 — Scaffold

### Task 0.1: Create directory tree

**Files (create empty):**
- `projects/healthcare-app-clinical-data/conditions/research/.gitkeep`
- `projects/healthcare-app-clinical-data/conditions/analysis/.gitkeep`
- `projects/healthcare-app-clinical-data/conditions/opportunities/.gitkeep`
- (repeat for `drugs/`, `lab-tests/`, `imaging/`, `procedures/`)
- `projects/healthcare-app-clinical-data/_context/.gitkeep`
- `projects/healthcare-app-clinical-data/_registry/.gitkeep`
- `projects/healthcare-app-clinical-data/export/.gitkeep`

**Step 1:** Use Bash `mkdir -p` to create all directories in one command.

**Step 2:** Verify with `ls projects/healthcare-app-clinical-data/`.

Expected: 5 cohort dirs + `_context`, `_registry`, `export`.

---

### Task 0.2: Write project README

**File:** `projects/healthcare-app-clinical-data/README.md`

**Content:** project name, client (internal team), goal, five cohorts table, geography (Uganda + Kenya + Tanzania), ranking basis (IHME GBD), hard exclusions verbatim, hard inclusions, links to design doc and CLAUDE.md.

---

### Task 0.3: Write project CLAUDE.md

**File:** `projects/healthcare-app-clinical-data/CLAUDE.md`

**Content:** sub-agent invariants for this project — verbatim hard-constraint clause, source-tier rules, file-write conventions (append on Wave 2), exclusions, the structured-output format every sub-agent must produce.

---

### Task 0.4: Write PROJECT-STATUS.md

**File:** `projects/healthcare-app-clinical-data/PROJECT-STATUS.md`

**Content:** wave tracker table — Phase 0/1/2/3/4/5 × cohort columns × status. Resumption anchor for multi-session work.

---

### Task 0.5: Write EVIDENCE-AUDIT.md skeleton

**File:** `projects/healthcare-app-clinical-data/EVIDENCE-AUDIT.md`

**Content:** header + empty table (cohort | item | claim | reason struck | wave | date).

---

### Task 0.6: Write `_context/coding-standards-master.md`

**File:** `projects/healthcare-app-clinical-data/_context/coding-standards-master.md`

**Content:** Reference doc explaining ICD-10, ATC, LOINC, RadLex, ICD-10-PCS, CDT, ICHI. What each is, who maintains it, how it's structured, how it's used in the app context. This text is reused (transcluded) into every cohort's Word report §1.

---

### Task 0.7: Write `_context/source-tiers.md`, `geographic-scope.md`, `exclusions.md`, `client-brief.md`

Four small files capturing the per-cohort T1/T2/T3 source lists (from design §5), the three-country triangulation rule, the verbatim exclusions list, and the client/team context.

---

### Task 0.8: Initialise `_registry/sources.bib`

**File:** `projects/healthcare-app-clinical-data/_registry/sources.bib`

**Content:** BibTeX header comment + a starter set of T1 sources for each cohort (WHO ICD-10, IHME GBD 2021, Uganda Clinical Guidelines, WHO EML 23rd, Uganda EMHSLU, LOINC, RadLex, ICD-10-PCS, CDT 2024). Future entries appended by sub-agents and the orchestrator during QA.

---

### Task 0.9: Commit Phase 0

```
git add projects/healthcare-app-clinical-data/
git commit -m "Scaffold healthcare-app-clinical-data project"
```

**Verification gate:** `python -m engine doctor` runs clean (per project kernel workflow). If the engine flags any missing kernel files, fix before proceeding.

---

## Phase 1 — Wave 1 Research (parallel sub-agents, background)

### Task 1.1: Draft sub-agent brief template

**File (orchestrator scratch, not committed):** Internal template containing every required clause:

1. **Goal block** — cohort, minimum item count, deliverable shape
2. **Scope** — geography (UG primary; KE+TZ triangulation), population scope, hard exclusions verbatim
3. **Coding standard** — which standard, with link to `_context/coding-standards-master.md` (the agent should read this)
4. **Data model** — full column list from design §4
5. **Source tiers** — T1/T2/T3 lists from design §5, with instruction "T1 must be cited; T2 may corroborate; T3 never sole source"
6. **Verbatim hard-constraint clause** from `skills/source-evaluation/references/evidence-discipline.md`
7. **Output paths** — `<cohort>/research/wave1-findings.md` (narrative + categorisation analysis) AND `<cohort>/research/wave1-data.md` (markdown table matching the data model)
8. **Gap-marking rule** — "any field without a sourced answer must be marked `[GAP — no source found]`. Do not fabricate."
9. **Source bibliography** — agent appends new sources to `_registry/sources.bib` with access date
10. **Reporting back** — completion `<result>` block must summarise: items covered, items gap-marked, sources used by tier, any blockers

---

### Task 1.2: Dispatch Wave 1 — 6 parallel agents

Single message with 6 `Agent` tool calls (`run_in_background: true`):

- **Agent 1** — Conditions cohort (target 220, ICD-10)
- **Agent 2** — Drugs cohort, ATC A–J (Alimentary, Blood, Cardio, Dermatologicals, GU/sex hormones, Systemic hormones, Antiinfectives)
- **Agent 3** — Drugs cohort, ATC L–V (Antineoplastics, Musculoskeletal, Nervous, Antiparasitics, Respiratory, Sensory, Various)
- **Agent 4** — Lab tests cohort (target 220, LOINC)
- **Agent 5** — Imaging cohort (target 220, LOINC + RadLex)
- **Agent 6** — Procedures cohort (target 220, ICD-10-PCS + CDT for dental)

Each agent uses `subagent_type: content-marketing:search-specialist` (fallback `general-purpose`).

**Verification gate:** All 6 background tasks return `<result>` blocks. Read each block, do NOT shell-tail the markdown files. Record completion in `PROJECT-STATUS.md`.

---

### Task 1.3: Commit Wave 1 outputs

```
git add projects/healthcare-app-clinical-data/
git commit -m "Wave 1 research dispatched and returned for all 5 cohorts"
```

---

## Phase 2 — QA Loop (orchestrator, per cohort, sequential)

For each of the 5 cohorts, perform the following 7-step verification before moving to the next cohort:

### Task 2.x.1: Read the cohort's `wave1-data.md` and `wave1-findings.md`

Use `Read` tool. Note item count, gap-marked count, sources cited.

### Task 2.x.2: Spot-check 10% of items via WebFetch

Pick random 10% of items. For each: WebFetch the cited source URL. Verify the code, the value, and the categorisation match.

### Task 2.x.3: Verify all coding-standard codes (sample)

For each cohort: pick 20 codes at random, verify against the official lookup (e.g., LOINC website for labs, WHO ICD-10 browser for conditions, WHO ATC index for drugs).

### Task 2.x.4: Verify regulation/statute citations (every one)

For drugs: every NDA/PPB/TMDA registration claim must be verified or marked `[unverified — agent could not access register]`.

### Task 2.x.5: Run `gap-analysis` skill

Does the cohort hit minimum count with sourced items? Are categories balanced? Are any obvious priority items missing?

### Task 2.x.6: Strike-and-log

Anything failing verification: row removed from `wave1-data.md`; entry written to `EVIDENCE-AUDIT.md` with reason.

### Task 2.x.7: Compute Wave-2 brief for this cohort

Specific gap list: which items, which fields, which sources to chase.

### Task 2.x.8: Commit per-cohort QA

```
git add projects/healthcare-app-clinical-data/<cohort>/
git add projects/healthcare-app-clinical-data/EVIDENCE-AUDIT.md
git add projects/healthcare-app-clinical-data/PROJECT-STATUS.md
git commit -m "Phase 2 QA: <cohort> — N items struck, gap-fill brief drafted"
```

Repeat for each cohort. Update `PROJECT-STATUS.md` after each.

---

## Phase 3 — Wave 2 Gap-Fill

### Task 3.1: Dispatch Wave 2 — only for cohorts with gaps

Sub-agents briefed on the **specific gap list** from Phase 2. Outputs append (do not overwrite) using `# Pass 2 — Gap-fill addendum` header in `<cohort>/research/wave1-findings.md` and `<cohort>/research/wave1-data.md`.

### Task 3.2: Re-run condensed QA on Wave-2 additions only

Steps from Phase 2 applied to the addendum content only.

### Task 3.3: Commit Wave 2

```
git add projects/healthcare-app-clinical-data/
git commit -m "Wave 2 gap-fill complete; QA pass on addendum content"
```

---

## Phase 4 — Critical Reasoning + Cross-Cohort Synthesis

### Task 4.1: Per-cohort critical-reasoning pass

Use `skills/critical-reasoning-and-argument/SKILL.md`. For each cohort's analysis section: are claims warranted by cited GBD data? Categorisation defensible? Any business-sense / app-utility checks?

Output: `<cohort>/analysis/critical-reasoning-notes.md`.

### Task 4.2: Cross-cohort synthesis (orchestrator-only, never delegated)

Use `cross-cohort-synthesis` skill.

**File:** `projects/healthcare-app-clinical-data/00-cross-cohort-master.md`

**Content:**
- Condition ↔ drug ↔ lab ↔ imaging ↔ procedure clusters (e.g., malaria → antimalarials → mRDT/microscopy → no imaging → no procedure; obstructed labour → oxytocin/MgSO4 → coag profile + group-and-save → obstetric US → C-section)
- Corpus-level coverage gaps
- App-implementation notes (data-model decisions the team needs to make)

### Task 4.3: Commit Phase 4

```
git add projects/healthcare-app-clinical-data/
git commit -m "Phase 4: critical reasoning + cross-cohort synthesis"
```

---

## Phase 5 — Deliverable Assembly

For each of the 5 cohorts, produce one Word doc + one Excel file. Then the cross-cohort master.

### Task 5.x.1: Generate `0X-<cohort>-data.xlsx`

Use `document-skills:xlsx` skill. Sheets:
- `data` — every column from data model, every kept item
- `categories` — pivot/lookup of grouping values
- `sources` — bibliography (filtered from `_registry/sources.bib` to this cohort)
- `audit` — items struck during QA with reasons (filtered from `EVIDENCE-AUDIT.md`)
- `readme` — column dictionary

Output: `projects/healthcare-app-clinical-data/export/0X-<cohort>-data.xlsx`

### Task 5.x.2: Generate `0X-<cohort>-report.docx`

Use `professional-word-output` skill. Structure:
- Cover + executive summary
- §1 Coding standard explained (transcluded from `_context/coding-standards-master.md`, filtered to this cohort's standard)
- §2 Methodology (geography, ranking basis, sources, exclusions)
- §3 Categorised list with commentary per category
- §4 Gaps and limitations
- §5 App-implementation notes
- Appendix A: full data table
- Appendix B: bibliography by tier

Output: `projects/healthcare-app-clinical-data/export/0X-<cohort>-report.docx`

### Task 5.x.3: Verification gate per cohort

- Open `.xlsx` row count ≥ minimum target
- Open `.docx`, confirm appendix table renders, confirm bibliography is non-empty, spot-check formatting
- Tick cohort off in `PROJECT-STATUS.md`

### Task 5.x.4: Commit per cohort

```
git add projects/healthcare-app-clinical-data/export/0X-*
git add projects/healthcare-app-clinical-data/PROJECT-STATUS.md
git commit -m "Phase 5: <cohort> deliverables generated"
```

Repeat for all 5 cohorts.

### Task 5.6: Generate `00-cross-cohort-master.docx`

From `00-cross-cohort-master.md` via `professional-word-output`.

### Task 5.7: Final commit + handoff

```
git add projects/healthcare-app-clinical-data/
git commit -m "Healthcare-app-clinical-data: corpus complete"
```

Update `PROJECT-STATUS.md` to "complete." Optional kernel commands per project CLAUDE.md:
- `python -m engine validate healthcare-app-clinical-data`
- `python -m engine pack healthcare-app-clinical-data --out export/healthcare-app-clinical-data.zip`

---

## Verification gates summary

| Phase | Gate |
|---|---|
| 0 | Directory tree exists; engine doctor clean (if applicable) |
| 1 | All 6 sub-agent `<result>` blocks received; item counts ≥ targets |
| 2 | 10% spot-check passes; codes verified; gap-fill briefs drafted |
| 3 | Wave-2 additions QA-passed; minimum item counts hit after strikes |
| 4 | Cross-cohort master doc identifies linkage clusters and gaps |
| 5 | All 6 `.docx` + 5 `.xlsx` files exist in `export/` and open cleanly; row counts hit minimums |

---

## Resumption rules (multi-session)

`PROJECT-STATUS.md` is the single source of truth. On a new session: read it first, find the last completed task, resume from the next.

Never re-dispatch a Wave-1 agent for a cohort that completed — use Wave-2 with explicit gap briefs instead. Never overwrite committed research files; append.

---

## Next step

Plan complete and saved to `docs/plans/2026-05-03-healthcare-clinical-data-plan.md`. Two execution options:

**1. Subagent-Driven (this session)** — I dispatch fresh subagent per task, review between tasks, fast iteration.

**2. Parallel Session (separate)** — Open new session with `superpowers:executing-plans`, batch execution with checkpoints.

Given the scale (multi-hour, multi-session, lots of WebFetch) and that this is research orchestration rather than code, I recommend **option 1 in this session for Phase 0** (the scaffold is small and quick), then on your call we either continue here or hand Phase 1+ to a parallel session. Confirm.
