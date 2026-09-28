"""Finite [FRAME] for claimed hyperobject lineage and presentation invariance.

The identifiers and witness references below are declarations. A PASS means only
that the registered finite claims meet this contract; it does not prove that a
hyperform has closed, that an object exists, or that a transport is sound.
"""

from dataclasses import dataclass
from itertools import combinations


@dataclass(frozen=True)
class Result:
    status: str
    reason: str


@dataclass(frozen=True)
class Form:
    identifier: str


@dataclass(frozen=True)
class HyperformClaim:
    identifier: str
    source_forms: tuple[str, ...]
    closure_claim: str


@dataclass(frozen=True)
class HyperobjectClaim:
    identifier: str
    hyperform: str


@dataclass(frozen=True)
class Presentation:
    identifier: str
    object_id: str
    reality_kind: str
    appearance: str
    traits: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class Transport:
    source_presentation: str
    target_presentation: str
    witness_claim: str


def _index(items, label):
    indexed = {}
    for item in items:
        identifier = item.identifier
        if not identifier or identifier in indexed:
            raise ValueError(f"{label} identifiers must be nonempty and unique")
        indexed[identifier] = item
    return indexed


@dataclass(frozen=True)
class Registry:
    forms: tuple[Form, ...]
    hyperforms: tuple[HyperformClaim, ...]
    objects: tuple[HyperobjectClaim, ...]
    presentations: tuple[Presentation, ...]
    transports: tuple[Transport, ...]

    def __post_init__(self):
        forms = _index(self.forms, "form")
        hyperforms = _index(self.hyperforms, "hyperform")
        objects = _index(self.objects, "object")
        presentations = _index(self.presentations, "presentation")
        for h in self.hyperforms:
            if not h.source_forms or not h.closure_claim or any(f not in forms for f in h.source_forms):
                raise ValueError("hyperform claim needs known source forms and a closure claim reference")
            if len(set(h.source_forms)) != len(h.source_forms):
                raise ValueError("duplicate source form")
        for obj in self.objects:
            if obj.hyperform not in hyperforms:
                raise ValueError("object claim references unknown hyperform")
        for p in self.presentations:
            if p.object_id not in objects or not p.reality_kind:
                raise ValueError("presentation needs known object and nonempty reality kind")
            keys = [key for key, _ in p.traits]
            if any(not key for key in keys) or len(keys) != len(set(keys)):
                raise ValueError("trait names must be nonempty and unique per presentation")
        seen = set()
        for t in self.transports:
            a = presentations.get(t.source_presentation)
            b = presentations.get(t.target_presentation)
            if a is None or b is None or a.identifier == b.identifier or not t.witness_claim:
                raise ValueError("transport needs two known distinct presentations and witness claim")
            if a.object_id != b.object_id:
                raise ValueError("presentation transport must retain claimed object id")
            key = frozenset((a.identifier, b.identifier))
            if key in seen:
                raise ValueError("duplicate transport pair")
            seen.add(key)

    def _transported(self, a: Presentation, b: Presentation) -> bool:
        if a.identifier == b.identifier:
            return True
        pair = frozenset((a.identifier, b.identifier))
        return any(frozenset((t.source_presentation, t.target_presentation)) == pair
                   for t in self.transports)

    def same_object_candidate(self, first: str, second: str) -> Result:
        by_id = _index(self.presentations, "presentation")
        a, b = by_id[first], by_id[second]
        if a.object_id != b.object_id:
            return Result("FAIL", "different claimed object identifiers; matching appearances do not merge them")
        if not self._transported(a, b):
            return Result("UNKNOWN", "presentation continuity lacks a declared transport")
        return Result("PASS", "same claimed object and declared presentation continuity in this finite registry")

    def invariant(self, object_id: str, trait: str) -> Result:
        if object_id not in _index(self.objects, "object") or not trait:
            raise ValueError("known object and nonempty trait required")
        views = [p for p in self.presentations if p.object_id == object_id]
        if len(views) < 2:
            return Result("UNKNOWN", "at least two registered presentations are needed to test invariance")
        values = [dict(p.traits).get(trait) for p in views]
        if any(value is None for value in values):
            return Result("UNKNOWN", "trait absent in at least one registered presentation")
        if len(set(values)) != 1:
            return Result("FAIL", "registered presentations disagree on the proposed invariant")
        if any(not self._transported(a, b) for a, b in combinations(views, 2)):
            return Result("UNKNOWN", "at least one presentation comparison lacks a declared transport")
        return Result("PASS", "trait agrees across all registered presentations under declared transports")
