---
project: healthcare-app-clinical-data
date: 2026-05-03
purpose: Cross-cohort master document — links the 5 cohorts (conditions ↔ drugs ↔ labs ↔ imaging ↔ procedures) into clinical clusters the app will need to handle in real practice. Orchestrator-only synthesis (per project CLAUDE.md and source-evaluation discipline).
---

# Cross-Cohort Master — clinical clusters

This document is the integration layer over the five cohort wave files. It walks the high-burden Uganda clinical entities and shows, for each, which entries from the other cohorts the app needs to surface together. It does **not** introduce new clinical claims — every assertion below is sourced through the cohort wave files committed under `<cohort>/research/wave1-*.md`, `wave2-*.md`, `wave3-*.md`. Where a row referenced here is missing from the corpus, that gap is named.

Coverage scope: Uganda primary; Kenya + Tanzania triangulation. Hard exclusions per `_context/exclusions.md`. Evidence discipline per repo `skills/source-evaluation/references/evidence-discipline.md`.

## How to read this file

Each cluster has the shape:

> **Cluster name** — common burden context (one line, sourced).
> - Conditions: `<icd10_code>` items from `conditions/research/`
> - Drugs: `<atc_code>` items from `drugs/research/`
> - Lab: `<loinc_code>` items from `lab-tests/research/`
> - Imaging: `<loinc_code>` items from `imaging/research/`
> - Procedures: `<ichi_code | icd10_pcs_code | cdt_code>` items from `procedures/research/`
> - **App surfacing note** — what the app should make easy
> - **Gap** — what is missing from the corpus

The clusters are ordered by approximate Uganda DALY contribution; for the cancer and mental-health clusters DALY rank is less informative than service-delivery need so they are grouped logically.

---

## 1. Malaria (Uganda DALY rank 1, all-ages)

- **Consumables:** mRDT kits; microscopy slides and stains; lancets; EDTA tubes; IV cannulae/giving sets; LP needles when CNS differential is live.

Falciparum malaria dominates; parasitaemia drives clinical course. Severe malaria is a paediatric and obstetric emergency.

- **Conditions:** B54 unspecified; B50 falciparum; B51 vivax; B50.0 cerebral; B50.8 severe; obstetric malaria (O98.6 plus B50/B54)
- **Drugs:** P01BF01 artemether-lumefantrine (AL — first-line uncomplicated); P01BE03 artesunate (severe); P01BC01 quinine (alternate severe); P01BA01 chloroquine (P. vivax non-falciparum; G6PD-tested primaquine for radical cure); P01BA03 primaquine
- **Lab:** mRDT (LOINC scope: malaria antigen rapid tests — exact LOINC codes for HRP-2 vs pLDH variants flagged `[GAP — East African mRDT not yet standardised]` in lab Wave 1 findings); thick-and-thin film microscopy; full blood count (haemolysis monitoring); G6PD before primaquine; lactate (severe)
- **Imaging:** Cerebral malaria → CT/MRI head only if differential includes structural lesion (most cerebral malaria diagnosed clinically + LP). Chest XR if respiratory distress.
- **Procedures:** Lumbar puncture (any cluster suspecting CNS involvement); blood transfusion (severe anaemia); IV artesunate administration protocol (anaesthesia/emergency procedure list)
- **App surfacing note:** Pair B54 selection with one-tap mRDT order, AL prescription, and severity triage prompt (parasitaemia + LOC + lactate). Default offline-OK at HC II/III.
- **Gap:** mRDT-variant LOINC codes; primaquine paediatric dose roster.

## 2. Tuberculosis

- **Consumables:** sputum cups; AFB slides and Ziehl-Neelsen stains; GeneXpert cartridges; masks/PPE; specimen bags.

Pulmonary TB is HMIS-reportable and IDSR-notifiable. Drug-resistant TB rising. HIV co-infection is the rule.

- **Conditions:** A15 (bacteriologically confirmed pulm TB); A16 (presumptive pulm TB); A17 (TB nervous system); A18 (TB other organs incl. lymph, spine, GU); A19 (miliary)
- **Drugs:** J04AB02 rifampicin; J04AC01 isoniazid; J04AK02 ethambutol; J04AK01 pyrazinamide; J04AB30 rifapentine (TPT); fixed-dose combinations (RHZE, RH, RHE); J04AK06 delamanid + J04AK08 bedaquiline (DR-TB at NRH); pyridoxine prophylaxis
- **Lab:** Sputum smear AFB (LOINC sourced); GeneXpert MTB/RIF (Xpert — LOINC 86901-0 sourced); culture + drug-susceptibility (line probe assay — LOINC partial); HIV test paired (always); LFTs baseline + monthly; baseline visual acuity (ethambutol)
- **Imaging:** Chest XR PA (LOINC 36572-6 study; corpus has it); chest CT for complications; spine XR / MRI for Pott's; abdo US for nodes/effusions
- **Procedures:** Sputum induction; pleural tap; lymph node biopsy; bronchoscopy (RRH+); BCG vaccination
- **App surfacing note:** A15 selection should auto-trigger HIV test order, contact-tracing checklist, and 6-month treatment-card workflow. Connectivity-tolerance offline-OK except Xpert result return (online).
- **Gap:** Line probe assay LOINC codes; full DR-TB regimen drug rows.

## 3. HIV / AIDS

- **Consumables:** HIV rapid test kits; EDTA tubes for VL/CD4; CrAg kits; LP consumables; condoms and VMMC supplies.

Generalised epidemic; PMTCT, paediatric, and adolescent HIV all need separate care plans.

