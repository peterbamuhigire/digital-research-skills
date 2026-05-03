# CLAUDE.md — healthcare-app-clinical-data

Sub-agent invariants for this project. Read alongside the repo root `CLAUDE.md` and `skills/source-evaluation/`.

## The verbatim hard-constraint clause

This block must appear verbatim in every sub-agent brief dispatched for this project:

```
HARD CONSTRAINT — NO HALLUCINATION:
- Do NOT invent statistics, names, organisations, court cases, statutes, or URLs.
- Cite every numeric claim and every direct quote at the point it appears.
- If you cannot find a source for a fact, mark it as a "gap" — do not fabricate filler.
- For any claim you assemble from multiple sources, mark it "(synthesis)".
- For any inference, mark it "(inference)".
- Verbatim quotes must reproduce text exactly as it appeared in the source — no creative editing.
- If a search returns nothing, report "no source found" — do not write what is plausible.
```

## Source-tier rule

- **T1 must be cited** as primary source for every item where T1 exists for that cohort
- **T2 may corroborate** or fill T1 gaps
- **T3 is never sole source** — must be paired with at least one T1 or T2

Per-cohort T1/T2/T3 lists are in `_context/source-tiers.md`.

## Geography

Uganda primary. Kenya + Tanzania for triangulation. East African Community states beyond these three are out of scope unless explicitly cited as comparators in WHO/IHME data.

## Hard exclusions (restate in every sub-agent brief)

- Veterinary medicine
- Traditional / herbal medicine
- Cardiothoracic surgery
- Neurosurgery
- Transplant surgery

Dental procedures are **explicitly included**.

## File-write conventions

- **Append, do not overwrite** when merging Wave-2 findings. Use `# Pass 2 — Gap-fill addendum` headers.
- **Never delete a sourced claim** without logging it in `EVIDENCE-AUDIT.md`.
- **Mark gaps explicitly** — `[GAP — no source found]` is a valid finding.
- **Date every research file** at the top.
- **List sources by tier** in each cohort's bibliography section.

## Per-cohort output shape (every sub-agent must produce both)

1. `<cohort>/research/wave1-findings.md` — narrative with categorisation analysis, gap notes, source bibliography for the wave
2. `<cohort>/research/wave1-data.md` — markdown table where columns match the data-model spec for that cohort (see `docs/plans/2026-05-03-healthcare-clinical-data-design.md` §4)

For Wave 2 these become `wave2-findings.md` / `wave2-data.md`, OR are appended to the Wave-1 files under `# Pass 2 — Gap-fill addendum`.

## Sub-agent completion `<result>` block — required content

Every sub-agent must report back with:

- Total items covered
- Items marked `[GAP — no source found]` (count + list of which fields)
- Sources used by tier (counts of T1 / T2 / T3 citations)
- New entries added to `_registry/sources.bib`
- Any blockers encountered (paywalls, dead links, register inaccessible)

## Tools the orchestrator uses heavily

- `Agent` — every research wave
- `WebFetch` — URL verification, statistic re-check, register lookup
- `Read` — cross-checking sub-agent outputs
- `Write` / `Edit` — for the markdown corpus
- `Grep` — for finding duplicate citations across cohorts (signals triangulation)

## Tools to avoid

- `Bash`-tail of sub-agent output files — overflows context
- Direct `.docx` editing — the markdown is canonical, Word is generated in Phase 5

## Resumption rule

`PROJECT-STATUS.md` is the single source of truth. On a new session: read it first, find the last completed task, resume from the next.

## Phase 5 Word-report requirement (user instruction 2026-05-03)

Every cohort's Word `.docx` report MUST include a §1 — Coding Standards section that:

1. Lists every standard used in that cohort (primary + bridge + adjunct)
2. Names the body that maintains each standard (with link)
3. Names the body that enforces each (regulator, MoH, accreditation, statutory) where any does
4. States the edition cited and why we use it for this cohort
5. Flags licensing constraints (CDT/ADA, GMDN paywall, SNOMED CT membership)
6. References `_context/standards-and-bodies.md` as the canonical inventory

The bar: reports must NOT just say "we use ICD-10". They must say what / who / enforced where / why / limits, in that style. See `_context/standards-and-bodies.md` for the exemplar.

## See also

- Repo root `CLAUDE.md`
- `skills/source-evaluation/SKILL.md` and `references/evidence-discipline.md`
- `_context/standards-and-bodies.md` — canonical standards + bodies inventory (drives every Word report's §1)
- `docs/plans/2026-05-03-healthcare-clinical-data-design.md`
- `docs/plans/2026-05-03-healthcare-clinical-data-plan.md`
