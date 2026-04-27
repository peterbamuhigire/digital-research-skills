# Research engine skills expansion — design

**Date:** 2026-04-27
**Author:** Claude (with Peter)
**Status:** Approved, building

## Goal

Add three new skills to the digital-research-engine, derived from eight reference EPUBs the user supplied, covering:

1. Online legal research
2. Systems thinking & mental models
3. Mind mapping & synthesis

Each skill follows the engine's existing **hybrid** shape: one `SKILL.md` plus a rich `references/` directory loaded on demand.

## Source materials

Located in `C:\Users\Peter\Downloads\`:

**Legal**
- *Legal Research, Analysis and Writing* — Putman & Albright (LRAW)
- *Legal research using the Internet* — Judy A. Long
- *Legal Research* (anonymous compendium)

**Systems thinking**
- *Systemic Thinking — building maps for worlds of systems* — Boardman & Sauser
- *Thinking in Systems and Mental Models* (anon., decision-science primer)
- *Thinking — The New Science of Decision-Making, Problem-Solving, and Prediction* — Brockman (ed.)

**Mind mapping & study**
- *Mind Map Mastery* — Tony Buzan
- *Buzan Study Skills Handbook* — Tony Buzan

## Design decisions (locked)

| Question | Decision |
|---|---|
| Granularity | **C** — three umbrella skills, hybrid pattern (SKILL.md + references/) |
| Legal jurisdiction posture | **C** — method-first, jurisdiction-agnostic core + East African overlay |
| Mind-map output format | **A+C** — method-only teaching + Mermaid `mindmap` artifacts as the engine-native deliverable |
| Systems framework lead | **C** — three co-equal toolkits; SKILL.md is a router |

## Skill 1 — `online-legal-research`

**Trigger description:** Use when the research question turns on statutes, regulations, case law, court decisions, legal authority, or jurisdictional analysis — including identifying primary vs secondary sources, validating legal currency, applying IRAC, and constructing legal citations.

**SKILL.md contents:** Decision flow — identify legal question → locate primary authority → triangulate with secondary → validate currency → analyse with IRAC → cite-check.

**references/**
- `source-hierarchy-and-authority.md`
- `online-research-workflow.md`
- `legal-analysis-irac.md`
- `citation-and-quoting-discipline.md`
- `east-african-overlay.md`

**Posture:** No invented case names, statutes, or citations. The East African overlay names *types* of sources (national law reports, gazettes, Hansard, court repositories) without fabricating specific entries.

## Skill 2 — `systems-thinking-and-mental-models`

**Trigger description:** Use when mapping system behaviour, stakeholder dynamics, root cause, feedback loops, leverage points, or when the analyst needs a structured mental-model checklist or decision-science heuristic for forecasting/judgement.

**SKILL.md contents:** Router. Behaviour/stakeholder maps → systemigram. Dynamics/policy → causal loop diagram. Analyst reasoning checklists → mental-models catalog. Forecasting/judgement → decision-science heuristics.

**references/**
- `systemigrams.md`
- `causal-loops-and-leverage-points.md`
- `mental-models-catalog.md`
- `decision-science-heuristics.md`

## Skill 3 — `mind-mapping-and-synthesis`

**Trigger description:** Use when synthesising a literature pass, taxonomising findings across cohorts, planning a research wave, or when an analyst needs Buzan-style radial organisation to compress a corpus into a navigable map.

**SKILL.md contents:** When to mind-map vs linear notes. Buzan's seven-step method adapted for research synthesis. How to translate Buzan's color/imagery into Mermaid styling without losing cognitive benefit.

**references/**
- `mind-map-construction.md`
- `study-and-recall-techniques.md`
- `mermaid-mindmap-patterns.md`

## Cross-cutting conventions

1. Every new skill embeds the `source-evaluation` hard-constraint clause verbatim (per project `CLAUDE.md`).
2. Each skill ships with `SKILL.md`, `README.md`, `CLAUDE.md`, `AGENTS.md`, `references/`.
3. Every references file dates itself and lists which book(s) it draws from.
4. No fabricated facts. Method only when sources don't support a specific claim.
5. EPUB extraction artifacts staged in `skills/_extraction-cache/` (gitignored, scratch only).

## Build order

1. Extract text from all 8 EPUBs (pandoc → markdown, staged in `_extraction-cache/`)
2. Build `online-legal-research` (largest source corpus → highest extraction effort first)
3. Build `systems-thinking-and-mental-models`
4. Build `mind-mapping-and-synthesis`
5. Update any skill index, commit per skill (local only — do not push without explicit ask)

## Out of scope

- Direct `.docx` skill output — Word generation remains via existing `professional-word-output` / `python-document-generation` skills
- New jurisdictions beyond US-method + East African overlay
- Visual mind-map rendering beyond Mermaid (Markmap/OPML mentioned in references but not core)
