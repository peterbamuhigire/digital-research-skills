# 01 Methodology and rubric

## Auditor independence

This audit was performed by an independent auditor who did not plan, execute or review any
my-10-kaizen phase for this engine. Scores are the auditor's own. Prior audit scores were read for
comparison only and were not copied.

## Method

This audit follows `chwezi-dev-engine/skills/sdlc-meta/skill-engine-audit/SKILL.md` and these
references:

- `scoring-rubric.md`, including "Engine Eval Readiness (measured)"
- `eval-readiness-worked-example.md`
- `audit-dimensions.md`
- `report-structure.md`

Steps:

1. **Harness first (SKILL step 0).** The engine's declared validators and its pytest suite were
   run from the engine root with `PYTHONDONTWRITEBYTECODE=1`, and exit codes recorded (see 11).
   Two supplementary read-only gates were also run: `validate_source_currency.py` and
   `validate_machine_error_gate.py`. The portfolio fan-in tool was run in read-only `--json` mode.
2. **Portfolio measured inputs.** Engine Eval Readiness was taken from
   `chwezi-engine-agents/docs/operations/m10-kaizen-evidence/M10-14/eval-readiness.json`. It was
   recomputed from `readiness/t2-inputs.json`, `readiness/tier1-results.json`,
   `readiness/coverage.json` and `readiness/collision-scan.json`. The routing dimension was not
   re-judged for the measured-constrained number.
3. **Remote CI.** `gh run list` and `gh run view --log-failed` were used read-only to confirm the
   red "Skill engine quality" workflow and name the failing links.
4. **Scope.** The auditor read the router (`SKILL.md`), `AGENTS.md`, `CLAUDE.md` (a thin bridge
   importing `AGENTS.md`), `README.md`, `rules/`, the standards register, the running example and
   the example projects.
5. **Sample reading.** 16 SKILL.md files spread across all eight groups were read:
   - Read in full: `source-evaluation`, `source-verification`, `online-legal-research`,
     `osint-investigation`, `quantitative-modelling`, `decision-support-analysis`,
     `calibration-and-forecasting`.
   - Read in substantial part: `research-orchestration`, `due-diligence`,
     `ai-evaluation-and-data-flywheel`, `academic-reporting-standards`,
     `dataset-discovery-and-analysis`.
   - Frontmatter and key sections only: `validation-contract`, `capability-matrix`,
     `update-claude-documentation`, `skill-safety-audit`, `spec-architect`,
     `project-requirements`.

   Selected references were also read, such as the East African legal overlay.
6. **Whole-catalogue scans.** Small read-only scripts, held in the auditor's scratchpad and not
   in the repository, counted the following for all 59 skills:
   - SKILL.md length, reference-file counts and worked-example word counts
   - duplicate H2 headings and generated "… Notes/Guidance/Detail" headings
   - companion-list skill names that resolve to neither an active skill nor a local reference file

   These scans are heuristics. Their counts are stated as such.
7. **External currency check.** One claim was checked against a primary source (TOP Guidelines,
   Center for Open Science). The standards-currency dimension is otherwise "judged from the
   engine's own currentness records (no fresh external research)".

## Documented limitation: no parallel fleet

The skill prescribes a parallel fleet of audit agents. In this re-audit the fleet was replaced by
the single auditor working through each concern in turn: standards, existing skills, taxonomy,
output readiness and hardening. Independence between concerns is therefore weaker than the method
intends. The reading list and full standards benchmark were not re-run.

## Rubric

The bands follow `scoring-rubric.md`:

| Band | Meaning |
|---|---|
| 90–100 | Rivals the field's best |
| 75–89 | Excellent professional |
| 60–74 | Solid but visibly short |
| 40–59 | Competent, with major gaps |
| below 40 | Skeletal |

The strictness directive applies: default 45–65, and any 70+ requires a written extraordinary
justification. None was awarded.

Every dimension carries one of three labels:

- **measured**: from a command and its output
- **judged**: auditor judgement against named evidence
- **NOT_ASSESSED**: scores 0 where it feeds a formula

## Weighting

| Bucket | Weight | Source dimension(s) |
|---|---:|---|
| Output-type readiness and coverage | 30 % | Mean of the 11 output-type scores (05) |
| Skill depth and worked examples | 25 % | Mean of dimension 3 (depth) and dimension 4 (worked examples) |
| Standards currency | 15 % | Dimension 5 |
| Taxonomy and structure | 10 % | Dimension 2 |
| Doctrine and philosophy | 10 % | Dimension 1 |
| Hygiene | 10 % | Mean of dimension 9 (redundancy), dimension 10 (discovery/routing) and dimension 11 (safety) |

Dimensions 7 (accessibility and inclusivity) and 8 (production and handoff) are scored and
reported in 09 but do not enter the weighted overall under the brief's weighting.

## Three published numbers

- **Raw**: the weighted overall, with routing as judged by the auditor.
- **Measured-constrained**: the same, with routing replaced by Engine Eval Readiness (57.5).
- **Published**: `min(measured-constrained, 65)`. The portfolio craft standard's acceptance
  evidence does not exist for this engine, so the cap applies. At 51.6 it does not bind.

## Hard-rule compliance

- Zero spend: no paid APIs, no model-executed evaluation runs.
- No git state changes; only read-only `git log`, `git show`, `git status` and `gh run` were used.
- Writes were confined to `docs/audits/2026-09-29-m10-reaudit/`.
- Running the validators and pytest did not modify tracked files (`git status --short` clean).
  `PYTHONDONTWRITEBYTECODE=1` was set. The git-ignored cache folders predate these runs; for
  example, `tests/__pycache__` is timestamped 03:24 on 29 September, before the audit began at
  about 07:20.
