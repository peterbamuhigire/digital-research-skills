# Cohort — vaccines

**Purpose:** enumerate every WHO-prequalified vaccine relevant to UG/KE/TZ EPI plus private/travel/occupational additions, with ATC J07 codes, schedules, cold-chain requirements, multi-dose-vial policy (MDVP), and AEFI Brighton classifications. This is the seed catalogue for Medic8's vaccine module (catalogue #8 of the onboarding spec).

## Scope (v1)

- All antigens in WHO IVB Routine Immunisation Summary
- All GAVI co-financed vaccines
- UG UNEPI, KE KEPI, TZ IVD national schedules
- Hepatitis B birth-dose policies per country
- Travel/occupational additions: yellow fever (ICVP), typhoid Vi/conjugate, cholera oral, MenACWY, hepatitis A, varicella, MMR private, zoster
- Rabies post-exposure (Essen + Zagreb regimens)
- Tetanus immunoglobulin

Out of v1: experimental / clinical-trial vaccines, vaccines withdrawn from WHO PQS list pre-2020.

## Data model (per spec)

`vaccine_code, atc_code, antigen, brand_names, who_pq_status, dose_form, route, dose_volume, schedule_who, schedule_uganda, schedule_kenya, schedule_tanzania, age_eligibility, contraindications, common_aefi_brighton, mdvp_compliant, open_vial_policy_hours, temperature_zone, who_pqs_fridge_class, supplier_default, gtin_pack, country_eml_codes, source_citations, code_system_version, code_accessed_date`

## Cross-cohort dependencies

- `atc_code` → `drugs` (J07 sub-tree)
- `temperature_zone` → `consumables` (cold-chain equipment, AD syringes, safety boxes, vaccine carriers)
- `schedule_*` → `workflows` (EPI session pathway)
- `country_eml_codes` → `country-packs`
- `common_aefi_brighton` → reporting (HMIS EPI dataset)

## Hard exclusions (project-wide)

- Veterinary vaccines
- Traditional / herbal preparations

## Outputs

- `research/wave1-data.md` — markdown table of antigens × the 25 columns above
- `research/wave1-findings.md` — narrative + bibliography
- `analysis/gap-analysis.md`
- `analysis/critical-reasoning-pass.md`
- `opportunities/product-ideas.md`

## Source tiers

- **T1:** WHO Vaccine Position Papers (per antigen), WHO PQS catalogue, country MoH EPI guidelines, GAVI procurement catalogue.
- **T2:** UNICEF Supply Catalogue, Brighton Collaboration AEFI definitions, country STG.
- **T3:** Manufacturer SmPCs, peer-reviewed implementation studies — never sole source.
