# Cohort — drug-interactions

**Purpose:** seed `tbl_drug_interactions` with curated drug-drug interaction pairs to power Medic8's clinical decision support engine. Without this, the CDS rules referenced in design §6.5 cannot fire.

## Scope (v1)

Minimum 5,000 pairs covering:

- **All WHO EML class-level major contraindications.** Examples: warfarin × ciprofloxacin (major bleeding), warfarin × azoles (bleeding), MAOI × SSRI (serotonin syndrome), metformin × IV iodinated contrast (hold 48h), digoxin × amiodarone, ACEi × spironolactone × potassium, ART × rifampicin, ART × statins, ART × hormonal contraceptives.
- **EAC clinically common pairs** — HIV ART regimens × TB therapy, malaria therapy × cardiac drugs (artemether-lumefantrine × QT-prolongers), pregnancy contraindications.
- **Severity classification** — `MAJOR` (avoid), `MODERATE` (monitor), `MINOR` (informational).

Out of v1: full pharmacogenomic interactions; lab-drug interactions; food-drug interactions (deferred to a later cohort).

## Data model

`interaction_id, drug_a_atc, drug_b_atc, severity, mechanism, clinical_consequence, management, monitoring, evidence_level, source_citations, code_system_version, code_accessed_date`

## Cross-cohort dependencies

- `drug_a_atc`, `drug_b_atc` → `drugs` cohort (must reference existing ATC codes)
- referenced by Medic8 CDS engine (Phase B integration)

## Hard exclusions (project-wide)

- Veterinary, traditional/herbal interactions

## Sourcing strategy

Primary: open **DDInter 2.0** dataset (Knowledge Base of Drug-Drug Interactions). Curate a 5,000-pair subset filtered to drugs in our `drugs` cohort.

Layer 2: WHO EML 23rd edition class-level warnings.

Layer 3: peer-reviewed reviews of EAC-relevant interactions (ART × TB, ART × malaria, ART × hormonal contraception).

## Outputs

- `research/wave1-data.md` — interaction pairs table
- `research/wave1-findings.md` — methodology, sourcing decisions, severity-classification rules, gap notes
- `analysis/gap-analysis.md`
- `analysis/critical-reasoning-pass.md`
- `opportunities/product-ideas.md`

## Source tiers

- **T1:** DDInter 2.0, WHO EML class warnings, FDA/EMA black-box warnings.
- **T2:** Lexicomp / Stockley's Drug Interactions excerpts (cited only, not bulk-imported), WHO HIV/TB co-treatment guidelines.
- **T3:** Peer-reviewed pharmacology literature — supporting role only.
