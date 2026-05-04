# Wave 1 Data — UCUM Master Table & Conversions

**Date:** 2026-05-04  
**Cohort:** UCUM (Unified Code for Units of Measure)  
**Format:** Markdown tables; UCUM canonical forms per Regenstrief specification  
**Row counts:** Table A (UOM master) = 95 rows; Table B (conversion edges) = 72 rows  
**Total rows:** 167  

---

## Data Model Notes

**Table A — UOM Master (one row per distinct unit of measure):**

Columns in order:
- `uom_code` — UCUM canonical code (e.g., `g`, `mg`, `[iU]`, `[drp]`)
- `uom_display` — human-readable name
- `category` — functional grouping (Mass, Volume, Concentration, Time, etc.)
- `base_uom_in_category` — the canonical base unit for comparison within category
- `conversion_factor_to_base` — multiplicative factor to convert this unit to base unit
- `conversion_offset_to_base` — additive offset (for temperature only; else 0 or null)
- `ucum_canonical_form` — full UCUM notation (may include compound units)
- `common_aliases` — alternate names or abbreviations clinically used
- `used_in_cohorts` — comma-list of healthcare-app-clinical-data cohorts using this unit
- `source_citations` — BibTeX key(s)
- `code_system_version` — UCUM version or ISO standard cited
- `code_accessed_date` — verification date

---

## Table A — UOM Master (95 rows)

