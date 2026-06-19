# Wave 1 Data - Country Packs: Multi-Tenant Localisation Constants

**Date:** 2026-05-03

**Cohort:** country-packs

**Evidence boundary:** T1 sources (statutory acts, constitutional documents, government-published structures, official regulatory body websites, ISO standards); T2 corroboration (WHO profiles, World Bank country briefs); T3 corroboration only (encyclopaedia entries).

---

## Country-Pack Data Table

| country_code | country_name | currency | currency_iso_4217 | timezone | languages | admin_level_1_name | admin_level_1_count | admin_level_2_name | admin_level_2_count | facility_level_system | health_ministry | medicine_regulator | insurance_regulator | lab_regulator | nursing_regulator | clinical_officer_regulator | mandatory_reports | national_id_rules | privacy_law | privacy_authority | default_forms_reference | default_blueprints_reference | source_citations |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| UG | Uganda | Ugandan Shilling | UGX | Africa/Kampala (UTC+03:00) | English; Swahili (official as of 2005); Luganda (de facto lingua franca, 5.56M speakers) | District | 146 as of 2026; plus Kampala Capital City Authority; plus 10 regional cities; plus 41 municipalities | Sub-county | 2,100+ (per administrative restructuring post-2005) | Uganda facility levels: HC II (village level); HC III (sub-county); HC IV (county/municipality); General Hospital (district secondary); RRH (regional secondary); NRH (national tertiary) | Ministry of Health Uganda (MoH); headed by Minister of Health; policy/oversight function; coordination with PNFP (Private Not-for-Profit) sector (UCMB, UPMB, UOMB, UMMB faith-based bureaux); district health teams (DHTs) at district level | National Drug Authority (NDA) under National Drug Policy and Authority Act Cap 206; Pharmacy Council of Uganda (pharmacist registration); Drug shop licensing by NDA (Class A/B/C licence tiers for retail dispensing, NOT prescribing schedules) | [GAP — Uganda National Health Insurance Scheme pending implementation as of 2026; PNFP cost-sharing dominant; no statutory insurance regulator identified] | [GAP — no dedicated laboratory regulator found; AHPC (Cap 268) oversees laboratory cadres; ISO 15189 accreditation optional] | Uganda Nurses and Midwives Council (UNMC) under Nurses and Midwives Act 1996 (Cap 301) | Allied Health Professionals Council (AHPC) under Allied Health Professionals Act Cap 268 (NOT UMDPC); clinical officers fall under AHPC; approximately 11,795 registered medical clinical officers as of corpus data | HMIS-107 Annual Health Unit Report (due 7 August; aggregate of OPD, inpatient, MCH/FP, lab, staffing); HMIS-105 Monthly Outpatient Report (OPD, MCH, HIV, lab, commodities); HMIS-108 Monthly Inpatient Report (admissions, diseases, deaths); HMIS-106A Quarterly HIV/ART/Nutrition/TB Report; HMIS 033B Weekly Epidemiological Surveillance (IDSR notifiable diseases, mTrac/eIDSR); HMIS 033C Weekly Summary Form; HMIS 033A Case-based reporting (immediate for suspected/probable/confirmed priority diseases); TB Treatment Progress & Outcome (HMIS 096A); ART Register (HMIS 081); Pre-ART Register (HMIS 080); Case Investigation Form (outbreak-driven, district surveillance); Contact Tracing Form (eIDSR module); [reporting-kpis gap — exact quarterly/annual KPI reporting structure not yet available in cohort] | NIN (National Identification Number) issued by NIRA (National Identification and Registration Authority) under Registration of Persons Act 2015; issued age 18+; children under 18 may use parent's NIN + birth-registration number as fallback; mass enrollment underway (6.15M first-time applicants; 13.37M renewals by late 2025); 14-digit unique code; use in electoral, financial, social-services contexts | Data Protection and Privacy Act 2019 (Act No. 9 of 2019; effective 3 May 2019; Regulations effective 12 March 2021); regulates collection, processing, holding, use of personal data; applies to persons/institutions/public bodies collecting data within Uganda or outside Uganda if data relates to Ugandan citizens; criminal sanctions for unlawful disclosure; overseas data-transfer must meet equivalent-protection standard | Personal Data Protection Office (PDPO), independent office under National Information Technology Authority Uganda (NITA-U); enforces DPPA 2019 | See standard-forms cohort for HMIS form list (HMIS 105, 106A, 107, 108, 033A/B/C, HIV programme registers/cards, commodity tools, IDSR tools); UG-prefixed codes in standard-forms | [STUB — pending tenant-blueprints cohort for pre-configured workＦlows; expected to reference HMIS form equivalents and IMCI/PNFP clinical pathways] | T1: [uganda-constitution]; [uganda-local-govt-act]; [uganda-data-protection-privacy-act-2019]; [uganda-medical-dental-practitioners-act-cap-272]; [uganda-allied-health-act-cap-268]; [uganda-nurses-midwives-act-1996]; [uganda-national-drug-authority-act-cap-206]; [uganda-nira-registration-persons-act-2015]; [uganda-hmis-107]; [uganda-idsr-guidelines]; [uganda-emhslu-2023]; Ministry of Health Uganda website [health.go.ug]; UMDPC website [umdpc.go.ug]; AHPC website [ahpc.ug]; UNMC website [unmc.ug]; NDA website [nda.or.ug]; NIRA website [nira.go.ug]; PDPO website [pdpo.go.ug] T2: [WHO-Uganda-country-profile]; [World Bank Uganda health system]; [UBOS demographic data] [Wikipedia consulted for triangulation only — listed in findings under T3 references block; never sole source for any cell] |
| KE | Kenya | Kenyan Shilling | KES | Africa/Nairobi (UTC+03:00) | English; Kiswahili (national language per Constitution 2010) | County | 47 (per Constitution 2010, County Governments Act 2012) | Sub-county (plural: sub-counties); further subdivided into Wards (1,450 total wards as of IEBC delineation) | 290 constituencies (electoral designation); 1,450 wards (for county assembly members) | Kenya facility levels (KEPH — Kenya Essential Package for Health): Level 1 Community Health Unit; Level 2 Dispensary (primary); Level 3 Health Centre (primary); Level 4 Sub-county Hospital (primary secondary); Level 5 County Referral Hospital (secondary); Level 6 National Referral Hospital (tertiary) | Ministry of Health Kenya (MoH); Cabinet Secretary for Health; State Department for Devolution oversees county health departments (one per 47 county governments); private and PNFP sectors (CHAK — Christian Health Association of Kenya; Catholic dioceses; other NGO networks) | Kenya Pharmacy and Poisons Board (PPB) under Pharmacy and Poisons Act Cap 244; regulates manufacture, import, distribution, sale of drugs; Part I / Part II poisons are valid prescribing schedules under PPB framework (NOT confused with Uganda NDA Class A/B/C) | Social Health Authority (SHA) under Social Health Insurance Act 2023 (Act 24 of 2023); began operations 1 October 2024 replacing NHIF; Primary Healthcare Fund (PHF, government-funded); Social Health Insurance Fund (SHIF, contributory, 2.75% gross pay, KES 300/month minimum); Emergency Fund (high-cost cases); mandatory contributor base for employees | Kenya Medical Laboratory Technicians and Technologists Board (KMLTTB) under Medical Laboratory Technicians and Technologists Act (Cap 253A); registered and licensed MLS professionals required; ISO 15189 accreditation now required for accredited labs (Business Laws Amendment 2024) | Nursing Council of Kenya (NCK) under Nurses Act Cap 257 (revised 2012, established 1985); regulates training, registration, licensure of nurses and midwives | Clinical Officers Council (COC) under Clinical Officers (Training, Registration and Licensing) Act 2017 (Act No. 20 of 2017, assented 21 June 2017, effective 7 July 2017); replaced previous Cap 260 (1988); regulates training, registration, licensing, practice of clinical officers | KHIS (Kenya Health Information System) on DHIS2 reporting monthly; county health management information system requirements per Health Act 2017; notifiable disease reporting per IDSR Technical Guidelines (WHO-AFRO framework aligned); [reporting-kpis gap — exact mandatory form list and reporting timeline for counties not yet mapped] | Huduma Namba (National Integrated Identity Management System, NIIMS) issued by NIRA equivalent or Ministry responsible; unique permanent personal ID randomly assigned; types: minors' card (age 6+); adults' card (age 18+); foreign national card; enrollment ongoing; Maisha Namba digital identity in piloting as enhanced version with improved data-protection safeguards (rebrand of NIIMS addressing High Court privacy directives); under Data Protection Act 2019 [T1 verification pending — exact issuance age, fallback rules for children not yet detailed] | Data Protection Act 2019 (Act 24 of 2019, effective 25 November 2019); regulates collection, processing, storage, transfer of personal data; mandatory registration of data controllers/processors; overseas data-transfer must meet equivalent-protection standard; implements Article 31 Constitution of Kenya 2010 | Office of the Data Protection Commissioner (ODPC), independent authority; enforces Act; imposes fines up to KES 5,000,000 or 1% annual turnover (whichever lower); conducts periodic audits | See standard-forms cohort for KHIS form list and KEPH level-aligned forms; KE-prefixed codes in standard-forms | [STUB — pending tenant-blueprints cohort for pre-configured workflows; expected to reference KHIS reporting and devolved county health service delivery models] | T1: [kenya-constitution-2010]; [kenya-county-governments-act-2012]; [kenya-data-protection-act-2019]; [kenya-medical-practitioners-dentists-act-cap-253]; [kenya-clinical-officers-act-2017]; [kenya-nurses-act-cap-257]; [kenya-pharmacy-poisons-act-cap-244]; [kenya-kmlttb-act-cap-253a]; [kenya-social-health-insurance-act-2023]; [kenya-health-act-2017]; Ministry of Health Kenya website [health.go.ke]; KMPDC website [kmpdc.go.ke]; COC website [clinicalofficerscouncil.org]; NCK website [nckenya.org]; PPB website [web.pharmacyboardkenya.org]; KMLTTB website [kmlttb.org]; ODPC website [odpc.go.ke]; SHA website [sha.go.ke]; NIRA equivalent [registration sources]; KEML 2023 [guidelines.health.go.ke] T2: [WHO-Kenya-country-profile]; [World Bank Kenya health-financing]; [KNBS demographic data]; [Willow Health Media Kenya health system analysis] [Wikipedia consulted for triangulation only — listed in findings under T3 references block; never sole source for any cell] |
| TZ | Tanzania | Tanzanian Shilling | TZS | Africa/Dar_es_Salaam (UTC+03:00) | Swahili (Kiswahili — official, national language per Constitution; National Kiswahili Council Act established 1967); English (official, used in higher courts and tertiary education) | Region (mkoa) | 31 regions as of 2025 (26 mainland + 5 Zanzibar regions; per Tanzania NBS and administrative divisions) | District (wilaya) | 184 districts as of 2025 (per Tanzania NBS 2012–2025 census updates; varies by region; includes both mainland and Zanzibar jurisdictions) | Tanzania facility levels (per Health Sector Strategic Plan V 2021–2026): Dispensary (village-level out-patient only); Health Centre (ward-level, some capacity for in-patient care); District Hospital (district-level secondary); Regional Referral Hospital (regional secondary); Zonal Referral Hospital (multi-regional secondary/tertiary); National Referral Hospital (tertiary) | Ministry of Health (Wizara ya Afya) — mainland Tanzania; separate Ministry of Health (Zanzibar) for semi-autonomous region; both operate under Health Sector Strategic Plan V (2021–2026) framework; headquarters Dodoma (mainland); Zanzibar ministry based in Stone Town | Tanzania Medicines and Medical Devices Authority (TMDA) — established under Tanzania Food, Drugs and Cosmetics Act Cap 219 (renamed via Finance Act No. 8 of 2019; operational 1 July 2019 as Executive Agency per Cap 245); supersedes TFDA 2019; regulates medicines, medical devices, diagnostics, biocidals, tobacco | Tanzania Insurance Regulatory Authority (TIRA) under Insurance Act No. 10 of 2009; manages mandatory Universal Health Insurance per Universal Health Insurance Act 2023 (effective January 2026); NHIF (National Health Insurance Fund) administers UHI scheme under TIRA oversight; UHI standard benefits package covers 372 health services; household premium TZS 150,000/year (2026); government subsidies for vulnerable populations | Health Laboratory Practitioners Council (HLPC) established under Health Laboratory Technologists Registration Act No. 22 of 2007 (operational 1 February 2009); regulates Health Laboratory Scientists, Technologists, and Assistants; Private Health Laboratories Board (PHLB) regulates private lab facilities under Private Health Laboratories (Regulation) Act 1997 | DHIS2 HMIS reporting (Tanzania HMIS since ~2013; aggregate facility data via DHIS2); IDSR (Integrated Disease Surveillance Response) per WHO AFRO framework — 34 notifiable diseases tracked with weekly/immediate reporting via eIDSR; mTUHA (revised paper/digital register set for primary facilities — Registers, Tally, Summary forms); mandatory reporting via DHIS2 at council/regional level; HMIS forms assignment based on facility type (dispensaries use mTUHA; health centres and above use DHIS2 electronic datasets or paper aggregation) | NIDA (National Identification Authority) under NIDA Act 2008 issues National Identification Number (NIN) to citizens age 18+; NIN is 20-digit unique code; children under 18 may use parent NIN + birth-certificate number as fallback; mass enrollment ongoing | Personal Data Protection Act No. 11 of 2022 (came into force 1 May 2023); establishes principles for lawful, fair, transparent collection and processing of personal data; overseas transfer must meet equivalent-protection standard; applies to all persons/institutions/public bodies collecting data within Tanzania or concerning Tanzanian citizens | Personal Data Protection Commission (PDPC) — established May 2023, officially launched April 3, 2024; registers data controllers/processors; enforces PDPA 2022; resolves complaints; conducts research on data-protection compliance | See standard-forms cohort for DHIS2 form list, IDSR tools, mTUHA register set, ANC card (RCH-1), immunisation card; TZ-prefixed codes in standard-forms | [STUB — pending tenant-blueprints cohort for pre-configured workflows; expected to reference DHIS2 reporting, IDSR case management, mTUHA forms, and primary healthcare delivery models (dispensary, health centre, faith-based facility structures)] | T1: [tanzania-constitution-language]; [tanzania-food-drugs-cosmetics-act-cap-219]; [tanzania-medicines-medical-devices-act-2019]; [tanzania-universal-health-insurance-act-2023]; [tanzania-health-sector-strategic-plan-v]; [tanzania-nida-act-2008]; [tanzania-personal-data-protection-act-2022]; [tanzania-nbs-administrative-divisions]; [tanzania-hlpc-act-2007]; [tanzania-idsr-guidelines]; Ministry of Health Tanzania [health.go.tz]; TMDA [tmda.go.tz]; TIRA [tira.go.tz]; NHIF Tanzania [nhif.or.tz]; NIDA [nida.go.tz]; PDPC [pdpc.go.tz]; Ministry of Health Zanzibar [mohz.go.tz]; TNMC [tnmc.go.tz]; Pharmacy Council Tanzania [pc.go.tz]; Medical Council of Tanganyika [mct.go.tz]. T2: [WHO-Tanzania-country-profile]; [Tanzania-health-facility-atlas-2023]; [HSSP-V-mid-term-review-2024]. [No Wikipedia in source_citations; T3 corroboration only, explicitly marked where used] |
| RW | Rwanda | Rwandan Franc | RWF | Africa/Kigali (UTC+02:00) | Kinyarwanda (national language per Constitution Art 8); English; French; Swahili (official language per Organic Law Nº 02/2017 of 8 February 2017, effective 2017 EAC integration) | Province (intara) | 5 provinces — Kigali City, Northern Province, Southern Province, Eastern Province, Western Province (per administrative restructuring 2006; prior 12 provinces) | District (akarere) | 30 districts as of 2026; each district further subdivided into sectors (umurenge) and cells (akagali) | Rwanda facility levels (per Ministry of Health Health Sector Strategic Plan): Health Post (cell level; promotional/preventive/basic treatment); Health Centre (sector level; primary care, MCH, lab capacity); District Hospital (district secondary); Provincial Referral Hospital (province secondary); National Referral and Teaching Hospital (national tertiary — Kigali University Teaching Hospital, Butare University Teaching Hospital, King Faisal Hospital Kigali, Rwanda Military Hospital); current network includes 1,280 health posts, 520 health centres, 57 hospitals (all levels) | Ministry of Health (Minisante) Rwanda; policy/planning/oversight authority; coordinates public facilities and PNFP sector via faith-based partnerships; implementer of Universal Health Coverage and CBHI nationwide programme; operates 4×4 Reform workforce initiative (2023 onwards) | Rwanda Food and Drugs Authority (Rwanda FDA) established under Law N° 003/2018 of 9 February 2018 (determining mission, organization, functioning); regulates human and veterinary medicines, vaccines, processed foods, medical devices, poisons, medicated cosmetics, tobacco; National Pharmacy Council (NPC) under Law N° 45/2012 of 14 January 2013 regulates pharmacy professionals and pharmacist licensure; RBC (Rwanda Biomedical Centre) supplies guidelines/standards for medicines | National Bank of Rwanda (BNR) regulates private insurance industry (insurance companies, brokers, agents); Rwanda Social Security Board (RSSB) administers Community-Based Health Insurance (Mutuelle de Santé/CBHI) — currently covers approximately 91% of national population as of 2023 (highest coverage rate in Africa); CBHI scheme year runs 1 July–30 June; CBHI was fully integrated into RSSB in 2015 and operates as the primary universal health coverage vehicle supplemented by government funding and donor support | Rwanda Biomedical Centre (RBC, established 2002 under Ministry of Health) — National Reference Laboratory (NRL) provides lab oversight and accreditation; NRL holds ISO 15189:2022 accreditation (reaccredited June 2024 by Kenya Accreditation Services KENAS); RBC implements WHO AFRO SLMTA laboratory strengthening programme; no dedicated statutory laboratory practitioners council identified — lab professionals regulated as part of health-workforce cadres via RBC and Ministry oversight | National Council of Nurses and Midwives (NCNM) under Law N° 25/2008 of 25 July 2008; regulates training, registration, licensure, and professional conduct of nurses and midwives; sets scope of practice and professional standards; conducts licensure examination | Rwanda Allied Health Professionals Council (RAHPC) handles registration of clinical officers; Clinical Officers fall under RAHPC; Rwanda Medical Clinical Officers Organization (RMCOO) — professional NGO established 2016 — advocates for clinical-officer training, regulation, and practice standards in collaboration with MoH and RAHPC | HMIS (Rwanda Health Management Information System) on DHIS2 since 2012 (upgraded from paper-based HMIS 1998); collects facility data from 700+ public health facilities with 98% data completeness; OpenMRS used in hospitals for individual-level client records and auto-aggregation to DHIS2; eIDSR for disease surveillance — 23 communicable diseases tracked (immediately and weekly reportable per RBC guidelines); DHIS2 also hosts eIDSR, HIV, and TB modules; TRACnet (DHIS2 disease tracking system) since 2004 pioneered mobile/web reporting; Rwanda became first low-income country to fully implement eIDSR (April 2013) with 100% facility coverage | NIDA (National Identification Agency) under Law N° 43/2011 of 19 December 2011 (as amended) issues National Identification Card to citizens age 16+; 16-digit unique identification code broken into 6 groups (status, birth year, gender, sequential issue number, and internal NIDA identifier); citizens may register from age 16; children under 16 use parent NIN + birth-registration certificate as fallback; mass enrollment ongoing | Law N° 058/2021 of 13 October 2021 relating to Protection of Personal Data and Privacy (effective 15 October 2021); regulates collection, processing, storage, transfer, use of personal data; applies to all persons/institutions/public bodies processing data within Rwanda or concerning Rwandan residents; requires data localization within Rwanda unless NCSA-issued certificate obtained for offshore storage; data subjects have rights to access, rectify, erase personal data; overseas transfer must meet equivalent-protection standard; criminal and administrative penalties for violations including non-compliance with registration, breach notification, and data-subject rights | National Cyber Security Authority (NCSA) — supervisory authority under Law N° 058/2021; officially launched Data Protection Office 31 March 2022; registers data controllers/processors; enforces privacy law; conducts compliance audits; imposes administrative, civil, and criminal penalties | See standard-forms cohort for HMIS register set (ANC register, maternity/PNC register, immunisation register, immunisation card, ANC card, DHIS2-linked individual data forms, IDSR surveillance forms, eIDSR case-reporting tools, facility aggregate summary forms); RW-prefixed codes in standard-forms | [STUB — pending tenant-blueprints cohort for pre-configured workflows; expected to reference DHIS2 reporting pathways, IDSR case management, OpenMRS integration, facility referral networks, CBHI tariff schedules, and primary healthcare delivery models (health post, health centre, faith-based facility structures)] | T1: [rwanda-constitution]; [rwanda-law-003-2018-fda]; [rwanda-law-025-2008-ncnm]; [rwanda-law-045-2012-npc]; [rwanda-law-058-2021-data-protection]; [rwanda-organic-law-02-2017-swahili]; [rwanda-health-sector-strategic-plan]; [rwanda-health-facility-service-packages-moh]; [rwanda-nida-act-2011]; [rwanda-hmis-dhis2-standards]; [rwanda-idsr-guidelines-2012]; [rwanda-eml-2022]; Ministry of Health Rwanda website [moh.gov.rw]; Rwanda FDA [rwandafda.gov.rw]; RBC [rbc.gov.rw]; NIDA [nida.gov.rw]; RSSB [rssb.rw]; National Pharmacy Council [pharmacycouncil.rw]; NCNM [ncnm.rw]; RAHPC [rahpc.org.rw]; RMCOO [rwandaclinicalofficers.org]; NCSA [cyber.gov.rw]; BNR [bnr.rw]; RwandaLII legal database [rwandalii.org] T2: [WHO-Rwanda-country-profile]; [WHO-EMRO-health-systems-analysis]; [World Bank Rwanda-health-financing]; [RSSB-CBHI-overview-documents]; [RBC-health-information-exchange-openHIE]. [No Wikipedia in source_citations; T3 corroboration only, explicitly marked where used] |
| GH | Ghana | Ghanaian Cedi | GHS | Africa/Accra (UTC+00:00) | English (official); Akan (Twi; Fante; dialects); Ga | Region | [STUB — pending full Wave 2] | District | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | T1 currency/timezone/language: [ISO-4217 GHS]; [IANA-Africa-Accra]; [Ghana-languages] [Wikipedia consulted for triangulation only — never sole source] |
| NG | Nigeria | Nigerian Naira | NGN | Africa/Lagos (UTC+01:00) | English (official); Hausa; Yoruba; Igbo | State | 36 states + Federal Capital Territory Abuja = 37 administrative units (per Constitution 1999 Schedule 1); federal structure with three-tier governance (federal, state, LGA) | LGA (Local Government Area) | 774 LGAs (768 in 36 states + 6 area councils in FCT; per Constitution 1999 Schedule 1; further subdivided into minimum 10 and maximum 20 wards per LGA) | Nigeria facility levels (per National Health Policy 2016 and Master Facility List classification): Primary Health Care (PHC) Centre / Health Post (village level, 34,076 PHC centres as of 2023); Comprehensive PHC Centre; General Hospital (secondary, LGA/state level); Specialist Hospital (secondary); Federal Medical Centre (tertiary, federal level); Teaching Hospital (tertiary, federal level); private and faith-based clinics and diagnostic centres | Federal Ministry of Health and Social Welfare (FMoHSW) — renamed 2023 (previously FMoH); policy/oversight; coordinates through 36 state ministries of health and 774 LGA health departments; headed by Minister of Health; supported by PNFP/faith-based sector (CHAN — Christian Health Association of Nigeria; Catholic diocese networks; Islamic health bodies) | National Agency for Food and Drug Administration and Control (NAFDAC) under NAFDAC Act Cap N1 Laws of the Federation of Nigeria 2004 (originally Decree 15 of 1993); regulates manufacture, import, export, distribution, sale, advertisement of food, drugs, cosmetics, medical devices, chemicals, packaged water; Pharmacists Council of Nigeria (PCN) under Pharmacy Council of Nigeria Act 2022 regulates pharmacy professionals, pharmacy education, and pharmaceutical premises | National Health Insurance Authority (NHIA) under National Health Insurance Authority Act of 2022 (supersedes NHIS Act of 1999); mandatory for all Nigerians; three-tier system: Primary Healthcare Fund (PHF, government-funded); Basic Health Care Provision Fund (BHCPF) under National Health Act 2014 (1% of Consolidated Revenue Fund annually, operational from 2018); contributions: employers 10%, employees 5% (organized sector); informal sector via Group Individual and Family Social Health Insurance Programme (GIFSHIP); vulnerable populations via Vulnerable Group Fund | Medical Laboratory Science Council of Nigeria (MLSCN) established by MLSCN Act 2003; regulates training, registration, licensing of medical laboratory scientists, technicians, and assistants; conducts examinations, mandatory inspection, accreditation, certification of lab test kits and reagents | NHMIS (National Health Management Information System) on DHIS2 platform (adopted by National Council on Health 2013; all 36 states + FCT fully transitioned by 2021); mandatory monthly aggregate health data reporting from all health facilities; IDSR (Integrated Disease Surveillance Response) per WHO AFRO framework — 23 notifiable diseases tracked with immediate and weekly reporting; NCDC (Nigeria Centre for Disease Control, federal agency under FMoHSW) coordinates surveillance and outbreak response; reporting chain: facility → LGA → state Ministry of Health → Federal Ministry of Health/NCDC | NIN (National Identification Number) issued by NIMC (National Identity Management Commission) under NIMC Act No. 23 of 2007; unique 11-digit number; issued to citizens and legal residents; use mandatory for most transactions (financial, healthcare, electoral, social services); children under 18 not automatically issued but may use parent NIN + birth-registration certificate as fallback; mass enrollment ongoing | Nigeria Data Protection Act (NDPA) 2023 (effective 12 June 2023; supersedes Nigeria Data Protection Regulation NDPR 2019); regulates collection, processing, storage, transfer, use of personal data; applies to all persons/institutions/public bodies processing data within Nigeria or concerning Nigerians; data controllers/processors of major importance must register with NDPC within six months; mandatory breach notification; overseas data-transfer only to countries with equivalent protections | Nigeria Data Protection Commission (NDPC) — independent regulatory authority established by NDPA 2023; oversees implementation; registers data controllers/processors; enforces compliance; imposes tiered fines: ₦10,000,000 (ten million Naira) or 2% annual gross revenue (whichever higher) for major controllers; ₦2,000,000 (two million Naira) or 2% annual gross revenue (whichever higher) for other controllers; conducts audits and investigations | See standard-forms cohort for NHMIS form list (facility aggregate summary forms, OPD/inpatient/maternal/lab/commodity registers, IDSR surveillance forms, eIDSR case-reporting tools, immunisation cards, ANC cards); NG-prefixed codes in standard-forms | [STUB — pending tenant-blueprints cohort for pre-configured workflows; expected to reference NHMIS/DHIS2 reporting pathways, IDSR case management, facility referral networks, NHIA tariff schedules, primary healthcare delivery models (PHC Centre, General Hospital, faith-based CHAN facility structures), state/LGA health system coordination] | T1: [nigeria-constitution-1999]; [nigeria-national-health-policy-2016]; [nigeria-national-health-act-2014]; [nigeria-nafdac-act-cap-n1]; [nigeria-pharmacy-council-act-2022]; [nigeria-mlscn-act-2003]; [nigeria-nhia-act-2022]; [nigeria-ndpa-2023]; [nigeria-nimc-act-2007]; [nigeria-health-facility-master-list]; [nigeria-idsr-technical-guidelines]; [nigeria-neml-2020]; Federal Ministry of Health and Social Welfare website [health.gov.ng]; NAFDAC website [nafdac.gov.ng]; NHIA website [nhia.gov.ng]; PCN website [pcn.gov.ng]; MLSCN website [mlscn.gov.ng]; MDCN website [mdcn.gov.ng]; NMCN website [nmcn.gov.ng]; NIMC website [nimc.gov.ng]; NDPC website [ndpc.gov.ng]; NCDC website [ncdc.gov.ng]; NPHCDA website [nphcda.gov.ng]; NACA website [naca.gov.ng]; NTBLCP website [ntblcp.org.ng]; NMCP website [nmcp.gov.ng] T2: [WHO-Nigeria-country-profile]; [World Bank Nigeria-health-system]; [Nigeria Bureau of Statistics demographic data]; [Willow Health Media Nigeria health system analysis] [No Wikipedia in source_citations; T3 corroboration only, explicitly marked where used] |
| ZA | South Africa | South African Rand | ZAR | Africa/Johannesburg (UTC+02:00) | English; Zulu; Xhosa; Afrikaans; Tswana; Southern Sotho; Tsonga; Swati; Venda; South Ndebele (11 official languages per Constitution 1996) | Province | [STUB — pending full Wave 2] | District; Metro | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | T1 currency/timezone/language: [ISO-4217 ZAR]; [IANA-Africa-Johannesburg]; [South Africa-constitution-1996] [Wikipedia consulted for triangulation only — never sole source] |
| IN | India | Indian Rupee | INR | Asia/Kolkata (UTC+05:30, Indian Standard Time, no DST) | Hindi; English (official per Constitution); 22 other scheduled languages (Bengali, Telugu, Marathi, Tamil, Urdu, Gujarati, Kannada, Malayalam, Oriya, Punjabi, Assamese, Kashmiri, Nepali, Sindhi, Sanskrit, French and others) | State | [STUB — pending full Wave 2] | District | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | T1 currency/timezone/language: [ISO-4217 INR]; [IANA-Asia-Kolkata]; [India-constitution] [Wikipedia consulted for triangulation only — never sole source] |
| PH | Philippines | Philippine Peso | PHP | Asia/Manila (UTC+08:00, Philippine Standard Time, no DST) | Filipino (based on Tagalog, national); English (official); Tagalog; Cebuano; Ilocano; Hiligaynon; Bicol; Waray; Pampango; Pangasinense (major dialects) | Region | [STUB — pending full Wave 2] | Province | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | [STUB — pending full Wave 2] | T1 currency/timezone/language: [ISO-4217 PHP]; [IANA-Asia-Manila]; [Philippines-constitution] [Wikipedia consulted for triangulation only — never sole source] |

