import unittest

import numpy as np

from model.perception import GROUPS, Perception, PerceptionParameters, scene
from model.primitives import quality_decode, quality_encode


def settle(samples, visible=None, duration=20, prior=None, parameters=None):
    model = Perception(parameters)
    visible = np.ones(4) if visible is None else np.asarray(visible)
    for _ in range(round(duration / model.p.dt)):
        model.step(samples, visible, prior=prior)
    return model


class PerceptionTests(unittest.TestCase):
    def test_partial_aperture_does_not_change_inferred_object_quality(self):
        for aperture in (.5, .75, 1):
            m = settle(scene('horizontal', -.8, .8), np.full(4, aperture), duration=80)
            self.assertEqual(m.result()['group'], 'horizontal')
            np.testing.assert_allclose(m.result()['qualities'], [-.8, .8], atol=.08)

    def test_ambiguous_feedback_does_not_bias_observed_qualities(self):
        m = settle(scene('horizontal', -.8, .8), [1, 0, 0, 1])
        np.testing.assert_allclose(m.result()['qualities'], [-.8, .8], atol=.08)
        self.assertLess(abs(m.group[0] - m.group[1]), .01)

    def test_feedback_changes_dynamics_not_fitted_equilibrium(self):
        enabled, disabled = Perception(), Perception()
        samples = scene('horizontal', -.8, .8)
        for _ in range(80):
            enabled.step(samples, [1, 1, 1, 1])
            disabled.step(samples, [1, 1, 1, 1], feedback=False)
        self.assertGreater(abs(enabled.z[0, 0]), abs(disabled.z[0, 0]) + .01)
        for _ in range(800):
            enabled.step(samples, [1, 1, 1, 1])
            disabled.step(samples, [1, 1, 1, 1], feedback=False)
        np.testing.assert_allclose(enabled.result()['qualities'], disabled.result()['qualities'], atol=.001)

    def test_spatial_reorganization_with_identical_histogram(self):
        horizontal = scene("horizontal", -.73, .61)
        vertical = scene("vertical", -.73, .61)
        np.testing.assert_equal(np.sort(horizontal), np.sort(vertical))
        for group, samples in [("horizontal", horizontal), ("vertical", vertical)]:
            m = settle(samples)
            self.assertEqual(m.result()["group"], group)
            self.assertGreater(max(m.group), .95)

    def test_one_object_is_distinct_from_two_objects(self):
        m = settle(scene("one_object", .37, -.9))
        self.assertEqual(m.result()["group"], "one_object")
        self.assertGreater(m.group[2], .95)

    def test_unseen_continuous_qualities_generalize(self):
        # No fitting: points deliberately not population-code centers.
        for first, second in [(-.83, .67), (.19, -.74), (-.37, .46)]:
            for group in GROUPS[:2]:
                m = settle(scene(group, first, second))
                self.assertEqual(m.result()["group"], group)
                np.testing.assert_allclose(m.result()["qualities"], [first, second], atol=.08)

    def test_diagonal_only_is_ambiguous(self):
        m = settle(scene("horizontal", -.8, .8), [1, 0, 0, 1])
        self.assertLess(abs(m.group[0] - m.group[1]), .01)
        self.assertLess(max(m.group), .7)

    def test_reveal_disambiguates_without_label_input(self):
        samples = scene("vertical", -.8, .8)
        m = settle(samples, [1, 0, 0, 1])
        for _ in range(800):
            m.step(samples, np.ones(4))
        self.assertEqual(m.result()["group"], "vertical")
        self.assertGreater(m.group[1], .95)

    def test_prior_changes_ambiguous_grouping(self):
        samples = scene("vertical", -.8, .8)
        mask = [1, 0, 0, 1]
        h = settle(samples, mask, prior=[.04, 0, 0])
        v = settle(samples, mask, prior=[0, .04, 0])
        self.assertGreater(h.group[0], v.group[0] + .5)

    def test_population_is_sparse_continuous_and_used_for_readout(self):
        values = np.linspace(-1, 1, 401)
        code = quality_encode(values)
        self.assertLessEqual(np.max(np.sum(code > 1e-10, axis=1)), 3)
        self.assertLess(np.max(np.linalg.norm(np.diff(code, axis=0), axis=1)), .05)
        self.assertLess(np.max(np.abs(quality_decode(code) - values)), .08)
        m = settle(scene("horizontal", -.7, .7))
        m.quality[:] = quality_encode([.8, -.8])
        np.testing.assert_allclose(m.result()["qualities"], quality_decode(m.quality))
        self.assertGreater(m.result()["qualities"][0], .7)

    def test_time_step_convergence(self):
        samples = scene("horizontal", -.63, .72)
        a = settle(samples, duration=8)
        b = settle(samples, duration=8, parameters=PerceptionParameters(dt=.0125))
        np.testing.assert_allclose(a.state_vector(), b.state_vector(), atol=.005)

    def test_state_inventory_and_roundtrip(self):
        a = settle(scene("horizontal", -.7, .7), duration=2)
        b = Perception()
        b.set_state(a.state_vector())
        self.assertEqual(len(a.state_vector()), 22)
        a.step(np.zeros(4), np.ones(4))
        b.step(np.zeros(4), np.ones(4))
        np.testing.assert_equal(a.state_vector(), b.state_vector())

    def test_invalid_inputs_fail(self):
        with self.assertRaises(ValueError):
            PerceptionParameters(dt=1)
        with self.assertRaises(ValueError):
            Perception().step([2, 0, 0, 0], [1, 1, 1, 1])
        with self.assertRaises(ValueError):
            quality_encode(float("nan"))


if __name__ == "__main__":
    unittest.main()
