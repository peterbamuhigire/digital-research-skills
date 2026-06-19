# Standards and Bodies — full inventory

**Date:** 2026-05-03

This document is the canonical reference for **every standard cited anywhere in the corpus** and **the body that maintains/enforces each**. It must be transcluded (or summarised at depth) into §1 of every Word `.docx` report generated in Phase 5. The user's instruction (2026-05-03) is verbatim: *"the word documents/reports must clearly explain the standards being used and the relevant bodies that enforce them."*

For each standard the report must state, at minimum:
- **What it is** (one sentence)
- **Which body maintains it** (with link)
- **Which body enforces it / where it has regulatory force** (if any — distinct from the maintainer)
- **Edition cited in this corpus** (with date)
- **Why we use it for this cohort** (one sentence — clinical-informatics rationale)
- **Known limits** (one sentence — e.g., ICD-10 is reporting-axis not clinical-concept axis)

---

## 1. Diagnosis-coding standards

### ICD-10 — International Statistical Classification of Diseases, 10th Revision
- **What:** WHO's primary morbidity / mortality reporting code system; 22 chapters, ~14,400 categories.
- **Maintained by:** World Health Organization (WHO), Geneva — `https://icd.who.int/browse10/2019/en`
- **Enforced where:** Mandatory reporting axis for Uganda HMIS / IDSR; Kenya MoH; Tanzania STG. Insurance and morbidity reporting in most jurisdictions.
- **Edition cited:** WHO ICD-10 2019 official version (ICD-11 published 2022 but national rollout uneven).
- **Why for Conditions cohort:** Single most widely-implemented diagnosis classification globally; aligns with Uganda HMIS reporting.
- **Known limits:** "ICD is not intended, nor is it suitable, for indexing distinct clinical entities" (Coiera 3e ch. 23, citing Gersenovic 1995). Pair with SNOMED CT for clinical-concept work.

### ICD-11 — International Classification of Diseases, 11th Revision
- **What:** WHO's successor to ICD-10; ontology-based, post-coordinated, ~85,000 entities.
- **Maintained by:** WHO — `https://icd.who.int/`
- **Enforced where:** Adoption in progress globally; not yet primary in Uganda / Kenya / Tanzania.
- **Edition cited:** ICD-11 (current MMS release).
- **Why for Conditions cohort:** Future-proofing — every condition row carries `icd11_candidate_code` where mapping is straightforward.
- **Known limits:** Mapping from ICD-10 is not 1:1; some collapsed categories explode in ICD-11.

### SNOMED CT — Systematized Nomenclature of Medicine — Clinical Terms
- **What:** Most comprehensive clinical terminology; post-coordinated, compositional; ~350,000 active concepts.
- **Maintained by:** SNOMED International (formerly IHTSDO), Copenhagen — `https://www.snomed.org/`
- **Enforced where:** National licensing required in member countries (UK NHS Digital, US ONC HIT certification, etc.). Uganda not currently a SNOMED International member; use is "reference only" until membership.
- **Edition cited:** Current International Edition.
- **Why for Conditions cohort:** Coiera 3e ch. 23 — clinical-concept axis distinct from ICD-10's reporting axis. FHIR `Condition.code` typically multi-coded with both.
- **Known limits:** Licensing — non-member countries have restricted use rights.

### Uganda IDSR notifiable list
- **What:** Priority diseases reported through the Integrated Disease Surveillance and Response system; ~30 conditions on weekly + immediate notification list.
- **Maintained by:** Uganda Ministry of Health Department of Surveillance
- **Enforced where:** Public Health Act regulations — clinicians legally required to notify within stipulated timeframes.
- **Edition cited:** Uganda National Technical Guidelines for IDSR (cached in `_context/sources-cache/uganda-idsr.md`).
- **Why for Conditions cohort:** Drives the `notifiable_uganda` column; the app must trigger notification workflow when these conditions are selected.
- **Known limits:** List updated periodically; corpus reflects edition cited.

---

## 2. Drug-coding standards

