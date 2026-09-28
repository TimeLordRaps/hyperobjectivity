# Technical debt and open proof obligations

| ID | Status | Location and consequence | Closure check / revisit |
|---|---|---|---|
| HO-1 | OPEN | `FIELD_SPEC.md`: no native rule constructs a hyperobject from a closed or closing hyperform; identifiers can only carry claimed ancestry. | Derive a typed instantiation rule with a non-instance countermodel; revisit before any claim labeled `[FORM]` (closed by a stated formal derivation). |
| HO-2 | OPEN | `hyperobjectivity.py`: transport references are unverified and pairwise; a declared loop can pass finite checks without a sound compositional law. | Define and test composition, inverses where applicable, and identity preservation; revisit before cross-kind promotion. |
| HO-3 | OPEN | `FIELD_SPEC.md`: hypergeometric reality has no field-local kind definition or source bridge. | Define its distinction and map to other reality kinds without ranking or equating it with Hypergeometry; revisit on the next reality taxonomy change. |
| HO-4 | OPEN | Finite registry coverage is caller-declared; an omitted presentation can make an invariant appear stable. | Add a source-bound completeness/coverage contract and adversarial omission case; revisit before certification or public invariant claims. |

Passing tests resolve none of these obligations. A `PASS` is scoped to supplied finite records; `UNKNOWN` remains the outcome where the required evidence is absent.

## Bounded sniff-audit state

At coherent checkpoint 2 on 2026-09-27, inspected the risk hotspot (`invariant` falsely passing one presentation or an unwitnessed same-kind comparison) and the neglected public-doc/link surface. The weak inference was reproduced RED and repaired GREEN; the public Hyperstructure link was removed because that repository is not live. An actual PowerShell `Get-Random -Minimum 3 -Maximum 8` draw returned **6**. Next sampled audit is due at checkpoint **8**, or earlier on a relevant contract/source change. Rotate next to serialization/import and omitted-presentation coverage.
