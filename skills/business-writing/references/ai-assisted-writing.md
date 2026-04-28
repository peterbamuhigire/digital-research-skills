# AI-assisted business writing (WI + AI)

Encodes Sheryl Lindsell-Roberts, *Business Writing with AI for Dummies* (Wiley, 2024) into the engine's workflow. Use whenever the engine, or a human collaborator, will use an LLM to draft, polish, brainstorm, summarise, or visualise content for a business deliverable.

## Core principle: WI before AI

Lindsell-Roberts's central distinction:

- **WI — Writer Intelligence.** The human's purpose, audience knowledge, judgment, voice, ethics, and accountability.
- **AI — Artificial Intelligence.** A drafting and transformation tool with speed, breadth, and zero stakes.

**AI does not replace WI. AI makes the WI parts of the work cheaper to attempt and easier to iterate on.** Every output is the writer's, even when the words came from a model.

The seven Maxwell steps still apply. AI shifts the *cost* of each step, not the discipline.

| Step | What AI does well | What only WI can do |
|---|---|---|
| 1. Identify reader and purpose | Generate audience hypotheses | Confirm against the actual reader, set the purpose, accept liability |
| 2. Collect information | Surface candidate sources, summarise long documents | Verify, cite, choose what is load-bearing |
| 3. Brainstorm | Spew 20 candidate angles fast | Pick the angle that fits *this* reader and *this* purpose |
| 4. Organise | Suggest outline shapes | Choose the structural pattern; align it with the recommendation |
| 5. Draft | Generate first-pass prose | Inject voice, specifics, names, numbers; remove anything fabricated |
| 6. Revise | Tighten, vary length, flag passive voice | Decide what to cut; preserve signature lines and arguments |
| 7. Proof | Catch obvious typos and inconsistencies | Catch misspelled names, transposed numbers, missing facts |

**Hard rule:** AI never owns Step 1 (purpose) or Step 7 (proof of fact). A document with the wrong purpose is a faster way to fail. A document with a fabricated fact is the kind of failure that is hard to recover from.

## The engine's evidence-discipline overlay

The engine's overriding rule (`source-evaluation/references/evidence-discipline.md`) is **stricter than Lindsell-Roberts**. AI may not be used to:

- Invent statistics, quotations, names, organisations, court cases, statutes, or URLs.
- Embellish citable claims or attribute statements to real people the model has not been given a verifiable source for.
- Confabulate page references, dates, or amounts.
- Fill gaps the human has not actually researched.

Every fact AI returns is treated as a **draft claim** until verified. If a sub-agent's brief allows AI drafting, the brief embeds the evidence-discipline hard-constraint clause verbatim — same as for any other research output.

## What AI is good for

Lindsell-Roberts groups AI's roles in business writing (chs. 2 and 23):

- **Audience research** — generate first-pass reader profiles, generational guesses, "what would matter to a CFO at a regional bank in Kampala?"
- **Writer's block** — produce 5–10 candidate openers, headlines, or angles in seconds. Pick one; rewrite.
- **Story drafts from a brief** — feed the model the four storytelling pillars (setting, character, conflict, resolution) plus the call to action; receive a draft narrative.
- **Tone shifting** — "make this two paragraphs shorter and more conversational without losing the recommendation."
- **Summarisation** — abstracts, executive summaries, FAQ extracts from long-form material **the human has read**.
- **Bridging languages** — first-pass translation between English / French / Kiswahili (then load `language-standards-en-fr-sw.md` and have a fluent human verify).
- **Visual prompts** — generating prompt copy for image, infographic, and chart-design tools (the writer still chooses the visuals).
- **Tables of contents, glossaries, indexes** — extraction tasks the model is genuinely good at.
- **Mechanical proof** — grammar, punctuation, parallelism, repeated words. Treat as a first pass, never as final.

## What AI is bad for

- **Names and pinpoint citations.** Models hallucinate authoritatively. Always verify against the source.
- **Numbers in context.** A model can produce a plausible-looking percentage that is wrong in your country, your year, or your category.
- **Voice you have already established.** AI tends to revert to a generic professional register; your house voice is not in its default distribution.
- **Strategic decisions.** AI can map options; only WI can pick.
- **Anything where the writer carries professional liability** — legal opinions, audit reports, medical advice, regulated marketing copy.

## Ten principles for prompts (Lindsell-Roberts ch. 23)