### ATC — Anatomical Therapeutic Chemical Classification
- **What:** WHO's drug classification; 5-level hierarchy (anatomical → therapeutic → pharmacological → chemical subgroup → chemical substance).
- **Maintained by:** WHO Collaborating Centre for Drug Statistics Methodology, Oslo — `https://www.atcddd.fhi.no/atc_ddd_index/`
- **Enforced where:** WHO drug-utilisation studies; widely adopted by national formularies including Uganda EMHSLU.
- **Edition cited:** Current WHO ATC/DDD index.
- **Why for Drugs cohort:** Single most used drug-classification system internationally; aligns with EMHSLU and WHO EML structure.
- **Known limits:** Doesn't carry brand information or formulation specifics — bridged via RxNorm.

### DDD — Defined Daily Dose
- **What:** Assumed average maintenance dose per day for a drug used for its main indication in adults; the unit of drug consumption analysis.
- **Maintained by:** WHO Collaborating Centre for Drug Statistics Methodology, Oslo (same body as ATC; published together).
- **Enforced where:** Drug-utilisation reporting in WHO and national systems.
- **Edition cited:** Current WHO ATC/DDD assignments.
- **Why for Drugs cohort:** Coiera 3e ch. 23 — without DDD, ATC strings are dosage-blind. Required for any consumption analytics.
- **Known limits:** Many topical / parenteral drugs have no defined DDD; some new agents lack stable assignments.

### RxNorm
- **What:** US National Library of Medicine's normalised medication terminology; provides RXCUI as a unique drug identifier bridging ATC, NDC, and brand names.
- **Maintained by:** US National Library of Medicine (NLM) — `https://rxnav.nlm.nih.gov/REST/`
- **Enforced where:** US Meaningful Use / ONC HIT certification; commonly used internationally as the e-prescribing / CPOE bridge.
- **Edition cited:** Current RxNorm release (queried via RxNav API).
- **Why for Drugs cohort:** Volpe ed. ch. 6 — operational identifier for e-prescribing/CPOE interoperability. FHIR `Medication.code` typically uses RxNorm.
- **Known limits:** US-anchored; some non-US INNs/brands not in RxNorm.

### Uganda EMHSLU — Essential Medicines and Health Supplies List of Uganda
- **What:** Uganda Ministry of Health's official formulary; lists drugs and health supplies by V/E/N tier (Vital / Essential / Necessary) and HC level of care.
- **Maintained by:** Uganda Ministry of Health, Pharmacy Department.
- **Enforced where:** Public-sector procurement (NMS) follows EMHSLU. Mandatory reference for clinicians prescribing in Uganda public facilities.
- **Edition cited:** EMHSLU 2023 (cached in `_context/sources-cache/emhslu-uganda.md`).
- **Why for Drugs and Consumables cohorts:** Single Uganda-authoritative source for what is procurable / dispensable at each HC tier.
- **Known limits:** Updated periodically; corpus reflects edition cited. Some brand-name details out of scope.

### WHO Model List of Essential Medicines (EML / EMLc)
- **What:** WHO's recommended essential drugs list — adult EML 23rd ed (2023) and Children's EMLc 9th ed.
- **Maintained by:** World Health Organization, Selection of Essential Medicines Expert Committee.
- **Enforced where:** Reference for national EMLs globally; NOT directly enforced by WHO but shapes most LMIC formularies.
- **Edition cited:** EML 23 (2023); EMLc 9.
- **Why for Drugs cohort:** The international comparator for Uganda EMHSLU.
- **Known limits:** Recommendation, not regulation; national lists deviate.

### Uganda National Drug Authority (NDA)
- **What:** Uganda's medicines regulator; maintains the register of products approved for marketing.
- **Maintained by:** National Drug Authority (statutory body under Ministry of Health) — `https://www.nda.or.ug/` and search at `https://search.nda.or.ug`
- **Enforced where:** **Regulatory** — registration is required for legal sale in Uganda. Equivalent bodies: Kenya Pharmacy and Poisons Board (PPB); Tanzania Medicines and Medical Devices Authority (TMDA).
- **Edition cited:** NDA register July 2024 (per agent reports).
- **Why for Drugs cohort:** Drives the `registered_uganda_nda` column; the app must show only locally-approved brands.
- **Known limits:** Register access is form-based / occasional bulk PDF — not always machine-friendly.

