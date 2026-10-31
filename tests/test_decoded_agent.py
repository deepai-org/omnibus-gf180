import unittest
import numpy as np
from experiments.decoded_agent import configured,project
from experiments.decoded_stability import configured as full_configured
from experiments.context_ambiguity import run_case


class DecodedAgentTests(unittest.TestCase):
    def test_reduced_candidate_solves_task_but_requires_context_feedback(self):
        intact=run_case('horizontal',1,factory=configured,distractor=True)
        cut=run_case('horizontal',1,lesion='context_return',factory=configured,distractor=True)
        self.assertTrue(intact['correct'])
        self.assertFalse(cut['report'])
        self.assertGreater(cut['retained_context'][0],.99)

    def test_reduced_state_tracks_unreduced_candidate(self):
        full,reduced=full_configured(),configured()
        rng=np.random.default_rng(103)
        for specialist in full.sensory.specialists:
            specialist.quality[:]=rng.dirichlet(np.ones(5),2)
        reduced.set_state(project(full))
        self.assertEqual(len(reduced.state_vector()),94)
        self.assertEqual(len(reduced.state_names()),94)
        for _ in range(400):
            samples=rng.uniform(-1,1,(2,4))
            mask=rng.uniform(0,1,(2,4))
            enabled=rng.integers(0,2,2)
            left=full.step(samples,mask,input_enabled=enabled)
            right=reduced.step(samples,mask,input_enabled=enabled)
            np.testing.assert_allclose(reduced.state_vector(),project(full),atol=1e-12,rtol=0)
            self.assertEqual(left,right)

    def test_checkpoint_round_trip_preserves_negative_quality(self):
        a=configured()
        a.sensory.specialists[0].decoded_quality[:]=[-.7,.2]
        state=a.state_vector()
        a.set_state(state)
        np.testing.assert_array_equal(a.state_vector(),state)
