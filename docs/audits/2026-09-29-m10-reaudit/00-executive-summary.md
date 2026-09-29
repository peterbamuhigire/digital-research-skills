# 00 Executive summary

**Scores:** raw 51.6, measured-constrained 51.6, published 51.6 out of 100.
Engine Eval Readiness 57.5 out of 100.
**Bar:** top intelligence-shop or peer-reviewed research practice (the rubric's apex for a
research engine).
**Auditor:** an independent re-auditor who did not execute any my-10-kaizen phase.
The audit was read-only at HEAD `2b9c87d` on 29 September 2026.

## Verdict

The Digital Research Engine has a defensible and unusually candid evidence doctrine. Its main
rules are these:

- No claim ships without a source.
- Missing evidence is `NOT_ASSESSED`, never a pass.
- Currentness is recorded as data.

It also has a working Python layer: a verifier, a citation-density dashboard, dataset tools and
sanctions tests. The engine's own validators pass locally, as does a 171-test pytest suite.

The overall score still lands at 51.6 because the skill layer and its applied proof are thin
against the bar. The engine explains well what a verified fact brief, an OSINT dossier or a
legal memorandum must contain. It rarely shows one.

## Headline findings

1. **Remote CI is red at HEAD, and the local T1 pass depends on the host.** GitHub Actions run
   `36520107821` ("Skill engine quality") fails with `broken_relative_link: 2` ("fully compliant: 57").
   The same validator reports 59/59 locally. Both links point to
   `../../../chwezi-dev-engine/references/ai-slop-responsible-publishing-standard-2026-09-11.md`:
   - `skills/ai-slop-audit/SKILL.md:146`
   - `skills/anti-ai-slop/SKILL.md:129`

   Those links resolve only where a sibling checkout exists. The measured T1 = 1.0 is therefore
   true on this workstation and false in clean CI.
2. **Applied proof is the weakest dimension (36/100).**
   - In 56 of 59 SKILL.md files the "Worked example" section is under 60 words. It is usually one
     sentence of method restated, not an example.
   - `projects/example-due-diligence-dossier`, `example-market-landscape` and
     `example-academic-paper` are kernel fixtures. For example, `sources.yaml` holds one "Fixture
     source" at tier 4, and `assembled.md` has three lines.
   - The two real tracked corpora (`healthcare-app-clinical-data`, `east-africa-property-hostel`)
     date from April and May 2026 and still carry open verification items in `EVIDENCE-AUDIT.md`.
   - Tier 3 behavioural evidence is `NOT_ASSESSED`.
3. **Routing coverage is zero.** 29 positive fixtures cover 28 skills. Five skills have an owned
   negative. No skill has three positives and two owned negatives (T2_cov = 0/59).
   - Precision@1 is 25/29 (lexical proxy).
   - One mirrored cross-engine owned negative, oracle `055-route-release-evidence-mirror`, fails
     at rank 4.
4. **The taxonomy is diluted and carries stale references.**
   - About 14 of 59 skills are engineering, documentation or skill-authoring material, for example
     `spec-architect`, `project-requirements`, `update-claude-documentation`, `capability-matrix`,
     `manual-guide` and `markdown-lint-cleanup`.
   - Three of these duplicate other engines above 0.75 cosine: `validation-contract` 1.0 with dev;
     `ai-slop-audit` 0.826 with dev and 0.790 with srs; `excel-spreadsheets` 0.823 with dev.
   - Companion lists name 52 skills that exist neither as active skills nor as local reference
     files (about 100 mentions). `data-quality-assessment` appears 11 times.
   - Meanwhile, benchmarking and competitive study, an output type the engine claims, has no
     owning skill at all.
5. **Standards currency is partial.**
   - The standards register has eight rows, last verified 2026-07-08.
   - `academic-reporting-standards/SKILL.md:90` still describes TOP as "8 modular standards × 3
     implementation levels". The Center for Open Science now publishes TOP 2025 with seven
     research practices, three implementation levels, two verification practices and four
     verification study types (https://www.cos.io/initiatives/top-guidelines, accessed 2026-09-29).
   - The East African legal overlay names categories only, dated 2026-04-27, with no repository
     access log.
6. **Contract accretion.**
   - 19 skills repeat H2 sections, for example duplicate "Companion Skills", "Workflow",
     "Anti-Patterns" and "Degraded Mode".
   - Many skills carry generated headings such as "Quantitative Modelling Evidence Notes 1/2" and
     "Online Legal Research Fallback Notes".
   - This passes the contract validator but reads as compliance padding and dilutes depth.

## What is strong

- The **evidence doctrine** (`AGENTS.md`, `source-evaluation/references/evidence-discipline.md`,
  `rules/common/core.md`): the verbatim hard-constraint clause, claim-level support states and an
  untrusted-source contract in `source-verification`.
- The **OSINT and due-diligence reference depth**: 11 and 7 reference files, CARA report
  architecture, sanctions-screening discipline, and an explicit refusal list covering doxxing,
  minors, pretexting and state intelligence.
- The **model-policy currentness review** (`docs/continuous-improvement/model-policy-review-gpt6-luna-2026-09-28.md`).
  Each row of its dated source register gives publication date, access date and review date. It
  is the best worked example of the engine's own method.
- **Tooling and tests**: 171 pytest passes, a deterministic source-currency validator and the
  ME1–ME7/AS1–AS7 machine-error gate across 12 engines.

## Movement since prior audits

- 6 September 2026 Kaizen: no numeric score. Its fixes, source-currency validator input hardening and
  portable tests, are confirmed in place: `validate_source_currency.py` exits 0 and pytest passes.
  The test count rose from 115/124 to 171.
- The contract validator still reports 59/59 locally, as it did then. CI has since turned red
  (since at least 25 September).
- The 23 September scraping Kaizen (54.8, scraping-only) is not comparable in scope.
- The April 2026 self-assessment (62 to 65) used a different, self-scored rubric. This audit's
  lower figure reflects the stricter bar and the measured routing constraint, not proven
  regression.

## Path to the bar

- **P0 (hygiene and proof, target about 57):**
  - Fix the two CI links.
  - Replace the one-line worked examples in the ten core research skills with short real
    artefacts.
  - Raise fixture coverage to at least 3+2 for the core routes.
  - Correct the TOP entry.
- **P1 (scope and output owners, target about 62):**
  - Retire or redirect the engineering imports to their canonical dev skills.
  - Add a benchmarking and competitive-study skill and deepen market sizing.
  - Resolve the 52 stale companion names.
- **P2 (behavioural proof, target about 65 published, with raw able to exceed it):**
  - Execute Tier-3 runs and graded reference products for every output type.
  - Add a legal repository access register.
  - Complete the portfolio craft standard's acceptance evidence.
