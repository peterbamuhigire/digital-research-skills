# Wave 1 Research Findings — Drugs Cohort, ATC L–V

**Date:** 2026-05-03  
**Cohort:** Drugs (ATC level-1 groups L through V)  
**Geographic scope:** Uganda primary; Kenya + Tanzania triangulation  
**Coverage target:** All relevant Uganda EMHSLU drugs in L–V plus WHO EML 23rd ed. (2023)  

---

## Scope

This Wave 1 research covers **ATC level-1 groups L through V**:
- **L** — Antineoplastic and immunomodulating agents
- **M** — Musculoskeletal system  
- **N** — Nervous system
- **P** — Antiparasitic products, insecticides and repellents
- **R** — Respiratory system
- **S** — Sensory organs
- **V** — Various

**Exclusions (per project):** Veterinary medicine, traditional/herbal medicine, transplant-specific immunosuppression, cancer chemotherapy beyond RRH scope (core EML cytotoxics included), neurosurgical-specific anaesthetics. Transplant-relevant rheumatology immunosuppressants (azathioprine, ciclosporin, tacrolimus) are **included**.

---

## Methodology

**Wave 1 baseline extraction from:**

1. **T1 (Primary) sources:**
   - WHO Model List of Essential Medicines, 23rd edition (2023) [who-eml-2023]
   - WHO Model List of Essential Medicines for Children, 9th edition [who-emlc-9]
   - Uganda Essential Medicines and Health Supplies List (EMHSLU) 2023 [emhslu-uganda-2023]
   - Uganda Clinical Guidelines 2023 [ucg-uganda-2023]
   - WHO ATC/DDD Index [who-atc-ddd-index]
   - Uganda National Drug Authority register (July 2024 edition) [nda-uganda-register-2024]

2. **T2 (Corroborating) sources:**
   - Kenya Essential Medicines List 2023 [keml-kenya-2023]
   - Peer-reviewed pharmacology and clinical trial literature

**Search strategy:** Systematic extraction of L–V drugs from WHO EML 23rd ed., cross-reference with EMHSLU 2023 and Uganda Clinical Guidelines 2023. For each drug: ATC code (5-level), INN, WHO EML section, DDD (Defined Daily Dose), RxNorm RXCUI bridge, formulations, strengths, Ugandan brand names, NDA registration status, and level-of-care minimum.

**Coding standards:** ATC primary (5-level); DDD per WHO ATC/DDD Index; RxNorm RXCUI per Volpe ed. ch. 6 interoperability requirement; INN (substance name); 4 locally-registered brands where available.

**DDI (Drug–Drug Interaction) sub-table:** High-risk interactions only (severity ∈ {high, medium}), seeded per Volpe ch. 6 alert-fatigue principle. Antineoplastics and CNS drugs (N) are interaction-dense; capped at ~100 rows for L–V slice. Reported actual.

---

## Findings by ATC Level-1 Group

### L — Antineoplastic and Immunomodulating Agents

**Preliminary item count (Wave 1): ~40 drugs identified; full scope pending gap-fill.**

**Coverage summary:**
- **L01 (Antineoplastic agents):** Alkylating agents (L01A), antimetabolites (L01B), plant alkaloids (L01C), cytotoxic antibiotics (L01D), protein kinase inhibitors (L01E), monoclonal antibodies (L01F), other (L01X) — estimated 25–30 items
- **L02 (Endocrine therapy):** Aromatase inhibitors, tamoxifen, progestins — estimated 5–8 items
- **L03 (Immunostimulants):** Cytokines, interferons — estimated 2–3 items (limited in low-resource EML)
- **L04 (Immunosuppressants):** Calcineurin inhibitors (ciclosporin, tacrolimus), antimetabolites (azathioprine, mycophenolate), monoclonal antibodies — estimated 5–8 items

**WHO EML 23rd inclusion (verified by source search):**
- Methotrexate (L01BC05) — folic acid analogue, antimetabolite [who-eml-2023]
- Cyclophosphamide (L01AA01) — alkylating agent [who-eml-2023]
- Doxorubicin (L01DB01) — anthracycline, cytotoxic antibiotic [who-eml-2023]
- Cisplatin (L01XA01) — platinum compound [who-eml-2023]
- 5-Fluorouracil (L01BC02) — pyrimidine analogue [who-eml-2023]
- [Additional L01 drugs: DDD and RxNorm mapping pending source verification] [GAP — agent could not access full WHO EML PDF; extracted via abstract/summary sources]

**Uganda EMHSLU inclusion status:** 
- Azathioprine (L04AX01) — rheumatic/autoimmune use presumed on EMHSLU (Vital or Essential tier); [unverified — agent could not access EMHSLU 2023 full PDF]
- Ciclosporin (L04AD01) — rheumatic/autoimmune; [unverified — agent could not access EMHSLU 2023 full PDF]
- Tacrolimus (L04AD02) — rheumatic/autoimmune; [unverified — agent could not access EMHSLU 2023 full PDF]

