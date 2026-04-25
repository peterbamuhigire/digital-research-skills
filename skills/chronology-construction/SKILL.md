---
name: chronology-construction
description: Use whenever a project involves time-ordered events — builds a date-indexed timeline as a first-class research artefact. Cashore (via Rowland): "the heart, the backbone, of investigative journalism." Gaps in the chronology are work-queue items, not embarrassments.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Chronology construction

Cashore: *"You put in all kinds of dates… not only is your story written, but you begin to see gaps."* The chronology is simultaneously a synthesis tool and a gap-detection mechanism.

## What goes into the chronology

For every project with a time dimension:

```yaml
date: YYYY-MM-DD (or YYYY-MM, YYYY for less-precise events)
event: "..."
actors: [...]
location: <where>
sources: [{citation, url, tier}]
confidence: high | medium | low
related_minianalysis: <id>
```

Place every datable event in the chronology — laws passed, court rulings, market events, named incidents, statistical observations, key publications, PPP signings, allowance disbursements.

## Format

`projects/<project-id>/CHRONOLOGY.md`:

```markdown
# Chronology — <project>

## 1965
- 1965 (month unknown) — [Event] — [Source]

## 2018
- 2018-10-11 — Komakech & 7 Ors v Ayaa & Anor decided — [ULII]

## 2022
- 2022-06-17 — Uganda L&T Act 2022 enacted — [ULII]
- 2023-12-31 — Act becomes operative

## 2023
- 2023-08-02 — Daily Monitor publishes 80% deposit-non-refund investigation
- ...

## Open dates / gaps
- Date that Act § 26 first cited in court? — gap
- Date of first NEMA Lubigi demolition order? — gap
```

## Decision rules

- **Every datable event goes in.** Better one chronology with 200 events than five sub-chronologies.
- **Date-uncertainty marked, not hidden.** "2018 (specific month unknown)" is fine.
- **Gaps section at end.** What dates does the chronology suggest should exist but don't?
- **Cross-reference to crosswalk** — chronology gaps often map to crosswalk gaps.
- **Cross-reference to minianalyses** — each event ideally points to the minianalysis that surfaced it.
- **Re-read the chronology before any synthesis or report assembly.** The narrative often hides in the order.

## What the chronology surfaces

- **Causal chains** — A → B → C in time
- **Contradictions** — two sources place the same event differently
- **Latency** — gap between law passing and first enforcement
- **Cycles** — recurring events with periodicity
- **Acceleration / deceleration** — events bunching or spreading
- **Gaps** — periods that should have events but don't

The Cashore lesson: when you can see a clean chronology, you can see what's missing.

## Anti-patterns

- Chronology hidden in narrative prose — the format is part of the value
- Date-only chronology without sources — defeats verifiability
- Chronology built once, never updated
- Treating chronology as decorative — it's a synthesis tool
- Ignoring the gaps section — the gaps are why the chronology exists

## Pairs naturally with

- Schema I (historical research) — chronology is the centrepiece
- Schema A (pain-point research) — for time-bounded multi-cohort projects
- Schema F (due diligence) — entity history
- Schema G (OSINT) — temporal patterns
- Schema J (trends) — leading indicator construction

## See also

- `gap-analysis` — chronology gaps feed gap-analysis
- `crosswalk-matrix` — sibling synthesis tool
- `minianalysis-engine` — Timeline / Biography / Narrative is one of the four families
- `historical-research-methods` — chronology + source appraisal is the historical pair
