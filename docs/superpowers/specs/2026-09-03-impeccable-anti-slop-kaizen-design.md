# Impeccable-Derived Anti-Slop Kaizen Design

**Date:** 2026-09-03
**Status:** approved for implementation
**Owner:** Peter Bamuhigire
**Scope:** all 12 registered skill engines, with full treatment in web development, website, and design

## Source and currentness record

| Field | Record |
|---|---|
| `source_id` | `impeccable-slop-page-2026-09-03` |
| Source | [Impeccable Slop catalog](https://impeccable.style/slop/) |
| Publisher | Impeccable; first-party catalog for its own detector and critique workflow |
| Access date | 2026-09-03 |
| Publication/revision date | Not disclosed on the accessed page |
| Scope | Web-interface AI-slop patterns and general rendered-page quality defects |
| Freshness class | `context-bound`; recheck before changing any tool, package, or detector dependency |
| Support status | `supported` for the catalog's own taxonomy; `partial` for any claim about prevalence or universal machine authorship |
| Limitation | The page is not independent evidence that every listed pattern is always AI-generated. Visual patterns are review signals, not universal bans. |
| Next review | 2026-10-03 or before a future anti-slop standardisation change |

The page describes 66 patterns and distinguishes deterministic CLI checks, browser-layout checks,
and LLM-only judgments. The implementation records those evidence modes but does not add
Impeccable as a required dependency.

## Problem

The current shared ME1-ME7 gate catches semantic and rhetorical machine errors. The external
catalog adds a useful adjacent class: interfaces and polished artifacts that converge on defaults,
signal hierarchy without a user need, repeat identical modules, demand attention decoratively, use
placeholder material, or hide delivery defects under surface polish.

Applying those patterns as a universal style ban would create false positives. Applying no overlay
would leave the web, website, and design engines under-protected. The solution is a typed overlay:
full for visual/product work, lightweight for text and operational engines, and explicit about
evidence mode and functional exceptions.

## Approved architecture

The shared Digital Research gate gains seven `AS` overlay checks. ME1-ME7 remain unchanged and
continue to govern semantic purpose and information delta.

| ID | Overlay | Recognition test | Default correction |
|---|---|---|---|
| AS1 | Default convergence | Is a common palette, typeface, layout, or copy pattern present without a recorded project reason? | Keep only with a brief-specific reason; otherwise choose a deliberate alternative. |
| AS2 | Unearned hierarchy | Do eyebrows, chips, badges, icon tiles, hero metrics, or numbered labels imply importance without improving the task? | Remove, integrate into useful content, or document the hierarchy reason. |
| AS3 | Module monoculture | Are identical cards, nested cards, or uniform spacing flattening distinctions between items? | Vary structure by information need, flatten nesting, or preserve it with a hierarchy rationale. |
| AS4 | Decorative attention | Does glow, gradient, marquee, cursor, pulse, bounce, hover transform, or similar motion lack state or task value? | Remove, reduce, or tie it to a real state/action; respect accessibility preferences. |
| AS5 | Placeholder material | Is an image, illustration, example, icon, or asset generic, shape-assembled, washed out, missing, or placeholder-valued? | Use traceable purposeful material or remove the slot. Never invent provenance. |
| AS6 | Copy tell | Do buzzwords, repeated em-dashes, manufactured aphorisms, or theatrical framing recur as a house cadence? | Replace with literal verbs/nouns and varied plain prose; count recurrence in the audit. |
| AS7 | Polish-covered delivery debt | Is content invisible, unreadable, cramped, overflowing, clipped, broken, or structurally invalid beneath the visual polish? | Fix the defect before judging style; record browser or render evidence. |

Each finding records `id`, `unit`, `evidence_mode` (`cli`, `browser`, `llm_only`, or
`human_review`), `new_information_or_task_value`, `evidence_or_decision`, `action`, `severity`,
`exception`, `reviewer`, and `date`. `NOT_ASSESSED` is used when the required render, browser,
tool, context, or reviewer evidence is unavailable.

## Engine adapters

- **Full overlay:** `skills-web-dev`, `website-skills`, and `design-system-skills`. Their gates
  cover the entire AS1-AS7 set, with visual rules interpreted against the project's own design
  system and accessibility requirements.
- **Content/structure overlay:** SRS, business plan, social media, proposal, accounting, Digital
  Research, Windows, Linux, and political engines use AS1, AS3, AS5, and AS6 where human-facing
  prose, templates, examples, dashboards, or documentation are in scope. AS2, AS4, and AS7 are
  included when the artifact contains an interface or rendered deliverable; otherwise they are
  `not_applicable`, not silently passed.
- **Cross-engine contract:** every adapter links to this shared gate, declares its applicable
  checks, preserves the existing ME1-ME7 exceptions, and must not broaden a source claim beyond
  the recorded scope.

## Testing and release criteria

1. Add a source-evaluation record and Kaizen record in Digital Research.
2. Add deterministic coverage tests for AS1-AS7 across all 12 target adapters.
3. Add a pressure fixture containing one positive case for each AS check and functional exceptions
   for requirements, finance, legal/policy, accessibility, and operational safety.
4. Run each engine's native validator, routing smoke test, source-ingestion/currentness gate,
   and relevant domain tests. Missing capabilities remain `NOT_ASSESSED`.
5. Run `git diff --check`, inspect staged diffs, commit per repository, push only to `main`, and
   verify zero ahead/behind after push.

## Recovery

If an adapter creates false-positive harm, remove only that adapter's AS mapping and retain the
shared source record and existing ME1-ME7 gate. If the source page changes materially, mark the
affected source claims `NOT_ASSESSED`, re-run source verification, and do not update the standard
until the scoped taxonomy is re-reviewed.
