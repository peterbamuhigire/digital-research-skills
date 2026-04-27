# Decision-science heuristics

**Date written:** 2026-04-27
**Drawn from:** Brockman (ed.), *Thinking — The New Science of Decision-Making, Problem-Solving, and Prediction* (essays from a range of cognitive scientists; the engine treats the volume as a curated source for *operationalisable* findings, not as a coherent theory).

This reference distils the operationalisable parts of the decision-science literature for use in engine outputs that involve **forecasts, probability claims, judgement under uncertainty, or causal attribution**. It is not a complete cognitive-science primer; it is a checklist the analyst runs when the output ships a prediction or judgement.

## Two systems — the working frame

The dominant frame from the Brockman volume (echoing Kahneman): the mind operates two ways.

| System | Description | Strength | Failure mode |
|---|---|---|---|
| **System 1** | Fast, automatic, intuitive, pattern-matching | Cheap and accurate in familiar environments | Fooled by base-rate neglect, anchoring, availability, framing |
| **System 2** | Slow, deliberate, calculative, effortful | Catches and corrects System 1 errors | Lazy — rarely engaged unless forced |

Operational rule: **System 2 must be deliberately engaged on any consequential forecast or judgement.** "Going with the gut" is acceptable in domains where (a) the analyst has thousands of hours of feedback experience and (b) the environment is regular enough for pattern-matching to be valid (Gigerenzer's "kind learning environment"). It is not acceptable in novel, contested, or sparse-feedback domains.

## When intuition is trustworthy (Gigerenzer)

Gigerenzer's contribution to the volume rebuilds intuition's reputation in specific conditions:

- **Frequent feedback** — the analyst has been right and wrong many times and learned
- **Quick feedback** — within minutes or hours of the judgement
- **Stable environment** — the rules of the domain haven't shifted under the analyst
- **Low-information sufficiency** — fewer cues, well-known cues, beat richer noisier ones (the "less-is-more" effect)

In domains that meet these conditions (e.g., a trauma surgeon's triage call, an experienced firefighter's read of a building), intuition is fast and reliable. In domains that don't (e.g., long-horizon political forecasts, novel regulatory regimes), intuition is mostly noise dressed as judgement.

## The standard System-1 traps (Kahneman family)

Operational checklist before shipping a judgement:

### Anchoring

Did the first number mentioned in the conversation drag the estimate? Try generating the estimate from independent base rates first, then compare.

### Availability

Did vividness of recent or memorable cases inflate the perceived frequency? Frequency claims must come from data, not memory.

### Representativeness

Did pattern-matching to a stereotype override base rates? Treat the base rate as the prior and the case-specific evidence as a small adjustment.

### Confirmation bias

Were sources searched neutrally, or with the conclusion in mind?

### Overconfidence

Are stated probabilities calibrated? A series of "90% confident" judgements should be wrong about 10% of the time, on average. If the analyst hasn't tracked, assume miscalibration.

### Hindsight bias

After the outcome is known, the inevitability of the outcome inflates. "It was obvious in retrospect" — usually it wasn't.

### Framing

Was the same option evaluated differently because of how it was described (gain frame vs loss frame)? Re-state in the inverse frame.

### Sunk-cost fallacy

Is the position being defended because of resources already committed, rather than expected returns from here?

### Narrative fallacy (Taleb / Pinker family)

Is a coherent story being told about events that were partly random? The neatness of the explanation is a warning sign, not a credibility signal.

## Pinker on rationality (selected operational points)

Pinker's contribution emphasises the costs of motivated reasoning: when the conclusion has identity, tribal, or status implications, the intellect is recruited *defensively*, not analytically. The engine countermove:

- Identify the analyst's stake in the conclusion before publishing
- If a stake exists, name it in the analysis (transparency over suppression)
- Apply steelmanning to the disfavoured side of the question

## Calibration discipline

Calibration is the alignment between stated probability and actual frequency of being right at that probability. Practical operating rules:

1. **State probabilities, not modal hedges.** "70%" is better than "likely". Modal hedges hide miscalibration.
2. **Track outcomes.** A forecaster who never reviews their record cannot improve.
3. **Report ranges where appropriate.** "Between 40% and 60%" reveals the breadth of uncertainty — and is harder to fudge in retrospect.
4. **Use reference classes.** "How often do regulatory reforms of this type pass within 18 months in this jurisdiction?" Generate the reference class explicitly.

## Forecasting routine

Before an engine output ships a forecast or probability claim:

1. **State the question precisely** — what counts as the event, by what date?
2. **Identify the reference class** — comparable past cases
3. **Compute or estimate the base rate** in the reference class
4. **Adjust for case-specific factors** — but not by much (System 1 over-adjusts)
5. **State the forecast as a probability or range**
6. **Run a pre-mortem** (`mental-models-catalog.md`) — imagine being wrong; how would that look?
7. **Identify the conditions that would update the forecast** — and at what threshold

## Sources of judgement quality (signal generation)

Brockman's contributors converge on a few practical signals:

- **Track records beat credentials.** A forecaster's past calibration matters more than their job title.
- **Diverse aggregation beats single experts.** "Wisdom of crowds" works when participants are independent, informed, and incentivised honestly.
- **Pre-registered predictions beat retrofitted ones.** Predictions made before the outcome are testable; retrospective ones are not.
- **Disagreement is information.** When forecasters who normally agree begin to disagree, the question has become genuinely uncertain — note this rather than papering over it.

## Limits and caveats

- The volume is an essay collection, not an integrated theory. Operational rules above are conservative selections that survive across multiple contributors.
- The "two systems" model is a useful heuristic, not a literal neuroscience. Don't over-load on it.
- Calibration takes years to develop; an analyst new to a domain should be especially humble about probabilities.
- Decision science is more confident about *bias detection* than about *bias correction*. Knowing about anchoring does not eliminate it; pre-commitment routines do.

## When to use this in engine work

- Any output that ships a probability or forecast
- Any judgement under sparse feedback (long-horizon political risk, untested regulatory effect, market response)
- Reviewing a past analysis: was the judgement well-made *given the information available at the time*, or was it lucky?
- Stress-testing an analysis before publication

## Anti-patterns

- Treating a hedge ("likely") as a probability claim — it isn't, it's deniable
- Reporting a single-point forecast without uncertainty
- Using base rates only when they support the preferred conclusion
- Calling a judgement "intuition" to avoid stating its inputs
- Dismissing a heuristic as "bias" without checking whether it's accurate in the relevant environment
- Updating on confirmation while ignoring disconfirmation
- Applying the two-systems frame mechanically (it's a model, not a finding)
- Citing Kahneman or Gigerenzer to add prestige to a judgement that has not actually been disciplined by their methods
