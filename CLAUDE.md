# CLAUDE.md — digital-research-engine

Operating instructions for Claude Code working inside this engine.

## The one rule that overrides everything

**Do not hallucinate.** No statistic, quote, name, court case, statute, organisation, or URL appears in any output unless traceable to a real source.

This is enforced by the `source-evaluation` skill — read `skills/source-evaluation/SKILL.md` and `skills/source-evaluation/references/evidence-discipline.md` before doing any research work. The hard-constraint clause from that reference **must appear verbatim** in every sub-agent prompt you dispatch.

If a sub-agent returns content that violates evidence discipline, strike it. Do not paper over with fixes — log it in the project's `EVIDENCE-AUDIT.md` and adjust the next agent prompt.

## Standard research workflow

Triggered by user requests like "research X", "find pain points of Y", "do another pass":

1. **Plan the waves.** One sub-agent per cohort. Use `Agent` tool with `subagent_type: content-marketing:search-specialist` (or `general-purpose` if unavailable).
2. **Brief each agent self-contained.** They don't see the conversation history. Include:
   - Goal, scope, out-of-scope
   - Themes to cover (numbered)
   - Sources to mine (named)
   - Deliverable shape
   - **Verbatim** hard-constraint clause from `source-evaluation/references/evidence-discipline.md`
