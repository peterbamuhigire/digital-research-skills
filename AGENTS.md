# AGENTS.md — digital-research-engine

Operating instructions for Codex and other agent runtimes that load skills via `AGENTS.md`.

## The one rule that overrides everything

**Do not hallucinate.** No claim, statistic, quote, name, court case, statute, organisation, or URL appears in any output unless it can be traced to a real source.

Read `skills/source-evaluation/SKILL.md` and `skills/source-evaluation/references/evidence-discipline.md` before any research work. The hard-constraint clause from that reference **must appear verbatim** in every sub-task agent prompt you dispatch.

## Standard workflow

1. Load `skills/source-evaluation/SKILL.md` + `skills/source-evaluation/references/evidence-discipline.md` → enforce throughout
2. Load `skills/research-orchestration/SKILL.md` → drives wave planning
3. For each cohort: dispatch a research sub-task with the standard brief structure
4. After each wave: run `source-verification` and `gap-analysis`
5. Before synthesis or final drafting: run `skills/critical-reasoning-and-argument/SKILL.md` so claims, warrants, assumptions, countercases, implications, and business-sense checks are visible
6. After all waves: run `cross-cohort-synthesis` (orchestrator only)
7. Generate Word doc via `research-report-builder` → `python-document-generation`

## Skill loading

Every skill ships:
- `SKILL.md` — canonical instructions
- `AGENTS.md` — runtime-specific notes
- `README.md` — human overview
- `CLAUDE.md` — Claude-Code notes (ignored by non-Claude runtimes)
- `references/` — deep-dive references

## Sequential fallback

If parallel sub-task dispatch is not available, run waves sequentially:

1. Wave 1 per cohort
2. Wave 2 gap-fill per cohort
3. Wave 3 verification
4. Wave 4 synthesis (orchestrator only)

## Output paths

```
projects/<project-id>/_context/
projects/<project-id>/_registry/
projects/<project-id>/05-output/<output-family>/manifest.md
projects/<project-id>/export/
projects/<project-id>/<cohort>/research/
projects/<project-id>/<cohort>/analysis/
projects/<project-id>/<cohort>/opportunities/
projects/<project-id>/report-v<N>-<date>.docx
```

## Project structure invariants

- Every kernel project: `README.md`, `CLAUDE.md`, `PROJECT-STATUS.md`, `EVIDENCE-AUDIT.md`, `_context/`, `_registry/`, `01-initiation/` through `06-governance/`, `export/`
- Every cohort sub-project: `README.md`, `CLAUDE.md`, `research/`, `analysis/`, `opportunities/`

## Kernel commands

1. `python -m engine doctor`
2. `python -m engine new-project "<name>" --type "<research-type>" --audience "<audience>" --variant "<variant>"`
3. `python -m engine sync <project-id>`
4. `python -m engine status <project-id>`
5. `python -m engine validate <project-id>`
6. `python -m engine assemble <project-id> <output-family>`
7. `python -m engine pack <project-id> --out export/<project-id>.zip`

## See also

- `CLAUDE.md` — the Claude-Code-specific equivalent
- `PROJECT_BRIEF.md` — engine mission
