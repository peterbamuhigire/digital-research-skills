# Anti-slop overlay pressure fixture

These examples are deliberately tempting, polished defaults. Each finding needs human or
tool-backed evidence before it becomes a real defect; keyword presence alone is insufficient.

- AS1: A dark SaaS landing page uses a purple-to-blue gradient, a fashionable display face, and a
  three-column hero layout because the generator selected its default, with no brief or design
  system reason.
- AS2: A tiny uppercase eyebrow, pill chip, numbered section label, icon tile, and oversized hero
  metric all announce importance without changing what the user can understand or do.
- AS3: Six identical icon-heading-copy cards are nested inside a rounded summary card, with the
  same spacing between every item and no distinction in information priority.
- AS4: A static “systems operational” dot pulses, a non-editable headline shows a blinking cursor,
  and a decorative marquee moves continuously without a state change or task benefit.
- AS5: A hero illustration is assembled from generic SVG blobs, the supplied image is hidden under
  an opaque wash, and a missing asset is left as a placeholder instead of being removed.
- AS6: The page repeats “supercharge”, “world-class”, em-dash-heavy clauses, “not X, but Y” lines,
  and “we killed the theater” framing until the cadence announces itself.
- AS7: Entrance animations leave content at opacity zero, body text falls below readable contrast,
  a menu is clipped by overflow, and a long line spills horizontally beneath the polished shell.

Functional exception: a repeated “Stop service / Verify state / Roll back” sequence remains because
it is an operational recovery procedure; a repeated required field remains because it preserves
traceability; a repeated focus label remains because it supports accessibility. Record the reason
and use `not_applicable` or `not_assessed` where the overlay cannot be evidenced.
