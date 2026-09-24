# Estimative Probability Language

Use this guide whenever an output makes a judgment about something uncertain (a forecast, an
attribution, an assessment of intent or outcome). It fixes the words to numeric bands, separates
likelihood from confidence, and sets up calibration.

## Why this exists

Verbal probability words ("possible", "likely", "may") are read very differently by different
readers. One reader's "likely" is another's "almost certain". The remedy, first argued inside
the US intelligence community in the 1960s and now codified in its analytic standards, is to tie
each term to a numeric band and to state separately how good the evidence is.

## Inputs

- The judgment in one sentence, with an outcome window ("by 31 March 2027").
- The evidence set, with tier and independence of each source.
- The reader: decision-grade outputs always carry numbers; popular outputs may carry the words
  with the band in a note.

## Decision rule 1: use the ICD 203 bands

The engine adopts the likelihood scale in ODNI Intelligence Community Directive 203 (Analytic
Standards). Use one row of terms consistently; do not mix rows in one product.

| Band | Preferred term | Alternative term |
|---|---|---|
| 1 to 5% | almost no chance | remote |
| 5 to 20% | very unlikely | highly improbable |
| 20 to 45% | unlikely | improbable |
| 45 to 55% | roughly even chance | roughly even odds |
| 55 to 80% | likely | probable |
| 80 to 95% | very likely | highly probable |
| 95 to 99% | almost certain(ly) | nearly certain |

Every estimative claim ships with the term and the band: "We assess it likely (55 to 80%) that
the regulator approves the merger by Q3 2027." "May", "could" and "might" are not estimative
terms; replace them with a band or state that the likelihood is not assessed.

## Decision rule 2: separate likelihood from confidence

- **Likelihood** is how probable the judgment is.
- **Confidence** is how strong the basis is: quantity, quality and independence of sources, and
  the analyst's understanding of the topic.

State both, separately:

```
Likelihood:  LIKELY (55-80%)
Confidence:  MODERATE - two independent sources (one tier-1 registry, one tier-3 press report)
```

"High confidence" without saying which of the two it means is ambiguous and must be rewritten.
If confidence is low (single source, or only weak-tier sources), cap the likelihood at "roughly
even chance" unless the analyst writes down why the evidence supports more, and add the
indicators that would corroborate. A confident judgment on thin evidence is the failure mode
most post-mortems of intelligence failures identify.

## Procedure

1. Write the judgment and its outcome window.
2. Grade the evidence (tier, independence, recency) with `source-verification`.
3. Assign a numeric probability first, then pick the matching term from the table.
4. Assign confidence with a one-line basis.
5. Record dissent: if analysts disagree across bands, show both positions; do not average them
   into one word.
6. Log the judgment for calibration.

## Calibration

Over many judgments, events called "likely" should occur roughly 55 to 80% of the time.
1. Log each judgment with term, band, confidence and outcome window.
2. At the window, record whether the event happened.
3. Track the hit rate per band. If "likely" events happen 95% of the time, the analyst is
   under-confident; if 30%, over-confident.
4. Review calibration tables at each quarterly engine self-evaluation. The log is manual until
   tooling ships; see `calibration-and-forecasting`.

## Common errors and fixes

| Error | Fix |
|---|---|
| "We assess with high confidence that X" | State likelihood band and confidence basis separately |
| "X is likely" with no number | Add the band: "likely (55 to 80%)" |
| "X may happen" | Pick a band or mark NOT_ASSESSED |
| "Almost certainly X" when you would not bet at about 19 to 1 | Move down a band |
| "Probably" meaning "I believe" | Use the term the evidence supports |
| Single-source claim labelled high confidence | Lower confidence, cap likelihood, list corroborating indicators |

## Original worked example

Question: will Uganda's central bank cut its policy rate at the next meeting?
- Evidence: the bank's last statement flagged easing inflation (tier 1); two local bank
  economists expect a cut (tier 3, not independent of each other).
- Judgment: "We assess a cut at the [date] meeting as likely (55 to 80%)."
- Confidence: moderate: one official signal and one correlated market view; no minutes yet.
- Indicator that would move the band: the next monthly inflation release.

## Checklist

- [ ] Every estimative claim has a term from one ICD 203 row and its numeric band.
- [ ] Likelihood and confidence stated separately, with the basis for confidence.
- [ ] Low-confidence judgments capped or justified.
- [ ] Dissent shown, not averaged.
- [ ] Judgment logged with its outcome window.

Evidence and currentness: ODNI ICD 203, *Analytic Standards* (signed 2 January 2015, with later
technical amendments), likelihood table under the analytic standard on expressing uncertainty (paragraph (2)(a)), retrieved from
archive.dni.gov/files/documents/ICD/ICD-203.pdf, accessed 2026-09-24. The previous engine table
(for example "likely 60 to 80%", "very likely 80 to 90%") did not match ICD 203 and was
corrected. The exact date of the most recent technical amendment: NOT_ASSESSED.

Sources: ODNI (2015, amended) ICD 203 *Analytic Standards*; Kent (1964) "Words of Estimative
Probability", *Studies in Intelligence* (CIA, declassified).
