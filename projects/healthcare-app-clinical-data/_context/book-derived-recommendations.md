# Book-Derived Recommendations

**Date:** 2026-05-03
**Sources studied:**

- Coiera, *Guide to Health Informatics*, 3rd edition
- *Healthcare Information Systems — Progress, Challenges and Future Directions* (cited as **HIS-Progress**)
- Tan et al., *Healthcare Information Systems and Informatics — Research and Practices* (HIS-RP)
- *Health Informatics: A Systems Perspective*, 2nd edition (Systems Perspective 2e)
- Volpe (ed.), *Health Informatics: Multidisciplinary Approaches* (Multidisciplinary)

The orchestrator commissioned a research agent to extract project-specific recommendations from these texts. Findings below; every recommendation carries a book + chapter citation. **All Wave 1 sub-agent briefs must reference this document.**

---

## 1. Standards-choice critique (per cohort)

### Conditions — ICD-10 has named limits

Coiera 3e ch. 23 is explicit: ICD's "goal is to allow morbidity and mortality data… to be systematically collected and statistically analyzed. **It is not intended, nor is it suitable, for indexing distinct clinical entities** (Gersenovic 1995)." For an app aimed at clinical reference use, ICD-10 is the *reporting* axis, not the *clinical-concept* axis. Coiera ch. 23 names SNOMED CT (post-coordinated, compositional) as the appropriate clinical-concept terminology. Systems Perspective 2e ch. 12 (Buntrock) makes the post-coordination point with a worked SNOMED example.

**Action:**
- ADD `snomed_ct_concept_id` and `snomed_ct_description_id` columns to Conditions cohort (Coiera 3e Fig. 23.3)
- ADD `icd11_candidate_code` column where mapping is straightforward; flag where it is not
- ADD `granularity_caveat` boolean — TRUE where ICD-10 collapses two clinically distinct entities

### Drugs — ATC alone is insufficient

Coiera ch. 23 pairs ATC with **DDD (Defined Daily Dose)**; without DDD, ATC strings are dosage-blind. Multidisciplinary ch. 6 (Medication Errors) and the index entry on RxNorm note that **RxNorm is the operational identifier for e-prescribing/CPOE interoperability**. Volpe ch. 6 also describes the NDC labeler/product/package three-segment structure relevant to long-term app interoperability.

**Action:**
- ADD `atc_ddd_value` and `atc_ddd_unit` columns
- ADD `rxnorm_rxcui` (where mappable) — bridge column for CDSS interoperability
- ADD `lasa_tallman_form` column citing ISMP tall-man list (Volpe ch. 6)
- DROP free-text "interactions" column in favour of structured DDI sub-table (Volpe ch. 6 — DDI is rule-engine input, not narrative)

### Lab — LOINC is correct but partial

Coiera ch. 23: "LOINC provides a set of names and identification codes for identifying laboratory and clinical test results"; "SNOMED CT also integrates LOINC to enhance its coverage of laboratory test nomenclature." HIS-Progress ch. 3 enumerates the **PHII 19 core LIS functions** (specimen tracking, TAT, critical-value rules, reference-range comparison, delta checks). LOINC names the *observation*; the structural columns must be modelled separately.

**Action:**
- KEEP LOINC primary
- ADD `snomed_ct_concept` column (Coiera ch. 23 LOINC↔SNOMED integration)
- ENSURE all 19 PHII LIS columns covered: specimen type/container/volume/min, TAT routine, TAT stat, critical low/high, interferences, delta-check threshold, reference-range population qualifier

### Imaging — LOINC + RadLex are the pair, but DICOM SR drives the report template

Coiera ch. 23 describes RadLex as "a radiology specific terminological system." HIS-Progress ch. 4 documents DICOM Part 20 ("Imaging report using HL7 CDA") and Part 3 ("Information Object Definitions" including structured reports). LOINC carries study name; RadLex carries anatomy/finding lexicon; **DICOM SR / CDA template drives the report.**

