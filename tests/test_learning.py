import unittest

import numpy as np

from model.learning import AdaptiveSpecialists, Reliability
from model.perception import Perception, scene


class LearningTests(unittest.TestCase):
    def test_no_feedback_no_learning(self):
        r = Reliability()
        before = r.variance.copy()
        for _ in range(100):
            r.step([2, 0], [0, 0], .1)
        np.testing.assert_array_equal(before, r.variance)

    def test_learns_and_reverses_contingency(self):
        r = Reliability()
        for _ in range(2000):
            r.step([.25, 1], [1, 1], .1)
        np.testing.assert_allclose(r.variance, [.0625, 1], atol=.001)
        self.assertGreater(r.precision[0], 10 * r.precision[1])
        for _ in range(2000):
            r.step([1, .25], [1, 1], .1)
        np.testing.assert_allclose(r.variance, [1, .0625], atol=.001)

    def test_persistence_and_downstream_effect(self):
        agent = AdaptiveSpecialists()
        for _ in range(2000):
            agent.reliability.step([.25, 1], [1, 1], .1)
        learned = agent.reliability.variance.copy()
        agent.reset_trial()
        np.testing.assert_array_equal(learned, agent.reliability.variance)
        stimulus = np.stack([scene('horizontal', -.8, .8)] * 2)
        for _ in range(80):
            agent.step(stimulus, np.ones((2, 4)))
        # Same evidence, different retained reliability: faster supported estimate.
        self.assertGreater(abs(agent.specialists[0].z[0, 0]),
                           abs(agent.specialists[1].z[0, 0]) + .2)
        np.testing.assert_array_equal(learned, agent.reliability.variance)
        self.assertEqual(agent.state_vector().shape, (46,))

    def test_hidden_evidence_cannot_enter_any_state(self):
        a, b = Perception(), Perception()
        for _ in range(100):
            a.step([-.8, -1, 1, .8], [1, 0, 0, 1])
            b.step([-.8, 1, -1, .8], [1, 0, 0, 1])
        np.testing.assert_array_equal(a.state_vector(), b.state_vector())
        with self.assertRaises(ValueError):
            a.step([0] * 4, [1, float('nan'), 0, 1])

    def test_bounded_updates_and_invalid_feedback(self):
        r = Reliability()
        for _ in range(1000):
            r.step([0, 2], [1, 1], 1)
        self.assertTrue(np.all(r.variance >= r.minimum))
        self.assertTrue(np.all(r.variance <= r.maximum))
        with self.assertRaises(ValueError):
            r.step([0, float('nan')], [1, 1], .1)


if __name__ == '__main__':
    unittest.main()
