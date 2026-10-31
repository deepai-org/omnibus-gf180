import unittest
import numpy as np
from experiments.return_replay import configured
from experiments.reduced_persistence import lift,project,configured_transition as transition


class ReducedLiftTests(unittest.TestCase):
    def state(self,rng):
        return np.concatenate((rng.random(4),rng.dirichlet([1,1,1],2).ravel(),
                               rng.uniform(-1,1,4),rng.dirichlet([1,1,1],2).ravel(),
                               rng.uniform(-1,1,6),rng.random(3),
                               rng.dirichlet([1,1,1]),rng.random(1),rng.random(2)))

    def test_constructive_interventions_round_trip_and_evolve(self):
        rng = np.random.default_rng(1901)
        for _ in range(100):
            state = self.state(rng)
            a = lift(state,configured())
            a.set_state(a.state_vector())
            np.testing.assert_allclose(project(a),state,atol=2e-16,rtol=0)
            expected = transition(state)
            a.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0))
            np.testing.assert_allclose(project(a),expected,atol=1e-12,rtol=0)

    def test_invalid_lift_is_atomic(self):
        a = configured()
        before = a.state_vector()
        state = project(a)
        state[33] = 2
        with self.assertRaises(ValueError):
            lift(state,a)
        np.testing.assert_array_equal(before,a.state_vector())

    def test_alternative_micro_realizations_agree_after_intervention(self):
        rng = np.random.default_rng(82)
        for _ in range(100):
            state = self.state(rng)
            a,b = lift(state,configured()),lift(state,configured())
            # Common-mode observer activity changes while difference is fixed.
            room = np.minimum(1-b.observer.evidence,1-b.observer.conflict)
            common = rng.random((2,3))*room
            b.observer.evidence += common
            b.observer.conflict += common
            for s in b.sensory.specialists:
                s.x[:] = rng.permutation(s.x)
            b.set_state(b.state_vector())
            np.testing.assert_allclose(project(a),project(b),atol=3e-16,rtol=0)
            for _ in range(10):
                for agent in (a,b):
                    agent.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0))
                np.testing.assert_allclose(project(a),project(b),atol=1e-12,rtol=0)
