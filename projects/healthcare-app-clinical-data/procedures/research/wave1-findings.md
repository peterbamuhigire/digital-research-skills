# Wave 1 Findings — Procedures Cohort

**Date:** 2026-05-03

**Scope:** Clinical procedure reference corpus for Uganda-targeted healthcare management app. RRH-level (Regional Referral Hospital) surgical and clinical scope.

**Geographic scope:** Uganda primary; Kenya and Tanzania for triangulation. District hospital and regional referral hospital capacity per WHO and Ministry of Health standards.

**Hard exclusions (applied verbatim):** Cardiothoracic surgery (no open-heart, CABG, valve replacement, major thoracic); Neurosurgery (no cranial, spinal cord, specialist neurosurgical interventions); Transplant surgery (no solid-organ or stem-cell transplant); Veterinary; Traditional/herbal.

**Hard inclusions:** Dental procedures (CDT codes, with ADA licensing flag for app team). Paediatric-specific procedure variants as separate rows where technique materially differs.

---

## Coverage Summary

**Target:** 220 procedures. **Wave 1 yield:** [COUNT TBD] items with sourced data. Gap-marking applied per evidence-discipline standards.

### By category:

- **Obstetrics-Gynaecology (OB-Gyn):** Emphasis on emergency maternal procedures (caesarean section, assisted vaginal delivery, manual vacuum aspiration, manual placental removal), post-abortion care, and cervical/uterine procedures [SOURCE: Uganda MoH Essential Maternal and Newborn Clinical Care Guidelines 2022; WHO EmOC definition per _Cesarean section in sub-Saharan Africa_](ucg-maternal-2022, who-emoc-pmc).
- **General Surgery:** Appendectomy, hernia repair (inguinal, femoral, umbilical), wound exploration and closure, exploratory laparotomy, bowel resection [SOURCE: _Groin Hernia Surgery in Uganda…_ (Springer); PLOS Medicine cross-country study](uganda-hernia-springer, plos-essential-surgery).
- **Orthopaedics:** Fracture reduction and fixation (femur, tibia, upper limb), open reduction internal fixation (ORIF), external fixation, traction methods, plaster casting [SOURCE: _Musculoskeletal Trauma Services in Uganda_ (PMC); _Developing Orthopaedic Trauma Capacity in Uganda_](uganda-trauma-pmc, uganda-ortho-capacity).
- **ENT:** Tonsillectomy, myringotomy, tympanostomy tube insertion, functional endoscopic sinus surgery (FESS), ear canal procedures [SOURCE: Uganda hospital directories; _Top 10 Most Common ENT Procedures_ LifeCare](ent-services-uganda, ent-common-procedures).
- **Ophthalmology:** Cataract extraction (manual extracapsular, phacoemulsification variants), pterygium excision, corneal abrasion management, laser surgery, glaucoma diagnostic procedures [SOURCE: _Eye care where there are no ophthalmologists: the Uganda experience_ (PMC); _Cataract surgery at district hospital level_](uganda-eye-care-pmc, cataract-district-hospital).
- **Urology:** Urinary catheterization (urethral, suprapubic), catheter management, bladder catheter exchange, urinary diversion [SOURCE: StatPearls (NIH); _Urinary Catheter Documentation in a Nigerian Teaching Hospital_](suprapubic-catheter-statpearls, nigerian-catheter-documentation).
- **Paediatrics:** Appendectomy (paediatric variant), intussusception reduction, exploratory laparotomy, hernia repair (paediatric), gastroschisis closure, inguinal hernia [SOURCE: _Paediatric surgery in Uganda: current challenges and opportunities_ (Springer 2024); _Access to pediatric surgery delivered by general surgeons…_ (Surgery journal)](uganda-paeds-surgery-springer, uganda-paeds-access-surgery).
- **Dental:** Full CDT (Code on Dental Procedures and Nomenclature) 2024 classification. Includes extraction (D7xxx series), restorative (D2xxx), prosthodontic, periodontal, orthodontic, preventive [SOURCE: ADA CDT 2024](ada-cdt-2024). **LICENSING NOTE:** CDT is ADA-licensed; codes used here under fair-use for reference. App team requires an ADA license for commercial deployment surfacing CDT codes to end-users.
- **Minor Procedures:** Laceration repair (simple, intermediate, complex), abscess incision and drainage, wound exploration, suture removal, minor foreign body removal [SOURCE: _Incision and Drainage_ StatPearls; _Common Questions About Wound Care_ AAFP](incision-drainage-statpearls, wound-care-aafp).
- **Anaesthesia:** Spinal anesthesia, epidural anesthesia, general anesthesia induction, local infiltration, regional nerve blocks, airway management [SOURCE: _Spinal versus epidural anesthesia for vesicovaginal fistula repair…_ (ScienceDirect); _SPINAL ANAESTHESIA — A Practical Guide_ (WFSA)](spinal-epidural-vvf, spinal-wfsa-practical).
- **Emergency:** Emergency resuscitation, trauma resuscitation, perimortem caesarean section, emergency laparotomy, emergency wound management [SOURCE: _Emergency Obstetric Protocols_ (Kenya); WHO EmOC standards](kenya-emoc-protocols, who-emoc-standards).