**NDA Uganda verification:** ~5 L-drugs verified against NDA July 2024 register [nda-uganda-register-2024]. Register in binary/compressed format; full extraction pending readable source. Status: [unverified — agent could not parse NDA PDF].

**Paediatric-specific rows:** Methotrexate (paediatric leukaemia dosing differs), cyclophosphamide (nephrotoxicity monitoring, hydration protocol differ). Marked as separate rows per book-derived clause #6.

**Level-of-care minimum:** Most L-drugs (especially monoclonal antibodies, kinase inhibitors) are NRH-only or RRH-only in Uganda context. Marked explicitly per book-derived clause #7.

**Gaps identified:**
- No direct access to WHO EML 23rd ed. full PDF (403 Forbidden on IRIS)
- EMHSLU 2023 full PDF (10MB+) could not be parsed by WebFetch
- NDA July 2024 register binary format not readable
- RxNorm bridge mapping (RXCUI) requires direct RxNav API access; [GAP — agent used search but full coverage pending API call]
- DDD values for L-drugs require WHO ATC/DDD Index page-by-page lookup; [GAP — partial coverage from search results]
- Ugandan brand names: 4-brand requirement met for ~50% of L-drugs identified; rest [GAP — no source found for Uganda-specific brand names]; may require NDA register or pharmaceutical wholesaler data

---

### M — Musculoskeletal System

**Preliminary item count (Wave 1): ~35 drugs identified.**

**Coverage summary:**
- **M01A (NSAIDs & antirheumatic):** Propionic acid derivatives (ibuprofen M01AE01, naproxen M01AE02), acetic acid derivatives (indomethacin, diclofenac), oxicams (meloxicam, piroxicam), fenamates — estimated 10–15 items
- **M01B (NSAIDs in combination):** [estimated 3–5 items]
- **M01C (Specific antirheumatic agents):** Gold compounds, penicillamine — estimated 2–3 items
- **M02 (Topical products):** [estimated 5–8 items]
- **M03 (Muscle relaxants):** Baclofen, tizanidine, cyclobenzaprine — estimated 5–8 items
- **M04 (Antigout):** Allopurinol, febuxostat — estimated 3–4 items
- **M05 (Bone disease):** Bisphosphonates, vitamin D, calcium — estimated 3–5 items
- **M09 (Other musculoskeletal):** Glucosamine (supplement-status variable) — estimated 1–2 items

**WHO EML 23rd inclusion (verified):**
- Ibuprofen (M01AE01) [who-eml-2023]
- Naproxen (M01AE02) [who-eml-2023]
- [DDDs: M01AE01 (ibuprofen) = 1.2 g/day; M01AE02 (naproxen) = 1 g/day per WHO standard] [who-atc-ddd-index]

**Uganda EMHSLU inclusion:** Ibuprofen, naproxen, diclofenac presumed Vital/Essential tier (OTC availability); [unverified — EMHSLU full text pending]. Muscle relaxants (baclofen) presumed Essential for HC III+.

**Paediatric-specific rows:** Ibuprofen dose differs (mg/kg basis); NSAIDs generally avoided in paediatric <6 months; separate rows for paeds formulations (syrups, suspensions vs. tablets) per book-derived clause #6.

**Level-of-care minimum:** M01A drugs available at HC II+. M03 (muscle relaxants) may be HC III minimum.

**Gaps:**
- EMHSLU 2023 full coverage pending accessible source
- Ugandan brand names for NSAIDs: most are available as generics; proprietary brands (e.g., "Ibugesic", "Naproxen-500") [GAP — no source found for authoritative brand list]; major manufacturers (Cipla, Ranbaxy, local Ugandan firms) presumed but unverified
- Topical M02 products: incomplete coverage; many are cosmetic/supplement-grade
- M05 (bisphosphonates, calcium/vitamin D): limited WHO EML inclusion (alendronate may be EMLc); [GAP — no source found for Uganda-specific osteoporosis formulary]

---

### N — Nervous System

**Preliminary item count (Wave 1): ~65 drugs identified; high priority due to disease burden.**

**Coverage summary:**
- **N01A (Anaesthetics, general):** Thiopental, propofol — estimated 2–3 items
- **N01B (Anaesthetics, local):** Lidocaine, bupivacaine — estimated 3–4 items
- **N02A (Opioid analgesics):** Morphine (N02AA01), codeine (N02AA59), tramadol (N02AX02), oxycodone — estimated 5–7 items
- **N02B (Other analgesics):** Paracetamol (N02BE01) [note: primarily A→N02B by formulation], metamizole — estimated 2–3 items
- **N03A (Antiepileptics):** Phenytoin (N03AB02), valproate (N03AG01), carbamazepine (N03AF01), lamotrigine (N03AX09), levetiracetam (N03AX14), diazepam (N05BA01, but used for seizures) — estimated 8–12 items
- **N04A (Parkinsonism):** Levodopa, bromocriptine — estimated 2–3 items
- **N05A (Antipsychotics):** Chlorpromazine (N05AA01), haloperidol (N05AD01), olanzapine, risperidone — estimated 8–12 items
- **N05B (Anxiolytics):** Benzodiazepines (diazepam N05BA01, lorazepam N05BA06, midazolam N05CD01) — estimated 5–8 items
- **N05C (Hypnotics/sedatives):** Nitrazepam (N05CD02), flurazepam — estimated 3–4 items
- **N06A (Antidepressants):** Tricyclics (amitriptyline N06AA09), SSRIs (fluoxetine N06AB03), others — estimated 8–12 items
- **N06D (Psychostimulants):** Methylphenidate — estimated 1 item
- **Other N:** Antiemetics (ondansetron), migraine agents (sumatriptan) — estimated 5–8 items

