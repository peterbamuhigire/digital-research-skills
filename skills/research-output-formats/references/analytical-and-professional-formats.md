# Analytical and professional formats

Covers: **intelligence report, legal opinion**.

These are decision-grade outputs governed by **professional tradecraft norms** — the IC analytic standards (ICD 203 / 206) for intelligence work, and rules of professional conduct plus citation discipline for legal work. The voice is calibrated, the structure is conventional within the profession, and the consequences of fabrication are severe.

---

## Intelligence report

A structured, decision-grade analytical product written for a named decision-maker or stakeholder. Length ranges from a 1-page **flash** to a 30-page **assessment**.

**Sub-types.**
- **Current intelligence** / situational update — what just happened, why it matters, near-term outlook.
- **Estimative / strategic assessment** — forward-looking judgment over months to years.
- **Warning intelligence** — anomaly or emerging-threat alert.
- **Target / entity profile** — focused dossier on an organisation, person, or system.
- **Open-source intelligence (OSINT) report** — same shape, different sourcing regime; see `osint-investigation`.

**Structure (assessment).**
1. Title and classification (or distribution marking).
2. Bottom Line Up Front (BLUF) — the answer in 2–4 sentences.
3. Key judgments — 3–6 numbered, each with a confidence level (high / moderate / low) and an "if-this-changes-our-view" line.
4. Background — the question, scope, what was and was not assessed.
5. Sources and methodology — sourcing regime, gaps, alternative hypotheses considered.
6. Analysis — body, organised by key judgment.
7. Indicators / warnings — what would change the assessment.
8. Outlook.
9. Annexes — chronology, entity table, source-reliability matrix.

**Voice rules.**
- "Estimative language" — words have technical meaning. "Likely" ≠ "almost certainly" ≠ "possible". Define terms in an annex.
- Confidence is a separate axis from likelihood and is stated explicitly.
- Distinguish information from judgment. Every judgment cites or footnotes the information it rests on.
- Alternative analysis is part of the deliverable, not an afterthought.

**Common failure modes.**
- Burying the BLUF.
- Conflating likelihood and confidence.
- Single-source judgments without an alternative-hypothesis section.
- Importing OSINT without grading the source.

**Academic variant.** **Strategic studies / area studies paper** — same forward-looking, judgment-heavy character but in journal format with full citations. Submit as a paper (see `academic-formats.md`).

**Non-academic variant.** The default. Government, military, corporate-security, and competitive-intelligence reports all sit here. The engine's OSINT outputs follow this format unless the customer has prescribed another.

**Cross-skill dependencies.**
- `analytic-tradecraft` — the underlying methodological skill (ACH, structured analytic techniques, source grading).
- `osint-investigation` — for sourcing and entity tradecraft.
- `source-evaluation` — every claim and every source.

**References.**
- Office of the Director of National Intelligence, *ICD 203: Analytic Standards* (most recent revision; open).
- Office of the Director of National Intelligence, *ICD 206: Sourcing Requirements for Disseminated Analytic Products* (open).
- Heuer, *Psychology of Intelligence Analysis*, CIA Center for the Study of Intelligence, 1999 (open).
- Heuer & Pherson, *Structured Analytic Techniques for Intelligence Analysis*, 3rd ed., CQ Press, 2020.
- Clark, *Intelligence Analysis: A Target-Centric Approach*, 6th ed., CQ Press, 2019.
- Treverton, *Reshaping National Intelligence for an Age of Information*, Cambridge UP, 2003.
- UK Professional Head of Intelligence Assessment (PHIA), *Probability Yardstick* (open public-sector guidance for confidence wording).

---

## Legal opinion

A reasoned written advice from a lawyer to a client (or to another lawyer) on a specific legal question. May be a 2-page memo or a 50-page formal opinion. Carries professional liability.

**Structure.**
1. Heading — opining lawyer, addressee, date, matter, file reference.
2. Question(s) presented.
3. Short answer — one or two sentences.
4. Facts assumed — explicit and bounded.
5. Applicable law — statutes, regulations, leading cases, treaties.
6. Analysis — IRAC or CREAC structure per issue (Issue / Rule / Application / Conclusion).
7. Counter-analysis — the strongest opposing argument and why it fails (or, if it does not fail, why the answer is qualified).
8. Conclusion and any qualifications, assumptions, or limits on reliance.
9. Signature block and bar identification (where applicable).

**Voice rules.**
- Third person, formal.
- Calibrated — distinguish clear law, unsettled law, and policy.
- Pinpoint citations to paragraph (case law) or section (statute). No generic page references for electronic judgments.
- Assumptions are explicit. The opinion is only as good as the facts assumed.
- A formal opinion identifies the lawyer's qualifications and the jurisdiction of admission; many also include a reliance clause.

**Common failure modes.**
- Conflating advice with prediction without saying so.
- Citing cases without checking they are still good law (citator failure).
- Burying the assumptions.
- Failing to flag conflicts of law in cross-jurisdictional matters.

**Academic variant.** **Doctrinal analysis / case comment** — published in a law journal. Same IRAC discipline, full footnotes (OSCOLA in the Commonwealth tradition; Bluebook in the US), no client-advice frame. Submit as an academic paper (see `academic-formats.md`).

**Non-academic variant.** The default — client memorandum or formal opinion letter.

**Cross-skill dependencies.**
- `online-legal-research` — primary methodology skill; load it first.
- Specifically `references/legal-analysis-irac.md` and `references/citation-and-quoting-discipline.md` from that skill.
- For East African work, `references/east-african-overlay.md`.
- `source-evaluation` — fabrication of a case name or pinpoint cite is malpractice-grade.

**References.**
- Putman & Albright, *Legal Research, Analysis and Writing*, Cengage, 2018.
- Garner, *Legal Writing in Plain English*, 2nd ed., University of Chicago Press, 2013.
- Kunz, Schmedemann, Erlinder, Downs & Bateson, *The Process of Legal Research: Practices and Resources*, 9th ed., Wolters Kluwer, 2020.
- Edwards, *Legal Writing and Analysis*, 5th ed., Wolters Kluwer, 2019.
- ABA Model Rules of Professional Conduct (US) / SRA Code of Conduct (England & Wales) / Uganda Advocates (Professional Conduct) Regulations / Kenya Law Society of Kenya Code of Standards — all govern the duties owed when issuing an opinion. Load the regime that governs the opining lawyer.
- *OSCOLA: The Oxford University Standard for the Citation of Legal Authorities*, 4th ed., 2012 (open) — for Commonwealth opinions.
- Bluebook: *A Uniform System of Citation*, 21st ed., 2020 — for US opinions.
