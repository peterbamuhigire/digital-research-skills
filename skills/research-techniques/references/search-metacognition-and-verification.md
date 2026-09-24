# Search Metacognition and Verification

Use this guide while a search is running: to keep the question in view, recognise dead ends,
reframe, read laterally, verify what was found, and decide when to stop. The structural layer
(question framing, operators, databases) is in `search-craft-and-deep-web.md`.

## Inputs

- The written research question and its sub-questions.
- The research log (queries, sources, dates, results).
- The claim or claims currently believed to answer the question.

## Decision rules

1. **The written question is the anchor.** Keep it visible. Questions legitimately change as
   evidence arrives; when they do, record the new version and change the search strategy with
   it. A strategy left over from an earlier framing is a common cause of dead ends.
2. **Know what you are doing at every moment.** You should be able to say what the current query
   is for and how confident you are in what you already "know".
3. **Question the surprising.** Spend verification effort on what looks unusual, too neat or not
   quite right; resist interesting diversions that do not serve the question.
4. **Context before numbers.** A 4.5-star rating from three reviews is not a 4.5-star rating
   from two thousand. Check denominator, period, unit and definition before using any figure.
5. **Read the interface, not just the results.** Snippets are machine-assembled fragments, AI
   overviews and knowledge panels can drop qualifiers; open the source.
6. **Read laterally.** Before judging an unfamiliar site, open new tabs to see what independent
   sources say about who runs it and how reliable it is. Do not judge a site by its own "about"
   page.
7. **Avoid leading queries.** A query that contains the expected answer ("is Lake Victoria 69,000
   square kilometres") retrieves confirmation. Ask neutrally ("Lake Victoria surface area").
8. **Heuristics over checklists.** Published credibility checklists get gamed; judge sources in
   context.
9. **Not everything is online.** Older, local and paywalled material thins out; archives,
   libraries, registries and people are legitimate next steps.

## Verification standard

Treat a claim as verified only when:
1. At least two independent sources agree (not several outlets repeating one press release).
2. Units and definitions match (feet versus metres, gross versus net, calendar versus fiscal year).
3. The original source has been read, not only the abstract or summary.
4. The publisher has a record of correcting errors.
5. The date is current enough for the claim.
6. The figures are internally consistent (shares sum to 100, totals match known populations).
7. An adversarial reader could reproduce or refute it from your cited sources.

Record the verification state in the evidence register (`../../source-evaluation/SKILL.md`).

## Procedure while searching

1. Before each query, note its purpose in the log.
2. After each batch, write one line: what was learned, what changed, confidence now.
3. If three consecutive queries add nothing, treat it as a dead end: reframe (new vocabulary, a
   different source class, a narrower or broader question) rather than repeating.
4. When a candidate answer appears, run the verification standard.
5. Apply the stop rule.

## Stop rule

Stop when the original (or consciously revised) written question is answered to the verification
standard, or when further search has stopped changing the answer and the remaining gap is recorded
as a limitation. Stopping is a decision, logged with its reason.

## Tool patterns worth automating

Query composer that rejects leading questions · unit normaliser · triangulator that fetches the
same figure from several sources and flags disagreement · Wayback snapshot fetcher · EXIF
extractor for images · cross-language Wikipedia comparison to expose framing differences · a
stop-condition check comparing findings with the original question. Treat these as design
inputs for `tools/`; none is claimed to exist unless present in the repository.

## Failure modes

Answering a question that drifted without noticing · repeating a failed query with small
variations · trusting a snippet or AI overview · citing an abstract · accepting three copies of one
press release as three sources · ignoring units · judging a site by its own claims · never
stopping, or stopping at the first plausible answer.

## Original worked example

Question: "What share of Rwanda's electricity came from hydropower last year?"
- First hit is a snippet giving a figure without a year. Opened: it is a 2019 blog.
- Lateral check shows the blog restates an old utility press release.
- Reframed to official sources: the national utility's annual report and the energy regulator's
  statistics; the question is revised to specify installed capacity versus generation, because
  the two sources report different measures.
- Verified: both official sources give generation for the same year and agree within rounding;
  the log records the revision and the stop decision.

## Checklist

- [ ] Written question visible; revisions logged.
- [ ] Every figure checked for denominator, unit, period and definition.
- [ ] Unfamiliar sources read laterally.
- [ ] Queries free of embedded answers.
- [ ] Verification standard met for each load-bearing claim.
- [ ] Stop decision recorded with reason.

Sources: Russell (2019) *The Joy of Search*; Wineburg and McGrew (2019) "Lateral reading and the
nature of expertise", *Teachers College Record* 121(11). Reorganised by task; examples are the
engine's own.
