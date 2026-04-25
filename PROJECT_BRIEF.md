# PROJECT_BRIEF — digital-research-engine

## Mission

Build a **world-class research engine** — multi-agent, evidence-disciplined, portable across AI runtimes — that produces world-class research, status, intelligence, evaluation, and decision-support reports for diverse audiences and purposes.

This is not a document-generator. It is a research operating system. The Word document is one of many possible outputs.

## Audiences served

The engine produces work for distinct audiences with distinct standards:

- **Designers, product managers, founders** — pain-point and product research that informs new systems
- **Investors, M&A, lenders** — due-diligence and market-landscape research that informs capital decisions
- **Strategists, forecasters, planners** — trend research that informs scenario planning
- **Policy-makers, advocates, NGOs** — policy / regulatory research and single-cohort deep-dives
- **Journalists, researchers, academics** — historical research and OSINT
- **Security, integrity, brand teams** — OSINT and reputational research
- **Communications, brand, monitoring teams** — social-media and sentiment research
- **Internal decision-makers and external clients** — comparative / benchmarking research

Each audience has different tolerance for inference, different citation expectations, and different report shape requirements.

## Research types supported (15 types, 19 schemas)

The engine supports — and selects between — fifteen distinct research types. Four of them come in academic + popular variants, yielding nineteen report schemas in total.

### Investigative / analytical (11)
1. Pain-point research (multi-cohort)
2. Single-cohort deep-dive
3. Market / industry landscape
4. Comparative / benchmarking
5. Social-media / sentiment research
6. Due diligence
7. OSINT (open-source intelligence)
8. Product research
9. Historical research
10. Trends research
11. Policy / regulatory research

### Long-form scholarly outputs (4 types × 2 variants = 8 schemas)
12. Master's / honours thesis (academic | popular)
13. Paper / journal article (academic | popular long-form)
14. PhD dissertation (academic | popular book)
15. Essay (academic | popular)

Each maps to a specific orchestration approach, methodology skill set, and report schema (A–S). The `research-type-router` skill handles selection upfront before any sub-agent fires.

## Non-negotiable

**Anti-hallucination guardrail.** No claim, statistic, quote, name, court case, statute, organisation, or URL appears in any output unless traceable to a real source. The `evidence-discipline` skill takes precedence over every other rule in the engine. Each project keeps a running `EVIDENCE-AUDIT.md` log of caught fabrications, corrections, and verification status.

## Design principles

1. **Type-routing first.** Pick the research type before the first sub-agent fires.
2. **One cohort per agent.** Don't muddle perspectives in a single research wave.
3. **Plan in waves.** Broad sweep → gap fill → verification → synthesis.
4. **Synthesis is the orchestrator's job.** Never delegate it.
5. **Markdown is canonical.** Word docs are generated from markdown source.
6. **Tier every source.** A 5-level credibility ladder runs from peer-reviewed academic down to social-platform.
7. **Mark uncertainty explicitly.** "(synthesis)", "(inference)", "(paraphrased)", "(gap)".
8. **Skills are portable.** Every skill ships with `SKILL.md`, `README.md`, `CLAUDE.md`, `AGENTS.md`.
9. **Skill priority is fixed.** `evidence-discipline` first, always.
10. **Audience drives tone.** Internal-design tone is direct; client-deliverable tone is formal; due-diligence tone is legalistic; advocacy tone is evidence-heavy.

## Skill inventory (engine-native)

### Tier 1 — Always loaded
- `evidence-discipline` — anti-hallucination guardrail (precedes everything)
- `research-type-router` — selects research type and report schema
- `research-orchestration` — coordinates multi-wave dispatch
- `source-verification` — credibility tiers + triangulation
- `quote-extraction` — verbatim attribution discipline
- `gap-analysis` — corpus-coverage audit + Wave-2 briefing

### Tier 2 — Loaded per research type
- `pain-point-taxonomy` — for pain-point and product research
- `cross-cohort-synthesis` — for multi-cohort projects
- `regulatory-landscape-mapping` — for policy / regulatory research
- `academic-source-mining` — for any project needing tier-1 academic sources
- `social-source-extraction` — for social-media / sentiment research
- `due-diligence-framework` — for due-diligence projects
- `osint-methodology` — for OSINT projects
- `trend-analysis` — for trend research
- `historical-research-methods` — for historical research
- `academic-writing-conventions` — for theses, dissertations, papers, academic essays
- `academic-citation-styles` — for any academic variant (Schemas L, N, P, R)

### Tier 3 — Final-output assembly
- `research-report-builder` — markdown → designed Word doc with 19 schemas (A–S)

## Repository

https://github.com/peterbamuhigire/digital-research-skills

## Roadmap

- v0.1 (current) — engine scaffolded; first project (`east-africa-property-hostel`) complete through Wave 2 on all four cohorts; cross-cohort synthesis written; EVIDENCE-AUDIT framework live
- v0.2 — generate the first Word-document report for the active project; close the markdown→docx loop
- v0.3 — second project to validate the engine generalises beyond the property/hostel domain (likely a due-diligence or trend project to stress-test type variety)
- v0.4 — fill in `references/` deep-dives for the 11 new methodology skills
- v0.5 — formalise the `EVIDENCE-AUDIT.md` review-loop discipline; add automated URL-liveness CI check
- v0.6 — open the engine to additional AI runtimes beyond Claude Code and Codex; verify portability claim

## Engine status

| Aspect | Status |
|---|---|
| 16 engine skills | scaffolded with SKILL/README/CLAUDE/AGENTS |
| 14 supporting skills (skill-building, doc, language) | imported from `~/.claude/skills` and `business-plan-skills` |
| First project | 4 cohorts × Wave 1 + Wave 2 (students/owners), Wave 1 + Wave 2 (landlords/tenants) |
| Word-document export | not yet generated |
| Evidence audit | active; 8 verified items, 4 corrections applied, 7 gaps remaining |
| Git | initialised + committed; pushed to GitHub |

Maintained by Peter Bamuhigire.
