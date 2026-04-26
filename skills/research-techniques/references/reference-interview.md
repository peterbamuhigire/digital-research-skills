# Reference interview

Bell: the largest single failure mode in research is the gap between what the user says they want and what they actually want. Taylor's "compromised need" — users phrase queries as what they think the system can answer, not what they actually want.

## The three components (Bell)

1. **Establish contact** — set the user at ease; non-judgemental
2. **Determine the actual information need** — open + closed questions; Bates's clarifying probes
3. **Verify the answer met the need** — never end without this; "negative closure" is a documented failure mode

## Bates's eight clarification questions

These are the highest-leverage probes for any stated query:

1. "Can you tell me more about what you're working on?"
2. "What kind of information are you hoping to find?"
3. "How will this be used?"
4. "If you were writing an article about this, what would the headline be?"
5. "If I can't find exactly _____, what would be second-best?"
6. "Do you have a specific source in mind, or should we explore?"
7. "Is there a specific time period or geographic scope?"
8. "What level of detail do you need — overview, deep-dive, or specific fact?"

## Six types of misstated query (Bell)

Watch for these — they look like clear queries but aren't:

| Type | Example | Real question often is |
|---|---|---|
| **Misdirected** | "Find me data on hostel fires" | The user means a specific fire incident |
| **Proxy-for-easier** | "What's the average rent in Nairobi?" | Affordability gap; needs distribution not mean |
| **Interpreter** | "My friend wants to know..." | The interpreter's framing distorts |
| **Compromised** | "Can you find some statistics on X?" | They want a specific stat; "some" hides specificity |
| **Mishearing** | User repeats what they think you said | Recheck the original |
| **Sounds-reasonable-but-isn't** | "Show me hostel deaths by university" | No such data exists; the real Q needs reframing |

## Open + closed mix

- **Open** ("Tell me about your project") — seed vocabulary; surface unstated needs
- **Closed** ("Scholarly or popular?", "Last 5 years or longer?") — prune scope
- Bell warns against using only one type. Mix deliberately.

## Rowland's premise

Beyond Bates: every research project needs a one-sentence driving premise (Egri, via Rowland). Force the user to state it:

- "Romeo and Juliet: great love defies even death."
- "The 80% deposit-non-refund crisis in Uganda is enabled by toothless statutory enforcement."

A project without a premise drifts.

## Decision rules

- **Run the reference interview before any sub-agent fires.** Skipping = silently wrong-question research.
- **At least 2 Bates questions per project.** More for ambiguous starts.
- **Always verify at end** — "did this answer the question you actually had?"
- **Document the elicited intent** — write it into `projects/<project-id>/DESIGN.md` as the empirical puzzle and out-of-scope.
- **Beware the compromised need.** When the user phrases a query that seems to fit what the engine "should" be able to answer, suspect it.

## Workflow

1. Receive user's stated query
2. Run 2–4 Bates questions
3. Identify any misstatement type
4. Force a one-sentence premise
5. State back to user: "Here's what I think you actually want — confirm?"
6. Write into `DESIGN.md` as empirical puzzle
7. Dispatch research with the *actual* question

## Anti-patterns

- Treating the first stated query as final
- Asking only closed questions (over-prunes)
- Asking only open questions (loses precision)
- Ending without verifying the answer met the need (negative closure)
- Skipping the premise — leads to drifting projects

## See also

- `research-design-document` — output of the interview lands here
- `research-type-router` — runs after interview, before orchestration
- `gap-analysis` — for follow-up "what else might you need?" probes
