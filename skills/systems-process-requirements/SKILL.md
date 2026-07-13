---
name: systems-process-requirements
description: Use when describing a system, process, workflow, scope boundary, requirements set, interface, state model, data architecture, business rules, user journey, operating model, or design system in testable and traceable form; use spec-architect for a coding-ready feature specification.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Systems Process Requirements

<!-- dual-compat-start -->

## Use When

- Describe current or target systems, processes, requirements, states, interfaces, data, scope, or operating rules.

## Do Not Use When

- Use spec-architect for an end-to-end coding-ready feature spec and systems-thinking for causal feedback analysis.

## Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Stakeholders, purpose, boundary, current artifacts, and constraints | Owners and repository | Stop boundary-sensitive modelling and list missing authorities. |
| Rules, events, data definitions, and interfaces | Process owners and source systems | Mark unknowns; do not invent behaviour. |

## Workflow

1. Choose the artifact type and establish system boundary and owner.
2. Elicit actors, triggers, states, rules, exceptions, data, and interfaces.
3. Model traceable requirements and acceptance conditions.
4. Validate with owners or source artifacts; stop on unresolved contradictions.
5. Recover by narrowing scope and issuing a decision/gap log.

## Outputs

| Artifact | Consumer | Acceptance condition |
|---|---|---|
| Process/system model and requirements set | Owners, designers, implementers | Boundaries, branches, errors, data, rules, and traceability are observable. |

## Evidence Produced

| Category | Artifact | Acceptance condition |
|---|---|---|
| Correctness | Traceability and validation record | Each requirement maps to source, owner, and acceptance condition. |

## Capability Contract

Analysis defaults to read-only. Editing authoritative specifications or operating processes must be explicitly authorised by the owner; implementing, deploying, or changing production data requires separate explicit authorisation.

## Degraded Mode

Without owner access, current artifacts, or modelling tools, return a qualified text/table model with assumptions and unassessed decisions. Do not certify it as current-state truth or approved future state.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| Current behaviour is disputed | Preserve variants and seek owner decision | Invented consensus |
| Requirement lacks acceptance evidence | Rewrite or classify as open | Untestable scope |
| Boundary crosses another system | Document interface and ownership | Orphan responsibility |

## Quality Standards

Models are bounded, source-traceable, testable, explicit about errors and exceptions, and understandable by their named consumer.

## Preliminary Modelling Corrections

- Modelling without a boundary. Fix: name in/out scope.
- Happy path only. Fix: add exceptions and recovery.
- Mixing current and future state. Fix: label both.
- Requirement without source. Fix: add owner/provenance.
- Diagram without definitions. Fix: add a glossary/data dictionary.

## Worked Example

For an approval workflow, identify trigger, actors, states, decision rules, rejection and timeout paths, audit data, interfaces, and acceptance tests; keep unresolved ownership in the gap log.

## References

- [Modelling router](references/modeling-router.md)
- [Process and system description](references/process-system-description.md)
- [Requirements and scope](references/requirements-and-scope.md)
- [Data architecture](references/data-architecture-modeling.md)
- [Design-system documentation](references/design-system-documentation.md)
- [Source register](references/source-register.md)

<!-- dual-compat-end -->

Use this skill when the engine must explain how something works, how it should work, what its boundaries are, what users/stakeholders need, what data/entities it handles, what rules constrain it, or how its components/processes fit together.

This skill is for both research and delivery work: institutional process descriptions, market/industry operating models, system requirements, workflow documentation, data architecture notes, design-system inventories, software specifications, implementation scope, and current-state/future-state analysis.

## Mandatory Pairings

- Run `source-evaluation` for any source-backed description.
- Run `critical-reasoning-and-argument` for every claim about why a system behaves as it does, what causes a process failure, which requirements matter, or what should change.
- Run `data-quality-assessment` when the description relies on datasets, reports, or operational data.

## First Decision: What Is Being Described?

| Need | Primary artifact | Load |
|---|---|---|
| External boundary of a system | Context diagram, actors, interfaces, data flows | `references/process-system-description.md` |
| Process or workflow | Swimlane, trigger, preconditions, steps, branches, exceptions | `references/process-system-description.md` |
| Requirements set | Business/user/functional/nonfunctional/interface/data requirements | `references/requirements-and-scope.md` |
| Project/product scope | In-scope/out-of-scope, assumptions, constraints, WBS, change control | `references/requirements-and-scope.md` |
| Data architecture | Entities, attributes, synonyms, definitions, relationships, data dictionary | `references/data-architecture-modeling.md` |
| Design system | Tokens, components, patterns, usage rules, contribution model, governance | `references/design-system-documentation.md` |
| Multi-artifact documentation | Router across all artifact types | `references/modeling-router.md` |
| Source provenance for this skill | Local book register | `references/source-register.md` |

## Universal Workflow