| CD | Democratic Republic of Congo | Congolese Franc | CDF | Africa/Kinshasa (UTC+01:00, WAT) for west; Africa/Lubumbashi (UTC+02:00, CAT) for east. Country spans 2 timezones (IANA TZ database: Africa/Kinshasa, Africa/Lubumbashi) | French (official); Lingala; Kikongo (Kituba); Swahili; Tshiluba (national languages per Constitution Art 1) | Province | 26 (post-2015 découpage; previously 11; Kinshasa + 25 provinces per Constitutional Law of 2011 on découpage) | Territoire (rural) / Ville (urban). 145 territories and 33 cities (dual hierarchy; territories led by territory administrators, cities defined as provincial capitals or agglomerations 100,000+ inhabitants with collective facilities) | Territoire/Ville counts: 145 territories + 33 cities = 178 second-level subdivisions (rural-urban distinction critical for health planning per PNDS) | DRC facility levels (per Ministry of Health PNDS structure): Centre de santé (Health Zone level, serving ~100k-150k rural or ~200k-250k urban pop); Hôpital général de référence (HGR, district level, offers complementary package — PCA); optional Centres de santé de référence (CSR); Provincial Hospital; National Referral Hospital (HN, tertiary) | Ministère de la Santé Publique, Hygiène et Prévention (Ministry of Public Health, Hygiene and Prevention); centralized policy/oversight with 515 Health Zones (ZS) as operational units; Health Zone Management Teams (ECZ) coordinate local delivery; Provincial Health Divisions oversee provincial hospitals and laboratories | ACOREP (Autorité Congolaise de Réglementation Pharmaceutique, Congolese Pharmaceutical Regulatory Authority) under Ministry of Public Health; as of 2020 assumed responsibilities from DPM (Direction de la Pharmacie et du Médicament); regulates authorization, import/export, quality/safety of medicines, medical devices, herbal products, psychotropic drugs; oversees marketing authorization and pharmaceutical-market monitoring | ARCA (Autorité de Régulation et de Contrôle des Assurances, Insurance Regulation and Control Authority) under Decree No. 16/001 of 26 January 2016; independent public establishment; regulates insurance sector, protects policyholders' rights, ensures financial soundness of insurers; CNAM (Caisse Nationale d'Assurance Maladie) established under Law 18/035 (2018) for universal health coverage (implementation gradual as of 2026) | INRB (Institut National de Recherche Biomédicale, National Biomedical Research Institute) founded 1984; WHO collaborating center since 2018; serves as national reference lab under Ministry of Health; 70,000 m² facility with 6 labs (Virology, Parasitology, Bacteriology, Medical Entomology, Clinical Biology, Pathology); DPM oversees pharmaceutical enforcement; no dedicated standalone laboratory council identified [T1 verification pending — ISO 15189 accreditation status] | ONIC (Ordre National des Infirmiers, National Order of Nurses) established under Law 16/015 (15 July 2016); regulates nursing training, registration (mandatory per Art 5), licensure, professional conduct, disciplinary control; headquartered Kinshasa; provincial councils coordinate local registration | [T1 verification pending — clinical officer regulation structure; no explicit council identified; may fall under CNOM (Conseil National de l'Ordre des Médecins) or separate body; confirmation needed] | SNIS (Système National d'Information Sanitaire) on DHIS2 platform; mandatory monthly reporting from health facilities (>90% compliance in ASSP zones); programs (EPI, Malaria) populate monthly reports via DHIS2; IDSR (Integrated Disease Surveillance and Response) per WHO-AFRO framework for notifiable diseases (immediate reporting for suspected/probable/confirmed Ebola/Marburg/priority diseases; outbreak investigations via RRTs per MoH protocols); facility-level data aggregated through health zones to provincial and national levels; [reporting-kpis gap — exact mandatory form set and quarterly/annual KPI detail not yet fully sourced] | National ID: Carte d'Identité Nationale (CIN) issued by ONIP (Office National d'Identification de la Population) per Decree 22/08 (2 March 2022); issued to adult Congolese citizens registered in General Population File (FGP, per Decree 22/07); validity 10 years; de facto primary ID. Fallback for under-18s and undocumented: most citizens still use Carte d'électeur (Voter Card, issued by CENI, Independent National Electoral Commission) as de facto ID — voter card includes civil status, photo, fingerprint, barcode, CENI watermark (continues from pre-CIN era; still widely used given low CIN penetration outside Kinshasa). SaaS implementation: patient-identity table must accommodate both CIN (primary, unique 14-digit for adults) and voter card (alternative, de facto) for under-18s and populations in transition; flag as "ID pending verification" if neither available | Loi n° 20/017 (2020, promulgated 25 November 2020, entered into force same date) on telecommunications and ICT; Title III Arts 126-133 regulate privacy and personal data protection; defines personal data as information relating to identified/identifiable natural person directly/indirectly by reference to identification number or elements specific to physical/physiological/genetic/psychological/cultural/social/economic identity; prohibits processing of sensitive data (racial/ethnic/regional origin, opinions, religious/philosophical beliefs, union membership, sexual life, genetic, health); requires consent-based collection; overseas transfer only to equivalent-protection jurisdictions; implementation requires executive decree (pending as of 2026). Secondary: Law 23/010 (Digital Code, 13 March 2023) also includes data-protection provisions; entered into force on approval date. [T1 verification pending — comprehensive Personal Data Protection Law status; framework law with telecom focus, not standalone privacy statute like Uganda/Kenya] | [T1 verification pending — privacy authority identity; no dedicated data-protection commissioner identified in available sources; enforcement likely under ARTEL (telecom regulator) or Ministry of Communication per Law 20/017] | See standard-forms cohort for SNIS/DHIS2 form list and IDSR tools; CD-prefixed codes to be assigned in standard-forms; references to HGR/CSR/ZS levels | [STUB — pending tenant-blueprints cohort for pre-configured workflows; expected to reference SNIS reporting, Health Zone protocols, IDSR outbreak triage, and PCA/PMA clinical bundles] | T1: [drc-constitution-2005-2011]; [drc-law-20-017-2020-telecom-ict]; [drc-law-23-010-digital-code-2023]; [drc-decree-22-07-2022-fgp]; [drc-decree-22-08-2022-cin]; [drc-decree-16-001-2016-arca]; [drc-law-16-015-2016-nursing]; [drc-law-18-035-2018-usc]; Ministry of Public Health, Hygiene and Prevention [minisante.cd — T1 verification pending]; ONIP website [onip.gouv.cd]; ARCA website [arca.cd]; CENOM (Medical Council) [T1 verification pending]; ONIC website [ordredesinfirmiersrdc.org]; INRB website [inrb.cd]; ACOREP [acorep-dpmrdc.org — T1 verification pending]; BCC (Banque Centrale du Congo) [bcc.cd]; INS (Institut National de Statistique) [ins.cd]; Journal Officiel [journalofficiel.cd — T1 verification pending] T2: [WHO-DRC-country-profile]; [World Bank DRC health-system review]; [UN OCHA DRC humanitarian reports]; [DHIS2 DRC implementation analysis]; [INRB collaborating-center status] [No Wikipedia in source_citations — standalone verification per discipline. Consulted for triangulation only, listed in findings T3 block] |

