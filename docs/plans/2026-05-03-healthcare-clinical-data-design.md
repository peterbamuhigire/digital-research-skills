# Healthcare App Clinical Data Corpus — Design

**Date:** 2026-05-03
**Project ID:** `healthcare-app-clinical-data`
**Client:** Internal team building a healthcare management app for Uganda
**Status:** Design approved — implementation plan pending (`writing-plans` skill is the next step)

---

## 1. Goal

Produce a thoroughly sourced, locally-accurate clinical data corpus the app team can use to seed dropdowns, structured records, decision logic, and reference content. Five cohorts, each delivered as a Word `.docx` report + Excel `.xlsx` data sheet, plus a cross-cohort master document.

| # | Cohort | Min items | Coding standard |
|---|---|---|---|
| 1 | Most commonly diagnosed conditions | 200 | ICD-10 |
| 2 | Most commonly prescribed/issued drugs | full Uganda EMHSLU (~700) cross-mapped to WHO EML | ATC |
| 3 | Most common laboratory tests | 200 | LOINC |
| 4 | Most common imaging tests | 200 | LOINC + RadLex |
| 5 | Most common medical procedures (incl. dental) | 200 | ICD-10-PCS + CDT (dental) + ICHI secondary |

---

## 2. Confirmed scope parameters

- **Geography:** Uganda primary; Kenya + Tanzania for triangulation
- **Ranking basis:** IHME GBD 2021 + WHO country profiles (DALYs / mortality), not HMIS volumes
- **Population:** All-ages merged with `population` column (adult / paeds / neonatal / obstetric / geriatric / all)
- **Drug brand listing:** INN + 4 locally-registered brands (Uganda NDA primary, Kenya PPB + Tanzania TMDA secondary). Drugs not registered locally are flagged and given internationally common brands as fallback.
- **Lab/imaging detail:** Full structured template (data-model depth — specimen, units, ranges, critical values, turnaround, interferences for labs; structured reporting fields and key measurements for imaging). No prose example reports.
- **Hard exclusions:** veterinary, traditional/herbal medicine, cardiothoracic surgery, neurosurgery, transplant
- **Hard inclusions:** dental procedures (CDT codes)

---

## 3. Project layout

```
projects/healthcare-app-clinical-data/
├── README.md                          (project charter + scope-exclusions)
├── CLAUDE.md                          (sub-agent invariants for this project)
├── PROJECT-STATUS.md                  (wave tracker — resumption anchor)
├── EVIDENCE-AUDIT.md                  (every struck/flagged claim)
├── _context/
│   ├── client-brief.md
│   ├── geographic-scope.md            (Uganda + Kenya + Tanzania)
│   ├── coding-standards-master.md     (reused in every Word report)
│   ├── source-tiers.md                (per-cohort allowed sources)
│   └── exclusions.md                  (verbatim hard exclusions)
├── _registry/
│   └── sources.bib
├── conditions/                        research/ analysis/ opportunities/
├── drugs/                             research/ analysis/ opportunities/
├── lab-tests/                         research/ analysis/ opportunities/
├── imaging/                           research/ analysis/ opportunities/
├── procedures/                        research/ analysis/ opportunities/
└── export/
    ├── 01-conditions-report.docx      + 01-conditions-data.xlsx
    ├── 02-drugs-report.docx           + 02-drugs-data.xlsx
    ├── 03-lab-tests-report.docx       + 03-lab-tests-data.xlsx
    ├── 04-imaging-report.docx         + 04-imaging-data.xlsx
    ├── 05-procedures-report.docx      + 05-procedures-data.xlsx
    └── 00-cross-cohort-master.docx
```

`opportunities/` is repurposed per-cohort as `app-implementation-notes`.

---

## 4. Data models (Excel column specs)

### 4.1 Conditions

`icd10_code`, `icd10_title`, `icd10_chapter`, `icd10_block`, `common_name_en`, `common_name_local`, `category_burden` (Communicable / NCD / Maternal-Neonatal / Injury / Mental-Behavioural), `population`, `daly_rank_uganda`, `daly_rank_kenya`, `daly_rank_tanzania`, `notifiable_uganda` (Uganda IDSR), `clinical_notes`, `ucg_reference`, `source_tier`, `source_citation`.

### 4.2 Drugs

