import unittest
import numpy as np
from experiments.return_replay import configured,prepare
from experiments.reduced_persistence import project,configured_transition as transition
from model.association import Association


class ReducedPersistenceTests(unittest.TestCase):
    def test_full_agent_trajectory_matches_sufficient_statistics(self):
        a = configured()
        a.set_state(prepare())
        reduced = project(a)
        self.assertEqual(reduced.shape,(35,))
        for _ in range(400):
            reduced = transition(reduced)
            a.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0))
            np.testing.assert_allclose(reduced,project(a),atol=1e-12,rtol=0)

    def test_random_valid_full_states_match_one_step(self):
        rng = np.random.default_rng(824)
        for _ in range(100):
            a = configured()
            a.forced_source = None if _%2 else 0
            a.association = Association(rng.dirichlet(np.ones(3),(3,3)))
            for name,array in a.state_fields():
                if name == 'learned_variance':
                    array[:] = rng.uniform(.0625,4,array.shape)
                elif name.endswith(('.group','.quality')) and name!='content.quality' or name=='rule':
                    array[:] = rng.dirichlet(np.ones(array.shape[-1]),array.shape[:-1])
                elif name.endswith(('.x','.z')) or name=='content.quality':
                    array[:] = rng.uniform(-1,1,array.shape)
                else:
                    array[:] = rng.random(array.shape)
            a.set_state(a.state_vector())
            reduced = transition(project(a),forced_source=a.forced_source,weights=a.association.weights)
            a.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0))
            np.testing.assert_allclose(reduced,project(a),atol=1e-12,rtol=0)
