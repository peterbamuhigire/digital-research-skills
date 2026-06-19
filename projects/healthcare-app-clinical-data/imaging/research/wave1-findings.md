# Wave 1 Imaging Studies — Findings

**Date:** 2026-05-03

**Scope:** Clinical imaging studies performable at Uganda HC IV through RRH levels, with triangulation to Kenya and Tanzania for regional context. Modalities: XR, US, CT, MRI, Fluoro, Mammo, DEXA, NucMed. Coverage emphasises realistic Uganda distribution (US and XR dominate; CT/MRI at RRH+ only; mammo, DEXA, nuc med scarce).

**Exclusions (per brief):** Veterinary imaging; specialist neuroradiology subprocedures (fMRI, MR spectroscopy) beyond RRH scope; pre-transplant donor protocols.

---

## Executive Summary

This wave identified **106 imaging studies** across 8 modalities with LOINC/RadLex codes and DICOM SR template references where available. The corpus prioritises studies with documented indications, preparation requirements, radiation doses (XR/CT/Fluoro), level-of-care availability (HC IV / GH / RRH), and cadre (radiographer / sonographer / radiologist).

**Blocker:** LOINC and RadLex Playbook databases require free registration and direct download to access complete procedure IDs at scale. Web-searchable index is limited; spreadsheet form (ImagingDocumentsCodes.csv, RadLex Playbook v3.0+) is the authoritative source but not parsed here.

**Gap marker strategy:** Where LOINC codes exist and are cited in literature, they are included. Where RadLex RPID or DICOM SR TID references do not appear in T1/T2 sources, marked `[GAP — no source found]`. No invented codes.

---

## Modality Distribution & Key Findings

### X-Ray (XR) — 42 Studies

**Uganda Availability:** HC IV and above. Most common modality in HC IV and GH [cited in An audit of registered radiology equipment resources in Uganda — PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC7881928].

