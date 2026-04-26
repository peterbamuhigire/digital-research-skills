# 05 — Implementation Roadmap (6 months)

**Date:** 2026-04-26
**Goal:** Lift engine score from 62 / 100 to ≥ 85 / 100. Close every "must-meet" baseline from `02-benchmark-standards.md` Part 3.

---

## Sequencing logic

Three constraints drive the order:

1. **Highest-leverage skills first.** `analytic-tradecraft` and `executive-communication` close the largest scoring gaps and have no upstream dependencies.
2. **Skills before tools where the skill defines the contract.** Building `tools/verification/` is easier once `osint-investigation` upgrades have specified exactly what each tool must return.
3. **Stress-test by month 4.** A second project shakes out integration bugs before adding the knowledge-base layer (which depends on having more than one project's worth of artefacts).

---

## Month 1 — Analytic + communication backbone

### Week 1–2: A1 `analytic-tradecraft`
- Author SKILL.md + 5 references (ICD 203, SATs catalog, estimative probability, Admiralty Code, cognitive biases)
- Add `analytic-tradecraft.checklist.md` — the ICD 203 ship-gate
- Wire into `research-orchestration` so Wave 2 invokes Key Assumptions Check + Pre-Mortem before Wave 3
- Smoke-test: run ACH on a contested claim from the East Africa project; check that the matrix surfaces alternatives the original synthesis missed

### Week 3–4: A2 `executive-communication`
- Author SKILL.md + 4 references (Pyramid Principle, action titles, Zelazny chart selection, executive summary template)
- Build `templates/executive-summary.md`, `templates/action-titled-deck.md`, `templates/one-pager.md`
- Smoke-test: regenerate the East Africa report's executive summary using Pyramid; compare to v1; capture before/after diff in `EVIDENCE-AUDIT.md`

**Month 1 exit criteria:** Both skills shipped; one before/after artefact each.

---

## Month 2 — Academic standards + verification tooling

### Week 1: A3 `academic-reporting-standards` (skill + references)
- Author SKILL.md
- References: EQUATOR decision tree, PRISMA 2020, CONSORT 2025, STROBE, MOOSE, GRADE, Cochrane summary, TOP Guidelines, style-guide router
- **Wave-2 sub-task:** dispatch a research agent to mine Cambridge / Oxford / LSE / Harvard / Yale / Princeton published examination regulations. Encode word counts, original-contribution requirement, viva conventions into `references/oxbridge-examination-conventions.md`

### Week 2–4: complete `tools/verification/`
- `exif.py`: full extraction with timestamp / GPS / camera reconciliation
- `reverse_image.py`: Google Lens + Yandex + TinEye + Bing fan-out with rate limiting
- `archive.py`: Wayback + archive.today resurrection; memento.org endpoints
- `provenance.py`: earliest-known-timestamp tracing across platforms
- Wire to `osint-investigation` and `source-evaluation` so Silverman methodology runs end-to-end

**Month 2 exit criteria:** Academic-reporting skill shipped; verification tools production-ready; one verified-image case study run end-to-end.

---

## Month 3 — Quantitative layer

### Weeks 1–3: A4 `quantitative-modelling` + `tools/quant/`
- SKILL.md + references (Bain sizing 5-step, sensitivity, scenario, financial-model skeleton, confidence bands)
- `tools/quant/sizing.py` — top-down + bottom-up triangulation utility
- `tools/quant/sensitivity.py` — one-variable sweep with auto-plot
- `tools/quant/scenario.py` — base / bull / bear with assumption-set declaration
- `tools/quant/confidence_band.py` — produces +/- ranges from named assumptions
- Wire into `report-and-proposal-craft` so any quant claim ships with confidence band

### Week 4: integrate
- Re-run a market-sizing question on the East Africa hostel domain through the new skill
- Verify the output meets the McKinsey "uncertainty cube" pattern (≥6 variables varied)

**Month 3 exit criteria:** One end-to-end market sizing with triangulated estimate, sensitivity table, and scenario span. Report meets Bain output expectations.

---

## Month 4 — Primary research + DD tooling + second project

### Weeks 1–2: A5 `primary-research`
- SKILL.md + references (interview protocol, survey design, Delphi, qualitative coding, consent & ethics)
- Templates: interview guide, survey instrument, Delphi round-1 brief, codebook

### Weeks 2–3: complete `tools/sanctions/` + `tools/dd/registry_atlas.py`
- Live OFAC + UN + EU + UK + Canada watchlist sync
- Fuzzy-match discipline + false-positive disposition log
- Registry connectors for East African jurisdictions first, then global

### Weeks 3–4: stand up SECOND project
- Choose a domain outside East Africa housing (suggested: financial-services or healthcare DD on a single named entity)
- Goal: stress-test `due-diligence`, `quantitative-modelling`, `primary-research` together
- Capture lessons in `projects/<id>/EVIDENCE-AUDIT.md` and propagate fixes back to skills

**Month 4 exit criteria:** Primary-research skill shipped; sanctions tooling live; second project under way with at least one wave complete.

---

## Month 5 — Knowledge management + peer review

### Weeks 1–2: A6 `knowledge-base`
- SKILL.md + sanitisation rules + indexing schema
- `tools/kb/index.py`, `tools/kb/search.py`, `tools/kb/sanitise.py`
- Lift sanitised artefacts from East Africa project + second project into the KB
- Wire into `research-orchestration` so Wave 1 cohort agents query KB before launching

### Weeks 2–3: A7 `peer-review-loop`
- SKILL.md + external-review-brief template + dissent-footnoting template
- Recruit one external SME for the second project
- Run Wave 3.5 on the second project; capture review log

### Week 4: enforce ship-gate automation
- `tools/ci/url_liveness.py` — every URL in any output must be live + archived
- Pre-commit hook runs the ICD 203 checklist + Pyramid Principle structure check on flagged outputs

**Month 5 exit criteria:** KB live with ≥30 sanitised nuggets; one external peer review completed and logged; URL-liveness CI enforced.

---

## Month 6 — Deferred-tier skills + bake-off

### Weeks 1–2: deferred skills (parallel)
- `competitive-intelligence`
- `data-visualisation` (separate from Zelazny chart-selection: Tufte + dashboards + infographics)
- `cost-control` (token-budget discipline retrofit into `research-orchestration`)

### Weeks 2–3: deferred skills cont'd
- `multi-language-research` (start with Swahili + French given East Africa exposure)
- `paywalled-database-access` workflow patterns

### Week 4: bake-off
- Pick one strategic question (e.g., "should client X enter market Y in East Africa?")
- Run engine end-to-end (10 hours of analyst supervision)
- Run a manual McKinsey-style consultant pass on the same brief (analyst time-boxed)
- Score both outputs against ICD 203 + Pyramid Principle + Bain sizing standards
- Publish results internally; revise scorecard rubric based on findings

**Month 6 exit criteria:** Bake-off complete; revised scorecard run; engine score targeted ≥ 85 / 100.

---

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Skill build velocity overruns | Cut Month 6 deferred-tier scope before cutting peer-review or KB |
| Second project domain mismatch with skills | Pick the second project from a domain where existing tools (`tools/dd/`, `tools/data/`) already have coverage |
| External SME unavailable | Use cross-discipline peer (e.g., academic for a DD project) — different lens still surfaces blind spots |
| Sanctions API costs balloon | Cache aggressively; throttle; use OFAC SDN list directly (free) before paid feeds |
| Bake-off subjective | Score against published checklists (ICD 203, Pyramid, PRISMA) — not "feels better" |

---

## After month 6

The engine should be at ≥ 85 / 100 against the rubric in `06-scorecard.md`. The remaining gap to 95+ is largely:

- Brand and trust (consultancies sell the brand as much as the work)
- Multi-year longitudinal data (Gartner has 25 years of MQ history; engine has months)
- Network access (MBB partner networks open doors no engine can)
- Headcount-of-experts (1,800 McKinsey knowledge pros vs. 1 engine instance)

Closing those gaps is operating-model work, not skill-build work. The engine's job is to make the consulting practice's *output* world-class. Brand, network, and longitudinal data are the practice's job.
