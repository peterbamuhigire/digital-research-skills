# Automated Healthcare-Facility Onboarding — Design

**Date:** 2026-05-04
**Status:** Draft v1, approved through brainstorming
**Project:** healthcare-app-clinical-data → Medic8
**Authors:** Peter Bamuhigire (product) + Claude (design partner)
**Related:**
- `projects/healthcare-app-clinical-data/` (research corpus that becomes the global seed)
- Onboarding requirements catalogue (provided 2026-05-04, 25 sections + 2 appendices)
- `docs/plans/2026-05-03-healthcare-clinical-data-design.md` (research data-model design)

---

## Executive summary

Medic8 needs to onboard a new healthcare facility — clinic, hospital, mission hospital, NGO project site, multi-facility group — fast enough to win against competitors who take weeks. The benchmark goal is "live in days, complete in weeks" rather than a hard 3-hour SLO; the 3-hour figure is marketing illustration of the AI-augmented portion of the pipeline.

The design is a **two-track convergent pipeline**:

- **Greenfield track** ingests rigid, dropdown-driven Excel templates (auto-generated per tenant from country + blueprint + capability flags). Server-side AI is light, used only on free-text and local extensions.
- **Brownfield track** ingests whatever the facility provides — QuickBooks export, Tally stock statement, paper register photo, supplier price list. Server-side AI does file-kind detection, OCR where needed, column detection, value normalisation, and seed alignment.

Both tracks land in a **single staging schema** and route through a **risk-tiered reviewer console**:

- Controlled drugs / vaccines / paediatric formulations / blood products → 100% manual review.
- High-risk classes (antibiotics, anaesthetics, ART, insulin, maternal critical-care) → manual review unless very-high-confidence, with mandatory sample audit.
- Routine items → auto-accept above per-catalogue confidence threshold; exception queue below; reject under floor.
- Prices → never AI-set; always human.

Acceptance is gated by **Tier-1** catalogue completeness (the minimum to legally and clinically operate, mapped to §22.1 of the requirements doc) plus smoke tests against staging plus dual sign-off (Director + Medic8 ops). **Tier-2** catalogues — patient migration, opening AR/AP, full consumable tail, BOM overrides, scheme tariff matrices — complete asynchronously post-go-live without blocking patient service.

Every cohort that contributes to the global seed ships a paired `(catalogue.docx, catalogue.xlsx)` artifact. The Excel is what Medic8's seed-loader consumes. The Word is what the facility signer reads before they tick-and-price. Word reports are auto-generated from the same markdown corpus the cohorts already produce, extended with an enriched §0–§9 structure.

---

## 1. Background and constraints

The healthcare-app-clinical-data research project produces 14 cohorts of catalogue data that will become Medic8's global seeds. Per the onboarding requirements doc, a facility cannot serve a single patient until 11 clinical + 3 operational catalogues are loaded, validated, and signed off. The design closes the loop from research-corpus → tenant-scoped seed → live facility.

### 1.1 Decisions made during brainstorming

| # | Decision | Rationale |
|---|---|---|
| D1 | Deliverable = design doc, then implementation plan (no code in this session) | Medic8 codebase isn't in this repo; prototype would target a strawman |
| D2 | 3-hour target = AI-augmented portion only; "live in days, complete in weeks" is the real goal | Honest framing — humans count drugs, not AI |
| D3 | Enriched Word reports bundled into onboarding deliverable, not separate workstream | One coherent contract per cohort: docx + xlsx pair |
| D4 | Architecture = Approach C (hybrid two-track: rigid templates for greenfield, freeform-AI for brownfield, converging on shared staging) | Only honest match to the two real client populations |
| D5 | Tier-1 / Tier-2 split — Tier-1 inside the go-live gate, Tier-2 deferred async | Maps to §22.1 of the requirements doc |
| D6 | AI trust model = hybrid risk-tiered (Q3 option d) | Defensible to regulators; cost-tractable |
| D7 | 8 catalogue gaps commissioned as Wave-3 cohorts | Vaccines, BOMs, DDIs, allergens, paeds-dosing, UCUM, holidays, country-packs full extension |
| D8 | Seed bundle is versioned + tenant-pinned at onboarding | Protects facility-side prices/BOMs/pathways from silent drift |

