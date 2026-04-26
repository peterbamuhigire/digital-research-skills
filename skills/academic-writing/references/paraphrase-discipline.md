# Paraphrase discipline

A "synonym-swap" paraphrase is structurally identical to the original with words substituted. Plagiarism detectors that use semantic similarity flag it. True paraphrase reorganises the structure.

## The four-step paraphrase technique

For any passage you want to use:

### 1. Read the passage
Read it twice. Close the source.

### 2. Note the *idea* (not the words)
Write 2-3 bullet points capturing the *argument* — not the sentences.

### 3. Reconstruct from the bullets
Open a blank space. Write the idea in *your structure*, *your sentence order*, *your verb choices*.

### 4. Compare back
Open the source. Where do they look similar? Restructure those sentences again.

## What true paraphrase looks like

**Original:**
> "Research suggests that 80% of Ugandan tenants never recover their security deposit, even when the property is left in good condition."

**Synonym-swap (BAD — flagged by detectors):**
> "Studies indicate that 80% of Ugandan renters do not get back their security deposit, even when the unit is left undamaged."

Same structure. Same word order. Word-for-word substitution. Detector verdict: plagiarism.

**True paraphrase (GOOD):**
> "The Daily Monitor (Aug 2023) found a deposit-recovery rate of just 20% in Uganda. Even tenants who left their units in good condition typically saw none of their deposit returned."

Different structure. Different sentence count. Different focal point. Same idea, properly cited.

## The verdict matrix

`tools.academic.paraphrase_distance(original, paraphrase)` returns:

| Verdict | Surface | Lexical | Action |
|---|---|---|---|
| `verbatim` | high | high | Quote with attribution OR rewrite from scratch |
| `synonym_swap` | medium-high | very high | Restructure, don't substitute |
| `true_paraphrase` | low | moderate | Acceptable; cite the source |
| `too_distant` | very low | very low | Drift risk — verify meaning preserved |

## Tools

```python
from tools.academic import paraphrase_distance

score = paraphrase_distance(
    original="Research suggests that 80% of Ugandan tenants...",
    paraphrase="The Daily Monitor (Aug 2023) found...",
    use_semantic=True,  # uses sentence-transformers if available
)
print(score.verdict, score.rationale)
```

## Multi-source synthesis as paraphrase shield

The strongest defence against detection is **synthesising from multiple sources**. A claim that combines findings from 3+ sources cannot match any single source verbatim.

See `source-synthesis-craft` for the technique.

## Reporting verbs (vary them)

Don't repeat "argues" / "states" / "says". Rotate:

- Neutral: states, notes, observes, reports
- Argumentative: argues, contends, maintains, asserts
- Tentative: suggests, proposes, implies, indicates
- Evaluative-positive: demonstrates, shows, establishes
- Critical: challenges, disputes, problematises
- Comparison: parallels, echoes, contrasts

`tools.academic.reporting_verb_variety(text)` audits.

## Anti-patterns

- Synonym swap with no structural change
- "I'll just change every third word"
- Paraphrasing source A using source B's structure (still plagiarism)
- Paraphrasing without citing (citation is required even when paraphrased)
- Forgetting to verify meaning preserved (too-distant paraphrase = misrepresentation)
- Patchwriting (sentence from A + sentence from B with no cite)

## See also

- `tools/academic/paraphrase.py` — verdict engine
- `plagiarism-prevention` — overall gate
- `source-synthesis-craft` — multi-source technique
- `academic-voice-and-register` — sentence-level variety
- `evidence-discipline` — engine-wide rule
