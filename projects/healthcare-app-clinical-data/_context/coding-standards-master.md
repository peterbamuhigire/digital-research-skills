# Coding Standards — Master Reference

**Date:** 2026-05-03

This document is the canonical reference for the coding standards used in the healthcare-app-clinical-data corpus. It is reused (transcluded) into §1 of every cohort's Word report.

Every clinical concept in the corpus is keyed to an internationally recognised classification. The choice of standard per cohort follows international clinical-informatics practice.

---

## ICD-10 — International Statistical Classification of Diseases and Related Health Problems, 10th Revision

**Used for:** Conditions / diagnoses cohort.

**Maintainer:** World Health Organization (WHO).

**Edition cited:** ICD-10 2019 official version (the version most jurisdictions, including Uganda, currently report on through HMIS / IDSR; ICD-11 was published in 2022 but national rollout is uneven).

**Structure:**
- 22 chapters (Roman numerals I–XXII), each grouping a major class of disease (e.g., Chapter I "Certain infectious and parasitic diseases", Chapter II "Neoplasms", Chapter XV "Pregnancy, childbirth and the puerperium")
- Within each chapter, **blocks** of related categories (e.g., "B50–B64 Protozoal diseases")
- Within blocks, **three-character categories** (e.g., `B54` Unspecified malaria) and **four/five-character subcategories** (`B50.0` Plasmodium falciparum malaria with cerebral complications)

**How we use it:** Every condition row has `icd10_code`, `icd10_title` (WHO official title), `icd10_chapter`, `icd10_block` columns. Categorisation in the report uses ICD-10 chapter as the primary grouping.

**Reference URL pattern:** `https://icd.who.int/browse10/2019/en` for the official WHO browser.

---

## ATC — Anatomical Therapeutic Chemical Classification

**Used for:** Drugs cohort.

**Maintainer:** WHO Collaborating Centre for Drug Statistics Methodology (Oslo).

**Edition cited:** Current ATC/DDD index (`atcddd.fhi.no`).

**Structure:** A 5-level hierarchy:
- **Level 1:** Anatomical main group, single letter (e.g., `J` Antiinfectives for systemic use)
- **Level 2:** Therapeutic subgroup, two digits (e.g., `J01` Antibacterials for systemic use)
- **Level 3:** Pharmacological subgroup, one letter (e.g., `J01C` Beta-lactam antibacterials, penicillins)
- **Level 4:** Chemical subgroup, one letter (e.g., `J01CA` Penicillins with extended spectrum)
- **Level 5:** Chemical substance, two digits (e.g., `J01CA04` amoxicillin)

**How we use it:** Every drug row has the full hierarchy as separate columns plus the 5-level code itself. Categorisation in the report uses ATC level 1 as the primary grouping with level 2 as secondary.

**Pairs naturally with:** WHO Model List of Essential Medicines (each EML entry maps to an ATC code) and Uganda EMHSLU.

---

## LOINC — Logical Observation Identifiers Names and Codes

**Used for:** Lab tests cohort (and as the primary code for imaging studies; see RadLex below).

**Maintainer:** Regenstrief Institute (loinc.org).

**Edition cited:** Current LOINC release.

**Structure:** Each LOINC code is a fixed numeric identifier (e.g., `718-7` Hemoglobin [Mass/volume] in Blood). Six axes describe the test:
- **Component** — the analyte (e.g., Hemoglobin)
- **Property** — what is measured (mass concentration, substance concentration, presence/absence, ratio)
- **Time** — point-in-time vs. timed collection
- **System** — specimen (Blood, Serum, Urine, CSF, etc.)
- **Scale** — quantitative, ordinal, nominal, narrative
- **Method** — methodology where it changes the result (rarely populated)

**Discipline grouping** is not a LOINC field; we add it (Haematology / Clinical Chemistry / Microbiology / Serology / Endocrinology / Histopathology / Molecular) as a more clinically intuitive primary categorisation in the report.

**How we use it:** `loinc_code`, `loinc_long_common_name`, `loinc_class`, plus our `discipline_grouping` for report categorisation.

---

## RadLex — Radiology Lexicon (and the RadLex Playbook)

**Used for:** Imaging cohort, alongside LOINC.

**Maintainer:** Radiological Society of North America (RSNA).

**The RadLex Playbook** is a controlled set of radiology procedure names with unique IDs (e.g., `RPID2467` "CT Head without IV Contrast"). It pairs with LOINC for cross-walk; many RadLex Playbook items have an associated LOINC code.