### 1.2 Hard exclusions (carry forward from project CLAUDE.md)

- Veterinary, traditional/herbal, cardiothoracic surgery, neurosurgery, transplant surgery — not in seed corpus, not in onboarding.
- Geographic primary: Uganda; full triangulation Kenya + Tanzania; secondary RW/CD/NG via country-packs Wave-3.

---

## 2. High-level architecture

```
┌───────────────────────────────────────────────────────────────────────┐
│  GLOBAL SEED CORPUS (output of healthcare-app-clinical-data project)  │
│  drugs · lab-tests · imaging · procedures · conditions · consumables  │
│  · standard-forms · facilities · roles · workflows · country-packs    │
│  · billing-tariffs · reporting-kpis · tenant-blueprints               │
│  + Wave-3: vaccines · BOMs · DDIs · allergens · paeds-dosing · UCUM   │
│  · holiday-calendars · country-packs full extension                   │
│                                                                       │
│  Published as: seed-bundle-vMAJOR.MINOR.PATCH.zip                     │
│  (per-cohort .docx + .xlsx + .md, manifest.json, signed)              │
│  Refreshed quarterly. Tenants pin to the version they onboarded under.│
└───────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌───────────────────────────────────────────────────────────────────────┐
│  PRE-KICKOFF (T-3 weeks before go-live)                               │
│  Super-admin selects: country + tenant blueprint + capability flags   │
│  → Auto-generates per-tenant Excel template pack with embedded        │
│    dropdowns from country-scoped seed slice, in EN/FR/SW              │
│  → Email pack from onboarding@medic8.health (audit logged)            │
└───────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
                    ┌─────────────┴──────────────┐
                    ▼                            ▼
           GREENFIELD PATH               BROWNFIELD PATH
        (rigid template ingest)      (freeform legacy upload)
                    │                            │
       Schema-validate workbook      AI: file-kind detect → OCR
       Dropdown picks → seed IDs     AI: catalogue classify
       Free-text → light AI          AI: column detect
                                     AI: value normalise → seed ID
                                     Confidence + rationale logged
                    │                            │
                    └─────────────┬──────────────┘
                                  ▼
┌───────────────────────────────────────────────────────────────────────┐
│  STAGING SCHEMA (per session, per catalogue)                          │
│  tbl_staging_<catalogue>: source_kind, source_ref, mapped_seed_id,    │
│  confidence, ai_rationale, alternates_considered, status              │
└───────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌───────────────────────────────────────────────────────────────────────┐
│  RISK-TIERED REVIEWER CONSOLE                                         │
│  4 queues per catalogue: auto · critical · exceptions · done          │
│  Risk tier from seed (controlled/paeds/vaccine = 100% review)         │
│  Per-catalogue signer (Pharmacist / Lab Manager / Med Director / …)   │
│  Sign-off hash re-locks gate if staging mutates after                 │
└───────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌───────────────────────────────────────────────────────────────────────┐
│  ACCEPTANCE GATE                                                      │
│  Tier-1 catalogues signed · cross-FKs resolve · GL accounts mapped    │
│  · BOMs approved · 6 smoke tests pass · dual sign-off                 │
└───────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
              tbl_facilities.onboarding_status = LIVE
                                  │
                                  ▼
              Tier-2 async track: patient migration · opening AR/AP
              · full consumable tail · BOM overrides · scheme tariffs
              (does not block patient service)
```

### 2.1 Architectural invariants

1. **Seed → template → staging → production** is a strict one-way flow. Production tables are written only by the promotion job, never by Excel uploads directly.
2. **Greenfield and brownfield converge on a shared staging schema.** Reviewer console doesn't distinguish except for the `source_kind` badge.
3. **AI rationale is logged on every mapped row.** Regulator audit answer is one DB column away.
4. **Risk tier is derived from the mapped seed, not from AI confidence.** A controlled drug at confidence 0.99 still gets 100% review.
5. **AI never invents prices.** Always human-set; reviewer = accountant.
6. **Seed bundles are versioned and tenant-pinned at onboarding.** No silent drift.
7. **Tier-1 / Tier-2 are flags on catalogue config, not separate pipelines.** Same code path; different completion gates.
8. **Every seed-producing cohort ships paired (Word + Excel).** The Excel is machine-loaded; the Word is human-read; the markdown is the source-of-truth substrate.

