---
name: decision-support-analysis
description: Use when research must support a decision, recommendation, investment, policy choice, product bet, go/no-go call, prioritization, or executive memo. Encodes decision framing, alternatives, values, uncertainty, tradeoffs, pre-mortem, and commitment quality gates.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Decision Support Analysis

<!-- dual-compat-start -->

## Use When

- Use when the output must help someone choose, prioritize, fund, stop, launch, regulate, buy, sell, hire, partner, litigate, or investigate further.
- Use for decision memos, recommendation reports, options papers, board papers, feasibility studies, and executive briefs.
- Use after `critical-reasoning-and-argument` and before `executive-communication`.

## Do Not Use When

- The user only needs a descriptive research brief with no choice or recommendation.
- A binding legal, regulatory, or institutional template controls the decision form.

## Required Inputs

- Decision owner, deadline, decision rights, options, constraints, success criteria, values, risks, and evidence base.
- Non-negotiables, budget/time limits, excluded options, and implementation capacity.
- Source manifest and reasoning map for all load-bearing claims.

## Workflow

1. Define the decision: owner, timing, irreversible elements, and default path.
2. Frame success: objectives, values, constraints, and disqualifiers.
3. Widen options: include the base case, at least two live alternatives, and a wait option when realistic.
4. Map evidence to options: what supports, weakens, or is unknown for each option.
5. Test uncertainty through calibration and tradecraft companion skills.
6. Run tradeoff analysis: benefits, costs, risks, reversibility, option value, implementation friction, and stakeholder incentives.
7. Pre-mortem the preferred option and name kill criteria.
8. State the recommendation, dissenting view, decision ask, next actions, owner, and review date.

## Quality Standards

- The real decision is visible in the first page or opening section.
- Options are live choices, not straw alternatives.
- Criteria are weighted or at least ordered by importance.
- Recommendation strength matches evidence strength and uncertainty.
- Implementation reality is part of the decision, not an appendix.

## Anti-Patterns

- Recommendation without options.
- Options without criteria.
- Criteria chosen after the preferred answer is known.
- Risk register with no owner, trigger, or mitigation.
- "More research" as a recommendation without specifying the decision it unlocks.

## Outputs

- Decision frame.
- Options matrix.
- Tradeoff and uncertainty table.
- Recommendation with dissent, pre-mortem, next actions, and review trigger.

## Evidence Produced

| Category | Artifact | Format | Example |
|---|---|---|---|
| Correctness | Decision frame | Markdown table | Owner, decision, deadline, criteria |
| Release evidence | Options matrix | Markdown table | Option, evidence, risks, tradeoffs, recommendation |

## References

- Load `references/decision-frame.md` for framing and options templates.
- Load `references/options-and-tradeoffs.md` for quality gates and anti-patterns.

<!-- dual-compat-end -->

## Companion Skills

- `research-output-formats` or `analytical-report-shapes` selects the deliverable form.
- `executive-communication` turns the tested decision logic into a board-ready artifact.
- `calibration-and-forecasting` handles probability and uncertainty.
- `knowledge-productization` packages reusable decision frameworks.
