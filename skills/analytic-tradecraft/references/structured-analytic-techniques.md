# Structured Analytic Techniques

Use this guide to choose and run a structured analytic technique when a judgment is contested,
high-stakes, inherited, forward-looking or about an adversary's behaviour. Each technique has a
trigger, steps, output and pitfalls; the selection table at the end maps situations to techniques.

## Inputs

- The judgment or question in one sentence.
- The evidence set with source tiers (`source-verification`).
- The people available: a technique that needs a devil's advocate or a second team needs named
  people with standing.
- The decision deadline, which limits how many techniques are affordable.

## Techniques (engine-priority subset)

Each technique is documented with four fields: **trigger**, **steps**, **output**, **pitfalls**. The engine implements a runnable mini-protocol for each.

---

### Analysis of Competing Hypotheses (ACH)

**Trigger.** Contested evidence; multiple plausible accounts of the same event; whenever a single dominant hypothesis is forming.

**Steps.**
1. Brainstorm the full set of hypotheses, including unlikely ones. (Include at least one denial-and-deception hypothesis if adversary action is plausible.)
2. List all evidence and assumptions, including the absence of expected indicators.
3. Build a matrix scoring each piece of evidence against each hypothesis: **C** (consistent), **I** (inconsistent), **N** (not applicable / not diagnostic).
4. Focus on **disconfirming** evidence — eliminate hypotheses with the most inconsistencies, not confirm those with the most consistencies.
5. Sensitivity-test: how much does the conclusion depend on a few critical pieces of evidence? If those pieces were wrong, would the ranking flip?
6. Report the surviving hypotheses with their relative likelihood, and identify the diagnostic gaps that would change the ranking if filled.

**Output.** Matrix attached to the judgment; ranked hypotheses with relative likelihood; named diagnostic gaps.

**Pitfalls.** Garbage-in (a poor or biased hypothesis set produces a confident wrong answer). ACH treated as confirmation theatre (analyst marks evidence "consistent" with the hypothesis they already hold, ignoring inconsistencies). Ignoring weight / diagnosticity (some evidence is more diagnostic than others; weight accordingly). Treating the absence of expected indicators as proof of concealment, instead of testing "the thing is not there" as a hypothesis in its own right.

---

### Key Assumptions Check (KAC)

**Trigger.** Inherited assumptions; "everyone knows" claims; long-running judgments with unchanged premises; whenever the analyst notices "we have always thought…".

**Steps.**
1. List every load-bearing assumption underlying the current judgment.
2. For each, ask: what new evidence would falsify this assumption?
3. Re-examine all available data through the inverse of each assumption.
4. Flag any assumption that turns out not to be challengeable (no falsifying evidence is even imaginable) — that is dogma, not analysis.
5. Re-test the judgment on the surviving (challenged-and-held) assumptions.

**Output.** Assumption ledger attached to the judgment, with "challenged on what basis" for each.

**Pitfalls.** Listing only the assumptions that are easy to challenge. Confusing premise with conclusion. Failing to consider that the question itself rests on an assumption (e.g. "should we cut prices?" assumes pricing is the variable that matters).

---

### Devil's Advocacy

**Trigger.** Strong consensus on a high-stakes call; "can't afford to get wrong" issues; when the analytic team notices it has stopped disagreeing.

**Steps.**
1. Assign a named analyst (or sub-team) to argue the best contrary case.
2. The advocate marshals all disconfirming evidence and attacks the load-bearing assumptions.
3. The contrary memo is prepared at full effort and submitted alongside the main judgment.
4. The decision-maker reads both.

**Output.** Contrary memo or "box" inside the estimate; not a footnote.

**Pitfalls.** Token / pro-forma exercise. Advocate without standing or budget. Advocate selected from team members least likely to disrupt — defeats the purpose. The advocate needs enough standing that the contrary case is actually heard.

---

### Team A / Team B

**Trigger.** Paradigm-level disagreement; when one mindset dominates an account; high-stakes calls where the cost of being wrong is structural, not tactical.

**Steps.**
1. Two named teams, same evidence pool, different priors.
2. Each team conducts independent analysis.
3. Structured face-off (oral or written).
4. Adjudication by the customer or by a designated chair.

**Output.** Two competing estimates, presented in parallel; adjudication note.

**Pitfalls.** Politicisation. A second team stacked with people committed to the opposite answer produces advocacy, not analysis. Teams must be selected for analytic capability and genuinely different priors, not for predetermined conclusions.

---

### Red Cell

**Trigger.** Adversary or competitor action under consideration; D&D suspected; warning problems; whenever "what would they do?" is load-bearing.

**Steps.**
1. Immerse a named analyst (or team) in the adversary's worldview, written record, and decision constraints.
2. Plan from the adversary's perspective.
3. Identify what the adversary would want US (the analytic side) to believe.
4. Reverse-engineer the collection gaps that would let the adversary's preferred narrative dominate.

