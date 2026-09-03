# Anti-Slop Governance for Digital Research Outputs

Last verified: 2026-07-08
Standard/version: Digital Research Engine July 2026 anti-slop gate

This file governs research prose quality. Visual formatting routes to the design-system-skills engine; this engine owns evidence, reasoning, and language quality.

Apply the dated [Machine-Error Editorial Gate](../continuous-improvement/machine-errors-editorial-gate-2026-09-03.md)
in addition to the evidence and reasoning controls below. A polished sentence is not automatically
useful: every retained unit needs a semantic delta or a documented functional exception.

## Prohibited output patterns

- Generic openings that announce the topic instead of stating the decision problem.
- "Studies show", "experts say", "it is important to note", or similar unsourced filler.
- Decorative recommendations that do not name a decision, owner, evidence threshold, or risk.
- Bullet lists that avoid explaining warrants.
- Quotes used as colour when they are not verified.
- "Comprehensive" claims when the search strategy was bounded.
- Executive summaries that summarize sections instead of giving the answer.
- Semantic repetition, decorative symmetry, over-explanation, inflated significance, generic examples,
  rhetorical mannerisms, and insight-shaped filler.

## Required polish criteria

- Each section must answer a real reader question.
- Each finding must identify whether it is fact, inference, synthesis, recommendation, or gap.
- Each recommendation must name the condition under which it changes.
- Each caveat must be material, not ritual.
- Tables must reduce complexity; they must not bury weak reasoning.
- Every major paragraph has an identified claim, warrant, evidence, implication, or decision; otherwise
  cut it or record the missing evidence as a gap.

## Release-blocking slop failures

| Failure | Why it blocks release | Fix |
|---|---|---|
| Unsourced specificity | Looks concrete while being unverifiable | Source it or remove it |
| Viewpoint-free section | Gives information without judgment or relevance | Add the claim, warrant, and decision implication |
| Template sameness | Could apply to any project | Replace with project-specific evidence and stakes |
| Hedged conclusion | Avoids the decision the reader needs | State the judgment and confidence level |
| Evidence laundering | Converts weak sources into strong findings | Downgrade or triangulate |

## Final read-through

Before release, read the output once as a sceptical reviewer and once as the target reader. If either reader cannot trace the evidence or understand the decision implication, the output does not ship.
