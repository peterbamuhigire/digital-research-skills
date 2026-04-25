"""Earliest-known-timestamp tracer.

Per Silverman + the Ottawa Shooting case: chronological provenance from
the earliest known timestamp, not from the loudest re-poster. This module
helps an agent collect candidate origins and pick the earliest defensibly.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass(slots=True)
class ProvenanceCandidate:
    url: str
    platform: str  # "twitter" | "reddit" | "blog" | "news" | "wayback" | ...
    timestamp: Optional[datetime] = None
    author: Optional[str] = None
    found_via: str = ""  # how we discovered this candidate
    confidence: float = 1.0  # 0.0–1.0


@dataclass(slots=True)
class ProvenanceTrace:
    artefact_id: str
    candidates: list[ProvenanceCandidate] = field(default_factory=list)

    def earliest(self) -> Optional[ProvenanceCandidate]:
        """Return the candidate with the earliest timestamp.

        Candidates without timestamps are excluded from "earliest" but kept
        in the trace for human review.
        """
        dated = [c for c in self.candidates if c.timestamp is not None]
        if not dated:
            return None
        return min(dated, key=lambda c: c.timestamp)  # type: ignore[return-value]


def trace_earliest_known(
    artefact_id: str, candidates: list[ProvenanceCandidate],
) -> ProvenanceTrace:
    """Group candidates and select the earliest defensibly known origin.

    The caller is responsible for finding candidates (e.g. by reverse-image
    search, retweet-walk, archive lookup). This function organises them.
    """
    return ProvenanceTrace(artefact_id=artefact_id, candidates=candidates)
