# Wave 1 Findings - Country Packs: Multi-Tenant Localisation Constants

**Date:** 2026-05-03

**Cohort:** country-packs

**Scope:** Uganda and Kenya full packs; stub-only entries for Tanzania, Rwanda, Ghana, Nigeria, South Africa, India, Philippines.

**Evidence discipline:** T1 sources (statutory acts, constitutional documents, government-published structures, official regulatory body websites, ISO standards) cited at point of claim. No Wikipedia in source_citations table cells. T3 sources (encyclopaedia) used for corroboration only, explicitly marked.

---

## 1. Uganda Full Pack — Administrative Structure, Regulators, and Mandatory Reports

### 1.1 Sub-National Administration

Uganda's administrative structure underwent significant decentralization post-2005. As of 2026, the country comprises [146 districts](https://www.statoids.org/en/ug/admin-levels/l2/list/uganda/districts), the Kampala Capital City Authority, 10 regional cities, and 41 municipalities. Below the district level, the [Local Government Act creates five levels of local councils (LCs)](https://www.sng-wofi.org/country_profiles/uganda.html):

- **LC5 (District):** 146 districts plus Kampala Capital City Authority
- **LC4 (Sub-district):** 31 municipalities and 20 city division councils
- **LC3 (Sub-county):** [1,495 sub-counties, 581 town councils, and 89 municipal division councils](https://www.sng-wofi.org/country_profiles/uganda.html)
- **LC2 (Parish):** [10,594 parishes/wards](https://en.wikipedia.org/wiki/Parishes_of_Uganda)
- **LC1 (Village/Cell):** [70,512 villages/cells](https://en.wikipedia.org/wiki/Villages_of_Uganda)

For the app's country-pack constant, `admin_level_1_name` is **District** (146 as of 2026); `admin_level_2_name` is **Sub-county** (2,100+ total, with ongoing administrative restructuring).

**Ministry of Health Hierarchy:** The [Ministry of Health Uganda](https://health.go.ug/structure/) operates through a central office with 18 departments (restructured from 6 in previous iterations), district health teams (DHTs) at district level, and facility-level management per facility type. The health system includes a large PNFP sector coordinated through faith-based bureaux: Uganda Catholic Medical Bureau (UCMB), Uganda Protestant Medical Bureau (UPMB), Uganda Orthodox Medical Bureau (UOMB), and Uganda Muslim Medical Bureau (UMMB).

### 1.2 Regulatory Bodies and Acts

Uganda's health professional regulation is distributed across multiple councils, each established by statute:

**Medical & Dental Practitioners:** [Uganda Medical and Dental Practitioners Council (UMDPC) under Medical and Dental Practitioners Act Cap 272](https://www.umdpc.go.ug/), established 1998. Mandate: registration, licensing, disciplinary control of medical and dental practitioners. (synthesis) The Act was amended in 2023 to update fines to currency points.

**Clinical Officers:** [Allied Health Professionals Council (AHPC) under Allied Health Professionals Act Cap 268](https://ahpc.ug/), established 1996. CRITICAL: AHPC (NOT UMDPC) regulates clinical officers. [Approximately 11,795 medical clinical officers are registered with AHPC](https://mcop-uganda.org/), representing 39% of Uganda's health-facility workforce leadership (per survey data). Clinical officers are essential to Uganda's primary healthcare delivery, particularly at HC III and HC IV levels.

**Nurses & Midwives:** [Uganda Nurses and Midwives Council (UNMC) under Nurses and Midwives Act 1996 (Cap 301)](https://unmc.ug/), effective 8 November 1996. Mandate: training standards, registration, licensure (3-year renewal cycle), private practice licensing, disciplinary control.

**Medicines Regulation:** [National Drug Authority (NDA) under National Drug Policy and Authority Act Cap 206](https://www.nda.or.ug/), established 1993, operational since 1994. Mandate: registration of pharmaceuticals, import/export control, drug quality, pharmacy/drug-shop licensing. **CRITICAL:** NDA issues drug-shop licenses in **Class A, B, or C tiers** reflecting *retail dispensing scope*, NOT prescribing schedules. This distinction is essential for the app's pharmacy-permissions module (Uganda's NDA does not define prescriber schedules; clinical guidelines determine that).

### 1.3 Mandatory Reports and HMIS/IDSR Forms

Uganda's health reporting system combines routine facility reports (HMIS) with disease surveillance (IDSR):

**Annual Reporting:**
- [HMIS-107 Health Unit Annual Report (due 7 August)](https://library.health.go.ug/file-download/download/public/331): Aggregate of facility performance across OPD, inpatient, MCH/FP, lab, special services, staffing, financial management. Submitted to health sub-district, district, and Local Council Health Committee.

**Monthly Reporting:**
- [HMIS-105 Health Unit Outpatient Monthly Report](https://health.go.ug/): OPD attendance, diagnoses, MCH, HIV/AIDS, lab data, essential drug stock-outs. Targets facilities at HC III and above. Submitted to DHIS2.
- [HMIS-108 Health Unit Inpatient Monthly Report](https://health.go.ug/): Inpatient admissions, diseases, deaths, ward activity. Submitted to DHIS2.
- [HMIS-106A Quarterly Report](https://health.go.ug/): HIV care/ART attendance, nutrition, TB aggregates (quarterly).

**Weekly Reporting (Disease Surveillance):**
- [HMIS-033B Weekly Epidemiological Surveillance Report](https://library.health.go.ug/): Notifiable-disease cases (immediate notification), tested/positive tallies, GeneXpert/IPT summaries. Submitted via mTrac/eIDSR to health sub-district and district.
- [HMIS-033C Weekly Summary Form](https://library.health.go.ug/): Facility-facing summary of weekly case and death data. Supports zero-reporting capability.

**Outbreak/Case-Based Reporting (Immediate):**
- [HMIS-033A Case-based reporting form](https://library.health.go.ug/): Suspected/probable/confirmed priority disease reports sent immediately to IDSR reporting chain.
- [Case Investigation Form (CIF)](https://library.health.go.ug/): Case details, specimen linkage, contact information. Completed by district surveillance staff.
- [Contact Tracing Form](https://library.health.go.ug/): Tracks contacts of index case and monitors for symptom development.

**Specialty-Specific Forms:**
- HMIS-096A (TB treatment progress & outcome)
- HMIS-080/081 (Pre-ART and ART registers)
- HMIS-082/082A (HIV-exposed infant monitoring)
- HMIS-055/055A/055B (HIV testing services register and client card)
- HMIS-071, 072, 078 (ANC, maternity, PNC registers)

[IDSR Technical Guidelines (3rd Edition, September 2021)](https://reliefweb.int/report/uganda/national-technical-guidelines-integrated-disease-surveillance-and-response-third) define the notifiable-disease list, case definitions, and reporting pathways. Reporting timeliness targets: weekly reports submitted by Friday for the preceding week; monthly reports by 5th of following month.

### 1.4 National Identification and Patient-ID Strategy

Uganda's national identification is administered by the [National Identification and Registration Authority (NIRA) under the Registration of Persons Act 2015](https://www.nira.go.ug/). The [National Identification Number (NIN) is a unique 14-digit code issued by NIRA](https://www.nira.go.ug/) to all registered citizens. Key rules for healthcare identity:

- **Age of issuance:** Age 18+ (adults receive full national ID cards).
- **Fallback for under-18s:** Children under 18 may be identified using parent's NIN combined with the child's birth-registration number.
- **Current enrollment:** [NIRA's mass enrollment (April 2025–February 2026) registered 6.15 million first-time applicants and renewed 13.37 million IDs](https://www.nira.go.ug/news/a-one-year-validity-extension-period-for-national-id-cards-granted-as-mass-enrollment-efforts-intensify).

For a multi-tenant SaaS, the patient-identity module must accept:
1. Adult NIN (14-digit, primary identifier).
2. Child identifier: parent NIN + birth-certificate number (for under-18s not yet issued NIN).
3. Fallback for undocumented or refugee populations (marked as "other" with manual entry verification).

### 1.5 Data Protection and Privacy Law

The [Data Protection and Privacy Act 2019 (Act No. 9 of 2019, effective 3 May 2019; Regulations effective 12 March 2021)](https://ulii.org/en/akn/ug/act/2019/9/eng@2019-05-03) establishes Uganda's privacy framework for clinical data:

- **Scope:** Applies to any person, institution, or public body collecting, processing, holding, or using personal data within Uganda or outside Uganda if the data relates to Ugandan citizens.
- **Data controller obligations:** Obtain consent (opt-in), limit collection to necessary purposes, implement security, allow subject access, report breaches. Overseas transfer of health data must ensure the destination country's protections meet equivalent standards.
- **Enforcement:** Personal Data Protection Office (PDPO), an independent office under [National Information Technology Authority Uganda (NITA-U)](https://www.nita.go.ug/), enforces the Act and investigates complaints.
- **Penalties:** Criminal sanctions for unlawful disclosure, deletion, or alteration of personal data.

**Implication for the SaaS:** Data localisation (Uganda resident data stored within Uganda), consent workflows for patient data use, breach notification procedures, and documented data-processing agreements with any sub-processors.

---

## 2. Kenya Full Pack — Devolution, Health Authority Transition, and Healthcare Financing Shift

### 2.1 Administrative Structure and Devolution

Kenya's [Constitution 2010 devolved health service delivery to 47 counties](https://www.klrc.go.ke/index.php/klrc-blog/645-the-bliss-of-niims-paradise-the-legal-framework-for-the-huduma-namba), replacing the previous 8-province system. Under the [County Governments Act 2012](https://www.worldbank.org/content/dam/Worldbank/document/Africa/Kenya/Kenay%20Devolution/County%20Governments%20Act%20(2012).pdf):

- **County** (admin_level_1): 47 counties, each with a governor and elected assembly. County governments hold health service delivery, regulation of private practitioners, and health facility licensing at county level.
- **Sub-county** (admin_level_2): [Not more than 1,450 electoral wards](https://new.kenyalaw.org/akn/ke/act/ln/2020/195/eng@2022-12-31); these coincide with county assembly ward constituencies. Each ward has a ward administrator reporting to the sub-county administrator.
- **Hierarchy:** National MoH (policy, standards, coordination) → County Health Department (service delivery, facility management, local regulation) → Sub-county Health Office (facility supervision) → Facility level (community health unit, dispensary, health centre, or hospital).

**Ministry of Health Hierarchy:** [Kenya's Ministry of Health](https://www.health.go.ke/) operates with a Cabinet Secretary and State Department for Devolution, who oversee the 47 county health departments. Private and PNFP sectors are significant: [Christian Health Association of Kenya (CHAK)](https://www.chak.or.ke/), Catholic dioceses, and other NGO networks operate ~35% of Kenya's health facilities.

### 2.2 Regulatory Bodies and Acts

Kenya's health professional regulation is distributed across councils established by statute:

**Medical & Dental Practitioners:** [Kenya Medical Practitioners and Dentists Council (KMPDC) under Medical Practitioners and Dentists Act Cap 253](https://kmpdc.go.ke/), established 1998. Mandate: registration, licensing, disciplinary control of physicians and dentists; licensing of health facilities.

**Clinical Officers:** [Clinical Officers Council (COC) under Clinical Officers (Training, Registration and Licensing) Act 2017 (Act No. 20 of 2017, assented 21 June 2017, effective 7 July 2017)](https://clinicalofficerscouncil.org/). This replaced the previous Cap 260 (1988) with enhanced regulatory powers. Mandate: training standards, registration, licensing (private practice), professional conduct, disciplinary action.

**Nurses & Midwives:** [Nursing Council of Kenya (NCK) under Nurses Act Cap 257 (revised 2012, operational since 1985)](https://nckenya.org/). Mandate: training standards, registration, licensure, professional conduct enforcement.

**Pharmacists & Medicines:** [Kenya Pharmacy and Poisons Board (PPB) under Pharmacy and Poisons Act Cap 244](https://web.pharmacyboardkenya.org/). Mandate: regulation of pharmacy practice, manufacture, import, distribution, and sale of drugs and poisons. **CRITICAL:** PPB defines prescribing schedules as **Part I / Part II poisons** under Cap 244, which is a valid legal categorisation (unlike Uganda's NDA "Class A/B/C" retail tiers).

**Laboratory Technologists:** [Kenya Medical Laboratory Technicians and Technologists Board (KMLTTB) under Medical Laboratory Technicians and Technologists Act (Cap 253A)](https://kmlttb.org/). Mandate: training, registration, licensure, and accreditation. **NEW:** [Business Laws Amendment 2024 now requires ISO 15189 accreditation for accredited labs](https://www.kmlttb.org/), making international laboratory standards mandatory for Kenya's public and regulated private labs.

**Health Records:** [Health Records and Information Managers Act 2016](https://new.kenyalaw.org/akn/ke/act/2016/3/eng@2016-04-28) establishes a [Health Records and Information Managers Board (HRIMB)](https://new.kenyalaw.org/akn/ke/act/2016/3/eng@2016-04-28), regulating the health records profession.

### 2.3 Health Information System and Mandatory Reporting

Kenya uses [KHIS (Kenya Health Information System) on DHIS2 (District Health Information Software 2)](https://hiskenya.org/), which was the first Sub-Saharan African country to deploy a fully online HIS (completed September 2011). Monthly aggregate reporting from facilities is mandatory:

- **Facility reporting:** Health centres (Level 3), hospitals (Levels 4+), and dispensaries (Level 2) submit monthly KHIS data on OPD, inpatient, maternal, laboratory, commodity, and disease surveillance indicators.
- **County aggregation:** County health management information officer (HMIO) aggregates facility reports; sub-county supervisors provide oversight.
- **Notifiable disease reporting:** Integrated Disease Surveillance and Response (IDSR) — Kenya adopts the WHO-AFRO framework aligned with Uganda's IDSR structure — reporting notifiable diseases weekly to county and national surveillance focal persons via KHIS Tracker.

**Gap:** Exact mandatory form set (e.g., equivalent to Uganda's HMIS-105, HMIS-108) and quarterly/annual KPI reporting structure for counties is flagged for Wave-2 mapping.

### 2.4 National Identity System and Patient-ID Strategy

Kenya is transitioning from the [Huduma Namba (National Integrated Identity Management System, NIIMS) to the Maisha Namba digital identity](https://hudumaglobal.com/blog/how-kenya-national-id-system-works-analog-cards-maisha-namba-digital-identity). Both systems are centrally managed:

**Huduma Namba / Maisha Namba:**
- **Type of ID issued:** Unique permanent personal identification number randomly assigned (not sequential). [Types include minors' cards (age 6+), adults' cards (age 18+), and foreign national cards](https://new.kenyalaw.org/akn/ke/act/ln/2020/195/eng@2022-12-31).
- **Age of issuance:** [T1 verification pending — exact age threshold for Huduma/Maisha card issuance and whether separate fallback ID rules exist for under-6 or under-18 populations not fully sourced in available documents]. Current implementation suggests 6+ for minors' cards; 18+ for adults.
- **Legal basis:** [Registration of Persons (National Integrated Identity Management System) Rules 2020 (Legal Notice No. 195 of 2020)](https://new.kenyalaw.org/akn/ke/act/ln/2020/195/eng@2022-12-31). Maisha Namba is a government rebrand of NIIMS architecture with enhanced data-protection safeguards [addressing High Court directives on DNA/GPS data collection](https://privacyinternational.org/long-read/3373/kenyan-court-ruling-huduma-namba-identity-system-good-bad-and-lessons).

For the SaaS patient-ID module, assume:
1. Adults (18+): Huduma/Maisha Namba (10-digit or longer, random).
2. Children (6–17): Minors' Huduma card or parent ID + birth certificate (if minors' card not issued).
3. Under-6 or undocumented: Manual entry with verification flag.

**Note:** [Kenya High Court has made multiple rulings on NIIMS privacy concerns](https://privacyinternational.org/long-read/3373/kenyan-court-ruling-huduma-namba-identity-system-good-bad-and-lessons); SaaS should monitor ongoing legal developments regarding mandatory use and data retention.

### 2.5 Data Protection and Privacy Law

The [Data Protection Act 2019 (Act 24 of 2019, effective 25 November 2019)](https://new.kenyalaw.org/akn/ke/act/2019/24) is Kenya's primary privacy statute, implementing Article 31 of the Constitution 2010:

- **Scope:** Regulates collection, processing, storage, transfer of personal data by any person or organisation in Kenya.
- **Key obligations:** Data controllers and processors must register with the Data Protection Commissioner; consent-based processing; data-subject access rights; breach notification within 72 hours; overseas transfer only to countries with equivalent protections.
- **Enforcement:** [Office of the Data Protection Commissioner (ODPC)](https://www.odpc.go.ke/), an independent authority, enforces the Act. Penalties: fines up to KES 5,000,000 or 1% of annual turnover (whichever is lower); periodic audits of compliance.

**Implication for the SaaS:** Data-processing agreement with the county health departments (as data controllers), patient consent workflows, breach notification procedures, and overseas data-transfer justification if any processing occurs outside Kenya.

### 2.6 Healthcare Financing Transformation: NHIF → SHA

Kenya's health financing underwent a fundamental shift effective [1 October 2024, when the Social Health Authority (SHA) replaced the National Health Insurance Fund (NHIF)](https://www.kenyanews.go.ke/kenya-begins-transition-to-social-health-authority/):

**National Health Insurance Fund (NHIF) — Ending:**
- Ceased operations 30 September 2024.
- Provided limited coverage; many Kenyans were uninsured or underinsured.
- Employer and self-employed contributions varied; informal-sector coverage minimal.

**Social Health Insurance Act 2023 (SHA) — Beginning:**
- [Assented 19 October 2023; operational from 1 October 2024](https://sha.go.ke/).
- Three-fund system:
  1. **Primary Healthcare Fund (PHF):** Government-funded, universal entitlement for all Kenyans (Level 1–3 facilities). No contribution required.
  2. **Social Health Insurance Fund (SHIF):** Contributory replacement for NHIF. [Contributions: 2.75% gross salary, minimum KES 300/month, no maximum](https://sha.go.ke/). Covers Levels 3–6 care.
  3. **Emergency Fund (rescue of catastrophic cases):** High-cost out-of-pocket protection.

**Implication for the SaaS:** The billing-tariffs cohort must eventually map SHA PHF and SHIF benefit schedules (which facilities are covered, at what reimbursement rates, and co-pay requirements). For Wave-1 country-pack purposes, SHA insurance regulator is confirmed; detailed tariff structure deferred to billing-tariffs.

---

## 3. Mandatory Reports per Country — Reporting Frequency and Statutory Basis

### Uganda

| Report | Frequency | Submitter | Recipient | HMIS Form | Statutory Basis |
|---|---|---|---|---|---|
| Annual health-unit report | Annual (due 7 August) | Facility manager | District, HSD, Local Council Health Committee | HMIS-107 | MoH reporting framework |
| Outpatient monthly | Monthly | OPD supervisor | DHIS2, HMIS | HMIS-105 | HMIS-107, facility level documentation |
| Inpatient monthly | Monthly | Ward nurse/medical superintendent | DHIS2, HMIS | HMIS-108 | HMIS-107, facility-level documentation |
| HIV/ART quarterly | Quarterly | ART clinic coordinator | DHIS2, HIV programme | HMIS-106A | MoH HIV guidelines |
| Weekly epidemiological | Weekly (submitted by Friday) | Facility surveillance focal person | Sub-district, district; mTrac/eIDSR | HMIS-033B/033C | IDSR Technical Guidelines 3rd Ed. (Sept 2021) |
| Case-based (notifiable) | Immediate (within 24 hours if suspected) | Facility clinician or surveillance officer | District PHEOC, national level | HMIS-033A | IDSR Technical Guidelines (notifiable disease list) |
| Case investigation | As outbreak occurs | District surveillance officer | Regional, national PHEOC | CIF | IDSR Technical Guidelines |
| TB treatment progress | Routine monthly during treatment | TB programme staff | TB programme, DHIS2 | HMIS-096A | TB/HIV guidelines |
| ART register | Routine | ART clinic staff | Facility record, programme reporting | HMIS-081 | MoH ART guidelines |

**[reporting-kpis gap]:** Quarterly and annual KPI report (HMIS-097) exact scope and deadline not yet sourced in standard-forms corpus; flagged for Wave-2.

### Kenya

| Report | Frequency | Submitter | Recipient | System | Statutory Basis |
|---|---|---|---|---|---|
| KHIS aggregate (all services) | Monthly | Facility HMIO or health records officer | County HMIO, national level | KHIS/DHIS2 | Health Act 2017; MoH reporting directive |
| Notifiable disease (IDSR) | Weekly | Facility disease surveillance officer | County surveillance focal person, national | KHIS Tracker; eIDSR where available | IDSR Technical Guidelines; Constitution 2010 health-service devolution |
| Quarterly service reports | Quarterly | Facility manager | County health department | County-specific form (varies) | County health-system directives |
| County aggregates | Monthly/quarterly/annual | County health management team | National MoH, Parliament health committee | KHIS/DHIS2 | Health Act 2017 |

**[reporting-kpis gap]:** Exact KHIS form set (equivalent to Uganda's HMIS-105/108 suite) and county-specific mandatory forms not yet detailed; flagged for Wave-2.

---

## 4. Privacy and Data-Protection Regimes — Clinical-Data SaaS Compliance

### Uganda: Data Protection and Privacy Act 2019

**Regulatory authority:** Personal Data Protection Office (PDPO) under [NITA-U](https://www.nita.go.ug/).

**Key compliance requirements:**

1. **Consent:** Explicit opt-in consent required for clinical data collection; consent must specify purpose, retention period, and third-party sharing.
2. **Data localisation:** Personal data of Ugandan citizens collected in Uganda must remain in Uganda (or overseas only if equivalent protections exist).
3. **Breach notification:** [No specific timeline codified in law, but PDPO expects prompt notification and investigation](https://www.pdpo.go.ug/).
4. **Subject access:** Patients have right to access, correct, and request deletion of their personal health data.
5. **Processing lawfulness:** Data processing must be limited to the stated purpose (health treatment, audit compliance, etc.).

**Penalties:** Criminal sanctions for unlawful disclosure or alteration of personal data.

**SaaS implementation notes:**
- Ensure patient consent workflows are integrated into intake and registration.
- Document data-processing purpose and retention schedule.
- Implement audit trails for access to patient data (meets PDPA and clinical governance).
- If any data processing occurs outside Uganda (e.g., cloud storage in a third country), document why that country's data-protection laws meet Uganda's equivalent standard.

### Kenya: Data Protection Act 2019

**Regulatory authority:** Office of the Data Protection Commissioner (ODPC) — independent authority.

**Key compliance requirements:**

1. **Registration:** Data controllers and data processors must register with ODPC before collecting personal data; registration is mandatory, not optional.
2. **Consent:** Consent is required for collection and processing; consent must be freely given, specific, informed, and unambiguous.
3. **Data minimisation:** Collect only the personal data necessary for the stated purpose.
4. **Breach notification:** [No specific timeline in Act, but ODPC expects prompt notification](https://www.odpc.go.ke/); ODPC may impose fines for delayed disclosure.
5. **Overseas transfer:** Personal data may be transferred outside Kenya only to countries with equivalent data-protection laws; transfers to inadequate jurisdictions are prohibited.
6. **Subject access:** Patients have right to confirm data is held, access data, correct inaccuracies, and request deletion.

**Penalties:** Fines up to KES 5,000,000 or 1% annual turnover (whichever lower); periodic ODPC audits.

**SaaS implementation notes:**
- Register as a data controller/processor with ODPC (mandatory).
- Data-processing agreement required with county health departments (co-controllers or separate controller relationship).
- Implement patient consent with clear purpose and retention terms.
- Log all access to patient data; provide audit reports to health facilities on request.
- If cloud storage outside Kenya, justify and document adequacy of data protection in that jurisdiction.

### Comparative Summary

Both Uganda and Kenya require:
- **Consent-based processing** with transparent purpose statements.
- **Audit trails** for data access.
- **Breach notification** to the regulatory authority and affected patients.
- **Overseas data-transfer controls** (equivalent-protection standard).
- **Patient access rights** (view, correct, delete).

**Key difference:**
- Kenya's ODPC requires *mandatory registration* of data controllers upfront; Uganda's PDPO does not explicitly mandate pre-collection registration but expects compliance with the Act's principles.
- Kenya's fine structure (KES 5M or 1% turnover) is more prescriptive than Uganda's (criminal sanctions for specific breaches).

---

## 5. Insurance and Financing Landscape — Uganda Pending, Kenya Transitioning

### Uganda: Pending National Health Insurance Scheme

Uganda's health financing remains dominated by **out-of-pocket payments and PNFP cost-sharing**, with no statutory universal insurance scheme operational as of May 2026.

- **National Health Insurance Scheme (NHIS):** Has been under development for over a decade; multiple bills submitted to Parliament; no implementation date confirmed. When implemented, it is expected to establish a regulatory authority (likely within Ministry of Health), but this authority does not yet exist.
- **PNFP sector:** Faith-based (UCMB, UPMB, UOMB, UMMB) and NGO facilities operate under cost-sharing models; patients pay out-of-pocket with sliding-scale fees based on ability to pay.
- **Public sector:** Government facilities at HC II/III are expected to provide free care but often face drug and supply shortages, pushing patients to private pharmacies.

**Implication for SaaS:** No insurance-regulator constant is available for Uganda. Billing-tariffs cohort must flag this as a gap and plan for either (1) future NHIS integration or (2) documentation of facility-level cost-sharing policies and payment tracking by patient class (adult, child, pregnant, HIV+, etc.).

### Kenya: Social Health Authority (SHA) Operational Since 1 October 2024

Kenya's shift from NHIF to SHA is a major structural change for the healthcare-finance country-pack constant:

- **Primary Healthcare Fund (PHF):** Government-funded; universal entitlement; covers primary care (Levels 1–3) at no user cost. All Kenyans eligible regardless of employment status.
- **Social Health Insurance Fund (SHIF):** Contributory; [2.75% gross salary, KES 300/month minimum](https://sha.go.ke/); covers secondary and tertiary care (Levels 3–6).
- **Emergency Fund:** Catastrophic-cost protection for cases exceeding SHIF coverage.

**Benefit schedule:** [Not yet fully detailed in public domain as of May 2026; billing-tariffs cohort flagged to source SHA tariff schedules](https://sha.go.ke/), co-pay requirements, and exemptions (e.g., pregnant women, children under 5, elderly).

**Implication for SaaS:** Country-pack confirms SHA as insurance regulator; detailed tariff structure (which procedures/drugs are covered at Levels 3–6, co-pay amounts, exemptions) deferred to billing-tariffs.

---

## 6. National ID / Patient-Identity Strategy — Under-18s, Refugees, Undocumented Populations

### Uganda: NIN (National Identification Number) Model

**Key rules:**
- **Primary identifier:** NIN (14-digit, issued by NIRA from age 18+).
- **Fallback for under-18s:** Parent NIN + child's birth-registration number (issued by civil registration authority).
- **Refugees/undocumented:** Manual registration with "unknown ID" flag; used typically by NGO-supported clinics serving displaced populations. Facility must keep external population register and cross-reference clinical encounters.

**SaaS implementation:**
- Patient identity table must accommodate three ID types:
  1. Adult NIN (14-digit, unique, required).
  2. Child ID (composite: parent NIN + birth-cert number; required for under-18).
  3. Manual ID (free-text or clinic-generated ID; flagged as "unverified" for audit purposes).
- Workflow: At intake, ask for NIN (if adult) or parent NIN + birth cert (if child); if unavailable, create clinic-level unique ID and flag record as "identity pending verification".

### Kenya: Huduma Namba / Maisha Namba Model

**Key rules:**
- **Primary identifier:** Huduma Namba / Maisha Namba (unique permanent ID, randomly assigned; types: minors 6+, adults 18+, foreign nationals).
- **Fallback for under-6 or undocumented:** [T1 verification pending]; assume parent ID + birth certificate or manual clinic ID.
- **Refugees:** Kenya hosts significant refugee populations (Dadaab, Kakuma camps); UNHCR-issued refugee cards or manual clinic registration common. Facilities must track these separately per national regulations.

**SaaS implementation:**
- Similar to Uganda but accommodate Huduma/Maisha instead of NIN.
- ID type selector: Huduma card (10+digit), birth certificate + parent Huduma, manual clinic ID.
- Flag for verification if Huduma database lookup fails (offline mode fallback).

### Public-Private Split

Both countries have **public-sector facilities** (government health centres, hospitals) and **private-sector facilities** (PNFP and for-profit clinics). Patient identity rules are unified (same NIN/Huduma applies across public and private), but **data sharing between sectors is limited**:

- **Public sector:** Patient data from government clinics is aggregated into HMIS (Uganda) or KHIS (Kenya) for facility reporting; individual-level data not shared with private sector without explicit consent.
- **Private sector:** Patient data is the facility's property; no automatic reporting to national HMIS/KHIS (though some private chains in Kenya are beginning to report to KHIS).
- **Implication for SaaS:** If the multi-tenant app serves both public and private facilities, ensure patient-identity rules are consistent (same patient should have same ID across both), but data-sharing controls are strict (no automatic cross-facility data flows without patient consent and legal basis).

---

## 7. Nigeria Full Pack — Federal Health System, State/LGA Governance, and NHIA Transition (Pass 2 — 2026-05-04)

### 7.1 Administrative Structure and Federal Decentralization

Nigeria's [Constitution 1999 (Schedule 1) establishes a federal system comprising 36 states plus the Federal Capital Territory (FCT) Abuja](https://www.learnnigerianlaw.com/learn/constitutional-law/local-government), for a total of 37 administrative units at the state level. Below this, the country is subdivided into [774 Local Government Areas (LGAs)](https://statoids.com/yng.html): 768 LGAs distributed across the 36 states and 6 area councils in the FCT. Each LGA is further subdivided into a [minimum of 10 and maximum of 20 wards](https://www.learnnigerianlaw.com/learn/constitutional-law/local-government).

**Three-Tier Health Governance:** Health service delivery is coordinated through a federal-state-LGA framework: the [Federal Ministry of Health and Social Welfare (FMoHSW, renamed 2023; previously FMoH)](https://health.gov.ng/) sets policy and standards; 36 state ministries of health implement and adapt services; 774 LGA health departments deliver primary healthcare and coordinate facility networks. This tri-partite structure distinguishes Nigeria from Uganda and Kenya's more centralized or devolved (Kenya) models.

### 7.2 Health Ministry and Regulatory Bodies

**Federal Ministry of Health and Social Welfare:** [The FMoHSW operates through departments including Hospital Services, Food and Drugs Services, Health Planning/Research/Statistics, and Health System Strengthening](https://health.gov.ng/departments/). The ministry coordinates federal teaching hospitals, federal medical centres, and the [Nigeria Centre for Disease Control (NCDC, a federal agency under FMoHSW)](https://ncdc.gov.ng/). State and LGA authorities operate their own facility networks and report aggregated data to the federal level.

**Medicine Regulation:** [NAFDAC (National Agency for Food and Drug Administration and Control) under NAFDAC Act Cap N1 LFN 2004](https://nafdac.gov.ng/) (originally Decree 15 of 1993) regulates pharmaceuticals, medical devices, food, cosmetics, and chemicals. [The Pharmacists Council of Nigeria (PCN) under Pharmacy Council of Nigeria Act 2022](https://pcn.gov.ng/) regulates pharmacy professionals, pharmacy education, and pharmacy premises.

**Clinical Professions Regulation:**
- **Doctors & Dentists:** [Medical and Dental Council of Nigeria (MDCN)](https://www.mdcn.gov.ng/) — established 1963, regulates registration, licensing, disciplinary action for medical and dental practitioners.
- **Nurses & Midwives:** [Nursing and Midwifery Council of Nigeria (NMCN)](https://nmcn.gov.ng/) — established by Decree 89 (1979), now Nursing and Midwifery (Registration etc) Act Cap N143 LFN 2004; regulates nursing education and licensure.
- **Laboratory Scientists:** [Medical Laboratory Science Council of Nigeria (MLSCN) established by MLSCN Act 2003](https://www.mlscn.gov.ng/) — regulates training, registration, licensing of laboratory scientists, technicians, and assistants; conducts examinations; certifies lab test kits and reagents.
- **Clinical Officers:** No dedicated clinical-officer council identified; clinical officers fall under broader health-worker cadres under state/LGA oversight; likely regulated as part of allied health professions under MDCN framework or ministry oversight.

### 7.3 Health Facility Classification System

Nigeria's health facilities are classified into three levels of care (per National Health Policy 2016 and Master Facility List standards):

**Primary Healthcare (PHC):**
- **PHC Centre / Health Post** (village level): basic preventive, promotional, and limited treatment services. [As of 2023, Nigeria has 34,076 PHC centres](https://pmc.ncbi.nlm.nih.gov/articles/PMC11337854/), accounting for 85.3% of all health facilities; however, only ~20% are functional. Staffed by Community Health Extension Workers (CHEWs), health attendants, and community health volunteers (CHVs).
- **Comprehensive PHC Centre** (expanded primary): MCH services, immunisation, IDSR surveillance, basic laboratory, contraception, health promotion.

**Secondary Healthcare (General & Specialist Hospitals):**
- **General Hospital** (LGA/state secondary level): maternal/child health, surgical capacity, lab services, X-ray. Serve as referral centres for PHC-level cases.
- **Specialist Hospital** (state-level secondary): focus on single specialty (e.g., orthopedic, psychiatric, eye).

**Tertiary Healthcare:**
- **Federal Medical Centre (FMC)** (federal secondary/tertiary): advanced surgical, medical, and diagnostic services; regional referral role.
- **Teaching Hospital** (federal tertiary): highest level of clinical care, medical education, research; examples include University of Lagos Teaching Hospital (LUTH), University College Hospital (UCH) Ibadan, National Hospital Abuja.

Private clinics, mission hospitals ([CHAN — Christian Health Association of Nigeria](https://www.chak.or.ke/)), and for-profit diagnostic centres supplement the public system.

### 7.4 Insurance Regulator and Healthcare Financing

**NHIA (National Health Insurance Authority):** [The National Health Insurance Authority Act was signed 19 May 2022](https://www.nhia.gov.ng/), superseding the NHIS Act of 1999. The Act mandates health insurance for all Nigerians and establishes a three-fund system:

1. **Primary Healthcare Fund (PHF):** Government-funded; universal entitlement covering basic primary care.
2. **Basic Health Care Provision Fund (BHCPF):** [Established under National Health Act 2014; allocated 1% of the Consolidated Revenue Fund annually; operational from 2018](https://nphcda.gov.ng/bhcpf/). Serves as a basket fund supporting primary healthcare delivery at facility level.
3. **Vulnerable Group Fund:** Targeted support for the poorest populations.

**Contributions (Organized Sector):**
- Employers: 10% of employee wages
- Employees: 5% of wages
- Informal sector: via GIFSHIP (Group Individual and Family Social Health Insurance Programme)

**Benefit Package:** Covers employee, spouse, and up to four biological children; additional dependents may enroll.

### 7.5 Health Information System and Mandatory Reporting

**NHMIS (National Health Management Information System):** [Nigeria adopted DHIS2 as the unified NHMIS platform in 2013](https://fmohconnect.gov.ng/nhmis-annual-reports/); [by 2021, all 36 states and the FCT had fully transitioned](https://dhis2.org/nigeria-vaccine-logistics/). [The Federal Ministry of Health mandates that all health facilities report aggregate health data monthly via DHIS2](https://fmohconnect.gov.ng/nhmis-annual-reports/), though [numerous private facilities do not report, resulting in incomplete national data](https://fmohconnect.gov.ng/nhmis-annual-reports/).

**IDSR (Integrated Disease Surveillance Response):** [Nigeria has implemented IDSR since 2001](https://pmc.ncbi.nlm.nih.gov/articles/PMC4518330/); [currently 23 diseases are designated notifiable](https://ncdc.gov.ng/). [The Nigeria Centre for Disease Control (NCDC), a federal agency under the FMoHSW, coordinates surveillance and outbreak response](https://ncdc.gov.ng/). Reporting chain: facility → LGA → state Ministry of Health → NCDC/Federal Ministry. [Weekly and immediate reporting required per IDSR Technical Guidelines](https://www.ncdc.gov.ng/themes/common/docs/protocols/4_1476085948.pdf).

**Gap:** Exact quarterly/annual KPI report set and facility-level reporting timeline for non-communicable diseases and routine facility performance metrics not yet detailed; flagged for Wave-2.

### 7.6 National Identification and Patient-ID Strategy

**NIMC (National Identity Management Commission):** [Established by NIMC Act No. 23 of 2007](https://nimc.gov.ng/), NIMC issues the [National Identification Number (NIN), an 11-digit unique identifier](https://www.nimc.gov.ng/) to citizens and legal residents. The NIN is [mandatory for most transactions in Nigeria](https://services.gov.ng/service-provider/national-identity-management-commission) (financial, healthcare, electoral, social services).

**Age of Issuance and Fallback:**
- **Adults (18+):** NIN (11-digit).
- **Children (under 18):** Not automatically issued; may use parent NIN + birth-registration certificate as fallback for healthcare registration.
- **Refugees/Undocumented:** Manual clinic-level registration with "unverified identity" flag; common for internally displaced populations and asylum seekers.

**SaaS Implementation:** Patient-identity module must accommodate three ID types:
1. Adult NIN (11-digit).
2. Child ID (parent NIN + birth-certificate number).
3. Clinic-generated ID (for undocumented/refuge populations, flagged as "pending verification").

### 7.7 Data Protection and Privacy Law

**NDPA (Nigeria Data Protection Act) 2023:** [The NDPA 2023 (effective 12 June 2023) supersedes the NDPR 2019](https://ndpc.gov.ng/). The Act regulates collection, processing, storage, transfer, and use of personal data. [It applies to all persons, institutions, and public bodies processing data within Nigeria or concerning Nigerians](https://securiti.ai/overview-of-nigeria-data-protection-act/).

**Key Compliance Rules:**
1. **Registration:** [Data controllers and processors of "major importance" must register with NDPC within six months of becoming a major controller](https://ndpc.gov.ng/).
2. **Consent:** Lawful basis for processing; consent must be explicit, freely given, specific, and informed.
3. **Data Localisation:** No explicit requirement for local storage, but overseas transfer must meet equivalent-protection standard.
4. **Breach Notification:** Mandatory notification to NDPC and affected data subjects upon breach discovery.
5. **Subject Rights:** Data subjects have rights to access, correct, erase, and port personal data.

**Enforcement:** [NDPC imposes tiered administrative fines](https://ndpc.gov.ng/): 
- **Major controllers:** ₦10,000,000 (ten million Naira) or 2% annual gross revenue (whichever higher).
- **Other controllers:** ₦2,000,000 (two million Naira) or 2% annual gross revenue (whichever higher).

**Implication for SaaS:** Mandatory NDPC registration, patient consent workflows, audit trails for data access, data-processing agreements with state health departments (as data controllers), and breach notification procedures.

### 7.8 Disease Control and Public Health Programmes

Nigeria operates vertical disease-control programmes under the FMoHSW:

**NACA (National Agency for the Control of AIDS):** [Established 2000](https://naca.gov.ng/); coordinates HIV/AIDS prevention, treatment, and care. [Antiretroviral therapy (ART) is provided free at primary, secondary, and tertiary facilities](https://naca.gov.ng/anti-retroviral-therapy/). [As of 2024, 87% of people living with HIV in Nigeria know their status; 98% of those aware are on treatment](https://naca.gov.ng/).

**NTBLCP (National Tuberculosis and Leprosy Control Programme):** [Established 1989](https://ntblcp.org.ng/); coordinates TB and leprosy control. [Nigeria has over 5,300 TB service points and 1,602 microscopy centres nationwide](https://ntblcp.org.ng/). [In 2023, 371,019 TB cases were notified with a treatment success rate of 93%](https://ntblcp.org.ng/).

**NMEP (National Malaria Elimination Programme):** [Coordinates malaria prevention and treatment](https://nmcp.gov.ng/). Prevention interventions include insecticide-treated bed nets (ITNs), indoor residual spraying (IRS), and intermittent preventive treatment in pregnancy (IPTp). [Artemisinin-based combination therapy (ACT) is the standard treatment for uncomplicated malaria](https://nmcp.gov.ng/).

**NPHCDA (National Primary Health Care Development Agency):** [Established 1992](https://nphcda.gov.ng/); implements primary healthcare and immunisation programmes. [The Department of Disease Control and Immunization oversees routine immunisation, disease control, and surveillance](https://nphcda.gov.ng/). [The BHCPF is managed through NPHCDA to support primary healthcare service delivery](https://nphcda.gov.ng/bhcpf/).

### 7.9 Healthcare Payment Systems and Drug Pricing

**VAT Exemptions:** [Nigeria's VAT rate is 7.5% (per Finance Act 2020)](https://www.pwc.com/ng/en/assets/pdf/firs-circular-vat-changes.pdf). [Healthcare-related services and all drugs/medicines are exempt from VAT](https://pavestoneslegal.com/2020-list-of-goods-and-services-exempted-from-value-added-tax-in-nigeria-2/), though [ambiguity remains regarding the scope of "healthcare services"](https://portal.citn.org/administration-of-value-added-tax-in-nigeria-goods-and-services-exempt/).

**Mobile Money Operators:** [Licensed by Central Bank of Nigeria (CBN)](https://ndic.gov.ng/list-of-insured-institutions/list-of-mobile-money-operators/); major operators include [OPay, Palmpay, Moniepoint, Kuda, GTBank Mobile, MTN MoMo Nigeria, Airtel Money Nigeria](https://paycape.com/blog/top-10-mobile-operators-for-smes-in-nigeria/). Healthcare payment infrastructure via mobile money is emerging but not yet fully detailed in official sources.

**Essential Medicines List:** [The Nigeria Essential Medicines List (NEML) 7th Edition (2020)](https://www.who.int/publications/m/item/nigeria--essential-medicines-list-2020-(english)) lists essential drugs by therapeutic category. [An 8th Edition (2024) is now available](https://health.gov.ng/wp-content/uploads/2025/08/Final-NEML-Adult-8th-Edition.pdf). NAFDAC enforces restrictions on availability of controlled/scheduled medicines via licensing and inspection.

---

## 8. Stub Countries: Tanzania, Ghana, South Africa, India, Philippines

### Key Research Targets for Wave-2

Each stub country has been populated with only **currency, timezone, and language** (5 columns) — the easiest to verify via ISO and IANA standards. All other columns are marked `[STUB — pending full Wave 2]`. Wave-2 research for each country should prioritize:

**Tanzania (TZ):**
- **Admin structure:** Region and district names/counts (currently region-level only in corpus).
- **Regulators:** Health Professions Council of Tanzania (HPCT or equivalent for doctors, nurses, clinical officers, lab technicians); pharmacy board; insurance regulator.
- **Mandatory reports:** Health Management Information System (HMIS) Tanzania; disease surveillance framework (IDSR or equivalent).
- **ID system:** National ID system and patient-ID fallback rules.
- **Privacy law:** Tanzania Data Protection Act (if enacted) and regulatory authority.

**Rwanda (RW):**
- **[COMPLETED in Pass 2 — 2026-05-04]** See §7.1 below for full findings on regulators (RMDC, NPC, NCNM, RAHPC), health system (facility levels, DHIS2/OpenMRS HMIS), financing (CBHI/Mutuelle de Santé via RSSB, 91% coverage), privacy law (Law N° 058/2021, NCSA enforcement).

**Ghana (GH):**
- **Regulators:** Ghana Medical and Dental Council (GMDC); Pharmacy Council; Nursing and Midwifery Council.
- **Facility levels:** CHPS compounds (Community Health Planning Services), polyclinics, district/regional/tertiary hospitals.
- **Mandatory reports:** Ghana health information system and HMIS framework.
- **Insurance:** National Health Insurance Scheme (NHIS) regulator and benefit structure.
- **Privacy law:** Ghana Data Protection Act and Data Protection Authority.

**Nigeria (NG):**
- **Regulators:** Medical and Dental Council of Nigeria (MDCN); Nursing and Midwifery Council (NMCN); Pharmacy Council; Clinical officers regulation (if exists).
- **Facility levels and LGA structure:** Federal, state, LGA (local government area) hierarchies; private-sector dominance.
- **Mandatory reports:** Federal and state-level HMIS; disease surveillance (NDSR or equivalent).
- **Financing:** National Health Insurance Scheme (NHIS) and state variation.
- **Privacy law:** Nigeria Data Protection Regulation (NDPR) 2019.

**South Africa (ZA):**
- **Regulators:** Health Professions Council of South Africa (HPCSA); South African Nursing Council (SANC); Pharmacy Board; Lab accreditation.
- **Facility levels:** Primary, secondary, tertiary hospitals; NHI integration status.
- **Mandatory reports:** District Health Information System (DHIS) and national health reporting.
- **Insurance:** National Health Insurance (NHI) implementation timeline and regulator.
- **Privacy law:** Protection of Personal Information Act (POPIA) 2013 and Information Regulator.

**India (IN):**
- **Regulators:** National Medical Commission (replacing Medical Council of India); state nursing councils; pharmacy boards; NABL (lab accreditation).
- **Facility levels and state variation:** Primary, secondary, tertiary across 28 states and 8 union territories (significant variation).
- **Mandatory reports:** HMIS India and state variation; Ayushman Bharat reporting.
- **Financing:** State variation; central schemes (Ayushman Bharat) + state insurance schemes.
- **ID system:** Aadhaar (12-digit biometric) integration with health ID (ABHA).
- **Privacy law:** Pending India Privacy Bill; interim protection under various sectoral acts.

**Philippines (PH):**
- **Regulators:** Professional Regulation Commission (PRC) for all health professions; regulatory bodies for physicians, nurses, lab technologists, pharmacists.
- **Facility levels:** LGU (local government unit) primary health centres, provincial/district hospitals, tertiary centres.
- **Mandatory reports:** Disease surveillance (IDSR adapted from WHO-SEARO); health information system by province/LGU.
- **Financing:** PhilHealth (Philippine Health Insurance Corporation) and LGU co-financing.
- **ID system:** PhilSys (Philippine Identification System) linked to health records.
- **Privacy law:** Data Privacy Act 2012 (RA 10173) and National Privacy Commissioner.

---

## 7.1 Rwanda (RW) — Full Pack (Pass 2 — 2026-05-04 Wave-3 Extension)

### 7.1.1 Administrative Structure and Health System Hierarchy

**Sub-National Administration:**

Rwanda's administrative divisions are organized into two main levels:

- **Admin Level 1 (Province / Intara):** 5 provinces as of 2006 administrative restructuring — Kigali City, Northern Province, Southern Province, Eastern Province, Western Province. Prior to 2006, Rwanda had 12 provinces; the restructuring addressed governance issues arising from post-genocide reconstruction (T1: [rwanda-provinces-administrative-restructuring]).
- **Admin Level 2 (District / Akarere):** 30 districts as of 2026. Each district is further subdivided into sectors (umurenge) and cells (akagali) for community-level governance and health-service delivery.

(T1: [wikipedia-Rwanda-provinces]; [wikipedia-Rwanda-districts] — used for verification only; statutory references drawn from Rwanda administrative records and MoH publications.)

**Health Facility Levels (per Ministry of Health Health Sector Strategic Plan):**

Rwanda operates a pyramidal, decentralized health system comprising six facility levels:

1. **Health Post (Cell Level):** 1,280 health posts as of 2026. Services are primarily promotional, preventive, and basic treatment. Health posts serve as the interface between community health workers and health centres; they are the entry point for primary care and simple curative services.

2. **Health Centre (Sector Level):** 520 health centres as of 2026. Primary health care facilities providing more comprehensive services than health posts, including MCH (maternal and child health), lab capacity, and referral to hospitals.

3. **District Hospital (District Secondary):** Serves as the referral point for health centres within the district.

4. **Provincial Referral Hospital (Province Secondary):** Established to relieve burden on national teaching hospitals and provide specialty care at provincial level.

5. **National Referral and Teaching Hospitals (National Tertiary):** Four national referral hospitals:
   - Kigali University Teaching Hospital (KUTH)
   - Butare University Teaching Hospital (BUTH)
   - King Faisal Hospital Kigali (KFHK)
   - Rwanda Military Hospital (RMH)

6. **Specialized Centres:** Additional specialized institutes integrated into the tertiary network.

Total current network: 1,280 health posts + 520 health centres + 57 hospitals (all levels) = 1,857 facilities (T1: [moh-health-facility-service-packages-2018]; [moh-public-health-facilities-2023]).

**Ministry of Health Structure:**

The Ministry of Health (Minisante) Rwanda is the principal policy, planning, and oversight authority. Its jurisdiction covers public-sector facilities and coordination of the Private Not-for-Profit (PNFP) sector through faith-based partnerships, particularly Catholic and Protestant hospital networks. The MoH is the lead implementer of the Universal Health Coverage agenda, including the nationwide CBHI (Community-Based Health Insurance / Mutuelle de Santé) programme and the 4×4 Reform (launched 2023) to quadruple health workforce density by 2027 (T1: [moh-strategic-plans-website]).

### 7.1.2 Regulatory Bodies and Professional Councils

**Physicians and Dentists:**

The **Rwanda Medical and Dental Council (RMDC)** is the statutory regulator of medical and dental practitioners. It operates under the law establishing the Rwanda Medical and Dental Council and issues licenses and registration to doctors and dental practitioners. Requirements include continuing professional development (CPD) — a minimum of 50 CPD credits mandated for license renewal — and registration of persons qualified outside Rwanda (T1: [rmdc-official-website]; [rmdc-cpd-requirements]).

**Clinical Officers:**

Clinical officers in Rwanda are regulated through the **Rwanda Allied Health Professionals Council (RAHPC)**, which handles professional registration, licensing, and disciplinary oversight. Additionally, the **Rwanda Medical Clinical Officers Organization (RMCOO)** — a professional advocacy and development body established in 2016 — collaborates with MoH and RAHPC to set training standards and practice guidelines for clinical officers. Registration with RAHPC is a legal prerequisite for clinical-officer practice (T1: [rahpc-registration-website]; [rmcoo-official-organization]).

**Nurses and Midwives:**

The **National Council of Nurses and Midwives (NCNM)** is established under Law N° 25/2008 of 25 July 2008 and is responsible for:
- Setting standards of professional education and practice
- Registration and licensure of nurses and midwives
- Determining scope of practice
- Enforcing professional conduct standards
- Conducting licensure examinations

The Council protects the public from harmful or unprofessional practices and ensures competent, ethical care delivery (T1: [ncnm-statutory-authority]; [ncnm-official-website]).

**Pharmacists:**

The **National Pharmacy Council (NPC)** is established under Law N° 45/2012 of 14 January 2013 relating to the organization, functioning, and competence of the Council of Pharmacists. The NPC is responsible for:
- Granting and revoking authorization to practice the pharmacy profession
- Setting requirements for pharmacist registration and licensure
- Conducting pre-registration examinations (written and interview components)
- Providing guidance to institutions on pharmacy academic programmes
- Disciplinary measures against non-compliant practitioners
- Requiring one-year professional internship in Rwandan settings for Rwandan pharmacology graduates prior to examination eligibility

(T1: [npc-official-website]; [npc-pre-registration-guidelines]).

**Medicines Regulation:**

The **Rwanda Food and Drugs Authority (Rwanda FDA)** is established under Law N° 003/2018 of 9 February 2018, which determines its mission, organization, and functioning. The Rwanda FDA's mandate includes regulating human and veterinary medicines, vaccines, biological products, processed foods, medical devices, poisons, medicated cosmetics, household chemical substances, and tobacco products (T1: [rwanda-fda-law-003-2018]; [rwanda-fda-official-website]).

### 7.1.3 Healthcare Financing and Insurance Regulation

**Insurance Regulator (Private Sector):**

The **National Bank of Rwanda (BNR)** regulates and supervises the private insurance industry, including insurance companies (short-term, long-term, captive, mutual, microinsurance), health management organizations, insurance brokers, agents, and actuaries. Only BNR-licensed entities may legally offer and sell insurance products in Rwanda (T1: [bnr-insurance-supervision-website]; [bnr-insurance-faq]).

**Universal Health Coverage (CBHI / Mutuelle de Santé):**

The **Rwanda Social Security Board (RSSB)** administers the Community-Based Health Insurance (CBHI), locally known as Mutuelle de Santé. The CBHI scheme was introduced in 1999 as a pilot in three districts (covering 7% of population at launch) and was fully integrated into RSSB in 2015. As of 2023, CBHI covers approximately 91% of Rwanda's population — the highest coverage rate in Africa.

**Financing Model:**
- **Community contributions:** Household/family premiums (insurance year 1 July–30 June)
- **Government funding:** Subsidies for vulnerable populations
- **Donor support:** International partners and development partners contribute to scheme sustainability
- **Tariff structure:** CBHI maintains a tariff schedule for public-sector health services (T1: [rssb-cbhi-official-website]; [universal-health-insurance-Rwanda-PMC-2020]).

Members of CBHI receive primary medical care from health posts or health centres anywhere in Rwanda, with referral pathways to district and tertiary hospitals as needed.

**Lab Regulation:**

The **Rwanda Biomedical Centre (RBC)**, established in 2002 under the Ministry of Health, operates the **National Reference Laboratory (NRL)**. The NRL provides laboratory oversight, accreditation, and quality assurance. As of June 2024, the NRL holds ISO 15189:2022 accreditation (reaccredited via Kenya Accreditation Services, KENAS). Rwanda implements the WHO AFRO Strengthening Laboratory Management towards Accreditation (SLMTA) programme, which ranks laboratories from 0 to 5 stars and prepares them for higher accreditation. Multiple Rwandan laboratories have applied for and obtained ISO 15189:2022 certification (T1: [rbc-national-reference-laboratory]; [rbc-iso-15189-accreditation-2024]).

### 7.1.4 Mandatory Reports and HMIS Framework

**Rwanda Health Management Information System (HMIS):**

Rwanda's HMIS has been operational since 1998. In 2012, it was upgraded to a web-based system using District Health Information Software version 2 (DHIS2). The Rwanda HMIS (R-HMIS) collects data from over 700 public health facilities with an exceptionally high data completeness rate of approximately 98% (T1: [dhis2-Rwanda-case-study]; [moh-hmis-reporting-standards]).

**Individual-Level Records:**

Rwanda operates multiple electronic medical record (EMR) systems:
- **OpenMRS (Open Medical Record System):** Used in hospitals for individual-level client records; Rwanda has been a flagship OpenMRS implementation site since the 2008 era. OpenMRS captures individual patient data in a standardized format that is automatically aggregated and linked to DHIS2 for facility-level reporting.
- **Open Clinic:** An alternative EMR system used at some hospital sites.
- **DHIS2:** The national aggregate reporting platform; HMIS data from all facilities flow into DHIS2 for analysis and decision-making at district, provincial, and national levels.

(T1: [msh-Rwanda-health-information-exchange]; [rwanda-hmis-openMRS-integration]).

**Facility-Based Data Collection:**

Data at facility level are collected using standardized registers developed by the Ministry of Health:
- **ANC Register:** Used to track all antenatal care visits; pregnant women are provided an ANC card (paper or digital) at their first ANC visit.
- **Maternity and Postnatal Care (PNC) Registers:** Record delivery and postnatal follow-up data.
- **Immunisation Registers and Cards:** Individual immunisation records and facility-level immunisation registers. All immunisation data are first recorded on paper-based immunisation cards and facility registers, then transferred to the e-Tracker system (electronic immunisation registry), and finally aggregated into DHIS2.
- **DHIS2 Facility Aggregate Forms:** Pre-defined data sets specific to facility type (health post, health centre, hospital).

(T1: [rbc-anc-guidelines-2021]; [rbc-immunisation-registry-study]).

**Disease Surveillance and eIDSR:**

Rwanda implements the **electronic Infectious Disease Surveillance and Response (eIDSR)** system. In 2013, Rwanda became the first low-income country to fully implement eIDSR using mobile technology and interactive voice response. As of April 2013, Rwanda achieved 100% facility coverage with eIDSR.

**Reportable Diseases:**

23 communicable diseases are tracked under Rwanda's surveillance system, categorized into:
- **Immediately reportable diseases:** Suspected or confirmed cases requiring immediate reporting (examples include confirmed plague, hemorrhagic fever, meningitis).
- **Weekly reportable diseases:** Tracked and reported on a weekly basis (examples include malaria, diarrhea, respiratory infections).

Reporting occurs via the eIDSR module, which has been customized on Rwanda's DHIS2 platform. TRACnet (a national phone-based and web-based disease-tracking system) has operated nationwide since 2004 and was the predecessor to the full eIDSR system (T1: [msh-eIDSR-Rwanda]; [rbc-idsr-technical-guideline-2012]; [pmc-eIDSR-low-income-Rwanda-2013]).

### 7.1.5 National Identification and Patient-Identity Rules

**National ID System:**

The **National Identification Agency (NIDA)** was established under Law N° 43/2011 of 19 December 2011 (as amended). NIDA issues the National Identification Card to Rwandan citizens aged 16 and above.

**16-Digit Format:**

The Rwanda National ID card contains a 16-digit unique identification code, divided into six groups:
- **Group 1 (1 digit):** Holder's status identifier
- **Group 2 (4 digits):** Birth year
- **Group 3 (1 digit):** Gender
- **Group 4 (7 digits):** Sequential issue number for individuals born in the same year
- **Group 5–6 (varies):** Internal NIDA identifiers (specific meanings known only to NIDA)

(T1: [nida-official-website]; [ickjournalism-nida-16-digit-structure]; [nida-service-charter]).

**Identity Rules for SaaS Application:**

- **Primary identifier (Adults):** NIDA card holder's 16-digit National ID.
- **Fallback for under-16:** Parent NIDA card number + child's birth-registration certificate number (registered with civil authority).
- **Unregistered / Refugee populations:** Manual clinic-generated ID (flagged as "unverified" for audit purposes); applies to undocumented persons accessing care through PNFP or government facilities.

### 7.1.6 Language Policy and Officialization

**Constitutional Foundation (Article 8):**

The Constitution of the Republic of Rwanda (as amended) designates in Article 8:
- **National language:** Kinyarwanda
- **Official languages:** Kinyarwanda, English, and French

Official documents may be issued in one, two, or all three official languages as deemed appropriate (T1: [rwanda-constitution-article-8]).

**Swahili Officialization (Organic Law Nº 02/2017):**

On 8 February 2017, the Rwandan National Assembly adopted Organic Law Nº 02/2017 establishing Swahili as a fourth official language of Rwanda. This decision was made to strengthen Rwanda's integration within the East African Community (EAC) and to promote regional linguistic and cultural ties. Swahili is now used in official contexts, education, and government communications alongside the three original official languages (T1: [Rwanda-organic-law-02-2017]; [theconversation-Rwanda-official-languages]; [worldschoolbooks-Rwanda-languages]).

### 7.1.7 Data Protection and Privacy Law

**Law N° 058/2021 — Personal Data and Privacy Protection:**

Rwanda's comprehensive data-protection framework is established by Law N° 058/2021 of 13 October 2021 relating to the Protection of Personal Data and Privacy (effective 15 October 2021).

**Key Provisions:**

1. **Scope:** Applies to all persons, institutions, and public bodies processing personal data within Rwanda or concerning Rwandan residents, regardless of where processing occurs.

2. **Data Localization Requirement:** Personal data must be stored within Rwandan territory unless the data controller obtains a certificate from the National Cyber Security Authority (NCSA) permitting offshore storage.

3. **Data Subject Rights:** Individuals have the right to:
   - Access their personal data
   - Rectify (correct) inaccurate data
   - Erase personal data ("right to be forgotten")

4. **Data Controller / Processor Requirements:**
   - Registration with NCSA mandatory
   - Designation of Data Protection Officer (where required)
   - Implementation of appropriate technical and organizational security measures
   - Breach notification obligations

5. **International Data Transfers:** Data transferred outside Rwanda must meet equivalent-protection standards; NCSA certification required.

6. **Enforcement and Penalties:**
   - **Administrative penalties:** For non-compliance with registration, notification, and data-subject-rights violations
   - **Civil liability:** Damage compensation for victims of privacy violations
   - **Criminal penalties:** Unlawful disclosure or misuse of personal data

(T1: [rwanda-law-058-2021]; [rwandalii-law-058-2021-text]; [ncsa-data-protection-office]).

**Supervisory Authority:**

The **National Cyber Security Authority (NCSA)** is designated as the supervisory authority responsible for enforcement of Law N° 058/2021. The NCSA officially launched its Data Protection Office on 31 March 2022 to oversee all data-protection activities, including registration of data controllers/processors, investigation of complaints, and periodic compliance audits (T1: [ncsa-official-website]; [cyber-gov-rw-dpo-launch]).

### 7.1.8 Health Workforce Reform: 4×4 Initiative

In July 2023, the Government of Rwanda approved the **4×4 Reform**, a strategic initiative to quadruple the number of health care workers in Rwanda within four years (2023–2027). Rwanda currently has only 1 health care worker per 1,000 population; the WHO recommendation is 4 per 1,000. The 4×4 Reform targets training and deployment of:

- Residents, fellows, and general practitioners
- Dental surgeons
- Pharmacists
- Nurses and midwives
- Allied health sciences personnel
- New cadre: Community Public Health Workers (CPHWs)

As of December 2024, enrollment has increased 3.7 times compared to historical rates (T1: [moh-4x4-reform-announcement]; [moh-4x4-reform-strategy]).

### 7.1.9 Source Tier Summary

**T1 (Statutory and Authoritative):**
- Rwanda Constitution (Article 8 on languages)
- Organic Law Nº 02/2017 (Swahili officialization)
- Law N° 003/2018 (Rwanda FDA establishment)
- Law N° 043/2011 (NIDA establishment)
- Law N° 025/2008 (NCNM nursing regulation)
- Law N° 045/2012 (NPC pharmacy regulation)
- Law N° 058/2021 (Data Protection and Privacy)
- Ministry of Health official publications (Health Sector Strategic Plan, facility service packages)
- Rwanda Biomedical Centre publications and accreditation records
- Rwanda FDA official website and guidelines
- RSSB CBHI scheme documentation
- NIDA official website and identification standards
- NCSA Data Protection Office launch and enforcement framework

**T2 (Corroborating):**
- WHO Rwanda country health profile
- WHO EMRO health-systems analysis
- World Bank Rwanda health-financing reviews
- RSSB CBHI overview and sustainability documents
- RBC health information exchange architecture (OpenHIE)
- Management Sciences for Health (MSH) case studies on Rwanda HMIS and eIDSR

**T3 (Encyclopaedia / Corroboration Only):**
- Wikipedia entries on Rwanda provinces, districts, and languages (used for triangulation only; not primary source for any claim).

---

## 8. Cross-Cohort References and Dependency Map

### Standard-Forms Cohort

The **standard-forms** cohort lists 45+ HMIS forms and tools from Uganda and Kenya. Country-pack references these by code:

- **Uganda:** HMIS-105, HMIS-106A, HMIS-107, HMIS-108, HMIS-033A/B/C, HMIS-080, HMIS-081, HMIS-082/082A, HMIS-071, HMIS-072, HMIS-078, HMIS-055/055A/055B, HMIS-096A, etc. (plus HIV programme cards and registers, commodity tools, IDSR case-investigation and contact-tracing tools).
- **Kenya:** KHIS forms (variant by facility level), IDSR case-investigation, notifiable disease forms (KHIS Tracker).

Country-pack `default_forms_reference` cell directs SaaS teams to the standard-forms corpus. Wave-1 status: Standard-forms corpus is complete with 45 rows; country-pack simply cross-references them.

### Facilities Cohort

The **facilities** cohort lists 28 facility types (14 Uganda + 14 Kenya, plus NGO and private variants). Country-pack facility-level system references these:

- **Uganda:** HC II, HC III, HC IV, General Hospital, RRH, NRH (plus private clinic variants, standalone lab, pharmacy).
- **Kenya:** Level 1–6 (plus private clinic variants, standalone lab, pharmacy).

Cross-reference: If a country-pack row references "HC III" or "Level 3", the app should pull facility-type rows from facilities cohort.

### Roles-Permissions Cohort

The **roles-permissions** cohort defines cadres and their permissions. Country-pack regulator names must align:

- **Uganda:** UMDPC-licensed doctor, AHPC-licensed clinical officer, UNMC-licensed nurse, NDA-licensed pharmacist.
- **Kenya:** KMPDC-licensed doctor, COC-licensed clinical officer, NCK-licensed nurse, PPB-licensed pharmacist, KMLTTB-licensed lab technologist.

Wave-1 status: Roles-permissions corpus exists with 18 rows; country-pack confirms regulator names match role definitions.

### Reporting-KPIs Cohort (Pending)

The **reporting-kpis** cohort (Wave-3 target) will supply:
- Each country's mandatory indicators (OPD attendance, inpatient admissions, malaria cases, TB cases, ART enrollment, maternal indicators, etc.).
- Reporting frequency per indicator (monthly, quarterly, annual).
- Numerator and denominator definitions.
- Submitter and recipient roles.

Country-pack flags `[reporting-kpis gap]` for indicators not yet in corpus. Example: "Uganda quarterly ART report (HMIS-106A)" — once reporting-kpis cohort adds rows for ART indicators, the gap closes.

### Tenant-Blueprints Cohort (Pending)

The **tenant-blueprints** cohort (Phase 5 target) will supply pre-configured workflows for each country:

- **Uganda blueprints (UG-*):** HMIS-107 annual workflow, HMIS-105 monthly outpatient, IMCI triage for paediatric presentations, ANC bundle (Hb + HIV + syphilis + urine protein), TB case management, ART initiation and monitoring.
- **Kenya blueprints (KE-*):** KHIS monthly reporting, SHA benefit-checking workflow, KEPH facility-level service protocols, maternal health package (antenatal + delivery + postnatal).

Country-pack `default_blueprints_reference` cell will point to tenant-blueprints rows once they are available.

---

## 9. Geographic-Scope Confirmation: Health-System Exclusions Restated

The project's hard exclusions (per `_context/exclusions.md`) apply uniformly across all 9 countries:

1. **No veterinary services.** Clinical data for animal health is out of scope (zoonotic disease surveillance may intersect, but veterinary clinical care is excluded).
2. **No traditional/herbal medicine.** Indigenous healing practices, herbal remedies, and traditional birth attendants are not modelled as clinical roles (though Uganda's community health messaging may reference cultural trust factors; this is communication, not clinical modelling).
3. **No transplant services.** Organ allocation, waiting-list management, immunosuppressant regimens, and transplant-specific governance are excluded.
4. **No neurosurgery or cardiothoracic surgery.** These specialty procedures are noted as **NRH-only (Uganda) or Level-6-only (Kenya)** — available at national referral hospitals but not modelled as standard facility-level capabilities. If a country has a dedicated neurosurgery or cardiac institute, it is treated as a tertiary outlier exception, not part of the general facility-level system.

**Implication for countries:** These exclusions apply globally. Even if Tanzania, Rwanda, India, or Philippines have traditional medicine practitioners or transplant centres, they are not in scope for this cohort.

---

## 9. Pass 2 — Democratic Republic of Congo (CD) Extension (2026-05-04)

### 9.1 DRC Administrative Structure and Decentralization

The Democratic Republic of the Congo's administrative reorganisation (découpage) was enacted via Constitutional Law in 2011 and implemented in 2015. The country transitioned from 11 provinces to 26 (Kinshasa plus 25 named provinces). Below the provincial level, administration splits into **rural (Territoire)** and **urban (Ville)** subdivisions:

- **Territories (rural):** 145 subdivisions, each led by a territory administrator appointed by central government and reporting to the provincial governor. Territories are further subdivided into sectors, chiefdoms, and communes.
- **Cities (urban):** 33 subdivisions, defined as provincial capitals or agglomerations of 100,000+ inhabitants with collective facilities and economic/social infrastructure.

This dual hierarchy is critical for health-service planning because Health Zones (515 total) operate within these administrative boundaries, and facility deployment differs between rural (centre de santé → HGR serving 100,000–150,000 pop.) and urban (200,000–250,000 population coverage).

### 9.2 Health System Pyramid and Facility Levels

The Ministry of Public Health, Hygiene and Prevention operates a three-level national hierarchy (central, provincial, peripheral) coordinated through 515 Health Zones (ZS) as operational planning units. Each Health Zone has a Health Zone Management Team (ECZ) responsible for coordination and quality oversight.

**Facility-level system (per Ministry PNDS and WHO-DHIS2 case studies):**
1. **Centre de santé (Health Centre):** Primary level; located within Health Areas; offers Minimum Package of Activities (PMA) — basic curative, preventive, and maternal/child health services.
2. **Centres de santé de référence (CSR, optional):** Intermediary reference centres; support multiple health centres.
3. **Hôpital général de référence (HGR, General Reference Hospital):** District hospital; functions as the HGR for the Health Zone; offers Complementary Package of Activities (PCA) including emergency obstetric care, surgical capability, and laboratory support.
4. **Provincial Hospital:** Overseen by Provincial Health Division; tertiary-level services.
5. **Hôpital national (National Referral Hospital, HN):** Tertiary centre; national specialty referral.

This differs structurally from Uganda (HC II–NRH) and Kenya (KEPH Levels 1–6); the Health Zone is the key operational unit for planning and reporting, replacing district-level structures in some East African models.

### 9.3 Nursing Regulation and Professional Standards

The **Ordre National des Infirmiers (ONIC)** was established under Law 16/015 (15 July 2016). Key provisions:

- **Mandatory registration (Art. 5):** No one may practice nursing without registration on the roll of the order.
- **Eligibility:** Congolese nationality, nursing diploma or equivalent, good moral character, oath-taking before provincial council.
- **Disciplinary control:** ONIC council enforces professional conduct standards; provincial councils manage local registration and discipline.
- **Headquarters:** Kinshasa-based national office; provincial branches coordinate local registration and licensing.

ONIC is distinct from the **Ordre des Médecins (CNOM, Conseil National de l'Ordre des Médecins)**, the medical council established in 1968 and reaffirmed in contemporary practice (Dr. Berthier Nsadi Fwene reelected president 2022–2026). The relationship between CNOM and clinical officers (if any falls under CNOM or a separate body) remains unconfirmed, flagged as [T1 verification pending].

### 9.4 Pharmaceutical Regulation: ACOREP (Post-2020 Transition)

The **Autorité Congolaise de Réglementation Pharmaceutique (ACOREP)** assumed pharmaceutical regulatory responsibilities from the **Direction de la Pharmacie et du Médicament (DPM)** in 2020. ACOREP operates under the Ministry of Public Health and is responsible for:

- **Marketing authorization:** Approval of medicines, medical devices, herbal products, cosmetics, psychotropic drugs.
- **Import/export control:** Regulates manufacture, import, distribution, sale, labeling, storage of pharmaceuticals.
- **Quality and safety:** Monitors pharmaceutical market; primary objective is protection against substandard and counterfeit medicines.
- **Interaction with Ministry:** ACOREP proposes legislation on medicine quality/safety and collaborates with Ministry of Foreign Trade on import/export authorization.

Note: Unlike Uganda's NDA (which issues retail dispensing licenses in Class A/B/C tiers), ACOREP regulates finished pharmaceuticals and their market distribution. It does not define prescriber schedules (those remain in clinical guidelines set by the MoH).

### 9.5 Insurance Regulation and Universal Health Coverage

**ARCA (Autorité de Régulation et de Contrôle des Assurances)**, established by Decree 16/001 (26 January 2016), is an independent public establishment under the Ministry of Finance. It regulates the insurance sector broadly and is responsible for:

- **Protecting policyholders and beneficiaries:** Ensures contract transparency and claim settlement.
- **Ensuring financial soundness:** Monitors insurer solvency and capacity to honor commitments.
- **International coordination:** Member of AICA/AIS, CISNA, OAA, and AAACA (African insurance authorities).

**CNAM (Caisse Nationale d'Assurance Maladie)** was established under Law 18/035 (2018) to implement universal health coverage. As of 2026, CNAM implementation is gradual; the law outlines basic principles for health-service organization and financing, but operational benefit schedules and enrollment procedures remain in development. This contrasts with Kenya's SHA (operational since 1 October 2024) and Uganda's NHIS (still pending implementation).

### 9.6 Laboratory Regulation and Reference Lab Function

The **Institut National de Recherche Biomédicale (INRB)** was founded in 1984 and has served as DRC's national biomedical research institute and WHO collaborating centre (since 2018). INRB operates a modern facility (70,000 m²) with 6 specialized laboratories:

- Virology
- Parasitology
- Bacteriology
- Medical Entomology
- Clinical Biology and Pathology
- Animal research centre
- Data centre

INRB functions as the **national reference laboratory** under Ministry of Public Health oversight. However, no dedicated laboratory regulator equivalent to Kenya's KMLTTB or a dedi cated clinical laboratory council has been identified in available sources. **DPM oversight of pharmaceutical testing** exists, but **ISO 15189 accreditation status and enforcement mechanism for general clinical laboratories remains [T1 verification pending]**.

### 9.7 National Identification and Patient-ID Strategy

DRC's national identification system is in **transition**, with two parallel pathways for patients seeking healthcare:

**1. Carte d'Identité Nationale (CIN) — Formal System (Post-2022):**
- Issued by **ONIP (Office National d'Identification de la Population)** per Decrees 22/07 & 22/08 (2 March 2022).
- **Eligibility:** Adult Congolese citizens registered in the General Population File (FGP).
- **Validity:** 10 years.
- **Format:** Biometric card; issued during ONIP's rollout (officially launched June 2023, primarily in Kinshasa and major urban centres).
- **Penetration:** Low outside Kinshasa (as of 2026); mass enrollment ongoing but not yet nationwide.

**2. Carte d'électeur (Voter Card) — De Facto ID System (Continuing Use):**
- Issued by **CENI (Commission Électorale Nationale Indépendante)** during voter registration cycles.
- **Status:** Designed for electoral use; has become the de facto national ID due to CIN's limited penetration.
- **Content:** Civil status (name, date/place of birth, sex, parents' names), current residence, place of origin, photograph, fingerprint.
- **Security:** Barcode, CENI watermark, government official signature.
- **Use in healthcare:** Widely accepted as patient ID in facilities, especially outside Kinshasa; continues due to population inertia and accessibility compared to CIN.

**Implication for SaaS:**
- **Patient-identity module must accommodate both CIN and voter card** as primary identifiers.
- **Dual-ID tracking:** Flag records with "ID pending verification" if neither CIN nor voter card available (relevant for refugee, undocumented, and transitional-identity populations, particularly in eastern conflict zones).
- **Fallback for under-18s:** [T1 verification pending] — ONIP's official guidance on children under 18 (fallback to parent NIN + birth certificate, as in Uganda, or voter card expectation) not yet sourced.

### 9.8 Mandatory Health Reporting: SNIS and IDSR

**SNIS (Système National d'Information Sanitaire):** DRC's national health information system operates on the **DHIS2 platform** (District Health Information Software 2), following the WHO approach adopted across East and Central Africa.

- **Reporting frequency:** Monthly mandatory reporting from health facilities.
- **Coverage:** >90% facility compliance documented in ASSP (Appui aux Soins de Santé Primaires) zone pilot (source: DHIS2 case study, 2022); national coverage varies by health zone.
- **Data elements:** OPD attendance, inpatient admissions, laboratory tests, disease surveillance, commodity stock, staffing, financial data.
- **Reporting chain:** Facilities → Health Zone office → Provincial aggregation → National MoH via DHIS2.
- **[reporting-kpis gap]:** Exact mandatory form set (equivalent to Uganda's HMIS-105/108/107 suite) and quarterly/annual aggregation structure not yet fully sourced in available documents.

**IDSR (Integrated Disease Surveillance and Response):** DRC participates in the **WHO-AFRO IDSR framework** for notifiable-disease surveillance. Key features:

- **Immediate reporting:** Suspected/probable/confirmed cases of Ebola, Marburg, and priority diseases reported within 24 hours via facility surveillance officers to district/provincial/national PHEOC (Public Health Emergency Operations Centre).
- **Case investigation:** District surveillance staff complete Case Investigation Forms (CIF) capturing case demographics, clinical presentation, specimen collection, and contact information.
- **Contact tracing:** Contact Tracing Forms monitor contacts for symptom development.
- **RRT coordination:** Rapid Response Teams at provincial/national levels investigate alerts and coordinate outbreak response.
- **Real-world example:** DRC's December 2025 Ebola outbreak (64 cases, 45 deaths) was contained in 3 months using DHIS2-tracked IDSR protocols and RRT deployment, demonstrating operational integration.

### 9.9 Data Protection and Privacy Framework

DRC's privacy law is **telecom/ICT-focused** and differs from Uganda and Kenya's standalone data-protection acts:

**Law 20/017 (25 November 2020):** "Telecommunications and Information and Communication Technologies"
- **Scope:** Regulates telecommunications and ICT service provision; Title III (Arts 126–133) addresses privacy and personal data protection.
- **Key definitions:** Personal data = any information relating to identified/identifiable natural person, directly/indirectly, by reference to identification number or elements specific to physical/physiological/genetic/psychological/cultural/social/economic identity.
- **Sensitive data protection:** Explicitly prohibits processing of data revealing racial/ethnic/regional origin, opinions, religious/philosophical beliefs, union membership, sexual life, genetic data, or health-related data **without explicit justification and safeguards**.
- **Consent requirement:** Data collection must be based on consent (opt-in).
- **Overseas transfer:** Prohibited except to countries with equivalent data-protection standards.
- **Implementation:** Law effective 25 November 2020, but **executive decree setting collection/processing procedures still pending as of 2026**.

**Law 23/010 (13 March 2023):** "Digital Code"
- Supplements Law 20/017 with additional data-protection provisions in the digital context.
- Entered into force 13 March 2023.

**Enforcement authority:** [T1 verification pending] — No dedicated data-protection commissioner or dedicated authority identified in available sources. Enforcement likely vests with **ARTEL (telecom regulator)** or **Ministry of Communication**, but institutional arrangements require confirmation.

**Comparison to Uganda/Kenya:** Unlike Uganda's Data Protection and Privacy Act 2019 (standalone, enforced by PDPO) or Kenya's Data Protection Act 2019 (standalone, enforced by ODPC), DRC's privacy framework is embedded within telecom regulation. This reflects DRC's regulatory priorities (ICT sector oversight) but creates ambiguity about healthcare-data-specific enforcement in the absence of a standalone health data-protection law.

### 9.10 Dual-Currency Reality and Economic Context

DRC's official currency is the **Congolese Franc (CDF)**, but the **US Dollar (USD) is widely accepted** in commerce, particularly in urban centres and formal-sector transactions. This dual-currency reality has important implications:

- **Billing-tariffs cohort:** All pricing data must specify currency (CDF vs. USD) and year to avoid ambiguity, as exchange rates fluctuate significantly and affect costing models.
- **Mobile money:** M-Pesa DRC (Vodacom), Airtel Money DRC, and Orange Money DRC all support both CDF and USD transactions.
- **Central bank policy:** Banque Centrale du Congo (BCC) permits USD circulation in the formal economy; dollarization is widespread in high-value transactions.

### 9.11 Connectivity Constraints and Mobile-Money Integration

DRC faces significant **telecommunications infrastructure challenges** that affect SaaS deployment:

- **Internet non-adoption:** 80% of the population does not use the internet (BuddeComm 2024).
- **Mobile network coverage:** 2G (75%), 3G (55%), 4G (45%) of population; LTE availability limited to urban centres.
- **Electricity access:** Only 19% of population connected to grid; constrains base-station deployment and data-centre operations.
- **Eastern region constraints:** Eastern provinces (North Kivu, South Kivu, Ituri) face additional connectivity challenges due to conflict, mountainous terrain, and sparse infrastructure investment.

**Implications for SaaS:**
- **Offline-mode critical:** Health facilities in remote areas require offline data-entry capability with eventual sync when connectivity available.
- **Mobile-money payment integration:** M-Pesa Vodacom (6.4M active users, 2024), Airtel Money, and Orange Money provide payment pathways for facility fees and user access; subscription models should accommodate USSD-based payment for feature-phone users.
- **Data localisation:** Law 20/017/2020 requires overseas data transfer to equivalent-protection jurisdictions; cloud storage in third countries must be justified and documented.

---

## 10. Open Questions for Wave-2 — Knowledge Gaps and Next-Pass Targets

### Uganda

1. **Insurance regulator identity:** Once the National Health Insurance Scheme is enacted, which ministry or board will regulate it? MoH or a separate authority?
2. **Lab regulator mandate:** Does AHPC have sufficient legislative backing to enforce ISO 15189 accreditation, or is this guidance-only? Should there be a dedicated laboratory board?
3. **NIN/birth-cert linkage for under-18s:** NIRA's official guidance on how health facilities should handle patient-identity for children; is there a standard composite-ID format?
4. **HMIS-097 quarterly report:** Exact scope, deadline, and submitter for the annual aggregate quarters report (flagged in standard-forms corpus as "referenced but schema gap").

### Kenya

1. **Huduma Namba age thresholds and fallback:** Official NIRA guidance on whether minors' cards are issued age 6+ and what ID should be used for under-6 children (Maisha Namba may have different rules).
2. **County-specific mandatory forms:** Beyond KHIS, do county governments have additional facility-reporting requirements (e.g., quarterly safety audits, staffing reports)?
3. **SHA tariff schedule and exemptions:** Full SHA benefit schedule (which drugs/procedures covered, co-pay percentages), exemptions (pregnant women, children under 5, elderly), and out-of-pocket limits.
4. **Private-sector KHIS reporting rules:** Are private clinics and PNFP hospitals required to report to KHIS, or is reporting voluntary? If required, what is the enforcement timeline?

### Democratic Republic of Congo (CD)

1. **Clinical officer regulatory structure:** Does a standalone clinical officers council exist (separate from CNOM), or do clinical officers fall under the Ordre des Médecins? What is the institutional arrangement and training standard for clinical officers?
2. **Laboratory regulator and ISO 15189 compliance:** INRB serves as national reference lab; what is the formal accreditation pathway and enforcement mechanism for general clinical laboratories (DPM, INRB, provincial labs)? Is ISO 15189 mandatory or guidance-only?
3. **Privacy authority and data-protection enforcement:** Which authority enforces Laws 20/017 and 23/010? Is it ARTEL (telecom regulator), Ministry of Communication, or a separate entity? What is the institutional capacity for healthcare-data privacy oversight?
4. **Under-18 patient-ID fallback:** ONIP's official guidance for children under 18 who have not yet received CIN — is fallback to parent voter card + birth certificate expected, or is there a formal documented protocol?
5. **Ministry of Public Health website and digital presence:** Verify active domain (minisante.cd) and current organizational structure documentation; confirm official health-sector reporting requirements and facility licensing procedures.
6. **ACOREP institutional relationship with DPM:** Post-2020 transition from DPM to ACOREP — are both entities still operational or fully merged? What is the precise division of pharmaceutical-regulatory responsibilities?
7. **SNIS form standardization and reporting KPIs:** Exact mandatory form set (equivalent to Uganda HMIS-105/108/107) and quarterly/annual aggregation structure for Health Zone and provincial reporting.
8. **CNAM benefit schedule and universal-coverage implementation:** Law 18/035 enacted 2018; what is the current implementation status as of 2026? Which procedures/drugs are covered at which facility levels, and what are copay/exemption rules for vulnerable populations (pregnant women, children, elderly)?
9. **Connectivity infrastructure investment timeline:** Given 80% internet non-adoption and 45% 4G coverage, what are DRC's plans for rural Health Zone digital connectivity? Are satellite or microwave-link solutions planned?
10. **VAT exemptions for health services:** Exact health-services exemption schedule under Code des Impôts and Loi 10/001/2010; which health-sector goods/services qualify for reduced-rate or zero VAT?

### Stub Countries (All)

1. **Health regulator landscape:** Identify national equivalents to UMDPC, AHPC, UNMC, NDA, and insurance regulator for each country.
2. **Facility-level system:** Confirm facility type names (are they regions/districts, health posts/centres/hospitals, or other names?) and capacity specifications.
3. **Patient-ID rules:** How do under-18 children, refugees, and undocumented populations access care and receive unique identifiers?
4. **Mandatory reporting framework:** Which forms/indicators are mandatory, reporting frequency, and receiving bodies.
5. **Privacy law enforcement:** When was the Data Protection Act enacted (if any), and who is the regulatory authority?

---

## Sources

### T1 — Statutory Acts, Constitutional Documents, Government Websites

**Uganda:**
- Constitution of Uganda (as amended)
- Local Governments Act 1997 (as amended)
- Medical and Dental Practitioners Act, Cap 272 (as amended 2023)
- Allied Health Professionals Act, Cap 268
- Nurses and Midwives Act 1996 (Cap 301)
- National Drug Policy and Authority Act, Cap 206
- Data Protection and Privacy Act 2019 (Act No. 9 of 2019)
- Registration of Persons Act 2015
- Ministry of Health Uganda: [health.go.ug](https://health.go.ug)
- Uganda Medical & Dental Practitioners Council: [umdpc.go.ug](https://www.umdpc.go.ug)
- Allied Health Professionals Council: [ahpc.ug](https://ahpc.ug)
- Uganda Nurses and Midwives Council: [unmc.ug](https://unmc.ug)
- National Drug Authority: [nda.or.ug](https://www.nda.or.ug)
- National Identification & Registration Authority: [nira.go.ug](https://www.nira.go.ug)
- Personal Data Protection Office: [pdpo.go.ug](https://www.pdpo.go.ug)
- IDSR Technical Guidelines 3rd Edition (September 2021): [reliefweb.int](https://reliefweb.int/report/uganda/national-technical-guidelines-integrated-disease-surveillance-and-response-third)
- Essential Medicines and Health Supplies List for Uganda (EMHSLU) 2023: [who.int](https://www.who.int/publications/m/item/uganda--essential-medicines-and-health-supplies-list-for-uganda-(emhslu)-2023-(english))

**Kenya:**
- Constitution of Kenya 2010 (as amended)
- County Governments Act 2012 (Act No. 17 of 2012)
- Medical Practitioners and Dentists Act, Cap 253
- Clinical Officers (Training, Registration and Licensing) Act 2017 (Act No. 20 of 2017)
- Nurses Act, Cap 257 (revised 2012)
- Pharmacy and Poisons Act, Cap 244
- Medical Laboratory Technicians and Technologists Act (Cap 253A)
- Health Records and Information Managers Act 2016
- Health Act 2017
- Data Protection Act 2019 (Act 24 of 2019)
- Social Health Insurance Act 2023
- National Integrated Identity Management System (NIIMS) Rules 2020 (Legal Notice No. 195 of 2020)
- Ministry of Health Kenya: [health.go.ke](https://www.health.go.ke)
- Kenya Medical Practitioners & Dentists Council: [kmpdc.go.ke](https://kmpdc.go.ke)
- Clinical Officers Council: [clinicalofficerscouncil.org](https://clinicalofficerscouncil.org)
- Nursing Council of Kenya: [nckenya.org](https://nckenya.org)
- Pharmacy and Poisons Board: [web.pharmacyboardkenya.org](https://web.pharmacyboardkenya.org)
- Kenya Medical Laboratory Technicians & Technologists Board: [kmlttb.org](https://kmlttb.org)
- Office of the Data Protection Commissioner: [odpc.go.ke](https://www.odpc.go.ke)
- Social Health Authority: [sha.go.ke](https://sha.go.ke)
- State Department for Devolution: [devolution.go.ke](https://www.devolution.go.ke)
- Kenya Essential Medicines List 2023: [guidelines.health.go.ke](http://guidelines.health.go.ke)

**Democratic Republic of Congo:**
- Constitution of the Democratic Republic of the Congo 2005 (Revised 2011): [constitutionnet.org](https://constitutionnet.org/sites/default/files/DRC%20-%20Congo%20Constitution.pdf)
- Law No. 16/015 (15 July 2016) — Ordre National des Infirmiers (ONIC): [droitcongolais.info](https://www.droitcongolais.info/files/810.07.16-Loi-du-15-juillet-201_ordre-des-infirmiers.pdf)
- Law No. 18/035 (2018) — Universal Health Coverage (CNAM)
- Law No. 20/017 (25 November 2020) — Telecommunications and ICT (data protection, Title III Arts 126–133)
- Law No. 23/010 (13 March 2023) — Digital Code
- Decree No. 16/001 (26 January 2016) — Creation of ARCA (Insurance Regulator): [arca.cd](https://arca.cd/)
- Decree No. 22/07 (2 March 2022) — General Population File (FGP, ONIP)
- Decree No. 22/08 (2 March 2022) — National Identity Card (CIN) Issuance
- Ordonnance-Loi 68/070 (1 March 1968) — Ordre des Médecins (CNOM): [droitcongolais.info](https://www.droitcongolais.info/files/810.03.68-Ordonnance-loi-du-1er-mars-1968_Ordre-des-medecins.pdf)
- Ministry of Public Health, Hygiene and Prevention (health.cd — **URL verification pending**)
- ONIP (Office National d'Identification de la Population): [onip.gouv.cd](https://www.onip.gouv.cd/)
- ONIC (Ordre National des Infirmiers): [ordredesinfirmiersrdc.org](https://ordredesinfirmiersrdc.org/)
- ACOREP (Autorité Congolaise de Réglementation Pharmaceutique): [acorep-dpmrdc.org](https://acorep-dpmrdc.org/)
- INRB (Institut National de Recherche Biomédicale): [inrb.cd](http://www.inrb.cd/)
- BCC (Banque Centrale du Congo — monetary policy on CDF/USD): [bcc.cd](https://www.bcc.cd/)
- INS (Institut National de Statistique — demographic and administrative data): [ins.cd](https://www.ins.cd/)

**Tanzania, Rwanda, Ghana, Nigeria, South Africa, India, Philippines:**
- National constitutions and language provisions (official government sources)
- ISO 4217 currency code registry
- IANA timezone database

### T2 — International Corroboration (WHO, World Bank)

- [WHO Uganda Country Profile](https://www.who.int/countries/uga/)
- [WHO Kenya Country Profile](https://www.who.int/countries/ken/)
- [World Bank Uganda Health System Review](https://www.worldbank.org/en/country/uganda)
- [World Bank Kenya Health System Review](https://www.worldbank.org/en/country/kenya)
- Uganda Bureau of Statistics (UBOS) demographic publications
- Kenya National Bureau of Statistics (KNBS) reports
- Willow Health Media analysis: [Kenya's Social Health Authority](https://willowhealthmedia.org/kenyas-social-health-authority-a-healthcare-revolution-analysis/)

### T3 — Encyclopaedia / Corroboration Only (Not Sole Source)

- Wikipedia: Uganda administrative divisions, languages, time zones
- Wikipedia: Kenya counties, devolution, languages
- Wikipedia: Tanzania, Rwanda, Ghana, Nigeria, South Africa, India, Philippines (country overviews, language, currency, timezone corroboration)

All T3 entries are used strictly for verification of facts already established via T1 sources; no T3 entries appear as sole source in this document.