`atc_code`, `atc_level1` … `atc_level4`, `inn`, `who_eml_inclusion` (Adult / Children / Both / None), `who_eml_section`, `emhslu_inclusion`, `emhslu_vital_essential_necessary` (V/E/N), `emhslu_level_of_care` (HC II/III/IV/GH/RRH/NRH), `dosage_forms`, `strengths`, `population`, `paeds_dose_summary`, `adult_dose_summary`, `key_indications`, `brand_inn`, `brand_1`–`brand_4`, `brand_1_holder`–`brand_4_holder`, `registered_uganda_nda`, `registered_kenya_ppb`, `registered_tanzania_tmda`, `controlled_substance_schedule`, `storage`, `source_tier`, `source_citation`.

### 4.3 Lab tests

`loinc_code`, `loinc_long_common_name`, `loinc_class`, `discipline_grouping` (Haematology / Clinical Chemistry / Microbiology / Serology / Endocrinology / Histopathology / Molecular), `test_name_local`, `specimen_type`, `specimen_volume`, `container`, `methodology_typical`, `units_si`, `units_conventional`, `ref_range_adult_male`, `ref_range_adult_female`, `ref_range_paeds`, `ref_range_neonate`, `critical_low`, `critical_high`, `turnaround_time_routine`, `turnaround_time_urgent`, `common_interferences`, `level_of_care_available`, `population`, `clinical_indications`, `source_tier`, `source_citation`.

### 4.4 Imaging

`loinc_code`, `radlex_id`, `modality` (XR/US/CT/MRI/Fluoro/Mammo/DEXA/NucMed), `body_region`, `study_name`, `indication_top3`, `contrast_used`, `radiation_dose_typical`, `report_template_fields` (structured list), `key_measurements` (numerical fields with units), `level_of_care_available`, `population`, `preparation_required`, `source_tier`, `source_citation`.

### 4.5 Procedures

`icd10_pcs_code`, `cdt_code` (dental), `who_chi_code` (ICHI secondary), `procedure_name`, `category` (OB-Gyn / Gen Surg / Ortho / ENT / Ophth / Urol / Paeds / Dental / Minor / Anaesthesia / Emergency), `body_system`, `setting`, `level_of_care_minimum`, `anaesthesia_typical`, `typical_duration_min`, `key_indications`, `cadre_who_performs`, `consent_required`, `population`, `notes`, `source_tier`, `source_citation`.

---

## 5. Source tiers per cohort

**Conditions** — T1: WHO ICD-10, IHME GBD 2021, WHO CCS, Uganda AHSPR, Uganda Clinical Guidelines. T2: Kenya KHSSP, Tanzania STG, Lancet Global Health, DHS 2022 (UG/KE/TZ), PubMed peer-reviewed. T3: UNICEF, WHO regional bulletins, hospital studies (corroborating only).

**Drugs** — T1: Uganda EMHSLU (latest), WHO EML 23rd ed. + EMLc 9th, Uganda NDA register, Kenya PPB register, Tanzania TMDA register, Uganda Clinical Guidelines, WHO ATC/DDD index. T2: BNF, BNFc, Kenya EML, Tanzania STG/NEMLIT. T3: Manufacturer SmPCs (brand verification only).

**Labs** — T1: LOINC, Uganda MoH Lab Services SOPs, Uganda National Health Laboratory Diagnostic Services Policy, Tietz Textbook of Clinical Chemistry, WHO laboratory manuals. T2: Mulago/Aga Khan Nairobi/Muhimbili lab handbooks, peer-reviewed East African reference interval studies. T3: Manufacturer reagent inserts.

**Imaging** — T1: LOINC, RadLex Playbook (RSNA), ACR Practice Parameters, RCR iRefer, WHO diagnostic imaging manuals, Uganda Atomic Energy Council / Uganda Society of Radiology. T2: RSNA reporting templates, Pan-African Congress of Radiology, peer-reviewed structured-reporting papers. T3: Hospital-specific templates.

**Procedures** — T1: ICD-10-PCS (CMS), WHO ICHI beta, ADA CDT 2024, Uganda Clinical Guidelines (procedural), Uganda MoH Health Sector Service Standards. T2: WHO Surgical Care at the District Hospital, Maurice King's Primary Surgery, Kenya MoH norms, Tanzania STG procedural. T3: Specialist society guidelines (RCOG/RCS/etc.).

---

## 6. Execution plan (phased)

### Phase 0 — Scaffold (orchestrator)
Create directory tree, write README/CLAUDE/PROJECT-STATUS/EVIDENCE-AUDIT, populate `_context/coding-standards-master.md` (reused in every report), `_context/source-tiers.md`, `_context/exclusions.md`, initial `_registry/sources.bib`.

