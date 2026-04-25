# Claude-specific guidance — source-verification

- Use `WebFetch` to verify URL liveness on tier-1/2 sources before quoting their statistics.
- Use `Grep` on the project's `sources.md` files to find duplicate citations across cohorts (signal of cross-cohort triangulation).
- Use `Read` on draft reports to audit citation strength before generating the Word output.

## Tier-tagging in practice

When writing `<cohort>/research/sources.md`, group by tier so an auditor can see balance at a glance:

```markdown
## Tier 1 — Academic & official statistics
- ...

## Tier 2 — Regulatory & institutional
- ...

## Tier 3 — Established journalism
- ...
```

See `SKILL.md` for the full ladder.
