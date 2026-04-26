# Reference — OSINT Doctrine and History

**Canonical source:** Bean, Hamilton. *No More Secrets: Open Source Information and the Reshaping of U.S. Intelligence*. Praeger Security International / ABC-CLIO, 2011. Foreword by Senator Gary Hart. Tier 1. Local extract: `extracted-books/no-more-secrets.txt`.

This reference encodes the **institutional lineage** of OSINT and its **competing definitions**. The operating-discipline companion is `references/osint-validation-and-anti-patterns.md`.

Bean's central thesis: the post-Cold War "coming of age" of OSINT in the U.S. is the contested product of organisational discourse — a struggle among officials, contractors, citizen-advocates, and reformers to define what "open source" means, who owns it, and whose authority it serves. Institutional outcomes (DNI Open Source Center, ADDNI/OS post, IRTPA language, DoD Instruction 3115.12) reflect rhetorical victories of particular stakeholders rather than neutral adoption of best practice.

---

## Why doctrine matters for the engine

The engine is a civilian, lawful OSINT operation. Bean's contribution is that **OSINT is contested terrain, not a settled discipline** — and the engine inherits that contest. Knowing the lineage:

- Sharpens the engine's own definition (the engine adopts a hybrid; see below).
- Makes visible the institutional biases that shape what counts as "open source" and what counts as "intelligence".
- Anchors the engine's analytic-tradecraft posture (`analytic-tradecraft/SKILL.md`) in the public-source / classified-source debate the IC has been having for 80 years.
- Surfaces the **democratic potential** of OSINT — informing citizens and challenging classified-stream groupthink — that civilian use of the discipline can realise where the IC has not.

---

## Four competing definitions Bean catalogs

### 1. OSC self-definition (institutional)

> "*Premier provider of foreign open source intelligence*" drawn from publicly available material in 160+ countries and 80+ languages. (Ch 1, p. 5.)

OSC vision: "*We are the nucleus of a global information enterprise serving U.S. national security interests.*"

### 2. Congress (Simmons, 2006 Defense Authorization Act)

> *OSINT is intelligence that is produced from publicly available information collected, exploited, and disseminated in a timely manner to an appropriate audience for the purpose of addressing a specific intelligence requirement.* (Ch 4, p. 63.)

Validated OSINT "*inherently enables information sharing… because of its unclassified nature.*" The Congressional definition foregrounds **requirement-driven tasking** — OSINT is not "research that happens to use public sources"; it is research that responds to an intelligence requirement.

### 3. NATO / Steele

> Unclassified information "*deliberately discovered, discriminated, distilled, and disseminated to a select audience.*" (Ch 4, p. 63.)

The Steele framing positions OSINT as a **foundation** for SIGINT / HUMINT / IMINT, not as a discipline of equal rank — controversial inside the IC.

### 4. Historical synonyms

Non-secret information · overt intelligence · white intelligence · public information · gray literature.

### Engine adoption

The engine adopts the **Congressional + NATO/Steele hybrid**: requirement-driven (Congressional) production of unclassified intelligence using deliberately discovered, discriminated, distilled, and disseminated public sources (NATO/Steele). The engine refuses the OSC framing's institutional capture.

---

## Distinctions Bean draws

### OSINT vs. clandestine INTs

OSINT analysts "*are not spies… work mostly from behind their desks using the Internet,*" but pursue similar strategic-advantage goals. The engine's posture is downstream: civilian, lawful, no covert action, no surveillance of private individuals.

### OSINT vs. journalism

OSINT is **requirement-driven** (tasked by a customer via a collection plan) and oriented to **decision advantage**, not public publication. Products are routinely classified after the fact — a tension Bean treats at length (see `references/osint-validation-and-anti-patterns.md` on over-classification).

The engine sits between the two: requirement-driven like OSINT; oriented toward published deliverables (reports, theses, executive summaries) like journalism.

### OSINT vs. SOCMINT

Bean's book predates "SOCMINT" as a fixed term. The engine treats social-media intelligence as **one source stream among many** (blogs, gray literature, broadcasts, deep-web material) — never as a stand-alone discipline. Social-media-only OSINT inherits that stream's bias and noise floor.

