# Claude-specific guidance — evidence-discipline

This is the most important rule in this engine. Apply it on every project.

## When briefing sub-agents

**Always include the verbatim hard-constraint clause from `SKILL.md` in every research-agent prompt.** Without it, agents default to plausible-sounding filler when sources run thin.

## Verification before merging sub-agent output

Before writing sub-agent findings to project files:

1. Spot-check 10% of statistics with `WebFetch` against the cited URL
2. Spot-check 5 verbatim quotes — confirm exact text in source
3. Verify court cases on Kenyalaw / ULII / TanzLII / RwandaLII
4. Confirm named organisations actually exist
5. `WebFetch` URLs to confirm liveness (or at least HEAD-check)

If verification fails, **strike the affected content** rather than letting it pass.

## When the user asks for "more detail" on a thin section

The instinct is to elaborate. Don't. Either:
- Find a real new source and cite it
- Or restate the existing source's claim more thoroughly
- Never embellish with plausible-sounding additions

## Maintenance

Each project keeps an `EVIDENCE-AUDIT.md` logging caught hallucinations. Update it whenever a fabrication is caught, before fixing it. This is institutional memory.

See `SKILL.md`.
