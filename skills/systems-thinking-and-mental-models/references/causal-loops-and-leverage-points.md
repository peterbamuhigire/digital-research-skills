# Causal loops, the Iceberg Model, and leverage points

**Date written:** 2026-04-27
**Drawn from:** *Thinking in Systems and Mental Models* (anonymous primer), Part 1 (Chapters 5–9 in particular: System Models, the Iceberg Model, Four Steps to Solve Any Problem, System Archetypes); Donella Meadows' framework as referenced in that primer.

This reference covers the dynamics half of systems thinking: why a system produces the behaviour it does over time, and where intervention has real leverage. Use it when the question is *not* "who does what to whom" (that's `systemigrams.md`) but *why does this keep happening?*

## The Iceberg Model — four levels of system reality

The primer lays out the Iceberg as the entry point to systems analysis:

| Level | Question | Leverage |
|---|---|---|
| **Events** | What just happened? | Low — fix this event |
| **Patterns / trends** | What has been happening over time? | Medium — change behaviour going forward |
| **Structure (systemic)** | What is the underlying structure that produces these patterns? | High — re-engineer the system |
| **Mental models / paradigms** | What deeply-held beliefs make this structure feel inevitable? | Highest — shift the paradigm |

Most analysis stops at events. The Iceberg pushes the analyst to look beneath:

- A pothole on a road is an *event*
- A road that always has potholes is a *pattern*
- A road maintenance system that funds emergency repairs but not preventive resurfacing is the *structure*
- A belief that "we deal with problems when they appear" is the *mental model*

The deepest sustainable interventions act on structure or paradigm. The cheapest reversible interventions act on events. Knowing which level a recommendation operates on is half the battle.

## Stocks and flows (the building blocks)

A **stock** is anything that accumulates over time: water in a reservoir, money in an account, trust in an institution, undischarged technical debt, customer goodwill, regulatory backlog.

A **flow** is anything that changes a stock: rainfall and evaporation, deposits and withdrawals, kept promises and broken ones, code shipped and bugs filed.

Two analytic moves:

1. **Identify the stock** the system is meant to grow, protect, or drain
2. **Identify the flows** that fill or empty it — and what governs each flow

System behaviour over time is driven by the relative rates of inflow and outflow on the relevant stocks.

## Feedback loops

A feedback loop exists when a change in a stock affects the rate of one of its flows.

### Reinforcing (R) loops — virtuous or vicious cycles

A reinforcing loop amplifies change. More leads to more; less leads to less.

- *Profitability → reinvestment → capability → profitability* (virtuous)
- *Distrust → defection → distrust* (vicious)

The primer (Chapter 4 illustration of organizational profitability) frames reinforcing loops as the engine of compound growth or decay.

### Balancing (B) loops — homeostasis and constraint

A balancing loop resists change. When the stock departs from a target, the flows act to bring it back.

- *Thirst → drinking → reduced thirst*
- *Inventory rises → orders fall → inventory falls back*

Balancing loops give a system its stability — *and* its resistance to intervention. A "sticky" problem usually has a balancing loop the proposed intervention has not noticed.

### Reading a system's behaviour from its loops

| Behaviour over time | Likely loop structure |
|---|---|
| Exponential growth or collapse | Dominant reinforcing loop |
| Goal-seeking / settling to equilibrium | Dominant balancing loop |
| Oscillation | Balancing loop with a delay |
| S-shaped growth | Reinforcing loop that hits a balancing constraint |
| Drift to low performance | Slowly-eroding goal in a balancing loop |

## Drawing a causal loop diagram (CLD)

Steps:

1. **Define the variable of interest** — the thing whose behaviour over time the analyst wants to explain
2. **Plot the behaviour over time** (even informally) — exponential? oscillating? S-shaped?
3. **Identify the connected variables** that affect the variable of interest
4. **Draw arrows** with polarity — `+` when the cause and effect move in the same direction, `−` when in opposite directions
5. **Close the loops** — every causal arrow eventually returns; the loop is either reinforcing (R) or balancing (B)
6. **Label each loop** with its type and a name (e.g., "R1: trust spiral", "B2: capacity ceiling")
7. **Add delays** where there is a meaningful lag between cause and effect (oscillation almost always involves a delay)
8. **Stress-test** by simulating in your head: if X rises, does the diagram predict the observed behaviour?

A CLD that does not predict the actually-observed behaviour is wrong about a polarity, missing a loop, or missing a delay. Iterate.

## System archetypes

The primer (Chapter 8) names the recurring loop structures that show up across domains. Common archetypes:

- **Limits to growth** — a reinforcing growth loop runs into a balancing limit; behaviour goes S-shaped or collapses
- **Shifting the burden** — a quick fix relieves symptoms but weakens the capacity for fundamental fix; addiction-shaped dynamic
- **Tragedy of the commons** — multiple actors drawing from a shared stock; individual rationality collapses the stock
- **Fixes that fail / fixes that backfire** — the intervention's second-order effects undo or worsen the original problem
- **Eroding goals / drift to low performance** — the standard slowly drops to match observed performance
- **Success to the successful** — winners get more resources, become more successful, lock in advantage
- **Escalation** — two parties' balancing-relative-to-the-other behaviour produces an arms race

Recognising the archetype shortcuts the diagnosis. Many "novel" problems are recognisable archetypes in unfamiliar dress.

## Leverage points (Meadows-style)

Donella Meadows' insight: *not all interventions are equal*. Some intervention points produce huge change; others are almost cosmetic. Roughly ranked from low leverage to high leverage:

| Lower leverage | Higher leverage |
|---|---|
| Constants, parameters, numbers (taxes, subsidies, buffer sizes) | Goals of the system |
| The size of buffers and stocks relative to flows | The mindset / paradigm out of which the system arises |
| The structure of material stocks and flows | The power to transcend paradigms |
| The length of delays | |
| The strength of negative feedback loops | |
| The strength of positive feedback loops | |
| The structure of information flows (who can see what) | |
| The rules of the system (incentives, punishments, constraints) | |
| The power to add, change, evolve, or self-organise system structure | |

The order matters: tweaking a parameter is often pointless while a bad rule or a bad paradigm dominates. **Most political and organisational reform fails because it intervenes at low leverage.**

## Four-step problem solving (the primer, Chapter 7)

A simple operating loop the engine can use:

1. **Identify the problem** at the right level (Iceberg) — event, pattern, structure, paradigm
2. **Map the system** — stocks, flows, loops, delays, archetype if present
3. **Locate leverage points** — where intervention would actually move the system
4. **Design the intervention** at the highest practical leverage; pre-mortem the second-order effects

## When to use this in engine work

- A pain-point taxonomy that is full of recurring complaints (look for archetypes)
- A regulatory landscape where reform attempts have failed (look at leverage)
- An organisational diagnosis that names symptoms but no structural causes
- A market analysis where competitor behaviour seems "irrational" (often a loop)
- Any problem that has been "solved" repeatedly without the underlying behaviour changing

## Anti-patterns

- Diagnosing at the event level when the pattern is what matters
- Listing factors without specifying polarity (the diagram is uninterpretable without `+`/`−`)
- Drawing only reinforcing loops (real systems always have constraints — find them)
- Treating an arrow as causal because two variables move together (correlation ≠ feedback)
- Recommending a parameter change when the dominant loop is structural
- Skipping delays (oscillation and overshoot are almost always about delay)
- Calling something "the system's goal" when it's actually one stakeholder's preference
- Naming an archetype without checking whether the loop polarities actually match
