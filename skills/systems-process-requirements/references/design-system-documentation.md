# Design System Documentation

Use this reference when describing or specifying a design system, component library, UI pattern library, token system, reusable interaction model, or product design governance.

## Design System Purpose

A design system is a shared product language. It reduces design debt, speeds delivery, improves consistency, and gives teams reusable standards for visual design, interaction, content, accessibility, and implementation.

## Discovery Workflow

1. **UI audit.** Inventory repeated buttons, forms, colors, typography, layouts, icons, messages, tables, navigation, and state patterns.
2. **Group patterns.** Identify duplicates, variants, inconsistencies, and missing rules.
3. **Define foundations.** Tokens for color, type, spacing, radius, elevation, iconography, motion, content voice, and accessibility.
4. **Define components.** Name, purpose, anatomy, variants, states, behavior, content rules, accessibility, code/design assets.
5. **Define patterns.** Cross-component solutions such as forms, filters, tables, dashboards, empty states, onboarding, errors.
6. **Set governance.** Ownership, contribution workflow, release process, versioning, deprecation, quality checks.
7. **Adoption plan.** Migration, training, support, metrics, feedback loop.

## Component Card

| Field | Description |
|---|---|
| Name | Preferred component name |
| Purpose | What user/system problem it solves |
| Use when | Appropriate situations |
| Do not use when | Misuse boundaries |
| Anatomy | Parts of the component |
| Variants | Supported forms |
| States | Default, hover, focus, disabled, loading, error, success, empty |
| Behavior | Interaction and responsive behavior |
| Content rules | Labels, helper text, error messages |
| Accessibility | Keyboard, focus, contrast, ARIA/semantic expectations |
| Code/design source | Link/path to implementation or design file |
| Owner/version | Maintenance accountability |

## Pattern Card

| Pattern | Problem | Components used | Rules | Example | Accessibility | Owner |
|---|---|---|---|---|---|---|

## Governance Minimum

- Contribution criteria.
- Review roles.
- Release cadence.
- Versioning.
- Deprecation policy.
- Testing/accessibility checks.
- Documentation standard.
- Support channel.
- Adoption metrics.

## Anti-Patterns

- Component library with no usage rules.
- Tokens that do not map to implementation.
- Unversioned system used by multiple teams.
- Governance dependent on one person.
- Visual consistency with broken interaction or accessibility.
- Documentation that shows examples but not when to use or avoid them.

## Ship Gate

- [ ] UI audit or source inventory exists.
- [ ] Tokens and foundations are named.
- [ ] Components have purpose, anatomy, variants, states, behavior, and accessibility notes.
- [ ] Patterns show multi-component use.
- [ ] Governance and contribution rules exist.
- [ ] Versioning and deprecation are handled.
- [ ] Adoption and migration plan is realistic.
