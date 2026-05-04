# Cohort — country-packs

**Purpose:** make global rollout configurable. Each country pack supplies currency, timezone, languages, admin levels, regulators, mandatory reports, ID rules, privacy law, default forms, and default blueprints.

## Scope (v1)

- **Uganda** — full pack
- **Kenya** — full pack
- **Stub-only:** Tanzania, Rwanda, Ghana, Nigeria, South Africa, India, Philippines (header row + flagged `[STUB — pending future wave]` for every column except country_code, country_name, currency, timezone, languages)

## Data model

`country_code, country_name, currency, timezone, languages, admin_level_1_name, admin_level_2_name, facility_level_system, health_ministry, medicine_regulator, insurance_regulator, lab_regulator, mandatory_reports, national_id_rules, privacy_requirements, default_forms, default_blueprints`

## Source priorities

- T1: Uganda MoH, NDA, NHIA-Uganda (in development), UBOS; Kenya MoH, PPB, NHIF, KNBS; Data Protection Acts (Uganda 2019; Kenya 2019)
- T2: gazette notices, statutory instruments, IDSR/HMIS guidelines
- T3: peer-reviewed/grey lit — corroborating only

## Cross-cohort dependencies

- `default_blueprints` → `tenant-blueprints`
- `default_forms` → existing `standard-forms`
- `mandatory_reports` → `reporting-kpis`
- `medicine_regulator`, `lab_regulator` → existing `drugs`, `lab-tests`

## Outputs

Standard 5: `wave1-data.md`, `wave1-findings.md`, `gap-analysis.md`, `critical-reasoning-pass.md`, `product-ideas.md`.
