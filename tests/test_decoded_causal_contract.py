import unittest
import numpy as np
from experiments.decoded_agent import configured
from experiments.acquisition_contract import inventory,project,transition
from experiments.return_replay import evaluate


class DecodedCausalContractTests(unittest.TestCase):
    def test_complete_reduced_boundary_and_reconstruction(self):
        names,dynamic,frozen,_=inventory(configured)
        self.assertEqual((len(names),len(dynamic),len(frozen)),(94,90,4))
        self.assertEqual(sorted(dynamic+frozen),list(range(94)))
        a=configured()
        state=project(a,configured)
        rng=np.random.default_rng(121)
        for _ in range(100):
            samples=rng.uniform(-1,1,(2,4))
            visibility=rng.uniform(0,1,(2,4))
            enables=rng.integers(0,2,2)
            state,result=transition(state,samples,visibility,input_enabled=enables,factory=configured)
            actual=a.step(samples,visibility,input_enabled=enables)
            np.testing.assert_array_equal(state,project(a,configured))
            self.assertEqual(result,actual)

    def test_reduced_state_cannot_use_original_contract_silently(self):
        with self.assertRaises(ValueError):
            project(configured())

    def test_replay_matches_every_reduced_state_coordinate(self):
        row=evaluate(factory=configured)
        self.assertEqual(row['states'],94)
        self.assertEqual(row['nominal_max_state_error'],0)
        self.assertGreater(row['perturbed_max_state_difference'],0)
