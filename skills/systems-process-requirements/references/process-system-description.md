# Process And System Description

Use this reference to describe current-state or future-state systems, operating models, workflows, handoffs, interfaces, states, and controls.

## System Boundary

Start with:

- System of interest.
- Purpose.
- Users and external actors.
- Upstream systems.
- Downstream systems.
- Inputs.
- Outputs.
- Interfaces.
- Data exchanged.
- Exclusions.

For research reports, state whether the model is based on observation, documents, interviews, system logs, or synthesis.

## Context Diagram Narrative

Even without drawing a diagram, write:

| External actor/system | Sends to system | Receives from system | Interface/channel | Source/evidence |
|---|---|---|---|---|

Do not describe internal steps in a context diagram. Its job is boundary and exchange.

## Workflow / Swimlane Template

| Step | Actor/lane | Trigger/input | Action | System response | Data created/changed | Rule/control | Exception |
|---|---|---|---|---|---|---|---|

Each workflow also needs:

- Preconditions.
- Start trigger.
- End state.
- Alternate paths.
- Error paths.
- Metrics.
- Owner.

## Event-Response Table

Use when a process is driven by events:

| State/precondition | Event | Actor/source | Response | Data/rule | Acceptance test |
|---|---|---|---|---|---|

## State-Transition Table

Use for entities with statuses:

| Entity | Current state | Trigger | New state | Allowed? | Guard condition | Notes |
|---|---|---|---|---|---|---|

Also list forbidden transitions. They are often as important as allowed transitions.

## Current-State / Future-State Comparison

| Dimension | Current state | Problem/pain | Future state | Requirement or action |
|---|---|---|---|---|

Useful dimensions:

- Actor.
- Step.
- System.
- Data.
- Rule.
- Control.
- Handoff.
- Time/cost.
- Error/failure mode.
- User experience.

## Failure And Control Analysis

For each process failure:

- Where does it occur?
- Who detects it?
- What evidence proves it occurs?
- What is the cause? Mark inference where needed.
- What control prevents, detects, or corrects it?
- What requirement or process change follows?

## Ship Gate

- [ ] Boundary and external actors are clear.
- [ ] Inputs and outputs are named.
- [ ] Steps are actor-specific.
- [ ] Triggers and end states are explicit.
- [ ] Exceptions and alternate paths are included.
- [ ] Data and business rules are attached to steps.
- [ ] Current-state evidence is traceable.
- [ ] Future-state changes are labelled as recommendations or requirements, not facts.