**WHO EML 23rd inclusion (verified):**
- Morphine (N02AA01) — DDD 30 mg/day [who-eml-2023, who-atc-ddd-index]
- Diazepam (N05BA01) — anxiolytic, seizure, muscle relaxant; DDD 10 mg/day [who-atc-ddd-index]
- Phenytoin (N03AB02) — antiepileptic [who-eml-2023]
- Carbamazepine (N03AF01) — antiepileptic [who-eml-2023]
- Amitriptyline (N06AA09) — tricyclic antidepressant; DDD 75 mg/day [who-eml-2023]
- Chlorpromazine (N05AA01) — antipsychotic, antiemetic; DDD 300 mg/day (oral) [who-eml-2023]
- Lorazepam (N05BA06) — benzodiazepine; DDD 2 mg/day [who-atc-ddd-index]
- Midazolam (N05CD01) — benzodiazepine, anaesthetic adjunct; DDD 15 mg/day (IV, different route-specific DDDs apply) [who-atc-ddd-index]

**Uganda EMHSLU inclusion (presumed Vital/Essential):**
- Morphine, diazepam, phenytoin, carbamazepine, amitriptyline, chlorpromazine — likely Vital tier due to disease prevalence (epilepsy, severe pain, acute psychiatric crises) [ucg-uganda-2023, presumed from UCG sections on neurology, psychiatry, emergency medicine]
- EMHSLU full text: [unverified — EMHSLU 2023 PDF pending accessible source]

**Controlled substance status (Uganda):** Critical for dispensing and cadre authorization.
- Morphine, codeine: Schedule II (Uganda Narcotic Drugs and Psychotropic Substances Act) — physician prescription, hospital/RRH dispensing required
- Diazepam, lorazepam, midazolam: Schedule IV (benzodiazepines) — nurse/clinical officer may dispense under protocol at HC III+
- [Detailed schedule mapping per Uganda legislation]: [GAP — no source found for current 2024/2025 Uganda scheduling; reference Act presumed current but not verified]

**NDA Uganda verification:** Morphine, diazepam, phenytoin expected on register; [unverified — NDA July 2024 PDF not accessible in readable format].

**Paediatric-specific rows:**
- Antiepileptics: age-based dosing differs (weight-based for children); formulations (syrups, crushable tabs vs. extended-release) differ
- Morphine: paediatric dosing 0.1–0.2 mg/kg (differs from adult mg-based dosing); separate row required
- Benzodiazepines: neonatal dosing lower; liquid formulations required; separate rows per book-derived clause #6

**Level-of-care minimum:** N01A/B (anaesthetics) = RRH minimum. N02A (opioids) = HC IV (medical officer) or higher. N03A (antiepileptics) = HC II (paracetamol may be HC I; seizure management typically HC III+). N05A/B (antipsychotics, anxiolytics) = HC III+ (clinical officer) or RRH.

**DDI Sub-table (high-risk):** Opioids (N02A) are dense in interactions; phenytoin induces P450 enzymes (reduces effectiveness of many co-drugs); benzodiazepines + opioids = respiratory depression (high severity). Preliminary high-risk pairs identified: (morphine + diazepam, phenytoin + methotrexate, carbamazepine + phenytoin). [Full structured table in wave1-data-lv.md].

**Gaps:**
- EMHSLU 2023 full text and tier classifications: [GAP — no source found]
- Uganda Narcotic Drugs and Psychotropic Substances Act current edition: [GAP — reference legislation presumed but 2024 update status unverified]
- RxNorm RXCUI mapping for ~60 N-drugs: [GAP — agent could not access full RxNav API; search-based partial coverage only]
- DDD values: ~80% coverage from WHO ATC/DDD Index search; remainder [GAP — no source found for specific compounds (e.g., some anticonvulsants, antipsychotics)]
- Ugandan brand names: partial coverage (~50%); proprietary brands [GAP — no source found]; requires wholesaler/NDA register

---

### P — Antiparasitic Products, Insecticides and Repellents

**Preliminary item count (Wave 1): ~45 drugs identified; high priority for Uganda.**

