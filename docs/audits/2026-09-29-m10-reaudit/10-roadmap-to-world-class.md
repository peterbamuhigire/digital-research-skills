# 10 Roadmap to world-class

The baseline is 51.6 published and Readiness 57.5. Targets are believable under the strictness
directive. The published score cannot exceed 65 until the portfolio craft standard's acceptance
evidence exists. Readiness cannot exceed 70 while Tier 3 is unexecuted.

## P0: restore integrity and prove the core (target: published about 57, Readiness about 64)

1. **Turn CI green.** Replace the cross-repository relative links in
   `skills/ai-slop-audit/SKILL.md:146` and `skills/anti-ai-slop/SKILL.md:129` with a canonical
   GitHub URL or an engine-local reference. Replace the absolute `C:/wamp64` paths in:
   - `skill-safety-audit/SKILL.md`
   - `skill-taxonomy-and-routing/SKILL.md`
   - `skill-writing/SKILL.md`
   - `source-evaluation/references/book-driven-source-admission-and-currentness.md`

   Acceptance: GitHub "Skill engine quality" run succeeds, and T1 holds in clean CI.
2. **Real worked examples for the ten core research routes.** Add `examples/` files, each a short,
   complete, synthetic-but-traceable artefact built on `docs/world-class-exemplars/running-example.md`:
   - `source-evaluation`
   - `source-verification`
   - `osint-investigation`
   - `due-diligence`
   - `online-legal-research`
   - `research-orchestration`
   - `academic-reporting-standards`
   - `quantitative-modelling`
   - `analytic-tradecraft`
   - `decision-support-analysis`

   Replace the one-sentence "Worked example" sections with links to these files. Acceptance: each
   example has a source register, claim-support states and a verification record.
3. **Routing fixture coverage.** Extend `tests/skill-engine/routing-fixtures.json` to 3 positives
   and 2 owned negatives for at least the 16 router primaries. Fix the 055 tie by removing or
   pointer-stubbing `validation-contract`. Target T2_cov 16/59 = 0.27 and T2_neg 1.0, giving
   Readiness of about 30 + 40 × (0.90 + 1 + 0.27 + 1) ÷ 4 = 61.7. P1 fixtures take it to about 64.
4. **Correct the TOP entry** in `skills/academic-reporting-standards/SKILL.md:90` and
   `references/equator-decision-tree.md` to the TOP 2025 structure. Add TOP, CONSORT 2025 and
   PRISMA-S rows with access dates to `docs/source-registers/research-standards-register.md`.
5. **De-duplicate sections** in the 19 skills with repeated H2 headings, and collapse the
   generated "… Notes 1/2" headings into the contract sections they repeat. Keep the validator
   green.

## P1: scope and missing owners (target: published about 62, Readiness about 66)

1. **Retire or pointer-stub the imports**, following the `skill-writing` stub pattern:
   - `spec-architect`
   - `project-requirements`
   - `systems-process-requirements`
   - `doc-architect`
   - `update-claude-documentation`
   - `markdown-lint-cleanup`
   - `manual-guide`
   - `capability-matrix`
   - `validation-contract`
   - `skill-safety-audit`

   Record the count change against the "preserve the 59-skill catalogue" rule in `AGENTS.md`,
   with routing justification.
2. **New skill `skills/benchmarking-and-competitive-study/`.** It should cover scope and
   comparator selection, like-for-like normalisation, evidence rules for competitor claims
   (vendor self-assertion is not verification), a scoring frame and sensitivity, and a worked
   matrix.
3. **Harden market evidence.** Add `quantitative-modelling/references/market-sizing-triangulation.md`
   and a worked reconciliation of a top-down and a bottom-up model. Consider a separate
   `market-evidence-and-sizing` route.
4. **Resolve the 52 stale companion names**, including `data-quality-assessment`,
   `due-diligence-framework` and `pearl-growing-iteration`, and add a validator check that fails
   on unresolved backticked skill names in companion lists.
5. **Group index.** Add `skills/GROUPS.md` listing every skill. Correct the README category table
   so it covers all skills.
6. **Legal repository register.** Add `online-legal-research/references/repository-register.md`
   with the URL, coverage, access date and review date per repository (KenyaLaw, ULII, EACJ,
   national gazettes), and extend the overlay to Tanzania and Rwanda at category level.
7. **Personal-data law checklist** for OSINT and due diligence, per jurisdiction, recorded in the
   standards register with dates.

## P2: behavioural proof (target: published 65 capped, with raw able to reach about 66–68)

1. **Execute Tier-3** behavioural runs for this engine's planned cases when spend is authorised.
   Bind grading files to a pinned model and CLI version. Even partial T3 (for example 0.5) lifts
   Readiness by 15 points.
2. **Graded reference products** for all 11 output types, each reviewed by a named human and
   recorded with support states. This is the evidence the published cap and dimension 4 require.
3. **First labelled flywheel cohort** in `evals/seek-research/`, 20–30 real cases with a baseline,
   as the pilot protocol already specifies.
4. **Portfolio craft standard acceptance evidence** for the engine, which removes the 65 cap.
5. **Re-verify the tracked corpora.** Close or formally quarantine the open items in
   `projects/east-africa-property-hostel/EVIDENCE-AUDIT.md` and the healthcare project, so that
   in-repository applied proof meets the engine's own doctrine.

## Phase targets

| Phase | Readiness | Measured-constrained | Published |
|---|---:|---:|---:|
| Baseline (29 Sep 2026) | 57.5 | 51.6 | 51.6 |
| After P0 | about 62–64 | about 57 | about 57 |
| After P1 | about 66 | about 62 | about 62 |
| After P2 (T3 partly executed, craft evidence present) | about 75 | about 66–68 | 65 while the cap applies |