---

## 3. Pre-kickoff: seed publication & template generation

### 3.1 Seed bundle structure

```
seed-bundle-v<MAJOR>.<MINOR>.<PATCH>.zip
├── manifest.json              # cohort list, row counts, sha256 per file, semver
├── signature.asc              # detached PGP signature over manifest.json
├── cohorts/
│   ├── drugs/
│   │   ├── drugs.xlsx         # canonical seed data (Medic8 ETL consumes)
│   │   ├── drugs.docx         # facility-facing explainer (intake pack)
│   │   ├── drugs.md           # source markdown (audit only)
│   │   └── drugs.bib          # citations
│   ├── lab-tests/
│   ├── imaging/
│   ├── procedures/
│   ├── conditions/
│   ├── consumables/
│   ├── standard-forms/
│   ├── facilities/
│   ├── roles-permissions/
│   ├── workflows/
│   ├── country-packs/
│   ├── billing-tariffs/
│   ├── reporting-kpis/
│   ├── tenant-blueprints/
│   ├── vaccines/              # Wave-3 new
│   ├── boms/                  # Wave-3 new
│   ├── drug-interactions/     # Wave-3 new (DDInter-derived + curated)
│   ├── allergens/             # Wave-3 new (RxNorm-derived)
│   ├── paediatric-dosing/     # Wave-3 new (WHO Children's Formulary)
│   ├── ucum/                  # Wave-3 new
│   └── holiday-calendars/     # Wave-3 new
├── cross-cohort-master.docx
└── CHANGELOG.md
```

### 3.2 Versioning rules

- **MAJOR** bump: schema-breaking column changes.
- **MINOR** bump: new cohort, new rows, additive fields.
- **PATCH** bump: corrections, citation updates, label translations.

Tenants pin to bundle version at onboarding. Migration to a newer bundle is a deliberate, signed-off action — never silent.

### 3.3 Template generator inputs

When the super-admin opens a new onboarding session, three inputs drive template generation:

1. **Country** (`UG | KE | TZ | RW | CD | NG`) → applies country-pack: currency, EML overlay, HMIS row codes, regulator references, language defaults, holiday calendar.
2. **Tenant blueprint** (1 of 6 canonical: small clinic, HC III, HC IV, general hospital, standalone lab, standalone pharmacy) → seeds default capability flags, default cost centres, default ward structure, default Tier-1 catalogue subset.
3. **Capability overrides** (additive): `+IMAGING_CT`, `+ART_HIV`, `+EPI`, `+THEATRE`, `+BLOOD_BANK`, etc. — toggles which catalogues appear.

### 3.4 Per-tenant template pack

```
onboarding-pack-<facility-id>-v<bundle-version>/
├── 00-intake-guide.<locale>.pdf         # generated from cohort .docx files
├── 01-facility-profile.xlsx              # one row, structured form
├── 02-departments-cost-centres.xlsx     # tier-default rows pre-filled
├── 03-staff-roll.xlsx
├── 04-diagnosis-tick-list.xlsx          # Top-200 pre-ticked per blueprint
├── 05-service-catalogue.xlsx            # blueprint-default rows; price blank
├── 06-drug-formulary.xlsx               # country-EML pre-ticked; ATC dropdown
├── 07-lab-test-catalogue.xlsx           # WHO EDL pre-ticked; LOINC dropdown
├── 08-vaccine-catalogue.xlsx            # country EPI schedule pre-ticked
├── 09-imaging-catalogue.xlsx            # only if +IMAGING_*
├── 10-consumable-master.xlsx            # GMDN dropdown
├── 11-bom-overrides.xlsx                # blank (defaults auto-accepted)
├── 12-insurer-tariff-<scheme>.xlsx      # one per declared scheme
├── 13-pathway-enable.xlsx               # blueprint-default ticked
└── 99-brownfield-upload/                # optional; legacy files dropped here
    └── README.txt
```

Workbooks are **digitally fingerprinted** with `bundle_version + facility_id + generated_at`. Server rejects uploads where fingerprint is missing or bundle version no longer accepted.

Locale: visible labels rendered EN/FR/SW per facility default; `_seed` sheet keys stay canonical (ATC, LOINC, etc.).

### 3.5 Intake-pack delivery

