import unittest
import numpy as np
from experiments.reliability_competition import configured
from experiments.return_replay import evaluate,prepare
from experiments.reduced_persistence import project,configured_transition


class CandidateCausalControls(unittest.TestCase):
    def test_activity_matched_replay_and_perturbation_use_same_candidate(self):
        row=evaluate(factory=configured)
        self.assertEqual(row['nominal_max_state_error'],0)
        self.assertGreater(row['perturbed_max_state_difference'],0)
        self.assertLess(row['live_perturbed_active_time'],row['replay_perturbed_active_time'])

    def test_shuttered_reduction_matches_candidate_trajectory(self):
        a=configured()
        a.set_state(prepare(factory=configured))
        state=project(a)
        for _ in range(160):
            state=configured_transition(state)
            a.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0))
            np.testing.assert_allclose(project(a),state,atol=1e-12,rtol=0)
