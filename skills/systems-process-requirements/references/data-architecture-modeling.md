# Data Architecture Modeling

Use this reference when describing data, entities, attributes, data quality, master data, governance, database design inputs, or data architecture.

## Data Modeling Workflow

1. **Gather source material.** Requirements, forms, reports, policies, screens, exports, databases, interviews, and process maps.
2. **Extract candidate entities.** Look for nouns that represent things the organization tracks.
3. **Normalize vocabulary.** Record synonyms, preferred terms, and ambiguous terms.
4. **Define entities.** State what each entity is and is not.
5. **List attributes.** Include type, format, required/optional, valid values, source, owner, and sensitivity.
6. **Identify relationships.** Cardinality, optionality, parent/child, lifecycle dependencies.
7. **Attach rules.** Validation, uniqueness, retention, security, stewardship, and quality rules.
8. **Review for feedback.** Validate with domain stakeholders and data owners.
9. **Model for implementation.** Convert conceptual model into logical/physical design only after the business meaning is stable.

## Entity Card

| Field | Description |
|---|---|
| Entity name | Preferred business term |
| Definition | Clear inclusion/exclusion boundary |
| Synonyms | Other names used in sources |
| Source | Form, report, system, interview, policy |
| Owner/steward | Accountable role |
| Key attributes | Main descriptive fields |
| Identifier | Natural/surrogate key candidate |
| Relationships | Linked entities and cardinality |
| Rules | Validation, uniqueness, lifecycle |
| Quality risks | Completeness, consistency, timeliness, accuracy |

## Data Dictionary Minimum

| Entity | Attribute | Definition | Type/format | Required | Valid values | Source | Owner | Quality rule |
|---|---|---|---|---|---|---|---|---|

## Data Quality And Governance Questions

- Who creates the data?
- Who approves it?
- Who updates it?
- Who consumes it?
- Where is the source of truth?
- What is master/reference/transactional/derived data?
- What are the key quality dimensions?
- What rules prevent duplicates, stale records, or inconsistent definitions?
- What data is sensitive, regulated, or access-controlled?

## Anti-Patterns

- Starting with tables before business definitions.
- Treating two synonyms as two entities.
- Treating two different concepts as one entity because they share a label.
- Data dictionary with names but no definitions.
- Ignoring source-of-truth and stewardship.
- No feedback cycle with business users.

## Ship Gate

- [ ] Entities have definitions and exclusions.
- [ ] Synonyms and ambiguous terms are resolved.
- [ ] Attributes have type, format, source, and quality rule.
- [ ] Relationships and cardinality are stated.
- [ ] Data owners/stewards are identified or marked as gaps.
- [ ] Master/reference/transactional/derived data distinctions are made where relevant.
- [ ] Implementation model does not outrun validated business meaning.
