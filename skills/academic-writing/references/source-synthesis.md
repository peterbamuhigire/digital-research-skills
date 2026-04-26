# Source synthesis craft

A claim that combines findings from three or more sources cannot match any single source verbatim. Multi-source synthesis is therefore the strongest defence against plagiarism — and the strongest signal of academic competence.

## Four synthesis patterns

### 1. Agreement / convergence
Multiple sources reach the same conclusion. Cite all of them in one sentence.

> Several studies have found that the deposit-recovery rate in informal urban housing markets falls below 30% (Daily Monitor, 2023; Hakijamii, 2022; KNBS, 2024).

### 2. Disagreement / divergence
Sources reach different conclusions. Acknowledge the disagreement; offer a frame for it.

> While the Daily Monitor (2023) reports a 20% recovery rate, KNBS (2024) places the figure closer to 35%. The discrepancy may reflect differing definitions of "recovery" — the former counts only full refunds, while the latter includes partial returns.

### 3. Supplementation / extension
One source establishes a finding; another extends or applies it.

> The deposit-recovery problem identified in Uganda (Daily Monitor, 2023) is not unique to East Africa: parallel patterns have been documented in Latin America (Reyes, 2021) and South Asia (Khan & Ahmed, 2022).

### 4. Gap-naming / silence-detection
Sources are united in *not* addressing something — itself a finding.

> Although several studies have catalogued the deposit-recovery problem (Daily Monitor, 2023; Hakijamii, 2022; KNBS, 2024), none has examined the role of micro-credit collateralisation in displacing deposit recovery — a gap this paper addresses.

## The synthesis sentence

Compress 3+ sources into one sentence with this template:

> [Reporting verb], several / multiple / a number of / various studies [verb-form] [claim] (Author1, year; Author2, year; Author3, year).

Examples:
> Studies converge on the finding that...
> Recent work has documented...
> A number of researchers have noted that...

## Avoid the listing trap

Do NOT do this:

> Smith (2020) argues X. Jones (2021) argues X. Brown (2022) argues X.

Three sentences saying the same thing. The reader's eyes glaze.

DO do this:

> Smith (2020), Jones (2021), and Brown (2022) all argue X.

OR (with more synthesis):

> Although Smith (2020), Jones (2021), and Brown (2022) reach broadly the same conclusion about X, their methodologies differ: Smith conducted [survey], Jones used [archive], and Brown drew on [interviews]. The convergence across methodologies strengthens the finding.

## The four-source rule for difficult passages

When you find yourself wanting to closely paraphrase a single source, force yourself to add three more. The synthesis itself becomes original even if individual claims are not.

## Citation density per synthesis sentence

A good synthesis sentence carries 2–5 citations. More than 5 starts to read as a list. Fewer than 2 isn't synthesis.

## Anti-patterns

- One paragraph, one source — patchwriting risk
- Listing sources sequentially without combining
- Synthesising sources that say *opposite* things without naming the disagreement
- Cherry-picking one source's framing while citing several
- Reusing the same synthesis pattern paragraph after paragraph
- Forgetting to cite the silence (gap-naming is itself a citation move)

## Tools

```python
# After drafting, audit citation density
from tools.academic import citation_density

report = citation_density(text)
# Substantive paragraphs should carry 1+ citation; sometimes 3-5 (synthesis)
print(report.thin_paragraphs)
```

## See also

- `paraphrase-discipline` — sentence-level technique
- `plagiarism-prevention` — overall gate
- `academic-voice-and-register` — verb / hedging variety
- `evidence-discipline` — engine-wide attribution rule
