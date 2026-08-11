# Digital Research Engine - Kaizen Wave 1 Report

Assessment date: 2026-08-11
Repository: `C:\wamp64\www\digital-research-engine`
Scope owner: repository maintainer
Wave: 1
Required-file availability: all mandatory files were available; no required read was unavailable.

## Baseline and maturity

The baseline assessment records a clean `main...origin/main` worktree, 58
active skills, 224 reference files, four templates, 20 example READMEs, 11
scripts, three test modules, four fixtures, and 19 report schemas. Source:
[KAIZEN-INITIAL-ASSESSMENT.md](../../../KAIZEN-INITIAL-ASSESSMENT.md),
the `digital-research-engine` inventory row.

The recorded raw diagnostic score was 59.6/100 and the exercise-published score
was capped at 55/100. The recorded maturity was Level 2: repeatable workflow
with material semantic-verification gaps. These are baseline facts, not a
certification. Source: [KAIZEN-INITIAL-ASSESSMENT.md](../../../KAIZEN-INITIAL-ASSESSMENT.md),
the repository score and maturity rows.

The pre-edit Git check was `## main...origin/main` with no changed paths
(command: `git status --short --branch`; exit 0). Before edits, the repository
also returned:

- `python -m engine doctor`: `Engine doctor OK.` (exit 0).
- `python -X utf8 scripts/skill_contract_validator.py --baseline tests/skill-engine/quality-baseline.json`: 58 active skills, 58 fully compliant, zero failure counts (exit 0).
- `python -X utf8 scripts/routing_smoke_test.py`: 28/28 top-three precision (exit 0).
- `python -X utf8 scripts/validate_engine.py`: 12 kernel tests passed (exit 0).
- `python -X utf8 scripts/validate_source_currency.py tests/fixtures/source-currency.json`: zero findings (exit 0).

The baseline assessment identified 15 absent route targets in the research-type
router, missing registry files in the three canonical example workspaces, a
verifier that checked source IDs but not semantic support, and stale module
names in `tools/README.md`. Source: [KAIZEN-INITIAL-ASSESSMENT.md](../../../KAIZEN-INITIAL-ASSESSMENT.md),
the repository findings and P0/P1 register. The pre-edit commands
`python -m engine validate example-market-landscape`,
`python -m engine validate example-due-diligence-dossier`, and
`python -m engine validate example-academic-paper` each exited non-zero with
GATE-03, GATE-06, and GATE-08 blockers for absent registry files.

No raw re-score is claimed for this wave. The exercise score remains published
at the baseline cap of 55/100 until the scoring instrument is re-run with
broader evidence. The repository's permanent 65/100 audit cap remains in its
canonical guidance and was not changed. Source: repository `SKILL.md` and the
assignment baseline rule.

## Changes made

| Improvement | Gap and root cause | Exact change and hypothesis | Owner, measure, and risk | Acceptance, standardisation, and re-audit |
|---|---|---|---|---|
| P0 route repair | The research-type router dispatched to absent skill directories. Root cause: reference-level techniques and parent skills were mixed in one route column without filesystem checks. | `skills/research-orchestration/references/research-type-router.md` now routes to active canonical skills and names existing reference files where a technique is reference-level. Hypothesis: a fresh agent can follow every active route without manual path repair. | Owner: repository maintainer. Measure: every canonical target and referenced file resolves in `engine/tests/test_research_type_router.py`. Risk: a nearest canonical parent may still require domain judgement; rollback is the single router-file change if route precision regresses. | Targeted route tests pass; 28/28 existing routing fixtures remain green. The test is the discoverable release guard. Re-audit: 2026-08-18, per the portfolio schedule. |
| P0 example registry repair | The ignored canonical project outputs lacked five schema files, so GATE-03/GATE-06/GATE-08 could not inspect them. Root cause: `scripts/seed_example_project.py` only wrote the older registry subset and used values outside the current schema contract. | The tracked seeder now writes `tradecraft.yaml`, `report-shapes.yaml`, `productization-manifest.yaml`, `calibration-log.yaml`, and `osint-tool-index.yaml`, alongside corrected test-only source/claim statuses. Hypothesis: a controlled fresh workspace can reproduce the full example gate contract without relying on ignored output. | Owner: repository maintainer. Measure: `test_tracked_seeder_creates_all_registry_inputs_for_example_gates`; no blocker findings. Risk: fixture data could be mistaken for research evidence; all values are explicitly `TEST ONLY`, and rollback is the seeder change. | The temp-workspace seeder test passes and all nine gates have no blocker findings. Existing ignored project directories were not deleted or rewritten; their missing files remain a local operator action. Re-audit: 2026-08-18. |
| P1 semantic support boundary | The verifier treated known source IDs as a high-confidence claim pass even when it had not inspected whether source content supported the claim. Root cause: structural linkage was used as a proxy for semantic review. | `tools/verification/source_verifier.py`, `skills/source-verification/SKILL.md`, and `templates/source-verification-manifest-template.yaml` now require an explicit `support_review` state and retain human-review boundaries. The verifier records `supported`, `unsupported`, `synthesis`, `inference`, and `no-source`; it does not infer semantic truth. Hypothesis: unsupported or unassessed semantics remain visible instead of becoming an automated certification. | Owner: repository maintainer with human evidence reviewer for real projects. Measure: the fixture produces zero claim-support `pass` results and `release_ready: no`. Risk: existing manifests without review now become low-confidence warnings; rollback is the verifier/template/skill change, but doing so restores the documented blind spot. | `tests/fixtures/claim-support-review.json` and two deterministic tests cover all five states. CLI result: pass 0, warn 5, fail 2, release ready no; the non-zero exit is expected because the fixture contains unsupported and no-source cases. Re-audit: 2026-08-25. |
| P0 documentation reconciliation | `tools/README.md` advertised module names absent from the filesystem. Root cause: a planned-tool layout was presented as an implemented module index. | The README now describes filesystem-backed groups, lists implemented module groups, identifies `source_verifier.py`, and labels unavailable runtimes as `not assessed`. Hypothesis: a fresh agent will not select an absent utility. | Owner: repository maintainer. Measure: the route/documentation test rejects the stale module names. Risk: the README can age as modules change; rollback is the README-only patch. | Documentation test passes and `git diff --check` passes. Standardise by updating the README in the same change as future module additions or by deriving it from the tree. Re-audit: 2026-08-18. |

