# Cohort — UCUM (units of measure)

**Purpose:** seed `tbl_uoms`, `tbl_uom_categories`, `tbl_uom_conversions` with the UCUM-canonical unit list that every clinical measurement, dose, lab result, and inventory quantity in Medic8 must reference. Small but blocking: lab-tests, drugs, vaccines, BOMs cohorts all reference UOMs.

## Scope (v1)

Cover every UCUM unit referenced (or implied) in our existing 14 cohorts plus the new Wave-3 cohorts. Practical universe per design doc §16.1:

- **Mass:** g, mg, mcg (µg), kg, ng
- **Volume:** mL, L, IU (international unit), mEq, mmol
- **Count units:** tab, cap, vial, amp, sachet, dose, drop, pack, box, strip, blister
- **Length:** mm, cm, m
- **Time:** min, hr, day, week, month
- **Concentration:** mg/mL, mg/L, %, mg/kg, mg/m², µg/mL, mmol/L
- **Lab counts:** 10*9/L, 10*12/L, cells/µL, cells/mm³, copies/mL
- **Pressure:** mmHg, kPa, cmH2O
- **Temperature:** °C, °F (display only)
- **Energy:** kcal, kJ
- **Rate:** drops/min, mL/hr, L/min
- **Pharmacology-specific:** DDD (defined daily dose), MED (morphine-equivalent dose)

Plus the conversion edges between every pair within a category (e.g., g ↔ mg ↔ mcg ↔ ng).

## Data model

```
uom_code (UCUM canonical), uom_display, category, base_uom_in_category,
conversion_factor_to_base, conversion_offset_to_base, ucum_canonical_form,
common_aliases, used_in_cohorts, source_citations, code_system_version, code_accessed_date
```

## Cross-cohort dependencies

- referenced by `lab-tests` (`unit` column), `drugs` (strength + dose UOMs), `vaccines` (dose volume), `paediatric-dosing` (`dose_per_kg_unit`), `boms` (`qty_in_base_uom`), `consumables` (pack-size, base UOM)
- canonical authority is UCUM; SNOMED CT unit codes referenced as cross-walk where Medic8 needs SCT bindings

## Hard exclusions

- None — UCUM is canonical and project-wide.

## Outputs

- `research/wave1-data.md` — UOM master table + conversion table
- `research/wave1-findings.md` — methodology, scope decisions, gap notes
- `analysis/gap-analysis.md`
- `analysis/critical-reasoning-pass.md`
- `opportunities/product-ideas.md`

## Source tiers

- **T1:** UCUM specification (Regenstrief Institute), UCUM essence file, ISO 80000 series.
- **T2:** SNOMED CT unit-of-measure concepts (cross-walk only), HL7 FHIR R4 unit value sets.
- **T3:** Vendor analyser unit conventions — only for documenting common aliases, never for canonical mapping.