Generated on-demand from `/adminpanel/facilities/{id}/onboarding-assets/` (per requirements doc §24). Email from `onboarding@medic8.health` with delivery audit (`ONBOARDING.ASSETS_EMAILED`). Re-send delta when bundle version changes.

---

## 4. Greenfield path: rigid template ingest

### 4.1 Upload & fingerprint check

Facility owner uploads completed pack to `/onboarding/{session-id}/upload`. Server checks each workbook independently:

- **Fingerprint match** — `bundle_version`, `facility_id`, `generated_at` from `_meta` sheet vs session record. Fails → reject with "regenerate template pack."
- **Schema match** — column count + header names against bundle's expected schema. Fails → reject with row/col diff.
- **Data-validation pass-through** — every dropdown-coded cell holds a key in `_seed` sheet. Fails → row-level error report.

No row enters staging until all three pass for that workbook.

### 4.2 Row classification

Each row tagged with `source_kind`:

| `source_kind` | Meaning | AI work |
|---|---|---|
| `DROPDOWN_PICK` | Coded cell holds a valid seed key | None — direct map |
| `BLUEPRINT_DEFAULT` | Pre-filled by template generator and unchanged | None — verify checksum |
| `FREEFORM_TEXT` | Free-text field (trading_name, brand additions, synonyms) | Light AI: locale detect, profanity / PII screen |
| `LOCAL_EXTENSION` | "Non-formulary" / "facility-specific" row | AI: best-effort seed alignment + flag for reviewer |
| `PRICE` | Numeric, currency-scoped | None — sanity check |

Confidence = 1.00 for DROPDOWN_PICK / BLUEPRINT_DEFAULT; AI-generated for LOCAL_EXTENSION; N/A for PRICE.

### 4.3 Cross-row + cross-workbook validations (synchronous at upload)

- Referential integrity: every `service.linked_bom_id`, `bom.line.item_id`, department reference resolves.
- Required-field completeness per requirements doc §22.1.
- Numeric sanity: prices > 0, pack-to-base ratio > 0, reorder ≤ max, bed count = sum of ward beds.
- Locale completeness: `label_en` mandatory; FR + SW required only for facility-customised rows.

Failures surface as a per-workbook upload report before reviewer time is consumed.

### 4.4 Persistence model

```sql
tbl_onboarding_sessions (
  session_id PK, facility_id FK, bundle_version,
  status, opened_at, closed_at
)

tbl_staging_<catalogue> (    -- one table per catalogue
  staging_id PK, session_id FK, row_index,
  source_kind, source_ref,    -- "06-drug-formulary.xlsx!A42"
  raw_payload JSON,            -- as-uploaded row
  mapped_seed_id,              -- FK to global seed
  confidence DECIMAL,
  ai_rationale TEXT,
  alternates_considered JSON,
  risk_tier ENUM,
  status ENUM(PENDING,AUTO,REVIEW,APPROVED,REJECTED),
  reviewer_user_id, reviewed_at,
  reviewer_action ENUM(ACCEPT,REMAP,REJECT,ANNOTATE)
)

tbl_onboarding_audit (
  audit_id PK, session_id FK, event_kind,
  before JSON, after JSON, actor_user_id, occurred_at
)

tbl_onboarding_signoffs (
  signoff_id PK, session_id FK, catalogue, signer_user_id,
  signed_at, staging_snapshot_hash, bundle_version
)
```

Production tables (`tbl_drugs_facility`, etc.) are written only by the promotion job (§7).

---

## 5. Brownfield path: AI alignment pipeline

### 5.1 Stage 1 — File ingest & normalisation

| Input kind | Pipeline |
|---|---|
| `.xlsx`, `.xls`, `.csv`, `.tsv` | Direct → tabular extractor |
| `.pdf` (text) | `pdfplumber` → text + tables → tabular extractor |
| `.pdf` (scanned) | OCR (Azure Doc Intelligence default) → text → AI table reconstruction |
| `.jpg`, `.png` | OCR → AI table reconstruction |
| `.qbb`, `.qbo` (QuickBooks) | `qbtools` convert → CSV |
| `.tdb` (Tally) | Tally XML export required from facility |

Output: normalised `raw_table` JSON (header + data rows) + `provenance` blob (filename, page, OCR confidence per cell).