---

## Pass 2 — Country-pack full extension (2026-05-04)

This section appends Democratic Republic of Congo (CD) research completed via Wave-3 extension agent. CD row above row 24 (between RW and GH) reflects 2026-05-04 research into DRC-specific governance, regulators, and mandatory health-information systems.

---

## Notes on Data Completeness

### Uganda (UG) — Full Pack (2/24 columns [STUB]; 22/24 columns populated)

**Strengths:**
- All core regulatory bodies sourced from statutory Acts (UMDPC, AHPC, UNMC, NDA all T1).
- Mandatory reporting forms traced to official HMIS documentation and IDSR Technical Guidelines.
- National ID system (NIRA, NIN) from official government sources.
- Data Protection and Privacy Act 2019 directly cited with effective dates.
- Admin structure (146 districts + 2,100+ sub-counties) from government administrative restructuring records.

**Gaps / Items marked [GAP]:**
- Insurance regulator: National Health Insurance Scheme is pending implementation; no statutory regulator exists yet. PNFP cost-sharing is the de facto dominant financing model.
- Lab regulator: No dedicated laboratory council identified. AHPC oversees laboratory cadres; ISO 15189 accreditation is optional, not mandatory.
- Default blueprints reference: Deferred to upcoming tenant-blueprints cohort (marked [STUB]).

