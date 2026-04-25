---
name: plagiarism-prevention
description: NON-NEGOTIABLE — use on every academic output before delivery. Prevents verbatim overlap with source corpus, enforces citation discipline, gates the originality check, runs N-gram audit. Backed by tools/academic/originality.py + citation_density.py + quotes.py.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
  priority: critical
---

# Plagiarism prevention

Plagiarism detection (Turnitin, iThenticate, Grammarly Premium, Copyleaks, SafeAssign, Quetext) flags:

- **Verbatim N-gram matches** (5–15 word strings); 7+ words is the typical alarm
- **Sentence-structure similarity** (semantic match with same word order)
- **Citation absence** for claims that look sourced
- **Quote-density anomalies** (too much quoted material)

This skill enforces the discipline that prevents all four.

## The five rules

### 1. No 7-word verbatim copy from any source
Run `tools.academic.detect_overlap(draft, sources)` before delivery. Any hit at length ≥ 7 must be either:
- Restructured (true paraphrase, not synonym swap)
- Quoted with proper attribution (`tools.academic.canonicalize_quote`)
- Cited as paraphrase even if no shared words remain

### 2. Cite the idea, not just the words
Even when paraphrased, the *idea* still belongs to its source. Every assertion that came from a source carries an inline citation. Use `tools.academic.citation_density(text)` to audit.

**Target rate**: 8–20 citations per 1000 words for academic body sections; lower for introduction / conclusion.

### 3. Direct quotes <5% of total words
Quotes are the wrong default. Use them only when:
- Exact phrasing is essential (technical / legal / historical)
- The quote is itself the object of analysis
- Paraphrase would distort the meaning

`tools.academic.detect_quote_density(text)` returns the ratio.

### 4. Block quotes ≥40 words (APA / Harvard)
Format with `tools.academic.canonicalize_quote(...)` which auto-routes to block format above the threshold.

### 5. Re-check every paraphrase
Use `tools.academic.paraphrase_distance(original, paraphrase)`. The verdict must be `true_paraphrase`, never `synonym_swap` or `verbatim`.

## The pre-delivery checklist

Run this before any academic output ships:

```python
from tools.academic import detect_overlap, citation_density, paraphrase_distance, hedging_audit

# 1. N-gram overlap against source corpus
overlap = detect_overlap(draft, sources={"src1": txt1, "src2": txt2})
critical = overlap.by_severity()["critical"]
high = overlap.by_severity()["high"]
assert not critical, f"Critical 12+ word verbatim matches: {critical}"
assert len(high) <= 2, f"Too many 7-11 word verbatim matches: {len(high)}"

# 2. Citation density
density = citation_density(draft)
assert not density.uncited_paragraphs, f"Uncited substantive paragraphs: {density.uncited_paragraphs}"

# 3. Paraphrase quality (per paraphrased passage)
score = paraphrase_distance(original_passage, my_paraphrase)
assert score.verdict == "true_paraphrase", score.rationale

# 4. Hedging discipline
hedge = hedging_audit(draft)
assert hedge.verdict not in ("UNDER-HEDGED", "OVER-HEDGED"), hedge.verdict
```

If any check fails: rewrite, don't ship.

## What plagiarism detectors actually look for (engine-specific anti-patterns)

| Detector signal | Engine guard |
|---|---|
| 7+ word verbatim | `detect_overlap` |
| Synonym-swap paraphrase | `paraphrase_distance` (low surface, high lexical = swap) |
| Citation absence on claim-heavy paragraph | `citation_density` |
| Quote density >5% | `detect_quote_density` |
| Sentence structure match across language | `paraphrase_distance` with `use_semantic=True` |
| Citation pattern matches another submission | per-run variation via `seed_from_run` |
| Off-the-shelf phrases ("In today's world", "Throughout history") | banned-phrase filter (roadmap) |
| AI-template phrases ("delve into", "intricate tapestry") | banned-phrase filter (roadmap) |

## Anti-patterns

- Synonym-swap paraphrasing (treats words; ignores structure)
- "Patchwriting" (mosaic of quoted + paraphrased without citation)
- Citing only when quoting (paraphrases need citations too)
- Reusing sentence structures across paraphrases of different sources
- Skipping the originality check before submission
- Treating "I changed three words" as paraphrase

## See also

- `paraphrase-discipline` — true paraphrase technique
- `source-synthesis-craft` — combining multiple sources
- `originality-engine` — run-to-run variation
- `academic-citation-styles` — format conventions
- `evidence-discipline` — engine-wide rule above this
