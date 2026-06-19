# healthcare-app-clinical-data

**Created:** 2026-05-03
**Client:** Internal team building a healthcare management app for Uganda
**Goal:** Sourced, locally-accurate clinical data corpus to seed the app's dropdowns, structured records, decision logic, and reference content.

## Cohorts

| # | Cohort | Min items | Coding standard |
|---|---|---|---|
| 1 | Most commonly diagnosed conditions | 200 | ICD-10 |
| 2 | Most commonly prescribed/issued drugs | full Uganda EMHSLU (~700) cross-mapped to WHO EML | ATC |
| 3 | Most common laboratory tests | 200 | LOINC |
| 4 | Most common imaging tests | 200 | LOINC + RadLex |
| 5 | Most common medical procedures (incl. dental) | 200 | ICD-10-PCS + CDT |

## Scope parameters

- **Geography:** Uganda primary; Kenya + Tanzania for triangulation
- **Ranking basis:** IHME GBD 2021 + WHO country profiles (DALYs / mortality)
- **Population:** all-ages merged with `population` column
- **Drug brands:** INN + 4 locally-registered brands (Uganda NDA primary, Kenya PPB + Tanzania TMDA secondary). Drugs not registered locally flagged with international fallback.
- **Lab/imaging detail:** full structured template (data-model depth)

## Hard exclusions (verbatim — restate in every sub-agent brief)

- Veterinary medicine
- Traditional / herbal medicine
- Cardiothoracic surgery
- Neurosurgery
- Transplant surgery

## Hard inclusions

- Dental procedures (CDT codes)

## Documents

- `CLAUDE.md` — sub-agent invariants for this project
- `PROJECT-STATUS.md` — wave tracker, multi-session resumption anchor
- `EVIDENCE-AUDIT.md` — every struck or flagged claim, per evidence-discipline
- `_context/` — coding standards, source tiers, geographic scope, exclusions, client brief
- `_registry/sources.bib` — master citation list
- `conditions/`, `drugs/`, `lab-tests/`, `imaging/`, `procedures/` — per-cohort `research/`, `analysis/`, `opportunities/` (the last is repurposed as app-implementation-notes)
- `export/` — final `.docx` reports + `.xlsx` data sheets

## See also

- `docs/plans/2026-05-03-healthcare-clinical-data-design.md`
- `docs/plans/2026-05-03-healthcare-clinical-data-plan.md`
- Repo root `CLAUDE.md` and `skills/source-evaluation/`
