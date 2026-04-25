"""Beneficial-ownership walker.

Hetherington's UBO trace: walk parent (up) and subsidiary (down), then cross
to related parties via shared officers / addresses. Output is a graph.

Adapter functions live in `tools/registry/` — this module orchestrates them.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Iterator, Optional


@dataclass(slots=True)
class OwnershipNode:
    entity_id: str
    name: str
    jurisdiction: Optional[str] = None
    entity_type: str = "company"   # "company" | "person" | "trust" | "unknown"
    address: Optional[str] = None
    officers: list[str] = field(default_factory=list)
    parent_id: Optional[str] = None
    source: str = ""               # "Companies House" | "OpenCorporates" | "EDGAR" | ...


@dataclass(slots=True)
class OwnershipGraph:
    seed: OwnershipNode
    nodes: dict[str, OwnershipNode]   # id -> node
    edges: list[tuple[str, str, str]]  # (parent_id, child_id, relationship)

    def to_mermaid(self) -> str:
        """Render as a Mermaid graph for inclusion in a DD report."""
        lines = ["graph TD"]
        for nid, node in self.nodes.items():
            label = f"{node.name}\\n({node.jurisdiction or '?'})"
            lines.append(f'    {nid}["{label}"]')
        for p, c, rel in self.edges:
            lines.append(f"    {p} -->|{rel}| {c}")
        return "\n".join(lines)


def trace_ubo(
    seed_entity_id: str, seed_name: str, *,
    fetch_parent: Callable[[str], Optional[OwnershipNode]],
    fetch_subsidiaries: Callable[[str], list[OwnershipNode]],
    fetch_officers: Callable[[str], list[str]] = lambda _: [],
    max_depth_up: int = 5,
    max_depth_down: int = 3,
) -> OwnershipGraph:
    """Walk ownership graph up + down from a seed entity.

    Caller provides the registry adapters as callables — keeps this module
    independent of any specific registry. See `tools/registry/` for adapters.
    """
    seed = OwnershipNode(entity_id=seed_entity_id, name=seed_name)
    nodes: dict[str, OwnershipNode] = {seed_entity_id: seed}
    edges: list[tuple[str, str, str]] = []

    # Walk up
    current = seed
    for _ in range(max_depth_up):
        try:
            parent = fetch_parent(current.entity_id)
        except Exception:
            break
        if parent is None:
            break
        nodes.setdefault(parent.entity_id, parent)
        edges.append((parent.entity_id, current.entity_id, "owns"))
        current = parent

    # Walk down (BFS)
    frontier = [seed_entity_id]
    seen = {seed_entity_id}
    for _depth in range(max_depth_down):
        next_frontier: list[str] = []
        for nid in frontier:
            try:
                subs = fetch_subsidiaries(nid)
            except Exception:
                continue
            for sub in subs:
                if sub.entity_id in seen:
                    continue
                seen.add(sub.entity_id)
                nodes.setdefault(sub.entity_id, sub)
                edges.append((nid, sub.entity_id, "owns"))
                next_frontier.append(sub.entity_id)
        frontier = next_frontier

    # Officer enrichment for each node
    for nid, node in list(nodes.items()):
        try:
            node.officers = fetch_officers(nid)
        except Exception:
            pass

    return OwnershipGraph(seed=seed, nodes=nodes, edges=edges)


def find_shared_officers(graphs: list[OwnershipGraph]) -> dict[str, list[str]]:
    """Across ≥1 ownership graph, find officers that appear in multiple entities.
    Strong signal of related-party network / shell ring."""
    occurrences: dict[str, list[str]] = {}
    for g in graphs:
        for nid, node in g.nodes.items():
            for officer in node.officers:
                occurrences.setdefault(officer, []).append(node.name)
    return {k: v for k, v in occurrences.items() if len(set(v)) > 1}


def find_shared_addresses(graphs: list[OwnershipGraph]) -> dict[str, list[str]]:
    """Across ≥1 ownership graph, find addresses shared by multiple entities."""
    occurrences: dict[str, list[str]] = {}
    for g in graphs:
        for nid, node in g.nodes.items():
            if node.address:
                occurrences.setdefault(node.address, []).append(node.name)
    return {k: v for k, v in occurrences.items() if len(set(v)) > 1}