3. **Run in parallel where independent.** Multiple `Agent` tool calls in one message.
4. **Use background mode (`run_in_background: true`)** for waves >2 minutes.
5. **Never read sub-agent transcripts directly with the shell tool** — they overflow context. Use the structured `<result>` block in the completion notification.
6. **Verify before merging.** Spot-check 10% of stats, 5 quotes, all court cases / statute citations.
7. **Run critical reasoning before synthesis or final drafting.** Use `skills/critical-reasoning-and-argument/SKILL.md` to make claims, warrants, assumptions, countercases, implications, and business-sense checks visible.
8. **Write outputs** to `projects/<project-id>/<cohort>/research/`, `analysis/`, `opportunities/` — append (don't overwrite) when merging Wave-2 findings.
9. **After all cohorts complete**, run `cross-cohort-synthesis` (orchestrator does this — never delegate).
10. **Generate the Word doc** via `research-report-builder` → `professional-word-output` or `python-document-generation`.
11. **Run the anti-slop ship gate.** Before delivering any report or `.docx`, run `ai-slop-audit` on it. The output must read as if a professional human researcher wrote it: sourced at every claim, with authored judgement, varied structure, no banned vocabulary, and the counter-case shown. Grade F (a fabricated stat/citation, a viewpoint-free section, template uniformity) blocks delivery until fixed.

## Skill priority order

For any non-trivial task:

0. `anti-ai-slop` — real-time, every output, every time. The quality counterpart to evidence-discipline: a report can be fully sourced and still read as slop (generic, voiceless, template-uniform). Apply continuously while writing. Run `ai-slop-audit` after each major iteration (drafted section, completed cohort, synthesis, generated .docx); grade F blocks progression.
1. `evidence-discipline` — every output, every time
2. `research-orchestration` — coordinates the rest
3. The specialist skill matching the task (e.g., `regulatory-landscape-mapping` for legal research)
4. `source-verification` + `quote-extraction` after every wave
5. `critical-reasoning-and-argument` before synthesis, recommendation, business analysis, or final output
6. `gap-analysis` before any "is this complete?" claim
7. `pain-point-taxonomy` after evidence is gathered
8. `cross-cohort-synthesis` only when ≥2 cohorts complete
9. `research-report-builder` last

## File-write conventions

- **Append, don't overwrite** when merging Wave-2 findings into existing files. Use `# Pass 2 — Gap-fill addendum` headers.
- **Never delete a sourced claim** without logging in `EVIDENCE-AUDIT.md`.
- **Mark gaps explicitly** — "no source found" is a valid finding; filler text is not.
- **Date every research file** at the top.
- **List sources by tier** in `<cohort>/research/sources.md` (per `source-verification`).

## Scope-exclusion discipline

If the user has set a hard exclusion (e.g., "do not cover topic X"):

- Restate it verbatim in every sub-agent brief
- If a sub-agent returns it, filter before writing files
- Track the exclusion in the project's `README.md` so it doesn't quietly close in later passes

## When the user asks for elaboration

Default reflex: find a new source. Acceptable alternatives: restate existing source more thoroughly, or acknowledge the gap. **Never embellish with plausible-sounding additions.**

## Tools to use heavily

- `Agent` — for every research wave
- `WebFetch` — for URL verification, statistic re-check, abstract retrieval
- `Read` — for cross-checking draft outputs
- `Write` / `Edit` — for the markdown corpus
- `Grep` — for finding duplicate citations across cohorts (signals triangulation)

## Tools to avoid

- `Bash`-based tail of sub-agent output files — overflows context
- Direct `.docx` editing — markdown source is canonical, Word is generated

## Project structure invariants

- Every project lives under `projects/<project-id>/`
- Every kernel project has `README.md`, `CLAUDE.md`, `PROJECT-STATUS.md`, `EVIDENCE-AUDIT.md`, `_context/`, `_registry/`, `01-initiation/` through `06-governance/`, and `export/`
- Every cohort sub-project has `README.md`, `CLAUDE.md`, plus `research/`, `analysis/`, `opportunities/`
- Final report is `projects/<project-id>/report-v<N>-<date>.docx`

## Kernel workflow

Use these commands for project-managed work:

1. `python -m engine doctor`
2. `python -m engine new-project "<name>" --type "<research-type>" --audience "<audience>" --variant "<variant>"`
3. Run `00-meta-initialization` and complete `_context/`
4. `python -m engine sync <project-id>`
5. `python -m engine status <project-id>`
6. `python -m engine validate <project-id>`
7. `python -m engine assemble <project-id> <output-family>`
8. `python -m engine pack <project-id> --out export/<project-id>.zip`

## Skill authoring and release gates

- Discover active skills from the filesystem below `skills/`. The standalone proposal engine is routed through the global engine table and is not part of this repository's catalogue. Do not use a README table as inventory.
- Follow `docs/skill-authoring-standard.md` and begin new skills from `templates/skill-template/SKILL.md`.
- Preserve the 58-skill active catalogue unless an independently justified routing change requires a count change.
- Run `python -X utf8 scripts/skill_contract_validator.py --baseline tests/skill-engine/quality-baseline.json`, `python -X utf8 scripts/routing_smoke_test.py`, and `python -X utf8 scripts/validate_engine.py` before release.
- Run the canonical `quick_validate.py` against every changed skill directory. A missing capability or unavailable check is `not assessed`, never passed.

## Proposal-output trigger

When a research project's output is a **proposal** — donor investment case, policy memorandum, bid response, expression of interest, pitch deck, Cabinet memo, Parliamentary briefing, white paper, or other persuasive document for an external audience — route the final-drafting stage through the standalone proposal engine at `C:\wamp64\www\proposal-skills`.

- Parent router: `C:\wamp64\www\proposal-skills\skills\SKILL.md`
- Section sub-skills: `C:\wamp64\www\proposal-skills\skills\pipeline\01-cover-letter\` through `10-financial-proposal\`
- Cross-cutting skills: follow the parent router into `domain-delivery`, `strategy-positioning`, `writing-content`, and other applicable families.
- Profiles: load `C:\wamp64\www\proposal-skills\skills\profiles-sectors\profiles\SKILL.md` before drafting.
- Language standards: British English; East African professional tone; day-month-year dates; apply the proposal engine's anti-slop and language gates.

The proposal engine evolves in its own repository and is updated independently from `C:\wamp64\www\proposal-skills`.

The research evidence corpus produced by the engine (under `projects/<project-id>/02-research/`, `04-synthesis/`) is the input to the proposal-skills drafting pipeline; the proposal document is written into `projects/<project-id>/05-output/` and exported via the standard `research-report-builder` → `python-document-generation` chain.

## See also

- `AGENTS.md` — Codex / generic-agent equivalent of this file
- `PROJECT_BRIEF.md` — engine mission & direction
- `skills/source-evaluation/SKILL.md` + `skills/source-evaluation/references/evidence-discipline.md` — the rule that precedes everything else
- `C:\wamp64\www\proposal-skills` — standalone proposal engine for projects whose output is a proposal

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
