# Reference — Kent Estimative Probability

**Canonical source:** Kent, Sherman. "Words of Estimative Probability." 1964 (declassified). Office of National Estimates internal memorandum. CIA Studies in Intelligence reproduction: https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf. Tier 1.

**Companion:** ODNI ICD 203, standard 8 (accuracy of likelihood judgments). George & Bruce, *Analyzing Intelligence*, Hedley Ch 1 (origins of estimative practice), Kerr Ch 2, Bruce Ch 11 (the Iraq WMD confidence-conflation case).

## The problem Kent solved

Kent observed that vague verbal probability ("possible", "likely", "may", "could") was read inconsistently across decision-makers. One reader's "likely" was another reader's "almost certain" was a third reader's "even chance". Kent proposed pairing each verbal term with an explicit numeric band so reader and writer would interpret the same word the same way.

The principle: **commit to a numeric band; choose the verbal term that matches**.

## The ODNI lexicon (engine-adopted)

Drawn from public ODNI / NIC writing and the National Intelligence Council's standard practice. The bands are intentionally overlapping; the analyst chooses the term that best fits the band.

| Verbal term | Numeric band |
|---|---|
| Almost certainly | ≥ 95 % |
| Very likely | 80 – 90 % |
| Likely | 60 – 80 % |
| Probably | 50 – 70 % |
| Roughly even chance | 45 – 55 % |
| Might / could | 20 – 50 % |
| Unlikely | 10 – 20 % |
| Very unlikely | 5 – 10 % |
| Almost no chance | ≤ 5 % |

**Engine rule.** Every estimative claim ships with both the verbal term and the numeric band, e.g. *"We assess it likely (60–80%) that the regulator will approve the merger by Q3."* The numeric band is non-negotiable; the verbal term alone is not enough.

## The separation rule

The single most important discipline from George & Bruce's treatment of the 2002 Iraq WMD NIE (Bruce Ch 11, pp 178–183) is the **separation of probability from source-confidence**.

- **Probability of the judgment** = how likely the conclusion is to be true, given the evidence.
- **Confidence in the source** = how good the underlying evidence is.

A "high-confidence judgment" can mean either of these; if the writer doesn't say which, the reader will guess wrong. The Iraq NIE failure was structural: the central claims were assigned high confidence on the basis of fragmentary, single-source evidence (Curveball HUMINT; Samarra-tanker IMINT). The "high confidence" referred to the analyst's level of conviction, not to the quality of the evidence.

**Engine format.** Every estimative claim carries two confidence labels:

```
Judgment confidence: LIKELY (60–80%)
Source confidence:   MEDIUM (two independent sources, one tier-1 and one tier-3)
```

If the source confidence is LOW (single source, or all sources tier-4/5), the judgment confidence cannot exceed POSSIBLE / ROUGHLY EVEN regardless of the analyst's conviction. The reasoning: a confident judgment built on uncertain evidence is the failure mode every Western IC post-mortem of the last 80 years has identified.

## Calibration

A calibrated probability lexicon is one where, over many judgments, "likely" events occur ~60–80% of the time. Calibration decays without feedback. The engine's calibration practice:

1. **Log every estimative judgment** with its verbal term, numeric band, and named outcome window.
2. **Re-check at the outcome window** — did the predicted event happen?
3. **Track hit rate per verbal term**. If "likely" judgments occur 90% of the time, the analyst is under-confident and should shift the lexicon. If "likely" judgments occur 30% of the time, the analyst is over-confident.
4. **Publish calibration tables** on the same cadence as the engine's quarterly self-evaluation.

This practice is not yet automated; calibration tables are a manual log until the relevant tool ships (planned Month 5 of the implementation roadmap).

## Common conflations and their fixes

| Conflation | Fix |
|---|---|
| "We assess with high confidence that X." | Specify whether high confidence refers to judgment or source. State both separately. |
| "X is likely." (no numeric) | Add the numeric band. "X is likely (60–80%)." |
| "X may happen." (no anchor) | Use *might / could* if numeric band is 20–50%. Otherwise re-pick. |
| "Almost certainly X." (no numeric) | Add ≥ 95% band. If you wouldn't bet at 19:1, you don't mean almost certainly. |
| "Probably X." (where probably means "I personally believe X") | Replace with the verbal term + band that match the actual evidence. *Probably* is for 50–70%; opinion is not evidence. |
| "We are confident X." (vague) | Replace with judgment confidence + source confidence, separately, with bands. |
| Single-source claim with high-confidence label | Demote to LOW source confidence; demote judgment confidence to POSSIBLE; add named indicators that would corroborate. |

## What the engine refuses to do

- Ship a judgment without a numeric band.
- Use "high / medium / low" confidence without specifying judgment vs. source.
- Inflate judgment confidence to soothe a reader who wants certainty. Bruce Ch 11: "Reasoning itself does not make something true; it can only identify a possible truth."
- Compress two contradictory analyst positions into one verbal term. Dissents footnote, NIE-style; the engine does not hide them in averages.

## Sources

- Kent, Sherman. "Words of Estimative Probability." 1964 (declassified). https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf. Tier 1.
- ODNI Intelligence Community Directive 203, January 2015. https://www.dni.gov/files/documents/ICD/ICD-203.pdf. Tier 1.
- George & Bruce, *Analyzing Intelligence*, Hedley Ch 1, Kerr Ch 2, Bruce Ch 11. Tier 1.
- ODNI National Intelligence Council Publications. https://www.dni.gov/index.php/who-we-are/organizations/mission-integration/nic/nic-related-menus/nic-related-content/nic-publications. Tier 1.
