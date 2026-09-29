# Claude Code repository memory

@AGENTS.md

## Claude-only notes

- Dispatch research waves with the `Agent` tool, `subagent_type: content-marketing:search-specialist`
  (or `general-purpose` if unavailable); one sub-agent per cohort.
- Run independent waves as multiple `Agent` tool calls in one message.
- Use background mode (`run_in_background: true`) for waves longer than 2 minutes.
- Never read sub-agent transcripts or output files directly with the shell tool (no `Bash`-based
  tail) — they overflow context. Use the structured `<result>` block in the completion notification.
- Tools to use heavily: `Agent` for every research wave; `WebFetch` for URL verification, statistic
  re-check and abstract retrieval; `Read` for cross-checking draft outputs; `Write` / `Edit` for the
  markdown corpus; `Grep` for finding duplicate citations across cohorts (signals triangulation).
