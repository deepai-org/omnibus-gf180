import unittest
import numpy as np
from experiments.attention_task import ControlIntervention, run
from model.attention import Attention


class AttentionTaskTests(unittest.TestCase):
    def test_default_intervention_is_identical_component(self):
        a, b = Attention(), ControlIntervention('model')
        for _ in range(100):
            np.testing.assert_array_equal(a.step([.45, .8]), b.step([.45, .8]))
            np.testing.assert_array_equal(a.state_vector(), b.state_vector())

    def test_all_controls_retain_estimator_state_and_nominal_task(self):
        for mode in ('model', 'direct', 'command'):
            with self.subTest(mode=mode):
                self.assertEqual(ControlIntervention(mode).state_count, 14)
                self.assertTrue(run(mode)['correct'])

    def test_invalid_mode_rejected(self):
        with self.assertRaises(ValueError):
            ControlIntervention('unknown')

    def test_saturated_actuator_does_not_deadlock_usable_evidence(self):
        for mode in ('model', 'direct', 'command'):
            for tau in (1, 3):
                with self.subTest(mode=mode, tau=tau):
                    result = run(mode, gain=.65, tau=tau)
                    self.assertTrue(result['correct'])
                    self.assertLess(result['aperture'], .66)
                    self.assertLess(result['estimate'], .95)