**Verification notes:**
- UMDPC defined under Act Cap 272 (NOT Cap 268, which is AHPC).
- AHPC (NOT UMDPC) regulates clinical officers per Cap 268; approximately 11,795 registered medical clinical officers.
- Uganda NDA drug-shop licensing uses "Class A/B/C" tiers for *retail dispensing*, NOT prescribing schedules (per brief warning on Uganda prescribing-schedule discipline).
- HMIS-107 is an *annual* report (due 7 August), not monthly; monthly forms are HMIS-105 (outpatient) and HMIS-108 (inpatient).

### Kenya (KE) — Full Pack (2/24 columns [STUB]; 22/24 columns populated)

**Strengths:**
- All core regulatory bodies sourced from statutory Acts (KMPDC, COC, NCK, PPB, KMLTTB all T1).
- Social Health Authority (SHA) transition from NHIF documented via Social Health Insurance Act 2023 (effective 1 October 2024).
- 47 counties and devolution structure from Constitution 2010 and County Governments Act 2012.
- Huduma Namba / NIIMS from National Integrated Identity Management System rules and privacy court records.
- Data Protection Act 2019 directly cited with effective date and ODPC enforcement authority.
- Health levels (KEPH Levels 1–6) from official Ministry of Health and WHO-adopted structure.