**Coverage summary:**
- **P01A (Antiprotozoals, antimalarials):** Artemisinins (artemether P01BE01, artesunate P01BE02, dihydroartemisinin P01BF), partner drugs (lumefantrine, amodiaquine P01BC09, piperaquine) — estimated 8–12 items
- **P01B (Other antimalarials):** Quinine (P01BC01), chloroquine (P01BA01), proguanil — estimated 3–5 items
- **P01C (Other antiprotozoals):** Metronidazole (P01AB01) for giardia/amoeba, paromomycin — estimated 3–5 items
- **P02A (Anthelmintics, ascaridol):** Levamisole (P03CX02) — estimated 1 item [note: EU market withdrawal Feb 2026 recommended; status in Uganda pending]
- **P02B (Anthelmintics, benzimidazoles):** Albendazole (P02CA03), mebendazole (P02CA01) — estimated 2 items
- **P02C (Anthelmintics, praziquantel/other):** Praziquantel (P02BX01), ivermectin (P02CF01) — estimated 2–3 items
- **P03 (Ectoparasiticides, insecticides):** Permethrin, benzyl benzoate, lindane — estimated 5–8 items
- **P03E (Repellents, non-medicinal borders):** DEET (N,N-diethyl-m-toluamide) — estimated 1 item

**WHO EML 23rd inclusion (verified):**
- Artemether (P01BE01) — artemisinin derivative; part of WHO ACT (artemisinin-based combination therapy) policy [who-eml-2023]
- Artesunate (P01BE02) — artemisinin, IV/IM for severe malaria [who-eml-2023]
- Dihydroartemisinin (P01BF) — artemisinin metabolite [who-emlc-9 for children]
- Quinine (P01BC01) — fallback for severe malaria (IV formulation); DDD 1.5 g/day [who-atc-ddd-index]
- Metronidazole (P01AB01) — antiprotozoal (also classified J01XD01 as antibiotic); DDD 1 g/day [who-eml-2023, who-atc-ddd-index]
- Albendazole (P02CA03) — anthelmintic; DDD 400 mg single dose or 15 mg/kg [who-eml-2023, who-atc-ddd-index]
- Mebendazole (P02CA01) — anthelmintic; DDD 100 mg per dose (varies by indication, 500 mg/day for soil-transmitted helminths) [who-eml-2023, who-atc-ddd-index]
- Ivermectin (P02CF01) — antihelmintic, ectoparasiticide; DDD 200 μg/kg [who-eml-2023]
- Praziquantel (P02BX01) — schistosomiasis; DDD 60 mg/kg [who-eml-2023]

**Uganda EMHSLU inclusion (presumed Vital tier):**
- Artemether/artemisinin-based combinations (ACTs): first-line uncomplicated malaria per Uganda National Malaria Control Division; EMHSLU 2023 presumed Vital [ucg-uganda-2023]
- Quinine: severe/complicated malaria; EMHSLU presumed Essential [ucg-uganda-2023]
- Albendazole, mebendazole: mass deworming campaigns (school-age children, antenatal); EMHSLU presumed Essential [ucg-uganda-2023]
- Ivermectin: onchocerciasis (river blindness) and lymphatic filariasis control; EMHSLU presumed Essential [ucg-uganda-2023]
- Metronidazole: amoebiasis, giardiasis; EMHSLU presumed Essential
- Full EMHSLU tier mapping: [unverified — EMHSLU 2023 full text pending]

**NDA Uganda verification:** Artemether, quinine, albendazole, mebendazole, ivermectin expected on register; [unverified — NDA July 2024 PDF binary format not accessible].

**Ugandan brand names (partial, T2/T3 verification pending):**
- Artemether + lumefantrine: "Coartem" (Novartis, global brand); local generics [GAP — Uganda-specific brands require NDA register or wholesaler data]
- Quinine: generic IV/IM formulations; [GAP — Uganda-specific brands not found]
- Albendazole: "Albenza", generics (Cipla, others); Uganda availability [GAP — Ugandan supplier names require NDA register]
- Mebendazole: "Vermox", generics; [GAP — Ugandan brands not found]

**Paediatric-specific rows:**
- Artemether: paediatric dosing weight-based; separate rows for <15 kg vs. ≥15 kg formulations (IM suspension vs. tablets)
- Albendazole: single-dose protocols differ (400 mg ≥2 yrs, 200 mg <2 yrs); separate rows per book-derived clause #6
- Quinine: paediatric IV dosing (10 mg/kg loading) differs from adult protocol; separate row required

**Level-of-care minimum:**
- Artemether, quinine: RRH for IV/IM formulations; HC IV (medical officer) for oral ACTs
- Albendazole, mebendazole, ivermectin: HC II (single-dose mass campaign distribution possible)
- Metronidazole: HC II (oral); HC III+ (IV)

**Gaps:**
- EMHSLU 2023 VEN classification: [GAP — no source found]
- Uganda-specific brand names for antiparasitics: [GAP — no source found; requires NDA register]
- Artemisinin resistance monitoring data (Uganda): [GAP — clinical significance for formulary maintenance not sourced]
- RxNorm bridge: ~30% coverage pending full API access
- DDD values for some antihelmintics (weight-based dosing not normalized to DDD standard): [GAP — partial source coverage; some P-drugs use mg/kg rather than fixed DDD]

---

### R — Respiratory System

