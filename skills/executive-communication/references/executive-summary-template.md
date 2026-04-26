# Reference — Executive Summary Template

A McKinsey-grade executive summary fits on **one page** (≤ 300 words) and follows the SCQA-then-three-points pattern.

## Template

```
[ TITLE — the governing thought as a complete sentence ]

[ SCQA opener — 4 to 8 sentences. Use Direct (Answer / Situation / Complication / Question)
  if the audience is decision-ready; Standard (Situation / Complication / Question / Answer)
  if context is needed first. ]

We base this on three findings:

1. [ Action-title sentence for Finding 1 ]. [ One sentence of evidence,
   sourced. ]

2. [ Action-title sentence for Finding 2 ]. [ One sentence of evidence,
   sourced. ]

3. [ Action-title sentence for Finding 3 ]. [ One sentence of evidence,
   sourced. ]

We recommend [ ONE SENTENCE ACTION ]. Next steps: [ 2 to 4 short bullet
points, each starting with a verb and naming an owner if known. ]

Confidence: [ HIGH / MEDIUM / LOW ] overall, with [ named uncertainties ].
Source manifest: [ pointer to the upstream research file ].
```

## Worked example

```
Acme should launch a digital-first sub-brand in nine months and hold
legacy pricing.

Acme leads Kenya and Tanzania motor with 14% CAGR over five years
(Situation). Three digital-first entrants now offer instant-bind cover
at 22% below Acme's price and have taken 6pp of new business in two
quarters (Complication). The board's question is whether to cut prices,
launch a sub-brand, or hold (Question). Cutting prices on the legacy
book would destroy ~KES 1.4 bn of annual margin without slowing the new
entrants; a separate digital-first sub-brand can match their unit
economics without contaminating the legacy P&L (Answer).

We base this on three findings:

1. Legacy customer churn is not yet rising; the entrants are winning new
   customers, not stealing existing ones. [12-month cohort retention from
   IRA filings; tier-1.]

2. The entrants' unit economics depend on instant-bind, mobile-only
   distribution; Acme cannot replicate this inside the legacy IT stack
   in under three years. [System-architecture review; tier-2.]

3. Two East African peers (NIC and Britam) have already launched
   digital-first sub-brands and grown new-business share by 4pp and 6pp
   respectively in 18 months without legacy cannibalisation. [Regulator
   filings; tier-1.]

We recommend launching the digital-first sub-brand in nine months and
holding legacy pricing. Next steps:
  - Appoint sub-brand MD by end of Q3 (CHRO)
  - Approve KES 850 m capex budget at Q3 board
  - Lock distribution partnerships with two MNOs by Q4 (CCO)
  - Re-test pricing after 18 months on actual share data

Confidence: HIGH on the diagnosis (legacy churn is not yet moving;
entrants' economics are visible). MEDIUM on the build timeline (nine
months assumes no IT integration with legacy core; if integration is
required, add six months).
Source manifest: projects/acme-2026-strategy/synthesis.md
```

## Word budget breakdown

For a 300-word summary:

- Title: 15 words
- SCQA opener: 90 words (≈ 4–5 sentences)
- Three findings: 30 words each → 90 words
- Recommendation + next steps: 60 words
- Confidence + source pointer: 25 words
- **Total: ~280 words.** Leaves room.

## Tests

- [ ] Reader could stop after the title and know the answer.
- [ ] SCQA opener has all four moves, and the Answer matches the title.
- [ ] Each of the three findings is an action title with one piece of evidence.
- [ ] Recommendation is one sentence, in the active voice, with a verb.
- [ ] Next steps each have an owner (or "TBD" with a date by which it is named).
- [ ] Confidence statement specifies what is high-confidence and what is not.
- [ ] Source pointer leads to the upstream manifest where every claim can be tracked.

## Anti-patterns

- **Three findings that overlap.** Re-MECE; if you can't decompose into three non-overlapping findings, the analysis isn't done.
- **Wishy-washy recommendation.** "We recommend exploring options around launching a possible sub-brand" — commit.
- **Confidence label that means nothing.** "MEDIUM confidence" with no statement of what is uncertain. Always specify.
- **Next steps without owners.** Owners are forcing functions. Without them, next steps are wishes.
- **Summary > 300 words.** If you can't fit, the governing thought is too large; split the artefact.

## Companion patterns

- `references/pyramid-principle.md` — the executive summary is a pyramid compressed to one page.
- `references/scqa-opener.md` — the opener of the summary is SCQA.
- `references/action-titles.md` — each finding is an action title.
- For confidence labels and uncertainty discipline, see `analytic-tradecraft` (estimative-probability lexicon).
- For source-pointer format, see `source-evaluation` (every claim → source + tier + verification + confidence + accessed).
