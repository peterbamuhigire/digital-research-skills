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

## Decision Intake Guidance

- Decision owner, deadline, decision rights, options, constraints, success criteria, values, risks, and evidence base.
- Non-negotiables, budget/time limits, excluded options, and implementation capacity.
- Source manifest and reasoning map for all load-bearing claims.

## Decision Method Detail

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

## Decision Failure Notes

- Recommendation without options.
- Options without criteria.
- Criteria chosen after the preferred answer is known.
- Risk register with no owner, trigger, or mitigation.
- "More research" as a recommendation without specifying the decision it unlocks.

## Decision Deliverable Detail

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

## Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Decision owner, deadline, objectives, constraints | Sponsor or brief | Stop and frame the decision |
| Alternatives, evidence, uncertainty, values | Verified analysis and stakeholders | Expose missing options or values |

## Capability Contract

Analysis is read-only by default. Making the decision, committing funds, contacting parties, publishing, or implementing an option requires explicit authority.

## Degraded Mode

With incomplete evidence or stakeholder values, return a conditional options table and information-value gaps, not a definitive recommendation.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| No real alternatives | Generate or explain constraint | False choice |
| Uncertainty can change ranking | Seek highest-value evidence | Premature commitment |
| Option breaches a guardrail | Eliminate or escalate | Unsafe recommendation |

## Worked Example

When two options rank differently under unresolved cost assumptions, the recommendation remains conditional and names the decisive evidence.

## Companion Skills

- `research-output-formats` or `analytical-report-shapes` selects the deliverable form.
- `executive-communication` turns the tested decision logic into a board-ready artifact.
- `calibration-and-forecasting` handles probability and uncertainty.
- `knowledge-productization` packages reusable decision frameworks.

## Workflow

1. Name the decision owner, deadline, objectives, constraints, values, and guardrails.
2. Generate genuine alternatives and compare them against explicit criteria and uncertainty.
3. Stop when no real alternative exists, a guardrail is breached, or decisive evidence is missing.
4. Recover by reframing options, seeking high-value evidence, or issuing a conditional recommendation.
5. Run a pre-mortem and state commitment, review, and reversal conditions.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Decision frame, options table, and recommendation | Decision owner and executive reviewer | Alternatives, criteria, evidence, uncertainty, tradeoffs, guardrails, and commitment are visible |

## Anti-Patterns

- Presenting one option as a choice. **Fix:** generate alternatives or explain the constraint.
- Hiding stakeholder values. **Fix:** make criteria explicit.
- Averaging away uncertainty. **Fix:** show ranges and sensitivity.
- Ignoring guardrails. **Fix:** eliminate or escalate unsafe options.
- Skipping the pre-mortem. **Fix:** test failure modes first.