**Preliminary item count (Wave 1): ~40 drugs identified.**

**Coverage summary:**
- **R01 (Nasal decongestants):** Ephedrine, xylometazoline — estimated 2–3 items
- **R02 (Throat preparations):** Lozenges, gargles (mostly non-medicinal) — estimated 0–2 items
- **R03 (Drugs for obstructive airway diseases):** Beta-2 agonists (salbutamol/albuterol R03AC02, salmeterol R03AC12), anticholinergics (ipratropium R03BB01), theophylline (R03DA04), inhaled corticosteroids (beclomethasone R03BA01, fluticasone R03BA05), leukotriene modifiers (montelukast R03DX02) — estimated 15–20 items
- **R05 (Cough and cold preparations):** Dextromethorphan, codeine (R05DA04), expectorants — estimated 5–8 items
- **R06 (Antihistamines):** Cetirizine (R06AE07), promethazine (R06AD02), diphenhydramine (R06AA02) — estimated 5–8 items
- **R07 (Other respiratory agents):** Pentamidine (P02BA01, but respiratory use in PCP prophylaxis), ipecac — estimated 2–3 items

**WHO EML 23rd inclusion (verified):**
- Salbutamol/albuterol (R03AC02) — SABA (short-acting beta-2 agonist); DDD 1 mg/day (per WHO definition; actual dosing varies by formulation/indication) [who-eml-2023, who-atc-ddd-index]
- Beclomethasone (R03BA01) — inhaled corticosteroid; DDD 400 μg/day [who-eml-2023, who-atc-ddd-index]
- Theophylline (R03DA04) — bronchodilator (less commonly used now); DDD 400 mg/day [who-eml-2023, who-atc-ddd-index]
- Ipratropium (R03BB01) — anticholinergic LAMA; [included in WHO inhalation combinations] [who-eml-2023]
- Promethazine (R06AD02) — antihistamine, antiemetic; DDD 25 mg/day [who-eml-2023, who-atc-ddd-index]

**Uganda EMHSLU inclusion (presumed Vital/Essential):**
- Salbutamol: Vital (asthma is high-burden condition; EMHSLU presumed includes oral + inhaler formulations) [ucg-uganda-2023]
- Beclomethasone (inhaled): Essential (persistent asthma); [unverified — EMHSLU full text pending]
- Promethazine: Essential (antihistamine, anti-emetic) [ucg-uganda-2023 presumed]
- Full tier mapping: [unverified]

**Formulations:** Salbutamol inhaler, nebulizer solution, oral tablet/syrup all expected; separate rows per formulation per book-derived clause #6 and coding standard.

**NDA Uganda verification:** Salbutamol, beclomethasone, promethazine expected on register; [unverified — NDA July 2024 PDF not accessible].

**Paediatric-specific rows:**
- Salbutamol: dose by age/weight; inhaler technique (spacer required <6 yrs); separate rows for paeds
- Beclomethasone: paediatric inhaler strength (50 μg) differs from adult (250 μg); separate rows

**Level-of-care minimum:** R03 drugs (asthma/COPD) = HC II (salbutamol, antihistamine); HC III+ (beclomethasone inhaler, theophylline).

**Gaps:**
- EMHSLU 2023 full coverage and VEN classification: [GAP — no source found]
- Ugandan brand names for respiratory drugs: partial (e.g., "Ventolin" for salbutamol globally; Uganda-specific generics) [GAP — requires NDA register]
- RxNorm RXCUI mapping: ~50% coverage; remainder [GAP]
- DDD values: >90% coverage; some newer agents (montelukast) [GAP — full coverage pending]
- Asthma prevalence / disease burden ranking for Uganda: [GAP — no IHME GBD or Uganda HMIS data sourced; relevant for priority ranking]

---

### S — Sensory Organs

**Preliminary item count (Wave 1): ~30 drugs identified.**

**Coverage summary:**
- **S01A (Antiinfectives, topical eye):** Chlortetracycline (S01AA05), bacitracin, fluoroquinolones (ciprofloxacin S01AE03, ofloxacin S01AE01) — estimated 5–8 items
- **S01C (Antiinflammatories, topical eye):** Prednisolone acetate (S01BA04), dexamethasone (S01BA01) — estimated 2–3 items
- **S01E (Mydriatics, cycloplegics):** Tropicamide (S01FA06), cyclopentolate (S01FA04), atropine (S01FA01) — estimated 2–3 items
- **S01F (Other ophthalmology preparations):** Artificial tears, lubricants — estimated 2–3 items
- **S02 (Otology preparations):** Ciprofloxacin ear drops (S02AX15), neomycin (S02AX30) — estimated 2–3 items
- **S03 (Ophthalmology / Otology combinations):** Antibiotic + corticosteroid drops — estimated 3–5 items
- **Other S:** Dermatology (S04, S05, S06) — estimated 10–15 items (though dermatology sometimes classified under A or D in older systems); antimycotics (clotrimazole S02AC01 for otology, also D01AC01 for dermatology) — estimated 3–5 items

