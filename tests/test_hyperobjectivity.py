import unittest

from hyperobjectivity import (
    Form,
    HyperformClaim,
    HyperobjectClaim,
    Presentation,
    Transport,
    Registry,
)


class ObjectivityFrameTests(unittest.TestCase):
    def frame(self, *, transported=True, value_a="stable", value_b="stable"):
        forms = (Form("f"),)
        hyperforms = (HyperformClaim("h", ("f",), "closure-claim-1"),)
        objects = (HyperobjectClaim("o", "h"),)
        presentations = (
            Presentation("p-base", "o", "base-reality", "seen-a", (("trait", value_a),)),
            Presentation("p-areal", "o", "areality", "seen-b", (("trait", value_b),)),
        )
        transports = (
            (Transport("p-base", "p-areal", "bridge-claim-1"),)
            if transported else ()
        )
        return Registry(forms, hyperforms, objects, presentations, transports)

    def test_finite_invariant_requires_declared_cross_kind_transport(self):
        self.assertEqual(self.frame().invariant("o", "trait").status, "PASS")
        self.assertEqual(self.frame(transported=False).invariant("o", "trait").status, "UNKNOWN")

    def test_conflicting_value_refutes_declared_invariant(self):
        self.assertEqual(self.frame(value_b="changed").invariant("o", "trait").status, "FAIL")

    def test_same_appearance_does_not_merge_different_objects(self):
        frame = Registry(
            (Form("f"),),
            (HyperformClaim("h", ("f",), "closure-claim-1"),),
            (HyperobjectClaim("o1", "h"), HyperobjectClaim("o2", "h")),
            (Presentation("p1", "o1", "base-reality", "same", (("trait", "x"),)),
             Presentation("p2", "o2", "base-reality", "same", (("trait", "x"),))),
            (),
        )
        self.assertEqual(frame.invariant("o1", "trait").status, "UNKNOWN")
        self.assertEqual(frame.invariant("o2", "trait").status, "UNKNOWN")
        self.assertEqual(frame.same_object_candidate("p1", "p2").status, "FAIL")

    def test_same_kind_and_same_claimed_id_still_need_presentation_transport(self):
        frame = Registry(
            (Form("f"),),
            (HyperformClaim("h", ("f",), "closure-claim-1"),),
            (HyperobjectClaim("o", "h"),),
            (Presentation("p1", "o", "base-reality", "a", (("trait", "x"),)),
             Presentation("p2", "o", "base-reality", "b", (("trait", "x"),))),
            (),
        )
        self.assertEqual(frame.same_object_candidate("p1", "p2").status, "UNKNOWN")
        self.assertEqual(frame.invariant("o", "trait").status, "UNKNOWN")

    def test_unknown_form_reference_is_rejected(self):
        with self.assertRaises(ValueError):
            Registry(
                (Form("f"),),
                (HyperformClaim("h", ("missing",), "closure-claim-1"),),
                (HyperobjectClaim("o", "h"),),
                (Presentation("p", "o", "base-reality", "a", ()),),
                (),
            )

    def test_missing_property_is_unknown(self):
        self.assertEqual(self.frame().invariant("o", "absent").status, "UNKNOWN")


if __name__ == "__main__":
    unittest.main()
