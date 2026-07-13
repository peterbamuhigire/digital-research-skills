---
name: report-and-proposal-craft
description: Use when choosing and drafting a long-form business report, proposal, business plan, bid response, or white paper whose evidence, persuasion structure, and reader decision must be explicit; use business-writing for short emails, memos, blogs, or web copy.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Report & Proposal Craft

<!-- dual-compat-start -->

Single entry skill for the engine's long-form business persuasion artifacts. For shorter forms (email, memo, blog, web copy), load `business-writing` instead.

Long-form reports and proposals must persuade by reasoning, not by arrangement. Before drafting findings, conclusions, recommendations, options, risks, or objections, run `critical-reasoning-and-argument` so the evidence-to-claim chain, countercase, and certainty level are explicit.

When a report or proposal describes a system, process, workflow, operating model, requirements set, interface, data architecture, or design system, also load `systems-process-requirements` before drafting the body.

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
| Growth strategy report | `../../extracted-books/growth-profit-disruption-research-notes.txt` · `references/forsyth-reports-proposals.md` | Growth engine + constraints + experiments + KPI tree |
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

### 3. Critical reasoning gate

Load `critical-reasoning-and-argument` before drafting the body. Each finding, conclusion, recommendation, and option must have an argument map, strongest objection, implementation constraint, and confidence limit.

### 4. White-paper mantra (Graham)

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
- [ ] `critical-reasoning-and-argument` run on findings, conclusions, recommendations, options, risks, and objections.
- [ ] `systems-process-requirements` run where the artifact describes systems, processes, workflows, scope, interfaces, data, requirements, or design systems.
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
- [ ] If growth strategy: growth engine, profit lever, experiment plan, dashboard owner, and retention logic are explicit.
- [ ] Format/template compliance verified.
- [ ] No client/competitor leftovers from prior boilerplate.
- [ ] Required signatures secured before despatch.

## Companion skills

- `business-writing` — short-form prose (email, memo, blog, web).
- `critical-reasoning-and-argument` — mandatory for every analytical finding, conclusion, recommendation, option, objection, risk, and implementation implication.
- `systems-process-requirements` — for system/process descriptions, requirements sets, scope, workflows, interfaces, data architecture, and design-system documentation.
- `academic-writing` — papers, essays, theses, dissertations.
- `data-quality-assessment` — score the data behind report findings.
- `dataset-discovery-and-analysis` — for evidence-driven reports.

## Use When

- The artifact is a long-form report, business plan, proposal, bid response, or white paper with a defined reader decision.

## Do Not Use When

- Use business-writing for short correspondence and academic-writing for examiner-facing scholarship.

## Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Brief, audience, decision, and required format | Requester or procurement pack | Stop before drafting and record the missing decision or format. |
| Findings and claim-level sources | Verified research corpus | Mark evidence gaps; never manufacture supporting facts. |

## Workflow

1. Classify the artifact and stop if the format or decision is unknown.
2. Build the audience grid, purpose statement, and evidence-to-claim map.
3. Choose the matching reference; separate findings, conclusions, and recommendations.
4. Draft, reconcile numbers and citations, test objections, then run the ship gate.
5. If evidence fails, recover by removing or qualifying the claim and return to research.

## Outputs

| Artifact | Consumer | Acceptance condition |
|---|---|---|
| Decision-ready report or proposal | Named reader or evaluator | Format matches the selected type; claims are traceable; ask, risks, and next action are explicit. |

## Evidence Produced

| Category | Artifact | Acceptance condition |
|---|---|---|
| Correctness | Claim-source and number-reconciliation record | Every material claim and repeated figure resolves to the same verified source/value. |

## Capability Contract

Planning and review default to read-only. Draft or edit only with artifact authority; submission, signature, pricing commitment, publication, or client contact requires separate explicit authority.

## Degraded Mode

If sources, required templates, rendering, or approval data are unavailable, return the outline, verified sections, and a named gap list. Do not present an unrendered, unverified, or unsigned artifact as final.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| Artifact type uncertain | Stop and resolve the reader decision and mandated structure | Hybrid document that satisfies no evaluator |
| Evidence contradicts the recommendation | Surface the countercase and revise | Persuasion that outruns evidence |
| Procurement format supplied | Mirror its order and build a compliance check | Administrative rejection |

## Worked Example

Given an external proposal and an RFP, select the bid-response route, map every mandatory item before drafting, and return a compliance matrix plus the proposal; do not substitute a generic sales document.

## Anti-Patterns

- Mixing artifact types. Fix: select one governing structure.
- Burying the decision. Fix: state the answer early.
- Merging finding and recommendation. Fix: separate the reasoning stages.
- Using untraceable evidence. Fix: remove or verify the claim.
- Submitting without format review. Fix: run the compliance gate.

## Quality Standards

The artifact matches one selected form, separates evidence from interpretation and action, reconciles material figures, and gives the named reader an explicit decision path.

## References

- [Forsyth reports and proposals](references/forsyth-reports-proposals.md)
- [Clippinger business reports](references/clippinger-business-reports.md)
- [Graham white papers](references/graham-white-papers.md)

<!-- dual-compat-end -->