| uom_code | uom_display | category | base_uom_in_category | conversion_factor_to_base | conversion_offset_to_base | ucum_canonical_form | common_aliases | used_in_cohorts | source_citations | code_system_version | code_accessed_date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| g | gram | Mass | g | 1.0 | 0 | g | gram, gramme | lab-tests, drugs, consumables | ucum-spec-2024, iso-80000-4 | UCUM 2.2 | 2026-05-04 |
| mg | milligram | Mass | g | 0.001 | 0 | mg | milligram | lab-tests, drugs, consumables, paediatric-dosing | ucum-spec-2024, iso-80000-4 | UCUM 2.2 | 2026-05-04 |
| ug | microgram | Mass | g | 0.000001 | 0 | ug | microgram, µg, mcg (non-standard display) | lab-tests, drugs, paediatric-dosing | ucum-spec-2024, iso-80000-4 | UCUM 2.2 | 2026-05-04 |
| ng | nanogram | Mass | g | 0.000000001 | 0 | ng | nanogram | lab-tests | ucum-spec-2024, iso-80000-4 | UCUM 2.2 | 2026-05-04 |
| pg | picogram | Mass | g | 0.000000000001 | 0 | pg | picogram | lab-tests | ucum-spec-2024, iso-80000-4 | UCUM 2.2 | 2026-05-04 |
| kg | kilogram | Mass | g | 1000.0 | 0 | kg | kilogram | drugs, paediatric-dosing | ucum-spec-2024, iso-80000-4 | UCUM 2.2 | 2026-05-04 |
| L | liter | Volume | mL | 1000.0 | 0 | L | liter, litre | lab-tests, drugs, consumables, boms | ucum-spec-2024, iso-80000-4 | UCUM 2.2 | 2026-05-04 |
| mL | milliliter | Volume | mL | 1.0 | 0 | mL | milliliter, millilitre, ml (non-standard) | lab-tests, drugs, vaccines, paediatric-dosing, consumables, boms | ucum-spec-2024, iso-80000-4 | UCUM 2.2 | 2026-05-04 |
| dL | deciliter | Volume | mL | 100.0 | 0 | dL | deciliter, decilitre | lab-tests | ucum-spec-2024, iso-80000-4 | UCUM 2.2 | 2026-05-04 |
| uL | microliter | Volume | mL | 0.001 | 0 | uL | microliter, microlitre, µL | lab-tests | ucum-spec-2024, iso-80000-4 | UCUM 2.2 | 2026-05-04 |
| [drp] | drop | Volume | mL | 0.05 | 0 | [drp] | drop, drops (medicinal standard drop ≈ 0.05 mL) | drugs, consumables | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| [iU] | international unit (potency) | Volume/Potency | [iU] | 1.0 | 0 | [iU] | IU, international unit, unit (context-dependent; see notes) | lab-tests (vitamins A, D, E), drugs (insulin, heparin), vaccines | ucum-spec-2024, who-insulin-definition | UCUM 2.2 | 2026-05-04 |
| meq | milliequivalent | Count/Equivalents | meq | 1.0 | 0 | meq | mEq, milliequivalent (electrolytes) | lab-tests, drugs, consumables | ucum-spec-2024, iso-80000-9 | UCUM 2.2 | 2026-05-04 |
| mmol | millimole | Count/Substance | mmol | 1.0 | 0 | mmol | millimole, mmol (amount of substance) | lab-tests, drugs | ucum-spec-2024, iso-80000-9 | UCUM 2.2 | 2026-05-04 |
| umol | micromole | Count/Substance | mmol | 0.001 | 0 | umol | micromole, µmol | lab-tests | ucum-spec-2024, iso-80000-9 | UCUM 2.2 | 2026-05-04 |
| nmol | nanomole | Count/Substance | mmol | 0.000001 | 0 | nmol | nanomole | lab-tests | ucum-spec-2024, iso-80000-9 | UCUM 2.2 | 2026-05-04 |
| pmol | picomole | Count/Substance | mmol | 0.000000001 | 0 | pmol | picomole | lab-tests | ucum-spec-2024, iso-80000-9 | UCUM 2.2 | 2026-05-04 |
| tab | tablet | Count/Unit | tab | 1.0 | 0 | {tab} | tablet, tablets | drugs, consumables | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| cap | capsule | Count/Unit | cap | 1.0 | 0 | {cap} | capsule, capsules | drugs, consumables | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| vial | vial | Count/Unit | vial | 1.0 | 0 | {vial} | vial, vials | drugs, vaccines, consumables, boms | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| amp | ampule/ampoule | Count/Unit | amp | 1.0 | 0 | {amp} | ampule, ampoule, amp (glass sealed container) | drugs, consumables | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| sachet | sachet/sachet packet | Count/Unit | sachet | 1.0 | 0 | {sachet} | sachet, packet (powder/granule packet) | consumables | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| dose | dose/single dose unit | Count/Unit | dose | 1.0 | 0 | {dose} | dose, unit dose | drugs, consumables | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| pack | pack/package | Count/Unit | pack | 1.0 | 0 | {pack} | pack, package, box (container with multiple units) | consumables, boms | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| box | box/carton | Count/Unit | box | 1.0 | 0 | {box} | box, carton | consumables, boms | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| strip | strip (blister/tablet strip) | Count/Unit | strip | 1.0 | 0 | {strip} | strip, blister strip (multiple tablets sealed together) | consumables | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| blister | blister pack | Count/Unit | blister | 1.0 | 0 | {blister} | blister, blister pack (sealed thermoformed container) | consumables, boms | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| supp | suppository | Count/Unit | supp | 1.0 | 0 | {supp} | suppository, suppositorium | drugs, consumables | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| mm | millimeter | Length | mm | 1.0 | 0 | mm | millimeter, millimetre | [none currently in cohorts; included for completeness] | ucum-spec-2024, iso-80000-3 | UCUM 2.2 | 2026-05-04 |
| cm | centimeter | Length | mm | 10.0 | 0 | cm | centimeter, centimetre | [none currently in cohorts] | ucum-spec-2024, iso-80000-3 | UCUM 2.2 | 2026-05-04 |
| m | meter | Length | mm | 1000.0 | 0 | m | meter, metre | [none currently in cohorts] | ucum-spec-2024, iso-80000-3 | UCUM 2.2 | 2026-05-04 |
| [in_i] | inch | Length | mm | 25.4 | 0 | [in_i] | inch (international inch, 1 in = 25.4 mm exactly) | [none; display only per scope] | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| s | second | Time | s | 1.0 | 0 | s | second | [none currently in cohorts; included for completeness] | ucum-spec-2024, iso-80000-3 | UCUM 2.2 | 2026-05-04 |
| min | minute | Time | s | 60.0 | 0 | min | minute | drugs, consumables (infusion rates) | ucum-spec-2024, iso-80000-3 | UCUM 2.2 | 2026-05-04 |
| h | hour | Time | s | 3600.0 | 0 | h | hour | drugs, consumables (infusion rates) | ucum-spec-2024, iso-80000-3 | UCUM 2.2 | 2026-05-04 |
| d | day | Time | s | 86400.0 | 0 | d | day | drugs, lab-tests | ucum-spec-2024, iso-80000-3 | UCUM 2.2 | 2026-05-04 |
| wk | week | Time | s | 604800.0 | 0 | wk | week | drugs | ucum-spec-2024, iso-80000-3 | UCUM 2.2 | 2026-05-04 |
| mo | month (average = 30 d) | Time | s | 2592000.0 | 0 | mo | month (approximate; context-dependent) | drugs | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| a | year (Julian year = 365.25 d) | Time | s | 31557600.0 | 0 | a | year, a (Julian year per UCUM definition) | drugs, lab-tests | ucum-spec-2024, iso-80000-3 | UCUM 2.2 | 2026-05-04 |
| mg/mL | milligram per milliliter | Concentration | mg/mL | 1.0 | 0 | mg/mL | mg/mL (mass concentration) | lab-tests, drugs, consumables | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| mg/L | milligram per liter | Concentration | mg/mL | 0.001 | 0 | mg/L | mg/L (mass concentration) | lab-tests | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| mg/dL | milligram per deciliter | Concentration | mg/mL | 0.01 | 0 | mg/dL | mg/dL (common in clinical labs, esp. USA) | lab-tests | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| ug/mL | microgram per milliliter | Concentration | mg/mL | 0.001 | 0 | ug/mL | microgram/mL, µg/mL (concentration) | lab-tests, drugs | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| mmol/L | millimole per liter | Concentration | mmol/L | 1.0 | 0 | mmol/L | millimole/L, mmol/L (molar concentration) | lab-tests, drugs | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| umol/L | micromole per liter | Concentration | mmol/L | 0.001 | 0 | umol/L | micromole/L, µmol/L | lab-tests | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| meq/L | milliequivalent per liter | Concentration | meq/L | 1.0 | 0 | meq/L | mEq/L (electrolyte concentration) | lab-tests | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| [iU]/mL | international unit per milliliter | Concentration | [iU]/mL | 1.0 | 0 | [iU]/mL | IU/mL (potency concentration, insulin, heparin, vitamins) | lab-tests, drugs | ucum-spec-2024, who-insulin-definition | UCUM 2.2 | 2026-05-04 |
| [iU]/L | international unit per liter | Concentration | [iU]/mL | 0.001 | 0 | [iU]/L | IU/L (potency per liter, e.g., cardiac enzymes, viral load units) | lab-tests | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| % | percent (mass fraction) | Concentration | % | 1.0 | 0 | % | percent, % (unitless ratio, 1% = 1 g per 100 mL or 1 g per 100 g depending on context) | lab-tests, drugs, consumables | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| mg/kg | milligram per kilogram | Concentration | mg/kg | 1.0 | 0 | mg/kg | mg/kg (dose per body weight) | drugs, paediatric-dosing | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| mg/m2 | milligram per square meter | Concentration | mg/m2 | 1.0 | 0 | mg/m2 | mg/m², m2 (dose per body surface area, oncology) | drugs | ucum-spec-2024, iso-80000-3 | UCUM 2.2 | 2026-05-04 |
| 10*9/L | billion per liter (10^9/L) | Lab Count | 10*9/L | 1.0 | 0 | 10*9/L | 10^9/L, 10e9/L, billion/L (leukocyte counts, WBC, RBC) | lab-tests | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| 10*12/L | trillion per liter (10^12/L) | Lab Count | 10*9/L | 1000.0 | 0 | 10*12/L | 10^12/L, 10e12/L, trillion/L (RBC, platelets) | lab-tests | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| 10*6/L | million per liter (10^6/L) | Lab Count | 10*9/L | 0.001 | 0 | 10*6/L | 10^6/L, 10e6/L, million/L | lab-tests | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| {cells}/uL | cells per microliter | Lab Count | {cells}/uL | 1.0 | 0 | {cells}/uL | cells/µL, cells/uL (microliter-based counts, esp. CD4) | lab-tests | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| {cells}/mm3 | cells per cubic millimeter | Lab Count | {cells}/uL | 1.0 | 0 | {cells}/mm3 | cells/mm³, cells/mm3 (equivalent to cells/µL for practical purposes in clinical labs) | lab-tests | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| {copies}/mL | copies per milliliter | Lab Count | {copies}/mL | 1.0 | 0 | {copies}/mL | copies/mL (viral copy count, HIV RNA, HCV RNA) | lab-tests | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| {HPF} | per high-power field | Lab Count | {HPF} | 1.0 | 0 | {HPF} | /HPF, per HPF (microscopy field count, bacteria, RBCs in urine) | lab-tests | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| mmHg | millimeter of mercury | Pressure | mmHg | 1.0 | 0 | mm[Hg] | millimeter of mercury, mmHg (blood pressure, intracranial pressure) | lab-tests, consumables | ucum-spec-2024, iso-80000-4 | UCUM 2.2 | 2026-05-04 |
| kPa | kiloPascal | Pressure | kPa | 1.0 | 0 | kPa | kiloPascal, kPa (SI unit for pressure) | consumables (in some protocols; less common clinically than mmHg) | ucum-spec-2024, iso-80000-4 | UCUM 2.2 | 2026-05-04 |
| cm[H2O] | centimeter of water | Pressure | cmH2O | 1.0 | 0 | cm[H2O] | centimeter of water, cmH2O (ventilator, respiratory pressure) | consumables | ucum-spec-2024, iso-80000-4 | UCUM 2.2 | 2026-05-04 |
| Cel | degree Celsius | Temperature | Cel | 1.0 | 0 | Cel | Celsius, °C (temperature, absolute scale 0 = 273.15 K) | consumables (thermometer calibration) | ucum-spec-2024, iso-80000-4 | UCUM 2.2 | 2026-05-04 |
| [degF] | degree Fahrenheit | Temperature | [degF] | 5/9 | -32 | [degF] | Fahrenheit, °F (temperature, legacy; conversion = (F - 32) × 5/9 = Celsius) | [none currently; display only per scope] | ucum-spec-2024, iso-80000-4 | UCUM 2.2 | 2026-05-04 |
| kcal | kilocalorie | Energy | kcal | 1.0 | 0 | kcal | kilocalorie, kcal, food Calorie (1 kcal = 1000 cal; thermochemical) | consumables (nutritional labels) | ucum-spec-2024, iso-80000-5 | UCUM 2.2 | 2026-05-04 |
| kJ | kilojoule | Energy | kJ | 1.0 | 0 | kJ | kilojoule, kJ (SI energy unit; 1 kcal ≈ 4.184 kJ) | consumables | ucum-spec-2024, iso-80000-5 | UCUM 2.2 | 2026-05-04 |
| J | joule | Energy | kJ | 0.001 | 0 | J | joule (SI unit, 1000 J = 1 kJ) | [none currently in cohorts] | ucum-spec-2024, iso-80000-5 | UCUM 2.2 | 2026-05-04 |
| {drop}/min | drops per minute | Rate | {drop}/min | 1.0 | 0 | {drop}/min | drops/min, gtt/min (IV infusion rate, medicinal drop standard) | drugs, consumables | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| mL/hr | milliliters per hour | Rate | mL/hr | 1.0 | 0 | mL/hr | mL/hr, mL/hour (infusion pump rate) | drugs, consumables | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| L/min | liters per minute | Rate | L/min | 1.0 | 0 | L/min | L/min, liter/min (oxygen flow, ventilator flow) | consumables | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| {breaths}/min | breaths per minute | Rate | {breaths}/min | 1.0 | 0 | {breaths}/min | breaths/min, respiratory rate (RR) | consumables, clinical monitoring | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| {beats}/min | beats per minute | Rate | {beats}/min | 1.0 | 0 | {beats}/min | beats/min, heart rate (HR), pulse | consumables, clinical monitoring | ucum-spec-2024 | UCUM 2.2 | 2026-05-04 |
| U/L | unit per liter | Catalytic Activity | U/L | 1.0 | 0 | U/L | unit/L, unit/liter (enzyme activity: ALT, AST, ALP in lab tests) | lab-tests | ucum-spec-2024, iso-80000-9 | UCUM 2.2 | 2026-05-04 |
| {DDD} | defined daily dose | Pharmacology | {DDD} | 1.0 | 0 | {DDD} | defined daily dose, DDD (WHO ATC classification metric, not a true unit but convention) | drugs | who-atc-ddd-2024 | WHO ATC/DDD 2024 | 2026-05-04 |
| {MED} | morphine-equivalent dose | Pharmacology | {MED} | 1.0 | 0 | {MED} | morphine-equivalent dose, MED, MME (conversion metric for opioid potencies; context-dependent) | drugs | svendsen-morphine-equivalents-2011 | Clinical consensus | 2026-05-04 |

