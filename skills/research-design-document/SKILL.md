---
name: research-design-document
description: Use to author and maintain the canonical 3–4-page design document that governs every research project — empirical puzzle, theoretical puzzle, research questions, action list. The "north-star artefact" every sub-agent must read and update. Adapted from Andrew Abbott, Digital Paper.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Research design document

Abbott: *"Only a clear design document can tell you when you are finished... it provides the necessary outside voice."* This is the artefact every project needs and most projects don't have.

## Required sections (3–4 pages total)

### 1. Empirical puzzle
**A *why* question, not a *what*, *how*, or *does-it-illustrate-Y* question.**

✅ "Why do 80% of Ugandan tenants never recover their security deposit despite a 2022 law mandating refund?"
❌ "What are the deposit-refund practices in Uganda?" (descriptive non-puzzle)
❌ "Does the East African rental market illustrate Polanyi's theory of the great transformation?" (illustration-not-puzzle)

**Seatmate test:** state the puzzle in two sentences such that a stranger can repeat it back **and** finds it interesting.

### 2. Theoretical puzzle
**Competing alternative accounts of the mechanism, not a larger version of the empirical puzzle.**

For the deposit example: "Is non-refund driven primarily by (a) information asymmetry between tenants and landlords, (b) deliberate exploitation enabled by weak enforcement, or (c) structural informality that makes formal refund unworkable?"

### 3. General research questions (4–5)
Higher-order questions the project answers, e.g.:
- What is the actual non-refund rate, broken down by city / property type / lease formality?
- What enforcement mechanisms exist and how often are they invoked?
- Which intervention designs have been tried elsewhere and with what success?
- What would a deposit-escrow product need to look like to fix the dynamic?

### 4. Specific research questions (10–20)
Operational questions a sub-agent can answer in a bounded session:
- "How many cases were filed at Kenya Rent Tribunal under CAP 301 in 2024?"
- "What does Uganda L&T Act 2022 § 26 actually require?"
- etc.

### 5. Action list / to-do
Concrete next steps, owner, deadline.

### 6. Out-of-scope
Explicit list of perspectives / cohorts / topics excluded by the project.

### 7. Stop criteria
What evidence would let us declare the project complete? Without this, the project never ends.

## Decision rules

- **Versioned, dated, append-only.** Each revision is a snapshot, not an overwrite.
- **Updated continuously.** Bell: "the search you start with is seldom the search you end up with" — same applies to the design.
- **Phase transitions are gated by design-document revisions.** Stable design → midphase I; positive establishment minianalysis → midphase II; minianalyses clustering into outline → midphase III; linear outline → endphase.
- **Every sub-agent must read the latest version.** This is the orchestrator's contract with its agents.
- **Empirical puzzle ≠ theoretical puzzle.** If the theoretical puzzle is just a re-statement of the empirical, the document is broken.
- **Stop criteria up front.** "Without an explicit finish line, you'll keep researching forever."

## File location

`projects/<project-id>/DESIGN.md` — top-level project artefact, alongside `README.md`, `CLAUDE.md`, `EVIDENCE-AUDIT.md`.

## Anti-patterns

- Descriptive *what*-questions framed as puzzles
- "Does X illustrate Y's theory" — illustration is not a puzzle
- Theoretical puzzle that is just a bigger empirical puzzle
- No stop criteria — the project drifts forever
- Hidden out-of-scope — leads to scope creep mid-project
- Single version, no revision history — loses the trace of how the project evolved

## See also

- `research-type-router` — runs upstream of this; picks type + schema
- `minianalysis-engine` — atomic units of progress per the design
- `crosswalk-matrix` — operational view of "research questions × sources"
- `gap-analysis` — feeds revisions to the design as gaps emerge
- `evidence-discipline` — the design itself is subject to evidence-discipline