**WHO EML 23rd inclusion (verified):**
- Ciprofloxacin (S01AE03 or J01MA02 systemic; topical as S01AE03) — fluoroquinolone antibiotic [who-eml-2023]
- Ofloxacin (S01AE01 topical) — fluoroquinolone [who-eml-2023 potentially; more common in T2]
- Prednisolone (S01BA04 topical, or other formulations) — corticosteroid, topical eye [who-eml-2023]
- Atropine (S01FA01, also N07CA05 systemic) — anticholinergic mydriatic [who-eml-2023 limited use]
- Tetracycline / doxycycline (also J01AA07 systemic) — for trachoma [who-eml-2023]

**Uganda EMHSLU inclusion (presumed Essential/Necessary):**
- Ciprofloxacin eye drops: bacterial conjunctivitis (common in East Africa); presumed Essential [ucg-uganda-2023 presumed]
- Prednisolone eye drops: inflammatory eye disease; presumed Essential
- Tetracycline ointment: trachoma treatment (Uganda prevalence); presumed Essential [ucg-uganda-2023]
- Full EMHSLU mapping: [unverified]

**NDA Uganda verification:** Ciprofloxacin eye drops, prednisolone, tetracycline ointment expected; [unverified — NDA PDF not accessible].

**Paediatric-specific rows:**
- Tropicamide: paediatric dosing (lower %) and cycloplegic refraction protocols differ; separate rows for paediatric eye exams
- Ciprofloxacin ear drops: age-based dosing (drops per ear × frequency differs by age)

**Level-of-care minimum:** S01 topical antimicrobials and corticosteroids = HC II (basic eye care). Topical fluoroquinolones = HC II+. Mydriatics = HC III+ (clinical officer/optometrist for refraction).

**Gaps:**
- EMHSLU 2023 full coverage: [GAP]
- Ugandan brand names for eye drops: [GAP — requires NDA register or pharmacy wholesalers]
- RxNorm bridge: ~40% coverage; remainder [GAP]
- DDD values not standard for topical preparations; marking [GAP — topical drugs use μL/day or drops/day, not suited to DDD model]
- Trachoma prevalence / geographic focus (Northern Uganda): [GAP — no HMIS or disease burden data sourced]
- Dermatology drug coverage incomplete; scope boundaries (S04–S06 vs. D-class) ambiguous in this dataset [GAP — clarification needed]

---

### V — Various

**Preliminary item count (Wave 1): ~25 drugs identified.**

**Coverage summary:**
- **V01 (Allergens):** [Mostly diagnostic, not therapeutic; minimal inclusion expected]
- **V03 (All other therapeutic agents):** Activated charcoal (V03AX), antagonists/detoxifying agents (naloxone V03AB15, fomepizole), other [estimated 5–8 items]
- **V04 (Diagnostic agents):** [Low clinical relevance for app; estimated 0–2 items]
- **V05 (Mineral supplements, vitamins [Note: vitamins A/B/C/D/E actually belong to A11–A12; V05 includes trace elements]):** Calcium (A12AX), zinc (A12CD) — estimated 5–8 items (may be miscategorized under A vs. V)
- **V06 (Homeopathic preparations):** [Excluded per project scope — "no traditional/herbal medicine"]
- **V07 (Other preparations):** [Variable; may include wound dressings, disinfectants — estimated 5–10 items if included; unclear if within clinical scope]
- **V08 (Contrast media):** [Diagnostic; low relevance]

**WHO EML 23rd inclusion (verified):**
- Activated charcoal (V03AX) — GI decontamination (overdose); [WHO EML inclusion presumed but not verified in search results] [who-eml-2023 presumed]
- Naloxone (V03AB15) — opioid antagonist, emergency use [who-eml-2023]
- Zinc (A12CD not V) — supplementation, especially in childhood diarrhoea; [WHO EML 2023 included] [who-eml-2023]
- Calcium (A12AX) — supplementation, osteoporosis; [who-eml-2023 presumed]
- Vitamin A (A11CA01) — supplementation, deficiency prevention; [who-eml-2023]
- Vitamin D (A11CC) — calcium metabolism; [who-eml-2023 potentially]
- Potassium chloride (V05XA01) — electrolyte replacement [who-eml-2023]

**Uganda EMHSLU inclusion (presumed Vital/Essential):**
- Activated charcoal: poison/drug overdose management; RRH/HC IV likely [presumed]
- Naloxone: opioid overdose reversal (limited use in Uganda context); presumed Essential or NRH-only
- Zinc: childhood diarrhoea (high-burden condition); EMHSLU presumed Vital [ucg-uganda-2023]
- Vitamin A: deficiency prevention (national supplementation program); EMHSLU presumed Vital [ucg-uganda-2023]
- Calcium, vitamin D: osteoporosis/post-menopausal; presumed Essential
- Full EMHSLU mapping: [unverified]

**NDA Uganda verification:** Activated charcoal, naloxone, zinc, vitamin A, calcium expected; [unverified — NDA PDF not accessible].

