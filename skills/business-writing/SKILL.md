---
name: business-writing
description: Use as the entry point for non-academic prose — emails, memos, letters, plans, blog articles, web copy, internal comms, fundraising letters, speeches, resumes, executive briefings. Carries the channel router, the seven-step process, the master "don't mumble" rule, and orchestration across six craft references (Maxwell 7 steps, Roman/Raphaelson principles, persuasion/narrative, web copywriting, blog publishing, multi-language standards).
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Business Writing

Single entry skill for any non-academic prose artifact. For reports, proposals, and white papers (longer-form persuasion artifacts with structural conventions of their own), load **`report-and-proposal-craft`** instead.

If the artifact explains, argues, persuades, recommends, evaluates, or interprets, run `critical-reasoning-and-argument` before drafting. This applies to market notes, strategy memos, intelligence-style updates, internal comms, speeches, fundraising letters, and executive briefings.

If the artifact describes how a system, process, workflow, operating model, interface, data architecture, requirements set, or design system works, run `systems-process-requirements` before drafting.

## Channel router

| Channel | Right reference | Process spine |
|---|---|---|
| Email | `references/maxwell-7-steps.md` § email · `references/roman-raphaelson-principles.md` § email | Subject line carries verb; ask in first line; ≤200 words |
| Memo | `references/roman-raphaelson-principles.md` § memos | Title, action recipient, obvious structure |
| Letter (sales / fundraising / complaint / recommendation) | `references/roman-raphaelson-principles.md` § letters | Open with reader's interest; specific ask + deadline; PS line |
| Plan / strategy | `references/persuasion-and-narrative.md` · `references/maxwell-7-steps.md` § organize | SCQA + plain English |
| Blog article | `references/blog-publishing-workflow.md` · `references/web-copywriting.md` | Hook → problem → solution → CTA |
| Web copy / landing page | `references/web-copywriting.md` | F-pattern; value above fold; ≤400 words / page |
| Speech / presentation | `references/roman-raphaelson-principles.md` § speeches | Tell-tell-tell; one idea / slide; one ask |
| Resume / cover letter | `references/roman-raphaelson-principles.md` § resumes | Customised; achievements with numbers |
| Internal comms (status, updates, FAQs) | `references/roman-raphaelson-principles.md` § memos · `references/persuasion-and-narrative.md` | Lead with the news; numbered structure |
| Multi-language artifacts (EN / FR / SW) | `references/language-standards-en-fr-sw.md` | Apply per-language register rules |
| Hard scenario (bad news, decline, apology, discourteous reply, policy change) | `references/scenario-playbooks.md` | Resolve the four axes before drafting; pick named scenario |
| Pitch deck (investor / VC) | `references/extended-channels.md` § Pitch decks | Three critical questions; four-part structure; one visual per slide |
| One-pager / capability statement | `references/extended-channels.md` § One-pagers | Headline + CTA + testimonial; Think/Feel/Do test |
| Training material / instruction manual / course | `references/extended-channels.md` § Training material | Five learning principles; tools, not just text |
| Business plan (for lender / angel) | `references/extended-channels.md` § Business plans | Argument hierarchy first; story supports; meet lender early |
| Grant proposal (foundation / agency) | `references/extended-channels.md` § Grant proposals · `report-and-proposal-craft` | Read the call; budget reconciles to methodology |
| Performance appraisal | `references/extended-channels.md` § Performance appraisals | Behaviour → calibrated phrase → specific action |
| AI-assisted draft of any of the above | `references/ai-assisted-writing.md` | WI before AI; embed evidence-discipline clause in every prompt |
| Long-form magazine piece — essay, criticism, investigative, profile, explainer | `references/long-form-business-journalism.md` | Pick the family (essay / investigative / profile / explainer) before choosing length |

## The seven-step process (load `references/maxwell-7-steps.md`)

Every non-academic artifact runs through:

1. **Identify Readers & Purpose** — name primary/secondary readers; one-sentence purpose.
2. **Collect Information** — source dossier; triangulate load-bearing facts.
3. **Brainstorm** — 15–20 candidate items without self-editing.
4. **Organize** — pick a structural pattern; outline as descriptive headings.
5. **Draft** — write fast; do not edit while drafting; use `[TK]` placeholders.
6. **Revise** — four passes (structure, paragraph, sentence, word) — never combined.
7. **Proof** — mechanical only; on paper or out loud; two human eyes.

Skipping a step or combining Steps 6 and 7 is the #1 quality failure.