**Action:**
- ADD `dicom_sr_template_ref` column
- ADD `radlex_anatomy_id` and `radlex_finding_id` columns (separate from generic `radlex_id`)
- Convert `key_measurements` from prose to structured array: `[{name, loinc_id, units}, ...]`

### Procedures — ICHI should be primary, ICD-10-PCS secondary

Coiera ch. 23 cites Averill et al. 2001 on ICD-10-PCS as a US-developed extension and lists ICHI separately as the **WHO international interventions classification**. Uganda's geography makes the US-anchored PCS the wrong primary.

**Action:**
- **SWAP primary/secondary** — ICHI primary, ICD-10-PCS secondary
- KEEP CDT for dental (no change)

---

## 2. Universal additions (every cohort)

Coiera ch. 23 q.5 (terminology maintenance cost dominates lifetime cost) and Systems Perspective 2e ch. 11 (Brown — LMIC HIT viability constrained by infrastructure, not technology) jointly require:

- `code_system_version` — the version of the code system the row was sourced against (e.g., LOINC 2.78, ICD-10 2019, ATC 2024)
- `level_of_care_min` — HC II / HC III / HC IV / GH / RRH / NRH (we already have this on most cohorts; add to Conditions and Drugs explicitly)
- `cadre_min` — minimum cadre that performs/orders the item (CHW / nurse / midwife / clinical officer / medical officer / specialist / dentist)
- `code_accessed_date` — when the row was sourced/verified

---

## 3. Uganda / LMIC-specific additions

Systems Perspective 2e ch. 11 (Brown, "Global Health Systems Informatics"): "the pace and breadth of applying clinical decision support systems globally are **not limited by the speed and power of HIT but by the economics, politics, culture, and information infrastructure** of countries." Encode the constraint in the data model:

- `connectivity_tolerance` flag — does this item require online lookup or can it run offline? Coiera ch. 21 (Lester et al. 2010 — Kenyan WelTel) is the LMIC m-health citation
- `paper_form_equivalent` — the paper-form name/code this item maps to in Uganda HMIS forms (HMIS 105/108 etc.). Coiera ch. 13 box 13.4 names "hybrid paper-computer transitions" as a primary safety hazard
- For Drugs: `eml_tier` (Vital/Essential/Necessary) — HIS-Progress ch. 5 §5.3 sets the 95% ICD-10 coverage benchmark for drug knowledge bases
- For Conditions, Drugs, Procedures: `coding_rule` field — Systems Perspective 2e ch. 12 shows ICD-10-CM I21 STEMI/NSTEMI rules require additional codes (tobacco exposure, etc.)

---

## 4. Pitfalls to avoid

| Pitfall | Citation | Mitigation |
|---|---|---|
| Coding-system version drift | HIS-Progress ch. 4 (DICOM standards-update process); Coiera ch. 23 q.5 | Every code column gets a `code_system_version` sibling; Phase 2 QA verifies dates ≤12 months stale |
| "Same concept, different code" in different systems | Coiera ch. 23 §"Comparing coding systems is not easy" | Phase 5 reports must list per-cohort count of items where ICD-10↔SNOMED↔ICHI mappings are not one-to-one |
| Pediatric CPOE mortality (Pittsburgh/Seattle PICU) — adult-anchored ranges | Coiera ch. 13 box 13.4 | Lab cohort: paediatric reference ranges as separate rows, not asterisks on adult rows |
| Alert fatigue / over-coding | Volpe ch. 6 (1.1M alerts/month, 20.3% overridden) | Drugs cohort: do not seed every theoretical DDI; apply "high-risk" filter; tier severity |
| EHR generic care-plan gap for specialty populations | Systems Perspective 2e ch. 7 | Mark every Procedure and Drug item where paediatric-specific dose/template differs |
| Data-quality tail | HIS-Progress ch. 2 §2.3.3.5 (logical checks: completeness, range, cross-field) | Phase 2 QA must run logical checks per HIS-Progress §2.3.3 |

---

