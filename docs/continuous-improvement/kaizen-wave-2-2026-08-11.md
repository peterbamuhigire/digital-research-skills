# Digital Research Engine - Kaizen Wave 2 Report

Assessment date: 2026-08-11
Repository: `C:\wamp64\www\digital-research-engine`
Scope: claim-support state verification, repaired research-type routes, and seeded example registries
Wave: 2
Owner: repository maintainer
Status: implementation and fresh re-audit complete; no commit or publication performed

## Outcome

Wave 2 challenged the Wave 1 claim-support implementation with isolated
negative controls and malformed manifests. Complete reviewer metadata does not
make an `unsupported`, `no-source`, or `inference` claim release-ready. The
verifier now also rejects malformed `source_ids` shapes, duplicate IDs, invalid
review dates, invalid state types, non-list manifest collections, and non-object
entries. The semantic boundary remains explicit: the verifier records review
state and structural integrity; it does not certify semantic truth.

The fresh route re-audit covers all 19 research-type table rows and keeps the
28/28 routing fixture result. The fresh seeder re-audit covers all three tracked
example definitions in disposable temporary workspaces. The three existing
ignored example workspaces were inspected read-only and still fail because
Wave 1 intentionally did not overwrite their registries; that is retained as a
visible release blocker rather than converted into a pass.

No full-engine raw score is recalculated for this focused wave. The permanent
portfolio cap remains 65/100 and the exercise adapter remains 55/100, as
recorded in the [portfolio standard](portfolio-kaizen-standard-2026-08.md),
the [initial assessment](../../../KAIZEN-INITIAL-ASSESSMENT.md), and the
[Wave 1 report](../../../KAIZEN-WAVE-1-REPORT.md). This report records changed
measures and evidence states, not a certification.

## Fresh re-audit findings

### Wave 1 challenge and result

Wave 1 correctly removed the old path where a known source ID could be treated
as a claim-support pass without a semantic review record. Its mixed fixture
showed five support states, zero claim-support passes, five warnings, two
failures, and `release_ready: no` (command evidence is retained in the
[Wave 1 report](kaizen-wave-1-2026-08-11.md)).

The independent Wave 2 challenge found that the implementation still coerced
any iterable `source_ids` value to strings and silently skipped a non-list
`claims` collection. That created a structural bypass risk (inference): a
malformed manifest could avoid the intended state/source checks rather than be
rejected as malformed. The correction moves shape checks ahead of semantic text
handling and adds an explicit release-readiness guard for every labelled
support state.

### Before / Wave 1 / Wave 2 measures

| Measure | Before Wave 1 | Wave 1 | Wave 2 | Evidence and interpretation |
|---|---|---|---|---|
| Claim-support semantics | Known source IDs could be reported as a claim pass without semantic support review | Five explicit states; zero claim-support passes; five warnings; two failures; release not ready | Three isolated non-certifying states (`unsupported`, `no-source`, `inference`) remain non-release-ready even with complete metadata | [Wave 1 report](kaizen-wave-1-2026-08-11.md); `python -m unittest engine.tests.test_source_verifier` exit 0; negative CLI exit 2 is expected |
| Malformed state/source combinations | No explicit list-shape or duplicate-ID gate in the changed verifier path | State relationships were checked for the mixed fixture | Five malformed cases fail deterministically, including scalar/non-string IDs and invalid empty/non-empty state pairings | `python -m unittest engine.tests.test_source_verifier` exit 0; `test_malformed_state_source_combinations_are_rejected` |
| Repaired research-type routes | 15 absent route names were recorded in the baseline | Canonical routes repaired; 28/28 routing fixtures passed | All 19 route-table rows resolve to active skill names; 28/28 routing fixtures still pass | [Initial assessment](../../../KAIZEN-INITIAL-ASSESSMENT.md); `test_all_repaired_research_type_rows_have_active_skill_routes`; `python -X utf8 scripts/routing_smoke_test.py --details` exit 0 |
| Seeded example registries | Three local canonical outputs lacked five required registry files each | The tracked seeder and a temporary market-landscape test proved the repair without rewriting ignored outputs | The temporary test covers all three seeded examples with no blocker findings; existing ignored outputs remain visibly blocked when validated read-only | Three `python -m engine validate example-*` commands exit 1 with missing registry blockers; `python -m unittest engine.tests.test_example_project_seed` exit 0 |
| Engine test evidence | 12 kernel tests were recorded before Wave 1 | 18 engine tests passed | 22 engine tests pass; 10 focused tests pass | `python -m unittest discover -s engine/tests` and `python -X utf8 scripts/validate_engine.py` both exit 0 |

