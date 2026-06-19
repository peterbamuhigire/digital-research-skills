# srs-skills-completion-2026 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce `srs-skills-completion-2026-v1.docx` — 17 Depth-2 implementation specs that the srs-skills dev team executes to close Stages 1–3 of the 2026-04-12 remediation roadmap, projecting 8.1 → ~9.0 / 10.

**Architecture:** Research-orchestration project under `digital-research-skills/projects/`. Five waves: scaffold (W0), four parallel cohort agents (W1), verification (W2), cross-cohort synthesis (W3), Word doc assembly (W4). Mirrors `webdevskills-engine-completion-2026` structure exactly.

**Tech Stack:** Markdown corpus → `professional-word-output` skill → `.docx`. Sub-agents via `Agent` tool with `subagent_type: content-marketing:search-specialist` (fallback `general-purpose`), `run_in_background: true`. Evidence discipline enforced via verbatim hard-constraint clause from `skills/source-evaluation/references/evidence-discipline.md`.

**Spec source:** `docs/superpowers/specs/2026-05-01-srs-skills-completion-design.md`

---

## Wave 0 — Scaffold and Context

### Task 0.1: Scaffold project tree

**Files:**
- Create: `projects/srs-skills-completion-2026/README.md`
- Create: `projects/srs-skills-completion-2026/CLAUDE.md`
- Create: `projects/srs-skills-completion-2026/PROJECT-STATUS.md`
- Create: `projects/srs-skills-completion-2026/EVIDENCE-AUDIT.md`
- Create: empty dirs `_context/`, `00-front-matter/`, `01-stage1-proof-restoration/specs/`, `02-stage2-skill-normalization/specs/`, `03-stage3a-academiapro-design/specs/`, `04-stage3b-academiapro-release/specs/`, `export/`

- [ ] **Step 1: Create directory tree**

```bash
mkdir -p projects/srs-skills-completion-2026/{_context,00-front-matter,01-stage1-proof-restoration/specs,02-stage2-skill-normalization/specs,03-stage3a-academiapro-design/specs,04-stage3b-academiapro-release/specs,export}
```

- [ ] **Step 2: Write `README.md`** — purpose (single Word doc, 17 Depth-2 specs, Stages 1–3 only), final deliverable path, spec inventory grouped by cohort, hard exclusions list (Stages 4–6, no srs-skills repo edits, no score promise above 9.1/10), source-document pointers, status pointers.

- [ ] **Step 3: Write `CLAUDE.md`** — model on the reference project's `CLAUDE.md`. Include: workflow phase definition (W0–W4); hard rules (verbatim evidence-discipline clause in every brief, append-don't-overwrite, gap-marking discipline, no deletion of sourced claims without `EVIDENCE-AUDIT.md` log); where things live (front matter, cohort specs, sources, verification logs, export).

- [ ] **Step 4: Write `PROJECT-STATUS.md`** — wave checklist with 17 spec slots, all unchecked.

- [ ] **Step 5: Write empty `EVIDENCE-AUDIT.md`** — header only ("# Evidence Audit Log — srs-skills-completion-2026"; columns: date, cohort, spec, claim, source-status, action).

- [ ] **Step 6: Commit**

```bash
git add projects/srs-skills-completion-2026/
git commit -m "scaffold: srs-skills-completion-2026 project tree"
```

### Task 0.2: Author `_context/` files

**Files:**
- Create: `_context/gap-analysis.md` (verbatim concatenation of the 9 evaluation files)
- Create: `_context/design-spec.md` (copy of approved design spec)
- Create: `_context/implementation-plan.md` (this plan)
- Create: `_context/per-spec-template.md`
- Create: `_context/agent-brief-template.md`
- Create: `_context/scope-exclusions.md`
- Create: `_context/scoring-ceiling.md`

- [ ] **Step 1: Concatenate evaluation into `gap-analysis.md`**

Read all 9 files in `C:\wamp64\www\srs-skills\docs\evaluation\2026-04-12\` (executive-summary, gap-analysis, phase-by-phase-analysis, recommendations, remediation-roadmap, scoring, suggested-reading, system-reconstruction, world-class-definition). Concatenate with `## Source: <filename>` separators. This is the canonical reference for every cohort agent.