- **Conditions:** B20–B24 series (HIV with various outcomes); Z21 asymptomatic HIV; opportunistic infections by code (B59 PCP, B58 toxoplasmosis, A07.1 cryptosporidiosis, B45.x cryptococcosis, B37 candidiasis)
- **Drugs:** J05A series — TLD (tenofovir + lamivudine + dolutegravir) first-line per WHO; J05AF07 tenofovir; J05AF05 lamivudine; J05AJ03 dolutegravir; J05AE10 atazanavir/r (second-line); J05AE08 lopinavir/r (paeds liquid); J05AB04 zidovudine (paeds); J04AB02 rifampicin–DTG interaction flagged in DDI sub-table
- **Lab:** HIV serology (LOINC 75622-1 + variants); HIV viral load (LOINC 25836-8); CD4 count (LOINC 24467-3); cryptococcal antigen (CrAg, LOINC sourced); CD4 <200 → ART initiation + OI prophylaxis; full PMTCT panel (HIV + syphilis + Hep B at first ANC)
- **Imaging:** Chest XR for OI workup; head CT for opportunistic CNS lesions; abdo US for visceral OIs
- **Procedures:** Voluntary medical male circumcision (VMMC; corpus contains the procedure rows); BCG (paediatric HIV-exposed); LP for cryptococcal meningitis
- **App surfacing note:** B20 selection auto-stages on CD4, opens TPT (rifapentine/INH) checkbox, surfaces TLD prescribing default. PMTCT mode for any pregnant HIV+ patient.
- **Gap:** CrAg-LOINC variant for serum vs CSF; paediatric ART liquid-formulation rows.

## 4. Maternal and obstetric

- **Consumables:** IV cannulae; giving sets; crossmatch tubes; urine protein strips; sterile delivery packs; sutures; catheters.

Maternal mortality remains high; PPH, eclampsia, obstructed labour, sepsis dominate causes.

- **Conditions:** O72 PPH; O14/O15 pre-eclampsia/eclampsia; O64–O66 obstructed labour; O75.3 sepsis; O98.6 malaria in pregnancy; Z34 normal supervision
- **Drugs:** H01BB02 oxytocin (Vital, cold-chain); G02AB03 ergometrine; G02AD06 misoprostol (off-label PPH); A03FA01 metoclopramide; B05XA03 saline; B05BA09 magnesium sulfate (eclampsia); J01CR02 amoxicillin/clavulanate; iron + folate (B03A series)
- **Lab:** Hb (LOINC 718-7); urinalysis incl. protein (LOINC 5804-0); blood group + Rh + crossmatch; HIV + syphilis + Hep B at first ANC; OGTT 75g (LOINC 14771-0); urine HCG
- **Imaging:** Obstetric US (full anatomy, biophysical profile, dating, doppler — corpus has these in imaging Wave 3); pelvic XR rarely; trans-vaginal US for early pregnancy
- **Procedures:** Caesarean section (primary, repeat — corpus); assisted vaginal delivery (vacuum, forceps); manual removal of placenta; manual vacuum aspiration; B-Lynch suture; Bakri balloon; internal iliac ligation; perimortem caesarean; episiotomy + repair
- **App surfacing note:** ANC visit module bundles Hb, HIV, syphilis, Hep B, urine protein orders + iron/folate prescribing + dating US referral (HC III+). PPH bundle one-tap for oxytocin + misoprostol + cross-match + escalation.
- **Gap:** Magnesium-sulfate paediatric eclampsia row; some advanced OB-Gyn procedures (e.g., classical CS) intentionally not included (RRH-only specialist).

## 5. Neonatal

- **Consumables:** neonatal bags/masks; suction catheters; umbilical catheter kits; glucose strips; bilirubin tubes; paediatric burette sets.

Birth asphyxia, prematurity, sepsis, jaundice. Neonatal CPOE is the highest-risk paeds context (Coiera 3e ch. 13, Pittsburgh PICU lesson).

- **Conditions:** P21 birth asphyxia; P22 RDS; P36 neonatal sepsis; P59 neonatal jaundice; P05 IUGR; P07 prematurity-related; P92 feeding problems
- **Drugs:** J01DD04 ceftriaxone (avoided in neonates — flag); J01CA04 ampicillin + J01GB03 gentamicin (first-line neonatal sepsis); R03DA04 caffeine citrate (apnoea of prematurity); B05BB01 dextrose 10%; A11CC04 vitamin K (1 mg IM at birth) — all rows present in drugs cohort
- **Lab:** Neonatal-specific reference ranges captured as separate rows per Coiera ch. 13: Hb, bilirubin total + direct (LOINC 1975-2; 1968-7), glucose, blood culture, CRP, LP findings. Critical values are population-specific (phototherapy thresholds age-in-hours).
- **Imaging:** Cranial US (paeds, LOINC sourced in imaging Wave 3); chest XR; abdo XR (NEC); hip US for DDH
- **Procedures:** Neonatal resuscitation (HBB protocol); umbilical catheterisation; phototherapy; exchange transfusion (NRH-only)
- **App surfacing note:** Strict separation of neonatal dosing UI from adult dosing. Bilirubin entry must trigger AAP nomogram lookup by age-in-hours. Ceftriaxone selection must check neonate flag and warn.
- **Gap:** International Neonatal Consortium (INC) preterm-specific critical-value thresholds — flagged in lab Wave 1 findings as Phase 2 outreach item.

## 6. Pneumonia (paediatric and adult)

- **Consumables:** pulse-ox probes; oxygen masks/prongs; nebuliser masks/tubing; blood-culture bottles; sputum cups; chest-drain kits.

Major cause of paediatric admission and mortality. Atypical and TB co-presentation.

