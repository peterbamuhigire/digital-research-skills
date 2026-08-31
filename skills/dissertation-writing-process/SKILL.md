---
name: dissertation-writing-process
description: Use when planning, drafting, reviewing, or formatting a dissertation from research question through defence-ready manuscript; use academic-writing for prose originality and research-design for method selection.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Dissertation Writing Process

Run dissertation work as a sequence of evidence-bearing chapters, not as a
single writing sprint. This skill covers planning, literature organisation,
chapter logic, methods, findings, discussion, references, formatting, and
responsible use of generative AI.

<!-- dual-compat-start -->
## Use When

- A thesis or dissertation needs a plan from research question to final formatting.
- A candidate has sources and notes but no defensible literature argument or chapter sequence.
- Methods, findings, and discussion need to remain aligned with research questions.
- AI assistance is being considered for drafting, editing, discovery, or analysis.

## Do Not Use When

- The task is a single citation or source check; use `source-verification`.
- The method or sampling design is the primary unresolved decision; use `research-design` first.
- The request is ordinary copy-editing without a dissertation structure; use `academic-writing`.

## Inputs

| Input | Required | Purpose |
|---|---:|---|
| Research question, contribution, and institutional rules | yes | Bound the manuscript |
| Source library and literature notes | yes | Build a traceable argument |
| Approved or proposed methodology | conditional | Align methods, results, and limitations |
| Supervisor or ethics requirements | conditional | Prevent an unapproved or unusable submission |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Dissertation production plan | Candidate and supervisor | Chapter milestones, review points, dependencies, and stop conditions are explicit |
| Chapter evidence map | Candidate and examiner | Each question links to literature, method, evidence, finding, discussion, and limitation |
| Source, citation, originality, AI-use, and final-formatting record | Candidate, supervisor, and institution | Required checks are executed or each unresolved gate is marked NOT ASSESSED |

## Non-negotiables

- Keep a literature database and annotated bibliography; do not draft from an open source window.
- Every research question must map to evidence, analysis, findings, discussion, and a limitation.
- Separate participant evidence, author interpretation, synthesis, and recommendation.
- State assumptions, delimitations, access gaps, positionality, and unresolved uncertainty.
- Follow the institution's current formatting and ethics rules; the book's workflow is not a substitute for them.
<!-- dual-compat-end -->

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Question, contribution, or audience is unclear | Stop drafting and resolve the problem frame | A fluent manuscript with no defensible contribution |
| Literature is broad but unstructured | Build the source database, annotated bibliography, and argument map first | A source catalogue without an argument |
| Method cannot produce evidence for a question | Narrow the question or redesign the method | Unsupported conclusions |
| Findings contain themes or statistics not linked to a question | Re-map the chapter before interpreting results | Interpretation detached from evidence |
| AI output affects a claim, method, analysis, or citation | Verify independently, disclose the use where required, and retain the human decision record | Unverified claims, hidden authorship, or citation error |
| Institutional rule conflicts with generic writing guidance | Follow the verified institutional rule and record the exception | Non-compliant submission |

## Workflow

1. Frame the problem, purpose, questions, significance, terms, assumptions,
   limitations, delimitations, audience, and institutional constraints.
2. Build a searchable literature database and annotated bibliography. Record
   each source's question, method, finding, limitation, relevance, and role in
   the argument.
3. Plan the introduction as context, problem, purpose, questions, significance,
   definitions, and boundaries. Choose a background shape that serves the
   reader: chronological, big-to-small, or cause-and-effect.
4. Write the literature review as an argument. Group sources by the research
   problem, theory, method, or contradiction; do not produce a source-by-source
   catalogue.
5. Write the methodology so another researcher can understand design,
   population, sampling, measures or instruments, collection, analysis,
   ethics, positionality, and limits.
6. Present findings in the order that answers the questions. Keep description
   separate from interpretation, show participant or quantitative evidence,
   and expose missing or contradictory results.
7. Use the discussion to summarise findings, integrate them with the reviewed
   literature, explain implications, state limitations, and separate practice
   recommendations from future research.
8. Manage citations continuously, then apply the institution's rules to title
   page, abstract, contents, lists, tables, figures, references, appendices,
   page numbers, and submission format.
9. Run source-away originality review, claim-source review, AI-use disclosure,
   supervisor/ethics checks, and a final question-to-conclusion trace. Stop
   before submission when a required source, ethics decision, or institutional
   rule cannot be verified; recover by recording the gap and revising the
   affected claim or chapter.

## Anti-patterns

- Writing the literature review as annotated summaries with no argument. Fix: organise by the problem, theory, method, or contradiction.
- Treating fluent AI prose as evidence of originality. Fix: draft from verified notes and run source-away review.
- Letting a method chapter promise analysis the dataset cannot support. Fix: reconcile questions, measures, access, and analysis before collection.
- Reporting findings and recommendations without a question link. Fix: label the question, evidence, interpretation, and implication.
- Treating a citation manager as proof that a source supports a claim. Fix: inspect the source and record its evidentiary role.
- Ignoring institutional formatting or ethics rules until the final day. Fix: add them as early production gates.

## Read next

- `academic-writing` for originality, synthesis, voice, and citation prose.
- `research-design` for method, case, sampling, and feasibility decisions.
- `evidence-claim-graph` for traceable claim-to-source relationships.
- `peer-review-loop` for supervisor and independent review cycles.
- `source-verification` for current or high-stakes source claims.

## References

- [Dissertation evidence workflow](references/dissertation-evidence-workflow.md)

## Capability Contract

Read and search are required. Editing is allowed for an authorised research
workflow. Execution is preferred for citation, originality, and document checks.

## Degraded Mode

If institutional rules, ethics approval, source access, or supervisor evidence
is unavailable, produce a qualified plan and mark the affected gate `NOT ASSESSED`.

## Evidence Produced

| Evidence | Acceptance condition |
|---|---|
| Chapter evidence map | Every question connects to evidence, analysis, findings, and limitations |
| Source and originality record | Claims, paraphrases, quotations, and synthesis remain distinguishable |
| Final-format and review record | Institution-specific checks are executed or explicitly unresolved |

## Quality Standards

- Every research question has a visible path to evidence, analysis, finding, discussion, and limitation.
- Literature review sections make an argument and distinguish synthesis from source summary.
- Methods expose design, sampling, instruments, analysis, ethics, positionality, and limits.
- Claims, citations, quotations, AI assistance, and unresolved uncertainty remain traceable.
- Formatting and ethics checks are verified against the institution's current requirements.

## Worked Example

For a dissertation on NGO cyber resilience, frame one question about the controls
that reduce mission harm, build an annotated source database, and map each source
to the literature argument. Select a feasible mixed-method design, show sampling
and ethics, report findings in question order, then use the discussion to connect
results to literature, limitations, and separately labelled practice recommendations.
