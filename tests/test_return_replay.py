import unittest
import numpy as np
from model.agent import Agent
from experiments.return_replay import evaluate


class ReturnReplayTests(unittest.TestCase):
    def test_null_and_small_perturbation_controls(self):
        null = evaluate(0)
        small = evaluate(.1)
        self.assertEqual(null['perturbed_max_state_difference'],0)
        self.assertGreater(small['perturbed_max_state_difference'],0)
        self.assertLess(small['live_perturbed_active_time'],small['replay_perturbed_active_time'])

    def test_nominal_activity_matched_but_perturbation_sensitive(self):
        result = evaluate()
        self.assertEqual(result['nominal_max_state_error'],0)
        self.assertGreater(result['perturbed_max_state_difference'],.1)
        self.assertLess(result['live_perturbed_active_time'],
                        result['replay_perturbed_active_time'])
        self.assertEqual(result['intact_active_time'],result['replay_perturbed_active_time'])

    def test_invalid_external_return_is_atomic(self):
        a = Agent()
        before = a.state_vector()
        for value in ((0,), (0,2), (float('nan'),0)):
            with self.assertRaises(ValueError):
                a.step(np.zeros((2,4)),np.ones((2,4)),return_override=value)
            np.testing.assert_array_equal(a.state_vector(),before)