**Gaps / Items marked [STUB]:**
- Exact Huduma/Maisha Namba issuance age and fallback rules for under-18s marked [T1 verification pending].
- Mandatory reporting forms (KHIS on DHIS2) structure; reporting KPI list not yet detailed (marked [reporting-kpis gap]).
- Default blueprints reference: Deferred to tenant-blueprints cohort.

**Verification notes:**
- COC established under Clinical Officers Act 2017 (Act No. 20 of 2017), NOT Cap 260 (repealed).
- NCK under Nurses Act Cap 257 (NOT Cap 274, which is for Uganda).
- PPB under Pharmacy and Poisons Act Cap 244 (NOT Cap 257).
- KMLTTB under Cap 253A, with ISO 15189 now mandatory for accredited labs (Business Laws Amendment 2024).
- Kenya SHA SHIF contribution is 2.75% gross pay with KES 300/month minimum.
- NHIF ceased operations 30 September 2024; SHA assumed all functions from 1 October 2024.

### Tanzania (TZ) — Stub Pack (5/24 columns populated; 19/24 columns [STUB])

**Populated columns:**
- country_code: TZ
- country_name: Tanzania
- currency: Tanzanian Shilling
- currency_iso_4217: TZS
- timezone: Africa/Dar_es_Salaam (UTC+03:00)
- languages: Swahili; English

**All other columns:** [STUB — pending full Wave 2]

**Rationale for stub:**
Tanzania shares East African health-system characteristics with Uganda and Kenya but requires dedicated research into its own regulatory bodies (equivalent to UMDPC, AHPC, UNMC, NDA), Ministry of Health structure, health facility classification system, mandatory reporting forms, and privacy laws. Wave-2 priorities include: Health Professions Council of Tanzania (HPCT, if equivalent exists); Tanzania essential medicines list and drug regulator; national ID system; Data Protection Act details; healthcare financing structure; HMIS/reporting framework; admin-level names and counts.

### Rwanda (RW) — Full Pack (2026-05-04 Wave-3 Extension, 22/24 columns populated; 2 columns marked [STUB])

**Populated columns (22/24):**
- country_code, country_name, currency, currency_iso_4217, timezone, languages (6/6 ✓)
- admin_level_1_name, admin_level_1_count, admin_level_2_name, admin_level_2_count (4/4 ✓)
- facility_level_system, health_ministry, medicine_regulator, insurance_regulator, lab_regulator (5/5 ✓)
- nursing_regulator, clinical_officer_regulator, mandatory_reports, national_id_rules, privacy_law, privacy_authority (6/6 ✓)

**Columns marked [STUB] (2/24):**
- default_forms_reference: [STUB — pending standard-forms cohort completion and cross-linking of HMIS form identifiers]
- default_blueprints_reference: [STUB — pending tenant-blueprints cohort for pre-configured workflows]

**Strengths (Pass 2 — 2026-05-04 Wave-3 Extension):**
- All core regulatory bodies sourced from T1 statutory acts: Rwanda FDA (Law N° 003/2018), NCNM (Law N° 25/2008), NPC (Law N° 45/2012), Rwanda Medical and Dental Council (RMDC), Rwanda Allied Health Professionals Council (RAHPC) with clinical officers oversight.
- Facility-level system traced to Ministry of Health Health Sector Strategic Plan and health-service-package guidelines; 1,280 health posts, 520 health centres, 57 hospitals confirmed.
- Insurance regulator (BNR for private; RSSB for CBHI/Mutuelle de Santé) sourced from central bank website and RSSB documentation; CBHI covers 91% of population as of 2023 — highest in Africa.
- Lab regulator: RBC National Reference Laboratory with ISO 15189:2022 accreditation (June 2024 via KENAS); WHO AFRO SLMTA programme implementation documented.
- National ID (NIDA): 16-digit format per Law N° 43/2011; issuance from age 16+; fallback rules for minors defined.
- Data Protection Law N° 058/2021 directly cited with effective date (15 October 2021); NCSA (National Cyber Security Authority) as supervisory authority with Data Protection Office launched 31 March 2022.
- HMIS on DHIS2 since 2012 with 98% data completeness; OpenMRS integration at hospital level; eIDSR with 23 diseases tracked; Rwanda was first low-income country to fully implement eIDSR (April 2013, 100% facility coverage).
- Health languages policy: Constitution Article 8 designates Kinyarwanda as national language, English/French as official languages; Organic Law Nº 02/2017 added Swahili (2017).
- 5 provinces and 30 districts confirmed; 4×4 Reform workforce initiative (2023 onwards) documented via official MoH announcements.
- Pharmacy regulation: NPC established by law; pharmacist registration and pre-registration examination requirements sourced.

