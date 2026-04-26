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
7. **Write outputs** to `projects/<project-id>/<cohort>/research/`, `analysis/`, `opportunities/` — append (don't overwrite) when merging Wave-2 findings.
8. **After all cohorts complete**, run `cross-cohort-synthesis` (orchestrator does this — never delegate).
9. **Generate the Word doc** via `research-report-builder` → `professional-word-output` or `python-document-generation`.

## Skill priority order

For any non-trivial task:

1. `evidence-discipline` — every output, every time
2. `research-orchestration` — coordinates the rest
3. The specialist skill matching the task (e.g., `regulatory-landscape-mapping` for legal research)
4. `source-verification` + `quote-extraction` after every wave
5. `gap-analysis` before any "is this complete?" claim
6. `pain-point-taxonomy` after evidence is gathered
7. `cross-cohort-synthesis` only when ≥2 cohorts complete
8. `research-report-builder` last

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

## See also

- `AGENTS.md` — Codex / generic-agent equivalent of this file
- `PROJECT_BRIEF.md` — engine mission & direction
- `skills/source-evaluation/SKILL.md` + `skills/source-evaluation/references/evidence-discipline.md` — the rule that precedes everything else