### ISMP Tall-Man / LASA list
- **What:** Institute for Safe Medication Practices recommended tall-man rendering of Look-Alike / Sound-Alike drug names (e.g., "predniSONE" vs "prednisoLONE").
- **Maintained by:** ISMP, Pennsylvania — `https://www.ismp.org/recommendations/tall-man-letters-list`
- **Enforced where:** Adopted by The Joint Commission (US accreditation) and many LMIC patient-safety programmes.
- **Edition cited:** Current ISMP list.
- **Why for Drugs cohort:** Volpe ed. ch. 6 — tall-man rendering reduces medication errors at prescribing/dispensing/administration. Drives `lasa_tallman_form` column.
- **Known limits:** Recommendation, not regulation; voluntary adoption.

---

## 3. Lab-coding standards

### LOINC — Logical Observation Identifiers Names and Codes
- **What:** Universal coding system for lab and clinical observations; ~109,000 active terms; 6-axis structure (Component / Property / Time / System / Scale / Method).
- **Maintained by:** Regenstrief Institute, Indianapolis — `https://loinc.org/`
- **Enforced where:** US ONC HIT certification (mandatory for lab orders); EU regulations increasingly. Free for international use.
- **Edition cited:** LOINC 2.78 / current release as of 2026-05-03.
- **Why for Lab and Imaging cohorts:** De facto international lab standard; FHIR `Observation.code` native.
- **Known limits:** Six-axis specificity sometimes too granular; Regenstrief publishes mapping guides.

### PHII LIS Core Functions (the "PHII 19")
- **What:** Public Health Informatics Institute's specification of 19 core LIS functions (specimen tracking, TAT, critical values, delta checks, reference ranges, etc.).
- **Maintained by:** Public Health Informatics Institute (US) — referenced in HIS-Progress ch. 3.
- **Enforced where:** Reference framework, not a regulatory standard.
- **Why for Lab cohort:** Drives the column structure of `lab-tests/research/wave*-data.md`. Specimen / TAT / critical / delta are all mandatory columns.

### Tietz Textbook of Clinical Chemistry and Molecular Diagnostics
- **What:** Reference textbook for clinical-chemistry analyte ranges, methodologies, interferences.
- **Maintained by:** Elsevier (commercial publisher); content authored by Burtis, Bruns et al.
- **Enforced where:** Not regulatory; widely cited in lab manuals globally.
- **Edition cited:** Latest available (referenced T3 fallback for Western reference ranges).
- **Why for Lab cohort:** Fallback when no East African reference range exists. Western fallbacks are explicitly flagged `[Western fallback — local validation pending]`.

---

## 4. Imaging-coding standards

### LOINC for Imaging
- See §3 LOINC. LOINC carries the imaging study name (e.g., "Chest XR PA").

### RadLex and the RadLex Playbook
- **What:** RadLex is RSNA's controlled radiology terminology (~70,000 terms covering anatomy, findings, modalities). The RadLex Playbook adds RPID procedure codes.
- **Maintained by:** Radiological Society of North America (RSNA) — `https://www.rsna.org/practice-tools/data-tools-and-standards/radlex-radiology-lexicon`
- **Enforced where:** Adopted by most modern PACS systems and structured radiology reporting platforms; reference standard for interoperability.
- **Edition cited:** Current RadLex / Playbook release.
- **Why for Imaging cohort:** Anatomy and finding lexicon distinct from LOINC procedure name. Drives `radlex_id`, `radlex_anatomy_id`, `radlex_finding_id` columns.
- **Known limits:** Free use but the Playbook CSV requires a free RSNA / LOINC account to download.

### DICOM — Digital Imaging and Communications in Medicine
- **What:** International standard for medical image format, transmission, and structured reporting (SR templates / TIDs).
- **Maintained by:** DICOM Standards Committee under National Electrical Manufacturers Association (NEMA) — `https://dicom.nema.org/`
- **Enforced where:** ISO 12052 — recognised as an international standard. Effectively mandatory for medical imaging interoperability.
- **Edition cited:** Current DICOM (PS3.16 for SR — `https://dicom.nema.org/medical/dicom/current/output/html/part16.html`).
- **Why for Imaging cohort:** TIDs (Template IDs) drive the structured-report shape — e.g., TID 5200 (Cardiac Echo), TID 1500 (Measurement Report). FHIR `ImagingStudy` integrates with DICOM.
- **Known limits:** Standard is very large; not all modalities have stable SR templates.