- **Conditions:** J18 unspecified pneumonia; J15.x bacterial; J12.x viral; J13 strep pneumoniae; J15.1 Hib (paeds, vaccine-preventable); J20 acute bronchitis; J45 asthma overlap
- **Drugs:** J01CA04 amoxicillin (first-line CAP); J01CR02 amoxicillin-clavulanate; J01FA10 azithromycin (atypical); J01DD04 ceftriaxone (severe); R03AC02 salbutamol (wheeze); H02AB06 prednisolone (severe asthma overlap); O2 therapy (gas)
- **Lab:** SpO2; CBC; CRP; blood culture; sputum culture (adult); urinary pneumococcal antigen (where stocked); influenza/RSV PCR (RRH+, LOINC partial); HIV (always)
- **Imaging:** Chest XR PA + lateral; chest CT for empyema/abscess (RRH); paeds chest XR; pleural US
- **Procedures:** Pleural tap; chest drain insertion; nebuliser administration; CPAP/HFNO at higher-tier centres
- **App surfacing note:** Paeds J18 selection bundles SpO2 entry, RR-by-age, IMCI severity classifier, amoxicillin or referral decision logic.
- **Gap:** Influenza/RSV PCR LOINC variants.

## 7. Diarrhoeal disease

- **Consumables:** ORS/zinc dispensing packs; stool containers; cholera RDT/transport media; IV cannulae/giving sets; NG tubes.

Paediatric mortality driver. ORS + zinc is the WHO standard.

- **Conditions:** A09 unspecified gastroenteritis; A00 cholera; A01 typhoid; A02 salmonellosis; A03 shigellosis; A06 amoebiasis; A07.1 cryptosporidiosis; B82.0 helminth-associated
- **Drugs:** A07CA ORS (Vital); A12CB01 zinc sulfate (paeds 10–14 days); J01XD01 metronidazole (amoebic, giardia); J01MA02 ciprofloxacin (cholera, shigellosis); J01EE01 cotrimoxazole; A07EA06 budesonide (chronic, niche)
- **Lab:** Stool microscopy + ova/parasites; stool culture; cholera RDT; rotavirus antigen (paeds); HIV (chronic diarrhoea); urea + creatinine (dehydration); blood gas (severe dehydration)
- **Imaging:** Abdo XR / US for complications (perforation, intussusception)
- **Procedures:** IV cannulation + rehydration protocol; nasogastric tube placement; stool sample collection
- **App surfacing note:** A09 paeds selection auto-bundles ORS + zinc + dehydration assessment. Cholera reportable flag → IDSR notification.

## 8. Malnutrition (under-fives)

- **Consumables:** MUAC tapes; weighing/height equipment; feeding cups; NG tubes; glucose strips; RUTF/micronutrient dispensing materials.

SAM (severe acute malnutrition) and stunting. Therapeutic-feeding programme integration.

- **Conditions:** E40 kwashiorkor; E41 marasmus; E42 marasmic-kwashiorkor; E43 unspecified severe; E44 moderate/mild; E45 retarded development; E46 unspecified
- **Drugs:** RUTF (ready-to-use therapeutic food, F-75 / F-100 — these are food formulations, not ATC rows; flagged); A11 vitamin A high-dose; B03 ferrous + folate (post-stabilisation); J01CA04 amoxicillin (routine in SAM); A07CA ORS
- **Lab:** Hb; glucose; electrolytes (refeeding); HIV (always); TB screening; stool/urine workup
- **Imaging:** Generally none unless complication
- **Procedures:** MUAC measurement; weight-for-height plotting; nasogastric feeding tube
- **App surfacing note:** MUAC entry triggers SAM/MAM stratification and admission criteria. Ten Steps WHO protocol bundles for SAM admission.

## 9. Hypertension and ischaemic heart disease (NCD spike)

- **Consumables:** BP cuffs; ECG electrodes/paper; troponin/BNP tubes; urine strips; oxygen and IV access supplies.

NCD shift in epidemiology — middle-aged adults dominate.

- **Conditions:** I10 essential HTN; I11 hypertensive heart disease; I20 angina; I21 acute MI; I50 heart failure; I63 ischaemic stroke; I64 stroke unspecified; I05 rheumatic mitral; I50.0 LV failure
- **Drugs:** C03AA03 hydrochlorothiazide; C03DA01 spironolactone; C07AB02 metoprolol; C07AB07 bisoprolol; C08CA01 amlodipine; C09AA01 captopril; C09AA02 enalapril; C09AA05 lisinopril; C09CA01 losartan; B01AC06 aspirin; C10AA01 simvastatin; C10AA05 atorvastatin; B01AA03 warfarin; B01AB05 enoxaparin
- **Lab:** Lipid panel; HbA1c; renal panel; ECG (not LOINC strictly); high-sens troponin (LOINC); BNP (LOINC); urinalysis; potassium (delta-check critical)
- **Imaging:** Chest XR; echocardiogram (LOINC + DICOM TID 5200 SR template — corpus has it); carotid doppler (Wave 3); CT brain non-contrast for stroke
- **Procedures:** ECG recording; stress test (RRH); pacemaker insertion (NRH-specialist); pleural tap (CHF complication)
- **App surfacing note:** I10 selection opens lifestyle-and-target dashboard; auto-orders renal + lipid + glucose at intervals; statin prescribing decision logic surfaced.

## 10. Diabetes mellitus

- **Consumables:** glucometer strips; lancets; ketone strips; insulin syringes/pens; sharps boxes; HbA1c consumables.

Type 1 paediatric and Type 2 adult both rising in Uganda.

- **Conditions:** E10 T1DM; E11 T2DM; E13 other specified; E14 unspecified; E16 hypoglycaemia; E11.5 with peripheral circulatory complications
- **Drugs:** A10BA02 metformin; A10BB01 glibenclamide; A10BB12 glimepiride; A10BJ01 exenatide (rare in Uganda); A10AB01 insulin regular; A10AB04 insulin lispro; A10AC01 insulin isophane (NPH); A10AE04 insulin glargine; insulin storage cold-chain flag; A11DA01 thiamine
- **Lab:** Fasting glucose (LOINC 1558-6); HbA1c (LOINC 4548-4); urine ACR; urine ketones; OGTT; LFTs (metformin); creatinine (metformin contraindication); HDL/LDL/triglycerides; eye-screen referral
- **Imaging:** Doppler peripheral arteries (foot); fundoscopy (annual)
- **Procedures:** Diabetic foot exam protocol; HbA1c blood draw; subcutaneous insulin teaching
- **App surfacing note:** E11 selection bundles HbA1c every 3-6 months, annual eye + foot + creatinine schedules. Insulin selection requires cold-chain flag confirmation.