The measures above are repository-local command results or findings already
recorded in the linked Wave 1 artefacts. They do not establish semantic truth
for any real research claim.

## Wave 2 actions

### W2-01 - Harden the claim-support state gate

| Contract field | Wave 2 record |
|---|---|
| Gap | Claim support could be structurally bypassed by non-list or malformed `source_ids`; the verifier's release decision needed an explicit non-certifying state guard. Evidence: the pre-edit implementation converted `source_ids` entries with `str()` and iterated manifest collections without validating list shape. |
| Root cause | Structural validation was narrower than the state contract, and release blocking relied partly on low confidence rather than a named semantic non-certification invariant (inference). |
| Change | `tools/verification/source_verifier.py` now requires explicit list-shaped source IDs, non-empty strings, no duplicates, known IDs for sourced states, `[]` only for `no-source`, string states from the allowed set, string review fields, parseable ISO-8601 review dates, list-shaped manifest collections, and object entries. Release readiness explicitly remains false for every labelled support state. `skills/source-verification/SKILL.md` and `templates/source-verification-manifest-template.yaml` teach the same boundary. |
| Hypothesis | If malformed state/source combinations fail before semantic handling, and release readiness has an explicit non-certification guard, metadata cannot promote unsupported, no-source, or inference claims. |
| Owner | Repository maintainer; semantic judgement remains with an authorised human evidence reviewer. |
| Measure | Isolated non-certifying state cases remain non-release-ready; five malformed cases return `fail`; the mixed fixture retains zero claim-support passes and release not ready. |
| Risk | Stricter shape checks may reject legacy manifests that relied on scalar or implicit values. This is an intentional release-safety trade-off; migration must make the list and state explicit. |
| Rollback | Revert the verifier, skill, template, and focused-test changes as one bounded group if a real authorised manifest demonstrates a valid contract case that the schema wrongly rejects. Retain the negative evidence and do not weaken the state gate merely to restore a pass. |
| Acceptance | `python -m unittest engine.tests.test_source_verifier` exit 0; `python tools/verification/source_verifier.py tests/fixtures/claim-support-review.json --no-archive --format md` exits 2 with release not ready, zero passes, five warnings, and two failures; the non-zero result is expected evidence. |
| Standardisation | The canonical skill, manifest template, verifier, and deterministic tests now state the same shape and non-certification rules. Future verifier changes must preserve both positive state-shape coverage and negative bypass coverage. |
| Re-audit | 2026-08-25, or earlier if a real project manifest is migrated to this contract. |

### W2-02 - Re-audit every repaired research-type route

| Contract field | Wave 2 record |
|---|---|
| Gap | Wave 1's route test checked a fixed canonical set and former dead names but did not assert that every repaired table row had an active route token. |
| Root cause | Route existence and route-row completeness were treated as related checks but were not represented by one all-row deterministic assertion (inference). |
| Change | `engine/tests/test_research_type_router.py` now parses the two repaired route tables, requires 19 route rows, and verifies each row's backticked skill token against the filesystem-backed active skill set. The Wave 1 router file itself was preserved. |
| Hypothesis | A fresh agent will receive a failure when a future edit leaves any repaired research type without an active canonical skill, even if the fixed canonical set still passes. |
| Owner | Repository maintainer. |
| Measure | 19/19 route rows resolve; the existing routing suite remains 28/28 top-three precision. |
| Risk | A future intentional route-table format change could require a test update; the test must not be loosened to accept dead names. |
| Rollback | Revert only the all-row test if its parser is invalidated by a documented route-table format change, then replace it with an equivalent filesystem-backed check before release. |
| Acceptance | `python -m unittest engine.tests.test_research_type_router` exit 0 and `python -X utf8 scripts/routing_smoke_test.py --details` exit 0. |
| Standardisation | The all-row route assertion is now the discoverable regression guard alongside the existing 28-fixture smoke test. |
| Re-audit | 2026-08-25 with any router taxonomy change. |

### W2-03 - Re-audit all seeded example registries without mutating user workspaces

