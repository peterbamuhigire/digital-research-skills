# source-verification

Credibility tiering, triangulation, and quote-attribution discipline. Applies to every research corpus produced by the engine.

## What it does

- Tiers each source on a 5-level ladder (academic → regulatory → journalism → analyst → social)
- Enforces ≥2-source triangulation for high-impact claims
- Standardises quote attribution
- Flags URL liveness, date-staleness, and tier-5-only claims

## When to invoke

Triggered automatically by `research-orchestration` Wave 3, or manually when:
- Auditing a draft report for citation strength
- Resolving conflicting claims across sources
- Tightening a section before final Word-doc export

See `SKILL.md` for canonical instructions.
