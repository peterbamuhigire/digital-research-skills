# Engine Tune — 10-Phase Implementation Plan

**Date:** 2026-04-26
**Scope:** Turn `digital-research-engine` into a project-oriented research operating system with formal project initiation, workspace scaffolding, registry-backed evidence control, validation gates, and exportable release packs.
**Primary inspiration studied from:** `C:\wamp64\www\srs-skills`
**Target outcome:** every research engagement is managed as a first-class workspace with deterministic state, reusable project scaffolds, and machine-checkable release readiness.

---

## Why this plan exists

The current repository has strong research skills, but project initiation and project management are still mostly convention-driven. The `srs-skills` repo demonstrates a stronger operating model:

- canonical workspace contract
- project scaffold command
- `_context/` as source of truth
- `_registry/` as machine-readable control plane
- deterministic validation gates
- evidence-pack export
- example projects that prove the kernel works

This plan adapts those mechanics to a research engine rather than an SDLC documentation engine.

---

## Design principles

1. **Project-first, not document-first.** A project workspace is the operating unit.
2. **Context is canonical.** `_context/` holds the user-approved project truth.
3. **Claims must be machine-trackable.** `_registry/` is not optional.
4. **Validation gates precede release.** Narrative quality alone is insufficient.
5. **Audience and output are explicit dimensions.** The same research corpus may produce multiple deliverables.
6. **Evidence packaging is part of the release process.** Final artifacts ship with auditability.

---

## Canonical workspace model

The implementation target is:

```text
projects/<project-id>/
  README.md
  PROJECT-STATUS.md
  EVIDENCE-AUDIT.md
  export/
  _context/
    brief.md
    methodology.md
    project-profile.md
    research-roadmap.md
    audience.md
    output-plan.md
    cohorts.md
    scope.md
    exclusions.md
    hypotheses.md
    success-criteria.md
    monetization.md
  _registry/
    sources.yaml
    claims.yaml
    quotes.yaml
    synthesis-map.yaml
    sign-offs.yaml
    waivers.yaml
    release-ledger.yaml
  01-initiation/
  02-research/
  03-analysis/
  04-synthesis/
  05-output/
  06-governance/
```

---

## Phase 1 — Establish the project kernel

**Objective:** Create the base runtime model for project workspaces inside this repo.

**Deliverables**
- `engine/__init__.py`
- `engine/__main__.py`
- `engine/workspace.py`
- `docs/plans/engine-tune/` plan set
- `docs/pathing-model.md`

**Implementation**
- Introduce a `Workspace` object similar in spirit to `srs-skills/engine/workspace.py`.
- Define `projects/<project-id>/` as the canonical runtime root.
- Define `_context/` and `_registry/` as mandatory workspace directories.
- Document canonical path rules and any legacy aliases.

**Dependencies**
- None.

**Exit criteria**
- A workspace loader can detect and validate a project root.
- Pathing model is documented clearly.

---

## Phase 2 — Build the new-project scaffold flow

**Objective:** Make project setup deterministic and fast.

**Deliverables**
- `engine/scaffold.py`
- `engine/cli.py` command: `new-project`
- `skills/00-meta-initialization/` equivalent for research
- scaffold templates for `_context/`, `_registry/`, README, status, export scripts

**Implementation**
- Add `python -m engine new-project <name> --type <research-type> --audience <audience> --variant <variant>`.
- Seed the canonical workspace tree.
- Pre-populate context files with TODOs and guidance.
- Create `PROJECT-STATUS.md`, `README.md`, and `export/`.

**Dependencies**
- Phase 1 workspace contract.

**Exit criteria**
- A new project can be scaffolded with one command.
- Scaffolded project opens cleanly as a valid workspace.

---

## Phase 3 — Implement research meta-initialization

**Objective:** Make every project start with an explicit intake and orchestration decision.

**Deliverables**
- `skills/00-meta-initialization/SKILL.md`
- `skills/00-meta-initialization/references/decision-tree.md`
- `_context/methodology.md`
- `_context/project-profile.md`
- `_context/research-roadmap.md`
- `_context/audience-output-matrix.md`

**Implementation**
- Create a first-run skill that asks or derives:
  - research type
  - domain
  - audience
  - output family
  - methodology mix
  - primary-research need
  - monetization intent
- Emit a roadmap and project profile.
- Make this the required first skill for project kickoff.

**Dependencies**
- Phase 2 scaffold.
- Existing `research-orchestration`, `research-design`, `knowledge-productization`.

**Exit criteria**
- A newly scaffolded project can be initialized into a concrete roadmap.
- Audience and output path are explicit before research begins.

---

## Phase 4 — Define registry schemas and sync logic

**Objective:** Move evidence control from prose-only files to machine-readable registries.

**Deliverables**
- `engine/registry/` package
- schema files for:
  - `sources.yaml`
  - `claims.yaml`
  - `quotes.yaml`
  - `synthesis-map.yaml`
  - `sign-offs.yaml`
  - `waivers.yaml`
  - `release-ledger.yaml`
- `python -m engine sync <project>`

**Implementation**
- Define minimal required fields for each registry.
- Add sync logic that derives or updates registries from project markdown where possible.
- Keep `EVIDENCE-AUDIT.md` as human log, but not the only evidence structure.

**Dependencies**
- Phase 1 workspace model.
- Existing evidence discipline from `source-evaluation`.

**Exit criteria**
- Registry files are schema-valid.
- Sync command can populate or repair baseline registry state.

---

## Phase 5 — Add project status and release management

**Objective:** Give each project a clear operational dashboard and release history.

**Deliverables**
- `PROJECT-STATUS.md` template
- `engine/status.py` or `engine/cli.py` command: `status`
- `_registry/release-ledger.yaml`
- export scripts for flattened deliverable collection