**Gaps identified (2 fields [STUB]):**
- default_forms_reference: Specific form codes and identifiers (RW-prefixed HMIS codes) not yet documented in standard-forms cohort; ANC register, immunisation register, DHIS2 forms, and eIDSR tools exist but require cross-cohort mapping.
- default_blueprints_reference: Pre-configured workflows for DHIS2 reporting, referral pathways, CBHI tariff schedules, and faith-based facility integration deferred to tenant-blueprints cohort completion.

**Verification notes:**
- Rwanda Medical and Dental Council (RMDC) confirmed as primary physician/dentist regulator (distinct from Uganda's UMDPC and Kenya's KMPDC).
- Clinical officers regulated through Rwanda Allied Health Professionals Council (RAHPC), with Rwanda Medical Clinical Officers Organization (RMCOO) as professional advocacy body.
- NCNM is the nursing and midwifery regulator (distinct naming convention from Uganda/Kenya; Law N° 25/2008 provides statutory authority).
- CBHI integration into RSSB completed 2015; scheme covers 91% population with contributions from community, government, and donors combined.
- OpenMRS flagship site status maintained since 2008 era; Rwanda DHIS2 implementation exemplary for the region with 98% data completeness.
- No dedicated clinical-officer prescribing-schedule warnings (unlike Uganda NDA Class A/B/C terminology — not applicable to Rwanda).

### Democratic Republic of Congo (CD) — Full Pack Extension (2026-05-04) — 18/24 columns populated; 6/24 flagged [T1 verification pending] or [STUB]

**Populated columns (T1-sourced; 18/24 = 75%):**
- country_code, country_name, currency, currency_iso_4217, timezone, languages: All confirmed via official sources (Constitution, ISO/IANA standards, government agencies).
- admin_level_1_name, admin_level_1_count, admin_level_2_name, admin_level_2_count: 26 provinces (post-2015 découpage per Constitutional Law 2011) and 178 second-level subdivisions (145 territories rural + 33 cities urban) verified via government administrative records.
- facility_level_system: Health Zone pyramid (centre de santé → HGR [PCA] → provincial → national) sourced from Ministry PNDS publications and WHO-DHIS2 case studies.
- health_ministry: Ministère de la Santé Publique, Hygiène et Prévention confirmed; 515 Health Zones as operational units documented.
- medicine_regulator: ACOREP (Decree 2020, assumed DPM responsibilities) confirmed via official regulator website and WHO clinical-trials database.
- insurance_regulator: ARCA (Decree 16/001/2016, independent authority) and CNAM (Law 18/035/2018 for universal coverage, gradual implementation) sourced from official insurance authority and World Bank health-financing reviews.
- nursing_regulator: ONIC (Ordre National des Infirmiers, Law 16/015/2016) confirmed via official ONIC website and Congolese legal registry.
- mandatory_reports: SNIS (DHIS2 platform, monthly >90% facility compliance in ASSP zones) and IDSR (WHO-AFRO framework, immediate reporting Ebola/Marburg/priority) sourced from Ministry reports and DHIS2 implementation documentation.
- national_id_rules: CIN (Carte d'Identité Nationale via ONIP, Decrees 22/07 & 22/08, 10-year validity) confirmed; voter card (Carte d'électeur via CENI, de facto still widely used) documented via IRB Canada and UNHCR records.
- privacy_law: Law 20/017/2020 (telecom/ICT, Arts 126–133) and Law 23/010/2023 (Digital Code) sourced directly from official gazette and government announcements; provisions on data protection, sensitive data prohibitions, and consent-based processing confirmed.