## 11. Mental health

- **Consumables:** screening forms/cards; ECG electrodes; serum drug-level tubes; CBC tubes for clozapine monitoring.

Fully in scope across all cohorts.

- **Conditions:** F32/F33 depression; F41 anxiety; F20 schizophrenia; F31 bipolar; F10 alcohol use disorder; F60 personality disorders; F84 autism spectrum (paeds); F90 ADHD; G40 epilepsy (overlap)
- **Drugs:** N06AB04 citalopram; N06AB03 fluoxetine; N06AB06 sertraline; N06AA09 amitriptyline; N05AH02 clozapine (NRH-only); N05AH03 olanzapine; N05AH04 quetiapine; N05AX08 risperidone; N05AB04 fluphenazine depot; N03AG01 valproate; N03AB02 phenytoin; N03AF01 carbamazepine; N03AX09 lamotrigine; N05BA01 diazepam; N06AX16 venlafaxine; N07BB04 naltrexone (alcohol)
- **Lab:** Lithium level (LOINC); valproate level; carbamazepine level; LFTs; ECG (psychotropic QT); CBC (clozapine ANC monitoring critical-value)
- **Imaging:** Brain CT/MRI for first-episode psychosis or atypical presentation
- **Procedures:** Psychotherapy session structures (not ICD-10-PCS); ECT administration (NRH); detox protocols
- **App surfacing note:** Mental-health module needs offline-OK suicidality screening (PHQ-9, GAD-7) and prescribing logic with QT and DDI checks (esp. methadone, antipsychotics, SSRI + tramadol).
- **Gap:** Lithium critical-value thresholds in lab cohort flagged.

## 12. Cancer (RRH scope)

- **Consumables:** Pap/cytology brushes and slides; biopsy needles; specimen pots; sutures; IV chemotherapy access supplies.

Cervical, breast, prostate, Kaposi, paediatric leukaemia/lymphoma dominate. Specialist surgical oncology beyond RRH excluded.

- **Conditions:** C53 cervical; C50 breast; C61 prostate; C46 Kaposi; C81 Hodgkin; C82–C85 NHL; C91 ALL; C92 AML; C18 colon; C16 stomach; C22 liver (HepB-driven); C73 thyroid
- **Drugs:** L01 chemo cytotoxics — L01AA01 cyclophosphamide; L01AA06 ifosfamide; L01BA01 methotrexate; L01BB02 mercaptopurine; L01BC02 5-fluorouracil; L01CA01 vinblastine; L01CA02 vincristine; L01DA01 actinomycin; L01DB01 doxorubicin; L01DB07 mitoxantrone; L01XA01 cisplatin; L01XA02 carboplatin; L01XX02 asparaginase; H02AB02 dexamethasone (chemo-induced N+V); A04AA01 ondansetron
- **Lab:** Tumour markers (CEA, AFP, beta-HCG, CA-125, PSA — corpus has these); HPV PCR + Pap (cervical); breast biopsy histology; FISH/IHC; CBC + ANC nadir monitoring (delta-check); LFTs + creatinine (chemo dosing)
- **Imaging:** Mammography (Wave 3); breast US; pelvic US; abdo CT staging; chest XR / CT; PET/CT — `[GAP — not available in Uganda public sector]` flagged in imaging Wave 1 findings; bone scan (Wave 3 NucMed)
- **Procedures:** Cervical screening (VIA, Pap, HPV); cone biopsy; mastectomy — included as district-hospital scope; breast core biopsy (Wave 2/3); FNAC (lab cohort); palliative care (procedures cohort); chemo administration protocols
- **App surfacing note:** C53 selection bundles VIA/Pap/HPV order, colposcopy referral pathway, and treatment-pathway flowchart by FIGO stage.
- **Gap:** PET/CT, specialist surgical oncology (intentional). LASA tall-man for cytotoxics seeded in DDI sub-tables.

## 13. Mental ↔ Neurology overlap: Epilepsy

- **Consumables:** IV cannulae; airway adjuncts; oxygen masks; glucose strips; anti-epileptic drug monitoring tubes.

- **Conditions:** G40.x epilepsy variants (focal, generalised, status epilepticus G41)
- **Drugs:** N03AA02 phenobarbital; N03AB02 phenytoin; N03AG01 valproate; N03AF01 carbamazepine; N03AX09 lamotrigine; N03AX14 levetiracetam; N03AE01 clonazepam; emergency: N05BA01 diazepam IV/PR; N05CD08 midazolam buccal
- **Lab:** Anti-epileptic drug levels; LFTs; CBC (carbamazepine); HCG (women of childbearing age — valproate teratogenicity)
- **Imaging:** EEG (not LOINC strictly); MRI brain; CT brain (acute)
- **Procedures:** Status epilepticus protocol; airway management; seizure observation
- **App surfacing note:** Status epilepticus pathway one-tap (diazepam or PR midazolam → second-line phenobarbital → third-line phenytoin/levetiracetam IV).
- **Gap:** Levetiracetam IV not on Uganda EMHSLU — flagged in drug cohort.

## 14. Injury and trauma (RTA + burns + snake bite)

- **Consumables:** cervical collars; IV cannulae; pressure dressings; sutures; chest-drain kits; splints; FAST ultrasound gel.

