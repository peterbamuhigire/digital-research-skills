---
name: systems-thinking-and-mental-models
description: Use when analysing system behaviour, stakeholder dynamics, root causes, feedback loops, leverage points, or judgement under uncertainty with systemigrams, causal loops, mental models, or decision heuristics; use systems-process-requirements for normative process or requirements documentation.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
  priority: high
---

# Systems thinking and mental models

<!-- dual-compat-start -->

## Use When

- Analyse observed behaviour through stakeholders, feedback, root causes, leverage points, base rates, or judgement heuristics.

## Do Not Use When

- Use systems-process-requirements to prescribe a workflow or requirements set.

## Inputs

| Input | Source/provider | If absent |
|---|---|---|
| Focal behaviour, boundary, timeframe, actors, and evidence | Research brief and verified corpus | Stop mapping and define the missing frame. |
| Competing explanations and uncertainties | Analysts and sources | Mark the map provisional and seek counterevidence. |

## Workflow

1. Define behaviour over time, boundary, and decision.
2. Choose one toolkit based on the question.
3. Map evidence separately from inference; test feedback and alternatives.
4. Stop if causal direction is unsupported; recover with a hypothesis/gap map.
5. Validate implications and limitations before recommending intervention.

## Outputs

| Artifact | Consumer | Acceptance condition |
|---|---|---|
| System map or decision-analysis record | Analyst and decision-maker | Boundary, evidence, inferred links, alternatives, leverage points, and limits are explicit. |

## Evidence Produced

| Category | Artifact | Acceptance condition |
|---|---|---|
| Correctness | Evidence-to-link register | Every factual node/link has a source; inference is labelled. |

## Capability Contract

Analysis defaults to read-only. Stakeholder contact, data collection, intervention, policy change, or publication requires explicit authority.

## Degraded Mode

With sparse time-series, stakeholder, or causal evidence, return a qualified provisional map with unsupported links and unassessed checks labelled as hypotheses. Do not claim causality or predict outcomes.

## Decision Rules

| Choice | Action | Failure/risk avoided |
|---|---|---|
| Stakeholder flows dominate | Use a systemigram | Actor relationships hidden |
| Feedback over time dominates | Use causal loops | Static root-cause story |
| Forecast judgement dominates | Use base rates and calibration | Inside-view bias |

## Quality Standards

The map distinguishes observation from inference, includes countercases, states its boundary, and avoids causal claims unsupported by evidence.

## Anti-Patterns

- Drawing arrows without evidence. Fix: label hypotheses.
- Treating a map as reality. Fix: state boundary and omissions.
- Finding one root cause. Fix: test feedback and alternatives.
- Recommending a leverage point without side effects. Fix: model counter-response.
- Ignoring base rates. Fix: compare the reference class.

## Worked Example

For recurring service delays, map observed queue behaviour and stakeholder flows, label suspected reinforcing loops as hypotheses, test alternative causes, and recommend no intervention until the critical link is supported.

## References

- [Systemigrams](references/systemigrams.md)
- [Causal loops and leverage points](references/causal-loops-and-leverage-points.md)
- [Mental-model catalogue](references/mental-models-catalog.md)
- [Decision-science heuristics](references/decision-science-heuristics.md)

<!-- dual-compat-end -->

The engine handles complex, interlinked, often political domains: regulatory landscapes, organisational pain points, market dynamics, academic synthesis. None of these reduce to a flat list of facts — they have structure, feedback, and observer effects. This skill gives the analyst four toolkits and a router for picking the right one.

## When to invoke this skill

- The research question is about *how* something works, not just *what* exists
- Stakeholders are entangled and the question is "what is really going on?"
- A linear list of pain points doesn't capture the relationships
- The user asks for "root cause", "system map", "stakeholder dynamics", "feedback loops", "leverage points"
- Analyst reasoning is about to commit to a position and needs a discipline check (mental-models catalog)
- Forecasting or judgement is being made under uncertainty (decision-science heuristics)

## The router