### ACR Practice Parameters / RCR iRefer
- **What:** American College of Radiology practice parameters / Royal College of Radiologists referral guidelines for imaging.
- **Maintained by:** ACR (US) and RCR (UK).
- **Enforced where:** ACR — accreditation reference in US. RCR iRefer — recommended in UK NHS and many Commonwealth countries including Uganda.
- **Why for Imaging cohort:** Source of `indication_top3` and `preparation_required` columns where Uganda-specific guidance is absent.

---

## 5. Procedure-coding standards

### ICHI — International Classification of Health Interventions
- **What:** WHO's emerging international interventions classification (currently in beta release).
- **Maintained by:** World Health Organization — `https://icd.who.int/dev11/l-ichi/en`
- **Enforced where:** Recommended by WHO; not yet mandatory in Uganda / Kenya / Tanzania (still beta).
- **Edition cited:** ICHI beta (2026 access).
- **Why for Procedures cohort (PRIMARY per Coiera 3e ch. 23):** WHO-international, geographically agnostic; future-proofs procedure data for Uganda which is not US-anchored.
- **Known limits:** Many procedures still lack stable codes — `[GAP — ICHI not yet stable]` is expected.

### ICD-10-PCS — ICD-10 Procedure Coding System
- **What:** US-developed extension for inpatient procedure coding; 7-character alphanumeric, multi-axial.
- **Maintained by:** US Centers for Medicare and Medicaid Services (CMS) — `https://www.cms.gov/medicare/icd-10/2024-icd-10-pcs`
- **Enforced where:** Mandatory for US Medicare / Medicaid reimbursement. Not enforced outside US.
- **Edition cited:** ICD-10-PCS 2024.
- **Why for Procedures cohort (SECONDARY per Coiera 3e ch. 23):** Most complete public procedural code set. We carry it as a bridge until ICHI matures.
- **Known limits:** US-anchored; some procedure conventions (e.g., approach naming) reflect US practice.

### CDT — Code on Dental Procedures and Nomenclature
- **What:** ADA's dental procedure code set; ~750 codes (D0xxx–D9xxx categories).
- **Maintained by:** American Dental Association (ADA) — `https://www.ada.org/publications/cdt`
- **Enforced where:** Mandatory for US dental insurance reimbursement; **proprietary / licensed**.
- **Edition cited:** CDT 2024.
- **Why for Procedures cohort (DENTAL only):** Single dental procedure standard used by virtually every dental practice management system globally.
- **Known limits:** **ADA-licensed.** Codes used in this corpus under fair-use for reference. **Commercial deployment of the app exposing CDT codes to end-users requires an ADA license.** This constraint is flagged in `_context/exclusions.md` and must appear in §5 (App-implementation notes) of the Procedures Word report.

