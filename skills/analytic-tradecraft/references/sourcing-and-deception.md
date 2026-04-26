# Reference — Sourcing and Deception

**Canonical sources:**
- Bruce, James B., and Bennett, Michael. "Foreign Denial and Deception: Analytical Imperatives." Ch 8 in George & Bruce, *Analyzing Intelligence*, Georgetown UP, 2008. Tier 1.
- Bruce, James B. "The Missing Link: The Analyst-Collector Relationship." Ch 12, same volume. Tier 1.
- NATO STANAG 2511 / AJP-2.1 — Source Reliability A–F × Information Credibility 1–6 (Admiralty Code). Tier 1.
- Silberman-Robb WMD Commission Report, 2005. Tier 1.

This reference governs three things: (1) the single-source rule, (2) the NATO Admiralty Code as a parallel grading lane to the engine's 5-tier credibility ladder, and (3) the denial-and-deception (D&D) discipline.

## The single-source rule

**No key judgment may rest on a single uncorroborated stream.**

The 2002 Iraq WMD NIE (Bruce Ch 11, pp 179–183) is the canonical violation. The central claims rested on Curveball (a single HUMINT source) and the Samarra-tanker imagery (a single IMINT stream), neither corroborated. Both turned out to be wrong. Silberman-Robb (2005) identified single-source over-reliance as the most consequential sourcing failure of the era.

The engine's rule, derived from this:

| Number of independent sources | Source confidence ceiling | Permitted judgment confidence ceiling |
|---|---|---|
| 1 (uncorroborated) | LOW | POSSIBLE / ROUGHLY EVEN — never higher |
| 2 (independent, ≥ 1 tier-1 or tier-2) | MEDIUM | LIKELY |
| 3+ (independent, mixed tiers including ≥ 1 tier-1) | HIGH | VERY LIKELY / ALMOST CERTAINLY |

A single-source judgment ships as a **HYPOTHESIS** with explicit indicators of what would corroborate it — never as an assessment.

"Independent" means the sources do not share an upstream origin. Three news outlets republishing one wire story count as one source. Three peer-reviewed papers using the same dataset count as one source for the dataset, three for the analysis.

## The NATO Admiralty Code

The Admiralty Code (NATO STANAG 2511, AJP-2.1) is a two-axis grading system widely used across NATO and allied services. It separates **source reliability** from **information credibility**, which addresses the conflation problem (see `kent-estimative-probability.md` on judgment vs. source confidence).

**Source reliability scale (A–F):**

| Letter | Meaning |
|---|---|
| A | Completely reliable. Proven track record of complete reliability. |
| B | Usually reliable. Minor doubt; mostly valid information. |
| C | Fairly reliable. Some doubt; has provided valid information in past. |
| D | Not usually reliable. Significant doubt; some past valid information. |
| E | Unreliable. Lacks authenticity or trustworthiness; history of invalid information. |
| F | Reliability cannot be judged. No basis for assessment. |

**Information credibility scale (1–6):**

| Number | Meaning |
|---|---|
| 1 | Confirmed by other independent sources; logical; consistent with other information. |
| 2 | Not confirmed; logical; consistent with other information. |
| 3 | Possibly true; reasonably logical; agrees with some other information. |
| 4 | Doubtful. Not confirmed; possible but illogical; no corroborating sources. |
| 5 | Improbable. Contradicts existing well-corroborated information. |
| 6 | Truth cannot be judged. No basis for evaluating validity. |

Each axis is assessed independently. **Source reliability does not bias credibility rating**: an A-rated source can supply a "2" piece of information; an E-rated source can supply a "1". The engine grades both.

**Engine integration.** The Admiralty Code runs *parallel* to the 5-tier credibility ladder in `source-evaluation`. The 5-tier ladder is the engine's first cut (1 = primary; 5 = unvetted). The Admiralty Code is the second cut for any source carrying a load-bearing claim. The two grades together appear in the manifest:

```
Source: Bellingcat geolocation report 2024-11-12
Tier (5-tier ladder): 2 (authoritative secondary; vetted OSINT publication)
Admiralty Code:       B-1 (usually reliable source; confirmed by independent satellite imagery and shadow-time computation)
```

## Denial and deception (D&D)

Bruce and Bennett (Ch 8, *Analyzing Intelligence*) lay out the D&D framework. Key principles:

1. **All deception works within a context of truth.** A pure fabrication is detectable; a deception inserts a false element into a true context. This makes D&D particularly hard to spot.
2. **D&D principles.** (a) Channel manipulation — feed false information through a channel the target trusts. (b) Mindset exploitation — supply information that confirms the target's existing assumptions. (c) Confirmation bias exploitation — supply information that confirms the leading hypothesis the analyst is forming.
3. **Counter-D&D.** (a) Include an explicit D&D hypothesis in every ACH matrix when adversary action is plausible. (b) Treat absence of expected evidence as a candidate hypothesis (X may not exist) rather than assuming D&D explains it. (c) Maintain analyst-collector dialogue (Bruce Ch 12) so the analyst understands how each source was acquired and what its known limits are.

The Pearl Harbor case (Bruce-Bennett Ch 8, pp 122–125, citing Wohlstetter) illustrates the failure mode: warning indicators were drowned in noise and filtered through a mindset that war was not imminent. The Yom Kippur 1973 case (Davis Ch 10) illustrates the same pattern in a different theatre: confirmation bias led analysts to keep moving the warning threshold until war began.

## Negative evidence

A subtle but lethal failure: the absence of an expected indicator is treated as evidence of D&D rather than as a hypothesis in its own right. Bruce Ch 11 on the Iraq WMD NIE: the absence of expected WMD-program indicators was explained away as Iraqi concealment success rather than entertained as the hypothesis "the programs were largely destroyed in 1995 as the Kamel defection reporting indicated".

**Engine rule.** Any time the analyst writes "we don't see X", a hypothesis "X may not exist" enters the ACH matrix. The hypothesis is tested against the evidence with the same rigour as the dominant hypothesis.

## Analyst-collector dialogue

Bruce Ch 12 ("The Missing Link") argues that analysts who do not understand how their sources were acquired routinely overweight some streams and underweight others. The engine's analogue: every source in the manifest carries its acquisition story (where it came from, who collected it, what its known limits are), not just the URL.

For OSINT sources this means: who first published; under what conditions; with what stake in the framing; with what corroboration available.

## Sources

- George & Bruce, *Analyzing Intelligence*. Bruce-Bennett Ch 8; Bruce Ch 11; Bruce Ch 12. Tier 1.
- NATO STANAG 2511 / AJP-2.1. Tier 1.
- Silberman-Robb WMD Commission Report, 2005. Tier 1.
- Wohlstetter, Roberta. *Pearl Harbor: Warning and Decision*. Stanford UP, 1962. Tier 1 (the canonical D&D case study, cited by Bruce-Bennett).