- [ ] **Step 2: Copy design spec**

Copy `docs/superpowers/specs/2026-05-01-srs-skills-completion-design.md` content into `_context/design-spec.md`.

- [ ] **Step 3: Copy this plan**

Copy this plan into `_context/implementation-plan.md`.

- [ ] **Step 4: Author `per-spec-template.md`**

Adapt the reference project's template to remediation-spec context. Sections: 1) Metadata (spec id, stage, cohort, target dimension(s), severity), 2) Scope (in/out, dependencies on other specs), 3) Outcomes (5–8 testable outcomes), 4) Deliverable shape (concrete files, paths, formats), 5) Source mapping (which 2026-04-12 finding(s), which standards clauses), 6) Implementation steps for the dev team (numbered, concrete), 7) Acceptance criteria (checkbox, command-verifiable where possible), 8) Anti-patterns (what failure looks like), 9) Verification commands, 10) Owner notes / open questions.

- [ ] **Step 5: Author `agent-brief-template.md`**

Adapt the reference brief template. Mandatory sections: verbatim evidence-discipline clause, goal (N specs for cohort X), Depth-2 definition, per-spec template (verbatim), spec list with placeholders, sources discipline (29119/27001/ITIL/NIST clause numbers must be real and verifiable; URLs WebFetched and dated; AcademiaPro claims must match repo content), verbatim hard exclusions, deliverables (specs + sources.md + verification-log.md), process (read gap-analysis section, plan outline, mine sources, write spec, never placeholder), result format (≤300-word summary), prohibitions (no fabrication, no scope creep, no other-cohort dirs).

- [ ] **Step 6: Author `scope-exclusions.md`**

