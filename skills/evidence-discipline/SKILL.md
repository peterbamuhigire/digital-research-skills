---
name: evidence-discipline
description: NON-NEGOTIABLE GUARDRAIL — use on every research output to prevent AI hallucination, fabricated statistics, invented quotes, plausible-sounding fiction, or unattributed claims from reaching final reports. Applies to every skill, every wave, every report in this engine.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
  priority: critical
---

# Evidence discipline — anti-hallucination guardrail

**This is the most important rule in the engine.** Every other skill defers to it.

## The core rule

**No claim, statistic, quote, citation, name, date, organisation, court case, regulation, or URL appears in any output unless it can be traced back to a real, verified source.**

If you cannot cite it, you cannot say it.

## Five forbidden behaviours

1. **Fabricating statistics** — never invent percentages, sample sizes, dates, or amounts to make a paragraph feel concrete
2. **Inventing quotes** — never write "an X resident said..." without a real, attributable source
3. **Hallucinating organisations / cases / laws** — never name a tribunal case, NGO, statute, or operator that you can't link to
4. **Plausible-sounding fiction** — never fill a coverage gap with what *probably* happens; admit the gap
5. **Citation drift** — never let a real source's claim mutate. The number you cite must match the number in the source.

## Five required behaviours

1. **Cite at point of claim**, not just in a bibliography. A statistic without an inline citation is treated as unverified.
2. **Mark inferences explicitly.** "(inference)" or "(estimated)" — never disguise reasoning as fact.
3. **Mark gaps explicitly.** Better to write "no published data found" than to fabricate filler.
4. **Mark paraphrase explicitly.** "(paraphrased)" — never present synthesis as a direct quote.
5. **Verify before quoting.** When a sub-agent returns a verbatim quote, confirm it exists in the cited source before publishing.

## Severity tiers

| Severity | Example | Response |
|---|---|---|
| Critical | Fabricated statute, court case, tribunal ruling | Strike from output; investigate sub-agent prompt |
| Critical | Invented direct quote attributed to a named person | Strike; mark agent untrusted for the project |
| High | Statistic without cited source | Either find the source or remove the statistic |
| High | Named organisation that doesn't exist | Strike; investigate |
| Medium | URL that 404s or is for a different page | Replace or remove |
| Medium | Date drift (year off by one) | Correct against source |
| Low | Mild paraphrase tightening | Mark with "(paraphrased)" |

## Verification routine

For every research output before it ships:

1. **Random spot-check 10% of statistics** — open the cited URL, confirm the number matches
2. **Random spot-check 5 quotes** — confirm verbatim text appears in source
3. **All court cases / statute citations** — verify on Kenyalaw / ULII / TanzLII / RwandaLII
4. **Named persons / organisations** — confirm they exist (not invented combos like "Acorn Estate Agents Ltd" when the real name is "Acorn Holdings")
5. **All URLs** — `WebFetch` or HEAD-check; replace dead links

## Sub-agent briefing — required boilerplate

Every research-agent prompt **must include this clause verbatim**:

```
HARD CONSTRAINT — NO HALLUCINATION:
- Do NOT invent statistics, names, organisations, court cases, statutes, or URLs.
- Cite every numeric claim and every direct quote at the point it appears.
- If you cannot find a source for a fact, mark it as a "gap" — do not fabricate filler.
- For any claim you assemble from multiple sources, mark it "(synthesis)".
- For any inference, mark it "(inference)".
- Verbatim quotes must reproduce text exactly as it appeared in the source — no creative editing.
- If a search returns nothing, report "no source found" — do not write what is plausible.
```

If a sub-agent's output appears to violate this clause, treat the entire output as suspect.

## Anti-patterns

- "Reports suggest..." with no report named
- "Studies show..." with no study cited
- "It is estimated that..." with no estimator
- "Industry sources say..." without naming the industry source
- Round numbers presented as if measured (e.g., "60% of tenants" with no underlying study — likely fabricated unless the source is named)
- Court case names that follow a real format but aren't on Kenyalaw / ULII (the format `Komakech & 7 Ors v Ayaa & Anor 2018` is real; the format `Mwangi v Otieno 2019` could be fabricated — verify before citing)

## What "evidence-discipline" is not

- It is not a bar against synthesis. Synthesis is allowed; it must be marked.
- It is not a bar against inference. Inference is allowed; it must be marked.
- It is not a bar against gap-flagging. Flagging gaps is the *point*.
- It is not a tier requirement. A tier-5 social post can be cited if attributed honestly.

## Integration with the rest of the engine

- `research-orchestration` — the boilerplate clause above goes into every sub-agent brief
- `source-verification` — feeds the verification routine
- `quote-extraction` — verbatim discipline overlaps directly
- `gap-analysis` — gaps are findings, not embarrassments to be filled
- `research-report-builder` — runs the verification routine before .docx export
- `cross-cohort-synthesis` — synthesis must remain traceable to underlying claims

## Failure mode log

When a hallucination is caught in review, log it in the project's `EVIDENCE-AUDIT.md`:

```markdown
## YYYY-MM-DD
- Source agent / wave: ...
- Fabricated content: "..."
- Caught by: <human reviewer | spot-check | URL-fetch | source-grep>
- Action: <strike | flag | replace>
- Lesson: <what should change in the next prompt>
```

This is the engine's institutional memory against drift.

## See also

- `source-verification` — credibility tiers
- `quote-extraction` — verbatim discipline
- `research-orchestration` — sub-agent briefing