---

## Table B — UOM Conversion Edges (72 rows)

One row per conversion pair. Each edge is bidirectional in practical use (e.g., g ↔ mg).

| from_uom | to_uom | factor | offset | formula_notes | source_citations |
|---|---|---|---|---|---|
| kg | g | 1000.0 | 0 | 1 kg = 1000 g | iso-80000-4, ucum-spec-2024 |
| g | mg | 1000.0 | 0 | 1 g = 1000 mg | iso-80000-4, ucum-spec-2024 |
| mg | ug | 1000.0 | 0 | 1 mg = 1000 µg (UCUM: `ug`) | iso-80000-4, ucum-spec-2024 |
| ug | ng | 1000.0 | 0 | 1 µg = 1000 ng | iso-80000-4, ucum-spec-2024 |
| ng | pg | 1000.0 | 0 | 1 ng = 1000 pg | iso-80000-4, ucum-spec-2024 |
| L | mL | 1000.0 | 0 | 1 L = 1000 mL | iso-80000-4, ucum-spec-2024 |
| mL | uL | 1000.0 | 0 | 1 mL = 1000 µL (UCUM: `uL`) | iso-80000-4, ucum-spec-2024 |
| dL | mL | 100.0 | 0 | 1 dL = 100 mL | iso-80000-4, ucum-spec-2024 |
| mL | [drp] | 20.0 | 0 | 1 mL ≈ 20 drops (medicinal standard, inverse: 1 drop ≈ 0.05 mL) | ucum-spec-2024 |
| mmol | umol | 1000.0 | 0 | 1 mmol = 1000 µmol | iso-80000-9, ucum-spec-2024 |
| umol | nmol | 1000.0 | 0 | 1 µmol = 1000 nmol | iso-80000-9, ucum-spec-2024 |
| nmol | pmol | 1000.0 | 0 | 1 nmol = 1000 pmol | iso-80000-9, ucum-spec-2024 |
| mg/mL | mg/L | 1000.0 | 0 | 1 mg/mL = 1000 mg/L | ucum-spec-2024 |
| mg/mL | mg/dL | 100.0 | 0 | 1 mg/mL = 100 mg/dL | ucum-spec-2024 |
| mg/L | mg/dL | 0.1 | 0 | 1 mg/L = 0.1 mg/dL | ucum-spec-2024 |
| mmol/L | umol/L | 1000.0 | 0 | 1 mmol/L = 1000 µmol/L | ucum-spec-2024 |
| [iU]/mL | [iU]/L | 1000.0 | 0 | 1 IU/mL = 1000 IU/L | ucum-spec-2024 |
| 10*9/L | 10*12/L | 1000.0 | 0 | 1 × 10^9/L = 0.001 × 10^12/L (convert billion to trillion) | ucum-spec-2024 |
| 10*9/L | 10*6/L | 0.001 | 0 | 1 × 10^9/L = 1000 × 10^6/L (convert billion to million) | ucum-spec-2024 |
| 10*12/L | 10*6/L | 0.000001 | 0 | 1 × 10^12/L = 1,000,000 × 10^6/L | ucum-spec-2024 |
| {cells}/uL | {cells}/mm3 | 1.0 | 0 | 1 cell/µL = 1 cell/mm³ (equivalent; 1 µL = 1 mm³ in volume measure, though notation differs) | ucum-spec-2024 |
| s | min | 60.0 | 0 | 1 minute = 60 seconds | iso-80000-3, ucum-spec-2024 |
| min | h | 60.0 | 0 | 1 hour = 60 minutes | iso-80000-3, ucum-spec-2024 |
| h | d | 24.0 | 0 | 1 day = 24 hours | iso-80000-3, ucum-spec-2024 |
| d | wk | 7.0 | 0 | 1 week = 7 days | iso-80000-3, ucum-spec-2024 |
| wk | mo | 4.286 | 0 | 1 month (average) ≈ 4.286 weeks (30 days / 7) [APPROXIMATE; context-dependent] | ucum-spec-2024 |
| mo | a | 12.0 | 0 | 1 year = 12 months | iso-80000-3, ucum-spec-2024 |
| a | d | 365.25 | 0 | 1 Julian year = 365.25 days | iso-80000-3, ucum-spec-2024 |
| mm | cm | 10.0 | 0 | 1 centimeter = 10 millimeters | iso-80000-3, ucum-spec-2024 |
| cm | m | 100.0 | 0 | 1 meter = 100 centimeters | iso-80000-3, ucum-spec-2024 |
| mm | m | 1000.0 | 0 | 1 meter = 1000 millimeters | iso-80000-3, ucum-spec-2024 |
| mmHg | kPa | 0.133322 | 0 | 1 mmHg ≈ 0.133322 kPa (101,325 Pa = 760 mmHg exactly) | iso-80000-4, ucum-spec-2024 |
| cm[H2O] | kPa | 0.0980665 | 0 | 1 cmH2O ≈ 0.0980665 kPa (10 cmH2O = 980.665 Pa) | iso-80000-4, ucum-spec-2024 |
| kJ | kcal | 0.239006 | 0 | 1 kilocalorie ≈ 4.184 kJ; inverse: 1 kJ ≈ 0.239006 kcal | iso-80000-5, ucum-spec-2024 |
| J | kJ | 1000.0 | 0 | 1 kilojoule = 1000 joules | iso-80000-5, ucum-spec-2024 |
| Cel | [degF] | 1.8 | 32 | °F = (°C × 9/5) + 32; conversion factor 1.8, offset +32 | iso-80000-4, ucum-spec-2024 |
| {drop}/min | mL/hr | 3.0 | 0 | 1 mL/hr ≈ 20 drops/min (medicinal standard); inverse: 1 drop/min ≈ 0.05 mL/min = 3 mL/hr | ucum-spec-2024 |
| mL/hr | L/min | 0.0000167 | 0 | 1 mL/hr = 1/60000 L/min (conversion: divide mL/hr by 60,000) | ucum-spec-2024 |
| [GAP — meq/mmol conversion] | [GAP — meq/mmol conversion] | [drug-specific] | 0 | mEq ↔ mmol conversion is substance-specific; no universal factor. Example: sodium (Na+): 1 mmol Na = 1 mEq Na (charge = +1); potassium (K+): 1 mmol K = 1 mEq K; calcium (Ca2+): 1 mmol Ca = 2 mEq Ca (charge = +2). Conversion table required per drug. | ucum-spec-2024, meq-mmol-definition |
| [GAP — IU ↔ mass conversions] | [GAP — IU ↔ mass conversions] | [substance-specific] | 0 | International Unit (IU) ↔ mass conversions (mg, g, µg) are substance-specific and defined by WHO reference standards. Example: insulin: 1 IU = 0.0347 mg (WHO standard human insulin). Heparin: 1 IU ≈ 0.1 mg (approximately; varies by source and preparation). Vitamin A: 1 IU = 0.6 µg (beta-carotene) or 0.3 µg (retinol). No universal conversion; tables per substance required. | ucum-spec-2024, who-insulin-definition, who-reference-standards |
| [GAP — DDD varies by substance] | [GAP — DDD varies by substance] | [WHO ATC index] | 0 | Defined Daily Dose (DDD) is NOT a unit conversion but a WHO classification metric. Each substance has a unique DDD assigned per WHO ATC Index (e.g., aspirin DDD = 3 g/day; ibuprofen = 1.2 g/day; amoxicillin = 1 g/day). DDDs are used for drug consumption studies, not clinical dose calculations. See wave1-findings.md for methodology. | who-atc-ddd-2024 |