Verbatim list, identical wording in every cohort brief:
1. Stages 4–6 of the remediation roadmap (traceability schema, runtime evidence ingestion, semantic correctness, AI hallucination scoring) — not in scope.
2. New skills outside the existing 240 in the catalog — not in scope.
3. Direct edits to `C:\wamp64\www\srs-skills\` — this deliverable is spec-only.
4. Cost estimates, vendor selection, hiring plans — not in scope.
5. Score promises above 9.1/10 — the ceiling is honest.
6. No fabricated standards clauses, URLs, statistics, or AcademiaPro repo facts.
7. No content older than 2024 unless the gap analysis explicitly cites it.

- [ ] **Step 7: Author `scoring-ceiling.md`**

The per-dimension projection table from §2 of the design spec, plus narrative on why Stages 4–6 are needed for 9.5+, plus the explicit "no spec promises >9.1" rule.

- [ ] **Step 8: Commit**

```bash
git add projects/srs-skills-completion-2026/_context/
git commit -m "context: author _context/ files for srs-skills-completion-2026"
```

### Task 0.3: Author `00-front-matter/` files

**Files:**
- Create: `00-front-matter/exec-summary.md`
- Create: `00-front-matter/evaluation-baseline.md`
- Create: `00-front-matter/remediation-thesis.md`
- Create: `00-front-matter/cross-reference-matrix.md` (skeleton; populated in W3)

- [ ] **Step 1: Author `exec-summary.md`**

~2 pages. Sections: Purpose (close Stages 1–3 gaps from 2026-04-12 evaluation), Current state (8.1/10), Projected state after execution (~8.9–9.1/10 with per-dimension table), Honest ceiling (Stages 4–6 needed for 9.5+; explicit statement that this deliverable does not promise 9.9), Spec inventory (17 specs, 4 cohorts), How to read this document (cohort order = stage order = recommended execution order), Hand-off (deliverable is spec-only; srs-skills dev team executes).

- [ ] **Step 2: Author `evaluation-baseline.md`**

~3 pages. Condensed reproduction of the 2026-04-12 findings: scoring table, key strengths (5 bullets), critical weaknesses (6 bullets verbatim), high-severity gaps (4), medium-severity gaps (5). Cite every claim back to its source file in `_context/gap-analysis.md`.

- [ ] **Step 3: Author `remediation-thesis.md`**

~2 pages. Why Stages 1–3 first (reproducibility before depth); why this order (proof restoration unblocks Stage 2 validators which unblock Stage 3 project validation); what we deliberately defer (Stages 4–6) and why (multi-quarter R&D, not "completion").

- [ ] **Step 4: Author `cross-reference-matrix.md` skeleton**

Header only: a markdown table with columns `Spec ID | Cohort | Stage | Primary Score Dimension | Secondary Dimensions | Source Finding | Standards Clause(s) | Acceptance-Criteria Count`. Populate in Wave 3.

- [ ] **Step 5: Commit**

```bash
git add projects/srs-skills-completion-2026/00-front-matter/
git commit -m "front-matter: author exec-summary, baseline, thesis, matrix skeleton"
```

---

## Wave 1 — Cohort Agent Dispatch

### Task 1.1: Build the four cohort briefs

**Files:**
- Create: `_context/scripts/cohort-01-brief.md` (Stage 1: Proof Restoration, 4 specs)
- Create: `_context/scripts/cohort-02-brief.md` (Stage 2: Skill Normalization, 5 specs)
- Create: `_context/scripts/cohort-03-brief.md` (Stage 3a: AcademiaPro Design, 4 specs)
- Create: `_context/scripts/cohort-04-brief.md` (Stage 3b: AcademiaPro Release, 4 specs)

- [ ] **Step 1: Create scripts dir**

```bash
mkdir -p projects/srs-skills-completion-2026/_context/scripts
```

- [ ] **Step 2: Author Cohort 01 brief**

Substitute into the agent-brief template:
- `<COHORT-NAME>` = "Stage 1: Proof Restoration"
- `<COHORT-DIR>` = `01-stage1-proof-restoration`
- `<COHORT-SPEC-COUNT>` = 4
- `<COHORT-SPECS-LIST>` = the 4 specs from §4 of the design (01-demo-workspace-restoration, 02-engine-suite-green-up, 03-dev-environment-bootstrap, 04-readme-proof-claims-rewrite), each with: themes (e.g., for spec 01: what artifacts `_demo-hybrid-regulated` needs, fixture vs committed strategy, what `engine/tests/test_cli_sabotage.py` checks), source-mining hints (2026-04-12 evaluation sections, `srs-skills/engine/tests/`, `srs-skills/README.md`, pytest docs, `srs-skills/scripts/validate_engine.py`), acceptance hooks (which engine commands must pass, what coverage % is honest).

- [ ] **Step 3: Author Cohort 02 brief**

Same pattern. Cohort 02 = Stage 2 Skill Normalization, 5 specs (05–09). Source-mining hints: `srs-skills/skills/` tree, the 15 failing skills (exact IDs from quick-validator output — agent must run validator first to enumerate), AGENTS.md path drift, contract-gate output, Anthropic skills docs, OpenAI Codex agent docs.

- [ ] **Step 4: Author Cohort 03 brief**

Cohort 03 = Stage 3a AcademiaPro Design, 4 specs (10–13). Critical: the agent must read `C:\wamp64\www\srs-skills\projects\AcademiaPro\` to ground specs in actual repo state, not invented context. Source-mining hints: existing AcademiaPro files, ISO/IEC/IEEE 42010 (architecture descriptions), STRIDE/LINDDUN canonical refs, Google Engineering Practices, Atlassian/GitLab contribution-guide patterns.

- [ ] **Step 5: Author Cohort 04 brief**

Cohort 04 = Stage 3b AcademiaPro Release, 4 specs (14–17). Source-mining hints: ISO/IEC/IEEE 29119 parts 1–5 (clause numbers verifiable), ITIL 4 deployment/change/incident, Google SRE workbook (SLO/runbook patterns), ISO 27001:2022 Annex A control evidence patterns, the engine's existing `engine pack` and evidence-pack code in `srs-skills/engine/`.

- [ ] **Step 6: Commit**

```bash
git add projects/srs-skills-completion-2026/_context/scripts/
git commit -m "wave-1: author 4 cohort dispatch briefs"
```

### Task 1.2: Dispatch all four cohorts in parallel

- [ ] **Step 1: Single message, four parallel `Agent` calls**

All four use `subagent_type: content-marketing:search-specialist` (fallback `general-purpose`), `run_in_background: true`. Each `prompt` is the full content of the corresponding `cohort-NN-brief.md` (self-contained — sub-agents have no parent context).

- [ ] **Step 2: Record dispatch**

Update `PROJECT-STATUS.md`: mark Wave 1 in-progress, list 4 agent IDs returned by the tool, expected completion ~45–90 min.

- [ ] **Step 3: Do not poll**

Per CLAUDE.md: never tail sub-agent transcripts via Bash. Wait for completion notifications.

### Task 1.3: Read each cohort's `<result>` block on completion

- [ ] **Step 1: For each completed cohort**

Read the structured `<result>` block (≤300 words). Note: specs produced, source counts by tier, anything struck for evidence-discipline reasons, gap-analysis items not addressed.

- [ ] **Step 2: Verify files on disk**

```bash
ls projects/srs-skills-completion-2026/<cohort-dir>/specs/
```

Confirm spec count matches the brief. Flag missing specs as Wave-2 blockers.

- [ ] **Step 3: Update `PROJECT-STATUS.md`**

Mark each cohort complete with file count and any reported gaps.

- [ ] **Step 4: Commit each cohort's output**

```bash
git add projects/srs-skills-completion-2026/<cohort-dir>/
git commit -m "wave-1: <cohort-dir> specs delivered"
```

---

## Wave 2 — Verification

### Task 2.1: Spot-check evidence discipline per cohort

For each of the 4 cohorts:

- [ ] **Step 1: Sample 10% of statistics and standards-clause citations**

For each cohort with ~4–5 specs and (estimate) 30–60 citations, sample 4–6 random citations. WebFetch every cited URL. For 29119/27001/ITIL/NIST clause references, confirm clause number exists in the standard.

- [ ] **Step 2: AcademiaPro repo grounding (Cohorts 03 + 04 only)**

For every Cohort 03/04 spec claim about AcademiaPro's current state, verify against `C:\wamp64\www\srs-skills\projects\AcademiaPro\`. Examples: "AcademiaPro currently lacks ADRs" — confirm by listing the directory. Strike any claim contradicted by the repo.

- [ ] **Step 3: Append findings**

For each cohort, append a `# Pass 2 — Gap-fill addendum` section to affected specs. Do not overwrite. Log every strike to `EVIDENCE-AUDIT.md`.

