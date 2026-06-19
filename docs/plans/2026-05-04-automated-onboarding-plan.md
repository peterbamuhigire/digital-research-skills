# Automated Healthcare-Facility Onboarding — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build the seed-corpus and Word-report infrastructure (Phase A, this repo) and hand off the production pipeline contracts (Phase B) so Medic8 can stand up new healthcare facilities in days, not weeks.

**Architecture:** Two-track convergent pipeline — rigid Excel templates for greenfield, AI alignment for brownfield, both into shared staging → risk-tiered reviewer console → Tier-1 promotion + Tier-2 async. See `docs/plans/2026-05-04-automated-onboarding-design.md`.

**Tech Stack (this repo, Phase A):** Python 3.11+, `python-docx`, `openpyxl`, existing `scripts/generate_healthcare_app_clinical_data_outputs.py`, sub-agent dispatching via Claude Code `Agent` tool, evidence-discipline skills under `skills/source-evaluation/`.

**Tech Stack (Medic8, Phase B — assumed):** Laravel/PHP backend, Postgres or MySQL, Redis queue, S3-compatible object store; reviewer console TBD (Laravel reuse vs separate React/Next).

---

## Phase boundary

| Phase | Repo | Granularity | Owner |
|---|---|---|---|
| **A — Research / corpus / bundle** | this repo (`digital-research-engine`) | Bite-sized tasks below | Peter + Claude |
| **B — Medic8 production pipeline** | Medic8 repo (separate) | Contract specs (§B1–§B7) | Medic8 dev team |

---

## Phase A — Research-engine work (this repo)

### Section A1 — Wave-3 research cohorts (7 new + 1 extension + 1 confirmation)

Goal: produce `(catalogue.docx + catalogue.xlsx + wave1-data.md + wave1-findings.md)` for each missing catalogue.

The cohorts each follow the established pattern from `projects/healthcare-app-clinical-data/`. Per-cohort work is one sub-agent dispatch with the verbatim hard-constraint clause from `skills/source-evaluation/references/evidence-discipline.md`.

#### Task A1.1 — Scaffold the 7 new cohort folders

**Files to create:**
- `projects/healthcare-app-clinical-data/vaccines/{README.md, CLAUDE.md, research/, analysis/, opportunities/}`
- `projects/healthcare-app-clinical-data/boms/{...}`
- `projects/healthcare-app-clinical-data/drug-interactions/{...}`
- `projects/healthcare-app-clinical-data/allergens/{...}`
- `projects/healthcare-app-clinical-data/paediatric-dosing/{...}`
- `projects/healthcare-app-clinical-data/ucum/{...}`
- `projects/healthcare-app-clinical-data/holiday-calendars/{...}`

**Step 1:** Use the existing `consumables/` cohort as the structural template. Each new cohort `README.md` carries: scope, T1/T2/T3 source list, hard exclusions, output shape (per `CLAUDE.md` of the parent project).

**Step 2:** Update `projects/healthcare-app-clinical-data/PROJECT-STATUS.md` to add a Wave-3 phase tracker row per new cohort.

**Step 3:** Commit.

```bash
git add projects/healthcare-app-clinical-data/
git commit -m "Wave-3 scaffold: 7 new cohort folders + status tracker"
```

---

#### Task A1.2 — Vaccines cohort (Wave-3 dispatch)

**Cohort:** `projects/healthcare-app-clinical-data/vaccines/`

**Sub-agent brief contents (mandatory):**
- Goal: enumerate every WHO-prequalified vaccine relevant to UG/KE/TZ EPI + private/travel + occupational stocks. Cover ATC J07 + WHO PQS lot semantics + AEFI Brighton classification.
- Scope: WHO IVB, GAVI co-financed schedule, UG UNEPI, KE KEPI, TZ IVD; private/travel additions (yellow fever, typhoid, cholera, MenACWY, HepA, varicella, MMR, zoster).
- Out of scope: cardiothoracic / neuro / transplant (per project exclusion).
- Sources to mine: WHO Vaccine Position Papers, WHO PQS catalogue, GAVI procurement catalogue, country MoH EPI guidelines.
- Deliverable shape: `wave1-data.md` (markdown table), `wave1-findings.md` (narrative + bibliography).
- **Verbatim hard-constraint clause** from `skills/source-evaluation/references/evidence-discipline.md`.
- Cumulative discipline clauses from memory `feedback_research_discipline_clauses.md`.

**Step 1:** Dispatch sub-agent (`subagent_type: content-marketing:search-specialist`, `run_in_background: true`).

**Step 2:** On completion, read structured `<result>` block. Verify ≥80% T1 coverage; spot-check 5 antigens against WHO PQS.

**Step 3:** Apply any patches per `EVIDENCE-AUDIT.md` discipline (Wikipedia stripping, regulator conflation).

