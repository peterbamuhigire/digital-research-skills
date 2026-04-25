---
name: reading-mode-router
description: Use whenever an agent retrieves a source for processing — classifies the source and routes to the right reading mode (narrative / meditative / scan / mastery / partial-mastery). Prevents over-reading low-density sources and under-reading core ones. Adapted from Andrew Abbott, Digital Paper.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Reading-mode router

Most reading failures come from using the wrong mode for the source. Five modes; one per role; route deliberately.

## The five modes

### 1. Narrative reading
- **Purpose:** orientation; story; building "attractors" for later browsing
- **Speed:** ~1 minute / page
- **When:** background phase; getting the general shape of a domain
- **Trap:** **never use for analytic work** — Abbott: "reading without questions always reverts to narrative reading"

### 2. Meditative reading
- **Purpose:** theoretical stimulation; letting text "come apart into shreds of insight and allusion"
- **Speed:** 3–5 minutes / page
- **When:** core theoretical sources; redesign moments; when stuck and need fresh framing
- **Output:** idea-notebook entries; not extracted facts

### 3. Scan reading
- **Purpose:** template-driven extraction in low-density material with rare hits
- **Speed:** seconds per page
- **When:** sweeping a 600-dissertation collection for one term; dense indexes
- **Trap:** disattention; works only if you know exactly what you're looking for

### 4. Mastery reading
- **Purpose:** master entire argument
- **Speed:** ~1 hour per 300-page book; ~20 min per article
- **Algorithm (book):**
  1. Read TOC 4–5 times
  2. Note top 12 abstractions in the index
  3. Read end-of-chapter summaries
  4. Recite argument to yourself
  5. Write summary notes within the hour
- **Algorithm (article):**
  1. Read abstract 5 times
  2. Enumerate what's missing
  3. Scan-fill the gaps
  4. Write notes
- **Use for:** core sources only — typically 3–10 per project, not more
- **Test:** "If you catch yourself reading steadily for five minutes, stop. You are out of mastery mode."

### 5. Partial mastery reading
- **Purpose:** extract one specific thing
- **Speed:** ~10 minutes / article
- **When:** most secondary sources — read with one explicit question
- **Trap:** drifting into narrative reading without a question

## Decision rules

- **Always have an explicit question before partial-mastery reading.** Without one, you'll narrative-drift.
- **Mastery is rare.** Only 3–10 sources per project warrant it. Most secondary literature gets partial mastery.
- **Scan and browse work only if you've done narrative-reading-as-priming first.** Background creates the "attractors" without which scanning is just disattention.
- **Don't cite-and-paste extract during reading.** Abbott: "that takes extra time and is postponing mastery." Read first; extract second.

## Routing heuristics

| Source role | Default mode |
|---|---|
| Background overview | Narrative |
| Theoretical anchor | Meditative |
| Index / dissertation list | Scan |
| Core 3–10 of project | Mastery |
| Most secondary lit | Partial mastery |

## Anti-patterns

- Narrative reading when you should be doing partial mastery — produces non-extractable summaries
- Mastery reading on >10 sources per project — exhausting and wasteful
- Skipping the abstract-multiple-times step in mastery (Abbott's algorithm depends on it)
- Reading-and-extracting in one pass — splits attention
- "Reading the whole book" before deciding the question — standard novice trap

## Output discipline

Each mode produces a different artefact:

| Mode | Output |
|---|---|
| Narrative | (informally) attractor priming; idea-notebook tag seeds |
| Meditative | Idea-notebook entries with controlled-vocabulary tags |
| Scan | Hits / no-hits with location |
| Mastery | Whole-source summary note within ~1 hour |
| Partial mastery | One extracted answer to one question |

## See also

- `controlled-vocabulary-builder` — meditative reading feeds it; mastery reading depends on it
- `pearl-growing-iteration` — the iteration loop calls this skill on each retrieved source
- `quote-extraction` — runs *after* the right reading mode, not during
- `evidence-discipline` — every extracted item still needs source citation
