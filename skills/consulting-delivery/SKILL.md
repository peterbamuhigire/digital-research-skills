---
name: consulting-delivery
description: "Use when the engine's research must be turned into consulting-grade problem solving: issue trees, hypothesis-led workplans, analysis plans, stakeholder management, implementation logic, and transformation framing. Encodes consulting craft without relaxing evidence discipline."
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
  priority: high
---

# Consulting Delivery

<!-- dual-compat-start -->
## Use When

- Use when research must become consulting-grade diagnosis, recommendation, workplan, or transformation framing.
- Use when the deliverable needs issue trees, hypotheses, quantified options, or implementation logic.

## Do Not Use When

- The task is purely academic writing or pure source collection with no client decision attached.
- The work only needs prose polish rather than consulting problem-structuring.

## Required Inputs

- Client or decision-owner question.
- Time horizon and constraints.
- Expected deliverable and implementation ambition.

## Workflow

- Read this `SKILL.md` first, then load only the relevant reference file for the current phase.
- Structure the problem before expanding the workplan.
- Tie analyses and recommendations back to the client decision throughout.

## Quality Standards

- Decision owner and question are explicit.
- Issue tree and hypotheses are visible.
- Recommendation includes value, risk, and implementation implications.

## Anti-Patterns

- Workstreams with no governing client question.
- Recommendations with no owner or sequence.
- Treating stakeholder politics as outside the analysis.

## Outputs

- A consulting-grade problem frame, workplan, recommendation structure, or implementation path.

## References

- Use the `references/` files for problem framing, workplans, stakeholders, and transformation logic.
<!-- dual-compat-end -->

This skill turns a research corpus into a consulting-grade decision process. It is about how to structure the problem, sequence the analysis, manage the client interface, and carry recommendations into implementation.

Consulting output must be more than polished slides. Run `critical-reasoning-and-argument` before finalizing issue trees, hypotheses, options, recommendations, value cases, risks, or implementation logic.

## When to use

- Strategy, market-entry, growth, transformation, or operating-model work
- Client-facing diagnostics or recommendations
- Internal decision memos that must survive executive scrutiny
- Research that must lead to quantified choices, implementation options, or a value case

## Five rules

1. **Start from the client decision.** The problem statement must name the decision, owner, and time horizon.
2. **Structure before analysis.** Use issue trees, hypotheses, and workplans before gathering endless facts.
3. **Quantify the value and the risk.** A recommendation without upside, downside, and assumptions is unfinished.
4. **Manage stakeholders explicitly.** Good analysis fails when the buyer, blocker, and user were treated as the same person.
5. **Implementation begins in the diagnosis.** Recommendations must name who does what, in what sequence, and what proves progress.
6. **Reason before recommendation.** Every recommendation must pass `critical-reasoning-and-argument`: argument map, strongest objection, alternatives, evidence sufficiency, and implementation constraints.

## Router

| Situation | Load |
|---|---|
| Framing the problem and hypothesis tree | `references/problem-framing-and-issue-trees.md` |
| Designing the analyses and workplan | `references/consulting-workplan-and-analysis.md` |
| Managing client, team, and stakeholders | `references/client-and-stakeholder-management.md` |
| Transformation / implementation / agile delivery | `references/implementation-and-transformation.md` |

## Core workflow

1. Define the governing client question.
2. Break it into an issue tree and draft initial hypotheses.
3. Design the analysis plan: what must be true, what data proves it, what would falsify it.
4. Sequence the work into a workplan with owners and decision points.
5. Translate findings into options, value case, risks, and implementation path.

## Ship gate

- [ ] Decision owner, question, and time horizon named
- [ ] Issue tree or equivalent decomposition exists
- [ ] Critical-reasoning gate passed for hypotheses, options, recommendations, risks, and implementation implications
- [ ] Hypotheses are testable, not slogans
- [ ] Analyses are tied to decisions, not curiosity
- [ ] Stakeholders mapped beyond the formal sponsor
- [ ] Recommendation includes assumptions, risks, and implementation path
- [ ] Metrics or KPIs identified for tracking progress

## Anti-patterns

- Research with no client decision attached
- Workstream explosion because the problem was never decomposed
- Elegant recommendation with no owner or sequencing
- Treating stakeholder politics as outside the scope of strategy
- Confusing slide polish with problem solving

## Companion skills

- `research-orchestration` — drives the research waves
- `critical-reasoning-and-argument` — validates hypotheses, issue trees, options, recommendations, value cases, and implementation logic
- `analytic-tradecraft` — for uncertainty, alternatives, and confidence
- `executive-communication` — for answer-first client delivery
- `report-and-proposal-craft` — for the long-form report or proposal shell
- `data-visualization` — for charts, tables, and KPI trees

## Sources for this skill

- Rasiel, Ethan M., and Friga, Paul N. *The McKinsey Mind*. Tier 1.
- Burtonshaw-Gunn, Simon. *Essential Tools for Management Consulting*. Tier 1.
- *Inside the Minds: Leading Consultants*. Tier 1.
- Hattori, Shu. *The McKinsey Edge*. Tier 1.
- *Rewired: The McKinsey Guide to Outcompeting in the Age of Digital and AI*. Tier 1.