| Contract field | Wave 2 record |
|---|---|
| Gap | The Wave 1 temporary test exercised one example definition, while the three existing ignored outputs remained unseeded and therefore failed registry gates. |
| Root cause | The seeder's destructive target replacement and ignored project output made it unsafe to use the normal seeder directly against existing workspaces; the test scope was narrower than the `EXAMPLES` tuple (inference). |
| Change | `engine/tests/test_example_project_seed.py` now iterates every entry in the tracked `EXAMPLES` tuple, creates each workspace beneath a temporary directory, writes the expected registry set, assembles output, and asserts that all gates have no blocker findings. No existing `projects/example-*` directory was rewritten. |
| Hypothesis | Testing the seeder contract from the source tuple in disposable workspaces will prove all repaired registry paths without treating ignored local output as released evidence. |
| Owner | Repository maintainer. |
| Measure | All three temporary seeded examples pass the blocker assertion; all three existing ignored examples remain explicitly recorded as blocked until an authorised operator reseeds disposable or approved copies. |
| Risk | The test proves the tracked seeder and kernel gates, not the historical content of existing ignored workspaces or production research quality. |
| Rollback | Revert the test-only expansion. If real workspaces must be repaired, first make an authorised copy and retain the pre-seed registry state; do not run the destructive seeder against user work in this audit. |
| Acceptance | `python -m unittest engine.tests.test_example_project_seed` exit 0; read-only validation of `example-market-landscape`, `example-due-diligence-dossier`, and `example-academic-paper` retains exit 1 with missing-registry blockers. |
| Standardisation | The test derives coverage from `EXAMPLES` rather than repeating one example name, keeping future seeded examples inside the same gate. |
| Re-audit | 2026-08-25, after an authorised operator supplies disposable or approved seeded-workspace evidence. |

## Exact Wave 2 files

Wave 2 touched only these repository-local files:

- `tools/verification/source_verifier.py`
- `skills/source-verification/SKILL.md`
- `templates/source-verification-manifest-template.yaml`
- `engine/tests/test_source_verifier.py`
- `engine/tests/test_research_type_router.py`
- `engine/tests/test_example_project_seed.py`
- `docs/continuous-improvement/kaizen-wave-2-2026-08-11.md`

The Wave 1 implementation files `scripts/seed_example_project.py`,
`skills/research-orchestration/references/research-type-router.md`,
`tools/README.md`, and `tests/fixtures/claim-support-review.json` were
re-audited and preserved. They remain in the pre-existing Wave 1 worktree
change set; they are not new Wave 2 edits.

## Validation record

| Command | Observed result | Exit |
|---|---|---:|
| `python -m engine doctor` | Engine doctor OK | 0 |
| `python -X utf8 scripts/skill_contract_validator.py --baseline tests/skill-engine/quality-baseline.json` | 58 active; 58 fully compliant; zero failure counts | 0 |
| `python -X utf8 scripts/routing_smoke_test.py --details` | 28/28 top-three precision; all fixtures pass | 0 |
| `python -X utf8 scripts/validate_engine.py` | Contract, routing, doctor, and 22 engine tests pass | 0 |
| `python -X utf8 scripts/validate_source_currency.py tests/fixtures/source-currency.json` | Zero findings; source currency complete | 0 |
| `python -X utf8 scripts/source_ingestion_guardrail.py` | Zero findings | 0 |
| `python -m unittest discover -s engine/tests` | 22 tests passed | 0 |
| `python -m unittest engine.tests.test_source_verifier engine.tests.test_research_type_router engine.tests.test_example_project_seed` | 10 focused tests passed | 0 |
| `python -X utf8 C:\wamp64\www\skills-web-dev\skills\sdlc-meta\skill-writing\scripts\quick_validate.py skills/source-verification` | Skill is valid | 0 |
| `python -X utf8 C:\wamp64\www\skills-web-dev\skills\sdlc-meta\skill-writing\scripts\contract_gate.py --skill skills/source-verification` | Evidence contract scanned with zero errors and zero warnings | 0 |
| `python tools/verification/source_verifier.py tests/fixtures/claim-support-review.json --no-archive --format md` | Release not ready; zero passes, five warnings, two failures; intentional negative fixture | 2 (expected non-zero) |
| `python -m unittest discover -s tests` | No tests discovered by the repository-root pattern | 1 (expected discovery debt) |
| `python -m engine validate example-market-landscape` | Missing Wave 1 registry files remain blockers | 1 (expected until authorised reseed) |
| `python -m engine validate example-due-diligence-dossier` | Missing Wave 1 registry files remain blockers | 1 (expected until authorised reseed) |
| `python -m engine validate example-academic-paper` | Missing Wave 1 registry files remain blockers | 1 (expected until authorised reseed) |
| `git diff --check` | No whitespace errors; Git reported line-ending conversion warnings for existing changed files | 0 |

