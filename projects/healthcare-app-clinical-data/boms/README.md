# Cohort — BOMs (bills of materials)

**Purpose:** define default kit composition (drugs, reagents, consumables) for every clinical event that produces auto-deduction in Medic8 — so when a clinician clicks "procedure done," stock decrements correctly without manual entry. This is catalogue #10 of the onboarding spec, the auto-deduction backbone.

## Scope (v1 — broad, all auto-deduction-bearing events)

Per design doc §11.2, every active row of the following catalogues must have an approved BOM at go-live:

1. **Lab tests** — reagent + consumable BOM per test (CBC, LFT, RFT, malaria RDT, GeneXpert, etc.)
2. **Imaging procedures** — contrast / film / gel / electrode BOM per procedure
3. **Vaccines** — AD syringe + reconstitution syringe + safety box per dose
4. **Surgical packs** — instrument + consumable BOM per pack (suturing, dressing, delivery, episiotomy, MVA, IUCD, circumcision, LP, paracentesis, chest-drain, abscess I&D, OT basic, laparotomy, C-section, hernia, hysterectomy)
5. **Maternity bundles** — delivery pack + cord clamp + vit K1 + tetracycline eye + chlorhexidine cord gel + baby wrap
6. **Dental procedures** — LA cartridge + gloves + mask + gauze + suction tip + bib per procedure
7. **Wound care / dressing** services — gauze, plaster, gloves
8. **Reusable theatre packs** vs single-use packs (each gets distinct BOM)

NOTE: BOM scope is intentionally broad here — the user has flagged this for review; can be narrowed to Tier-1 only if needed at consumption time.

## Data model (per spec)

```
bom_code, linked_kind, linked_id, version, effective_from, status,
default_yield_qty,
[ line items: item_id, qty_in_base_uom, allowed_substitutes,
  loss_factor_pct, critical_item ]
```

## Cross-cohort dependencies

- `linked_id` → `procedures`, `lab-tests`, `imaging`, `vaccines`, `workflows`, `tenant-blueprints`
- line `item_id` → `drugs`, `consumables`
- `loss_factor_pct` defaults derive from cohort-level rules (drugs ±5%, reagents ±15%, contrast ±10%, sterile sets ±0%)

## Hard exclusions (project-wide)

- BOMs for veterinary, traditional/herbal, cardiothoracic, neuro, transplant procedures (excluded at the parent catalogue level — no rows to map)

## Outputs

- `research/wave1-data.md` — table of BOMs with line items (likely a normalised two-table form: header + lines)
- `research/wave1-findings.md` — narrative on BOM derivation methodology, gap notes, sources
- `analysis/gap-analysis.md`
- `analysis/critical-reasoning-pass.md`
- `opportunities/product-ideas.md`

## Source tiers

- **T1:** WHO PEN protocols, IMCI charts, country STG, manufacturer-published surgical-pack composition standards, WHO PQS vaccine-injection-equipment specs.
- **T2:** Hospital procurement catalogues from UNICEF Supply Division, MSF Essential Drugs/Supplies List, peer-reviewed BOM studies.
- **T3:** Vendor catalogues — never sole source; only for SKU disambiguation.
