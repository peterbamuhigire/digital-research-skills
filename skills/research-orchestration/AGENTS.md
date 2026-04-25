# Codex / generic-agent guidance — research-orchestration

For Codex and other agent runtimes that consume skills via `AGENTS.md`:

## Capability requirements

- Multi-agent dispatch (or sequential simulation if parallel unavailable)
- Web fetch / search tool
- File write capability for project tree
- Background-task support preferred (not required)

## Sequential fallback

If parallel sub-agents aren't available, run the same waves sequentially in this order:

1. Wave 1 per cohort (one cohort at a time)
2. Wave 2 gap-fill per cohort
3. Wave 3 verification
4. Wave 4 synthesis

The wave structure and agent-brief shape from `SKILL.md` apply unchanged.

## Output paths

Skill output is written to:

```
projects/<project-id>/<cohort>/research/
projects/<project-id>/<cohort>/analysis/
projects/<project-id>/<cohort>/opportunities/
```

See `SKILL.md` for canonical instructions.