---

## Coding Standard Notes

### ICHI (Primary)
WHO ICHI beta was released October 2020 (Beta-3). Clinical and functioning intervention components finalized; public health component finalized 2023 [SOURCE: WHO ICHI overview](who-ichi-beta). **Status:** Beta release; many surgical procedures do not yet have stable ICHI codes. Of 55 items evaluated in a recent study, 93.2% were successfully assigned an ICHI code, but the system remains under active refinement [SOURCE: _Coding Public Health Interventions for Health Technology Assessments: A Pilot Experience With WHO's ICHI_](ichi-hta-pilot). Mark `[GAP — ICHI code not yet stable]` where ICHI is unavailable; these will be reconciled in post-QA when ICHI stabilizes.

### ICD-10-PCS (Secondary)
US-origin procedural classification. 2024 update includes 78,603 total codes (41 new codes effective 2024-04-01, 78 new total for 2024, 5 deletions) [SOURCE: _2024 ICD-10-PCS Updates_ (yes-himconsulting); CMS ICD-10 website](icd10pcs-2024-updates, cms-icd10pcs-2024). Seven-character alphanumeric code structure per CMS guidelines [SOURCE: _ICD-10-PCS Official Guidelines for Coding and Reporting 2024_](cms-icd10pcs-2024-guidelines).

### CDT (Dental)
ADA CDT 2024 includes 14 new codes, 2 revisions, 1 new service category (sleep apnea). 5-character alphanumeric codes starting with D, grouped by service category [SOURCE: _Decoding the Codes: 2024 CDT Coding Updates_ (AAE); Delta Dental CDT updates](cdt-2024-updates-aae, cdt-2024-delta-dental).

---

## Level of Care Mapping (Uganda MoH Service Standards)

Per Uganda MoH Comprehensive Service Standards Manual (2021) [SOURCE: moh-uganda-service-standards-2021](moh-uganda-service-standards-2021):

- **Health Centre III (HC III):** Outpatient care, minor wound management, antenatal care, delivery of normal labour (no surgical procedures except in emergencies).
- **Health Centre IV (HC IV):** Basic Emergency Obstetric Care (BEmONC), wound closure, catheterization, some minor procedures.
- **District Hospital (DH):** Comprehensive Emergency Obstetric Care (CEmONC) including caesarean section, appendectomy, hernia repair, fracture reduction, uncomplicated cataract extraction.
- **Regional Referral Hospital (RRH):** Advanced surgical care, complex fracture management, complicated caesarean sections, comprehensive ophthalmologic procedures, paediatric surgery.

This app targets RRH-level scope with downward compatibility to DH-level.

---

## Procedure Distribution Notes

### High-volume Uganda procedures (per regional literature)
Obstetric procedures dominate volume: caesarean section, manual vacuum aspiration (MVA), assisted vaginal delivery. General surgery: hernia repair (7/100,000 population annual rate per Uganda study) [SOURCE: _Groin Hernia Surgery in Uganda…_](uganda-hernia-springer). Orthopedics: fracture management at all levels; tibia is most frequent open fracture site (1504 cases in regional study), femur 347 cases [SOURCE: _A Scoping Review on the Management of Open Fractures in African Trauma and Orthopaedics Centres_](open-fractures-scoping-review). Ophthalmology: cataract extraction is high-volume due to burden of cataract blindness in Uganda [SOURCE: _Eye care where there are no ophthalmologists_](uganda-eye-care-pmc).

### Anaesthesia procedures
Spinal anesthesia preferred in resource-limited settings (86% of operations in one sub-Saharan hospital) [SOURCE: _Spinal versus epidural anesthesia for vesicovaginal fistula repair…_](spinal-epidural-vvf). Local infiltration widely available. General anesthesia limited by oxygen availability; emergency cases prefer spinal where GA not safe [SOURCE: _Groin Hernia Surgery in Uganda…_](uganda-hernia-springer).

### Paediatric-specific variants
Paediatric appendectomy, intussusception reduction, and inguinal hernia repair documented as separate cases [SOURCE: _Paediatric surgery in Uganda…_](uganda-paeds-surgery-springer). Paediatric surgical mortality at two rural RRHs: 0% for hernia/appendicitis, <1% for infection, <2% for trauma [SOURCE: _Access to pediatric surgery delivered by general surgeons…_](uganda-paeds-access-surgery).

---

## Gaps Identified in Wave 1

1. **ICHI Codes:** Many surgical procedures lack stable ICHI codes in the beta release. Marking these as `[GAP — ICHI code not yet stable]`.
2. **Specific Uganda-level procedure lists:** While Uganda MoH guidelines exist, detailed procedure-by-level-of-care matrices are fragmented across documents. Some procedures (e.g., advanced ophthalmology procedures at RRH) lack explicit level-of-care designation in available sources.
3. **CDT code full roster:** ADA CDT 2024 is proprietary. Complete CDT code list not freely available; extracting from published subsets (AAE, Delta Dental).
4. **Paediatric dosage and equipment specifications:** Beyond the note that paediatric variants should be separate rows, specific anaesthetic doses, airway sizes, and equipment specs are outside the scope of this procedure reference (belong to Clinical_Drugs and Medical_Equipment cohorts).

---

## Sources Used in This Wave

### T1 (Primary)

- @misc{cms-icd10pcs-2024} — ICD-10-PCS 2024 official code set and guidelines
- @misc{ada-cdt-2024} — ADA CDT 2024 (proprietary; codes used under fair-use for reference)
- @misc{who-ichi-beta} — WHO ICHI beta classification system (primary for procedures, but many codes unstable)
- @misc{ucg-maternal-2022} — Uganda MoH Essential Maternal and Newborn Clinical Care Guidelines, May 2022
- @misc{moh-uganda-service-standards-2021} — Uganda MoH Comprehensive Health Service Standards Manual, 2021

### T2 (Corroborate)

- @article{plos-essential-surgery} — _Essential Surgery at the District Hospital: A Retrospective Descriptive Analysis in Three African Countries_ (PLOS Medicine 2010)
- @article{uganda-hernia-springer} — _Groin Hernia Surgery in Uganda: Caseloads and Practices at Hospitals Operating Within the Publicly Funded Healthcare Sector_ (World Journal of Surgery, Springer)
- @article{uganda-trauma-pmc} — _Musculoskeletal Trauma Services in Uganda_ (PMC)
- @article{uganda-ortho-capacity} — _Developing Orthopaedic Trauma Capacity in Uganda: Considerations From the Uganda Sustainable Trauma Orthopaedic Program_ (PubMed/PMC)
- @article{uganda-eye-care-pmc} — _Eye care where there are no ophthalmologists: the Uganda experience_ (PMC)
- @article{uganda-paeds-surgery-springer} — _Paediatric surgery in Uganda: current challenges and opportunities_ (Springer Nature 2024)
- @article{uganda-paeds-access-surgery} — _Access to pediatric surgery delivered by general surgeons and anesthesia providers in Uganda: Results from 2 rural regional hospitals_ (Surgery journal)
- @article{open-fractures-scoping-review} — _A Scoping Review on the Management of Open Fractures in African Trauma and Orthopaedics Centres_ (PMC)
- @article{spinal-epidural-vvf} — _Spinal versus epidural anesthesia for vesicovaginal fistula repair surgery in a rural sub-Saharan African setting_ (ScienceDirect)

### T3 (Triangulation only, never sole source)

- @misc{ent-services-uganda} — Uganda hospital facility directories (C-Care, Norvik, Roswell ENT)
- @misc{ent-common-procedures} — _Top 10 Most Common ENT Procedures_ (LifeCare Hospitals)
- @article{cataract-district-hospital} — _Cataract surgery at district hospital level_ (International Ophthalmology, Springer)
- @misc{incision-drainage-statpearls} — _Incision and Drainage_ (StatPearls, NIH)
- @misc{wound-care-aafp} — _Common Questions About Wound Care_ (American Academy of Family Physicians)
- @misc{suprapubic-catheter-statpearls} — _Suprapubic Bladder Catheterization_ (StatPearls, NIH)
- @article{nigerian-catheter-documentation} — _Urinary Catheter Documentation in a Nigerian Teaching Hospital_ (PMC)
- @misc{spinal-wfsa-practical} — _SPINAL ANAESTHESIA — A Practical Guide_ (World Federation of Societies of Anaesthesiologists)
- @misc{kenya-emoc-protocols} — _Emergency Obstetric Protocols_ (Emergency Medicine Kenya)
- @misc{cdt-2024-updates-aae} — _Decoding the Codes: 2024 CDT Coding Updates_ (American Association of Endodontists)
- @misc{cdt-2024-delta-dental} — CDT 2024 updates (Delta Dental)
- @article{ichi-hta-pilot} — _Coding Public Health Interventions for Health Technology Assessments: A Pilot Experience With WHO's International Classification of Health Interventions_

---

## Next Steps (Wave 2)

- Access Uganda MoH service standards documents directly to extract level-of-care matrices for all procedures.
- Reconcile ICHI gaps as new codes stabilize (likely post-2026).
- Extract full CDT roster from authoritative dental specialty source (if ADA license obtained for app team).
- Triangulate paediatric-specific variants with Kenya and Tanzania paediatric surgery literature.

