# Requirements And Scope

Use this reference for requirements writing, requirements analysis, project/product scope, acceptance criteria, baselines, and traceability.

## Requirements Types

| Type | Describes | Example form |
|---|---|---|
| Business requirement | Why the organization is undertaking the work | Objective, outcome, value, constraint |
| User requirement | What a user must be able to accomplish | Use case, scenario, user story |
| Functional requirement | What the system shall do | Testable capability statement |
| Nonfunctional requirement | How well the system must perform or behave | Quality attribute with measurable fit criterion |
| Interface requirement | How systems/users/devices exchange data or signals | API, UI, hardware, software, communication interface |
| Data requirement | What data is captured, stored, transformed, governed, or reported | Entity, attribute, validation, lineage |
| Business rule | Policy, calculation, condition, or constraint that governs behavior | Rule statement with owner and source |
| Constraint | Limit on solution, method, cost, schedule, technology, regulation | Must/must not boundary |

## Good Requirement Test

A requirement should be:

- Accurate.
- Atomic.
- Complete.
- Concise.
- Consistent.
- Feasible.
- Necessary.
- Prioritized.
- Traceable.
- Unambiguous.
- Verifiable.

Avoid bundling multiple requirements into one sentence.

## Elicitation Sources

Use multiple sources, then reconcile contradictions:

- Stakeholder interviews.
- Workshops/JAD sessions.
- Observation/shadowing/Gemba.
- Existing documents and policy manuals.
- Logs, tickets, complaints, support records.
- Existing systems and reports.
- Market/competitor/regulatory research.
- Prototypes and usability tests.
- Scenarios, events, and edge-case walkthroughs.

## Scope Template

Record:

- Problem/opportunity.
- Product/system vision.
- Objectives and success criteria.
- In scope.
- Out of scope.
- Stakeholders and decision rights.
- Assumptions.
- Constraints.
- Dependencies.
- Risks.
- Deliverables.
- Acceptance/verification method.
- Change-control rule.

## Acceptance Criteria

Use acceptance criteria to make requirements testable:

- Given a precondition/state.
- When an event/action occurs.
- Then the system/process response is observable.

Include functional behavior, relevant business rules, data validation, exception handling, and nonfunctional expectations.

## Managing Scope Creep

Scope change is not automatically bad. It becomes failure when unmanaged.

For each change:

- Name the request source.
- Link to business objective or stakeholder need.
- Identify affected requirements, data, workflows, tests, cost, schedule, risk, and documentation.
- Decide: accept, defer, reject, split, or investigate.
- Update baseline and traceability if accepted.

## Traceability Matrix

Minimum columns:

| Source/owner | Requirement ID | Type | Requirement | Rationale | Priority | Status | Design/test link | Notes |
|---|---|---|---|---|---|---|---|---|

Use persistent IDs. Do not rely only on outline numbering because numbers change as requirements are inserted or deleted.

## Ship Gate

- [ ] Requirements are classified by type.
- [ ] Each requirement has one source/owner and one rationale.
- [ ] Nonfunctional requirements are measurable.
- [ ] Business rules are separated from functional requirements.
- [ ] Interfaces and data requirements are explicit.
- [ ] Scope exclusions are stated.
- [ ] Acceptance criteria exist for buildable requirements.
- [ ] Baseline/change-control rule exists.
- [ ] Traceability matrix links source -> requirement -> design/test.