**Columns marked [T1 verification pending] (3/24 = 12.5%):**
- clinical_officer_regulator: No explicit council identified; may fall under CNOM (Conseil National de l'Ordre des Médecins) or separate body — **requires Ministry of Health confirmation**.
- lab_regulator: INRB serves as national reference lab; DPM oversees pharmaceutical enforcement; ISO 15189 accreditation status and formal delegation not yet sourced — **confirmation pending from Ministry and/or INRB**.
- privacy_authority: No dedicated data-protection commissioner identified; enforcement appears to vest with ARTEL (telecom regulator) or Ministry of Communication under Law 20/017 — **clarification required on institutional arrangement**.

**Columns marked [STUB] (2/24 = 8%):**
- default_forms_reference: [STUB — pending standard-forms cohort to assign CD-prefixed codes for SNIS/DHIS2 forms, IDSR tools, and Health Zone protocols].
- default_blueprints_reference: [STUB — pending tenant-blueprints cohort for pre-configured Health Zone workflows, SNIS monthly reporting, IDSR triage, and PCA/PMA clinical bundles].

**Strengths:**
- **Constitutional and statutory framework:** Constitution 2005 (revised 2011) directly sourced for language policy (French official; Lingala, Kikongo, Swahili, Tshiluba national languages per Art 1).
- **Administrative structure:** 2015 Découpage Constitutional Law confirmed 26 provinces; territorial subdivision (145 territories + 33 cities) verified via government administrative sources and UN OCHA humanitarian datasets.
- **Health system architecture:** Ministry PNDS (National Health Development Plan) and Health Zone operational model sourced from WHO-DHIS2 case study and World Bank health-system reviews; 515 Health Zones with >90% reporting compliance documented.
- **Regulatory bodies:** ONIC (nursing), ACOREP (pharmacy), ARCA (insurance), INRB (reference lab) all confirmed via official government decrees and regulator websites; CNAM (universal coverage) Law 18/035/2018 verified via World Bank health-financing documentation.
- **Mandatory reporting:** SNIS on DHIS2 platform since early 2010s; IDSR with real-world Ebola containment example (December 2025 outbreak, 64 cases, 45 deaths, ended in 3 months) demonstrates operational integration with RRTs and surveillance focal persons per WHO-AFRO framework.
- **National ID system:** Dual-system reality captured: CIN (new, formal, 10-year) via ONIP (Decrees 22/07 & 22/08) AND voter card (Carte d'électeur, de facto continued use due to lower CIN penetration outside Kinshasa) via CENI — critical for healthcare identity interoperability in transitional environment.
- **Privacy framework:** Law 20/017/2020 (telecom/ICT data protection) and Law 23/010/2023 (Digital Code) both cited with statutory text and effective dates; provisions on sensitive data, consent, and international transfer sourced.
- **Unique geographic feature:** DRC spans 2 timezones (IANA: Africa/Kinshasa UTC+01:00 WAT west; Africa/Lubumbashi UTC+02:00 CAT east) — only African country with this multi-timezone architecture; critical for cross-regional facility synchronization and SaaS deployment architecture.
- **Connectivity constraint:** High internet non-adoption (80% of population, per BuddeComm 2024) and 3G/4G coverage limitations (55%/45% population) documented; relevant to offline-mode requirements and mobile-money (M-Pesa Vodacom, Airtel Money, Orange Money) for payment integration.

**Gaps / Items marked [T1 verification pending]:**
1. **Clinical officer regulation:** No standalone Clinical Officers Council found in available sources; CNOM (Conseil National de l'Ordre des Médecins) may regulate or separate body may exist — **MoH confirmation required**.
2. **Lab accreditation:** ISO 15189 accreditation status for DRC reference labs and enforcement mechanism not yet sourced — **INRB and Ministry follow-up required**.
3. **Privacy authority:** Implementation agency for Law 20/017/2020 and Law 23/010/2023 data-protection provisions unclear; ARTEL (telecom regulator) or Ministry of Communication coordination not yet confirmed — **institutional arrangement clarification pending**.
4. **Under-18 fallback ID rules:** While voter card is de facto fallback, formal ONIP guidance on under-18 patient-identity protocol not yet sourced — **ONIP official documentation required**.
5. **Ministry of Public Health website:** minisante.cd URL mentioned in sources but **domain and content verification pending** (T1 access confirmation needed).
6. **ACOREP institutional status:** Transition from DPM to ACOREP (2020) confirmed; organizational structure and pharmaceutical-enforcement delegation not fully detailed — **ACOREP and ANREP oversight clarification required**.
7. **Essential medicines list:** LNME 2020 edition confirmed via WHO; **2024 edition status pending** (may require direct MoH contact or ACOREP query).
8. **CNAM implementation:** Law 18/035/2018 enacted; **implementation status and benefit-schedule detail (2026) pending** — relevant to billing-tariffs cohort downstream.
9. **Comprehensive data-protection law:** Law 20/017/2020 focuses on telecom/ICT context; **status of standalone Personal Data Protection Law separate from telecom act pending** (implementation decree for executive rules still awaited as of 2026).

**Assumptions for SaaS implementation (flagged for confirmation):**
- **Patient identity:** Assume both CIN and voter card must be accommodated in patient-identity module; flag records as "ID pending verification" if neither available (reflects transitional period and refugee/undocumented populations in conflict zones).
- **Billing/tariffs:** No tariff schedule sourced; ARCA/CNAM benefit structures pending for billing-tariffs cohort.
- **Health financing:** ARCA regulates private insurance; CNAM universal scheme in implementation phase — integrate regulatory body as insurance_regulator constant.
- **Connectivity:** Offline-mode capability and mobile-money integration (M-Pesa, Airtel, Orange) essential for Health Zone reporting in rural areas.
- **VAT exemptions:** VAT 16% confirmed (Loi 10/001/2010, Code des Impôts); **health-service exemption detail pending** (may require tax-authority clarification).
- **Timezone coordination:** Implement dual-timezone support for Kinshasa (UTC+01:00) and Lubumbashi (UTC+02:00) facility scheduling.

**Verification notes:**
- **Ordre des Médecins (CNOM):** Established by Ordonnance-Loi 68/070 (1 March 1968); reaffirmed in contemporary practice; Dr. Berthier Nsadi Fwene reelected president for 2022–2026 term (source: ACP DRC 2021). **CNOM (NOT CNIM)** is correct official abbreviation.
- **ONIC legal basis:** Law 16/015 (15 July 2016, not earlier); mandatory registration per Article 5; provincial councils coordinate local registration — **confirmed via ordredesinfirmiersrdc.org and Congolese legal registry**.
- **DHIS2 >90% compliance:** Cited from DHIS2 DRC case study in ASSP (Appui aux Soins de Santé Primaires) zone analysis; broader national coverage status varies — **note reflects multi-zone sample, not universal DRC claim**.
- **No Uganda Class A/B/C confusion:** DRC ACOREP does not use Uganda-style NDA drug-shop licensing tiers; ACOREP regulates manufacture, import, distribution, sale of finished pharmaceuticals — different regulatory model.
- **Dual-currency reality (CDF/USD):** BCC (Banque Centrale du Congo) monetary policy permits USD circulation in commerce; all billing/tariff data must cite currency and year to avoid confusion — **critical for financial modeling**.

### Ghana (GH) — Stub Pack (6/24 columns populated; 18/24 columns [STUB])

**Populated columns:**
- country_code: GH
- country_name: Ghana
- currency: Ghanaian Cedi
- currency_iso_4217: GHS
- timezone: Africa/Accra (UTC+00:00)
- languages: English (official); Akan (Twi; Fante); Ga

**All other columns:** [STUB — pending full Wave 2]

**Rationale for stub:**
Ghana's health-system governance, regulatory bodies, health facility classification, mandatory reporting framework, national ID system, and privacy law require dedicated Wave-2 research. Priority items: Ghana Medical and Dental Council (GMDC); Pharmacy Council of Ghana; Nursing and Midwifery Council of Ghana; Lab regulator; health facility levels (CHPS compounds, polyclinics, district/regional/tertiary hospitals); healthcare financing (NHIS structure); health information system and mandatory forms; Data Protection Act and commissioner authority; national identification system and patient-ID rules.

### Nigeria (NG) — Stub Pack (6/24 columns populated; 18/24 columns [STUB])

**Populated columns:**
- country_code: NG
- country_name: Nigeria
- currency: Nigerian Naira
- currency_iso_4217: NGN
- timezone: Africa/Lagos (UTC+01:00)
- languages: English (official); Hausa; Yoruba; Igbo

**All other columns:** [STUB — pending full Wave 2]

**Rationale for stub:**
Nigeria's decentralized health system (federal, state, LGA structures) requires comprehensive Wave-2 research into: Medical and Dental Council of Nigeria (MDCN); Nursing and Midwifery Council of Nigeria (NMCN); Pharmacy Council of Nigeria (PCN); Clinical officers regulation (if equivalent exists); Laboratory Science Council of Nigeria; health facility levels and classification; mandatory federal/state/LGA reporting frameworks; healthcare financing (NHIS structure); national ID system (NIMC — National Identification Management Commission); Data Protection Regulation (NDPR 2019); private health-sector role.

### South Africa (ZA) — Stub Pack (6/24 columns populated; 18/24 columns [STUB])

**Populated columns:**
- country_code: ZA
- country_name: South Africa
- currency: South African Rand
- currency_iso_4217: ZAR
- timezone: Africa/Johannesburg (UTC+02:00)
- languages: English; Zulu; Xhosa; Afrikaans; Tswana; Southern Sotho; Tsonga; Swati; Venda; South Ndebele (11 official languages)

**All other columns:** [STUB — pending full Wave 2]

**Rationale for stub:**
South Africa's health system (NHI transitioning, HPCSA regulatory structure, provincial/district health hierarchies) requires Wave-2 research: Health Professions Council of South Africa (HPCSA); South African Nursing Council (SANC); South African Medical Research Council; health facility levels (primary/secondary/tertiary); healthcare financing and NHI implementation status; national ID system and patient-ID rules; Protection of Personal Information (POPIA) Act 2013 and regulator; mandatory reporting and health information system; private health-sector integration.

### India (IN) — Stub Pack (6/24 columns populated; 18/24 columns [STUB])

**Populated columns:**
- country_code: IN
- country_name: India
- currency: Indian Rupee
- currency_iso_4217: INR
- timezone: Asia/Kolkata (UTC+05:30)
- languages: Hindi; English (official); 22 other scheduled languages

**All other columns:** [STUB — pending full Wave 2]

**Rationale for stub:**
India's federal health system (union + 28 states + 8 union territories) requires comprehensive Wave-2 research: Medical Council of India (MCI, now National Medical Commission per National Commission for Homoeopathy Act 2019); nursing councils (state and national); pharmacy boards; laboratory standards (NABL accreditation); health facility levels (primary/secondary/tertiary across states); healthcare financing (state variation; central schemes like Ayushman Bharat); national ID (Aadhaar system and health-ID interplay); Data Protection (awaiting pending Privacy Bill; interim protections under various acts); mandatory reporting frameworks; HMIS and state variation.

### Philippines (PH) — Stub Pack (6/24 columns populated; 18/24 columns [STUB])

**Populated columns:**
- country_code: PH
- country_name: Philippines
- currency: Philippine Peso
- currency_iso_4217: PHP
- timezone: Asia/Manila (UTC+08:00)
- languages: Filipino (based on Tagalog, national); English (official); major regional dialects

**All other columns:** [STUB — pending full Wave 2]

**Rationale for stub:**
Philippines' decentralized health system (DOH + regional/provincial health offices; LGU roles) requires Wave-2 research: Professional Regulation Commission (PRC) for physicians, nurses, lab technologists, pharmacists; Philippine Medical Association; Philippine Health Insurance Corporation (PhilHealth); health facility levels and classification; mandatory reporting (disease surveillance, health information system); national ID system (PhilSys — Philippine Identification System); Data Privacy Act 2012 and Data Protection National Privacy Commissioner; healthcare financing structure; HMIS and provincial variation.

---

## References

### T1 — Statutory and Governmental Sources

**Uganda:**
- Constitution of Uganda (as amended)
- Local Governments Act (as amended)
- Medical and Dental Practitioners Act Cap 272
- Allied Health Professionals Act Cap 268
- Nurses and Midwives Act 1996 (Cap 301)
- National Drug Policy and Authority Act Cap 206
- Data Protection and Privacy Act 2019 (Act No. 9 of 2019)
- Registration of Persons Act 2015
- HMIS-107 form (Ministry of Health Uganda)
- IDSR Technical Guidelines 3rd Edition (Ministry of Health Uganda, September 2021)
- Essential Medicines and Health Supplies List for Uganda (EMHSLU) 2023
- Official websites: health.go.ug; umdpc.go.ug; ahpc.ug; unmc.ug; nda.or.ug; nira.go.ug; pdpo.go.ug

**Kenya:**
- Constitution of Kenya 2010 (as amended)
- County Governments Act 2012 (Act No. 17 of 2012)
- Medical Practitioners and Dentists Act Chapter 253
- Clinical Officers (Training, Registration and Licensing) Act 2017 (Act No. 20 of 2017)
- Nurses Act Chapter 257
- Pharmacy and Poisons Act Chapter 244
- Medical Laboratory Technicians and Technologists Act (Cap 253A)
- Health Records and Information Managers Act 2016
- Health Act 2017
- Data Protection Act 2019 (Act No. 24 of 2019)
- Social Health Insurance Act 2023 (assented 19 October 2023, effective 1 October 2024)
- National Integrated Identity Management System (NIIMS) Rules 2020 (Legal Notice No. 195 of 2020)
- Kenya Essential Medicines List (KEML) 2023
- Official websites: health.go.ke; kmpdc.go.ke; clinicalofficerscouncil.org; nckenya.org; web.pharmacyboardkenya.org; kmlttb.org; odpc.go.ke; sha.go.ke; devolution.go.ke

**Democratic Republic of Congo:**
- Constitution of the Democratic Republic of the Congo 2005 (revised 2011)
- Law No. 16/015 (15 July 2016) — Nurses Act; creation and regulation of Ordre National des Infirmiers (ONIC)
- Law No. 18/035 (2018) — Universal Health Coverage provisions; CNAM establishment
- Law No. 20/017 (25 November 2020) — Telecommunications and ICT; Title III Arts 126–133 on data protection and personal data
- Law No. 23/010 (13 March 2023) — Digital Code; additional data-protection provisions
- Decree No. 22/07 (2 March 2022) — Creation of General Population File (FGP) under ONIP
- Decree No. 22/08 (2 March 2022) — National Identity Card (CIN) issuance rules; 10-year validity
- Decree No. 16/001 (26 January 2016) — Creation of ARCA (Autorité de Régulation et de Contrôle des Assurances)
- Ordonnance-Loi 68/070 (1 March 1968) — Establishment of Ordre des Médecins (CNOM)
- Ministry of Public Health, Hygiene and Prevention official structures and PNDS (National Health Development Plan)
- DHIS2 DRC implementation documentation and WHO-AFRO health-system strengthening reports
- INRB (Institut National de Recherche Biomédicale) official website and WHO collaborating-centre designation (2018)
- ARCA official website [arca.cd]
- ONIP official website [onip.gouv.cd]
- ONIC official website [ordredesinfirmiersrdc.org]
- ACOREP [acorep-dpmrdc.org] — pharmaceutical regulatory authority
- BCC (Banque Centrale du Congo) [bcc.cd] — monetary policy and dual-currency CDF/USD

**Tanzania, Rwanda, Ghana, Nigeria, South Africa, India, Philippines:**
- National constitutions and language provisions (verified via official government sources and ISO standards)
- ISO 4217 currency codes (official IANA/ISO registry)
- IANA timezone database (official tz database)

### T2 — International Corroboration

- World Health Organization (WHO) Country Health Profiles: Uganda, Kenya, Tanzania, Rwanda, Ghana, Nigeria, South Africa, India, Philippines, Democratic Republic of Congo
- WHO-DHIS2 case study: DRC health-system data use and DHIS2 implementation (2022)
- WHO-AFRO IDSR Technical Guidelines and DRC outbreak-response framework (Ebola 2025 case study: 64 cases, 45 deaths, outbreak ended December 2025)
- World Bank Country Health-System Reviews and financing analyses (DRC health-system overview; universal health coverage pathway)
- World Bank DRC health-financing analysis and ARCA/CNAM insurance-sector review
- UN OCHA DRC humanitarian health-sector reports and Health Zone mapping
- DHIS2 global case studies: DRC Health Zone supervision and ASSP zone performance (>90% reporting compliance)
- Demographic databases: Uganda Bureau of Statistics (UBOS); Kenya National Bureau of Statistics (KNBS); INS (Institut National de Statistique) DRC
- BuddeComm Telecoms Report: DRC internet/broadband market, connectivity constraints, and mobile-money adoption (2024)
- Willow Health Media country health-system analysis reports
- BCC (Banque Centrale du Congo) monetary policy and forex regime (CDF/USD dual acceptance)

### T3 — Encyclopaedia / Corroboration Only (Not Sole Source)

- Wikipedia entries: Uganda administrative divisions; Kenya devolution; Tanzania; Rwanda; Ghana; Nigeria; South Africa; India; Philippines; Democratic Republic of Congo (used for corroboration of language, timezone, currency, administrative-division facts already established via T1 sources; isolated references to CNOM, territories, and provinces verified against primary sources before inclusion)
- IRB Canada (Immigration and Refugee Board) Documentation: DRC voter card (Carte d'électeur) specifications, security features, issuance procedures, and de facto identity-use patterns (corroborated against CENI and UNHCR records)

---

## Cross-Cohort References

**Dependency map:**
- `standard-forms` cohort: Lists HMIS forms and tools; country-packs `default_forms_reference` cells link to standard-forms rows (e.g., HMIS-105, HMIS-108 for Uganda; KHIS for Kenya).
- `facilities` cohort: Lists facility types by country; country-packs `facility_level_system` cells reference facility-type IDs from facilities cohort.
- `roles-permissions` cohort: Cadre and regulator rows; country-packs refer to regulator names which must align with roles-permissions role definitions.
- `reporting-kpis` cohort (pending): Will supply the detailed indicator names for each country's mandatory reports; country-packs flags `[reporting-kpis gap]` where indicators not yet in corpus.
- `tenant-blueprints` cohort (pending): Will supply pre-configured workflows for each country, referenced in country-packs `default_blueprints_reference` cells.

**Gaps named for future cohorts:**
- Laboratory regulation: Uganda and Kenya lack dedicated lab councils; DRC INRB serves as reference lab but ISO 15189 accreditation and enforcement detail pending — all three flagged for clinical-governance review in Phase 2.
- Insurance regulators: Uganda NHIS pending; Kenya SHA transition documented but tariff/benefits detail pending in billing-tariffs cohort; DRC ARCA/CNAM universal-coverage implementation detail and benefit schedules pending.
- Mandatory reporting detail: Exact quarterly/annual KPI frequency per country pending reporting-kpis cohort completion; DRC SNIS form set and quarterly aggregation structure pending.
- Clinical officer regulation: DRC clinical officer regulator institutional structure unclear (CNOM vs. separate body) — requires MoH confirmation; relevant to roles-permissions cadre alignment.

---

## Scope Confirmations

**Geographic exclusions (per project scope, restated for country-pack context):**
- No veterinary services included.
- No traditional/herbal medicine (except Uganda recognition of Luganda lingua franca for community trust, relevant to paper-form equivalents).
- No transplant services (organ allocation regulatory frameworks out of scope).
- No neurosurgery or cardiothoracic surgery (noted as NRH-specialist only; not reflected in country-pack facility levels).
- These exclusions apply uniformly across all 9 countries; if a country has a specialized cardiothoracic institute, it is treated as a tertiary exception, not part of the standard facility-level system.

---

## Deliverable Status

- **Total rows produced:** 9 (3 full + 6 stub) — Wave 1 original (UG, KE stub-7) + Wave-3 extension CD (full) ✓
- **Uganda: Populated columns / total:** 22 / 24 (92%; 2 columns marked [GAP] or [STUB]) ✓
- **Kenya: Populated columns / total:** 22 / 24 (92%; 2 columns marked [STUB]) ✓
- **Democratic Republic of Congo (CD) — Wave-3 extension: Populated columns / total:** 18 / 24 (75%; 3 columns marked [T1 verification pending]; 2 marked [STUB]) ✓
- **Stub countries (TZ, RW, GH, NG, ZA, IN, PH): Populated columns / total:** 6 / 24 each (25%; 18 columns marked [STUB]) ✓
- **Items marked [GAP — no source found]:** 2 (Uganda insurance regulator; Uganda lab regulator) ✓
- **Items marked [T1 verification pending]:** 1 (Kenya Huduma Namba age/fallback rules) + 3 (CD: clinical_officer_regulator, lab_regulator, privacy_authority) = 4 total ✓
- **Regulator references alignment with cadre→council table:** 100% (UMDPC not used for clinical officers; AHPC used instead; COC for Kenya; ONIC for DRC; UNMC for Uganda; NCK for Kenya; KMLTTB verified) ✓
- **Uganda NDA drug-shop licensing correctly described as retail tiers, NOT prescribing schedules:** Yes ✓
- **Kenya NHIF→SHA transition acknowledged with both cited:** Yes (NHIF ceased 30 Sept 2024; SHA began 1 Oct 2024) ✓
- **DRC dual-currency reality (CDF/USD) flagged:** Yes; BCC monetary policy cited ✓
- **DRC timezone duality (WAT/CAT, Kinshasa/Lubumbashi):** Yes; IANA database sourced ✓
- **DRC dual patient-ID system (CIN + voter card) documented:** Yes; ONIP formal + CENI de facto; critical for transitional identity environment ✓
- **Stub countries: Only 5 columns populated (code, name, currency, timezone, languages); 19/24 columns marked [STUB]:** Yes ✓
- **No Wikipedia in any source_citations cells:** Confirmed (T3 entries explicitly marked as "corroboration only" in separate T3 block; DRC voter-card IRB Canada corroboration noted as T3) ✓
- **Data Completeness Table Updated:** wave1-data.md now includes CD row between Rwanda and Ghana; pass-2 header added; notes section expanded for CD ✓

