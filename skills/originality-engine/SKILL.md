---
name: originality-engine
description: Use to produce run-to-run variation in academic outputs — same prompt, different runs, different but authentic outputs. Deterministic seed per (project, run) drives opening hook, argument order, sentence-length preference, reporting-verb subset, paragraph pattern, section-header style. Backed by tools/academic/variation.py.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Originality engine

The user's requirement: same prompt → 3 runs → 3 different but authentic outputs. References overlap; sentences and structure don't.

This is achieved through **deterministic per-run variation knobs** that the writer (LLM or human) reads and respects.

## The seven variation knobs

| Knob | Variants |
|---|---|
| **opening_hook_style** | anchor_statistic / scene_setting / puzzle_framing / stake_framing / historical_anchor / definitional / contradiction |
| **argument_order** | general_to_specific / problem_to_solution / thesis_then_evidence / comparison_first / chronological / causal_chain / concentric |
| **sentence_length_preference** | varied_with_short_punctuation / longer_complex_dominant / balanced / shorter_punchier |
| **reporting_verb_subset** | argues_contends_maintains / suggests_implies_indicates / demonstrates_shows_establishes / questions_problematises_complicates / neutral_descriptive |
| **paragraph_pattern** | claim_evidence_commentary / evidence_first_then_claim / comparison_within_paragraph / concession_then_assertion / definition_application_implication |
| **section_header_style** | noun_phrase / interrogative / thesis_assertion / imperative / minimal |

## Standard usage

```python
from tools.academic import seed_from_run

# Each run produces a different combination
knobs_run1 = seed_from_run("ea-property-pain", run_number=1)
knobs_run2 = seed_from_run("ea-property-pain", run_number=2)
knobs_run3 = seed_from_run("ea-property-pain", run_number=3)

# Run 1 might be: scene_setting + chronological + balanced + argues + evidence_first + interrogative
# Run 2 might be: anchor_statistic + concentric + longer_complex + suggests + claim_evidence + noun_phrase
# Run 3 might be: puzzle_framing + thesis_then_evidence + varied + demonstrates + concession + thesis_assertion
```

The same project + run number always produces the same knobs. Different run number guarantees different knobs.

## How the writer reads the knobs

When generating an academic output, the writer takes the knobs as constraints:

```
Run 1 knobs:
- opening_hook_style: scene_setting   → start with context, not a statistic
- argument_order: chronological        → walk events forward in time
- reporting_verb_subset: argues...     → use argumentative verbs
- paragraph_pattern: evidence_first    → evidence sentence first, claim sentence next
```

The writer respects these knobs as it drafts. Result: same evidence, same citations, but different rhetorical shape.

## What stays the same across runs

- Cited sources
- Factual claims
- Numerical findings
- Direct quotes (with attribution)
- Bibliography
- Methodology

## What varies across runs

- Sentence-by-sentence wording
- Paragraph order within sections (where causality permits)
- Section ordering (where hierarchy permits)
- Verb choices for attribution
- Opening hooks per section
- Hedging-marker selection
- Connector vocabulary

## Pair with plagiarism-prevention

Originality variation is necessary but not sufficient. The output of every run must still pass `plagiarism-prevention` checks against the source corpus. Different runs vs each other shouldn't matter to detectors (each is novel against sources), but if all three runs are submitted to the same destination, they must read as three independently authored works.

## Anti-patterns

- Reusing the same opening hook across runs
- Same paragraph order with different word swaps
- Same citation order across runs
- Hardcoded section structure regardless of knobs
- Repeating sentence patterns within a single run

## See also

- `tools/academic/variation.py` — knob generator
- `plagiarism-prevention` — pre-delivery gate
- `paraphrase-discipline` — sentence-level variation
- `academic-voice-and-register` — voice consistency across knob variants
