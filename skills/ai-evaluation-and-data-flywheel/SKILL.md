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

| Input | Source/provider | If absent |
|---|---|---|
| Workflow, expected outputs, failure cases, source material, and acceptance criteria | Workflow owner and verified run records | Stop scoring and return an evaluation-design gap |
| Correctness, citation integrity, cost, latency, coverage, and usability measures | Decision owner | Record the missing outcome; do not substitute a convenient metric |

## Workflow

1. Define the task class and quality criteria.
2. Collect representative examples and known failures.
3. Build a small regression set before changing prompts or tools.
4. Measure correctness, source integrity, tool failure, cost, and latency.
5. Tag failures by cause: retrieval, reasoning, tool, prompt, source, or format.
6. Improve the workflow and rerun the same examples.
7. Add production feedback to the eval set after human review.
8. Stop when provenance is missing or a release gate fails; recover by quarantining affected cases and rerunning only with clean, versioned inputs.

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
- Hiding critical regressions in aggregate scores. **Fix:** keep critical and ambiguous-case slices as independent release gates.

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Eval set and failure taxonomy | Evaluation owner | Cases have provenance, expected checks, cause labels, and split status |
| Regression report | Release reviewer | Results identify configuration, baseline, slices, and unresolved failures |
| Data flywheel plan | Workflow owner | Feedback admission and rollback rules are explicit |

## Evidence Produced

| Category | Artifact | Format | Example |
|---|---|---|---|
| Correctness | Eval set | JSON/Markdown | Input, expected checks, source material |
| Release evidence | Regression report | Markdown table | Baseline, change, result, failure tags |

## References

- Load `references/eval-flywheel.md` for eval structure and failure tags.

<!-- dual-compat-end -->

## Companion Skills

## Capability Contract

Evaluation is read-only by default. Capturing feedback or changing datasets, prompts, models, production traffic, or release gates requires explicit authority and versioned rollback evidence.

## Degraded Mode

Without executable models or representative data, return an evaluation design and mark performance, regression, and safety outcomes `not assessed`.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| Failure is reproducible | Add a minimal versioned case | Anecdote-driven tuning |
| Synthetic case lacks provenance | Quarantine it | Contaminated benchmark |
| Regression gate fails | Block release | Known quality regression |

## Flywheel Failure Modes

- Optimising one headline score; retain slice metrics.
- Training on the test set; separate datasets.
- Adding unverified synthetic examples; record provenance.
- Erasing failures after fixes; retain regression cases.
- Mutating production from an evaluation run; require authority.

## Worked Example

A citation error becomes a versioned regression case with expected evidence fields before any prompt change is accepted.

## Companion Skills

- `agentic-research-operations` supplies agent workflow design.
- `validation-contract` supplies release evidence standards.
- `source-verification` supplies citation-integrity checks.

## Evaluation Intake Fields

| Input | Source/provider | If absent |
|---|---|---|
| Evaluated workflow, failure taxonomy, representative cases | Product owner and verified run logs | Stop scoring and return an evaluation-design gap |
| Versioned prompts, models, datasets, and expected outcomes | Evaluation registry | Quarantine results whose tested configuration cannot be identified |

## Evaluation Run Workflow

1. Define the decision, failure taxonomy, slices, and release threshold before running cases.
2. Execute representative cases and preserve raw outputs with configuration identifiers.
3. Stop when provenance is missing, test data leaks into training, or a release gate fails.
4. Recover by quarantining contaminated cases, restoring clean versions, and rerunning the affected slices.
5. Add reproducible failures to the regression set only after human verification.

## Evaluation Report Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Evaluation report and versioned regression set | AI workflow owner and release reviewer | Every metric maps to cases, slices, configuration, expected result, and observed result |

## Evaluation Failure Modes

- Optimising one headline score. **Fix:** retain failure slices and guardrail metrics.
- Training on the test set. **Fix:** enforce versioned separation and contamination checks.
- Adding unverified synthetic cases. **Fix:** record provenance and human acceptance.
- Deleting fixed failures. **Fix:** keep them as regression cases.
- Mutating production during evaluation. **Fix:** require separate deployment authority and rollback evidence.