1. **Name the system of interest.** State what is inside the system and what is outside it.
2. **Identify stakeholders and users.** Separate decision-makers, operators, end users, maintainers, regulators, upstream systems, downstream systems, and excluded groups.
3. **Define purpose and outcomes.** Explain what the system/process exists to accomplish and how success will be judged.
4. **Set the boundary.** Record scope, interfaces, inputs, outputs, assumptions, constraints, and exclusions.
5. **Model current state.** Describe what happens now using process steps, states, data flows, actors, rules, and exceptions.
6. **Elicit needs and pain points.** Use interviews, observation, documents, logs, complaints, prototypes, analytics, and source review. Do not treat requirements as merely "gathered"; they are discovered, invented, negotiated, and validated.
7. **Analyze and decompose.** Convert broad needs into business requirements, user requirements, functional requirements, nonfunctional requirements, interface requirements, data requirements, business rules, and acceptance criteria.
8. **Represent visually when useful.** Use context diagrams, process maps, swimlanes, state tables, event-response tables, use cases, user stories, data models, component inventories, or traceability matrices.
9. **Validate with stakeholders/evidence.** Review for correctness, completeness, ambiguity, feasibility, testability, and missing edge cases.
10. **Create traceability.** Every requirement, process step, data entity, rule, interface, and component needs an owner/source, rationale, status, and downstream test/design link where relevant.

## Good Description Standard

Descriptions must be:

- **Bounded:** the reader can see what is inside and outside the system.
- **Operational:** actors, triggers, steps, decisions, data, rules, and outcomes are concrete.
- **Testable:** requirements and acceptance criteria can be verified.
- **Traceable:** every claim has a source, owner, or evidence trail.
- **Change-aware:** assumptions, constraints, dependencies, risks, and change-control points are explicit.
- **Reader-fit:** executives get decisions and implications; implementers get detail; researchers get method and evidence; users get workflows.

## Common Artifacts

Use the lightest artifact that explains the system without hiding important complexity:

- Context diagram narrative.
- Stakeholder register.
- SIPOC-style supplier-input-process-output-customer summary.
- Swimlane workflow.
- Event-response table.
- State-transition table.
- Use case or user story set.
- Functional/nonfunctional/interface/data requirements list.
- Business rules catalogue.
- Scope statement and out-of-scope list.
- Requirements traceability matrix.
- Conceptual data model and data dictionary.
- Design-system component inventory.
- Current-state / future-state comparison.

## Extended Modelling Failure Modes

- Treating "requirements gathering" as passive note-taking.
- Describing UI clicks before explaining the user goal and system responsibility.
- Process narrative with no trigger, actor, exception, or outcome.
- Requirements with no source, rationale, priority, owner, or acceptance criterion.
- Nonfunctional requirements like "fast", "secure", or "user-friendly" without measurable fit criteria.
- Scope document with no exclusions or change-control rule.
- Data model with entities but no definitions, synonyms, attributes, or source.
- Design-system inventory with components but no usage rules, examples, governance, or versioning.
- Future-state recommendation that does not distinguish requirement, design choice, and implementation task.

## Universal Ship Gate

- [ ] System/process boundary stated.
- [ ] Stakeholders, users, upstream systems, and downstream systems identified.
- [ ] Purpose, success criteria, constraints, assumptions, and exclusions stated.
- [ ] Current state described before future state unless the task is greenfield.
- [ ] Requirements classified by type.
- [ ] Process steps include trigger, actor, system response, data, rule, branch, exception, and outcome where relevant.
- [ ] Nonfunctional requirements are measurable.
- [ ] Data entities have definitions, attributes, synonyms, relationships, and source.
- [ ] Business rules are separated from requirements and design choices.
- [ ] Traceability exists from source/stakeholder -> requirement/process/data/rule -> test/design/output.
- [ ] Open questions and gaps are explicit, not hidden.

## Companion Skills

- `project-requirements` - SaaS/product requirements interviews and project documentation.
- `spec-architect` - feature-level specs and SRS sections.
- `research-design` - formal research framing and system/process studies.
- `research-techniques` - gap analysis, crosswalk matrices, and synthesis.
- `report-and-proposal-craft` - formal reports and proposals describing systems/processes.
- `business-writing` - shorter memos or process notes.
- `data-quality-pipeline` and `data-quality-assessment` - when operational data and data governance are central.
- `executive-communication` - executive version of system/process findings.
- `critical-reasoning-and-argument` - causal diagnosis, recommendations, prioritization, and tradeoff logic.

## Anti-Patterns

- Modelling without a boundary. Fix: name in-scope and out-of-scope elements.
- Documenting only the happy path. Fix: add errors, exceptions, and recovery.
- Mixing current and future state. Fix: label each model.
- Writing requirements without provenance. Fix: name the owner or source.
- Drawing entities without definitions. Fix: add a glossary and data dictionary.
