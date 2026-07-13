---
name: markdown-lint-cleanup
description: Use when Markdown files need mechanical lint repair for headings, list spacing, fences, and whitespace without changing meaning; use a writing or editing skill when prose or structure needs substantive revision.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

## Platform Notes

- Optional helper plugins may help in some environments, but they must not be treated as required for this skill.

# Markdown Lint Cleanup
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- Fix markdown lint warnings by enforcing headings, blank lines around lists, and language-tagged code fences for clean documentation.
- The task needs reusable judgment, domain constraints, or a proven workflow rather than ad hoc advice.

## Do Not Use When

- The task is unrelated to `markdown-lint-cleanup` or would be better handled by a more specific companion skill.
- The request only needs a trivial answer and none of this skill's constraints or references materially help.


## Markdown Lint Cleanup Required Context
- Gather relevant project context, constraints, and the concrete problem to solve.
- Confirm the desired deliverable: design, code, review, migration plan, audit, or documentation.


## Markdown Lint Cleanup Core Method Notes
- Read this `SKILL.md` first, then load only the referenced deep-dive files that are necessary for the task.
- Apply the ordered guidance, checklists, and decision rules in this skill instead of cherry-picking isolated snippets.
- Produce the deliverable with assumptions, risks, and follow-up work made explicit when they matter.

## Quality Standards

- Keep outputs execution-oriented, concise, and aligned with the repository's baseline engineering standards.
- Preserve compatibility with existing project conventions unless the skill explicitly requires a stronger standard.
- Prefer deterministic, reviewable steps over vague advice or tool-specific magic.


## Markdown Lint Cleanup Existing Failure Notes
- Treating examples as copy-paste truth without checking fit, constraints, or failure modes.
- Loading every reference file by default instead of using progressive disclosure.


## Markdown Lint Cleanup Core Deliverables
- A concrete result that fits the task: implementation guidance, review findings, architecture decisions, templates, or generated artifacts.
- Clear assumptions, tradeoffs, or unresolved gaps when the task cannot be completed from available context alone.
- References used, companion skills, or follow-up actions when they materially improve execution.

## Evidence Produced

| Category | Artifact | Format | Example |
|----------|----------|--------|---------|
| Correctness | Markdown lint cleanup record | Markdown doc tracking lint warnings fixed (headings, blank lines around lists, language-tagged fences) per pass | `docs/lint/markdown-cleanup-2026-04-16.md` |

## References

- Use the links and companion skills already referenced in this file when deeper context is needed.
## Inputs

| Artefact | Source or provider | Requirement | If absent |
|---|---|---|---|
| Markdown files and lint configuration | repository | required | Return a proposed patch if edit or execution is unavailable |

## Capability contract

Read access to Markdown and its lint configuration is required. File edits need explicit authority and must remain mechanical; generated sources or substantive prose changes stay outside that permission.

## Degraded mode

If lint execution or editing is unavailable, return a qualified finding list or patch and mark the final lint result unassessed rather than claiming a clean document.

## Decision rules

| Choice | Action | Failure avoided |
|---|---|---|
| A warning can only be fixed by rewriting meaning | Stop and request editorial authority | Mechanical cleanup changes content |


## Outputs
| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Lint-clean Markdown and check result | maintainers and CI | Intended meaning is unchanged and configured lint passes |


## Markdown Lint Cleanup Evidence Notes 1
- Preserve the lint configuration, before-and-after rule findings, reviewed diff, and any warning withheld to avoid changing meaning.

## Worked example

Add a language tag to a known shell fence and blank lines around a list; do not guess the language of an ambiguous snippet.

<!-- dual-compat-end -->
## Overview

Use this skill to clean markdown files so they pass lint checks with zero warnings. It focuses on consistent headings, spacing, and fenced code block language tags.

## When to Use

- Markdown lint warnings appear (MD022, MD032, MD036, MD040, MD031)
- Documentation updates need a clean lint pass
- Large docs need formatting normalization without content changes

## Core Rules (Required)

1. **Headings must be proper headings**
   - Replace bold-only headings with `##`, `###`, etc.
2. **Blank lines around lists**
   - Add a blank line before and after lists
3. **Blank lines around fenced code blocks**
   - Surround code fences with blank lines
4. **Language tags on fenced code blocks**
   - Use `bash`, `php`, `sql`, or `text` as appropriate

## Common Fixes

### MD036: Emphasis used instead of a heading

**Replace**:

**Section Title**

**With**:

## Section Title

### MD032: Blanks around lists

Ensure blank lines before and after lists:

Text paragraph.

- Item one
- Item two

Next paragraph.

### MD022: Blanks around headings

Add a blank line before and after headings:

Paragraph text.

#### Heading

- List item

### MD040: Fenced code language

Add a language identifier:

```text
Example output line
```

### MD031: Blanks around fences

Ensure fences are separated from other text:

Paragraph text.

```bash
php scripts/verify_uom_system.php
```

## File Safety

- Do not change meaning or content structure
- Only adjust formatting to satisfy lint rules
- Preserve links and references exactly

## Recommended Workflow

1. Identify lint warnings and their line numbers
2. Apply targeted fixes (headings, spacing, code fence languages)
3. Re-check lint until clean

## Output Expectations

- No markdown lint warnings
- No content meaning changes
- Consistent formatting across documents


## Workflow
1. Read the repository lint configuration and define the authorised files.
2. Run or inspect lint findings and separate mechanical fixes from editorial changes.
3. Stop when a fix would change meaning or the code-fence language is unknown.
4. Apply mechanical repairs and rerun checks; recover by reverting the affected hunk and reporting the unresolved rule.


## Markdown Lint Cleanup Evidence Notes 2
| Evidence | Consumer | Acceptance |
|---|---|---|
| Lint result and reviewed diff | Maintainer and CI | Configured lint passes and semantic changes are absent or authorised |


## Anti-Patterns
- Guessing a code-fence language. Fix: inspect the snippet or leave a flagged gap.
- Reflowing prose during lint cleanup. Fix: keep changes mechanical.
- Renumbering intentional examples blindly. Fix: preserve semantic numbering.
- Editing generated Markdown. Fix: repair its source generator.
- Declaring success without rerunning lint. Fix: record the final check result.
