# Reference — ICD 203 and Tradecraft Standards

**Canonical source:** Office of the Director of National Intelligence, Intelligence Community Directive 203 — Analytic Standards. Effective 2 January 2015 (revalidated). PDF: https://www.dni.gov/files/documents/ICD/ICD-203.pdf. Tier 1.

**Companion:** *Analyzing Intelligence: Origins, Obstacles, and Innovations* (George & Bruce, eds., Georgetown UP, 2008) treats the MacEachin tradecraft reforms throughout — see esp. Davis Ch 10 ("Why Bad Things Happen to Good Analysts"), Bruce Ch 11 ("Making Analysis More Reliable").

## The nine analytic standards

Every estimative output of the engine must satisfy all nine before shipping.

### 1. Properly describes quality and credibility of underlying sources, data, and methodologies
Every load-bearing claim names its source; the source's tier (1–5 from `source-evaluation`) appears; the methodology by which the claim was reached is auditable. Single-source key judgments are flagged.

### 2. Properly expresses and explains uncertainties associated with major analytic judgments
Confidence levels are explicit, calibrated against the Kent / ODNI lexicon, and attached to numeric bands. Uncertainty is named, not hidden behind hedging language.

### 3. Properly distinguishes between underlying intelligence information and analysts' assumptions and judgments
Sentences are tagged: this is what we know (sourced); this is what we assume (Key Assumptions Check applied); this is our judgment (analytic step explained).

### 4. Incorporates analysis of alternatives
At least one alternative hypothesis is considered for any load-bearing judgment. Where the evidence is contested, an Analysis of Competing Hypotheses (ACH) matrix is attached. The case for and against the leading hypothesis is shown.

### 5. Demonstrates customer relevance and addresses implications
The output answers the question the customer (decision-maker, examiner, partner) actually asked. If the output is being repurposed across audiences, each audience-specific framing is explicit.

### 6. Uses clear and logical argumentation
Every conclusion follows from premises. No non-sequiturs. Argument map (or equivalent informal chain) is auditable.

### 7. Explains change to or consistency of analytic judgments
If this judgment differs from a prior judgment by the engine (or by an external authority the customer relies on), the change is explained and the trigger evidence cited. If the judgment is consistent, that is also noted (avoids the appearance of unexamined inheritance).

### 8. Makes accurate judgments and assessments of likelihood
Probability terms come from the Kent / ODNI lexicon and are calibrated against feedback where available. The numeric band attached to a verbal term is explicit.

### 9. Incorporates effective visual information where appropriate
Charts, maps, timelines, matrices serve the message and are labelled to action-title standard (`executive-communication/references/action-titles.md`). Visuals are sourced; manipulation or uncertainty in the underlying data is shown.

## The ship-gate checklist

```
ICD 203 ship-gate — run before any estimative output ships
  [ ] Sources tier-rated; single-source key judgments flagged
  [ ] Confidence stated with Kent / ODNI verbal term + numeric band
  [ ] Probability of judgment ≠ confidence in source — both stated separately
  [ ] Sentences tagged: what we know vs. what we assume vs. what we judge
  [ ] At least one alternative hypothesis considered
  [ ] ACH matrix attached for high-stakes contested judgments
  [ ] Customer-relevance statement: who reads this, what decision do they make
  [ ] Argument chain auditable (no non-sequiturs)
  [ ] Change-vs-prior-judgment explanation written if applicable
  [ ] Likelihood judgments calibrated; numeric band attached
  [ ] Visuals action-titled and sourced
```

If any box is not ticked, the output is not estimative-grade and does not ship. Either fix the gap or relabel the output (e.g. "draft for review" rather than "assessment").

## The MacEachin reforms

Douglas MacEachin (Deputy Director for Intelligence, CIA, early 1990s) introduced what George & Bruce treat as the precursor to ICD 203: making assumptions, sourcing, and confidence explicit on the face of every product. The reforms responded to a decade of post-mortems that found analysts had drawn confident conclusions from thin or single-source evidence without flagging either condition. The same pattern was diagnosed again in the Silberman-Robb WMD Commission report (2005). The lesson the engine adopts: **estimative discipline must be structural, not aspirational**. A skill enforces it; a writing-style guide does not.

## Practical application inside the engine

- **Wave 2 (gap-fill)**: Before launching gap-fill agents, run the ICD 203 checklist on the Wave 1 synthesis. Gaps in standards 1, 4, 8 most often surface here.
- **Wave 3 (verification)**: Standards 1, 2, 8 are re-tested after verification — does the source quality survive scrutiny; does the confidence still hold; does the probability band still fit.
- **Wave 3.5 (peer review)**: Standards 4 and 6 — the external reviewer surfaces alternative hypotheses and tests the argument chain.
- **Wave 4 (synthesis)**: Standards 5, 7, 9 — customer-relevance pass, change explanation, visual finalisation.
- **Pre-ship**: Full nine-standard checklist; if any fail, do not ship.

## Sources

- ODNI Intelligence Community Directive 203, January 2015. https://www.dni.gov/files/documents/ICD/ICD-203.pdf. Tier 1.
- George & Bruce, *Analyzing Intelligence*, esp. Davis Ch 10, Bruce Ch 11. Tier 1.
- Silberman-Robb WMD Commission Report, 2005. Tier 1.
- MacEachin, Douglas. "Tradecraft of Analysis: Challenge and Change in the CIA." 1994. Cited by Davis and Bruce.
