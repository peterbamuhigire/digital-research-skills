# AGENTS.md — digital-research-engine

The shared agent, command, hook, evidence, and handoff contract is adapted to
research in [`docs/control-plane-adoption.md`](docs/control-plane-adoption.md);
the central registry lives in `C:\wamp64\www\skills-web-dev\docs\engine-control-plane.json`.

Operating instructions for Codex and other agent runtimes that load skills via `AGENTS.md`.

## The one rule that overrides everything

**Do not hallucinate.** No claim, statistic, quote, name, court case, statute, organisation, or URL appears in any output unless it can be traced to a real source.

Read `skills/source-evaluation/SKILL.md` and `skills/source-evaluation/references/evidence-discipline.md` before any research work. The hard-constraint clause from that reference **must appear verbatim** in every sub-task agent prompt you dispatch.

## Standard workflow

Kaizen is mandatory for this engine and every research product. Load
`docs/continuous-improvement/portfolio-kaizen-standard-2026-08.md`; publish audits at a hard
maximum of 65/100 and remediation plans targeting 95/100. For book or source intake, record
provenance, completeness, limitations, and whether the material is current before synthesis.

1. Load `skills/source-evaluation/SKILL.md` + `skills/source-evaluation/references/evidence-discipline.md` → enforce throughout
2. Load `skills/research-orchestration/SKILL.md` → drives wave planning
3. For each cohort: dispatch a research sub-task with the standard brief structure
4. After each wave: run `source-verification` and `gap-analysis`
5. Before synthesis or final drafting: run `skills/critical-reasoning-and-argument/SKILL.md` so claims, warrants, assumptions, countercases, implications, and business-sense checks are visible
6. After all waves: run `cross-cohort-synthesis` (orchestrator only)
7. If the final output is a **proposal** (donor investment case, policy memo, bid, EoI, pitch deck, Cabinet memo, Parliamentary briefing, white paper): route the drafting stage through `skills/proposal-skills/skills/SKILL.md` (parent router) and the relevant section sub-skills (`01-cover-letter` through `10-financial-proposal`) plus cross-cutting domain skills (methodology, M&E, risk, GESI, sustainability, change-management, critical-analysis-business-logic, premium-commercial-writing). Load exactly one profile under `skills/proposal-skills/skills/profiles/` before drafting.
8. Generate Word doc via `research-report-builder` → `python-document-generation`
9. Apply `skills/anti-ai-slop/SKILL.md` in real time on every output, and run `skills/ai-slop-audit/SKILL.md` after each major iteration and as the final ship gate. Outputs must read as if a professional human researcher wrote them; grade F (fabricated stat/citation, viewpoint-free section, template uniformity, banned vocabulary) blocks delivery.

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

## Skill authoring and release gates

Run `python -X utf8 scripts/validate_source_currency.py tests/fixtures/source-currency.json`
for the deterministic currentness gate. Time-sensitive source records require
verification and review dates; overdue records block release.

- Discover active skills from the filesystem below `skills/`; exclude the `skills/proposal-skills` Git submodule because it is a separate engine. Do not use a README table as inventory.
- Follow `docs/skill-authoring-standard.md` and begin new skills from `templates/skill-template/SKILL.md`.
- Preserve the 58-skill active catalogue unless an independently justified routing change requires a count change.
- Run `python -X utf8 scripts/skill_contract_validator.py --baseline tests/skill-engine/quality-baseline.json`, `python -X utf8 scripts/routing_smoke_test.py`, and `python -X utf8 scripts/validate_engine.py` before release.
- Run the canonical `quick_validate.py` against every changed skill directory. A missing capability or unavailable check is `not assessed`, never passed.

## See also

- `CLAUDE.md` — the Claude-Code-specific equivalent
- `PROJECT_BRIEF.md` — engine mission

<!-- design-system-skills:trigger v1 -->
### Design / typography / UI/UX (cross-cutting — consult IN ADDITION)

Any work touching how an artifact LOOKS — font/typeface choice, type scale, colour, layout/grid,
visual identity, web/desktop/mobile UI screens, or the visual formatting of a DOCX/PPTX/PDF/XLSX
— routes to the **`design-system-skills`** engine, the single home for ALL design/UI/UX skills
and the anti-AI-slop doctrine.

**Resolve its location on THIS device from your global engine-routing table** (`~/.claude/CLAUDE.md`,
or `AGENTS.md` for Codex) — never assume an absolute path; it varies per machine. Then read its
`README.md` → `doctrine/design-doctrine.md` → glob `skills/**/SKILL.md` fresh and route by
frontmatter (read SKILL.md directly, not via the Skill tool). Content and structure stay in THIS
engine; presentation comes from design-system-skills. Hard rule: never use a banned AI-slop font
(Inter, Geist, Roboto, Arial, Open Sans, Lato, Space Grotesk, bare system stacks) as primary
type — state the chosen typeface and reason before producing any artifact.
<!-- /design-system-skills:trigger -->