**Output.** Adversary-perspective estimate; named indicators of D&D operating against our collection.

**Pitfalls.** Mirror-imaging dressed up as red-celling — analyst projects own rationality onto adversary. Insufficient immersion (the adversary's actual writing, doctrine, history must be read, not paraphrased).

---

### Pre-Mortem

**Trigger.** Before any high-stakes ship; before final synthesis; before recommendation.

**Steps.**
1. Imagine that, six months from now, the judgment has turned out catastrophically wrong.
2. Write a one-page memo explaining what happened.
3. Identify the load-bearing assumptions or evidence that turned out to be wrong.
4. Add the named indicators that would have warned us in time.
5. Decide whether the judgment ships as-is, ships with caveats, or returns to analysis.

**Output.** Pre-mortem memo attached to the judgment; warning indicators added to ongoing monitoring.

**Pitfalls.** Tokenism. Pre-mortem run after the judgment is politically committed (too late to do real work).

---

### What-If Analysis

**Trigger.** A high-impact, low-baseline-probability event; an outcome the team is reluctant to consider.

**Steps.**
1. Assume the unwelcome event has already happened.
2. Work backward to identify the pathway by which it could have happened.
3. Identify the warning indicators that would have appeared along the pathway.
4. Decide which indicators are now monitorable.

**Output.** Pathway memo; monitorable indicators.

---

### High-Impact / Low-Probability

**Trigger.** Tail risks (regime collapse, competitor exit, regulator reversal, WMD use). Risks the customer is least prepared to consider.

**Steps.**
1. Identify the wild card.
2. Construct a plausible pathway from current state to the wild-card outcome.
3. List signposts and tipping points along the pathway.
4. Quantify impact (financial, operational, reputational) at each tipping point.

**Output.** Scenario brief with indicators and impact bands.

---

### Indicators-and-Warning

**Trigger.** Continuous monitoring of any judgment that depends on conditions remaining roughly stable.

**Steps.**
1. List the indicators that would signal the judgment is starting to break (drawn from KAC, Pre-Mortem, What-If).
2. Set monitoring thresholds.
3. Schedule re-checks on a cadence appropriate to the risk.
4. When an indicator trips, re-run the relevant SAT.

**Output.** Indicator list with thresholds and re-check schedule; trip log.

**Pitfalls.** Moving the warning threshold each time it is reached ("not yet, wait for X; now wait for Y") until the event happens. Pre-commit to thresholds before evidence pressure builds.

---

### Argument Mapping / Signpost Analysis

**Trigger.** Long-form judgment with many supporting claims; whenever an analyst feels "this argument is right but I can't show why".

**Steps.**
1. Decompose the conclusion into the chain of premises supporting it.
2. For each premise, decompose into the evidence supporting it and the assumption underlying it.
3. Visualise the chain (tree or list).
4. Identify nodes where the chain is weakest.

**Output.** Argument map; identified weak nodes for re-research or re-thinking.

**Pitfalls.** Mapping itself becomes the deliverable; the analytic work the map was supposed to surface gets deferred.

---

## When to deploy which technique

| Situation | First technique | Then |
|---|---|---|
| Contested evidence, multiple accounts | ACH | KAC on the surviving hypotheses |
| Strong consensus, high stakes | Devil's Advocacy or Pre-Mortem | KAC; consider Team A/B |
| Forecast / future-state | What-If + High-Impact/Low-Probability | Indicators-and-Warning |
| Adversary / competitor action | Red Cell | ACH including a D&D hypothesis |
| Inherited / "everyone knows" claim | KAC | ACH if KAC surfaces an alternative |
| Long-form judgment hard to defend | Argument Mapping | KAC on weakest nodes |
| Pre-publication self-test | Pre-Mortem | ICD 203 ship-gate |

## Original worked example

A Ugandan agribusiness client believes a competitor's sudden price cut on maize flour means the
competitor is dumping stock before exiting the market. ACH hypotheses: (1) exit and stock
clearance; (2) a new low-cost supply contract; (3) an attempt to take share before a planned
expansion; (4) a data error in the price survey. Evidence scored for consistency: the competitor
is still hiring drivers (inconsistent with 1), import records show a new regional supplier
(consistent with 2 and 3), and prices were confirmed in three markets (inconsistent with 4).
Hypothesis 1 carries the most inconsistencies and is dropped; the diagnostic gap between 2 and 3
is whether the competitor has applied for new premises, which becomes the next collection task.

Sources: Pherson and Heuer (2021) *Structured Analytic Techniques for Intelligence Analysis*,
3rd ed.; Heuer (1999) *Psychology of Intelligence Analysis* (CIA Center for the Study of
Intelligence, public); George and Bruce (eds.) (2008) *Analyzing Intelligence*.