1. **GIGO is real.** Vague, incomplete, or misleading prompts produce vague, incomplete, or misleading output.
2. **Know the chatbot's strengths.** Some are stronger at narrative; some at factual extraction. Choose the tool for the task.
3. **Speak to it like a colleague who needs context.** Skip the *please* and *thank you* — but spell out the brief.
4. **One task per prompt.** Mixed prompts produce mixed output. *"Outline the email"* and *"draft the email"* are two prompts.
5. **Specify constraints.** Word count, paragraph count, tone, audience, format, must-include elements, must-avoid elements. The more explicit the constraint, the more usable the draft.
6. **Open-ended for exploration; closed for precision.** *"How do you envision the role of AI in healthcare?"* opens space; *"Does AI improve diagnostic accuracy in radiology?"* closes it.
7. **Use domain keywords.** *"Plants, soil, organic, fertiliser"* steers a gardening prompt; *"breed, size, training, temperament"* steers a pets prompt.
8. **Ask for evidence, then verify.** *"Provide three peer-reviewed studies that support your claim."* Then read the studies — many will be fabricated until you check.
9. **Iterate by re-prompting.** *"Shorten to two paragraphs."* *"Make the tone more conversational."* *"Strip the bizspeak."* *"Add a concrete example from East Africa."*
10. **Make the document yours.** Replace the model's words with your own where they don't sound like you. If a draft says *utilize this only when …*, change it to *use this only when …* if that's how you write.

## Prompt template — the engine's default

```
You are drafting [DELIVERABLE TYPE] for [READER] whose purpose in reading is to
[DECISION OR ACTION]. The audience knows [KNOWN]; they do not yet know [UNKNOWN].
The recommendation / news is: [ONE SENTENCE].

Constraints:
- Length: [WORDS / PAGES / SLIDES]
- Tone: [REGISTER]
- Must include: [NAMES, NUMBERS, DATES the model can rely on; quote them verbatim]
- Must avoid: [BIZSPEAK terms relevant to this audience], hedging, hallucinated cites
- Voice notes: [SAMPLE OF HOUSE VOICE if available]

Do not invent statistics, names, organisations, citations, or URLs.
Mark anything you are unsure of with [TK].
Where you have synthesised across sources I provided, mark "(synthesis)".
Where you have made an inference, mark "(inference)".
```

The hard constraints in the last block come straight from the engine's evidence-discipline clause. They go in every prompt, without exception, when the deliverable is meant to ship.

## Anti-patterns

- **Pasting the AI draft and shipping it.** First-draft AI prose is generic; voice and specifics are added by the human in revision.
- **Treating model citations as real.** Model citations are *plausible*; they are not *verified*.
- **Single-pass prompting.** Iteration is the workflow, not a fallback.
- **Mixing tasks in one prompt.** Brainstorm → outline → draft → polish are four prompts, not one.
- **Letting AI choose the purpose.** Step 1 is a human decision tied to the reader. AI can hypothesise the audience; it cannot set the purpose.
- **Letting AI compress where compression matters most.** Executive summaries, key judgments, and recommendations are written by hand; AI may suggest variants only.
- **Forgetting the audit trail.** When AI is part of the production chain, the engine notes which sections were AI-drafted and human-revised — same as it notes synthesis and inference elsewhere.

## Ten common failure modes the AI does not fix (ch. 24)

Lindsell-Roberts's "ten reasons business writing fails" — useful as a checklist for any AI-assisted draft, because the model will not catch most of them:

1. Failing to address the target reader.
2. Poor planning.
3. Lacking clear objectives.
4. *Where's the beef?* — no concrete substance behind the headline.
5. Lacking visual interest (paragraphs over 8 lines, sentences over 20 words).
6. Inconsistent tone.
7. Spelling and grammatical errors (especially names and numbers).
8. Insufficient supporting evidence.
9. Management-speak, buzzwords, jargon.
10. Not using AI as an assistant — *the failure of leaving the tool unused on tasks where it would compress hours of effort.*

The first nine are WI failures. The tenth is an AI-adoption failure. Both are mistakes.

## Source books

- Lindsell-Roberts, *Business Writing with AI for Dummies*, Wiley, 2024.
- HBR, *HBR Guide to Better Business Writing*, Harvard Business Review Press, 2013 — chs. on planning, drafting, and tone (still the WI baseline).
- `source-evaluation/references/evidence-discipline.md` — the engine's overriding hard rule.
- `references/maxwell-7-steps.md` — the workflow AI plugs into.