---

## Historical evolution

| Year | Event |
|---|---|
| 1941–47 | Foreign Broadcast Monitoring Service → renamed Foreign Broadcast Information Service (FBIS) under National Security Act 1947, placed in CIA. By peak, FBIS produced ~80 periodicals. |
| 1969 | CIA internal study warns of a "*virtual tidal wave of publicly printed paper*" (quoted in Bean's Foreword, p. viii). |
| 1992 | NIC's *A Vision for the Future*; Senator David Boren legislative push; Robert D. Steele's commentary. |
| 1995–96 | Aspin-Brown Commission "battle of the INTs" — Steele's Burundi demonstration vs. CIA's product. |
| 2004 | Intelligence Reform and Terrorism Prevention Act (IRTPA) creates ODNI. |
| 2005 | WMD ("Silberman-Robb") Commission urges DNI program office for advanced search / MT / knowledge extraction. **DNI Open Source Center (OSC)** established (built on FBIS). **ADDNI/OS** position created (Eliot Jardines first; Doug Naquin directs OSC). |
| 2006 | Simmons-authored OSINT definition in Defense Authorization Act. |
| 2007–08 | DNI Open Source Conferences (Reagan Building) institutionalise the field. |
| 2010 | DoD **Instruction 3115.12** unifies OSINT activities across DoD components. WikiLeaks disclosures reframe the secrecy debate. |

---

## The "five disciplines" frame

Bean situates OSINT as one of five intelligence disciplines:

1. **HUMINT** — Human intelligence.
2. **SIGINT** — Signals intelligence.
3. **IMINT / GEOINT** — Imagery / geospatial intelligence.
4. **MASINT** — Measurement and signature intelligence.
5. **OSINT** — Open source intelligence.

The Steele position: OSINT is a foundation for the other four. The OSC position: OSINT is the fifth, of equal rank. The engine, being civilian, operates **inside OSINT only** — but borrows tradecraft from the other four where the methodology is generalisable (notably HUMINT-derived interview protocols and IMINT-derived geolocation).

---

## Quotable passages

1. *"There are no secrets."* — Foreword, p. vii (Hart, opening line).
2. *"A virtual tidal wave of publicly printed paper threatens to swamp almost all enterprises of intellectual research."* — 1969 CIA study, quoted in Foreword, p. viii.
3. OSC vision: *"We are the nucleus of a global information enterprise serving U.S. national security interests."* — Ch 1, p. 5.
4. Aftergood: open-source products are withheld due to *"habit, the cultivation of the mystique of secret intelligence, the protection of copyrighted information, and the preservation of 'decision advantage.'"* — Ch 1, p. 5.
5. Aspin-Brown: open source *"took longer to produce, required validation, and failed to cover many key aspects of the situation important to policymakers."* — Ch 2.
6. Congress (Simmons): OSINT is *"intelligence that is produced from publicly available information collected, exploited, and disseminated in a timely manner to an appropriate audience for the purpose of addressing a specific intelligence requirement."* — Ch 4, p. 63.
7. Steele/NATO: OSINT is unclassified information *"deliberately discovered, discriminated, distilled, and disseminated to a select audience."* — Ch 4, p. 63.
8. Analyst quoted by Johnston: *"What we do is more art and experience than anything else."* — Ch 4, p. 81.
9. Fingar: *"if it ain't secret, it ain't real. If somebody is not cleared, they are not worthy. That is yesterday's thinking."* — Appendix, p. 156.
10. OSA Provost Kraus: *"There are very precise search and research strategies, that are not intuitive, to cull valuable information from the Internet."* — Appendix, p. 156.

---

## Companion reference

`references/osint-validation-and-anti-patterns.md` — operating discipline: validation cycles, source vetting, the speed/verification and volume/signal tensions, the Bean anti-pattern catalog (over-classification, factory-line outsourcing, "Googlification", single-advocate evidence gaps), positive cases (SARS early-warning, Aspin-Brown Burundi).

## Source

Bean, Hamilton. *No More Secrets: Open Source Information and the Reshaping of U.S. Intelligence*. Praeger Security International / ABC-CLIO, 2011. Tier 1.