## The master rule (Roman & Raphaelson)

> *"Don't mumble."*

Every sentence carries its point at full volume. Hedge soup, Latinate fog, and bureaucrat voice are cardinal sins. Detail in `references/roman-raphaelson-principles.md` (the 18 principles).

## Reference index

| Reference | Load when |
|---|---|
| `references/maxwell-7-steps.md` | Always — process spine for every artifact, plus channel overlays |
| `references/roman-raphaelson-principles.md` | Sentence-level prose discipline (18 principles, per-channel rules for email/memo/letter/plan/proposal/presentation/fund-raising/resume) |
| `references/persuasion-and-narrative.md` | Plans, pitches, fundraising, exec summaries — Hood plain English + Shiach persuasion + Geffner business style + Rubie/Provost narrative; also "make it sound less AI" |
| `references/web-copywriting.md` | Web pages, marketing copy, landing pages, blog post structure |
| `references/blog-publishing-workflow.md` | Producing a full blog article (topic dev, drafting, on-page structure, image prep, site integration) |
| `references/language-standards-en-fr-sw.md` | Multi-language artifacts: English (British/East African), French (Francophone African), Kiswahili (East African) |
| `references/ai-assisted-writing.md` | Any deliverable where an LLM is in the production chain — WI/AI division of labour, prompt design, fact-check discipline (Lindsell-Roberts) |
| `references/scenario-playbooks.md` | One-off communication artefacts where the message is hard — bad news, decline, apology, discourteous reply, policy change (Ramsey four-axis frame) |
| `references/extended-channels.md` | Pitch decks, one-pagers, training material, business plans, grant proposals, performance appraisals (Henwood / Lindsell-Roberts / Garner) |
| `references/long-form-business-journalism.md` | Long-form magazine writing — essay, investigative, profile, explainer — with craft lessons drawn from *The Best Business Writing 2014* (Starkman et al.) |

## Universal anti-patterns

- **Mumbling** — soft openings, hedge stacks, evasive verbs.
- **Latinate fog** — *facilitate, utilize, leverage, optimize, expedite*.
- **Bureaucrat voice** — *heretofore, pursuant, said party, the aforementioned*.
- **Passive evasion** — "it was decided that…" hiding the actor.
- **Adjective inflation** — *significant, substantial, world-class, leading*.
- **Buried lead** — recommendation on page 4.
- **Walls of text** — paragraphs over 5 sentences without break.
- **One-size email** — same long email used for an ask, an FYI, and a heads-up.
- **Drafting before outlining** (Step 4 skipped).
- **Editing while drafting** (Step 5 corrupted with Step 6).
- **Combining revision passes** (rewriting in circles).
- **Treating proof as revision** — missing typos and link rot.
- **Sounds-like-AI prose** — repeated reporting verbs, unhedged certainty, perfectly parallel sentences, no quirks. Load `references/persuasion-and-narrative.md`.

## Universal ship gate

- [ ] Channel identified; right reference loaded.
- [ ] Step 1 purpose statement written.
- [ ] `critical-reasoning-and-argument` run where the artifact contains a claim, recommendation, interpretation, or persuasive ask.
- [ ] `systems-process-requirements` run where the artifact describes systems, processes, requirements, scope, workflow, data, interfaces, or design systems.
- [ ] Outline approved before drafting.
- [ ] Lead carries the news; nothing buried.
- [ ] Average sentence ≤20 words; max 30; varied length.
- [ ] One idea per paragraph; ≤5 sentences typical.
- [ ] Active voice unless deliberate.
- [ ] No Latinate substitutes where Anglo-Saxon works.
- [ ] No vague adjectives (*significant, substantial, very, really*).
- [ ] Numbers, names, dates instead of adjectives.
- [ ] First-revision cut ≥25 %.
- [ ] Channel-specific rule applied (subject line, F-pattern, slide discipline, etc.).
- [ ] Mechanical proof on paper / out loud; two human eyes for external artifacts.
- [ ] Multi-language: per-language register rules verified.

## Companion skills

- `report-and-proposal-craft` — long-form persuasion (reports, proposals, white papers).
- `critical-reasoning-and-argument` — mandatory for non-academic prose that argues, recommends, evaluates, interprets, or persuades.
- `systems-process-requirements` — for process notes, operating-model descriptions, requirements summaries, workflow explanations, and system/data/interface descriptions.
- `academic-writing` — papers, essays, theses, dissertations.
- `web-scraping-foundations` — for pulling source material when needed.