## Files changed

Tracked repository files changed:

- `scripts/seed_example_project.py`
- `skills/research-orchestration/references/research-type-router.md`
- `skills/source-verification/SKILL.md`
- `templates/source-verification-manifest-template.yaml`
- `tools/README.md`
- `tools/verification/source_verifier.py`
- `engine/tests/test_example_project_seed.py`
- `engine/tests/test_research_type_router.py`
- `engine/tests/test_source_verifier.py`
- `tests/fixtures/claim-support-review.json`
- this report

No ignored `projects/example-*` registry file was retained as a change. The
tracked seeder and its temporary-workspace test are the acceptance source of
truth. This avoids treating ignored project output as a released repair and
avoids deleting or overwriting user project work.

## Before and after measures

| Measure | Before | After | Evidence and interpretation |
|---|---:|---:|---|
| Active skill contracts | 58/58 | 58/58 | Contract validator before and after; no catalogue expansion. |
| Existing routing fixtures | 28/28 | 28/28 | `routing_smoke_test.py`; unchanged structural routing evidence. |
| Kernel tests | 12 passed | 18 passed | `validate_engine.py`; six new focused tests are included in the after count. |
| Source-currency findings | 0 | 0 | Source-currency validator; no source register change was needed. |
| Source-ingestion findings | 0 | 0 | Source-ingestion guardrail after final edits. |
| Canonical route targets in the changed router | 15 stale targets | no active stale target tokens | Filesystem-backed route test; this is scoped to the changed router, not every historical reference in the repository. |
| Example seeder gate blockers | missing registry blockers in the local canonical outputs | 0 in a fresh temporary seeded workspace | `test_example_project_seed.py`; existing ignored workspaces were intentionally not rewritten. |
| Semantic claim-support fixture | known source IDs could be reported as pass without support review | 0 claim-support passes; 5 warnings; 2 failures | Verifier CLI on the negative fixture. This is a visibility improvement, not semantic certification. |

The numeric measures above are command results retained in this report; the
portfolio baseline counts and score are sourced in the baseline section. The
after measures do not prove production research quality, live-source truth, or
semantic correctness of any real claim.

## Validation record

| Command | Result | Exit state |
|---|---|---:|
| `git diff --check` | No whitespace errors; line-ending warnings only | 0 |
| `python -m engine doctor` | Engine doctor OK | 0 |
| `python -X utf8 scripts/skill_contract_validator.py --baseline tests/skill-engine/quality-baseline.json` | 58 active, 58 fully compliant, zero failure counts | 0 |
| `python -X utf8 scripts/routing_smoke_test.py --details` | 28/28 top-three precision; all fixtures pass | 0 |
| `python -X utf8 scripts/validate_engine.py` | Contract, routing, doctor, and 18 engine tests pass | 0 |
| `python -m unittest discover -s engine/tests` | 18 tests passed | 0 |
| `python -m unittest engine.tests.test_source_verifier engine.tests.test_research_type_router engine.tests.test_example_project_seed` | six focused tests passed | 0 |
| `python -X utf8 scripts/validate_source_currency.py tests/fixtures/source-currency.json` | zero findings; source currency complete | 0 |
| `python -X utf8 scripts/source_ingestion_guardrail.py` | zero findings | 0 |
| `python -X utf8 C:\wamp64\www\skills-web-dev\skills\sdlc-meta\skill-writing\scripts\quick_validate.py skills/source-verification` | Skill is valid | 0 |
| `python -m engine validate` through the tracked temp seeder test | all nine gates have no blocker findings | 0 |
| `python tools/verification/source_verifier.py tests/fixtures/claim-support-review.json --no-archive --format md` | release ready no; pass 0, warn 5, fail 2; intentional negative fixture | 1 (expected non-zero from the shell result) |
| `python -m unittest discover -s tests` | no tests discovered by the repository-root discovery pattern | 1 |