| If the question is about… | Use | Load |
|---|---|---|
| **Stakeholder/system behaviour mapping** — who does what to whom, what flows where | Systemigram (Boardman & Sauser) | `references/systemigrams.md` |
| **Dynamics and policy** — why does this system produce this behaviour over time; where would intervention work | Causal loop diagrams + Meadows leverage points + Iceberg | `references/causal-loops-and-leverage-points.md` |
| **Analyst reasoning checklist** — am I using the right mental model on this problem | Mental-models catalog | `references/mental-models-catalog.md` |
| **Prediction / judgement under uncertainty** — bias control, base rates, calibration | Decision-science heuristics | `references/decision-science-heuristics.md` |

Most non-trivial work loads two of these. A regulatory landscape map is often **systemigram + causal loops**. A pain-point analysis is often **causal loops + mental models**. A forecast is **mental models + decision science**. The router is not exclusive — it sequences.

## The four toolkits in one paragraph each

### Systemigrams (behaviour/stakeholder maps)

Boardman & Sauser's systemigram method takes a **structured prose description of a System of Interest (SoI)**, extracts the **noun phrases as nodes** and the **verb/preposition phrases as directed arrows**, and arranges them so the principal subject is at top-left, the principal object at bottom-right, and the **mainstay** flow runs diagonally between them. **Arrows do not cross.** The systemigram is iterated — early versions fail, and the failures reveal which connections actually matter. Best when the question is "how does this system fit together" and you need stakeholders + flows in one picture.

### Causal loop diagrams, Meadows, Iceberg

Stocks accumulate; flows change them; feedback loops either reinforce (R) the change or balance (B) it. The **Iceberg Model** (anon., Chapter 6) layers reality: events → patterns → structure → mental models, with leverage growing as you go deeper. Donella Meadows-style **leverage points** rank where to intervene in a system; high-leverage points often live in the deeper layers (rules, goals, paradigms) rather than the surface (parameters, buffers). Best when the question is *why is this happening over and over?* and you need to choose where to push.

### Mental-models catalog (analyst reasoning)

A mental model is a structured way of looking at a problem. The catalog (drawn from "Thinking in Systems and Mental Models" Part 2) gives the analyst a **checklist of frames** to apply: first principles, inversion, second-order effects, opportunity cost, base rates, regression to the mean, signal vs noise, and so on. Best as a discipline before committing to an analysis: *which of these should I have used and didn't?*

### Decision-science heuristics

Brockman's *Thinking* anthology is a non-systematic but powerful collection of insights from Kahneman, Gigerenzer, Pinker, and others on how human judgement actually works — and where it predictably fails. The reference distils the operationalisable parts: when to trust intuition (Gigerenzer's environments), when to actively distrust it (Kahneman's System 1 traps), what calibration looks like, and how to pre-mortem a forecast. Best when an output asserts a probability, prediction, or judgement under uncertainty.

## Universal anti-patterns across the four toolkits

- Drawing a "system map" that is just a labelled grouping of items, not a flow graph
- Causal loops with only reinforcing loops (real systems always include balancing constraints — find them)
- Listing mental models without applying them to the specific problem
- Asserting a prediction without naming the base rate or comparable reference class
- Treating system behaviour as the result of one actor's intent (most behaviour is structural)
- Skipping the second-order effects question when proposing an intervention
- Treating a one-time event as a pattern (single-data-point reasoning)
- Mistaking correlation for a causal loop (loops are claims about feedback, not co-occurrence)

## Companion skills

- `analytic-tradecraft` — when systems analysis becomes formal estimative judgement
- `critical-reasoning-and-argument` — when arguments using systems analysis must hold up to scrutiny
- `mind-mapping-and-synthesis` — for pre-systems brainstorming and synthesis (Buzan radial maps complement systemigrams)
- `research-orchestration` — for sequencing systems analysis across waves
- `pi-investigation`, `osint-investigation` — when systems mapping concerns specific persons, organisations, or schemes
- `source-evaluation` — every claim in a system map still needs a source