### 5.2 Stage 2 — Catalogue classification

First AI call classifies each `raw_table` against catalogue taxonomy. Returns `catalogue_kind`, `confidence`, `reasoning`. Below 0.80 → manual triage queue.

### 5.3 Stage 3 — Column detection

Per `raw_table`, AI maps facility columns to canonical schema. Logs per-column confidence and the rationale on every row.

### 5.4 Stage 4 — Value normalisation & seed alignment

Per row × column, AI derives canonical seed key. Strategy varies:

| Catalogue | Alignment strategy |
|---|---|
| **drug-formulary** | Free-text → ATC via INN/brand match. Strength + form parsed. Cross-check country EML. |
| **lab-test-catalogue** | Free-text → LOINC. Disambiguate by specimen + method. |
| **consumable-master** | Free-text → GMDN. Pack parsed; brand kept; risk-class inferred from GMDN node. |
| **service-catalogue** | Free-text → CPT/ICHI/local. Bundles flagged for blueprint mapping. |
| **diagnosis-tick-list** | Free-text + legacy code → ICD-10 leaf. Multi-code splits handled. |
| **vaccine-catalogue** | Free-text → ATC J07 + WHO PQS lot semantics. |
| **patient-migration** | Field-by-field cleansing: NIN, phone E.164, DOB parser, sex code. |
| **opening-AR / AP** | Aging recomputed from invoice dates; counterparty matched to insurer/vendor. |

Per-row output stored in staging:

```json
{
  "row_index": 42,
  "raw_payload": {"Drug Name": "Panadol 500", "Pack Size": "Box of 1000", ...},
  "mapped_seed_id": "DRUG-N02BE01-500MG-TAB",
  "confidence": 0.96,
  "ai_rationale": "INN paracetamol matched via brand 'Panadol'; strength 500mg parsed; tablet inferred from absence of liquid markers; pack 1000 → ratio=1000 base UOM TAB.",
  "alternates_considered": [
    {"seed_id": "DRUG-N02BE01-1000MG-TAB", "confidence": 0.04, "reason": "rejected — no '1g' marker"}
  ],
  "risk_tier": "ROUTINE"
}
```

### 5.5 Stage 5 — Risk-tier routing

Risk tier derived from the **mapped seed**, not the AI confidence:

| `risk_tier` | Rule | Reviewer treatment |
|---|---|---|
| `CRITICAL` | Controlled drug, vaccine, blood product, paeds-only formulation, narcotic | 100% manual review regardless of confidence |
| `HIGH` | Antibiotic (J01/J02/J04/J05), insulin, anaesthetic, ART, oxytocin, MgSO4 | Manual review if confidence < 0.95; else auto with mandatory sample |
| `ROUTINE` | All other drugs, consumables, lab tests, services | Auto-accept ≥ 0.92; review queue 0.70–0.92; reject < 0.70 |
| `PRICE` | Any monetary value | Always human-set; reviewer = accountant |
| `PII` | Patient names, NINs, phone | Auto-cleanse only; reviewer reviews dedupe collisions |

Confidence thresholds are **per-catalogue config**, tuned from pilot-tenant metrics.

### 5.6 Stage 6 — Persist to staging

Same staging schema as greenfield. `source_kind = AI_MAPPED`; `ai_rationale` populated.

### 5.7 Cost & latency budget

For a mid-size hospital (380 drugs + 200 consumables + 90 labs + 142 services + 287 diagnoses):

- ~1100 catalogue rows × ~1 LLM call per row × ~2k input + ~500 output tokens.
- Tractable on Claude Sonnet 4.6 in batched parallel calls.
- Wall-clock target: alignment run completes in **under 30 minutes** for a mid-size hospital.
- Patient migration is rule-based, not per-row LLM.
- AI provider: design is provider-neutral; default Claude API; OpenAI fallback for column-detect under rate-limit pressure.

---

## 6. Reviewer console & convergence layer

### 6.1 Four queues per catalogue tab

| Queue | Content | Exit condition |
|---|---|---|
| Critical review | All `CRITICAL` rows + sub-threshold `HIGH` rows | Empty — no skip |
| Exceptions | Sub-threshold `ROUTINE` rows | Empty — no skip |
| Auto-accepted | Above-threshold rows | Stratified 10% sample reviewed (auto-selected, not cherry-picked) |
| Done | Reviewed + signer-approved | Locked, read-only |

