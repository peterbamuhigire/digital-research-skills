---
project: upf-cris
title: Criminal Records Information System (CRIS) for Uganda Police Force — Engagement Design
date: 2026-04-26
last_updated: 2026-04-27
status: research-complete; awaiting synthesis + Doc 1 / Doc 2 assembly
deliverables:
  - Document 1 — RFP-grade System Design Document (~270–320 pp; revised down from 280–340 after §10 collapse following 2026-04-26 scope change)
  - Document 2 — Vendor proposal under C-model: Build (24 mo) + 5-yr Managed Services (~95–125 pp)
engagement_type: real (vendor preparing bid to Uganda Police Force / Ministry of Internal Affairs)
notes:
  - Project workspace lives at `projects/upf-cris/` and is git-ignored — local-only per operator preference. This design doc and the engine itself are pushed; the project corpus stays on the operator's machine.
---

# UPF CRIS — Engagement Design

> **Reading order:** §1–§11 are the original engagement design as agreed at project kick-off (2026-04-26). §12 (Engagement-state addendum, 2026-04-27) records what actually happened across Waves 1–4, the mid-engagement scope change, and the resulting deltas to the deliverable shape. If you only have time for one section, read §12.

## 1. Locked decisions (from brainstorm Q1–Q9)

| # | Decision | Choice | Implication |
|---|---|---|---|
| Q1 | Deliverable genre | **A — System Design Document spine, research as supporting evidence** | Doc 1 reads as SDD, not feasibility study |
| Q2 | Engagement reality | **A — Real engagement, full evidence rigor** | Real UPF org units, real DPP Act §, real UGX bands; gaps flagged not filled |
| Q3 | Buyer / voice | **B — Vendor / SI preparing a bid** | Persuasive voice in Doc 2; advocates a specific stack; benchmarks frame "why our approach" |
| Q4 | Sensitive-feature postures | Predictive policing **OUT**; live AFR **DEFERRED**; intelligence-agency integration **DEFERRED** (gateway exposed); commercial BG-check service **IN** | Defensive scope; one rationale paragraph per feature in Doc 1 §9 |
| Q5 | Current-state research approach | **B + C straw-man** — research the public record, propose Uganda-context defaults, mark every claim with source/tier/verification | Faster than waiting for UPF disclosure; honest about gaps |
| Q6 | Phase 1 MVP shape | **B — Operational core + revenue** — Modules 1, 2, 3, 5 + DEMS-lite (4) + BG-check (9). DEMS full / ECCMIS deep / iOS officer / analytics → Phase 2. AFR 1:1 / intelligence gateway / Interpol I-24/7 → Phase 3 (legal-basis gated) | 24-month build |
| Q7 | Document size envelope | **Hybrid B+C** for Doc 1 | ~280–340 pp; full FRs, NFRs, ADRs, RTM, M&E, pilot plan, benchmarking annex |
| Q8 | Commercial model (Doc 2) | **C — Build 24 mo + 5-yr Managed Services** | BG-check revenue accrues to Treasury (not vendor); cleaner conventional procurement; build CAPEX + annual MS fee |
| Q9 | Citizen reporting app | **B + ii** — Phase 1b (months 19–30); tiered auth (NIN-authenticated formal complaints, OTP for minor reports, fully anonymous for tips) | iOS moves into Phase 1 alongside Android; new public-facing trust zone in architecture; expanded threat model |

## 2. Project structure

- Project ID: `upf-cris`
- Path: `projects/upf-cris/`
- Kernel-managed (per `CLAUDE.md` workflow)

### Cohorts (7)

| # | Cohort | Drives Doc 1 sections | Drives Doc 2 sections |
|---|---|---|---|
| 1 | `uganda-context` | §2, §11 | §2, §13 |
| 2 | `functional-requirements` (split 2A: Modules 1–5 + citizen app · 2B: Modules 6–9) | §4, §8 | §3 |
| 3 | `architecture-and-tech` | §5–7, §11 | §4 |
| 4 | `security-legal-governance` | §9 | §13 |
| 5 | `benchmarks` | §17 | (referenced in §3, §4) |
| 6 | `bg-check-service` | §10 | (revenue placeholders only) |
| 7 | `commercial-delivery` (Doc 2 specific) | §12, §13, §14, §15, §16 | §5–12, §14, §15 |

