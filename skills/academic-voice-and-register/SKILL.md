---
name: academic-voice-and-register
description: Use to write in authentic academic voice — hedging, modality, reporting verbs, signposting, register. Audit drafts for over-claim, under-hedge, repetitive verbs, AI-template phrases. Backed by tools/academic/hedging.py + reporting_verbs.py.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Academic voice and register

Academic writing has a distinct register: hedged, attributed, formal but not stilted, signposted. Get any of these wrong and the prose reads as either student-amateur or AI-template.

## Hedging — the central discipline

Strong unqualified claims are usually overclaims. The discipline is to qualify.

| Marker class | Examples |
|---|---|
| Modal verbs | may, might, could, would, can, should |
| Epistemic adverbs | perhaps, possibly, probably, presumably, apparently, arguably |
| Approximators | approximately, roughly, around, several, a number of |
| Softening phrases | it appears that, this suggests, to some extent, broadly speaking |
| Evidentials | according to, the evidence suggests, research indicates |
| Qualifiers | tend to, often, in most cases, in general |

**Target rate**: 6–12 hedges per 1000 words. Below 4 = dogmatic. Above 15 = wishy-washy.

`tools.academic.hedging_audit(text)` reports + warns.

## Overclaim red flags (use sparingly or not at all)

- always / never / all / none / every / no one / everyone
- proves / definitely / undoubtedly / certainly / without doubt
- obviously / clearly / absolutely

When the audit flags these, ask: would this still be defensible if I qualified it?

## Reporting verbs — vary them

Don't repeat "argues" / "states" / "says". Rotate across categories:

- **Neutral**: states, notes, observes, describes, reports, comments
- **Argumentative**: argues, contends, maintains, asserts, posits, advances
- **Tentative**: suggests, proposes, implies, speculates, indicates
- **Evaluative-positive**: demonstrates, shows, establishes, confirms, corroborates
- **Critical**: challenges, disputes, questions, refutes, problematises
- **Discovery**: finds, discovers, identifies, recognises, uncovers
- **Comparison**: parallels, echoes, contrasts, distinguishes

`tools.academic.reporting_verb_variety(text)` audits + suggests substitutions.

## AI-template phrases (banned)

These phrases flag AI-generated text. Avoid them:

- "delve into" / "delve deeper"
- "intricate tapestry" / "rich tapestry"
- "navigate the complexities of"
- "in today's fast-paced world"
- "in today's digital age"
- "throughout history"
- "since the dawn of time"
- "it is important to note that"
- "in conclusion" (in body text)
- "in this essay, I will…"
- "this essay will explore…"
- "let us now turn to…"
- "first and foremost"
- "last but not least"
- "stands as a testament to"
- "play a crucial role"
- "the realm of"
- "myriad of"
- "at its core"

## Signposting — visible argument structure

Academic readers expect explicit signposting:

| Function | Markers |
|---|---|
| Adding | moreover, furthermore, in addition, additionally |
| Contrasting | however, in contrast, nevertheless, on the other hand |
| Sequencing | first, second, finally; subsequently |
| Causation | as a result, consequently, therefore, thus |
| Exemplification | for instance, for example, to illustrate |
| Concession | although, while, despite, granted |
| Reformulation | in other words, that is to say, more precisely |
| Conclusion | in sum, overall, to summarise |

**Vary across paragraphs.** Same connector twice in a row is a smell.

## Voice consistency

- **First-person plural** ("we") — common in collaborative academic writing
- **First-person singular** ("I") — humanities and reflective writing accept it; sciences resist
- **Passive impersonal** ("it is shown that") — sciences default; humanities resist
- **Active third-person** ("Smith demonstrates") — most flexible

Pick one register at the project's start and stay consistent.

## Tense conventions

| Tense | When |
|---|---|
| Present | Author's claim ("Smith argues") |
| Past simple | Specific past event ("the survey collected 200 responses") |
| Present perfect | Continuing relevance ("research has shown") |
| Future | Methodology section / abstract |

## Standard pre-delivery audit

```python
from tools.academic import hedging_audit, reporting_verb_variety

hedge = hedging_audit(draft)
verbs = reporting_verb_variety(draft)

assert hedge.verdict not in ("UNDER-HEDGED", "OVER-HEDGED"), hedge.verdict
assert not verbs.overused, f"Overused: {verbs.overused}"
assert len(verbs.underused_categories) <= 4, "Verb variety too narrow"
```

## Anti-patterns

- Strong unqualified claims throughout
- Same reporting verb >5 times in a draft
- AI-template phrases (any from the banned list)
- Inconsistent register (mixing first-person and impersonal-passive)
- Repeated connectors back-to-back ("Furthermore, ... Furthermore, ...")
- Sentence-length monotony

## See also

- `tools/academic/hedging.py`, `reporting_verbs.py` — implementations
- `paraphrase-discipline` — sentence-level variation
- `originality-engine` — run-to-run variation
- `academic-writing-conventions` — engine's existing structural skill
