# research-orchestration

Coordinates multi-wave, multi-agent web research. The default driver of any non-trivial research task in the `digital-research-engine`.

## What it does

- Plans **waves** (broad sweep → gap fill → verification → synthesis)
- Splits cohorts to **separate agents** to avoid muddling
- Standardises the **agent brief structure** so output is consistent
- Defines where outputs land in the project tree

## When to invoke

Triggered by user requests like:

- "Research the pain points of X across Y region"
- "Do another thorough pass / gap-fill"
- "Synthesise across the cohorts we've researched"

## Compatibility

Portable across Claude Code, Codex, and generic agent runtimes. See `SKILL.md` for the canonical instructions.

## Files

- `SKILL.md` — canonical instructions
- `CLAUDE.md` — Claude-specific notes
- `AGENTS.md` — Codex / generic agent compatibility notes
- `references/` — deep-dive references (placeholders)
