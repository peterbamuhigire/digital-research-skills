# Modeling Router

Use this reference to choose the right artifact for describing a system, process, workflow, scope, or requirements set.

## Artifact Selection

| Question | Use | Captures |
|---|---|---|
| Where does the system start and stop? | Context diagram narrative | Boundary, external actors, systems, data flows |
| Who participates and what do they want? | Stakeholder register | Role, interest, decision power, pain point, evidence source |
| What happens step by step? | Swimlane workflow | Actor, action, system response, branch, exception |
| What event triggers what response? | Event-response table | State, trigger, response, business rule, acceptance test |
| What statuses can an object have? | State-transition table | State, valid transition, trigger, guardrail, forbidden transition |
| What must the product/system do? | Requirements catalogue | Requirement ID, type, statement, rationale, priority, source |
| What constrains the work? | Scope statement | In/out, assumptions, constraints, dependencies, change control |
| What data exists? | Conceptual data model | Entity, attribute, relationship, synonym, definition, source |
| What reusable UI/UX structure exists? | Design-system inventory | Token, component, pattern, usage rule, version, owner |
| How do findings trace forward? | Traceability matrix | Source -> requirement -> design -> test -> output |

## Progressive Description

For complex systems, build in this order:

1. Purpose and boundary.
2. Stakeholders and users.
3. External systems and interfaces.
4. Process/workflow.
5. Data/entities.
6. Business rules.
7. Requirements.
8. Quality attributes.
9. Acceptance criteria.
10. Traceability and open issues.

## Detail Levels

- **Executive:** purpose, boundary, pain points, options, risks, next decisions.
- **Research:** evidence sources, method, current-state model, causal diagnosis, limits.
- **Product/engineering:** requirements, interfaces, data model, state rules, acceptance criteria.
- **Operations:** workflow, roles, handoffs, exceptions, controls, metrics.
- **Design:** user journeys, components, tokens, interaction patterns, content rules.

## Stop Rule

Stop adding artifacts when the remaining complexity is visible and governable. Do not create diagrams or matrices for their own sake.
