---
name: critical-reasoning-and-argument
description: Universal reasoning and argument discipline for any output that makes claims, explanations, interpretations, judgments, recommendations, forecasts, or persuasive conclusions. Use for academic writing, intelligence reports, market analyses, history essays, business cases, policy notes, due diligence, executive briefs, legal/policy argument, and technical recommendations before drafting or final delivery.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
  priority: critical
---

# Critical Reasoning And Argument

This is the engine's universal thinking layer. It prevents the engine from merely collecting information and arranging it into plausible prose: every serious output must expose its question, terms, evidence, assumptions, inference chain, countercase, limits, and action implications.

Use this skill for all forms of writing and reporting that contain a claim or conclusion: academic essays, theses, dissertations, literature reviews, systematic reviews, intelligence products, market analyses, history essays, business reports, proposals, board briefs, due diligence, policy analysis, legal argument, technical recommendations, and executive communication.

## Non-negotiable rule

No conclusion ships until it has passed the reasoning protocol in `references/reasoning-protocol.md`.

For research work, this skill operates after `source-evaluation`: source quality determines what can be used as evidence; this skill determines whether the evidence supports the conclusion. For intelligence or forward-looking work, run `analytic-tradecraft` after this skill to add probability language, hypothesis handling, and uncertainty discipline.

## Universal reasoning workflow

1. **Frame the real question.** Convert the prompt into a precise question the output must answer. If the prompt asks for "a report", infer the decision, controversy, interpretation, or action the report is meant to support.
2. **Define scope and terms.** Identify key terms, boundaries, jurisdiction, time period, population, market, method, or discipline. Flag ambiguous or loaded language.
3. **Separate the materials.** Distinguish facts, claims, assumptions, values, interpretations, inferences, recommendations, and unknowns.
4. **Map the argument.** Build the chain: main conclusion -> intermediate conclusions -> premises/evidence -> warrants/linking assumptions. Use the table in `references/reasoning-protocol.md`.
5. **Test evidence quality.** Apply `source-evaluation`; then ask whether the available evidence is relevant, sufficient, representative, current, and independent.
6. **Run the countercase.** State the strongest plausible objection, alternative explanation, rival hypothesis, or historiographical/market/technical counter-reading.
7. **Audit inference quality.** Test causal claims, generalisations, analogies, statistics, definitions, conditionals, necessity/sufficiency, and certainty calibration.
8. **Check coherence and fallacies.** Look for contradiction, circular reasoning, equivocation, straw-manning, false alternatives, hasty generalisation, post hoc causation, appeal to authority, appeal to majority, and unsupported value leaps.
9. **Choose the action form.** Route the tested reasoning into the right structure and tone using `references/audience-action-forms.md`.
10. **Ship with limits.** State what the conclusion means, what it does not mean, confidence limits, operational implications, and next actions.

## Output Standards

Every output using this skill must be:

- **Convincing:** the reader can see why the conclusion follows from the evidence.
- **Authentic:** the tone fits the institution, audience, discipline, and stakes; no generic filler or artificial certainty.
- **Realistic:** recommendations name constraints, tradeoffs, risks, time, cost, incentives, and implementation friction.
- **Actionable:** the reader knows what decision, interpretation, next step, or research move follows.
- **Proportionate:** claim strength matches evidence strength; uncertainty is not hidden.

## Reference Router

| Reference | Load when |
|---|---|
| `references/reasoning-protocol.md` | Always; universal argument map, inference tests, fallacy audit, and ship gate |
| `references/audience-action-forms.md` | Choosing structure, tone, and delivery form for academic, intelligence, market, history, business, policy, legal, technical, or executive outputs |
| `references/literature-review-and-thesis-hardening.md` | Academic writing, literature reviews, proposals, theses, dissertations, and postgraduate research design |
| `references/source-register.md` | Need provenance for the user-supplied books mined into this skill |

## Domain Routing

| Domain | Reasoning emphasis | Then call |
|---|---|---|
| Academic writing | Research question, literature gap, method justification, contribution, counter-literature | `academic-writing`, `academic-reporting-standards` |
| Literature review | Synthesis, theme formation, dispute mapping, gap logic, source quality | `academic-writing` |
| Intelligence report | Hypotheses, indicators, deception risk, probability and confidence separation | `analytic-tradecraft` |
| Market analysis | Decision criteria, segmentation logic, causal drivers, evidence currency, commercial implications | `business-writing`, `report-and-proposal-craft`, `executive-communication` |
| History essay | Chronology, causation, source limits, historiography, alternative interpretations | `academic-writing` |
| Business report/proposal | Finding-conclusion-recommendation separation, options, objections, risk, implementation | `report-and-proposal-craft` |
| Executive brief | Governing thought, 3-5 tested reasons, implications, decision ask | `executive-communication` |
| Due diligence | Claim substantiation, red flags, downside cases, confirmatory tests | `due-diligence`, `analytic-tradecraft` |
| Policy/legal/technical argument | Definitions, authority, standards, burdens, feasibility, tradeoffs | relevant domain skill plus `source-evaluation` |

## Universal Anti-Patterns

- Data dump with no conclusion or decision logic.
- Confident conclusion with no visible evidence-to-inference chain.
- Source summary pretending to be analysis.
- Annotated bibliography pretending to be a literature review.
- Recommendation without owner, timeline, cost, constraint, or risk.
- History narrative with chronology but no causation or interpretive argument.
- Market report with trends but no buyer, competitor, margin, regulation, or execution implication.
- Intelligence judgment that conflates source reliability with probability of the event.
- Academic argument that cites many sources but does not show the gap, method logic, or contribution.
- Counterargument dismissed by tone instead of defeated by evidence and reasoning.
- "It is clear that" language where evidence is partial, contested, stale, or indirect.

## Universal Ship Gate

- [ ] Core question stated.
- [ ] Key terms and scope defined.
- [ ] Facts, assumptions, values, inferences, conclusions, and recommendations separated.
- [ ] Argument map completed for every load-bearing conclusion.
- [ ] Source quality checked through `source-evaluation`.
- [ ] Evidence relevance, sufficiency, representativeness, independence, and currency checked.
- [ ] Strongest objection or alternative explanation addressed.
- [ ] Causal, analogical, statistical, generalisation, and definition claims audited where present.
- [ ] Fallacy/coherence audit completed.
- [ ] Certainty calibrated to evidence strength.
- [ ] Output form selected for audience and action.
- [ ] Limits, risks, implications, and next actions stated.

## Companion Skills

- `source-evaluation` - mandatory for source-backed research; establishes evidence discipline.
- `analytic-tradecraft` - intelligence, uncertainty, forecasts, contested evidence, and adversarial settings.
- `academic-writing` - academic form, originality, citation, synthesis, register, and source-away composition.
- `academic-reporting-standards` - thesis/dissertation examination standards and study-reporting checklists.
- `report-and-proposal-craft` - business reports, proposals, white papers, and formal research reports.
- `business-writing` - short-form professional prose.
- `executive-communication` - executive summaries, board briefs, and top-down communication.
- `research-design` - research questions, methods, and contribution logic.
- `research-techniques` - source mining, gap analysis, synthesis, and verification workflows.
