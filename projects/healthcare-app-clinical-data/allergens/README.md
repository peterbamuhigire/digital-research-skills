# Cohort — allergens

**Purpose:** seed `tbl_allergens` with the canonical allergen ingredient list that drives patient-banner allergy display, prescription-time allergy checks, and CDS engine rules. Required before any patient-record allergy field is meaningful.

## Scope (v1)

Three groups:

1. **Drug-class allergens** (RxNorm allergen ingredients): penicillin class, cephalosporin class, sulfa class, NSAID class, tetracycline class, macrolide class, quinolone class, aminoglycoside class, opioid class, local anaesthetic ester / amide subclasses.
2. **Single-substance drug allergens**: penicillin V, amoxicillin, ceftriaxone, cotrimoxazole, sulfasalazine, aspirin, ibuprofen, paracetamol (rare), iodinated contrast, gadolinium contrast, latex (medical-grade), egg (vaccine excipient), gelatin (vaccine), thimerosal.
3. **Common environmental / food allergens**: peanut, tree nuts, shellfish, fish, milk, soy, wheat / gluten, dust mites, pollen (grass / tree / weed), bee/wasp venom, animal dander.

Out of v1: occupational allergens (latex, formaldehyde for non-medical exposure); rare hereditary contact allergens.

## Data model

`allergen_id, allergen_name, allergen_kind, rxnorm_concept_id, snomed_ct_concept, atc_codes_implicated, common_cross_reactions, severity_typical, common_manifestations, source_citations, code_system_version, code_accessed_date`

## Cross-cohort dependencies

- `atc_codes_implicated` → `drugs`
- referenced by Medic8 patient-banner UI + prescription CDS rules
- `snomed_ct_concept` → SNOMED CT free-set (no separate cohort)

## Hard exclusions (project-wide)

- Veterinary allergens
- Traditional/herbal allergens (out of project scope)

## Outputs

- `research/wave1-data.md` — allergen master table
- `research/wave1-findings.md` — sourcing methodology, cross-reactivity rationale, gap notes
- `analysis/gap-analysis.md`
- `analysis/critical-reasoning-pass.md`
- `opportunities/product-ideas.md`

## Source tiers

- **T1:** RxNorm allergen ingredient class definitions (NLM), WHO ATC class warnings, WHO EML safety annotations.
- **T2:** SNOMED CT International Edition free-set allergen concepts, food-allergy authority (FARE) lists.
- **T3:** Peer-reviewed allergy reviews — supporting role.
