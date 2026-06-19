# OSINT Case Vaults

This reference covers case-memory architecture for OSINT work: how to store
notes, evidence assets, pivots, and source trails so an investigation remains
repeatable.

It is tool-agnostic, but the trigger sources here are Obsidian and public
Obsidian OSINT templates.

## When To Use

Load this reference when:

- an OSINT project has many entities, sources, screenshots, or pivots;
- the analyst needs a repeatable case notebook;
- multiple analysts need the same note structure;
- the output must explain activities, uncertainty, and evidence provenance.

## Architecture

Use a markdown-first case vault with separate folders for:

- `cases/` - case-level briefs, status, scope, and questions;
- `entities/` - people, organisations, usernames, domains, wallets, locations;
- `sources/` - source notes linked to `_registry/sources.yaml`;
- `claims/` - claim notes linked to `_registry/claims.yaml`;
- `assets/` - screenshots, downloaded records, PDFs, images, and exports;
- `logs/` - activity logs, queries, tool runs, and review notes;
- `templates/` - standard note templates;
- `outputs/` - report drafts and released artefacts.

Each note should be plain text Markdown. This keeps the material portable,
diffable, searchable, and easy to pack into the engine's release bundle.

## Required Note Fields

Case note:

```yaml
case_id:
status:
question:
scope:
legal_ethics_bound:
opened_at:
owner:
```

Entity note:

```yaml
entity_id:
entity_type:
display_name:
known_identifiers:
source_ids:
confidence:
status:
```

Source note:

```yaml
source_id:
url_or_ref:
tier:
accessed:
archive_ref:
verification:
confidence:
```

Activity log:

```yaml
logged_at:
actor:
tool_or_method:
query_or_action:
source_ids:
result_summary:
next_pivot:
```

## Vault Rules

- Every note that supports a finding links to a registry ID.
- Screenshots are supporting artefacts, not sources by themselves.
- Tool output is a lead until verified against the underlying source.
- Activity logs record failed searches and dead ends; gaps are evidence.
- Relationship maps must distinguish observed links from inferred links.
- Local-first storage is preferred for sensitive investigative metadata.
- If sync is used, document the sync provider, encryption posture, access list,
  and version-history behaviour.

## Obsidian-Specific Pattern

Obsidian is useful because it stores notes locally as plain text Markdown, uses
links between notes, supports graph / canvas views, and has plugins such as
Dataview and Tasks. The official site states that notes are stored locally as
plain text Markdown files and that plugins can tailor the workflow.

The WebBreacher `obsidian-osint-templates` repository is a practical template
source. It includes folders such as templates, standard operating procedures,
and an example case, and its README describes the templates as suggestions for
using Obsidian during an OSINT investigation.

Adopt cautiously:

- Use templates for structure, not as evidence.
- Keep the engine registries as the canonical source / claim control plane.
- Treat graph and canvas views as analytic aids, not proof of relationships.
- Store exported notes and assets inside project workspaces before release.

## Source Notes

- Obsidian homepage: https://obsidian.md/. Accessed 2026-05-16. Official
  product source for local Markdown storage, note links, graph, Canvas, plugins,
  Sync, and Publish.
- WebBreacher `obsidian-osint-templates`:
  https://github.com/WebBreacher/obsidian-osint-templates. Accessed
  2026-05-16. Practitioner template repository for OSINT note structure.
- Neon Maxima, "How I Turned Obsidian Into a Black-Ops Intelligence Hub...",
  Medium, 2025-10-08:
  https://medium.com/@neonmaxima/how-i-turned-obsidian-into-a-black-ops-intelligence-hub-and-why-you-should-too-a1534b39ec5e.
  Useful as a tier-5 workflow prompt for folders, assets, Dataview-style
  dashboards, Canvas maps, local-first storage, encryption, and versioning.
