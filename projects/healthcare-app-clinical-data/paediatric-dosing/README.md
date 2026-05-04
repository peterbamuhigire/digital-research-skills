# Cohort — paediatric-dosing

**Purpose:** seed `tbl_paediatric_dosing` with weight-band and age-band dosing rules for every paediatric-relevant drug, so Medic8's prescribing CDS can flag under/overdose risks at point of order. Without this, paediatric prescribing in Medic8 is unsafe by design.

## Scope (v1)

Coverage target: every drug in our `drugs` cohort that has WHO Model Formulary for Children (WMFc 2010) or WHO EMLc 2023 paediatric guidance — typical scope ~250 drugs.

Per-drug, per-route, per-indication: minimum dose, maximum dose, mg/kg/dose, mg/kg/day, max single-dose, max daily-dose, age cut-offs, weight-band rules, neonatal-specific rules where applicable, frequency.

Out of v1: full neonatal intensive-care drug guidance (deferred); chemotherapy paediatric dosing (out of project scope unless oncology toggled in).

## Data model

```
dosing_id, atc_code, indication, route, age_band_min_months, age_band_max_months,
weight_band_min_kg, weight_band_max_kg, dose_per_kg, dose_per_kg_unit,
frequency, max_single_dose, max_daily_dose, neonatal_specific, premature_specific,
renal_adjustment_required, hepatic_adjustment_required,
source_reference (WMFc page / EMLc section), source_citations,
code_system_version, code_accessed_date
```

## Cross-cohort dependencies

- `atc_code` → `drugs`
- referenced by Medic8 prescribing CDS engine
- weight-band logic must align with country IMCI weight bands (UG / KE / TZ)

## Hard exclusions (project-wide)

- Veterinary, traditional/herbal — no rows
- Cardiothoracic / neuro / transplant peri-operative dosing — out of scope

## Outputs

- `research/wave1-data.md` — dosing rules table
- `research/wave1-findings.md` — methodology, weight-band derivation, gap notes
- `analysis/gap-analysis.md`
- `analysis/critical-reasoning-pass.md`
- `opportunities/product-ideas.md`

## Source tiers

- **T1:** WHO Model Formulary for Children 2010 (full text), WHO EMLc 2023, WHO IMCI weight-band charts, WHO Pocket Book of Hospital Care for Children 2nd ed.
- **T2:** Country paediatric protocols (KE Basic Paediatric Protocols 2022, UG Clinical Guidelines paediatric chapter, TZ STG paediatric).
- **T3:** Peer-reviewed paediatric-pharmacology literature — supporting role.