### Wave plan

- **Wave 1** (parallel, foundation): cohorts 1, 4, 5
- **Wave 2** (parallel, after W1): cohorts 2A, 2B, 3 (briefed with W1 findings)
- **Wave 3** (parallel, after W2): cohorts 6, 7
- **Wave 4** (targeted, after EVIDENCE-AUDIT review): gap-fill only

After Wave 4: cross-cohort synthesis → research-report-builder → Doc 1, then Doc 2.

## 3. Document 1 outline (RFP-grade SDD)

Title: **"Criminal Records Information System (CRIS) for the Uganda Police Force — System Design Document"**

| § | Chapter | pp | Source cohort |
|---|---|---|---|
| 1 | Executive Summary | 6–8 | synthesis |
| 2 | Uganda Context & Drivers | 14–18 | 1 |
| 3 | Vision, Objectives, Success Criteria | 4–6 | synthesis |
| 4 | Functional Requirements (9 modules + citizen app) | 80–100 | 2A + 2B |
| 5 | Non-Functional Requirements | 12–16 | 3 + 4 |
| 6 | Reference Architecture (C4: Context / Container / Component) | 24–30 | 3 |
| 7 | Data Model & Information Architecture | 18–24 | 2 + 4 |
| 8 | Operational Workflows (BPMN) | 18–22 | 2 + 4 |
| 9 | Security, Privacy & Legal Framework | 28–34 | 4 |
| 10 | Background-Check Service Design | 16–20 | 6 |
| 11 | Integration & Interoperability | 14–18 | 1 + 3 |
| 12 | Implementation Roadmap (Phase 1 / 1b / 2 / 3) | 16–20 | 3 + 7 |
| 13 | Cost Model (UGX bands) | 10–14 | 7 |
| 14 | Risk Register & Mitigations | 8–10 | all |
| 15 | M&E Framework | 6–8 | 1 + 4 |
| 16 | Pilot Test Plan | 8–10 | 7 |
| 17 | Benchmarking Annex | 22–28 | 5 |
| 18 | Architecture Decision Records (14 ADRs) | 14–18 | 3 |
| 19 | Requirements Traceability Matrix | 8–12 | 2 |
| 20 | Glossary, Acronyms, Sources, EVIDENCE-AUDIT | 10–14 | all |

**Total: ~290–360 pp, ~110–135k words.**

Voice: third-person, advisory-neutral. Every claim about Uganda law / UPF structure / existing systems carries `[source-id, tier, accessed-date]`. Every figure carries source or `indicative — to be validated at inception`.

## 4. Document 2 outline (Vendor proposal — C-model)

Title: **"Proposal to Design, Develop, Implement, Maintain and Operate the Criminal Records Information System for the Uganda Police Force"**

| § | Chapter | pp |
|---|---|---|
| 1 | Cover Letter & Executive Summary | 4 |
| 2 | Understanding of UPF's Need | 6–8 |
| 3 | Proposed Solution Overview (refs Doc 1) | 8–10 |
| 4 | Proposed Technology Stack & Justification | 8–10 |
| 5 | Delivery Approach — Build Phase (24 mo + Phase 1b) | 10–12 |
| 6 | Managed Services Approach — 5-yr Operate (60 mo) | 10–14 |
| 7 | Implementation Plan & Milestones | 6–8 |
| 8 | Team & Key Personnel (placeholder structure) | 8–10 |
| 9 | Past Performance & Capability (placeholder) | 4–6 |
| 10 | Pricing Schedule (UGX, PPDA-format BoQ) | 8–10 |
| 11 | Commercial Terms (IP, warranty, exit, LDs) | 4–6 |
| 12 | Risk Allocation Matrix | 4–6 |
| 13 | Compliance Statement (DPP Act, PPDA, NITA-U IF, AML for BG-check) | 4–6 |
| 14 | Quality Assurance & Testing Plan | 4 |
| 15 | Knowledge Transfer & Capacity Building | 4–6 |
| 16 | Annexes | 8–12 |

