# Claude-specific guidance — research-orchestration

When operating inside Claude Code:

- Use the `Agent` tool with `subagent_type: content-marketing:search-specialist` (or `general-purpose` if that plugin isn't available) for each research wave.
- **Run independent waves in parallel** — emit multiple `Agent` tool calls in a single message rather than serialising.
- Use `run_in_background: true` for waves that take >2 minutes; you'll be notified on completion.
- **Never** read sub-agent output files directly with the shell tool — they overflow context. Wait for the completion notification and use the structured `<result>` block.
- Brief each agent self-contained — they don't see the prior conversation.
- After each wave, write the cohort's `research/` files using the Write tool. Append (don't overwrite) when merging Wave-2 findings.

## Filtering out scope exclusions

If the user has set a hard constraint (e.g., "exclude topic X"), restate it verbatim in the agent's prompt. If the agent returns it anyway, filter it out before writing files. Never let scope leak through.

## Cost control

- Each Wave-1 agent costs roughly 60–90k tokens
- Each Wave-2 agent costs roughly 70–100k tokens
- Plan accordingly — don't fire 4 Wave-2 agents speculatively

See `SKILL.md` for the canonical workflow.
