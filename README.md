# Hyperobjectivity

Hyperobjectivity asks how a **hyperform** can have identifiable **hyperobject** instances across situated presentations without confusing an object with its appearance, a name, or a subject's account of it. Tyler proposed this separate field while developing a forms → hyperforms → hyperobjects → new hyperemergents cycle.

The proposed definition is **[FRAME]**: an explicit construction with unresolved obligations, not a native derivation or an empirical claim. The finite [executable witness](hyperobjectivity.py) tests claimed lineage and presentation invariance; it does not certify hyperform closure, object existence, or transport soundness. See [FIELD_SPEC.md](FIELD_SPEC.md) for the contract and [PROVENANCE.md](PROVENANCE.md) for inspected source commitments.

This field is distinct from Hyperstructure, whose local research candidate owns recursive whole and closure conditions, and [Hypersubjectivity](https://github.com/TimeLordRaps/hypersubjectivity), which owns situated first-person relations. Hyperstructure has no public repository at this writing. Hyperobjectivity supplies a **candidate object boundary** for Hypersubjectivity; it cannot turn subjective agreement into objective identity.

Run the full local suite with Python 3.10 or later:

```text
python -u -m unittest discover -s tests -v
```

The suite uses only the standard library and prints each test outcome. Tests complete rapidly in the inspected environment, but standard-library `unittest` provides no per-test process isolation or automatic stack dump if a test hangs. No physical unit is assigned to forms, identities, or reality-kind labels. [TECHNICAL_DEBT.md](TECHNICAL_DEBT.md) names what remains open.