**Total: ~100–130 pp.**

Voice: persuasive vendor. Cross-references Doc 1 for technical depth.

## 5. Architecture Decision Records (locked)

| ADR | Decision | Driver |
|---|---|---|
| ADR-01 | Web frontend: Next.js 15 (App Router) + TypeScript + Tailwind | Server Components reduce mobile-network payload |
| ADR-02 | Mobile officer: Android (Kotlin + Jetpack Compose + Room) Phase 1; iOS (Swift + SwiftData) Phase 2. **Mobile citizen: both Android and iOS in Phase 1b** | Field-officer device base is Android-dominant; citizen app must reach both platforms |
| ADR-03 | Backend: modular monolith (TypeScript / NestJS) Phase 1; selective service extraction Phase 2 | Lower ops burden during early operate phase |
| ADR-04 | Primary DB: PostgreSQL 16 + PostGIS | Sovereign, no licensing, mature; PostGIS for geo-tagging |
| ADR-05 | Object storage (evidence): S3-compatible MinIO on-prem at NITA-U NDC; cold-DR optional sovereign cloud | Police evidence sovereignty |
| ADR-06 | Search: OpenSearch | Cross-entity search core to Modules 3 and 7 |
| ADR-07 | Identity / SSO: Keycloak (OIDC) + custom RBAC service for ABAC overlay | Open-source, federation-ready |
| ADR-08 | Biometric matching: integrate NIST-EBTS-compliant ABIS partner; do not build | Building ABIS is multi-year R&D |
| ADR-09 | Hosting: NITA-U National Data Centre primary + NITA-U DR site; no public-cloud production in Phase 1 | Sovereignty; PPDA precedent |
| ADR-10 | Integration: event-driven (Kafka) inter-module + REST/OpenAPI external (NIRA, ECCMIS, DCIC) | Decouples modules; standard for NITA-U IF |
| ADR-11 | Audit log: append-only with hash-chained Merkle entries | Evidence Act admissibility for chain-of-custody |
| ADR-12 | Mobile offline: local SQLite (Room/SwiftData) + outbound sync queue + conflict resolution | District connectivity reality |
| ADR-13 | AuthN/AuthZ: OIDC + RBAC + ABAC; step-up biometric on device for restricted-class records | Juvenile / witness / intelligence-marked record protection per DPP Act |
| ADR-14 | **Citizen app: separate app, separate trust zone, separate API gateway (DMZ + WAF + rate-limit). Tiered auth: NIN-authenticated formal complaints, phone-OTP for minor reports, fully anonymous tips. Submissions land in triage queue, not direct to case DB.** | Public attack surface; abuse mitigation; legal posture differs from officer flow |

## 6. Citizen-app expansion (Phase 1b, months 19–30)

- Submission types: crime incident, GBV (sensitive-handling flow), traffic, missing person, anonymous tip, panic/duress
- Media: photo / video / audio with hash-on-upload (ties to ADR-11)
- Offline buffering on device for network-poor areas
- Multilingual UI (English, Luganda, Swahili minimum; Runyankole / Acholi / Lugbara Phase 2)
- Accessibility (WCAG 2.2 AA, low-literacy iconographic mode)
- Duplicate / mass-event handling
- False-reporting deterrent: Penal Code Act Cap 120 §117 surfaced in T&Cs
- Anonymous-tip legal regime: separate from authenticated complaints; no callback, no status updates
- Witness/complainant protection: precise-location opt-out
- DDoS / false-flood mitigation: rate-limiting, behavioural CAPTCHA, NIN-binding for repeat reporters
- Citizen-supplied media admissibility: hash + provenance metadata at submission (Evidence Act)
- Push-notification leakage: sensitive case status hidden on lock screen

Cost impact (indicative, to be replaced with sourced estimates in Doc 1 §13): **+15–25% on build CAPEX, +8–12% on annual MS**.

## 7. Scope exclusions (must appear in every sub-agent brief)

1. **Predictive policing / hotspot AI** — OUT. Replace with descriptive crime-mapping dashboards.
2. **Live automated facial-recognition matching** — DEFERRED to Phase 3 behind a legal-basis gate. 1:1 mugshot lookup IN.
3. **Intelligence-agency data integration** (ISO, CMI, ESO data exchange) — DEFERRED. Architecture exposes a controlled gateway only.