**Implementation**
- Track:
  - current phase
  - cohort completion
  - source counts by tier
  - validation state
  - open gaps
  - outputs built
  - audience variants complete
- Add release entries whenever a deliverable version is built.

**Dependencies**
- Phases 2 and 4.

**Exit criteria**
- A user can inspect a project and see its real state quickly.
- Release history is recorded rather than inferred.

---

## Phase 6 — Implement deterministic research gates

**Objective:** Enforce research quality structurally, not only by good prompting.

**Deliverables**
- `engine/gates/base.py`
- `engine/gates/gate01_init_context.py`
- `engine/gates/gate02_research_coverage.py`
- `engine/gates/gate03_evidence_integrity.py`
- `engine/gates/gate04_analysis_tradecraft.py`
- `engine/gates/gate05_synthesis_traceability.py`
- `engine/gates/gate06_output_readiness.py`
- `engine/gates/gate07_audience_fit.py`
- `engine/gates/gate08_productization_readiness.py`
- `engine/gates/gate09_release_pack.py`

**Implementation**
- Start with 4 mandatory gates first:
  - init context
  - evidence integrity
  - synthesis traceability
  - output readiness
- Expand to all 9 gates once baseline works.
- Emit machine-readable findings with gate IDs and severities.

**Dependencies**
- Phase 4 registries.
- Existing skills: `source-evaluation`, `analytic-tradecraft`, `executive-communication`, `academic-writing`, `knowledge-productization`.

**Exit criteria**
- `python -m engine validate <project>` can fail deterministically on real structural problems.
- Blocking findings are separated from warnings.

---

## Phase 7 — Wire output assembly and manifests

**Objective:** Make report, proposal, paper, thesis, and book assembly ordered and repeatable.

**Deliverables**
- manifest convention for each output directory
- `05-output/` substructure templates
- assembly helper or CLI support for manifest-driven builds

**Implementation**
- Introduce `manifest.md` inside output directories to define chapter/section order.
- Support multiple output families from the same research corpus:
  - executive report
  - proposal
  - academic paper
  - thesis/dissertation
  - white paper
  - book manuscript structure
- Keep markdown canonical; rendering stays downstream.

**Dependencies**
- Phase 2 scaffold.
- Existing `research-design`, `report-and-proposal-craft`, `academic-writing`, `python-document-generation`.

**Exit criteria**
- Output assembly order is explicit and versionable.
- One project can carry more than one output family cleanly.

---

## Phase 8 — Build evidence-pack export

**Objective:** Ship each release with audit-ready support material.

**Deliverables**
- `python -m engine pack <project> --out <zip>`
- `engine/pack.py`
- release-pack spec in docs

**Implementation**
- Include in the pack:
  - final markdown source
  - built `.docx` / `.pdf` if present
  - source manifest
  - claim registry
  - quote registry
  - synthesis map
  - evidence audit
  - validation report
  - sign-offs and waivers
- Keep it deterministic and reproducible.

**Dependencies**
- Phases 4, 5, and 6.

**Exit criteria**
- A release pack can be produced for any validated project.
- Pack contents are sufficient for internal or client audit.

---

## Phase 9 — Seed example projects and tests

**Objective:** Prove the kernel works with realistic research workloads.

**Deliverables**
- `scripts/seed_example_project.py`
- `engine/tests/`
- at least 3 example projects:
  - market landscape
  - due-diligence dossier
  - academic paper or thesis

**Implementation**
- Build one tiny fixture for kernel tests.
- Build 2-3 richer examples that reflect real project structures.
- Add tests for:
  - scaffold
  - workspace detection
  - registry schema loading
  - validation gates
  - evidence pack generation

**Dependencies**
- Phases 1-8.

**Exit criteria**
- Example projects validate cleanly.
- Test suite covers the kernel’s critical flows.

---

## Phase 10 — Integrate into repo workflow and governance

**Objective:** Make the kernel part of normal repo operation, not an optional sidecar.

**Deliverables**
- updated `README.md`
- updated `AGENTS.md`
- updated `CLAUDE.md`
- `scripts/validate_engine.py` or equivalent repo-level validator
- migration notes for legacy projects

**Implementation**
- Document the new golden path:
  1. `python -m engine doctor`
  2. `python -m engine new-project ...`
  3. run research meta-initialization
  4. execute waves
  5. `python -m engine sync`
  6. `python -m engine validate`
  7. `python -m engine pack`
- Add migration guidance for old projects like `east-africa-property-hostel`.
- Make repo-level validation check for kernel docs and pathing contract.

**Dependencies**
- All prior phases.

**Exit criteria**
- The kernel is part of normal project operations.
- Existing and new users can follow a documented, repeatable workflow.

---

## Recommended build order

1. Phase 1
2. Phase 2
3. Phase 3
4. Phase 4
5. Phase 6
6. Phase 5
7. Phase 7
8. Phase 8
9. Phase 9
10. Phase 10

This order front-loads the workspace and validation backbone before polishing release ergonomics.

---

## Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Overbuilding the kernel before one real project uses it | High | migrate one current project early after Phase 4 |
| Registry burden makes project use too heavy | High | start with minimal required fields and automate sync |
| Validation gates become too editorial and non-deterministic | High | only encode structural and traceability checks in kernel |
| Too many output families too early | Medium | start with report, proposal, paper; add book/thesis depth later |
| Drift between markdown corpus and registries | Medium | make `sync` a normal step before `validate` |

---

## Immediate next implementation move

Start with **Phase 1 + Phase 2 together**:

- scaffold `engine/`
- implement `Workspace`
- implement `new-project`
- create canonical research workspace templates

That is the shortest path from brainstorming to a usable operating model.
