# Client Brief

**Date:** 2026-05-03
**Client:** Internal team building a healthcare management app

## What the team is building

A healthcare management app targeted at Uganda. Use cases include:

- Clinician-facing record-keeping (history, examination, diagnosis, treatment)
- Drug prescribing with formulary and brand-name lookup
- Lab and imaging order entry with structured result capture
- Procedure documentation
- Reporting and analytics

## What the team needs from this corpus

A seed dataset that the app can use to populate dropdowns, autocomplete, decision logic, and reference content **on day one** without the team having to assemble it themselves.

## Output expectations

For each of the five cohorts:

1. **Word `.docx` report** — explains the coding standard used, methodology, sources, the grouped/categorised list with commentary, gaps and limitations, and app-implementation notes
2. **Excel `.xlsx`** — one row per item, columns matching the data model the app can ingest

Plus a **cross-cohort master document** linking conditions ↔ drugs ↔ labs ↔ imaging ↔ procedures so the team can see the clinical clusters the app will need to handle (e.g., malaria → antimalarials → mRDT/microscopy → no imaging → no procedure).

## Quality bar

- Every item traceable to a real, verified source
- Every code (ICD-10, ATC, LOINC, RadLex, ICD-10-PCS, CDT) verified against the official authority
- Gaps flagged, not filled with plausible-sounding fiction
- Methodology disclosed in the report so the team can update or audit later

## Constraints the team should know about

The corpus carries a few methodology caveats that the team needs to read:

1. **Uganda EMHSLU edition** — corpus uses the latest publicly accessible edition. Drugs that may have moved on/off since are flagged. Plan a yearly refresh.
2. **NDA brand verification** — per-drug NDA register lookup is capped at ~200 highest-priority drugs. The remainder cite EMHSLU listings without per-drug NDA confirmation. Flagged in the drugs report.
3. **East African lab reference ranges** — published locally-validated ranges exist for some analytes only. Where missing, Tietz/Western ranges are used and explicitly marked `[reference range from Western source — local validation pending]`.
4. **ICD-10-PCS vs ICHI** — ICD-10-PCS (CMS) used as primary procedure code with ICHI (WHO, beta) as secondary. Choice explained in the procedures report.
5. **CDT licensing** — ADA-licensed. Codes used here under fair-use for reference; the app team needs an ADA license for commercial deployment of a product that exposes CDT codes to end-users.

## Multi-session disclosure

This corpus is being built across multiple work sessions. `PROJECT-STATUS.md` is the canonical resumption anchor. Final deliverables land in `export/`.