### 6.2 Row-card UX

Keyboard-driven (J/K nav, A accept, R remap, X reject, N annotate). Card shows: as-uploaded payload, mapped target with full attribution, AI rationale, alternates considered, action buttons.

`Remap` opens typeahead search over seed slice; logs `reviewer_action = REMAP` with old → new seed IDs.

### 6.3 Sign-off per catalogue

| Catalogue | Signer |
|---|---|
| Facility profile | Director |
| Departments / cost centres / wards | Facility Admin |
| Diagnoses + pathways | Medical Director |
| Service catalogue + prices | Medical Director + Accountant |
| Drug formulary | Pharmacist-in-Charge |
| Lab catalogue | Lab Manager |
| Imaging catalogue | Imaging In-Charge |
| Vaccine catalogue | EPI Focal Person |
| Consumable master | Store Keeper + Lab Manager |
| BOM overrides | Lab Manager + Imaging + Theatre + EPI (per scope) |
| Insurer schemes + tariffs | Insurance Clerk + Accountant |
| Staff roll | Facility Admin + HR |
| Patient migration (Tier-2) | Records Officer + Medical Director |

Sign-off enables only when all queues clear, FKs resolve, GL accounts mapped, §22.1 completeness satisfied.

Sign-off writes `tbl_onboarding_signoffs` with **hash of staging snapshot**. Mutation post-sign-off invalidates the hash and re-locks the gate.

### 6.4 Real-time validation strip

Per-tab strip surfaces queue counts, sample progress, missing-fields, sign-off button state. Updates in <1s on row changes; no page reload.

### 6.5 Re-upload semantics

- New rows merge by `source_ref`.
- Already-reviewed rows with unchanged `raw_payload` stay reviewed.
- Changed rows revert to `PENDING` and re-route through Stage 4.
- Banner notifies reviewer of "X rows reverted."

### 6.6 Audit log

Every action writes `tbl_onboarding_audit` with before/after JSON. Events: `ROW_REVIEWED`, `CATALOGUE_SIGNED`, `STAGING_HASH_BROKEN`, `ASSETS_EMAILED`, `GO_LIVE`.

---

## 7. Acceptance gates & go-live promotion

### 7.1 The promotion job

Single transactional `onboarding.promote(session_id)`:

1. **Snapshot** — staging → `tbl_onboarding_history` (immutable archive).
2. **Promote** — INSERT/UPDATE production tables keyed by `(facility_id, mapped_seed_id)`.
3. **Flip status** — `tbl_facilities.onboarding_status = LIVE`, `went_live_at = NOW()`, `ONBOARDING.GO_LIVE` audit log.

If any step throws → rollback; gate re-locks.

### 7.2 Gate-aggregate view

```
TIER-1 CATALOGUES SIGNED          12 / 12   ✓
TIER-1 CROSS-REFERENCES           ✓
GL ACCOUNTS MAPPED                ✓
BOMs APPROVED                     ✓
SMOKE TESTS                       6 / 6   ✓
  ✓ patient registration roundtrip
  ✓ OPD encounter end-to-end
  ✓ lab order → BOM → result → portal
  ✓ vaccine dose → AD-syringe deduction → EPI register
  ✓ HMIS 105 sample export matches expected
  ✓ insurance preauth flow (if any cashless scheme)
DUAL SIGN-OFF                     Director ✓   Medic8 ops ✓
                                                          [Promote to LIVE]
```

No "skip gate" admin override in standard flow — bypass is a separately-authenticated emergency action that triggers a P1 alert.

### 7.3 Smoke-test harness

Each smoke test scripts a scenario against staged tenant data with a synthetic `is_test = 1` patient. Assertions: stock decrement, journal post, register row insert. Tests run against **staging snapshots, not production** — re-runs cheap, no pollution.

### 7.4 Bundle-version pinning

Promotion record captures `bundle_version`. Every production row gets `seed_bundle_version`. Future bundle upgrades are deliberate, signed-off actions per Section 3.2.

### 7.5 Failure modes

