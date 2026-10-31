import unittest
import numpy as np
from model.perception import Perception
from model.primitives import quality_decode
from experiments.decoded_perception import project,transition


class DecodedPerceptionTests(unittest.TestCase):
    def test_exact_local_dynamics_across_changing_stimuli_masks_and_priors(self):
        rng=np.random.default_rng(23)
        a=Perception()
        a.quality[:]=rng.dirichlet(np.ones(5),2)
        state=project(a)
        for _ in range(500):
            sample=rng.uniform(-1,1,4)
            mask=rng.uniform(0,1,4)
            prior=rng.uniform(-.03,.03,3)
            precision=rng.uniform(.1,3)
            state=transition(state,sample,mask,precision,prior)
            a.step(sample,mask,precision,prior)
            np.testing.assert_allclose(state,project(a),atol=1e-14,rtol=0)

    def test_population_shape_stability_is_not_preserved_by_readout_reduction(self):
        a,b=Perception(),Perception()
        b.quality[:]=[.5,0,0,0,.5]
        np.testing.assert_array_equal(project(a),project(b))
        target=a.signals(np.ones(4))['quality_target']
        self.assertEqual(np.sum((target-a.quality)**2),0)
        self.assertGreater(np.sum((target-b.quality)**2),0)
        np.testing.assert_array_equal(quality_decode(a.quality),quality_decode(b.quality))
