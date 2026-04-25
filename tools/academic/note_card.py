"""Note-card store — Trzeciak's source-away composition discipline.

The central insight from Trzeciak: plagiarism is a workflow failure, not a
moral one. You cannot copy what is not in front of you. The note card is
the structural defence: one point per card, with full source provenance,
and a personal-comment field that becomes the seed of original argument.

When the engine generates prose from notes, the source text MUST be removed
from the active context. Generation reads only from cards. This is the
"source-away gate".
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass(slots=True)
class NoteCard:
    """One atomic point per card. Bailey + Trzeciak both endorse this.

    Notes that look like prose produce plagiarism.
    Notes that look like fragments produce paraphrase.
    """

    id: str
    project_id: str
    heading: str                      # short topic
    point: str                        # the actual finding/claim — NEVER a full source sentence
    source_id: str                    # which source this came from
    source_page: Optional[str] = None
    is_quote: bool = False            # True if `point` is a verbatim quote
    quote_marks_required: bool = False  # if True, must format as direct quote in prose
    personal_comment: str = ""        # the writer's own reaction — seed of argument
    captured_at: datetime = field(default_factory=datetime.now)
    tags: list[str] = field(default_factory=list)


@dataclass(slots=True)
class NoteCardStore:
    """A collection of cards keyed by id. Persists to JSON for resumability."""

    project_id: str
    cards: dict[str, NoteCard] = field(default_factory=dict)

    def add(self, card: NoteCard) -> None:
        self.cards[card.id] = card

    def by_source(self, source_id: str) -> list[NoteCard]:
        return [c for c in self.cards.values() if c.source_id == source_id]

    def by_tag(self, tag: str) -> list[NoteCard]:
        return [c for c in self.cards.values() if tag in c.tags]

    def quotes(self) -> list[NoteCard]:
        return [c for c in self.cards.values() if c.is_quote]

    def paraphrases(self) -> list[NoteCard]:
        return [c for c in self.cards.values() if not c.is_quote]

    def save(self, path: str | Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "project_id": self.project_id,
            "cards": [
                {
                    "id": c.id,
                    "heading": c.heading,
                    "point": c.point,
                    "source_id": c.source_id,
                    "source_page": c.source_page,
                    "is_quote": c.is_quote,
                    "quote_marks_required": c.quote_marks_required,
                    "personal_comment": c.personal_comment,
                    "captured_at": c.captured_at.isoformat(),
                    "tags": c.tags,
                }
                for c in self.cards.values()
            ],
        }
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: str | Path) -> "NoteCardStore":
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        store = cls(project_id=data["project_id"])
        for c in data["cards"]:
            store.add(NoteCard(
                id=c["id"],
                project_id=data["project_id"],
                heading=c["heading"],
                point=c["point"],
                source_id=c["source_id"],
                source_page=c.get("source_page"),
                is_quote=c.get("is_quote", False),
                quote_marks_required=c.get("quote_marks_required", False),
                personal_comment=c.get("personal_comment", ""),
                captured_at=datetime.fromisoformat(c["captured_at"]),
                tags=c.get("tags", []),
            ))
        return store


def validate_note_card(card: NoteCard, *, max_words_for_paraphrase: int = 25) -> list[str]:
    """Validate a card against the discipline rules.

    Returns a list of warning strings (empty = valid).
    """
    warnings: list[str] = []

    # Paraphrased points should be short — full source sentences are a smell.
    word_count = len(card.point.split())
    if not card.is_quote and word_count > max_words_for_paraphrase:
        warnings.append(
            f"Paraphrase point is {word_count} words — likely sentence-shaped. "
            "Compress to a fragment to prevent prose-copying."
        )

    # Quote cards must have quote-marks-required flag set
    if card.is_quote and not card.quote_marks_required:
        warnings.append("Quote card missing quote_marks_required flag — set True.")

    # Quote cards must have a page reference
    if card.is_quote and not card.source_page:
        warnings.append("Quote card missing source_page — required for citation.")

    # Personal comment is encouraged for paraphrases (seed of argument)
    if not card.is_quote and not card.personal_comment:
        warnings.append(
            "Paraphrase card missing personal_comment — Trzeciak: comment is "
            "the seed of original argument."
        )

    return warnings