**Step 4:** Commit cohort outputs.

```bash
git add projects/healthcare-app-clinical-data/vaccines/
git commit -m "Wave-3 vaccines cohort: Wave-1 data + findings"
```

---

#### Tasks A1.3 — A1.8 — Repeat A1.2 pattern for remaining cohorts

Same pattern as A1.2 with these per-cohort scope notes:

**A1.3 — BOMs.** Default kit composition per service / lab test / imaging / vaccine / dressing / surgical pack. Sources: WHO PEN protocols, IMCI charts, country STG, manufacturer-published consumable kits. Output is intentionally derivative — the cohort is opinionated on what *should* be in each kit.

**A1.4 — Drug-drug interactions.** Source: open DDInter dataset; supplement with WHO EML class-level contraindications (warfarin × azoles, MAOI × SSRI, etc.). Minimum coverage: 5000 pairs across EML classes 1.

**A1.5 — Allergens.** Source: RxNorm allergen ingredients + SNOMED CT food/environmental allergens. Required: penicillin class, sulfa class, NSAID class, peanut, egg, latex, iodine, tetracycline class.

**A1.6 — Paediatric dosing.** Source: WHO Model Formulary for Children 2010 + WHO EMLc 2023. Per-drug mg/kg dose, daily max, weight bands, age cut-offs.

**A1.7 — UCUM.** Source: Regenstrief UCUM essence list. Cover all UOMs referenced in lab-tests, drugs, vaccines, BOMs cohorts.

**A1.8 — Holiday calendars.** Per-country (UG/KE/TZ/RW/CD/NG) public holidays + per-religion (Christian Easter/Christmas, Muslim Eid al-Fitr/Eid al-Adha, plus regionally significant local holidays). 5-year forward window.

Each task ends with the same commit pattern.

---

#### Task A1.9 — Country-pack extension (TZ/RW/CD/NG full packs)

**Cohort:** `projects/healthcare-app-clinical-data/country-packs/` (extend, do not overwrite)

**Step 1:** Dispatch one sub-agent per country (4 parallel `Agent` calls in one message), brief includes country profile fields per design doc §3.3 (currency, tax, HMIS, regulator, drug list, insurer baseline, mobile money, languages, public-health programmes).

**Step 2:** Append findings under `# Pass 2 — Country-pack full extension` headers per project file-write conventions.

**Step 3:** Update PROJECT-STATUS.md country-packs row from "9 rows (UG+KE full; 7 stubbed)" to "13 rows (UG+KE+TZ+RW+CD+NG full; 3 stubbed)".

**Step 4:** Commit.

---

#### Task A1.10 — Specimen/container confirmation pass

**Cohort:** `projects/healthcare-app-clinical-data/lab-tests/`

**Step 1:** Read `lab-tests/research/wave1-data.md`. Verify each row carries `specimen_type`, `container`, `volume_min` per the PHII-19 enforcement noted in `PROJECT-STATUS.md` Phase 0 addendum.

**Step 2:** If gaps exist, dispatch one targeted sub-agent to fill them with LOINC system-axis + SNOMED CT specimen concepts.

**Step 3:** Otherwise, mark confirmation in `EVIDENCE-AUDIT.md` and proceed.

---

### Section A2 — Enriched Word reports (22 cohorts)

Goal: extend every cohort's `.docx` to the §0–§9 structure from design doc §8.

#### Task A2.1 — Extend the report-generation script

**File to modify:** `scripts/generate_healthcare_app_clinical_data_outputs.py`

**Step 1:** Read the current script to understand the existing `.docx` rendering pipeline.

**Step 2:** Write a failing pytest that asserts the new structure: every cohort `.docx` contains §0 Executive summary, §3 Per-entity reference, §4 Cross-cohort dependencies, §5 Onboarding workflow, §6 Acceptance criteria, §7 Open gaps, §9 Change log. Test against a fixture with 3 entities.

```python
# tests/test_enriched_docx_structure.py
def test_enriched_report_has_required_sections():
    doc = generate_enriched_docx(fixture_cohort)
    headings = [p.text for p in doc.paragraphs if p.style.name.startswith("Heading")]
    for required in ["Executive summary", "Per-entity reference",
                     "Cross-cohort dependencies", "Onboarding workflow",
                     "Acceptance criteria", "Open gaps", "Change log"]:
        assert any(required in h for h in headings), f"Missing: {required}"
```

**Step 3:** Run test, confirm fail.

**Step 4:** Implement minimal changes to script to render the §0–§9 skeleton (sections empty for now beyond §1 §2 §8 which already exist).

**Step 5:** Run test, confirm pass.

**Step 6:** Commit.

---

#### Task A2.2 — Per-entity explainer prose generation

**Files:**
- Create: `scripts/lib/explainer_prose.py`
- Test: `tests/test_explainer_prose.py`

