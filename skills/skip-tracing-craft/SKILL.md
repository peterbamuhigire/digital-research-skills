---
name: skip-tracing-craft
description: Use to find people who don't want to be found — driver-license-first chain, court-docket trick, FOIA address-correction, database router. With FCRA / DPPA permissible-purpose gates. From McMahon's Practical Handbook for Private Investigators.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
    - generic-agent
---

# Skip-tracing craft

McMahon: *unintentional, intentional, marital, criminal* — four kinds of skip. Each warrants a different intensity.

## The standard process

1. **Review in-house records first** — most "lost" people are findable in your own files
2. **Build profile sheet** — all known identifiers (DL, DOB, SSN, employer, phone, family, known associates)
3. **Flow chart** searches; **activity log** so subpoenaed records hold up
4. **Public-records sweep** → **commercial database** → **internet** → **interviews of family/friends/employers/enemies (especially ex-spouses)**
5. **Driver's license = the highest-yield identifier** (DOB + often SSN + photo)
6. **Reverse phone, criss-cross address, old city directories** for prior addresses
7. **Court records** — traffic tickets reveal current home address; civil dockets list every party's address; criminal dockets list defendants and witnesses
8. **State Division of Corporations** — officers + registered agents (out-of-state corps must register)
9. **FOIA address-correction trick** — send mail marked *"Do Not Forward — Address Correction Requested"*; USPS returns the new address

## Database router (FCRA / DPPA / GLBA gated)

| Source | Gate | Purpose |
|---|---|---|
| Driver's license | DPPA §2721(b)(3)/(b)(8) | Primary identifier |
| Voter registration | Open | Current address |
| Property records | Open | Real estate ownership |
| Court dockets | Open (mostly) | Address from any case |
| State Division of Corporations | Open | Officers + registered agents |
| Vital statistics | Open (varies state) | Birth / death / marriage |
| Credit header | FCRA §604 | Address + employer (no full pull without permissible purpose) |
| Commercial DB (Accurint, TLO, CLEAR) | Licensee + permissible purpose | Aggregated cross-source |

## The interview chain

Interviewees in priority order:
1. Family (current + estranged)
2. Ex-spouse(s) — McMahon's strongest signal
3. Former employers + supervisors
4. Old neighbours
5. Known associates / friends
6. Religious community (varies by subject)
7. Hobby groups (gun club, fishing, motorcycle, etc.)

## FCRA / DPPA permissible-purpose gate

Skip-tracing requires lawful basis. Before any commercial-DB pull or DMV query:
- Document the permissible purpose
- For DPPA: §2721(b)(3) (litigation), §2721(b)(8) (licensed-PI investigative purposes — state-by-state opt-in)
- For FCRA: §604 (court order, judgment, collection of an account, fraud detection)

The engine's `pi-legal-and-ethical-bounds` skill enforces this.

## Statute backbone

- **FCRA** (revised July 1999) — credit-data use; permissible purposes
- **Privacy Act 1974** — federal-agency PII
- **FERPA / Buckley Amendments** — school records
- **Right to Financial Privacy Act**
- **DPPA** — DMV; state opt-in for PI use
- **GLBA §521** — pretexting financial info = federal crime

## Anti-patterns

- Pulling full credit report without permissible purpose
- DMV query without DPPA basis
- Pretexting at the bank for current-employment confirmation (GLBA federal crime)
- Calling family with deceptive cover story (state law varies; ethical line)
- Using residential proxies to defeat per-IP rate limits as a habit
- Reporting the new address to a third party without the requesting party's authority

## See also

- `tools/dd/identity_triangulator.py` — anti-defamation layer when you have a candidate
- `pi-legal-and-ethical-bounds` — gates above
- `pi-report-writing` — output format
- `evidence-discipline` — citation rules