- **Conditions:** S00–T98 series (specific anatomical injuries); T07 multiple injuries; T20–T32 burns by region/depth; T63 venomous bite (snake, scorpion); T78 anaphylaxis; X00–X99 external causes
- **Drugs:** Tetanus immunoglobulin (J06BB02); tetanus toxoid (J07AM01); antivenom (V03AB — specific products); IV fluids (B05); ketamine (N01AX03 anaesthesia and analgesia); morphine (N02AA01); paracetamol (N02BE01); local anaesthetic (N01BB02 lignocaine)
- **Lab:** Type + crossmatch; CBC; coagulation; lactate; ABG; venom-related (snake bite — clotting time)
- **Imaging:** Trauma series XR; FAST (Wave 3); CT head/abdo/spine; XR specific bones
- **Procedures:** Wound exploration and closure (Minor procedures); fracture reduction (closed and open); ORIF (Ortho); chest drain (tension pneumothorax); burn care; intubation; cricothyroidotomy (NRH); LP if head injury workup
- **App surfacing note:** Trauma triage module (ABC, Glasgow, mechanism, field-triage). RTA = IDSR-reportable.

## 15. Dental and oral health

- **Consumables:** dental mirrors/probes; intraoral film/sensors; fluoride varnish; restorative materials; dental needles/syringes.

Explicitly in-scope. CDT codes carry ADA licensing constraint flagged for app team's commercial rollout.

- **Conditions:** K00 disorders of tooth development; K02 caries; K05 periodontal disease; K12 stomatitis; K07 dentofacial anomalies
- **Drugs:** N02BE01 paracetamol; M01AE01 ibuprofen; J01CA04 amoxicillin; J01XD01 metronidazole; A01AB03 chlorhexidine mouthwash; topical fluoride; lignocaine (local anaesthesia); diazepam (anxiety pre-procedure)
- **Lab:** Generally none routine; CBC + INR pre-extraction in select patients
- **Imaging:** OPG, bitewing, periapical, occlusal, panoramic, CBCT — corpus has these in imaging Wave 3
- **Procedures (CDT roster, ADA fair-use)**: D0xxx diagnostic; D1xxx preventive; D2xxx restorative; D3xxx endodontic; D4xxx periodontic; D5xxx prosthodontic; D7xxx oral surgery; D9xxx adjunctive — corpus has 60+ codes between Wave 1, 2, 3
- **App surfacing note:** Dental module separate UI track from medical. CDT selection must show licensing flag for commercial deployment. Bundle exam → radiograph → treatment-plan flow.

## 16. Eye care

- **Consumables:** visual-acuity charts; fluorescein strips; tonometer tips; sterile eye pads; ophthalmic sutures and drapes.

Cataract is the largest single intervention by volume nationally (per WHO).

- **Conditions:** H25 senile cataract; H40 glaucoma; H35.0 retinopathy; H35.3 AMD; H10 conjunctivitis; H16 keratitis; H20 iridocyclitis; H50 strabismus; H53 amblyopia (paeds, separate row)
- **Drugs:** S01 series — S01EC03 dorzolamide; S01ED01 timolol; S01EE01 latanoprost; S01EX02 brinzolamide; S01AA01 chloramphenicol drops; S01AA13 fusidic acid drops; S01BA04 prednisolone drops; S01EB01 pilocarpine; S01HA02 oxybuprocaine (procedure anaesthesia); S01FA01 atropine drops (mydriatic)
- **Lab:** Generally none routine; HbA1c for diabetic retinopathy patients
- **Imaging:** B-scan ocular US (Wave 3); OCT (Wave 3 — RRH+); fundoscopy (clinical not imaging-cohort)
- **Procedures:** Cataract extraction (phaco, ECCE — corpus); pterygium excision; corneal repair; laser procedures; trabeculectomy; lid surgery; lacrimal procedures (Wave 2 additions)
- **App surfacing note:** Visual acuity entry standardised. Glaucoma selection bundles IOP target + drug schedule + 6-month review.
- **Gap:** Anti-VEGF intravitreal injections — limited in Uganda public sector.

## 17. Sexual and reproductive health

- **Consumables:** implant/IUD kits; pregnancy tests; condoms; speculums; swabs; STI rapid tests; syringes.

- **Conditions:** A50–A53 syphilis; A54 gonorrhoea; A56 chlamydia; B97.7 HPV-related; N76 vaginitis; N70 PID; Z30 contraception encounter
- **Drugs:** Family planning — G03AA07 levonorgestrel/EE; G03AA12 desogestrel; G02BA02 IUS-LNG; G02BB01 IUD-Cu; G03AC03 medroxyprogesterone depot (DMPA); G03BA03 testosterone; oxytocics (above); J01CR02 amoxiclav; J01FA10 azithromycin; J01XD01 metronidazole (BV); J02AB02 ketoconazole (vaginal); benzathine penicillin (J01CE08) syphilis; ceftriaxone (gonorrhoea)
- **Lab:** Syphilis serology (RPR + treponemal); urine NAAT for GC/CT (LOINC partial); HIV; Hep B; Pap/HPV
- **Imaging:** Pelvic US (TV and TA); breast US (cyclical mass)
- **Procedures:** IUD insertion; bilateral tubal ligation; vasectomy; circumcision (paeds and VMMC); MVA; cervical cryotherapy
- **App surfacing note:** FP module presents methods by patient profile (parity, breastfeeding, contraindications). Counselling steps tracked.

## 18. Skin and dermatology

- **Consumables:** swabs; dressing packs; biopsy sets; KOH/microscopy slides; gloves and wound-care materials.

Burden mostly tinea, scabies, eczema, leprosy (residual), Kaposi (HIV-associated, see Cancer cluster), pyoderma.

- **Conditions:** B35 dermatophytosis; B86 scabies; L20 atopic eczema; L40 psoriasis; L00–L08 pyoderma series; A30 leprosy
- **Drugs:** D01AC01 clotrimazole topical; D01AE15 terbinafine topical; D02AA emollients; D05AA dithranol; D07A topical corticosteroids series; D06AX permethrin (scabies); ivermectin (P02CF01) onchocerciasis + scabies; D08AC02 chlorhexidine
- **Lab:** Skin scraping for fungal hyphae (KOH); skin biopsy histology; HIV (always for Kaposi)
- **Imaging:** Generally none
- **Procedures:** Skin biopsy (punch, incision, excision); abscess I&D (Minor); cryotherapy (warts, BCC); curettage
- **App surfacing note:** Body-map UI for lesion documentation. Scabies = household contact treatment auto-prompt.