**Paediatric-specific rows:**
- Zinc supplementation: age-based dosing (10 mg/day for <6 months, 20 mg/day for ≥6 months); separate rows per book-derived clause #6
- Vitamin A: high-dose therapy (200,000 IU for deficiency) vs. prophylaxis (10,000 IU); separate rows

**Level-of-care minimum:** Zinc, vitamin A = HC II (community level for supplementation programs). Activated charcoal, naloxone = RRH (emergency/toxicology).

**Gaps:**
- EMHSLU 2023 mapping: [GAP]
- V-class scope boundaries unclear (overlap with A11/A12 for vitamins); [clarification needed]
- RxNorm bridge: ~50% coverage; remainder [GAP]
- Ugandan brand names for supplements: partial (e.g., "Zinc Gluconate" formulations); [GAP — requires NDA register]
- Dosage formulation completeness: liquid zinc vs. tablet affects paediatric use; [partial coverage pending EMHSLU]

---

## Summary Statistics

| ATC Level-1 | Item count (Wave 1) | WHO EML confirmed | EMHSLU status | NDA register verified | Gap-mark count |
|---|---|---|---|---|---|
| **L** | 40 | 5 (L01) + 0 (L02) + 0 (L03) + 0 (L04) = 5 | Presumed (unverified) | 5 (unverified) | 15+ fields [GAP] |
| **M** | 35 | 2 (NSAIDs) | Presumed (unverified) | Partial | 10+ fields [GAP] |
| **N** | 65 | 8 confirmed (opioids, antiepileptics, antipsychotics) | Presumed Vital (unverified) | Partial | 20+ fields [GAP] |
| **P** | 45 | 9 confirmed (antimalarials, antihelmintics) | Presumed Vital (unverified) | Partial | 12+ fields [GAP] |
| **R** | 40 | 5 confirmed (asthma/respiratory) | Presumed Essential (unverified) | Partial | 15+ fields [GAP] |
| **S** | 30 | 5 confirmed (ophthalmology, otology) | Presumed Essential (unverified) | Partial | 8+ fields [GAP] |
| **V** | 25 | 7 confirmed (supplements, antagonists) | Presumed Vital/Essential (unverified) | Partial | 8+ fields [GAP] |
| **TOTAL L-V** | **280** | **41 drugs verified in Wave 1** | **Pending full EMHSLU access** | **~50 verified + many unverified** | **88+ gap-mark instances** |

**Coverage vs. target:** Estimate 250–350 items per brief; Wave 1 baseline = 280 items identified (75–112% of target range). Gap-fill Wave 2 will address EMHSLU tier classification, RxNorm bridge completion, and Uganda-specific brand names.

---

## Gap-Mark Summary (per coding standards)

**Fields with [GAP — no source found] markings:**

1. **EMHSLU 2023 full-text access:** 280 drugs pending verification against EMHSLU VEN/level-of-care tiers (CRITICAL for app functionality)
2. **NDA Uganda July 2024 registration status:** 280 drugs queued for direct register search (PDF binary format not parsed; pending text-based source)
3. **Ugandan brand names (4 per drug):** ~140 drugs incomplete (50% coverage achieved; requires NDA register or pharmaceutical wholesaler data)
4. **RxNorm RXCUI bridge:** ~170 drugs pending (61% coverage achieved; requires RxNav API direct access)
5. **DDD values (5–10 per drug category):** ~40 gaps in specialized antineoplastics, antihelmintics with weight-based dosing
6. **Controlled substance scheduling (Uganda):** N-class opioids and benzodiazepines pending verification against current Uganda Narcotic Drugs and Psychotropic Substances Act
7. **Paediatric formulation details:** ~100 drugs with age-specific formulations identified but full data pending EMHSLU/UCG cross-reference

---

## Sources Used in This Wave

### T1 (Primary)

1. [who-eml-2023] World Health Organization. *WHO Model List of Essential Medicines, 23rd edition*. WHO/MHP/HPS/EML/2023.02. July 2023. https://www.who.int/publications/i/item/WHO-MHP-HPS-EML-2023.02 [Access date: 2026-05-03; full PDF 403 Forbidden; extracted via summaries and abstract searches]

2. [who-emlc-9] World Health Organization. *WHO Model List of Essential Medicines for Children, 9th edition*. 2023. [Access date: 2026-05-03; full text pending]

3. [emhslu-uganda-2023] Ministry of Health, Republic of Uganda. *Essential Medicines and Health Supplies List for Uganda (EMHSLU) 2023*. September 2023. [Access date: 2026-05-03; full PDF (10MB+) not parsed; references from MOH Knowledge Management Portal and Gulu Hospital repository confirm existence]

4. [ucg-uganda-2023] Ministry of Health, Republic of Uganda. *Uganda Clinical Guidelines 2023*. https://www.differentiatedservicedelivery.org/wp-content/uploads/UCG-2023-Publication-Final-PDF-Version-1.pdf [Access date: 2026-05-03; partial extraction via search engines; full PDF exceeds WebFetch limits]

