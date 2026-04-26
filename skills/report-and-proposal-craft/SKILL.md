---
name: report-and-proposal-craft
description: Use for long-form persuasion artifacts — business reports (informational, analytical, recommendation, progress, feasibility, audit, formal research), business plans, formal proposals (internal and external), and B2B white papers (backgrounder, numbered list, problem/solution). Carries the artifact router, the audience-grid + purpose-statement + SCQA spine, and orchestration across three craft references (Forsyth, Clippinger, Graham).
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Report & Proposal Craft

Single entry skill for the engine's long-form business persuasion artifacts. For shorter forms (email, memo, blog, web copy), load `business-writing` instead.

## Artifact router

| Artifact | Reference | Distinguishing feature |
|---|---|---|
| Informational report | `references/clippinger-business-reports.md` | No conclusions; just the facts |
| Analytical report | `references/clippinger-business-reports.md` · `references/forsyth-reports-proposals.md` | Interprets data; conclusions but no required action |
| Recommendation report | `references/forsyth-reports-proposals.md` · `references/clippinger-business-reports.md` | Numbered, owned, dated, costed recommendations |
| Progress / status report | `references/clippinger-business-reports.md` · `references/forsyth-reports-proposals.md` § status | RAG status; variances; next-period plan |
| Feasibility report | `references/clippinger-business-reports.md` | Criteria-based go / no-go |
| Audit / compliance report | `references/clippinger-business-reports.md` | Findings ranked by severity; remediation plan |
| Formal research report | `references/clippinger-business-reports.md` (full template) | Methodology section; replicability standard |
| Business plan | `references/clippinger-business-reports.md` § business plan | Market analysis + financial projections + sensitivity |
| Internal proposal / business case | `references/forsyth-reports-proposals.md` § internal proposal | Recommendation upfront; options considered |
| Formal external proposal | `references/forsyth-reports-proposals.md` § external proposal | Cover letter + situation + approach + price + risks |
| Bid response (RFP) | `references/forsyth-reports-proposals.md` § bid | Mirror RFP order; compliance matrix as section 1 |
| White paper — backgrounder | `references/graham-white-papers.md` § backgrounder | Late-funnel; vendor named throughout |
| White paper — numbered list | `references/graham-white-papers.md` § numbered list | Early-funnel; light, scannable |
| White paper — problem/solution | `references/graham-white-papers.md` § problem/solution | Mid-funnel; vendor only in About + CTA |

**Hard rule:** pick the artifact type before drafting. Mixing types (e.g., audit body with recommendation framing, or backgrounder body with numbered-list opener) confuses readers and weakens both functions.

## The persuasion spine (universal)