## 19. ENT

- **Consumables:** otoscope specula; ear syringes; nasal packs; swabs; suction catheters; minor-procedure dressing sets.

- **Conditions:** H66 otitis media; H65 otitis media non-suppurative; J03 acute tonsillitis; J32 chronic sinusitis; J35.x adenoid/tonsil; J37 chronic laryngitis; H81 vestibular
- **Drugs:** J01CA04 amoxicillin; J01CR02 amoxiclav; topical S02 (otitis externa); R01AA series (decongestant nasal); R01AC antihistamine nasal; H02 systemic steroid where indicated
- **Lab:** Audiology assessment (Wave 1 procedures); throat swab + culture
- **Imaging:** Sinus XR (Wave 3); mastoid; neck soft tissue; CT sinuses (RRH)
- **Procedures:** Tonsillectomy; myringotomy ± grommet; FESS (RRH); audiology testing; foreign body removal; tracheostomy; mastoidectomy; adenoidectomy; septoplasty
- **App surfacing note:** Paeds otitis follows IMCI watch-and-wait + Day-3 review default.

## 20. Anaesthesia

- **Consumables:** airway adjuncts; endotracheal tubes; laryngoscope blades; spinal/epidural needles; syringes; monitoring electrodes.

Cross-cutting cohort underpinning Procedures.

- **Drugs:** N01AB06 isoflurane; N01AB08 sevoflurane (NRH); N01AH01 fentanyl; N01AH51 alfentanil; N01AX03 ketamine; N01AX10 propofol; N01BB02 lignocaine; N01BB04 prilocaine; N01BB52 lignocaine + adrenaline; N02AA01 morphine; N03AE01 clonazepam (premedication rare); N05BA01 diazepam (premed); M03 muscle relaxants — M03AB01 suxamethonium; M03AC04 vecuronium; M03AC09 rocuronium; M03AC11 cisatracurium; reversal — V03AB35 sugammadex (if available); naloxone (V03AB15) for opioid reversal
- **Lab:** Pre-op CBC, U&E, glucose; pregnancy test; group + crossmatch
- **Imaging:** Pre-op chest XR / ECG (not LOINC strictly) per ASA grade
- **Procedures:** Spinal anaesthesia; epidural; GA (induction + maintenance); regional blocks — TAP, fascia iliaca, interscalene, axillary, ankle, sciatic, femoral (Wave 3); local infiltration; airway management; cricothyroidotomy; emergency intubation
- **App surfacing note:** Pre-op assessment bundles fasting status, allergies, last meal, ASA grade, airway predictors, drug history.

## 21. Imaging-led emergency workflows

- **Consumables:** ultrasound gel; ECG electrodes/paper; IV cannulae and contrast lines; specimen tubes; procedure kits as indicated.

Workflows the app should treat as orderable bundles:

- **Stroke (suspected):** Conditions I63/I64 → CT brain non-contrast (urgent) → if ischaemic + tPA window → tPA at NRH only (B01AD02 alteplase — flagged restricted access)
- **Acute abdomen:** R10 abdominal pain → erect chest XR (free air) + abdo XR + abdo US + CBC + amylase/lipase + urine HCG
- **Trauma (FAST-eligible):** mechanism + suspicion → e-FAST (Wave 3) + trauma-series XR + CT head/abdo if indicated
- **Maternal collapse:** PPH bundle + Bakri/B-Lynch readiness; perimortem CS protocol if cardiac arrest in 3rd-trimester pregnancy
- **Snake bite:** clotting time (20-min whole blood) → polyvalent antivenom protocol → adrenaline standby

These cross-cohort bundles should appear as one-tap orderables in the app, not as separate manual selections.

---

## Corpus-level coverage summary

| Cohort | Items in corpus | Target | % | Verified by orchestrator row-count |
|---|---|---|---|---|
| Conditions | 220 | 220 | 100% | ✓ |
| Drugs A-J | 141 | ≥250 | 56% | ✓ |
| Drugs L-V | 189 | ≥280 | 67% | ✓ |
| Lab tests (distinct LOINC) | 177 | 220 | 80% | ✓ |
| Imaging | 255 | 220 | 116% | ✓ |
| Procedures | 254 | 220 | 116% | ✓ |
| **Total items / total target** | **1236 / ≥1410** | | **88%** | |

Three cohorts hit or exceed target. Two drug cohorts and lab tests are short for a single root cause: **Uganda-specific source documents (EMHSLU 2023, NDA register, Uganda Lab SOPs, full IDSR list) are PDFs that web-extraction agents could not parse reliably.** The agents that pushed through used machine-readable proxies (eEML, GitHub atcd CSV, RxNav API) but cannot replace the local-formulary specificity that EMHSLU brings.

## Cross-cohort gaps

Items the corpus expected to find but couldn't:

1. **mRDT LOINC variants** for Pf-specific, Pv-specific, Pan rapid antigens — flagged across malaria cluster
2. **Line probe assay LOINC** for TB drug-resistance phenotypes — flagged in TB cluster
3. **Cryptococcal antigen LOINC variants** (serum vs CSF) — flagged in HIV cluster
4. **INC neonatal critical-value thresholds** — flagged in neonatal cluster
5. **Influenza/RSV PCR LOINC variants** — flagged in pneumonia cluster
6. **Anti-VEGF intravitreal procedures** — limited public-sector availability (eye cluster)
7. **Specialist surgical oncology** — intentional exclusion per scope, but app should signpost referral pathway
8. **PET/CT** — confirmed unavailable in Uganda public sector (cancer cluster)
9. **Levetiracetam IV** — not on Uganda EMHSLU (epilepsy cluster); flagged
10. **Full ADA CDT roster** — proprietary, ~60 codes seeded under fair-use; commercial deployment requires ADA license

## App-implementation notes (cross-cohort)