**Step 1:** Write failing test: given a row from `drugs/wave1-data.md`, generate a 2–4 sentence plain-English explanation containing the drug's clinical context, common synonyms, and risk-tier flag.

**Step 2:** Run test, confirm fail.

**Step 3:** Implement using Claude API (Sonnet 4.6) with prompt cache. Prompt template includes evidence-discipline clauses; output is constrained 2–4 sentences citing only the row's sourced data.

**Step 4:** Test on 5 fixture rows; manually inspect for hallucination. Iterate prompt until no fabricated facts.

**Step 5:** Add per-row caching keyed by `(cohort, entity_code, bundle_version)` to `_cache/explainer/` so re-generations don't re-bill the API.

**Step 6:** Commit.

---

#### Task A2.3 — Cross-cohort dependency graph extractor

**Files:**
- Create: `scripts/lib/cross_cohort_links.py`
- Test: `tests/test_cross_cohort_links.py`

**Step 1:** Failing test: extract from existing `00-cross-cohort-master.md` the per-cohort inbound + outbound link sets.

**Step 2:** Implement parser; output per-cohort JSON consumed by §4 of the report template.

**Step 3:** Commit.

---

#### Task A2.4 — Onboarding workflow stub renderer

**Files:**
- Create: `scripts/lib/onboarding_workflow_stub.py`

**Step 1:** Per-cohort, render §5 "Onboarding workflow for this catalogue" from a static spec keyed on cohort name. The spec lives in `_context/onboarding-workflow-specs.md` and mirrors design doc §3.4 (workbook name, pre-fill scope, AI/dropdown/free-text rules, signer-must-verify fields).

**Step 2:** Write the spec file once for all 22 cohorts.

**Step 3:** Render and verify with a smoke test.

**Step 4:** Commit.

---

#### Task A2.5 — Run enriched generation across all 22 cohorts

**Step 1:** Run `python scripts/generate_healthcare_app_clinical_data_outputs.py --enriched --cohort=all`.

**Step 2:** Spot-check 3 cohort .docx files for structural correctness + 5 entities each for explainer-prose factuality.

**Step 3:** Mark any factual issues in `EVIDENCE-AUDIT.md`; iterate prompts where needed.

**Step 4:** Commit outputs to `05-output/clinical-data-deliverables/` + `export/`.

---

### Section A3 — Seed bundle publication infrastructure

Goal: turn the cohort outputs into a versioned, signed, manifest-bearing zip the Medic8 seed-loader can consume.

#### Task A3.1 — Manifest schema & writer

**Files:**
- Create: `scripts/lib/seed_bundle.py`
- Test: `tests/test_seed_bundle_manifest.py`

**Step 1:** Failing test: build a manifest from a fixture cohort directory; assert `version` (semver), `cohorts[].name`, `cohorts[].row_count`, `cohorts[].sha256` per file.

**Step 2:** Implement.

**Step 3:** Commit.

---

#### Task A3.2 — Bundle assembler

**Step 1:** Failing test: assemble fixture cohorts into `seed-bundle-vX.Y.Z.zip` with manifest at root.

**Step 2:** Implement (zipfile std-lib).

**Step 3:** Commit.

---

#### Task A3.3 — Signing

**Step 1:** Detached PGP signature over `manifest.json` using a project signing key stored outside the repo. Document key generation + storage in `docs/plans/2026-05-04-automated-onboarding-plan.md` only as a procedure (not in this plan body — too long).

**Step 2:** Implement signing step; test with throwaway key.

**Step 3:** Commit. Document key custody decision separately with Peter.

---

#### Task A3.4 — Bundle verification CLI

**Step 1:** `python -m engine verify-bundle <path-to-zip>` checks signature + manifest hashes + cohort row-counts.

**Step 2:** Failing test then implementation.

**Step 3:** Commit.

---

#### Task A3.5 — Publish v1.0.0

**Step 1:** Run full pipeline: `python -m engine assemble-bundle --version 1.0.0 --output export/seed-bundle-v1.0.0.zip`.

**Step 2:** Verify with `python -m engine verify-bundle export/seed-bundle-v1.0.0.zip`.

**Step 3:** Tag in git: `git tag seed-bundle-v1.0.0`.

**Step 4:** Hand zip + signature + public key to Medic8 dev team.

---

## Phase B — Medic8 production pipeline (separate repo)

These are **contracts**, not bite-sized tasks. The Medic8 team executes against these specs in their codebase, against schema/files I haven't seen.

### §B1 — Seed loader

**Inputs:** signed `seed-bundle-vX.Y.Z.zip`, public key.