The root `tests` discovery result is not treated as a pass or a failure of the
changed behaviour; the repository's active test runner is `engine/tests`, and
the focused tests ran there. It remains a test-discovery debt.

## Safety and anti-slop review

The changed `source-verification/SKILL.md` was read in full after editing. A
static red-flag scan over the changed skill, verifier, fixture, and test found
no installer, credential-harvesting, exfiltration, reverse-shell, or hidden
destructive instruction. The required source-ingestion guardrail returned zero
findings. Safety status: Safe for this bounded change, with the normal caveat
that code review and runtime security testing are separate activities.

The report and fixtures use specific test-labelled states and retain the
negative cases. No real person, organisation, external statistic, direct
quote, live source URL, or production success has been invented. The
`test-fixture://` URI is a test value, not a source claim. The verifier's
semantic boundary explicitly prevents the fixture from certifying support.

## Remaining backlog

### P0

- Re-run the tracked seeder in a disposable or explicitly authorised copy of
  each canonical example workspace, then run the CLI gates there. This was not
  run against the existing ignored workspaces because the seeder removes and
  recreates its target directories. Owner: repository maintainer. Re-audit:
  2026-08-18.
- Keep the research-type route test aligned when a canonical skill or reference
  is renamed. A test pass does not prove that the chosen parent is the best
  domain owner for every future research question.

### P1

- Obtain independent human semantic review for real claims and record the
  supporting locator, scope, definitions, and counter-evidence. The verifier
  deliberately does not replace that review.
- Add a real-source, non-production test case only when a lawful, stable source
  fixture is available. Until then, semantic truth of the test-labelled claims
  is **NOT ASSESSED**.
- Decide whether the root `tests` directory should become a package/discovery
  target or remain outside the active engine test runner. No change was made in
  this wave because it is broader than the assigned P1.

### P2

- Audit historical references in other skills for stale parent/technique names;
  this wave intentionally limited routing repair to the canonical
  research-type router.
- Measure source-verification review coverage over real project manifests and
  add a release dashboard only if it improves decisions rather than adding
  reporting volume.
- Revisit the tools README from the filesystem when the tool tree changes.

## NOT ASSESSED

- Semantic truth of any real claim: no real claim was supplied for this wave.
- URL liveness, archive availability, quote matching, or statistic matching for
  the test fixture: it intentionally contains no live source URL.
- Render, system, network, production, accessibility, or external-provider
  evidence: no production artefact or external research engagement was in scope.
- Destructive seeder execution against the existing canonical example
  directories: not run to preserve user work and avoid ignored-output reliance.
- Claude Code runtime execution, Codex vendor smoke beyond this run, and a
  generic agent's automatic instruction discovery: not assessed. The canonical
  skill and root instruction files remain model-neutral fallbacks.

## Compatibility

The changed canonical logic remains in Markdown skill/reference files, the
tracked Python seeder, and repository tests. No model-specific bridge was
added. The repository already provides `AGENTS.md`, `CLAUDE.md`, and root
`SKILL.md`; the changed `source-verification/SKILL.md` retains its portable
metadata for Claude Code and Codex. A generic agent can use the same canonical
files through explicit manual routing. Automatic discovery behaviour for an
arbitrary future agent is **NOT ASSESSED**.

## Next wave recommendations

1. Run the tracked seeder in disposable copies of the three canonical examples
   and retain their gate outputs as repository-local evidence without committing
   generated project output.
2. Have an independent reviewer exercise the claim-support fixture and one
   lawful real-source manifest, checking whether the state labels and required
   review fields are sufficient for the intended release decision.
3. Re-audit route-neighbour collisions for market, social-sentiment, policy,
   and academic variants; retain `research-techniques`, `research-design`,
   `due-diligence`, `osint-investigation`, and `online-legal-research` as the
   canonical parent skills unless evidence shows a better existing owner.
4. Recalculate the raw score only after the tracked seeder and semantic-review
   evidence are independently re-run. Do not award 95/100 from structural
   passes alone.

## Diff and scope conclusion

The final status contains only the ten repository-local implementation/test
files and this report. No pre-existing or unrelated changes were present at
the clean baseline, and no sibling repository or workspace-level report was
modified. No commit, push, fetch, pull, or reset was performed.