These are derived from the cohort findings files:

1. **Late-binding pattern (Systems Perspective 2e ch. 13)** — population qualifier (`population` column) is a first-class filter across labs, drugs, procedures. The app must default ranges/doses by patient population, not by single column.
2. **Connectivity-tolerance flag** — every cohort carries `connectivity_tolerance` ∈ {offline-OK, online-required}. The app must degrade gracefully at HC II/III where connectivity is intermittent.
3. **Paper-form equivalents** — Uganda HMIS forms 105 / 108 / 098 / 033b are partially mapped per row. The app should emit reports in HMIS format for facility-level statisticians.
   - **Standard Forms cohort addendum:** `standard-forms/research/wave1-data.md` now normalizes the form/tool catalogue found in the local corpus: HMIS 105, 106A, 107, 108, 033A/B/C, HIV programme registers/cards, commodity tools, IDSR case-investigation/contact-tracing tools, and explicit TBD/gap rows where the source did not give a current form code.
4. **Cadre-min and level-of-care-min** — every applicable row carries these. The app should hide items the current user's cadre/facility cannot perform.
5. **Code-system version + access date** — every code has `code_system_version` and `code_accessed_date`. The app must surface "last updated" so the team can plan annual refresh (Coiera 3e ch. 23 — terminology maintenance dominates lifetime cost).
6. **LASA / tall-man rendering** — drugs with confused names carry the ISMP-style rendering in `lasa_tallman_form`. The app's prescribing UI must use that rendering, not the plain INN, for these drugs.
7. **Granularity caveats** — Conditions cohort flags rows where ICD-10 collapses two distinct entities. The app should surface SNOMED CT alongside for clinical clarity (Coiera 3e ch. 23 quote: "ICD is not intended, nor is it suitable, for indexing distinct clinical entities").
8. **DDI sub-tables** — Drugs cohort seeds high-severity DDIs only (Volpe ch. 6 alert-fatigue principle). The app must NOT seed every theoretical interaction or it will replicate the 1.1M-alerts/month override pattern.
9. **DICOM SR templates** — Imaging cohort references TIDs (5200 echo, 1500 measurement, etc.). The app's structured-reporting interface should align with these TIDs for downstream PACS interop.
10. **CDT licensing** — Dental codes are ADA fair-use in this corpus. The app's commercial-deployment plan must include an ADA CDT license; surface the licensing flag in the dental module.

## Phase 4 / 5 readiness

The corpus is ready for:

- **Critical-reasoning pass** — `skills/critical-reasoning-and-argument` over each cohort's findings to make claims, warrants, assumptions, countercases, and business-sense checks visible before final report drafting
- **Word/Excel deliverable assembly (Phase 5)** — `skills/professional-word-output` for each cohort's report; `document-skills:xlsx` for each cohort's data sheet; `skills/research-report-builder` to orchestrate

These steps are deferred to a separate session to keep this orchestration session focused. `PROJECT-STATUS.md` is the resumption anchor.

## What this synthesis does NOT do

- It does not introduce new clinical claims. Every assertion above traces to the cohort wave files committed in this repo.
- It does not strike or replace claims. Strikes are recorded in `EVIDENCE-AUDIT.md`.
- It does not fabricate cluster memberships — where a row referenced is missing from the corpus, it is named as a gap, not silently asserted.

## See also

- `PROJECT-STATUS.md` — full wave tracker
- `EVIDENCE-AUDIT.md` — strike log + Wave 1 row-count fabrication entries
- `_context/book-derived-recommendations.md` — informatics-textbook-derived data-model decisions
- `_registry/sources.bib` — full bibliography across all waves
- `<cohort>/research/wave[1|2|3]-{data,findings}*.md` — per-cohort source-of-truth corpora
- `standard-forms/research/wave1-data.md` — Uganda paper forms/registers/cards/reports found in the local corpus; use as lookup for `paper_form_equivalent`

---

# Phase 6 — Tenant-setup synthesis (added 2026-05-03)

The original 7 cohorts above (conditions, drugs A–J, drugs L–V, lab-tests, imaging, procedures, consumables, standard-forms) are the **clinical-data corpus**: what items exist, how they're coded, and what populations they apply to.

Phase 6 added 7 **tenant-setup cohorts** that turn the clinical-data corpus into a runnable multi-tenant deployment: facilities, roles-permissions, workflows, country-packs, billing-tariffs, reporting-kpis, tenant-blueprints. Together the 14 cohorts let a new healthcare tenant be configured in minutes by selecting country + facility type + operating model.

## Phase 6 corpus-level coverage

| # | Cohort | Wave-1 items | Discipline patches applied |
|---|---|---|---|
| 2 | Facilities | 28 rows × 22 cols (14 UG + 14 KE) | Wikipedia citations stripped from 4 flagship-hospital rows |
| 3 | Roles-permissions | 18 rows × 23 cols | 8 cells corrected (UMDPC ≠ clinical officers; PSU ≠ registration council; AHPC for lab/clinical-officer/radiographer; "Class A/B/C" replaced with POM where used as prescribing schedule) |
| 4 | Workflows | 18 rows × 17 cols | 4 residual "Class A/B/C" prescribing-scope references in WF-RX-001 patched to "controlled / scheduled medicine — POM" with `[T1 verification pending]` |
| 5 | Country packs | 9 rows × 24 cols (UG+KE full; TZ/RW/GH/NG/ZA/IN/PH stub) | Wikipedia stripped from 9 `source_citations` cells |
| 6 | Billing-tariffs | 58 charge-items + 16 payer mappings | clean (no patch needed) |
| 7 | Reporting-KPIs | 55 indicators × 19 cols across 16 domains | clean (no patch needed) |
| 1 | Tenant blueprints | 6 canonical blueprints × 14 cols | clean (orchestrator-assembled integration cohort) |

## Phase 6 evidence-discipline lessons (logged in EVIDENCE-AUDIT.md)

