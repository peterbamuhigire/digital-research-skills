# PROJECT_BRIEF — digital-research-engine

## Mission

Build a portable, multi-agent **skills engine** for evidence-disciplined web research that produces designed Word-document reports. Usable by Claude Code, Codex, and any other agent runtime that consumes `SKILL.md` / `AGENTS.md` skills.

## Non-negotiable

**Anti-hallucination guardrail.** Every claim, statistic, quote, name, court case, statute, organisation, and URL in every output must be traceable to a real source. The `evidence-discipline` skill takes precedence over every other rule in the engine.

## Design principles

1. **One cohort per agent.** Don't muddle perspectives in a single research wave.
2. **Plan in waves.** Broad sweep → gap fill → verification → synthesis.
3. **Synthesis is the orchestrator's job.** Never delegate it.
4. **Markdown is canonical.** Word docs are generated, never authored.
5. **Tier every source.** A 5-level credibility ladder runs from peer-reviewed academic down to social-platform.
6. **Mark uncertainty explicitly.** "(synthesis)", "(inference)", "(paraphrased)", "(gap)".
7. **Skills are portable.** Every skill ships with `SKILL.md`, `README.md`, `CLAUDE.md`, `AGENTS.md`.
8. **Skill priority is fixed.** `evidence-discipline` first, always.

## Repository

https://github.com/peterbamuhigire/digital-research-skills

## Roadmap

- v0.1 (current) — first project (`east-africa-property-hostel`) complete through Wave 2 on 2 cohorts; Wave 1 on 2 cohorts
- v0.2 — generate the first Word-document report for the active project; close the markdown→docx loop
- v0.3 — second project to validate the engine generalises beyond the property/hostel domain
- v0.4 — fill in `references/` deep-dives for each new skill
- v0.5 — formalise the `EVIDENCE-AUDIT.md` review-loop discipline

Maintained by Peter Bamuhigire.
