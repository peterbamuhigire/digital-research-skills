# Portfolio Kaizen Standard

Status: mandatory cross-engine operating standard
Effective: 2026-08-04
Owner: Peter Bamuhigire

## Purpose

Kaizen is a governing principle for every skills engine and every product it produces. It is not a motivational paragraph or a once-a-year workshop. Each engine must make its own weaknesses visible, run small evidence-backed improvements, standardise what works, and keep a next improvement ready.

The engines remain independent repositories. This standard is a shared contract; each engine keeps its own implementation, domain rubric, examples, and validation commands.

## The non-negotiable cycle

`Observe -> Baseline -> Select -> Experiment -> Check -> Standardise -> Teach -> Re-measure`

1. **Observe.** Inspect the engine or product in its real operating context. Record the output types, users, constraints, evidence, and failure modes.
2. **Baseline.** Score every applicable dimension with named evidence. The published audit score is hard-capped at 65/100: `capped_score = min(raw_score, 65)`. A cap is a strict reporting ceiling, not permission to hide defects.
3. **Select.** Choose the smallest set of high-leverage gaps. Prefer root causes, repeated defects, customer harm, safety issues, and missing proof over cosmetic expansion.
4. **Experiment.** Write an improvement hypothesis, owner, time-box, expected measure, reversibility, and stop condition. Prefer a small change that can be tested quickly.
5. **Check.** Re-run the relevant validators, source checks, user/product tests, and independent review. Record both positive and negative evidence.
6. **Standardise.** Promote a successful change into a skill, reference, template, fixture, routing rule, test, or release gate. Do not leave successful learning in a conversation only.
7. **Teach.** Update the relevant engine router and cross-engine handoff so the improvement is discoverable and reusable.
8. **Re-measure.** Re-audit the changed dimensions and keep the next gap visible. Improvement plans must target 95/100, even though the audit report remains capped at 65/100.

## Audit contract

Score each applicable dimension /100 with evidence and a one-line deficiency statement:

| Dimension | Minimum evidence to inspect |
|---|---|
| Doctrine | current operating principles and boundaries |
| Taxonomy and routing | complete inventory, descriptions, handoffs, duplicate/dead routes |
| Skill depth | inputs, workflow, outputs, failure recovery, quality criteria |
| Applied proof | worked examples, fixtures, before/after or test evidence |
| Standards currency | dated source register, owner, review date, current-version check |
| Output readiness | each product type assessed end-to-end |
| Accessibility and inclusion | applicable accessibility, language, locale, safety checks |
| Production and handoff | render/build/deploy/export/rollback evidence where applicable |
| Hygiene | stale content, raw-source leakage, redundancy, broken links |
| Safety and integrity | permissions, provenance, privacy, harmful-output controls |

The audit report must show the raw dimension scores, the capped overall score, the cap calculation, evidence gaps, and blockers. Any safety, legal, financial, privacy, or release-blocking failure remains a blocker regardless of numeric score.

## Improvement-plan contract

Every plan must have a 95/100 target score and a traceable backlog:

| Field | Required value |
|---|---|
| Gap | named dimension, product type, and evidence |
| Root cause | process, skill, reference, routing, tooling, or proof failure |
| Change | exact new skill, reference, fixture, validator, or gate |
| Hypothesis | what should improve and why |
| Owner and due date | accountable person/team and review point |
| Acceptance evidence | command, test, user result, rendered artefact, or independent review |
| Risk and rollback | blast radius, reversibility, and stop condition |
| Target | dimension score and overall target contribution toward 95/100 |

Do not close an action because prose was added. Close it only when the named evidence exists and the route can be found by a fresh agent.

## Product-audit contract

Every product audit starts by naming the product type and its intended audience. It then checks: purpose and requirements, evidence and assumptions, domain correctness, usability/accessibility, security/privacy/safety, production fidelity, operational handoff, and observed user or stakeholder value. The audit produces:

- a capped scorecard (maximum 65/100);
- release blockers and uncertainty labels;
- a ranked improvement backlog targeting 95/100;
- one small experiment for the next cycle;
- a re-audit date and evidence owner.

Products include websites, web/mobile/desktop apps, games, databases, designs, documents, reports, proposals, business plans, research outputs, runbooks, and financial artefacts. Route visual and rendered work to the design-system engine when available; route finance/accounting work to Chwezi; route current external facts to this research engine.

## Research and source discipline

All engines may reach `C:\wamp64\www\digital-research-skills`. Current, contested, legal, regulatory, platform, safety, market, or standards claims must use `source-evaluation` and `source-verification`. Book-informed guidance is an independent synthesis: do not copy raw books, OCR, long extracts, or reconstructive chapter text into an engine.

## Cadence

- **Per deliverable:** capture defects and one improvement opportunity before release.
- **Per major iteration:** run the product audit and anti-slop/relevant quality gates.
- **Monthly:** review the engine improvement backlog and standardise completed learning.
- **Quarterly:** run a full engine audit with the 65 cap and refresh the 95 plan.
- **On trigger:** audit immediately after a serious failure, source/standard change, repeated customer complaint, or new book/evidence set.

## Definition of done

Kaizen work is done only when the change is implemented, routed, validated, documented with evidence, and assigned a next review. “We intend to improve” is not an improvement.
