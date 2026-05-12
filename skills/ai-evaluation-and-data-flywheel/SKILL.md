---
name: ai-evaluation-and-data-flywheel
description: Use when designing evaluation, failure analysis, feedback capture, regression datasets, synthetic data controls, and data flywheels for AI-assisted research and agentic workflows.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# AI Evaluation And Data Flywheel

<!-- dual-compat-start -->

## Use When

- Use when improving AI-assisted research workflows, agent prompts, retrieval, tool use, or model selection.
- Use when building eval datasets, failure taxonomies, feedback loops, or regression tests.
- Use when agent outputs must improve through measured evidence rather than intuition.

## Do Not Use When

- The task is a one-off research answer.
- There is no repeatable workflow to evaluate.

## Required Inputs

- Workflow under test, expected outputs, failure examples, user feedback, source material, and acceptance criteria.
- Metrics that matter: correctness, citation integrity, cost, latency, coverage, and usability.

## Workflow

1. Define the task class and quality criteria.
2. Collect representative examples and known failures.
3. Build a small regression set before changing prompts or tools.
4. Measure correctness, source integrity, tool failure, cost, and latency.
5. Tag failures by cause: retrieval, reasoning, tool, prompt, source, or format.
6. Improve the workflow and rerun the same examples.
7. Add production feedback to the eval set after human review.

## Quality Standards

- Evaluation examples are representative, not cherry-picked.
- Source-integrity failures are tracked separately from prose quality.
- Improvements are measured against a stable baseline.
- Synthetic data is labelled and does not replace real failure cases.

## Anti-Patterns

- Changing prompts without evals.
- Treating polished prose as correctness.
- Measuring only pass/fail when failures need categories.
- Adding user feedback without verification.

## Outputs

- Eval set.
- Failure taxonomy.
- Regression report.
- Data flywheel plan.

## Evidence Produced

| Category | Artifact | Format | Example |
|---|---|---|---|
| Correctness | Eval set | JSON/Markdown | Input, expected checks, source material |
| Release evidence | Regression report | Markdown table | Baseline, change, result, failure tags |

## References

- Load `references/eval-flywheel.md` for eval structure and failure tags.

<!-- dual-compat-end -->

## Companion Skills

- `agentic-research-operations` supplies agent workflow design.
- `validation-contract` supplies release evidence standards.
- `source-verification` supplies citation-integrity checks.
