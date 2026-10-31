from copy import deepcopy
import unittest

import numpy as np

from model.agent import Agent
from model.causal import boundary_screen, transition_table
from model.perception import scene


class CausalTests(unittest.TestCase):
    def test_attention_boundary_uses_actual_active_checkpoint(self):
        report = boundary_screen('attention', 'inspection')
        self.assertEqual(report['phase'], 'inspection')
        self.assertGreater(report['checkpoint_step'], 0)
        self.assertGreater(report['checkpoint_inspect_query'], .9)
        self.assertGreater(report['checkpoint_aperture'], .25)
        self.assertEqual(report['names'][0], 'attention.aperture[0,0]')
        self.assertNotIn(report['background_intervention'], report['names'])
        self.assertEqual(len(report['reports']), 2)
        self.assertTrue(all(len(r['nominal_table']) == 16 for r in report['reports']))

    def test_unused_latents_absent_and_legacy_raw_checkpoints_rejected(self):
        a = Agent()
        names = a.state_names()
        for stream in (0, 1):
            self.assertIn(f'sensory.{stream}.z[2,0]', names)
            self.assertNotIn(f'sensory.{stream}.z[2,1]', names)
        with self.assertRaises(ValueError):
            a.set_state(np.zeros(100))
        with self.assertRaises(ValueError):
            a.sensory.specialists[0].z[2, 1] = .5

    def test_full_checkpoint_reproduces_evolution(self):
        a = Agent(source=1)
        samples = np.stack([scene('horizontal', .73, -.61)] * 2)
        for _ in range(200):
            a.step(samples, np.ones((2, 4)))
        b = Agent(source=1)
        b.set_state(a.state_vector())
        self.assertEqual(len(set(a.state_names())), a.state_count)
        for _ in range(20):
            self.assertEqual(a.step(samples, np.ones((2, 4))), b.step(samples, np.ones((2, 4))))
            np.testing.assert_array_equal(a.state_vector(), b.state_vector())

    def test_invalid_restore_does_not_partially_mutate(self):
        a = Agent()
        initial = a.state_vector()
        state = initial.copy()
        state[-1] = 2
        with self.assertRaises(ValueError):
            a.set_state(state)
        np.testing.assert_array_equal(initial, a.state_vector())

    def test_intervention_table_preserves_original(self):
        a = Agent()
        initial = deepcopy(a.state_vector())
        table = transition_table(a, np.zeros((2, 4)), np.ones((2, 4)), steps=1)
        self.assertEqual(len(table), 16)
        np.testing.assert_array_equal(initial, a.state_vector())

    def test_boundary_screen_exposes_omitted_state_and_grain_dependence(self):
        report = boundary_screen()
        self.assertEqual(len(report['reports']), 2)
        self.assertTrue(any(r['background_sensitivity']['max_continuous_difference'] > .01
                            for r in report['reports']))
        self.assertTrue(any(r['within_bin_sensitivity']['changed_rows'] > 0
                            for r in report['reports']))


if __name__ == '__main__':
    unittest.main()
