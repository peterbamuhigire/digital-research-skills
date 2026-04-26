---
name: primary-research
description: Use when the project cannot rely on desk research alone and needs first-hand qualitative evidence such as interviews, observation, focus groups, field visits, or coded open-ended responses. Encodes qualitative design, fieldwork discipline, coding, credibility checks, and reporting gates.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
  priority: high
---

# Primary Research

<!-- dual-compat-start -->
## Use When

- Use when the project needs first-hand qualitative evidence such as interviews, observation, focus groups, field visits, or coded open-ended responses.
- Use when desk research alone cannot answer the decision with enough fidelity.

## Do Not Use When

- The work is purely secondary-source research.
- The task is about writing up existing findings rather than designing or interpreting primary evidence.

## Required Inputs

- Decision or question the fieldwork must inform.
- Proposed respondent / setting universe and access constraints.
- Expected output form and evidence-sensitivity level.

## Workflow

- Read this `SKILL.md` first, then load only the relevant reference file for the method being used.
- Design the instrument and sampling logic before collection.
- Preserve traceability from raw material to codes, themes, and final claims.

## Quality Standards

- Sampling logic is explicit.
- Notes distinguish quote, paraphrase, observation, and inference.
- Findings are theme-based, not anecdote-based.

## Anti-Patterns

- Casual interviews with no guide.
- Treating vivid respondent anecdotes as representative evidence.
- Coding only what confirms the working theory.

## Outputs

- A defensible primary-research design, collection plan, coding approach, or interpretation with traceable claims.

## References

- Use the `references/` files for the specific method being run.
<!-- dual-compat-end -->

This skill governs evidence the engine helps design or interpret when the source is a person, a setting, or a live interaction rather than a published document.

## When to use

Use this skill when the project includes any of:

- Expert or stakeholder interviews
- Key-informant interviews
- Focus groups or small discussion groups
- Field visits, shadowing, or direct observation
- Open-ended survey responses that need coding
- Case-study field evidence beyond desk research

Do not use this skill for purely secondary-source work. Pair it with `research-orchestration`, not instead of it.

## Five rules

1. **Design before collection.** Every interview, visit, or group needs a question-set, sampling logic, and note plan before the first contact.
2. **Purposeful sampling beats convenience sampling.** The point is coverage of perspectives, not easy access alone.
3. **Raw material stays traceable.** Claims in synthesis must be recoverable to notes, transcripts, observation logs, or coded excerpts.
4. **Coding precedes conclusion.** Do not jump from striking anecdotes to findings without theme-building.
5. **Credibility is engineered.** Use triangulation, disconfirming evidence, member-checking where appropriate, and explicit limits.

## Router

| Situation | Load |
|---|---|
| Interview-led project | `references/interview-protocols.md` |
| Observation / field visit / shadowing | `references/observation-and-fieldwork.md` |
| Coding and interpreting qualitative material | `references/qualitative-coding-and-analysis.md` |
| Quality / rigor / defensibility of findings | `references/credibility-and-quality.md` |
| Longitudinal online community research | `research-design/references/mroc-design-and-management.md` |

## Workflow

1. Define the decision the fieldwork must inform.
2. Build the sample frame: who must be heard, who may be heard, who is excluded.
3. Draft the instrument: interview guide, observation sheet, or discussion prompts.
4. Collect with disciplined notes: time, setting, speaker role, direct quotes vs paraphrase.
5. Code the material into themes, contrasts, and negative cases.
6. Write findings with provenance and limits.

## Ship gate

- [ ] Research question and user of the finding are explicit.
- [ ] Sample logic is stated and defended.
- [ ] Instrument exists before collection.
- [ ] Notes distinguish quote, paraphrase, inference, and observation.
- [ ] Theme-building is visible; findings are not anecdote dumps.
- [ ] At least one disconfirming or minority view is surfaced where relevant.
- [ ] Ethics / consent / sensitivity constraints are stated.
- [ ] Every load-bearing finding is traceable back to raw material.

## Anti-patterns

- Running interviews as casual conversations with no guide
- Quoting the most vivid respondent as if they represent the population
- Treating open-ended responses as decoration instead of data
- Coding only confirming evidence
- Hiding weak samples behind strong prose

## Companion skills

- `research-orchestration` — wave planning and sub-agent brief structure
- `research-design` — case study, MROC, and formal design layer
- `source-evaluation` — published sources still need tiering
- `analytic-tradecraft` — when field evidence feeds a contested judgment
- `academic-writing` / `report-and-proposal-craft` — final artifact layer

## Sources for this skill

- Patton, Michael Quinn. *Qualitative Research & Evaluation Methods: Integrating Theory and Practice*. 4th ed., SAGE, 2015. Tier 1.
- Poynter, Ray. *The Handbook of Online and Social Media Research*. Tier 1 for MROC and online qualitative practice.
