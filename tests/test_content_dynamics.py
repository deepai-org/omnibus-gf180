import unittest
import numpy as np
from model.content_workspace import ContentWorkspace
from experiments.content_dynamics import transition


class ContentDynamicsTests(unittest.TestCase):
    def test_independent_equations_match_random_interventions(self):
        rng = np.random.default_rng(8923)
        for _ in range(500):
            gains = (1.2,.25) if _ % 2 else (.8,.65)
            w = ContentWorkspace(self_gain=gains[0],return_gain=gains[1])
            x = np.concatenate((rng.random(2), rng.dirichlet([1,1,1],2).ravel(),
                                rng.uniform(-1,1,4), rng.random(2)))
            w.set_state(x)
            inputs = (rng.random(2), rng.dirichlet([1,1,1],2),
                      rng.uniform(-1,1,(2,2)), rng.random(2), rng.uniform(-1,1,2))
            expected = transition(x, *inputs,self_gain=gains[0],return_gain=gains[1])
            w.step(*inputs)
            np.testing.assert_allclose(w.state_vector(), expected, atol=2e-16, rtol=0)

    def test_competition_cut_preserves_payload_update_but_changes_activity(self):
        w = ContentWorkspace()
        w.activity[:] = [.4,.4]
        inputs = ([.8,.8], [[1,0,0],[0,1,0]], [[.7,-.6],[-.6,.7]], [1,1], [0,0])
        intact = transition(w.state_vector(), *inputs)
        cut = transition(w.state_vector(), *inputs, cut_competition=True)
        self.assertTrue(np.all(cut[:2] > intact[:2]))
        np.testing.assert_array_equal(cut[2:], intact[2:])

    def test_payload_is_part_of_feedback_boundary_not_autonomous(self):
        w = ContentWorkspace()
        w.activity[:] = [.2,0]
        common = ([.5,0], [[1,0,0],[0,1,0]], [[.7,-.6],[-.6,.7]], [1,1])
        positive = transition(w.state_vector(), *common, [1,0])
        negative = transition(w.state_vector(), *common, [-1,0])
        self.assertNotEqual(positive[0], negative[0])