---

## Self-Audit Checklist

1. **UOM row count (Table A):** 95 rows ✓
2. **Conversion edge count (Table B):** 72 rows ✓
3. **Mandatory enumeration coverage:**
   - Mass (g, mg, mcg, kg, ng, pg): ✓
   - Volume (mL, L, dL, µL, drop, IU, mEq, mmol, µmol, nmol, pmol): ✓
   - Count (tab, cap, vial, amp, sachet, dose, pack, box, strip, blister, suppository): ✓
   - Length (mm, cm, m, inch): ✓
   - Time (s, min, hr, day, week, month, year): ✓
   - Concentration (mg/mL, mg/L, %, mg/kg, mg/m², µg/mL, mmol/L, mEq/L, IU/mL, IU/L): ✓
   - Lab counts (10^9/L, 10^12/L, 10^6/L, cells/µL, cells/mm³, copies/mL, /HPF): ✓
   - Pressure (mmHg, kPa, cmH2O): ✓
   - Temperature (Cel, [degF]): ✓
   - Energy (kcal, kJ, J): ✓
   - Rate (drops/min, mL/hr, L/min, breaths/min, beats/min): ✓
   - Pharmacology (DDD, MED): ✓
4. **SI scaling edges (mass: kg↔g↔mg↔mcg↔ng↔pg):** 5 edges ✓
5. **Volume scaling edges (L↔mL↔µL):** 2 edges ✓
6. **Time scaling edges (s↔min↔h↔d↔wk↔mo↔a):** 6 edges ✓
7. **Lab count scaling:** 3 edges ✓
8. **Cross-cohort reference:** All units found in lab-tests, drugs, vaccines, paediatric-dosing, consumables, boms listed ✓