| Failure | Behaviour |
|---|---|
| Smoke test fails post-sign-off | Promotion blocked; failing rows surfaced; signer re-reviews; sign-off hash invalidates |
| Promotion transaction fails mid-flight | Full rollback; status `ONBOARDING`; staging untouched; ops notified |
| Bundle deprecated mid-onboarding | Session continues on pinned version; new sessions get new bundle |
| Reviewer disputes mapping post-sign-off, pre-promotion | `unsign` reopens; staging hash invalidates; re-resolve; re-sign |

### 7.6 What promotion does NOT do

- Patient migration → Tier-2.
- Opening AR / AP / inventory → Tier-2 (unless facility insists on day-1, opt-in).
- BOM tuning past defaults → optional, Tier-2.

---

## 8. Enriched Word reports per cohort

### 8.1 Why

The current cohort `.docx` files are research-team artefacts. A facility signer (Pharmacist-in-Charge facing 380 drugs, Lab Manager facing 220 tests) needs a document that answers four questions:

1. What is this catalogue?
2. Why does my facility need it?
3. What am I being asked to confirm?
4. What should I challenge?

### 8.2 Required structure

Every cohort `.docx` ships with:

```
§ 0  Executive summary (1 page)
§ 1  Coding Standards & Bodies (already required, preserved)
§ 2  Catalogue scope & taxonomy
§ 3  Per-entity reference (the bulk)
       — canonical name + code(s)
       — 2–4 sentence plain-English explanation
       — clinical / operational context
       — synonyms / brand names / locale variants
       — required co-fields (price, supplier, etc.)
       — cross-cohort links
       — risk-tier flag
       — known gaps / pending verification
§ 4  Cross-cohort dependencies
§ 5  Onboarding workflow for this catalogue
§ 6  Acceptance criteria
§ 7  Open gaps & limitations
§ 8  Source bibliography (preserved)
§ 9  Change log
```

### 8.3 Generation strategy

Reports are auto-generated, not hand-written:

- Markdown corpus + per-entity explainer prose (new research wave per cohort) + cross-cohort dependency map (from `00-cross-cohort-master.md`) + onboarding workflow stubs (from this design).
- Existing `scripts/generate_healthcare_app_clinical_data_outputs.py` extends to render §0–§9.

### 8.4 Per-cohort sizing

| Cohort | Rows | Target pages |
|---|---|---|
| drugs | 488 | ~120 |
| lab-tests | 220 | ~70 |
| imaging | 50 | ~25 |
| procedures | 222 | ~75 |
| consumables | 327 | ~90 |
| conditions | 220 | ~50 |
| standard-forms | 45 | ~30 |
| facilities | 28 | ~25 |
| roles-permissions | 18 | ~25 |
| workflows | 18 | ~30 |
| country-packs | 9 | ~60 |
| billing-tariffs | 74 | ~40 |
| reporting-kpis | 55 | ~50 |
| tenant-blueprints | 6 | ~40 |
| + Wave-3 (7 cohorts) | TBD | TBD |

### 8.5 Per-tenant intake pack subset

Intake packs ship only the entities the blueprint enables — small clinic doesn't get the full 120-page drug document for items it'll never stock.

---

## 9. Tier-2 async completion track

### 9.1 What runs on Tier-2

| Workstream | Why deferred from Tier-1 |
|---|---|
| Patient migration | Volume; fuzzy-dedupe needs human review; back-loadable |
| Opening AR / AP | Reconciliation needs accountant time; new AR starts at zero day-1 |
| Opening inventory | Physical count parallel to day-1 ops |
| Full consumable master | Long tail; expanded over weeks |
| Imaging catalogue | Per-modality + contrast protocols |
| BOM overrides beyond defaults | Tuned from real usage |
| Pathway customisations beyond library | Refined from observed practice |
| Scheme tariff matrices | Insurer negotiations may extend past go-live |
| Historical claim reconciliation | Last-3-months migration |

### 9.2 Same staging, different gate

Tier-2 reuses staging tables and reviewer console. Difference:

- **Tier-1 gate** = block go-live until satisfied.
- **Tier-2 gate** = block specific *features* until satisfied (feature-flag style):
  - No patient migration → legacy-patient lookup shows "not yet migrated."
  - No opening AR → AR aging report shows "from go-live."
  - Imaging contrast BOM missing → that procedure gated.

### 9.3 Async run model

