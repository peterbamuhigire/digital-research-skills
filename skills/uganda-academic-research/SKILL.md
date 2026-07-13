---
name: uganda-academic-research
description: Use when drafting or reviewing a concept paper, proposal, dissertation, thesis, report, viva plan, or dissemination artifact against a named Ugandan university handbook; use research-design for method logic and never generalise one institution's rule to another without evidence.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Uganda Academic Research

<!-- dual-compat-start -->

## Use When

- A named Ugandan university handbook governs an academic research artifact.

## Do Not Use When

- Do not generalise one institution's rules to another or replace research-design method logic.

## Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Named institution, artifact, programme/level, and current handbook | Student/supervisor and official institution source | Stop institution-specific claims and request the governing handbook. |
| Draft, research design, ethics status, and citation style | Author and project files | Return only the checks supported by available artifacts. |

## Workflow

1. Load evidence discipline and confirm the governing institution and handbook version.
2. Select the matching artifact route and extract only traceable requirements.
3. Compare the artifact to structure, ethics, citation, examination, and formatting rules.
4. Stop on missing or conflicting institutional evidence; recover with a gap list.
5. Revise only with authority and rerun the compliance check.

## Outputs

| Artifact | Consumer | Acceptance condition |
|---|---|---|
| Institution-specific compliance review or revised artifact | Student, supervisor, or reviewer | Each requirement cites the governing handbook location; gaps and unassessed checks remain visible. |

## Evidence Produced

| Category | Artifact | Acceptance condition |
|---|---|---|
| Correctness | Handbook compliance matrix | Every pass/fail maps to a real institutional source. |

## Capability Contract

Review defaults to read-only. Editing a student's work requires explicit authority; submission, ethics approval, supervisor/examiner representation, or certification requires the responsible institution or person.

## Degraded Mode

Without the current official handbook, return generic research guidance clearly labelled non-institutional and a source gap. Never claim university compliance.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| Official handbook conflicts with generic guidance | Follow the verified handbook | Institutional non-compliance |
| Institution or programme is unknown | Stop institution-specific review | False generalisation |
| Requirement cannot be traced | Mark a gap | Fabricated rule |

## Quality Standards

Institutional claims are current, source-linked, programme-aware, and separated from generic academic advice.

## Anti-Patterns

- Applying one university's format everywhere. Fix: identify the institution.
- Citing a handbook from memory. Fix: link the exact source.
- Calling a draft ethics-approved. Fix: distinguish review from approval.
- Treating supervisor preference as policy. Fix: label its authority.
- Hiding an unavailable handbook. Fix: mark a source gap.

## Worked Example

For a proposal governed by a named university, verify the current official handbook, map each required section and ethics item, and leave any untraceable formatting claim as a gap.

## References

- [Uganda handbook standards](references/uganda-handbook-standards.md)

<!-- dual-compat-end -->

Use this skill when an academic artefact must meet Ugandan university research-handbook expectations rather than generic international dissertation conventions.

Always load `source-evaluation/references/evidence-discipline.md` first. All handbook-derived requirements must remain traceable to `references/uganda-handbook-standards.md`.

## Router

| Task | Load |
|---|---|
| Concept paper or topic note | `references/uganda-handbook-standards.md` sections "Concept papers" and "Source register" |
| Research proposal | `references/uganda-handbook-standards.md` sections "Proposal structure", "Formatting", "Ethics", "Citation" |
| Dissertation / thesis / report | `references/uganda-handbook-standards.md` sections "Final research document", "Chapter structures", "Viva and examination" |
| Viva / oral defence preparation | `references/uganda-handbook-standards.md` section "Viva and examination" + `academic-reporting-standards/references/viva-defense-preparation.md` |
| Research dissemination | `references/uganda-handbook-standards.md` sections "Busitema" and "Final research document" |

## Operating Rules

1. Identify the target institution first: Makerere, Busitema, UCU, or another Ugandan institution.
2. Apply the exact institutional rule where the handbook provides one; do not merge conflicting institutional limits.
3. If the institution is unknown, use the "Uganda default scaffold" from the reference and mark institution-specific format as a gap.
4. Keep proposal tense future-oriented and final report/thesis tense past-oriented unless the discipline requires otherwise.
5. Require a clear research problem, purpose/objectives, research questions or hypotheses, significance, scope, literature gap, methodology, ethics, work plan, budget where required, and references.
6. For thesis/dissertation/report review, check both structure and examination readiness: contribution, literature depth, method fit, data analysis, discussion, conclusion, references, appendices, and viva defensibility.
7. For health, human-subject, or sensitive research, require REC/ethics routing before data collection.

## Companion Skills

- `academic-reporting-standards` for examiner-defensible dissertation logic and reporting checklists.
- `academic-writing` for citation, paraphrase, plagiarism prevention, and academic register.
- `research-design` for research design document, method selection, and report-building.
- `source-evaluation` for source credibility and anti-hallucination discipline.