### WHO Surgical Care at the District Hospital + Maurice King's Primary Surgery
- **What:** Reference manuals for surgical practice in district-hospital and primary-care settings, especially sub-Saharan Africa.
- **Maintained by:** WHO (district hospital manual) and TALC (Maurice King's, open access at talcuk.org).
- **Why for Procedures cohort:** Authoritative T2 source for level-of-care assignments and procedure-specific consumables.

---

## 6. Consumables / device standards

### GMDN — Global Medical Device Nomenclature
- **What:** Standardised system of nomenclature for medical devices; ~10,000 generic device groups.
- **Maintained by:** GMDN Agency, UK — `https://www.gmdnagency.org/`
- **Enforced where:** Required for medical-device registration in EU (under MDR), Australia (TGA), and many other regulators. Uganda not yet mandating GMDN but increasingly used in tenders.
- **Why for Consumables cohort:** Provides a stable identifier for device-type categorisation.
- **Known limits:** Full GMDN database is paywalled; agency provides limited free access.

### UNSPSC — UN Standard Products and Services Code
- **What:** UN-managed product/service classification; widely used in procurement systems.
- **Maintained by:** GS1 US (under license from UNDP) — `https://www.unspsc.org/`
- **Enforced where:** Procurement standards — adopted by World Bank, USAID, and many UN agencies. Used in Uganda Ministry of Health procurement reporting.
- **Why for Consumables cohort:** Enables cross-walking to procurement / supply-chain systems.

### UMDNS — Universal Medical Device Nomenclature System
- **What:** ECRI Institute's earlier device nomenclature; ~10,000 terms.
- **Maintained by:** ECRI Institute — `https://www.ecri.org/`
- **Enforced where:** WHO Health Technology series uses UMDNS; some LMIC procurement systems.
- **Why for Consumables cohort:** WHO-aligned alternative to GMDN where GMDN is paywalled.
- **Known limits:** Less actively maintained than GMDN; slowly being superseded.

### Uganda HMIS forms
- **What:** Uganda's Health Management Information System paper forms (105 facility OPD, 108 hospital, 098 lab, 033b weekly notification, 071 referral, 107 annual report, etc.).
- **Maintained by:** Uganda Ministry of Health Resource Centre.
- **Enforced where:** Mandatory facility-level reporting at all public-sector tiers (HC II → NRH).
- **Edition cited:** Current HMIS forms (HMIS Form 107 cached in `_context/sources-cache/uganda-hmis-107.md`).
- **Why for all cohorts:** Drives the `paper_form_equivalent` column. The app should be able to emit data in HMIS format for facility statisticians.

---

## 7. Cross-cutting standards (data and interoperability)

### HL7 FHIR — Fast Healthcare Interoperability Resources
- **What:** International standard for health-data exchange; resource-based (Patient, Condition, Medication, Observation, Procedure, etc.).
- **Maintained by:** Health Level Seven International — `https://www.hl7.org/fhir/`
- **Enforced where:** US ONC HIT mandates FHIR R4 since 2022; UK NHS Digital, EU member states, growing adoption in LMIC HIT systems.
- **Edition cited:** R4 / R4B / R5 as appropriate.
- **Why for the corpus:** Every cohort's column model is intended to map onto FHIR resources (`Condition.code`, `Medication.code`, `Observation`, `ImagingStudy`, `Procedure`, `Device`/`SupplyDelivery`). See `_context/book-derived-recommendations.md` §5.
- **Known limits:** Implementation guides (IGs) vary by jurisdiction.

### ISO and ISO/IEC standards relevant
- **ISO 12052** — Medical informatics — DICOM (formal recognition of DICOM as an ISO standard).
- **ISO 27799** — Health informatics — Information security in healthcare (for app security planning).
- **Maintained by:** International Organization for Standardization (Geneva) — `https://www.iso.org/`
- **Why for the app:** Security and interoperability compliance reference.

### IHE (Integrating the Healthcare Enterprise) profiles
- **What:** IHE profiles describe how to use existing standards (HL7, DICOM, LOINC) for specific clinical workflows.
- **Maintained by:** IHE International — `https://www.ihe.net/`
- **Why for the corpus:** Imaging report exchange (e.g., IHE PIR profile), order-entry workflows.

---

## Phase 5 Word-report requirement (drives section §1 of every cohort report)

For every cohort `.docx` report assembled in Phase 5, **§1 — Coding Standards** must:

1. **List the primary code** the cohort is keyed by (ICD-10, ATC, LOINC, ICHI, GMDN, etc.) with the body, edition, and rationale.
2. **List every bridge / adjunct standard** used in the cohort's data model (SNOMED CT, ICD-11 candidate, RxNorm, DDD, RadLex, DICOM TID, ISMP tall-man, FHIR resource name, etc.) with body and edition.
3. **State enforcement context** — for each, name the body that enforces (regulator, national MoH, accreditation body) where any does.
4. **Flag licensing constraints** explicitly — CDT (ADA), GMDN (paywall) are the headline ones; surface them so the app team knows.
5. **Reference this document** — `_context/standards-and-bodies.md` — as the canonical inventory.

Reports must NOT just say "we use ICD-10". They must say:

> Conditions are keyed by ICD-10 (WHO 2019 official version), with SNOMED CT concept IDs (SNOMED International) as the clinical-concept bridge per Coiera 3e ch. 23. ICD-11 candidate codes (WHO) are populated where mapping is straightforward as a future-proofing measure. Notifiable status is driven by the Uganda IDSR list (Uganda MoH, statutory enforcement under the Public Health Act).

That style — what · who · enforced where · why · limits — is the bar.

---

## Maintenance

When standards update (e.g., LOINC quarterly, CDT annually, EMHSLU triennially, ICHI when it leaves beta, ICD-11 as Uganda adopts), this document and every cohort's `code_system_version` + `code_accessed_date` columns must be refreshed. Coiera 3e ch. 23 — terminology maintenance dominates lifetime cost.
