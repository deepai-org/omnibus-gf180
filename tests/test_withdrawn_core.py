import unittest
import numpy as np
from experiments.return_replay import configured, prepare
from experiments.withdrawn_core import indices, screen, transition


class WithdrawnCoreTests(unittest.TestCase):
    def test_all_omitted_coordinates_can_vary_without_changing_projection(self):
        result = screen(trials=30,steps=30)
        self.assertEqual((result['included'],result['omitted']),(83,27))
        self.assertEqual(result['max_error'],0)

    def test_repeated_projected_transition_matches_full_agent(self):
        a = configured()
        a.set_state(prepare())
        selected = indices(a)
        state = a.state_vector()[selected]
        for _ in range(160):
            state = transition(state)
            a.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0))
            np.testing.assert_array_equal(state,a.state_vector()[selected])