**Behaviour:**
- Verify signature; reject on mismatch.
- Verify manifest hashes; reject on mismatch.
- Load each cohort `.xlsx` into `tbl_<cohort>_global` keyed by canonical seed ID.
- Idempotent: re-running with same bundle is a no-op.
- Bundle version recorded in `tbl_seed_bundle_versions`.

**Acceptance:**
- All 22 cohorts loaded.
- Re-load same bundle: zero rows changed.
- Load deliberately-corrupted bundle: rejected with audit log.

---

### §B2 — Per-tenant template generator

**Inputs:** facility country, tenant blueprint, capability flags, locale.

**Output:** `onboarding-pack-<facility-id>-v<bundle-version>.zip` per design §3.4.

**Behaviour:**
- Pulls country-scoped seed slice for dropdowns.
- Fingerprints each workbook with `bundle_version + facility_id + generated_at`.
- Renders intake-guide PDF from per-cohort `.docx` subset (only entities the blueprint enables).

**Acceptance:**
- Pack generated for a small clinic in <30s.
- Pack opens cleanly in MS Excel + LibreOffice + Google Sheets.
- Dropdowns enforce data-validation; free-text rejected in coded cells.

---

### §B3 — Greenfield ingest

**Behaviour per design §4.**

**Acceptance:**
- Accepts a fingerprinted, schema-valid pack.
- Rejects schema-mismatched workbook with row/col diff.
- Rejects fingerprint-missing or stale bundle version.
- Persists rows to `tbl_staging_<catalogue>` with correct `source_kind`.

---

### §B4 — Brownfield AI alignment pipeline

**Behaviour per design §5.**

**Acceptance:**
- Stage 1 handles all 6 documented input kinds.
- Stage 4 produces `mapped_seed_id`, `confidence`, `ai_rationale`, `alternates_considered` per row.
- Stage 5 risk-tier from seed metadata, not AI confidence.
- AI never sets prices.
- Mid-size hospital alignment completes in <30 minutes wall-clock.

---

### §B5 — Reviewer console

**Behaviour per design §6.**

**Acceptance:**
- 4 queues per catalogue tab.
- Sample-audit on auto-accepted; reviewer cannot cherry-pick the sample.
- Sign-off hash detects post-sign mutation.
- Re-upload preserves reviewed-and-unchanged rows.
- Audit log captures every reviewer action with before/after JSON.

---

### §B6 — Acceptance gate & promotion

**Behaviour per design §7.**

**Acceptance:**
- Gate-aggregate view returns green only when all sub-checks green.
- 6 smoke tests scripted against staging snapshots, not production.
- Promotion is single transactional; rollback on any failure.
- Bundle version pinned per tenant.
- Emergency bypass triggers P1 alert.

---

### §B7 — Tier-2 async track

**Behaviour per design §9.**

**Acceptance:**
- Tier-2 catalogues promotable independently post-go-live.
- Single-signer (not dual).
- Feature flags read at request time so missing Tier-2 catalogues gate corresponding features.

---

## Sequencing

```
A1 Wave-3 cohorts ──┐
                    ├──► A2 Enriched reports ──► A3 Bundle publish v1.0.0
A1.10 confirmation ─┘                                        │
                                                             ▼
                                                    Hand-off to Medic8 team
                                                             │
                                                             ▼
                                B1 seed loader ──► B2 template gen
                                                             │
                                                B3 greenfield ingest
                                                B4 brownfield ingest    } parallel
                                                             │
                                                             ▼
                                                    B5 reviewer console
                                                             │
                                                             ▼
                                                    B6 gate + promotion
                                                             │
                                                             ▼
                                                    B7 Tier-2 async
                                                             │
                                                             ▼
                                              Pilot tenant onboarding × 3
                                              (greenfield + mid + standalone)
                                                             │
                                                             ▼
                                              Confidence threshold tuning
                                                             │
                                                             ▼
                                                       GA rollout
```

---

## Definition of done

**Phase A (this repo):**
- [ ] 7 new + 1 extended + 1 confirmed cohort all at the standard "Wave-1 complete + patches applied" bar.
- [ ] All 22 cohorts ship `.docx` with §0–§9 enriched structure + `.xlsx` seed.
- [ ] `seed-bundle-v1.0.0.zip` published, signed, verifiable.
- [ ] Cross-cohort master `.docx` updated with Wave-3 sections.
- [ ] PROJECT-STATUS.md updated through Wave-3.
- [ ] EVIDENCE-AUDIT.md captures all discipline patches.

**Phase B (Medic8 repo):**
- [ ] All 7 acceptance specs (B1–B7) green in their respective test suites.
- [ ] 3 pilot tenants successfully onboarded end-to-end (one greenfield clinic, one brownfield mid-hospital, one standalone lab/pharmacy).
- [ ] Confidence thresholds tuned per catalogue from pilot metrics.
- [ ] Rollback runbook exercised at least once in staging.

---

*End of plan.*