Every artifact in this skill rides the same four-move spine (Forsyth's SCQA, Minto-style):

- **S — Situation** — stable, agreed background.
- **C — Complication** — change, threat, or opportunity that destabilises it.
- **Q — Question** — implicit reader question ("So what do we do?").
- **A — Answer** — recommendation, with the supporting pyramid below it.

Building the case: state answer first → 3–5 MECE reasons → evidence per reason → action.

## Prerequisites (run before drafting any artifact)

### 1. Audience grid (Forsyth)

| Role | Cares about | Decision power | What they must see | Likely objection |
|---|---|---|---|---|
| Decider | ROI, risk, reputation | Approves / kills | Bottom line + risk envelope on p.1 | "Too expensive / risky" |
| Influencer | Operational fit | Shapes view | Practicality of approach | "Won't work here" |
| Blocker | Cost, controls | Veto | Pricing logic, payment terms | "Numbers don't add up" |
| User | Day-to-day impact | Adoption | Transition plan | "Disrupts my team" |
| Gatekeeper | Compliance, format | Stops document reaching decider | Required headings, format | "Wrong template" |

### 2. Purpose statement (Forsyth)

> *After reading this [report/proposal/white paper], [primary reader] will [decide / approve / fund / change / understand] **X**, because the document shows **Y**, and the next action they will take is **Z** by **[date]**.*

If X/Y/Z is vague, planning is incomplete. Do not draft.

### 3. White-paper mantra (Graham)

For any white paper, the mantra test gates every section:

> *"A truly effective white paper helps business people understand an issue, solve a problem, or make a decision."*

If a section does none of those three, it is brochure or filler.

## Three-way discipline (Clippinger) — applies to every report

| Artifact | What it answers | Voice |
|---|---|---|
| **Finding** | What the data shows | Descriptive, neutral |
| **Conclusion** | What the finding means against the question | Interpretive, no new evidence |
| **Recommendation** | What to do about it | Imperative, owned, dated, costed |

Mixing them — a "finding" that recommends action, or a "conclusion" that introduces new data — is the most common formal-report failure.

## Reference index

| Reference | Source | Load when |
|---|---|---|
| `references/forsyth-reports-proposals.md` | Patrick Forsyth, *How to Write Reports and Proposals* (Kogan Page) | Any report or proposal — audience grid, X/Y/Z purpose, exec-summary stand-alone, SCQA, recommendation discipline, ship gate, 7 reusable templates |
| `references/clippinger-business-reports.md` | Dorinda Clippinger, *Business Report Guides: Research Reports and Business Plans* | Formal research reports and business plans — full section templates, replicability standard, three-way discipline, front/back matter rules |
| `references/graham-white-papers.md` | Gordon Graham, *White Papers For Dummies* | Any of the three white-paper flavors — flavor-picking, mantra, hook rules, evidence hierarchy, vendor-naming rules |

## Executive summary discipline

For any report >10 pages, the executive summary stands alone. Stand-alone test: delete the rest of the document mentally; can the decider still decide correctly? If no, the summary is wrong.

- Length: 1 page max (250–400 words). 2-page exception only for >50-page reports.
- Structure: context · core finding/proposition · 3–5 evidence headlines · ask/recommendation.
- No new material; everything in the summary appears expanded in the body.
- Write it last; placeholder first to constrain scope.

## Universal anti-patterns

- **Data-dump report** — every fact gathered, no synthesis.
- **Buried lead** — recommendation on page 14.
- **Kitchen-sink proposal** — every capability listed, none mapped to the buyer's specific need.
- **Frankenpaper** — three white-paper flavors mashed without discipline.
- **Weak recommendations** — "consider," "explore" with no owner, date, or cost.
- **Methodology hand-waving** — "we surveyed the market" without instrument, sample, dates.
- **Mixing findings, conclusions, recommendations** — the three-way discipline lapse.
- **Selling too hard in a white paper** — vendor name in title, product mention before page 3.
- **Naked claims** — "studies show" without footnote.
- **Five CTAs** in a white paper instead of one.
- **Tone whiplash** — neutral body, sudden marketing voice in conclusion.
- **Plagiarised boilerplate** — prior client/competitor name still in the file.
- **No risk section** in a proposal — sophisticated buyers read this as naïveté.
- **Inconsistent numbering** — body £2.4m, summary £2.6m.
- **Late-stage scope creep** — author keeps adding sections; document loses spine.
- **Format tax failure** — wrong template; fails procurement before reaching decider.
- **Stale stats** (>3 years) without flag in white papers.
- **Pie-chart abuse** — 3-D, exploded, percentages not summing.
- **Strawmanned alternatives** in problem/solution white papers.
- **No ask / no CTA** — document ends without telling the reader what to do next.

## Universal ship gate

- [ ] Artifact type identified; structure matches.
- [ ] Audience grid filled (decider, influencer, blocker, user, gatekeeper).
- [ ] Purpose statement (X/Y/Z) written and met.
- [ ] Lead on page 1 — recommendation/proposition not buried.
- [ ] Three-way discipline observed: findings, conclusions, recommendations strictly separated.
- [ ] Recommendations specific, owned, dated, costed, ranked.
- [ ] Executive summary stands alone — passes "if they only read this" test.
- [ ] Every claim sourced; numbers reconcile across summary, body, appendices.
- [ ] Every visual has takeaway-sentence title, source line, prose anchor.
- [ ] Headings descriptive, parallel, ≤3 levels.
- [ ] Known objections surfaced and rebutted (proposal) or limitations stated (report).
- [ ] Tone consistent: person, voice, terminology, number formatting.
- [ ] Risks/assumptions section present and honest (proposal).
- [ ] Pricing validity period and acceptance mechanism present (proposal).
- [ ] If white paper: flavor labeled; mantra passes; vendor named no earlier than the flavor allows; single CTA.
- [ ] If formal research report: methodology replicable.
- [ ] If business plan: sensitivity analysis on financials.
- [ ] Format/template compliance verified.
- [ ] No client/competitor leftovers from prior boilerplate.
- [ ] Required signatures secured before despatch.

## Companion skills

- `business-writing` — short-form prose (email, memo, blog, web).
- `academic-writing` — papers, essays, theses, dissertations.
- `data-quality-assessment` — score the data behind report findings.
- `dataset-discovery-and-analysis` — for evidence-driven reports.
