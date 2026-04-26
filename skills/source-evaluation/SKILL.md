---
name: source-evaluation
description: NON-NEGOTIABLE — use on every source the engine consults. Carries the engine's anti-hallucination guardrail (evidence discipline), the 5-tier credibility ladder, the Burke five-term source-doubt pentad, the Tudor twelve-point rubric for media/journalism, and Silverman/Bellingcat media-forensics workflow. Five references; load only what the source type demands.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
  priority: critical
---

# Source Evaluation

Single entry skill for vetting any source the engine consults. Plagiarism prevention is in `academic-writing`; this skill governs **whether a source is trustworthy in the first place** and whether claims drawn from it have hallucinated detail.

## The non-negotiable guardrail (load first)

Always load `references/evidence-discipline.md`. The engine's first rule: **no claim, statistic, quote, name, case, statute, URL, date, or place appears in output unless traceable to a real source.** This applies to every output of every skill.

## Source-type router — load the matching reference

| Source type | Load |
|---|---|
| **Any source — the universal floor** | `references/evidence-discipline.md` (always) + `references/credibility-ladder.md` |
| **Primary document** (archival record, legal filing, government publication, leaked file, manuscript) | `references/burke-five-term-doubt.md` |
| **Media, journalism, analyst report, think-tank publication** | `references/tudor-twelve-points.md` |
| **Misinformation-prone news / viral information stream** | `references/tudor-twelve-points.md` + `references/misinformation-and-bias-checks.md` |
| **Image, video, audio, screenshot, suspect document** | `references/silverman-media-forensics.md` |
| **Encyclopaedic / reference work** | `references/credibility-ladder.md` (tier 4: tertiary) |
| **Social media post / forum / comment** | `references/tudor-twelve-points.md` + `references/silverman-media-forensics.md` (provenance) |
| **Statistic / dataset** | `references/credibility-ladder.md` + Walker four-axis (`data-quality-assessment`) |

## The 5-tier credibility ladder (universal)

Detail in `references/credibility-ladder.md`. Quick reference:

| Tier | Type | Trust default |
|---|---|---|
| **1 — Primary** | Original document, dataset, transcript, recording, photo with provenance | High; still apply Burke pentad |
| **2 — Authoritative secondary** | Peer-reviewed paper, government statistical release, audited corporate filing, court judgment | High |
| **3 — Vetted journalism / analyst** | Established outlet, named analyst report, named expert quote in mainstream press | Medium-high; apply Tudor twelve points |
| **4 — Tertiary / reference** | Encyclopaedia, textbook, well-cited Wikipedia article, dictionary | Medium for orientation; never sole proof |
| **5 — Unvetted** | Social media post, blog, forum, AI output, anonymous source | Low; treat as lead, not evidence |

**Rule:** any tier-5 claim must be triangulated against ≥2 tier-1 to tier-3 sources before it appears as fact. Tier-4 claims need ≥1 tier-1 to tier-3 source for any load-bearing assertion.

## Burke's five-term source-doubt pentad (primary documents)

Detail in `references/burke-five-term-doubt.md`. For every primary document, ask:

1. **Author** — who wrote it; what was their position, motive, knowledge?
2. **Provenance** — chain of custody from creation to your hands; gaps; tampering opportunities.
3. **Production** — when, how, under what conditions; first or revised; original or copy.
4. **Mechanics** — language, format, conventions of the era; do they match?
5. **Aims** — what was the document trying to do; who was the intended audience?

A document that survives the pentad is **evidence with known limits.** A document that hasn't faced it is **evidence with unknown limits**, which is dangerously close to hallucination input.

## Tudor's twelve-point evaluation (media / journalism / analyst)

Detail in `references/tudor-twelve-points.md`. Twelve criteria:

1. Recency · 2. Relevancy · 3. Authority · 4. Completeness · 5. Accuracy · 6. Clarity · 7. Verifiability · 8. Statistical validity · 9. Internal consistency · 10. External consistency · 11. Context · 12. Comparative quality

Apply when a media or analyst source carries a load-bearing claim. The audit produces a one-line verdict that the engine logs in the manifest.

## Misinformation and bias checks (viral / politicized / contested claims)

Detail in `references/misinformation-and-bias-checks.md`. Before a contested or viral claim enters the corpus:

1. Separate **fact**, **opinion**, and **interpretation**.
2. Check the claim against the **original source**, not just reposts or reactions.
3. Identify the likely **biases** in the source and in the analyst.
4. Treat **virality** as a warning sign, not corroboration.
5. Downgrade any claim whose chain leads only to commentary, screenshots, or clipped excerpts.

## Silverman / Bellingcat media-forensics (images, video, documents)

Detail in `references/silverman-media-forensics.md`. Workflow:

1. **EXIF extraction** — camera, GPS, timestamp.
2. **Reverse image search** — Google Lens, Yandex, TinEye, Bing.
3. **Geolocation by landmark / shadow-time computation**.
4. **Archive recovery** — Wayback, archive.today, original posting site.
5. **Provenance tracing** — who first published; cross-platform trail.
6. **Tampering detection** — error-level analysis, metadata anomalies.

Output: provenance chain logged with timestamps, URLs, and confidence.

## Universal output rule

Every cited claim in engine output carries:

- **Source reference** (URL, DOI, archive link, document ID).
- **Source tier** (1–5 from the credibility ladder).
- **Verification trail** (Burke / Tudor / Silverman audit if applicable, otherwise "credibility-ladder" only).
- **Confidence** (high / medium / low).
- **Date accessed** (UTC).

If any of those is missing, the claim does not ship.

## Universal anti-patterns

- Trusting a tier-5 claim without triangulation.
- "Studies show" without footnote.
- Citing a stat older than 3 years without flagging.
- Single-source paragraph on contested terrain.
- Image used as evidence with no reverse-image-search trail.
- Wikipedia footnote chasing skipped — citing the article instead of its source.
- Author of a document never named, motive never considered.
- AI-generated source list passed through unchecked — **must be 100 % verified before any output**.
- Quote attribution to a person without locating the original utterance.
- URL cited without archival snapshot — link rot kills evidentiary trails.
- Mixing source-tier verdicts in one paragraph without flagging the weakest.

## Universal ship gate

- [ ] `evidence-discipline.md` audit run on every claim.
- [ ] Every source assigned a tier (1–5).
- [ ] Every primary document has Burke pentad notes.
- [ ] Every media / journalism source has at least a 12-point quick verdict.
- [ ] Every load-bearing image / video has a Silverman provenance trail.
- [ ] Every tier-5 claim triangulated against ≥2 tier-1 to tier-3 sources.
- [ ] No URL ships without an archive.org or archive.today snapshot.
- [ ] Manifest entry per source: `{ref, tier, verification, confidence, accessed}`.
- [ ] Hallucination check: any claim absent from the source list is removed.

## Companion skills

- `data-quality-assessment` — for source-vetting at the dataset level (Walker four axes).
- `web-scraping-foundations` — when you collect the source yourself.
- `osint-investigation` — when sources sit inside a broader investigation.
- `academic-writing` — when sources feed an academic artifact (citation styles in references).
- `analytic-tradecraft` — when source disputes become estimative judgments.