Each cohort's brief carried the cumulative discipline clauses learned from earlier cohorts in the phase. The accumulating clauses:

1. **Hard-constraint clause (no hallucination)** — verbatim from project root `CLAUDE.md`, every brief.
2. **Wikipedia-discipline clause — two halves** — added after cohort 2 (facilities) had Wikipedia in flagship-hospital `source_citations`. Refined after cohort 5 (country-packs) tagged "T3 corroboration: Wikipedia" inside cells thinking it was compliant. Final form: (a) Wikipedia may NEVER appear in `source_citations` cells, even when tagged T3; (b) Wikipedia entries belong only in the bottom `## Sources — T3` block of findings; (c) self-audit step: grep for `[Ww]ikipedia` and confirm zero hits in any data cell before reporting completion.
3. **Cadre→council lookup table** — added after cohort 3 (roles-permissions) confused UMDPC (medical & dental) with AHPC (clinical officers / lab cadres / radiographers) and listed PSU (a professional society) as a registration council. Final form: a verbatim lookup table in every brief that names the correct regulator per cadre per country.
4. **Uganda prescribing-schedule warning** — added after cohort 3 used "NDA Class A/B/C" as a prescribing schedule. Class A/B/C are drug-shop license tiers under NDA, NOT prescribing schedules. Final form: explicit warning + instruction to use "POM (Prescription Only Medicines) under NDA framework" or flag `[T1 verification pending]`.
5. **Pricing-evidence rules** — added for cohort 6 (billing-tariffs). Public Uganda tier rows must say `0 UGX (abolished 2001)` with citation, never invented fees. Private-tier prices must be ranges with named hospital anchors, never point values. Year and currency mandatory on every price quote. Kenya post-1-Oct-2024 financing must cite SHA, never NHIF.

The discipline clauses are reusable: any future research wave (Wave-2 gap-fill, Phase-7 new countries) should inherit clauses 1–5 verbatim.

## Cross-phase integration map

How the Phase-6 cohorts plug into the Phase-1–5 clinical-data corpus:

| Phase-6 cohort | Plugs into Phase-1–5 corpus via |
|---|---|
| facilities | every clinical row's `level_of_care_min` resolves to a facility-type ID; referral pathways across condition / procedure cohorts route between facility tiers |
| roles-permissions | every clinical row's `cadre_min` resolves to a role_id; deny-by-default rules gate access to controlled drugs, lab verification, prescribing |
| workflows | every clinical pathway (ANC, ART, TB, IDSR, immunisation) references conditions, drugs, lab-tests, imaging, procedures, consumables artefacts |
| country-packs | every cohort's `country_applicability` resolves to a country code; mandatory-reports field references HMIS-107 / KHIS forms in standard-forms |
| billing-tariffs | every charge-item's `linked_clinical_item` references conditions / drugs / lab-tests / imaging / procedures / consumables IDs |
| reporting-kpis | every KPI's `numerator_data_source` and `denominator_data_source` references standard-forms entries; programme KPIs (HIV/TB/malaria) reference conditions and drugs |
| tenant-blueprints | aggregates references from all 6 above plus standard-forms; one blueprint = one curated tenant configuration |

## Phase 6 — what's NOT done

- **Wave-2 gap-fill** — known gaps logged in each cohort's findings file; not yet researched.
  - facilities: Mulago/Gulu/Mbarara bed counts pending T1 verification (currently `[T1 verification pending]` after Wikipedia patch); Uganda Service Standards 2016 PDF unreachable; KMHFL 2020 implementation guide inaccessible.
  - roles-permissions: Uganda enrolled-nurse + radiographer scope-of-practice documents not retrieved; Kenya CHV statutory scope (no independent Act); exact NDA prescriber-schedule reference pending.
  - workflows: Kenya clinical-guideline cache (NCK / KMPDC) not yet sourced; NDA prescriber-schedule still pending in WF-RX-001.
  - country-packs: 7 stub countries (TZ/RW/GH/NG/ZA/IN/PH) at 5–6 columns each; full pack research deferred (estimated 2–3 days per country).
  - billing-tariffs: PNFP per-facility tariffs (Uganda) not centrally published; SHA specialist-consultation tariff PDF binary; private hospital price-lists for 5–10 named facilities pending retrieval.
  - reporting-kpis: 15 `[form-cohort gap]` markers awaiting standard-forms Wave-2; alert thresholds for 8 KPIs unsourced.
  - tenant-blueprints: domain-level KPI references need pinning to literal IDs; setup_steps need formalising as machine-executable JSON/YAML; pharmacy licence-tier parameter not yet implemented; 4 specialty blueprints deferred.

- **Phase-6 deliverable assembly** — Word + Excel reports for the 7 new cohorts not yet generated. The Phase-1–5 pipeline used `scripts/generate_healthcare_app_clinical_data_outputs.py` to emit per-cohort DOCX + grouped XLSX. The script needs extension for the 7 new cohorts before this phase has finalised deliverables. Each cohort's Word `.docx` must include a §1 Coding Standards section per the project's standing requirement (see `_context/standards-and-bodies.md`).

- **Critical-reasoning pass** over the 7 new cohorts — `skills/critical-reasoning-and-argument` not yet applied. The clinical-data cohorts had this pass in Phase-4; the operational cohorts have not.

## Phase 6 readiness for next session

The corpus is ready for:
1. Wave-2 gap-fill — dispatch sub-agents per the Wave-2 list above; each cohort's gap list is short and well-bounded.
2. Phase-6 deliverable assembly — extend the existing Python output script to handle the 7 new cohort folders; emit per-cohort DOCX + XLSX; include §1 Coding Standards section.
3. Critical-reasoning pass — apply `skills/critical-reasoning-and-argument` over each new cohort's findings before final-report drafting.
4. Updated cross-cohort master Word generation — re-run with the Phase-6 sections appended.

`PROJECT-STATUS.md` Phase-6 table is the resumption anchor.
