---
name: note-discipline-source-away
description: Use as the source-away composition gate — extract notes from sources first, store them as atomic cards with provenance, then REMOVE the source text from the active context before generating prose. Trzeciak's insight that plagiarism is a workflow failure, not a moral one. Backed by tools/academic/note_card.py.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
  priority: critical
---

# Note discipline — source-away composition

Trzeciak: *"You cannot copy what is not in front of you."*

Plagiarism is structural, not moral. The defence is the **shape of the workflow**, not the intent of the writer. Notes that look like prose produce plagiarism. Notes that look like fragments produce paraphrase.

## The pipeline

```
Source text  →  Note cards  →  [SOURCE-AWAY GATE]  →  Composition  →  Plagiarism check  →  Output
```

Each step has a non-negotiable rule.

### Step 1 — Extract notes
For each source, produce **one card per atomic point**. Each card has:

| Field | Required? | Notes |
|---|---|---|
| heading | yes | Short topic label |
| point | yes | The finding or claim — **fragment, not sentence** |
| source_id | yes | Which source |
| source_page | required for quotes | Page reference |
| is_quote | yes | True if verbatim |
| quote_marks_required | required for quotes | Forces quote format in prose |
| personal_comment | yes (for paraphrases) | The writer's reaction — seed of argument |
| tags | optional | Cross-cut tags for retrieval |

**Critical rule:** `point` must be a **fragment**, not a complete sentence. If it reads like prose, it will produce prose-shaped plagiarism. Use telegraphic style, bullet-clauses, or noun phrases.

✅ Good: `"deposit recovery rate ~20% UG (Mon Aug 2023)"`
❌ Bad: `"Studies have found that the deposit recovery rate in Uganda is approximately 20%, according to a Daily Monitor investigation in August 2023."`

The good version is impossible to copy verbatim. The bad version is one sentence away from plagiarism.

### Step 2 — Store + close source
```python
from tools.academic.note_card import NoteCard, NoteCardStore

store = NoteCardStore(project_id="ea-property-pain")
store.add(NoteCard(
    id="ea-deposit-rate-2023",
    project_id="ea-property-pain",
    heading="UG deposit recovery rate",
    point="~20% recovery; tenants who left units in good condition still got nothing",
    source_id="daily-monitor-2023-08",
    source_page=None,
    personal_comment="suggests enforcement gap, not lease-design problem",
    tags=["uganda", "deposit", "recovery_rate"],
))

# Then save and CLOSE THE SOURCE.
store.save("projects/ea-property-pain/notes.json")
```

After this step, the source text is no longer in the active context. The composition agent reads only from `notes.json`.

### Step 3 — Source-away gate
Before composition begins, the orchestrator verifies:
- Source texts have been removed from the working context
- Composition agent has access to **only** the notes store
- Any direct quote requested must come from a card with `is_quote=True` and `source_page` set

If a composition agent's prompt still contains source text after the note-extraction step, the run is **rejected** before any prose is generated.

### Step 4 — Compose from cards
The composition agent reads notes and writes prose. Because each card is a fragment, the writer must construct sentences from scratch. Multi-card synthesis is the natural pattern (see `source-synthesis-craft`).

### Step 5 — Plagiarism check
Run `plagiarism-prevention` against the original source corpus. Any 7+ word verbatim match → reject and rewrite.

## The personal-comment field

Trzeciak's underrated insight: every paraphrase card carries a **personal comment** — the writer's reaction to the point. This becomes the **seed of the writer's own argument**.

When composition reads a card, it sees both the cited fact AND the writer's reaction. The reaction shapes the surrounding prose, the framing, the comparative move. This is how the writer's voice emerges — not from style alone, but from the embedded analytical stance.

## Validation

```python
from tools.academic.note_card import validate_note_card

warnings = validate_note_card(card)
# Warnings include:
# - Paraphrase point too long (>25 words → likely prose-shaped)
# - Quote card missing page reference
# - Paraphrase card missing personal comment
```

## Anti-patterns

- Notes that are full sentences from the source
- Notes copied verbatim without `is_quote` flag
- No personal comment on paraphrase cards (lose argumentative seed)
- Source text persisting in composition context
- Composing without going through cards (direct source-to-output)
- Single mega-card holding multiple points (defeats atomicity)
- Skipping page references on quotes

## Pair with

- `paraphrase-discipline` — true paraphrase technique (operates on the card → prose move)
- `plagiarism-prevention` — post-composition gate
- `source-synthesis-craft` — multi-card synthesis (3+ sources per paragraph)
- `originality-engine` — varies *which* cards lead in different runs

## See also

- `tools/academic/note_card.py` — implementation
- `evidence-discipline` — engine-wide rule above