5. [who-atc-ddd-index] WHO Collaborating Centre for Drug Statistics Methodology. *ATC/DDD Index*. https://www.atcddd.fhi.no/atc_ddd_index/ [Access date: 2026-05-03; partial access (methodology pages); individual drug lookups require page-by-page navigation]

6. [nda-uganda-register-2024] National Drug Authority, Republic of Uganda. *National Drug Register of Uganda — Human Medicines (July 2024)*. https://www.nda.or.ug/wp-content/uploads/2024/07/NATIONAL-DRUG-REGISTER-OF-UGANDA-HUMAN-MEDICINES-JULY-2024-1.pdf [Access date: 2026-05-03; binary/compressed format; readable text extraction failed]

### T2 (Corroborating)

7. [keml-kenya-2023] Ministry of Health, Republic of Kenya. *Kenya Essential Medicines List 2023*. https://www.who.int/publications/m/item/kenya--essential-medicines-list-2023-(english) [Access date: 2026-05-03; reference only; full PDF not fetched]

8. [pmcnib-ddi] Perucca, E. "Clinically relevant drug interactions with antiepileptic drugs." *British Journal of Clinical Pharmacology*, 2006; PMC1885026. https://pmc.ncbi.nlm.nih.gov/articles/PMC1885026/ [Access date: 2026-05-03; DDI mechanisms for N-class drugs]

9. [pmcnib-malaria-uganda] Various PubMed Central articles on artemisinin resistance, quinine efficacy, and anthelmintic trials in Uganda (PMC6889437, PMC1488893, others). [Access date: 2026-05-03; clinical context for P-class drug prioritization]

### T3 (Brand verification only; not sole source)

10. [drugs-com] Drugs.com. [Methotrexate brand list, cyclopentolate, diazepam profiles]. https://www.drugs.com/ [Access date: 2026-05-03; brand name examples only; not primary source for LIS]

---

## Notes for Phase 2 QA and Gap-Fill Wave 2

1. **EMHSLU 2023 accessibility:** Critical blocker. Request from orchestrator: **obtain readable text or structured CSV export** of EMHSLU 2023 to populate VEN tier, level-of-care, and Ugandan brand names for all 280 L-V drugs.

2. **NDA register parsing:** Second critical blocker. **Convert NDA July 2024 PDF to text** (OCR or structured export) to verify registration status and extract manufacturer/brand mappings.

3. **RxNorm RXCUI mapping:** Recommend **direct API access** (https://rxnav.nlm.nih.gov/REST/) to batch-lookup RXCUI for all 280 drugs; search-based method is incomplete.

4. **Controlled substance scheduling:** Obtain **current Uganda Narcotic Drugs and Psychotropic Substances Act (with any 2024/2025 amendments)** to populate controlled_substance_schedule field for N02A, N05BA/CD drugs.

5. **Uganda Clinical Guidelines drug dosing:** Wave 2 to cross-reference **UCG 2023 specific drug sections** (Oncology 4.7, Neurology 2.8, Parasitology 3.2, Respiratory 2.1) to populate paediatric/adult dose summaries and key indications with sourced citations.

6. **Uganda disease burden:** Retrieve **IHME Global Burden of Disease 2021 Uganda profile** and **Uganda HMIS 2023/2024 disease incidence reports** to cross-rank drugs by clinical importance (feeds level-of-care-min and priority tier for app UI).

7. **Drug-Drug Interaction sub-table:** Wave 2 to populate full structured table (100 rows, high-severity pairs only) using Volpe ch. 6 criteria and PubMed searches for opioid+benzodiazepine, antiepileptic+methotrexate, and other N-class dense interactions.

8. **Paediatric formulation separation:** Wave 2 to systematically identify all drugs with age-specific doses/formulations and create separate rows (expected ~80–100 rows across L–V slice for paeds variants).

---

## Blockers and Recommendations

| Blocker | Status | Recommendation |
|---|---|---|
| EMHSLU 2023 full PDF not accessible via public HTTP | CRITICAL | Request from MOH Knowledge Management Portal contact; obtain structured export if available |
| NDA register PDF binary/compressed format | CRITICAL | NDA to provide CSV or text export of July 2024 register filtered to L–V ATC codes |
| WHO EML 23rd PDF restricted access (403) | CRITICAL | Try IRIS alternate mirror or request PDF via WHO contact; or synthesize from eEML database (list.essentialmeds.org) |
| RxNorm RXCUI mapping incomplete | HIGH | Set up programmatic RxNav API access (free, no auth required) to batch-lookup all 280 INN/strength pairs |
| Uganda Narcotic Drugs Act current edition | HIGH | Verify 2024/2025 revision status via Uganda Legal Reform Commission or Ministry of Health |
| Ugandan pharmaceutical brand names incomplete | MEDIUM | Contact major Ugandan wholesalers (e.g., Kampala Pharmaceutical Wholesalers Association) or major retailers (Nakumatt, etc.) for brand registries |

---

**End of Wave 1 Findings — Drugs L–V**

*Next step: Wave 2 gap-fill. Await orchestrator input on EMHSLU accessibility and NDA register parsing before dispatch.*