If any sub-agent returns content violating these exclusions, strike it and log in `EVIDENCE-AUDIT.md`.

## 8. Evidence discipline (non-negotiable)

- Verbatim hard-constraint clause from `skills/source-evaluation/references/evidence-discipline.md` MUST appear in every sub-agent prompt.
- Every claim → `{source, tier, verification, confidence, accessed}`.
- Tier-5 claims triangulated against ≥2 tier-1 to tier-3 sources.
- No URL ships without archive snapshot.
- Spot-check 10% of stats, 5 quotes, all court cases / statute citations before merging.

## 9. Timeline

| Day | Activity | Output |
|---|---|---|
| 0 | Design doc + kernel scaffold + commit | `docs/plans/`, `projects/upf-cris/` |
| 0–1 | Wave 1 dispatched (cohorts 1, 4, 5) | Foundation research |
| 1–2 | Wave 1 verified; Wave 2 dispatched (2A, 2B, 3) | FRs, architecture |
| 2–3 | Wave 2 verified; Wave 3 dispatched (6, 7) | BG-check + commercial |
| 3 | EVIDENCE-AUDIT review → Wave 4 gap-fill | Closed gaps |
| 3–4 | Cross-cohort synthesis | `synthesis/` |
| 4–5 | Doc 1 assembled | `report-v1-2026-04-XX.docx` |
| 5 | Doc 2 assembled | `proposal-v1-2026-04-XX.docx` |
| 5+ | User review → revisions → v2 | Final pair |

Status check after each wave: one paragraph + EVIDENCE-AUDIT delta. No raw transcripts.

## 10. Open items / parking lot

These items defer to Wave 1 findings — flagged for explicit verification:

- Status of UPF e-Police / EPS portal in 2026 (operational, dormant, or replaced)
- Current SafeCity FR platform integration boundaries and data-sharing agreements
- ECCMIS API maturity & DPP system status
- NIRA verification gateway commercial terms for police use
- NITA-U NDC capacity & current police hosting footprint
- Existing UPF Interpol Certificate of Good Conduct workflow (basis for BG-check service design)
- 2026 UPF org structure (any changes since Police Act amendments)
- Currently in force: Computer Misuse Act amendment 2022, Anti-Money-Laundering Act, Anti-Terrorism Act updates relevant to BG-check disclosures

## 11. Next step

Awaiting user "go" before dispatching Wave 1.

---

## 12. Engagement-state addendum — 2026-04-27

This section records what actually happened across Waves 1–4 and what changed from the original §1–§11 plan. It's the most up-to-date picture of the engagement and supersedes any conflicting detail above.

### 12.1 Mid-engagement scope change — commercial BG-check removed

On 2026-04-26 (mid-Wave-3 dispatch), the user removed the **commercial criminal background-check service** from CRIS scope. The exclusions and substitutions are recorded verbatim in `projects/upf-cris/_context/exclusions.md` (local-only). Summary:

- **OUT:** Commercial BG-check tiers 1–4 to external paying requesters (employers, banks, NGOs, government-as-customer); KYC-of-requesters under AML Act 2013 in this context; statutory-instrument workstream for commercial disclosure; Doc 2 BG-check revenue projection; Tier-4 barred-list / Safeguarding-Vulnerable-Groups-Act dependency.
- **IN (replacing):** **Internal Subject Report** — officer-facing, RBAC + ABAC + purpose-bound + audit-logged report on an individual, drawn from the Records Repository + Persons + Outcomes modules. Two tiers (Tier S Standard, Tier R Restricted) with 7-scheme Purpose Token; Tier R requires named-supervisor authorisation reference + 100% quarterly Internal-Affairs review.
- **PRESERVED:** **UPF Certificate of Good Conduct** — existing citizen self-request workflow rolled into CRIS as a built-in. UPF retains all fee revenue. No commercial expansion, no employer requests, no third-party paid disclosure. 5-day SLA preserved as M&E indicator. Recommended cutover: full replacement at Phase 1 with a 26-week dual-validity verification window for citizens holding valid legacy certificates.