```
onboarding.promote_tier2(session_id, catalogue)
  — same transactional shape as Tier-1
  — single signer (not dual)
  — no smoke tests required
```

Reviewer console keeps tabs visible after go-live; Tier-2 tabs show progress meters.

### 9.4 Brownfield typical timeline

```
Day -21       Pre-kickoff packet sent
Day -14       Facility profile + capability flags submitted
Day -7        Staff roll uploaded
Day  0        Tier-1 catalogues uploaded + reviewed + signed (1–2 days)
Day +1        GO LIVE — new encounters in Medic8
Day +1..+7    Parallel-run week (Medic8 + legacy)
Day +1..+14   Patient migration async
Day +7..+21   Opening AR/AP reconciled
Day +14..+28  Full consumables tail; BOM overrides; tariff matrices
Day +30       Tier-2 closed; legacy decommissioned
```

---

## 10. Open questions, risks, out-of-scope

### 10.1 Open questions for implementation

1. AI provider lock-in — Claude default; budget envelope and rate-limit fallback.
2. OCR provider — Azure Doc Intelligence vs Google Doc AI vs Tesseract.
3. Seed bundle hosting — S3 + signed manifests vs Git tag vs purpose-built service.
4. Reviewer console stack — Laravel reuse vs separate React/Next.
5. Excel template generation library — `openpyxl` vs `phpoffice/phpspreadsheet`.
6. Confidence-threshold tuning — needs ≥3 pilot tenants; conservative defaults until then.
7. Bundle-to-bundle migration UX for existing tenants — out of go-live scope.

### 10.2 Risks knowingly carried

| Risk | Mitigation |
|---|---|
| AI hallucinates drug → patient harm | Risk-tier 100% review for controlled/paeds/vaccine; rationale logging; AI never sets prices |
| Seed bundle drifts from Medic8 schema | Version pinning per tenant; MAJOR bumps required for breaking changes |
| Reviewer fatigue → rubber-stamp | Sample audit on auto-accepted; per-catalogue signer; sign-off hash detects mutation |
| Brownfield file too garbled | Triage queue for low-classification-confidence files |
| AI cost too high to scale | Batched calls; smaller models for classify; cache identical raw_payloads across same-country tenants |
| Re-upload loses reviewer work | Workbook-level independence; partial reviews preserved; mutation banner |
| Tier-2 stalls indefinitely | Per-catalogue progress meters + automated nudges; ops surfaces stalled sessions |

### 10.3 Out of scope

- Patient migration row-level cleansing rules — separate spec.
- Multi-tenant DB isolation — assumed handled.
- Auth / authz flows — assumed handled.
- i18n pipeline internals — already exists; design consumes.
- Facility-staff training & certification.
- Bundle-to-bundle migration tooling — flagged as future.
- Cross-tenant data sharing / benchmarking — privacy-sensitive separate design.
- Pricing economics — business decision, separate doc.

---

## 11. Dependencies on this research project

Before the pipeline can ship, **22 cohorts must be at the enriched-Word-report bar**:

- 14 existing cohorts (need §0–§9 enrichment + per-entity explainer prose)
- 7 new Wave-3 cohorts (vaccines, BOMs, drug-interactions, allergens, paediatric-dosing, UCUM, holiday-calendars)
- 1 country-packs extension (TZ/RW/CD/NG full packs)
- 1 confirmation pass (specimen/container coverage in lab-tests)

This is the long pole of the implementation plan — Word report generation depends on cohort completion, template generation depends on Word reports, pipeline shipping depends on templates.

---

## 12. Next steps

1. **Implementation plan** — produced via `superpowers:writing-plans` skill, sequencing: (a) Wave-3 research cohorts, (b) enriched Word reports for all 22 cohorts, (c) seed bundle publication infrastructure, (d) template generator, (e) ingest pipelines (greenfield + brownfield), (f) reviewer console, (g) acceptance gate & promotion, (h) Tier-2 async track, (i) pilot-tenant onboarding.
2. **Pilot tenant selection** — at least 3 (one greenfield small clinic, one brownfield mid hospital, one specialty/standalone) to tune confidence thresholds.
3. **Bundle versioning + seed-loader contract** with Medic8 dev team — agree the manifest schema and signature scheme before the loader is built.

---

*End of design.*