## 5. FHIR alignment (resource mapping for the app team)

| Cohort | FHIR resource | Notes |
|---|---|---|
| Conditions | `Condition.code` (CodeableConcept with multiple codings — ICD-10 + SNOMED + ICD-11 candidate) | Multi-standard column shape we already use maps cleanly |
| Drugs | `Medication.code` = ATC + RxNorm; `Medication.ingredient` = INN; brands = `MedicationKnowledge.packaging` | RxNorm bridge is the FHIR-friendly anchor |
| Lab | `Observation.referenceRange.appliesTo` | Population qualifier has a direct FHIR slot — Systems Perspective 2e ch. 13 calls this **late binding** |
| Imaging | `ImagingStudy` + `Observation` (per measurement) + `DiagnosticReport` (narrative) | Multi-resource decomposition; structure measurements as Observations |
| Procedures | `Procedure.code` + `Procedure.performer.function` (cadre) | `cadre_min` column maps directly |

---

## 6. Sub-agent briefing — required clauses to add

Insert these clauses verbatim into every Wave 1 sub-agent brief, in addition to the hard-constraint anti-hallucination clause:

1. *"For every code, capture the code-system version and access date. Coiera 3e ch. 23 establishes maintenance cost dominates terminology lifetime — undated codes will be stripped in QA."*
2. *"Where ICD-10 collapses two clinically distinct entities, flag with a `granularity_caveat` and quote Coiera 3e ch. 23: 'ICD is not intended, nor is it suitable, for indexing distinct clinical entities.'"*
3. *"Drug rows must carry ATC + DDD per Coiera 3e ch. 23 (WHO Drug Dictionary classification family) and an RxNorm RXCUI bridge per Volpe ed. ch. 6."*
4. *"Lab rows must follow PHII's 19 LIS core functions per HIS-Progress ch. 3 — specimen, TAT, critical value, delta check are mandatory columns."*
5. *"Procedures must carry an ICHI code as the WHO-international primary; ICD-10-PCS is secondary (US-anchored), per Coiera 3e ch. 23."*
6. *"Mark paediatric-specific reference ranges, doses, and templates as separate rows. Systems Perspective 2e ch. 7 names the generic-care-plan gap as a known EHR failure mode."*
7. *"Encode level-of-care minimum and minimum cadre on every applicable row. Systems Perspective 2e ch. 11 (Brown) ties LMIC HIT viability to infrastructure, not technology."*

---

## 7. Top 5 changes to make before Phase 1 dispatch

| # | Change | Rationale |
|---|---|---|
| 1 | Add `snomed_ct_concept_id` to Conditions and `rxnorm_rxcui` to Drugs as bridge columns | Coiera 3e ch. 23 makes ICD-10 unsuitable as a clinical-concept key; FHIR Condition/Medication require these bridges |
| 2 | Promote ICHI to primary on Procedures, ICD-10-PCS to secondary | Coiera 3e ch. 23 — ICHI is the WHO international interventions standard; Uganda's geography makes the US-anchored PCS the wrong primary |
| 3 | Replace single "reference range" column on Lab with `population`-keyed row variants and add the PHII-19 columns (specimen, TAT, critical value, interferences, delta) | HIS-Progress ch. 3; Systems Perspective 2e ch. 13 |
| 4 | Add `code_system_version`, `level_of_care_min`, `cadre_min` columns to every cohort | Coiera 3e ch. 23 + Systems Perspective 2e ch. 11 — terminology maintenance discipline + LMIC defensibility |
| 5 | Carve LASA/tall-man, ATC-DDD, and structured DDI out of free text in the Drugs cohort | Volpe ed. ch. 6 — these are first-class CDSS triggers; embedding them in narrative kills downstream Five Rights use |

---

## 8. Coverage note

Extraction succeeded for all five EPUBs. HIS-RP (Tan et al.) had thinnest direct yield on terminology design; its strongest contribution was on m-health/LMIC mobile context (ch. 2), absorbed into §3.
