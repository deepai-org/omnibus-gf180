import unittest
from itertools import combinations
import numpy as np
from experiments.return_replay import configured,prepare
from experiments.reduced_persistence import project,configured_transition as transition


class ReducedInterventionTests(unittest.TestCase):
    def test_content_intervention_does_not_redefine_observer_coordinates(self):
        a = configured()
        a.set_state(prepare())
        before = project(a)
        a.content.group[0] = [0,1,0]
        after = project(a)
        np.testing.assert_array_equal(before[20:26],after[20:26])
        np.testing.assert_array_equal(before[:4],after[:4])
        np.testing.assert_array_equal(before[10:],after[10:])
        self.assertGreater(np.max(np.abs(before[4:10]-after[4:10])),0)

    def test_all_return_cuts_commute_with_projection(self):
        initial = prepare()
        for n in range(4):
            for cuts in combinations(('sensory','observer','memory'),n):
                a = configured()
                a.set_state(initial)
                reduced = project(a)
                for _ in range(100):
                    reduced = transition(reduced,cuts=cuts)
                    a.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0),
                           sensory_return='sensory' not in cuts,
                           observer_feedback='observer' not in cuts,
                           memory_feedback='memory' not in cuts)
                    np.testing.assert_allclose(reduced,project(a),atol=1e-12,rtol=0)

    def test_return_clamp_and_content_intervention_commute(self):
        rng = np.random.default_rng(990)
        a = configured()
        a.set_state(prepare())
        for _ in range(100):
            a.content.group[0] = rng.dirichlet([1,1,1])
            # Reproject after the micro-intervention; observer difference
            # coordinates stay independent of the changed content coordinates.
            reduced = project(a)
            clamp = rng.uniform(-1,1,2)
            reduced = transition(reduced,return_override=clamp)
            a.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0),return_override=clamp)
            np.testing.assert_allclose(reduced,project(a),atol=1e-12,rtol=0)