**Cohort 6 renamed `bg-check-service` → `subject-report-service`.** Two FR-2B files (`04-module-bg-check-service.md`, `07-bg-check-statutory-workstream.md`) were tagged SUPERSEDED at the scope change and moved to `_archive/` in Wave 4 so synthesis tooling cannot accidentally pick them up.

### 12.2 Locked-decision deltas (vs §1)

| # | Original choice (§1) | Final state (post-scope-change) |
|---|---|---|
| Q4 | Commercial BG-check service **IN** | **OUT.** Internal Subject Report IN. Citizen Cert of Good Conduct preserved. |
| Q6 | Phase 1 MVP includes BG-check (9) | Phase 1 MVP = Modules 1, 2, 3, 5 + DEMS-lite (4) + **Internal Subject Report + citizen-cert preservation** (replacing Module 9 commercial). |
| Q8 | "BG-check revenue accrues to Treasury" | No commercial BG-check revenue at all. UPF retains existing Cert-of-Good-Conduct fee revenue (preserved, not expanded). Vendor pricing is **Build CAPEX + 5-yr OPEX, fully Treasury-funded, no offsetting revenue line.** Vendor value-prop reframes from "self-funding" to **operational efficiency + judicial throughput + record-integrity assurance + DPP Act 2019 compliance + citizen-cert continuity-of-service**. |
| Q1, Q2, Q3, Q5, Q7, Q9 | unchanged | unchanged |

### 12.3 Document outline deltas (vs §3, §4)

**Doc 1:** §10 collapses from the originally planned 16–20 pages to **8–12 pages** (Internal Subject Report design + Citizen Cert preservation; no commercial-tier design or statutory-instrument workstream). Total Doc 1 length revised to **~270–320 pages** (from 280–340).

**Doc 2:** §10 (Pricing) carries no commercial BG-check revenue line. §13 (Compliance) drops the AML-KYC-of-BG-check-requesters chapter. §3 (Solution Overview) replaces the BG-check pitch with the operational-efficiency + record-integrity narrative. Total Doc 2 length unchanged at ~95–125 pages.

### 12.4 ADR additions (vs §5)

The architecture cohort (Wave 2) added **10 PROPOSED ADRs** (ADR-15 through ADR-24) to the 14 LOCKED ADRs originally agreed:

| ADR | Topic |
|---|---|
| ADR-15 | Backup architecture (3-2-1 + air-gap + quarterly escrow envelope to PDPO and Auditor-General) |
| ADR-16 | Observability stack (OpenTelemetry-based) |
| ADR-17 | Secrets + HSM (FIPS 140-2 L3 sovereign availability is a flagged gap) |
| ADR-18 | Message queue choice (Kafka vs Redpanda) |
| ADR-19 | Phase-2 transcoding pipeline for full DEMS |
| ADR-20 | Multi-vendor / data-portability mandate (avoids the SAPS / UK PND lock-in failure mode) |
| ADR-21 | ECCMIS shape ratification at Phase-1 close |
| ADR-22 | Kubernetes substrate (RKE2 / k3s) — perimeter cluster + DMZ cluster, no shared identity / namespace / secret |
| ADR-23 | Citizen-app distribution resilience (app-store policy risk) |
| ADR-24 | Policy-as-code (OPA Rego or Cedar) for ABAC rule enforcement |

These await engagement-team ratification before Doc 1 lock. Full text in the project workspace.

### 12.5 NFR catalogue additions (vs §3 §5 NFR row)

Two new testable hard-exclusion NFRs added in Wave 4 alongside the original NFR-039 (no predictive policing) and NFR-040 (no live AFR):

- **NFR-041 — No commercial BG-check tier.** Architecture must not contain `bg-check-tier-2/3/4`, `commercial-disclosure`, or `requester-kyc` modules / routes. CI test asserts absence.
- **NFR-042 — No fabricated AML-KYC of external requesters in BG-check context.** CI test asserts absence of `aml-kyc-bg-check` modules. (Does not exclude AML KYC under other lawful contexts.)