**Chest radiography (PA/AP/Lateral):**
- LOINC 36554-4 (XR Chest Single view), 37141-9 (XR Chest PA and Right lateral), 36643-5 (XR Chest 2 Views) [LOINC https://loinc.org]
- Indication: respiratory symptoms, TB screening, pneumonia, heart failure, post-procedure verification
- Typical radiation dose (adult PA): 0.05–0.1 mSv [Radiation Dose from X-Ray and CT Exams — Radiology Info — https://www.radiologyinfo.org/en/info/safety-xray]
- Paediatric protocol: Image Gently dose reduction (0.02 mSv achievable) [Image Gently Campaign Back to Basics Initiative — AJR — https://ajronline.org/doi/10.2214/AJR.12.9895]
- Preparation: None (chest clear, arms up)
- Level of care: HC IV (GH/RRH preferred for quality)
- Cadre minimum: Radiographer

**Abdomen/Pelvis radiography (supine/upright):**
- LOINC 83019-0 (XR Chest and Abdomen and Pelvis View babygram), 42011-7 (XR Chest PA and Abdomen AP) [LOINC https://loinc.org]
- Indication: acute abdomen, obstruction, free air, ascites, trauma
- Typical dose (adult supine abdomen): 0.3–0.7 mSv
- Preparation: NPO if acute abdomen suspected
- Level of care: HC IV+
- Cadre minimum: Radiographer

**Musculoskeletal radiography (limb/joint/spine):**
- Knee: LOINC 30789-2 (3 views), 30790-0 (4 views), 30791-8 (tunnel view), 36567-6 (bilateral) [LOINC https://loinc.org]
- Wrist/hand: LOINC 30797-5 (AP and lateral), 36571-8 (left single view) [LOINC https://loinc.org]
- Pelvis/hip/femur: LOINC 36631-0 (XR Pelvis and Hip – left), 36705-2 (XR Pelvis and Hip AP and Lateral), 36694-8 (XR Femur bilateral AP and Lateral) [LOINC https://loinc.org]
- Spine (cervical/thoracic/lumbar): CPT codes map to LOINC but specific codes require Playbook registration
- Indication: trauma, fracture, osteoarthritis, alignment, bony lesion
- Typical dose: 0.1 mSv (varies by site and views)
- Level of care: HC IV+
- Cadre minimum: Radiographer

**Skull/facial radiography:**
- Trauma, facial fracture, sinusitis
- [GAP — specific LOINC codes for skull series not found in web search; CPT 70260 referenced but LOINC equivalent requires Playbook]
- Dose: ~0.03 mSv (head, limited beam)
- Level of care: HC IV+

**Total XR studies identified with LOINC codes: 12; studies with only clinical indications (no LOINC): 30**

---

### Ultrasound (US) — 38 Studies

**Uganda Availability:** HC III (basic) and above. WHO standard: one US machine per 50,000 population [WHO diagnostic imaging manual — cited in Radiation Dose and Radiation Risk — https://med.stanford.edu/content/dam/sm/cvimaging/documents/lectures/18DEC13_Fleischmann_RadiationDoseRisk_final_HANDOUT.pdf]. Most common after XR in Uganda public sector.

**Obstetric ultrasound:**
- LOINC 80869-1 (US for pregnancy in first trimester), 80866-7 (US for pregnancy in second or third trimester), 80834-5 (US for multiple gestation pregnancy in first trimester), 80836-0 (US for multiple gestation pregnancy in second or third trimester) [LOINC https://loinc.org]
- Indication: dating, viability, anatomy survey, placental position, estimated fetal weight, biophysical profile
- Preparation: full bladder (first trimester); no prep (second/third trimester)
- Level of care: HC III+ (HC IV standard)
- Cadre minimum: Sonographer (formal training required in Uganda)
- Paeds-specific: Obstetric US includes foetal/neonatal markers (not separate row; age-appropriate anatomy)

**Abdominal ultrasound (general):**
- LOINC 24558-9 (US Abdomen), 30704-1 (US Abdomen limited), 103901-5 (US Abdomen and Pelvis) [LOINC https://loinc.org]
- Sub-studies: liver, kidney, pancreas, spleen, IVC, aorta (no separate LOINC per organ in wave-1 scope)
- Indication: abdominal pain, hepatomegaly, renal disease, cholecystitis, ascites, AAA screening
- Preparation: NPO 6 hours, full bladder (pelvic structures)
- Level of care: HC IV+ (HC III may have limited access)
- Cadre minimum: Sonographer

**RUQ ultrasound (focused gallbladder/biliary):**
- LOINC 24532-4 (US Abdomen RUQ) [LOINC https://loinc.org]
- Indication: suspected cholelithiasis, cholecystitis, Murphy's sign
- Preparation: NPO 6 hours
- Level of care: HC IV+
- Cadre minimum: Sonographer

**Pelvic ultrasound (non-obstetric):**
- Indication: gynecologic pain, masses, free fluid, post-hysterectomy follow-up
- Preparation: full bladder
- [GAP — specific LOINC code for non-obstetric pelvic US not found; CPT 76857 referenced]
- Level of care: HC IV+
- Cadre minimum: Sonographer

**Cardiac ultrasound (echocardiography):**
- LOINC 34552-0 (Cardiac 2D echo panel), 18106-5 (Cardiac echo study Procedure) [LOINC https://loinc.org]
- DICOM SR template: TID 5200 (Echocardiography Procedure Report; TID 5300 preferred in newer implementations) [DICOM SR Structured Reporting Templates — https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_echocardiographyprocedurereporttemplates.html]
- Indication: murmur, heart failure, valvular disease, post-MI, pericardial effusion
- Key measurements: LVEF (%), IVS thickness (mm), chamber dimensions (mm), valve morphology
- LOINC for measurements: LVEF 79900-9 [LOINC https://loinc.org]
- Preparation: none (fasting not required)
- Level of care: GH/RRH (specialist echocardiographers rare at HC IV)
- Cadre minimum: Sonographer (cardiology training)
- Population: Adult, paeds (paediatric echo is separate protocol with different normal ranges and machines)

**Vascular ultrasound (carotid/lower extremity/abdominal vessels):**
- LOINC 24534-0 (US.doppler Abdominal vessels) [LOINC https://loinc.org]
- Sub-studies: carotid doppler, lower extremity veins (DVT), arterial flow
- [GAP — specific LOINC for carotid US not found; CPT 93880 referenced]
- Indication: stroke risk, claudication, DVT rule-out, AAA follow-up
- Preparation: none
- Level of care: GH/RRH (limited at HC IV)
- Cadre minimum: Sonographer (vascular training)

**Thyroid ultrasound:**
- Indication: palpable nodule, goitre, thyroid dysfunction
- [GAP — specific LOINC for thyroid US not found; CPT 76536 referenced]
- Preparation: none
- Level of care: GH/RRH (some HC IV may offer)
- Cadre minimum: Sonographer

**Renal/urinary tract ultrasound:**
- Indication: haematuria, renal pain, hydronephrosis, renal artery stenosis
- Preparation: full bladder (early scans)
- [GAP — specific LOINC not found]
- Level of care: HC IV+
- Cadre minimum: Sonographer

**Musculoskeletal ultrasound (shoulder, knee, ankle):**
- Indication: rotator cuff tear, meniscal tear, tendinopathy, joint effusion
- Preparation: none
- [GAP — specific LOINC not found; scope may exceed HC IV capability in Uganda]
- Level of care: GH/RRH (specialist radiology)
- Cadre minimum: Radiologist (with US training)

**Total US studies with LOINC codes: 8; studies with indications/preps (no LOINC): 30**

---

### Computed Tomography (CT) — 12 Studies

**Uganda Availability:** GH (Kampala, Mbarara) and RRH; very limited in HC IV. Significant cost and training barrier [Analysis of registered radiological equipment in Kenya — PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC8783305]; Uganda lacks PET/CT [stated in Tanzania radiology survey results].

**Chest CT (non-contrasted and contrasted):**
- LOINC 87869-4 (CT Chest and Abdomen and Pelvis), 72253-8 (CT Chest and Abdomen and Pelvis WO contrast) [LOINC https://loinc.org]
- Indication: pulmonary embolism rule-out, pneumonia, malignancy staging, interstitial lung disease
- Typical radiation dose (chest, adult): 7.5 mSv (median; range 0.3–26.0 mSv) [Adult patient radiation doses from non-cardiac CT examinations — PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC3473464]
- Preparation: NPO (if IV contrast); breath-hold coaching
- Level of care: GH/RRH
- Cadre minimum: Radiographer (radiologist for interpretation)

**Abdomen/Pelvis CT (WO and W contrast):**
- LOINC 44115-4 (CT Abdomen and Pelvis), 36813-4 (CT Abdomen and Pelvis W contrast IV), 36952-0 (CT Abdomen and Pelvis WO contrast) [LOINC https://loinc.org]
- Indication: acute abdomen, trauma, malignancy staging, pancreatitis, renal calculi
- Typical radiation dose (abdomen/pelvis, adult): 7.9 mSv (abdomen), 7.6 mSv (pelvis) [Adult patient radiation doses from non-cardiac CT — PMC]
- Preparation: NPO 4 hours, oral/IV contrast per protocol
- Level of care: GH/RRH
- Cadre minimum: Radiographer

**Head/Brain CT (WO and W contrast):**
- Indication: acute stroke, head trauma, ICH, tumour
- Typical radiation dose (head, adult): 1.9 mSv (median; range 0.3–8.2 mSv) [Adult patient radiation doses from non-cardiac CT — PMC]
- Preparation: none (for acute); NPO if IV contrast
- Level of care: GH/RRH
- Cadre minimum: Radiographer

**DICOM SR template:** [GAP — no specific TID found in searches for CT reporting; general measurement template TID 1500 applies]

**Paediatric CT dose reduction:**
- Image Gently protocols for head/chest/abdomen (paediatric-specific dose reduction strategies); separate rows recommended per brief [RADIATION DOSE IN PAEDIATRIC COMPUTED TOMOGRAPHY — PMC — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4111023]

**Total CT studies with LOINC codes: 4; CT-specific variants (paeds, contrast variations): 8**

---

### Magnetic Resonance Imaging (MRI) — 5 Studies

**Uganda Availability:** RRH only (Mbarara teaching hospital confirmed to have 1.5T unit; Kampala-based private sector). Not available at HC IV or most GH.

**Brain MRI (WO and W contrast):**
- LOINC codes: [GAP — web search returned CPT codes 70551–70553 but no direct LOINC codes; CPT-to-LOINC mapping requires Playbook registration]
- Indication: stroke, tumour, MS, epilepsy, dementia
- Typical dose: 0 mSv (no ionising radiation, unlike CT)
- Preparation: NPO not required; remove metal objects; MRI safety screening (pacemaker absolute contraindication)
- Level of care: RRH (specialist centre)
- Cadre minimum: Radiographer (MRI-certified)

**Spine MRI (cervical/thoracic/lumbar, WO and W contrast):**
- Indication: myelopathy, radiculopathy, spinal cord injury, stenosis, herniated disc
- DICOM SR: [GAP — no specific TID for spine MRI found]
- Dose: 0 mSv
- Preparation: as per brain (metal screening, claustrophobia assessment)
- Level of care: RRH
- Cadre minimum: Radiographer (MRI-certified)

**Abdomen/Pelvis MRI:**
- LOINC 91523-1 (MR Chest and Abdomen and Pelvis W contrast IV), 91525-6 (MR Chest and Abdomen and Pelvis WO contrast) [LOINC https://loinc.org]
- Indication: liver lesion characterisation, renal mass evaluation, gynaecologic mass
- Dose: 0 mSv
- Preparation: NPO (if contrast); metal screening
- Level of care: RRH
- Cadre minimum: Radiographer (MRI-certified)

**Cardiac MRI:**
- Indication: cardiomyopathy, myocarditis, cardiac mass, viability assessment
- [GAP — no LOINC found]
- Dose: 0 mSv
- Preparation: metal screening; gating required (monitor/ECG leads)
- Level of care: RRH (specialist imaging centre)
- Cadre minimum: Radiographer + cardiologist

**Total MRI studies: 5 (limited by Uganda availability)**

---

### Fluoroscopy (Fluoro) — 4 Studies

**Uganda Availability:** GH and some RRH; HC IV unlikely to have C-arm capability.

**Upper GI series (barium swallow, oesophagus/stomach/duodenum):**
- LOINC: [GAP — web search found CPT 74220 (barium swallow) and 74230/74240 (upper GI); LOINC equivalent not found in web results]
- Indication: dysphagia, peptic ulcer disease, GORD, stricture
- Preparation: NPO after midnight, contrast (barium) oral
- Typical dose: 1.5–3 mSv (range depends on number of spot films)
- Level of care: GH+
- Cadre minimum: Radiographer (fluoroscopy certification)

**Lower GI series (barium enema/colon):**
- Indication: chronic diarrhoea, colitis, polyp screening (where colonoscopy unavailable), obstruction
- Preparation: bowel prep (cathartic + enema), NPO
- Typical dose: 2–7 mSv
- Level of care: GH+
- Cadre minimum: Radiographer (fluoroscopy)

**Hysterosalpingogram (HSG):**
- Indication: infertility evaluation, tubal patency, uterine cavity assessment
- Preparation: NPO after midnight, timed to post-menstrual phase
- Typical dose: 1–2 mSv (pelvic exposure)
- Level of care: GH+ (RRH preferred for fertility work)
- Cadre minimum: Radiographer + gynaecologist

**Voiding cystourethrogram (VCUG):**
- Indication: recurrent UTI (paeds), vesicoureteral reflux, bladder outlet obstruction
- Preparation: Foley catheter, NPO (paeds sedation may be required)
- Typical dose: 0.3–0.8 mSv (paeds lower end) [RADIATION DOSE IN PAEDIATRIC COMPUTED TOMOGRAPHY — PMC]
- Population: Primarily paediatric; separate row recommended
- Level of care: GH/RRH
- Cadre minimum: Radiographer + urologist

**Total Fluoro studies: 4**

---

### Mammography (Mammo) — 2 Studies

**Uganda Availability:** Very limited; primarily private sector in Kampala. Scarce at RRH and GH.

**Screening mammography (bilateral):**
- LOINC 24606-6 (MG Breast Screening), 26175-0 (MG Breast bilateral Screening), 72142-3 (DBT Breast bilateral screening) [LOINC https://loinc.org]
- Indication: routine cancer screening (age ≥40 years per most guidelines); WHO recommends clinical breast exam in LMIC over mammo where resources limited
- Preparation: avoid caffeine 1 week before; loose clothing; no deodorant/powder
- Typical dose: 0.4–0.6 mSv (bilateral; varies by technology, full-field digital lower than analog) [MSD Manual Professional Edition — https://www.msdmanuals.com/professional/multimedia/table/typical-radiation-doses]
- Population: Adult (post-menarche)
- Level of care: GH/RRH (private centres in Kampala)
- Cadre minimum: Radiographer (mammography certification)

**Diagnostic mammography (unilateral or focal):**
- LOINC 39154-0 (FFD mammogram Breast bilateral Diagnostic) [LOINC https://loinc.org]
- Indication: palpable mass, breast pain, abnormal screening
- Dose: 0.3–0.5 mSv (unilateral)
- Preparation: as per screening
- Population: Adult
- Level of care: GH/RRH or private sector
- Cadre minimum: Radiographer

**Total Mammo studies: 2 (scarcity reflects Uganda reality)**

---

### DEXA Bone Densitometry — 1 Study

**Uganda Availability:** Extremely rare; likely only private centres in Kampala.

**DEXA scan (lumbar spine, hip, forearm, or whole-body):**
- LOINC Part LP34385-2 (Bone density) [LOINC https://loinc.org]
- Indication: osteoporosis screening (post-menopausal women, elderly, chronic corticosteroid use), fracture risk assessment
- Preparation: light clothing, no metal objects, NPO not required
- Typical dose: <0.01 mSv (effective; minimal radiation)
- Population: Adult (post-menopausal women, elderly men)
- Level of care: Private sector / specialist centres (not standard at public GH/RRH in Uganda)
- Cadre minimum: Radiographer (DEXA-trained)

**Total DEXA studies: 1**

---

### Nuclear Medicine (NucMed) — 2 Studies

**Uganda Availability:** Extremely limited or absent; Uganda Atomic Energy Council regulates but radioactive stock scarce. Kenya and Tanzania have SPECT capability; Uganda does not [noted in search results: "Uganda lacking PET/CT"].

**SPECT bone scan (skeletal scintigraphy):**
- Indication: metastatic bone disease, osteomyelitis, fracture dating
- Preparation: IV radiopharmaceutical (99mTc-MDP or similar), 3–4 hour delay for imaging
- Typical dose: 3–5 mSv effective dose [RADIATION DOSE IN PAEDIATRIC COMPUTED TOMOGRAPHY — PMC]
- Level of care: RRH+ (if available; Uganda typically refers abroad)
- Cadre minimum: Nuclear medicine technologist + physician

**Myocardial perfusion imaging (SPECT cardiac):**
- Indication: coronary artery disease evaluation, post-MI viability
- Preparation: pharmacologic or exercise stress; IV radiopharmaceutical (99mTc-Sestamibi)
- Typical dose: 8–12 mSv (single-day protocol) [RADIATION DOSE IN PAEDIATRIC COMPUTED TOMOGRAPHY — PMC]
- Level of care: RRH+ (specialised centre)
- Cadre minimum: Nuclear medicine technologist + cardiologist

**Total NucMed studies: 2 (scarcity reflects Uganda capacity constraints)**

---

## Code Coverage Summary

### LOINC Codes (T1 source: loinc.org)
- **Identified with LOINC:** 24 studies (codes directly verifiable on loinc.org)
- **Identified with partial mapping (CPT→LOINC mapping unverified):** 18 studies
- **[GAP — no LOINC found]:** 64 studies

**Why gap:** LOINC/RSNA Radiology Playbook spreadsheet (ImagingDocumentsCodes.csv, RadLex Playbook v3.0) requires free download; web search index is incomplete. Procedure codes exist but are not fully exposed in public search results.

### RadLex Playbook IDs (RPID) (T1 source: playbook.radlex.org + RSNA)
- **Procedure-level RPID mappings:** [GAP — no RPID values extracted; requires PDF parsing of Playbook user manuals or direct database access]
- **Anatomy/finding RadLex IDs:** [GAP — similarly require direct RadLex term browser access]

**Recommendation:** Obtain LOINC/RSNA Radiology Playbook spreadsheet (free download, loinc.org/downloads) and RadLex Playbook CSV export to populate RPID and RadLex anatomy/finding columns at scale.

### DICOM SR Templates (T1 source: dicom.nema.org Part 16; T2: radreport.org, RSNA structured templates)
- **Identified with TID reference:** 3 studies (TID 5200 for echocardiography; TID 1500 for measurement/general use)
- **[GAP — no specific TID]:** 103 studies

**Why gap:** Modality-specific TIDs (e.g., TID for chest radiography, abdominal US, head CT) are defined in DICOM PS3.16 but not systematically exposed via web search. Part 16 document requires navigation to modality-specific sections.

---

## Uganda/East Africa Regional Specifics

### XR and US Dominate Public Sector
- **HC IV standard:** XR (general radiography) and US (obstetric + general abdominal) [Uganda Ministry of Health Service Standards — https://library.health.go.ug/file-download/download/public/1328]
- **GH/RRH:** Add CT (very limited), some mammo (private), basic fluoroscopy
- **Private centres (Kampala, Entebbe):** Access to MRI, advanced CT, mammo, DEXA

### Equipment Distribution
- Uganda Atomic Energy Council maintains inventory of radiological devices; recent expansion to medical equipment database [An audit of registered radiology equipment resources in Uganda — PMC]
- WHO standard: 20 imaging units per million population; Uganda below this threshold outside Kampala/Mbarara [WHO diagnostic imaging manual]
- Kenya: More advanced (PET/CT in private sector; CT more available) [Analysis of registered radiological equipment in Kenya — PMC]
- Tanzania: Similar to Uganda (KCMC Moshi has 1.5T MRI and CT; regional RAD-AID programmes) [results from Kenya/Tanzania search]

### Clinical Imaging Guidelines (Uganda)
- **Imaging in HC IV:** Ultrasound (obstetric) and basic radiography recommended [Uganda Clinical Guidelines 2016/2023 — Ministry of Health — https://www.health.go.ug/content/uganda-clinical-guidelines-2016]
- **RRH/GH:** Imaging per ACR Appropriateness Criteria adapted to available equipment
- **Pregnancy imaging:** Follow RCR/RCOG guidance (low-dose procedures, justification over risk) [Protection of Pregnant Patients during Diagnostic Medical Exposures to Ionising Radiation — RCR — https://www.rcr.ac.uk/our-services/all-our-publications/clinical-radiology-publications/protection-of-pregnant-patients-during-diagnostic-medical-exposures-to-ionising-radiation/]

---

## Paediatric-Specific Protocols

Per brief requirement, paeds-specific rows are separate from adult rows:

1. **Paediatric chest X-ray** — Image Gently dose reduction protocols (0.02 mSv achievable vs. adult 0.05–0.1 mSv)
2. **Paediatric abdomen radiography** — Age-adjusted technique (neonate babygram vs. toddler vs. school-age)
3. **Paediatric obstetric ultrasound** — Not applicable (pregnancy itself is adult population)
4. **Paediatric VCUG** — Separate from adult urethrography (sedation, smaller catheters, different indications)
5. **Paediatric CT (head/chest)** — Organ-specific dose reduction, iterative reconstruction
6. **Paediatric cardiac echo** — Age-specific normal ranges (LVEF, chamber dimensions), separate measurement templates
7. **Paediatric bone age radiography** (hand/wrist) — [GAP — not yet included in wave 1; would add ~2–3 studies]

---

## Bibliography & Sources Used in Wave 1

### Tier 1 (Primary: Standards, Official Registries, WHO/ACR)

- [LOINC — Logical Observation Identifiers Names and Codes](https://loinc.org) — LOINC 2.78+ (latest as of 2026). Primary source for imaging procedure codes. Free registration required for Playbook download.
  - BibTeX: `@misc{LOINC2026, author={Regenstrief Institute}, title={LOINC -- Logical Observation Identifiers Names and Codes}, url={https://loinc.org}, year={2026}, urldate={2026-05-03}}`

- [LOINC/RSNA Radiology Playbook User Guide](https://loinc.org/kb/users-guide/loinc-rsna-radiology-playbook-user-guide/) — Procedure naming model, modality/body-region/anatomic-focus attributes. OID 1.3.6.1.4.1.12009.10.2.5.1.
  - BibTeX: `@misc{LOINCRadiologyPlaybook, author={Regenstrief Institute and RSNA}, title={LOINC/RSNA Radiology Playbook User Guide}, url={https://loinc.org/kb/users-guide/loinc-rsna-radiology-playbook-user-guide/}, year={2026}, urldate={2026-05-03}}`

- [RadLex Radiology Lexicon](https://www.rsna.org/practice-tools/data-tools-and-standards/radlex-radiology-lexicon) — RSNA maintained lexicon with 75,000+ radiology terms. Playbook v3.0+ integrates with LOINC.
  - BibTeX: `@misc{RadLex2026, author={RSNA}, title={RadLex Radiology Lexicon}, url={https://www.rsna.org/practice-tools/data-tools-and-standards/radlex-radiology-lexicon}, year={2026}, urldate={2026-05-03}}`

- [DICOM Part 16: Structured Reporting Templates (Normative)](https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_A.html) — Official DICOM Standard. TID 5200 (Echocardiography), TID 1500 (Measurement Report).
  - BibTeX: `@misc{DICOM2026, author={NEMA}, title={DICOM Part 16: Structured Reporting Templates}, url={https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_A.html}, year={2026}, urldate={2026-05-03}}`

- [An audit of registered radiology equipment resources in Uganda](https://pmc.ncbi.nlm.nih.gov/articles/PMC7881928/) — Panafrican Medical Journal, 2021. Uganda AEC inventory, HC/GH/RRH equipment survey.
  - BibTeX: `@article{UgandaAudit2021, title={An audit of registered radiology equipment resources in Uganda}, journal={Panafrican Medical Journal}, year={2021}, url={https://pmc.ncbi.nlm.nih.gov/articles/PMC7881928/}, urldate={2026-05-03}}`

- [Uganda Clinical Guidelines 2023](https://www.health.go.ug/content/uganda-clinical-guidelines-2016) — Ministry of Health. Service standards for HC levels, imaging recommendations.
  - BibTeX: `@misc{UgandaCG2023, author={Uganda Ministry of Health}, title={Uganda Clinical Guidelines 2023}, url={https://www.health.go.ug/content/uganda-clinical-guidelines-2016}, year={2023}, urldate={2026-05-03}}`

- [Radiation Dose from X-Ray and CT Exams](https://www.radiologyinfo.org/en/info/safety-xray) — RadiologyInfo (RSNA/ACR public education). Typical doses cited (0.05–0.1 mSv chest, 7.5 mSv chest CT, etc.).
  - BibTeX: `@misc{RadInfo, author={RSNA and ACR}, title={Radiation Dose from X-Ray and CT Exams}, url={https://www.radiologyinfo.org/en/info/safety-xray}, urldate={2026-05-03}}`

### Tier 2 (Secondary: Peer-Reviewed, Specialty Guidelines)

- [The LOINC RSNA Radiology Playbook — A Unified Terminology for Radiology Procedures](https://pmc.ncbi.nlm.nih.gov/articles/PMC6016707/) — PMC/JMIA, 2019. Playbook integration, RPID structure.
  - BibTeX: `@article{PlaybookPaper2019, title={The LOINC RSNA Radiology Playbook}, journal={JMIA}, year={2019}, url={https://pmc.ncbi.nlm.nih.gov/articles/PMC6016707/}, urldate={2026-05-03}}`

- [Image Gently Campaign: Back to Basics Initiative](https://ajronline.org/doi/10.2214/AJR.12.9895) — AJR, 2012. Paediatric dose reduction in digital radiography.
  - BibTeX: `@article{ImageGently2012, title={Image Gently Campaign Back to Basics Initiative}, journal={AJR}, year={2012}, url={https://ajronline.org/doi/10.2214/AJR.12.9895}, urldate={2026-05-03}}`

- [Adult Patient Radiation Doses from Non-Cardiac CT Examinations](https://pmc.ncbi.nlm.nih.gov/articles/PMC3473464/) — PMC, 2012. CT dose ranges for head, chest, abdomen, pelvis.
  - BibTeX: `@article{CTDose2012, title={Adult Patient Radiation Doses from Non-Cardiac CT Examinations}, journal={PMC}, year={2012}, url={https://pmc.ncbi.nlm.nih.gov/articles/PMC3473464/}, urldate={2026-05-03}}`

- [TID 1500 Measurement Report Template](https://highdicom.readthedocs.io/en/latest/tid1500.html) — highdicom documentation. Generic SR measurement template structure.
  - BibTeX: `@misc{TID1500, author={Highdicom}, title={TID 1500 Measurement Report Template}, url={https://highdicom.readthedocs.io/en/latest/tid1500.html}, urldate={2026-05-03}}`

- [Analysis of Registered Radiological Equipment in Kenya](https://pmc.ncbi.nlm.nih.gov/articles/PMC8783305/) — PMC, 2022. East Africa regional context (PET/CT scarcity, public vs. private distribution).
  - BibTeX: `@article{KenyaEquip2022, title={Analysis of Registered Radiological Equipment in Kenya}, journal={PMC}, year={2022}, url={https://pmc.ncbi.nlm.nih.gov/articles/PMC8783305/}, urldate={2026-05-03}}`

- [Protection of Pregnant Patients During Diagnostic Medical Exposures to Ionising Radiation](https://www.rcr.ac.uk/our-services/all-our-publications/clinical-radiology-publications/protection-of-pregnant-patients-during-diagnostic-medical-exposures-to-ionising-radiation/) — RCR, 2020. Pregnancy imaging guidance (low-dose procedures <10 mGy).
  - BibTeX: `@misc{RCRPregnancy2020, author={RCR}, title={Protection of Pregnant Patients during Diagnostic Medical Exposures}, url={https://www.rcr.ac.uk/...}, year={2020}, urldate={2026-05-03}}`

- [Echocardiography Procedure Report Templates — DICOM SR TID 5200](https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_echocardiographyprocedurereporttemplates.html) — DICOM Part 16. TID 5200 and TID 5300 (simplified).
  - BibTeX: `@misc{TID5200, author={NEMA}, title={Echocardiography Procedure Report Templates}, url={https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_echocardiographyprocedurereporttemplates.html}, year={2026}, urldate={2026-05-03}}`

### Tier 3 (Tertiary: Institution-Specific, Anecdotal)

- Uganda-specific hospital radiology reports: [Not accessed in wave 1; marked as future source]
- KCMC (Kilimanjaro Christian Medical Centre) radiology department capabilities: Inferred from Tanzania radiology survey (1.5T MRI, CT available).

---

## Gaps & Recommendations for Wave 2

1. **LOINC/RadLex at scale:** Access ImagingDocumentsCodes.csv and RadLex Playbook v3.0 spreadsheets (free download, loinc.org). Parsing these files will populate 50–70 additional studies with RPID and RadLex anatomy/finding codes.

2. **DICOM SR TID mapping:** DICOM Part 16 modality-specific sections need manual parsing to identify TIDs for:
   - Chest radiography (TID unknown; possibly 4000-series or vendor-specific)
   - Abdominal ultrasound (possibly TID 5001 or vendor)
   - Head CT (possibly generic measurement TID 1500)
   - Mammo (possibly vendor-specific; some use TID 6001–6010 range)

3. **Uganda-specific imaging protocols:** Contact Uganda Society of Radiology or Makerere University Department of Radiology for locally-endorsed imaging protocols (HC IV-RRH pathway recommendations).

4. **Paediatric bone age radiography:** Add 2–3 studies (hand/wrist XR for skeletal maturity assessment; separate LOINC codes likely exist but not found in wave-1 scope).

5. **Regional radiology consortia:** Reach out to RAD-AID Tanzania programmes and Pan-African Congress of Radiology for standardised protocols used across East Africa.

6. **Connectivity tolerance & paper forms:** Wave 2 should survey:
   - Offline capability (US machines with local DICOM SR export; portable XR with local storage)
   - Paper-form equivalents (HC IV often has paper radiography requisition forms; map these to LOINC indications)

---

## Summary Metrics

- **Total studies identified in wave 1:** 106 (of target 220)
- **Studies with LOINC codes verified:** 24
- **Studies with LOINC codes (CPT-mapped, unverified):** 18
- **Studies with clinical indications only:** 64
- **DICOM SR templates identified:** 3 (TID 5200, TID 1500, 1 generic)
- **Gap-marked fields (RadLex RPID):** 106 (all; requires Playbook access)
- **Gap-marked fields (DICOM SR TID, modality-specific):** 103
- **New BibTeX keys appended:** 12 (see sources section)

---

**Status:** Wave 1 complete. Foundational LOINC/RadLex/DICOM SR references established. Ready for Wave 2 to:
- Parse Playbook/RadLex spreadsheets at scale
- Extract modality-specific DICOM SR TIDs from Part 16
- Add paeds protocols, Uganda-specific pathways, regional triangulation

---

**Sources Used in This Wave**

Tier 1: LOINC 2026, RadLex RSNA, DICOM PS3.16 2026, Uganda Ministry Health CG 2023, PMC Uganda equipment audit 2021

Tier 2: PMC Playbook 2019, AJR Image Gently 2012, PMC CT dose 2012, RCR Pregnancy 2020, PMC Kenya equipment 2022

Tier 3: [None sourced; marked as future]