- [ ] **Step 4: Commit per-cohort verification**

```bash
git add projects/srs-skills-completion-2026/<cohort-dir>/ projects/srs-skills-completion-2026/EVIDENCE-AUDIT.md
git commit -m "wave-2: <cohort-dir> verification + pass-2 addenda"
```

### Task 2.2: Re-dispatch gap-fill if any cohort had >2 strikes

- [ ] **Step 1: Decision rule**

If a cohort had more than 2 evidence-discipline strikes OR more than one missing spec, dispatch a focused gap-fill agent for that cohort only. Brief: "Re-do specs X and Y; here are the strikes; here are the additional sources to mine; same evidence-discipline clause."

- [ ] **Step 2: Otherwise skip to Wave 3.**

---

## Wave 3 — Cross-Cohort Synthesis (orchestrator only — never delegated)

### Task 3.1: Populate cross-reference matrix

- [ ] **Step 1: For each of the 17 specs**

Read the spec, extract: cohort, stage, primary score dimension affected, secondary dimensions, source finding(s) from the 2026-04-12 evaluation, standards clauses cited, count of acceptance criteria.

- [ ] **Step 2: Write the populated matrix**

Replace the skeleton in `00-front-matter/cross-reference-matrix.md` with the full table.

### Task 3.2: Cross-cohort consistency check

- [ ] **Step 1: Canonical skill path**

Cohort 02 spec `05-canonical-skill-path-decision` chooses `skills/<name>` or `skills/skills/<name>`. Confirm Cohorts 03–04 specs reference skill paths consistent with that choice. If not, append a `# Pass 2 — Gap-fill addendum` to each affected spec stating the canonical path.

- [ ] **Step 2: Acceptance-criteria language**

Confirm every spec's acceptance criteria are verifiable by command, file presence, or `engine validate` output — not by narrative review alone. Flag any "vibe" criteria for repair.

- [ ] **Step 3: Score-ceiling reconciliation**

Tally the dimensions touched by the 17 specs. Confirm projection in `scoring-ceiling.md` matches what the specs actually deliver. Adjust the projection downward (never upward) if cohort output is thinner than expected.