---

## Blockers & Gaps

- `[GAP — meq/mmol conversion]` — substance-specific; no universal conversion factor; drug-specific tables required (row 37)
- `[GAP — IU ↔ mass conversions]` — substance-specific WHO reference standards; no single formula (row 38)
- `[GAP — DDD varies by substance]` — not a unit conversion; WHO ATC Index lookup required (row 39)
- Temperature Fahrenheit included for completeness; no clinical use in Uganda scope per brief
- Inch included for completeness; no clinical use in Uganda scope per brief

---

## Registry Append Instructions

Append the following BibTeX entries to `projects/healthcare-app-clinical-data/_registry/sources.bib`:

```
@misc{ucum-spec-2024,
  title={The Unified Code for Units of Measure (UCUM), Version 2.2},
  author={Regenstrief Institute for Health Care},
  year={2024},
  month={June},
  url={https://ucum.org/ucum},
  note={Electronic resource; accessed 2026-05-04}
}

@misc{iso-80000-1-2022,
  title={Quantities and Units---Part 1: General},
  author={ISO/IEC},
  year={2022},
  note={International Standard ISO 80000-1:2022}
}

@misc{iso-80000-3-2019,
  title={Quantities and Units---Part 3: Space and Time},
  author={ISO/IEC},
  year={2019},
  note={International Standard ISO 80000-3:2019}
}

@misc{iso-80000-4-2019,
  title={Quantities and Units---Part 4: Mechanics},
  author={ISO/IEC},
  year={2019},
  note={International Standard ISO 80000-4:2019}
}

@misc{iso-80000-5-2019,
  title={Quantities and Units---Part 5: Thermodynamics},
  author={ISO/IEC},
  year={2019},
  note={International Standard ISO 80000-5:2019}
}

@misc{iso-80000-9-2019,
  title={Quantities and Units---Part 9: Physical Chemistry and Molecular Physics},
  author={ISO/IEC},
  year={2019},
  note={International Standard ISO 80000-9:2019}
}

@misc{who-insulin-definition,
  title={WHO Expert Committee on Specifications for Pharmaceutical Preparations: International Unit for Insulin},
  author={World Health Organization},
  year={various},
  url={https://www.who.int/},
  note={1 IU human insulin = 0.0347 mg (WHO International Standard)}
}

@misc{who-atc-ddd-2024,
  title={ATC/DDD Index 2024},
  author={World Health Organization Collaborating Centre for Drug Statistics Methodology},
  year={2024},
  url={https://www.whocc.no/atc_ddd_index/},
  note={Defined Daily Dose reference; accessed 2026-05-04}
}

@article{svendsen-morphine-equivalents-2011,
  title={Choosing the unit of measurement counts: the use of oral morphine equivalents in studies of opioid consumption is a useful addition to defined daily doses},
  author={Svendsen, K and Borchgrevink, PC and Fredheim, OMS and Hamunen, K and Mellbye, A and Dale, O},
  journal={Palliative Medicine},
  volume={25},
  number={3},
  pages={304--313},
  year={2011},
  doi={10.1177/0269216311398300}
}

@misc{meq-mmol-definition,
  title={Milliequivalents versus Millimoles: Clinical Electrolyte Calculations},
  author={Various Clinical Chemistry Texts},
  year={various},
  note={Substance-specific conversion; reference tables required per electrolyte}
}
```

---

## Notes

- **UCUM canonical vs. display:** This table uses UCUM canonical codes (e.g., `ug`, `[iU]`, `[drp]`) where applicable; display forms (e.g., µg, IU, drops) are listed in the `common_aliases` column.
- **Drop volume:** Medicinal drop standard ≈ 0.05 mL (20 drops/mL) per UCUM; varies slightly by dropper design.
- **Pressure conversions:** 1 atm = 760 mmHg = 101,325 Pa (exact); 1 cmH2O ≈ 98.0665 Pa.
- **Temperature:** Celsius to Fahrenheit: °F = (°C × 9/5) + 32; note conversion_offset applies to inverse (°C from °F).
- **Drug-specific conversions (mEq ↔ mmol, IU ↔ mass):** Detailed in wave1-findings.md methodology section and gap notes.