### Phase 1 — Wave 1 (6 parallel sub-agents, background)
One sub-agent per cohort, with the drugs cohort split into two (ATC A–J and ATC L–V) due to size. Each `Agent(subagent_type: content-marketing:search-specialist, run_in_background: true)`. Briefs are self-contained:
- Goal, scope, exclusions verbatim
- Data-model columns (from §4)
- T1/T2/T3 sources (from §5)
- **Verbatim hard-constraint clause from `skills/source-evaluation/references/evidence-discipline.md`**
- Output: `<cohort>/research/wave1-findings.md` + `<cohort>/research/wave1-data.md` (markdown table)
- "Mark gaps as `[GAP — no source found]`; do not fabricate"

Targets: 220 conditions / full ~700 drugs / 220 labs / 220 imaging / 220 procedures (buffer above 200 for QA strikes).

### Phase 2 — QA loop (orchestrator, per cohort)
1. Spot-check 10% of stats via WebFetch
2. Verify all ICD-10/ATC/LOINC/CDT codes (sample)
3. Verify 5 quotes per cohort
4. Verify all statute/regulation citations
5. Run `gap-analysis` skill for completeness and category balance
6. Strike-and-log to `EVIDENCE-AUDIT.md`
7. Compute Wave-2 gap-fill brief

### Phase 3 — Wave 2 gap-fill
Sub-agents briefed on specific gap lists. Outputs append with `# Pass 2 — Gap-fill addendum` headers. Condensed QA on new content.

### Phase 4 — Critical reasoning + cross-cohort synthesis
- `critical-reasoning-and-argument` over each cohort's analysis
- `cross-cohort-synthesis` (orchestrator-only) → `00-cross-cohort-master.md`: condition↔drug↔lab↔imaging↔procedure clusters (e.g., malaria → antimalarials → mRDT/microscopy → no imaging → no procedure), corpus-level coverage gaps, app-implementation notes.

### Phase 5 — Deliverable assembly
Per cohort, generate `.docx` via `professional-word-output` and `.xlsx` via `document-skills:xlsx`.

**Word structure:** Cover + exec summary → §1 Coding standard explained → §2 Methodology → §3 Categorised list with commentary → §4 Gaps and limitations → §5 App-implementation notes → Appendix A data table → Appendix B bibliography by tier.

**Excel sheets:** `data` / `categories` / `sources` / `audit` / `readme`.

Plus `00-cross-cohort-master.docx`.

---

## 7. Evidence discipline

Per project CLAUDE.md and `source-evaluation` skill:
- Verbatim hard-constraint clause in every sub-agent brief
- Never tail sub-agent outputs via shell — only structured `<result>` blocks
- Every struck claim → `EVIDENCE-AUDIT.md`
- Every cited URL → `_registry/sources.bib` with access date
- Append, don't overwrite, on Wave-2 merges

---

## 8. Known risks / methodology notes (to be reflected in reports)

1. **Uganda EMHSLU edition** — depends on public availability of the latest edition. Edition used will be cited; drugs that may have moved on/off since will be flagged.
2. **NDA brand verification at scale** — 700 individual NDA register lookups is impractical. Plan: per-drug NDA verification for the highest-priority ~200; for the remainder, brands cited from EMHSLU listings without per-drug NDA confirmation. Methodology disclosed in the report.
3. **East African lab reference ranges** — published locally-validated ranges exist for some analytes only. Where missing, Tietz/Western ranges are used and explicitly marked `[reference range from Western source — local validation pending]`.
4. **ICD-10-PCS vs ICHI** — ICD-10-PCS (CMS) used as primary for procedures with ICHI (WHO, beta) as secondary; choice explained in report.
5. **CDT licensing** — ADA-licensed. Codes used with attribution; report flags the licensing constraint for the app team's commercial rollout.

---

## 9. Time / cost shape

Multi-session project. PROJECT-STATUS.md is the resumption anchor.

- Phase 0: ~15 min orchestrator
- Phase 1: 6 parallel background sub-agents, wall-clock ~30–60 min
- Phase 2: ~30–45 min QA per cohort
- Phase 3: 3–5 background sub-agents, ~20–40 min
- Phase 4: ~30–45 min orchestrator
- Phase 5: ~30 min per cohort × 5 + ~30 min cross-cohort

---

## 10. Next step

Invoke `superpowers:writing-plans` to convert this design into a step-by-step implementation plan with explicit verification gates.
