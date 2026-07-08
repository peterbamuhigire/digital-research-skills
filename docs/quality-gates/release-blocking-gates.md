# Release-Blocking Quality Gates

Last verified: 2026-07-08

These gates apply before any research deliverable leaves the engine. A single critical failure blocks release.

## Gate 1 - Evidence discipline

Pass criteria:

- Every numeric claim, direct quote, named organisation, statute, case, date, and URL maps to a source ID.
- Every source has tier, confidence, accessed date, and verification method.
- Tier-5 claims are clearly attributed and triangulated before they become findings.

Critical failures:

- Fabricated statistic, quote, organisation, law, or case.
- Citation drift where a cited source does not support the claim.
- Dead URL with no archive or replacement for a load-bearing source.

## Gate 2 - Verification

Pass criteria:

- URL status checked.
- Archive availability checked or gap logged.
- Quotes exact-matched against source text where source text is available.
- Statistics spot-checked or marked unresolved.
- Unsupported claims quarantined before synthesis.

Critical failures:

- Direct quote not found in cited source.
- Claim registry references missing source IDs.
- Statistic asserted without source text or explicit gap note.

## Gate 3 - Analytic reasoning

Pass criteria:

- Findings separate fact, inference, synthesis, and recommendation.
- Key assumptions are listed.
- At least one alternative explanation is considered for contested judgments.
- Confidence language follows the engine lexicon.

Critical failures:

- Recommendation presented without warrant.
- Forecast stated as fact.
- Dissenting evidence omitted from a high-stakes conclusion.

## Gate 4 - Anti-slop and professional voice

Pass criteria:

- No generic preambles, filler transitions, or vague claims.
- Output is audience-specific and decision-relevant.
- Headings carry meaning, not template labels alone.
- Length fits the deliverable norm.

Critical failures:

- "Studies show" or "experts say" without evidence.
- Boilerplate section that could fit any client.
- AI-default hedging that weakens sourced findings.

## Gate 5 - Output completeness

Pass criteria:

- Final output, evidence table, source register, verification report, gap register, and reviewer notes exist.
- Any unresolved gaps are explicit and decision-relevant.
- Cross-engine handoffs are documented when design, finance, legal, security, spreadsheets, or document generation are involved.

Critical failures:

- Final deliverable separated from its evidence pack.
- No reviewer or verification manifest.
- Compliance-sensitive content missing last-verified date.
