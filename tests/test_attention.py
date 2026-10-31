import unittest

import numpy as np

from model.attention import Attention
from model.compare_attention import comparison


class AttentionTests(unittest.TestCase):
    def test_matched_control_sweep_reports_both_successes_and_failures(self):
        rows = comparison()
        self.assertEqual(len(rows), 9)
        for row in rows:
            self.assertTrue(np.isfinite(row['model_error']))
            self.assertTrue(np.isfinite(row['direct_feedback_error']))
        nominal_gain = [r for r in rows if r['gain'] == 1]
        self.assertTrue(all(r['model_error'] < r['direct_feedback_error'] for r in nominal_gain))
        # Preserve the adverse cases in the experiment, not just the wins.
        self.assertTrue(any(r['model_error'] > r['direct_feedback_error'] for r in rows))

    def test_prediction_is_not_command_copy(self):
        a = Attention()
        a.step([1, 0])
        self.assertLess(a.estimate[0], .1)
        self.assertEqual(a.estimate[1], 0)
        self.assertEqual(a.state_vector().shape, (14,))

    def test_held_out_plant_gain_control(self):
        for gain in (.65, 1.4):
            controlled = Attention(actuator_gain=gain, actuator_tau=2)
            direct = Attention(actuator_gain=gain, actuator_tau=2)
            for _ in range(1600):
                controlled.step([.45, .35])
                direct.step([.45, .35], schema_enabled=False)
            target = np.array([.45, .35])
            controlled_error = np.linalg.norm(controlled.aperture.mean(axis=1) - target)
            direct_error = np.linalg.norm(direct.aperture.mean(axis=1) - target)
            self.assertLess(controlled_error, direct_error * .5)

    def test_feedback_distinguishes_actual_from_expected_motion(self):
        connected = Attention(actuator_tau=3)
        disconnected = Attention(actuator_tau=3)
        for _ in range(80):
            connected.step([.5, 0])
            disconnected.step([.5, 0], feedback_enabled=False)
        connected_error = abs(connected.estimate[0] - connected.aperture[0].mean())
        disconnected_error = abs(disconnected.estimate[0] - disconnected.aperture[0].mean())
        self.assertLess(connected_error, disconnected_error)

    def test_schema_intervention_changes_control_at_fixed_plant(self):
        a, b = Attention(), Attention()
        a.estimate[0] = .8
        b.estimate[0] = .2
        np.testing.assert_array_equal(a.aperture, b.aperture)
        ca, cb = a.step([.5, 0]), b.step([.5, 0])
        self.assertLess(ca[0], cb[0])


if __name__ == '__main__':
    unittest.main()
