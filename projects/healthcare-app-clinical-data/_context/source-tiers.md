# Source Tiers — per cohort

**Date:** 2026-05-03

The tier system controls what counts as authoritative for each cohort. Sub-agents must cite **T1 as primary** wherever a T1 source covers the claim. T2 may corroborate or fill T1 gaps. T3 is **never sole source** — must be paired with at least one T1 or T2.

---

## Conditions

**T1 (must cite where applicable)**
- WHO ICD-10 official browser — `https://icd.who.int/browse10/2019/en`
- IHME Global Burden of Disease 2021 country profiles for Uganda, Kenya, Tanzania — `https://www.healthdata.org/research-analysis/health-by-location`
- WHO Country Cooperation Strategy briefs for Uganda, Kenya, Tanzania
- Uganda Annual Health Sector Performance Report (AHSPR), latest available
- Uganda Clinical Guidelines (UCG), latest edition

**T2 (corroboration / gap-fill)**
- Kenya Health Sector Strategic Plan (KHSSP)
- Tanzania National Health Policy and Standard Treatment Guidelines (STG)
- Lancet Global Health country burden papers
- DHS Program — Uganda DHS 2022, Kenya DHS 2022, Tanzania DHS 2022 — `https://dhsprogram.com`
- PubMed-indexed peer-reviewed literature

**T3 (corroborating only, never sole source)**
- UNICEF country profiles
- WHO regional bulletins
- Hospital-based observational studies

---

## Drugs

**T1**
- Uganda Essential Medicines and Health Supplies List (EMHSLU), latest edition (Ministry of Health Uganda)
- WHO Model List of Essential Medicines, 23rd edition (2023) — `https://www.who.int/publications/i/item/WHO-MHP-HPS-EML-2023.02`
- WHO Model List of Essential Medicines for Children (EMLc), 9th edition
- Uganda National Drug Authority register — `https://search.nda.or.ug`
- Kenya Pharmacy and Poisons Board register
- Tanzania Medicines and Medical Devices Authority (TMDA) register
- Uganda Clinical Guidelines (drug-prescribing sections)
- WHO ATC/DDD index — `https://www.atcddd.fhi.no/atc_ddd_index/`

**T2**
- British National Formulary (BNF) and BNF for Children
- Kenya Essential Medicines List
- Tanzania National Essential Medicines List (NEMLIT) and STG

**T3**
- Manufacturer Summary of Product Characteristics (SmPCs) — for brand verification only

---

## Lab tests

**T1**
- LOINC database — `https://loinc.org`
- Uganda Ministry of Health Laboratory Services SOPs / Uganda National Health Laboratory Diagnostic Services Policy
- Tietz Textbook of Clinical Chemistry and Molecular Diagnostics (reference ranges)
- WHO laboratory manuals (haematology, clinical chemistry, microbiology)

**T2**
- Mulago National Referral Hospital lab handbook (where accessible)
- Aga Khan University Hospital Nairobi lab manual
- Muhimbili National Hospital lab manual
- Peer-reviewed papers on East African reference intervals

**T3**
- Lab manufacturer reagent inserts

---

## Imaging

**T1**
- LOINC (imaging procedure codes)
- RadLex Playbook (RSNA) — `https://www.rsna.org/practice-tools/data-tools-and-standards/radlex-radiology-lexicon`
- ACR Practice Parameters and Technical Standards
- Royal College of Radiologists iRefer guidelines
- WHO diagnostic imaging manuals (where applicable)
- Uganda Atomic Energy Council guidance / Uganda Society of Radiology resources where available

**T2**
- RSNA structured radiology reporting templates — `https://radreport.org`
- Pan-African Congress of Radiology resources
- Peer-reviewed structured-reporting papers

**T3**
- Hospital-specific reporting templates

---

## Procedures

**T1**
- ICD-10-PCS reference (CMS) — `https://www.cms.gov/medicare/icd-10/2024-icd-10-pcs`
- WHO International Classification of Health Interventions (ICHI) beta — `https://icd.who.int/dev11/l-ichi/en`
- ADA CDT 2024 (Code on Dental Procedures and Nomenclature)
- Uganda Clinical Guidelines (procedural sections)
- Uganda MoH Health Sector Service Standards & Service Delivery Standards (which procedure at which level of care)

**T2**
- WHO Surgical Care at the District Hospital (still the standard reference manual for sub-Saharan Africa)
- Maurice King's Primary Surgery (Vol 1 & 2)
- Kenya MoH norms and standards
- Tanzania STG procedural sections

**T3**
- Specialist society guidelines (RCOG, RCS, AAOS, etc.) for cross-checking

---

## Triangulation rule

Per the repo `source-evaluation` skill: any T3-only claim must be triangulated against ≥2 T1/T2 sources before appearing as fact. Any URL citation must be paired with an archive snapshot reference (e.g., `web.archive.org`) where feasible.

## Citation format

Every cited source gets a BibTeX-style key in `_registry/sources.bib`. Inline citations in research outputs use the key (e.g., `[who-eml-2023]`, `[ihme-gbd-uganda-2021]`).