The expected non-zero rows are retained as evidence. Existing ignored project
directories were not deleted, overwritten, seeded, or otherwise mutated.

## Safety and anti-slop findings

### Safety

Safety status: **Safe for this bounded change**.

- The changed `skills/source-verification/SKILL.md` was read in full after the
  edit, as required by the safety-audit procedure.
- A static scan of the changed skill, verifier, template, and focused test found
  no remote installer, credential request, exfiltration, reverse shell, hidden
  destructive action, or new external dependency instruction.
- The only install-related matches are existing runtime messages explaining
  that optional Python packages are unavailable; they do not execute an
  installer or grant permissions.
- `python -X utf8 scripts/source_ingestion_guardrail.py` returned zero findings.
- Runtime security, network, archive, and external-provider behaviour is not
  certified by this static review.

### Anti-slop

The changed human-facing contract contains named support states, explicit
failure paths, a release boundary, and deterministic test references. A static
scan found no banned filler use; its only `landscape` matches are exact
fixture/project identifiers. It also found no placeholder test assertions,
TODO stubs, or invented source claims in the changed surfaces. The anti-slop audit's
genericness score is **NOT ASSESSED** because no repository-native automated
genericness scorer was run; this does not lower the separate safety or test
results. Semantic judgement remains human and non-certifying.

## Portability

- Canonical claim-support behaviour remains in the model-neutral Python
  verifier, `SKILL.md`, template, and tests.
- `skills/source-verification/SKILL.md` declares portable compatibility with
  Claude Code and Codex; the repository already has root `AGENTS.md`,
  `CLAUDE.md`, and `SKILL.md` entry points.
- No vendor-specific adapter or duplicated semantic doctrine was added in Wave
  2.
- A generic agent can use the canonical files through explicit manual routing.
  Automatic discovery by every present or future agent is **NOT ASSESSED**.
- Live Claude Code execution, live Codex vendor execution, and external-agent
  instruction discovery are **NOT ASSESSED**.

## Residual P0 / P1 / P2 and NOT ASSESSED states

### P0

- The three existing ignored canonical example workspaces still fail GATE-03,
  GATE-04, GATE-06, and GATE-08 because the five Wave 1 registry files are
  absent. An authorised operator must reseed disposable or explicitly approved
  copies and retain the gate output. This audit did not mutate them.
- Semantic support for real project claims still requires an authorised human
  reviewer and claim-level evidence. The verifier is not a semantic certifier.

### P1

- Add a lawful stable real-source fixture when one is available, then test
  source liveness, archive handling, locator support, quote matching, and
  statistic matching without claiming that a test-labelled source is real.
- Decide whether the root `tests` directory should become a supported discovery
  target or remain outside the active engine runner; the current discovery exit
  1 remains visible.
- Revisit route-parent choices with domain review when a real research brief
  exposes a collision; the all-row test proves path existence, not best-method
  selection.

### P2

- Audit historical stale references outside the repaired research-type router.
- Revisit the tools README from the filesystem when tool modules change.
- Re-run the Claude/Codex/generic discovery matrix when vendor instruction
  mechanisms change.

### NOT ASSESSED

- Semantic truth of any real claim; no real claim was supplied for this wave.
- URL liveness, archive availability, quote matching, and statistic matching for
  the test-labelled claim fixture.
- Render, system, network, production, accessibility, and external-provider
  evidence.
- Destructive seeding against existing canonical example directories.
- Automatic instruction discovery by an arbitrary generic agent and live vendor
  runtime execution.
- Longitudinal reviewer agreement, false-positive rate, and operational
  performance of the verifier.

## Standardisation and re-audit

The successful learning is standardised in the source-verification skill,
manifest template, verifier, and focused regression tests. The route and seeder
tests are filesystem- and source-tuple-backed rather than manually asserting one
example only. The next scheduled re-audit remains 2026-08-25, with earlier
review required if a real manifest is migrated or a router/seeder contract
changes. No score was awarded for unexecuted semantic, production, or runtime
evidence.

No commit, push, fetch, pull, reset, publish, sibling-repository edit, or
workspace-level report edit was performed.