### Task 3.3: Append synthesis findings

- [ ] **Step 1: Write `00-front-matter/synthesis-notes.md`**

~1 page. What we found across cohorts: shared dependencies, sequencing constraints (e.g., spec 05 must complete before specs 10–17 reference paths), risks the dev team should know about.

- [ ] **Step 2: Commit**

```bash
git add projects/srs-skills-completion-2026/00-front-matter/ projects/srs-skills-completion-2026/EVIDENCE-AUDIT.md
git commit -m "wave-3: cross-cohort synthesis"
```

---

## Wave 4 — Word Document Assembly

### Task 4.1: Build the assembly manifest

**Files:**
- Create: `_context/assembly-manifest.md`

- [ ] **Step 1: Author manifest**

Document order:
1. Cover page (title, date, author, version 1, target repo, source evaluation)
2. Executive summary (`00-front-matter/exec-summary.md`)
3. Evaluation baseline (`00-front-matter/evaluation-baseline.md`)
4. Remediation thesis (`00-front-matter/remediation-thesis.md`)
5. Score ceiling (`_context/scoring-ceiling.md`)
6. Cohort 01 — 4 specs in numerical order
7. Cohort 02 — 5 specs in numerical order
8. Cohort 03 — 4 specs in numerical order
9. Cohort 04 — 4 specs in numerical order
10. Cross-reference matrix (`00-front-matter/cross-reference-matrix.md`)
11. Synthesis notes (`00-front-matter/synthesis-notes.md`)
12. Hard exclusions (`_context/scope-exclusions.md`)
13. Appendix A — Sources by cohort (concatenate the 4 `sources.md`)
14. Appendix B — Verification log (concatenate the 4 `verification-log.md`)
15. Appendix C — Evidence audit (`EVIDENCE-AUDIT.md`)

For each entry: heading level, page break before/after, table-of-contents inclusion.

- [ ] **Step 2: Commit**

```bash
git add projects/srs-skills-completion-2026/_context/assembly-manifest.md
git commit -m "wave-4: assembly manifest"
```

### Task 4.2: Generate `.docx`

- [ ] **Step 1: Invoke `professional-word-output` skill**

Pass the assembly manifest. Target: `projects/srs-skills-completion-2026/export/srs-skills-completion-2026-v1.docx`. Style: professional report, TOC, page numbers, headers/footers per the skill's defaults.

- [ ] **Step 2: Spot-check the .docx**

Open and confirm: TOC populates, every spec appears, page count is in the 170–200 range, no markdown leakage, tables render.

- [ ] **Step 3: Commit**

```bash
git add projects/srs-skills-completion-2026/export/srs-skills-completion-2026-v1.docx
git commit -m "deliverable: srs-skills-completion-2026 v1 .docx"
```

### Task 4.3: Hand-off

- [ ] **Step 1: Copy to subject repo**

```bash
mkdir -p "C:/wamp64/www/srs-skills/docs/completion-2026"
cp projects/srs-skills-completion-2026/export/srs-skills-completion-2026-v1.docx "C:/wamp64/www/srs-skills/docs/completion-2026/"
```

- [ ] **Step 2: Update `PROJECT-STATUS.md` to Complete**

- [ ] **Step 3: Final commit**

```bash
git add projects/srs-skills-completion-2026/PROJECT-STATUS.md
git commit -m "complete: srs-skills-completion-2026 delivered"
```

---

## Self-Review Notes

- Spec coverage: every section of the design spec maps to a task — §3 layout (T0.1), §4 spec inventory (T1.1), §5 wave plan (W0–W4), §6 exclusions (T0.2 step 6, embedded in every brief at T1.1), §7 evidence discipline (verbatim clause in every brief at T1.1, verification at W2), §8 deliverable (T4.2–4.3).
- Placeholders: none — every step lists the actual content to write or command to run.
- Type consistency: cohort directory names are consistent across all tasks (`01-stage1-proof-restoration`, `02-stage2-skill-normalization`, `03-stage3a-academiapro-design`, `04-stage3b-academiapro-release`).
- Note: this is research orchestration, not TDD code; steps are scaffold + dispatch + verify actions, not red-green-refactor cycles. That's appropriate for the deliverable.
