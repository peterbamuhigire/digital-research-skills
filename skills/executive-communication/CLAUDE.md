# Claude-specific — executive-communication

- **Trigger.** Invoke this skill whenever the user asks for an executive summary, one-pager, slide deck, briefing note, cover memo, or proposal. Also invoke when restructuring a long-form report for a senior audience.
- **Read order.** Always read `SKILL.md` first; then load only the references the decision router specifies for the artefact at hand.
- **Hard rule.** Every section title in the output must be an action title (complete declarative sentence). If the user supplies a topic label ("Methodology", "Findings"), replace it with the takeaway sentence and explain why in one line.
- **Hard rule.** The governing thought appears in the first 50 words. If it doesn't, the artefact has failed the ship-gate; rewrite the opener.
- **Hard rule.** Every fact in the executive artefact must still tie back to the upstream research manifest (source + tier + confidence). Restructuring does not relax evidence-discipline.
- **Charts.** Pick the chart family for the message before opening any chart tool. If the message doesn't need a chart, don't add one.
- **Length.** Executive summary ≤ 300 words. One-pager ≤ 5 sentences in the opener. If the artefact won't fit, the governing thought is too large — split it.
- **Refuse to embellish.** This skill restructures; it never invents new claims. If the upstream research can't support a claim the executive output needs, raise it as a gap rather than fill with plausible content.

See `SKILL.md`.