**How we use it:** Each imaging row carries both `loinc_code` and `radlex_id` where available. `report_template_fields` and `key_measurements` columns describe the structured report a radiologist completes (e.g., for Chest XR PA: lungs, pleura, cardiac silhouette, mediastinum, hila, bones, soft tissue, lines/tubes, impression). Categorisation in the report uses **modality** (XR / US / CT / MRI / Fluoro / Mammo / DEXA / Nuc Med) as the primary axis with **body region** as secondary.

---

## ICD-10-PCS — ICD-10 Procedure Coding System

**Used for:** Non-dental procedures cohort (primary code).

**Maintainer:** US Centers for Medicare and Medicaid Services (CMS) — note the standard is US-origin. WHO's international successor is ICHI (see below) but ICHI is still in beta release.

**Structure:** 7-character alphanumeric code where each character position has a defined meaning depending on the **section** (the first character):
- Section 0 (Medical and Surgical): char 1 = section, char 2 = body system, char 3 = root operation, char 4 = body part, char 5 = approach, char 6 = device, char 7 = qualifier

**Example:** `0DTJ4ZZ` = Resection (root op) of Appendix (body part) via Percutaneous Endoscopic Approach.

**How we use it:** `icd10_pcs_code` for non-dental rows. Categorisation in the report uses our `category` field (OB-Gyn / General Surgery / etc.) which does not directly mirror PCS section because PCS sections are organised by approach-type rather than specialty.

**Methodology note (in report):** ICD-10-PCS is US-centric; we document the choice and note that WHO ICHI is the eventual international standard. Each row also carries a `who_chi_code` secondary field where ICHI mapping exists.

---

## CDT — Code on Dental Procedures and Nomenclature

**Used for:** Dental procedures (subset of procedures cohort).

**Maintainer:** American Dental Association (ADA). **Proprietary / licensed** — codes are reproduced under fair-use for reference and the app team will need an ADA license for commercial rollout. This licensing constraint is flagged in the procedures report.

**Edition cited:** CDT 2024.

**Structure:** Five-character codes starting with `D` followed by four digits, organised into 12 categories (D0xxx Diagnostic, D1xxx Preventive, D2xxx Restorative, etc., through D9xxx Adjunctive General Services).

**How we use it:** `cdt_code` field on dental rows; non-dental rows leave it blank. Dental categorisation in the report uses CDT category as the primary axis.

---

## ICHI — International Classification of Health Interventions (WHO)

**Used for:** Procedures cohort, **secondary** code only.

**Status:** WHO is developing ICHI as the international successor to ICD-10-PCS. Currently in beta release. Not all procedures have stable ICHI codes yet.

**How we use it:** `who_chi_code` column populated where a stable ICHI code exists; otherwise blank. We retain it because the app may need to migrate in future when ICHI matures.

---

## Other clinical-context codes used as columns

These are not the primary keying standard but appear in the data model:

- **WHO EML / EMLc section** (drugs): the section number from the WHO Model List (e.g., "6.2.1 Beta lactam medicines")
- **Uganda EMHSLU V/E/N classification** (drugs): Vital / Essential / Necessary
- **Uganda HC level codes** (drugs, labs, imaging, procedures): HC II, HC III, HC IV, GH, RRH, NRH (the Uganda MoH service-delivery tiers)
- **Uganda IDSR notifiable list** (conditions): the list of priority diseases reported through the Integrated Disease Surveillance and Response system
- **Uganda Clinical Guidelines (UCG) section** (conditions, procedures): cross-reference to the Ministry-published clinical guideline section number

These are derived, not primary keys, but enable the app to filter clinically.

---

## Why these standards (rationale for non-clinicians)

- **ICD-10** is what Uganda HMIS reports on, what insurance coding uses regionally, and what SNOMED-CT and ICD-11 cross-walk to. Future-proof.
- **ATC** is the WHO-maintained drug classification; pairs with the EML and the Uganda EMHSLU which are themselves ATC-organised.
- **LOINC** is the de facto international lab standard; FHIR (Fast Healthcare Interoperability Resources) — the leading health-data exchange format — uses LOINC natively. If the app ever exchanges data with another system, LOINC is the lingua franca.
- **RadLex** is RSNA-maintained and used by most modern PACS systems and structured radiology reporting platforms.
- **ICD-10-PCS** is the most complete public procedural code set; ICHI is the future but not yet stable.
- **CDT** is the dental-coding standard used by virtually every dental practice management system globally.

---

## Maintenance

When standards update (e.g., LOINC quarterly releases, CDT annually), the corpus does not auto-update. The app team should plan a yearly refresh of this corpus to stay current. Each cohort's `methodology` section in its Word report records the exact edition cited.