Total NFR count: **42**. The hard exclusions (predictive policing, live AFR, commercial BG-check, AML-KYC-of-BG-check-requesters) are now testable contracts in the architecture, not just policy paragraphs in §9.

### 12.6 Wave outcomes summary

| Wave | Cohorts dispatched | Files written | Lines | Headline outputs |
|---|---|---|---|---|
| W1 | uganda-context (retry after fabrication incident), security-legal-governance, benchmarks | 38 (12+14+12) | ~5,615 | Uganda current-state baseline, DPP Act 2019 article-by-article mapping, 7-comparator benchmark library |
| W2 | functional-requirements-2a, functional-requirements-2b, architecture-and-tech | 28 (8+8+12) | ~5,645 | 348 FRs (Modules 1-9 as W2-scoped), C4 model, 14 LOCKED + 10 PROPOSED ADRs, 40 NFRs, 18 architecture risks |
| W3 | subject-report-service (post-scope-change, renamed from bg-check-service), commercial-delivery | 21 (7+14) | ~5,080 | 104 Internal-Subject-Report FRs, full Doc 2 spine, Doc 1 §12-§16, 33 consolidated risks (R-01..R-33), indicative pricing bands UGX 180–390 bn over 84 months |
| W4 | targeted reconciliation + verification (orchestrator-only) | 1 synthesis note + 2 catalogue updates | small | NFR-041/042 promoted, 2 SUPERSEDED files archived, ISR reconciliation note at `04-synthesis/01-isr-reconciliation-wave-4.md`, 2 honest tagged Tier-1 gaps remain (BoU FX, UPF Cert anchor fee — both behind authenticated portals) |

**Project corpus end-state: 87 files in `projects/upf-cris/02-research/` (85 active in `**/research/*.md`, 2 archived); ~319,000 words across 7 cohorts; ~452 FRs total; 42 NFRs; 33 risks; 14 LOCKED + 10 PROPOSED ADRs; full RBAC/ABAC matrices; 7-comparator benchmark library; 1 reconciliation synthesis note.**

### 12.7 Operational learnings encoded as standing rules

The engagement surfaced two operating-discipline lessons that are now standing rules:

1. **`ls`-verify cohort directory file existence before treating any sub-agent's output as complete.** Sub-agent result blocks are *claims*, not evidence. Wave 1 caught a fabricated result block (uganda-context agent reported writing 12 files; zero existed on disk) that would have polluted the corpus had the orchestrator trusted the result block. Logged in `EVIDENCE-AUDIT.md`.
2. **Sub-agent briefs require the strict reporting envelope:** Windows-style absolute paths, write-tool-only persistence, mandatory post-write `ls -la` reproduced verbatim in `<directory_listing_proof>`, mandatory `wc -w`-measured word counts, explicit `<files_skipped>` for partial completions, fail-and-report behaviour rather than result-block padding. This shape eliminated the failure mode on retry and across Waves 2–4.

Both belong in the engine's `research-orchestration` skill as protocol rules; carry forward to future engagements.

### 12.8 What remains before Doc 1 + Doc 2 ship

- Cross-cohort synthesis (orchestrator-only per repo `CLAUDE.md` rule; never delegated). Consolidates findings, builds the source/claim/quote registry that becomes Doc 1 §20.
- Doc 1 + Doc 2 assembly via `research-report-builder` → `professional-word-output` (or `python-document-generation`).
- Diagrams via `mermaid-expert` (architecture / sequence / BPMN flows) and `canvas-design` (executive infographics).
- `python -m engine validate upf-cris` clean run.
- `python -m engine pack upf-cris --out export/upf-cris.zip` — the deliverable bundle.

The two honest tagged gaps (Tier-1 BoU FX rate; Tier-1 UPF Cert anchor fee) close at inception-time pricing exercise — both clearly marked in their downstream document treatments and not blockers.

### 12.9 Pointers (project workspace is local-only)

The project workspace at `projects/upf-cris/` is git-ignored per the operator's preference. Anyone reproducing or auditing the engagement off another machine would need:
- This design doc (in-repo, pushed)
- The engine + skills (in-repo, pushed)
- The `projects/upf-cris/` directory (handed over directly, not via git)
- Or to re-run the wave-dispatch protocol from this design doc as the script
