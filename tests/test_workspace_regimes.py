import unittest
import numpy as np
from model.content_workspace import ContentWorkspace
from experiments.workspace_regimes import candidate_step, REGIMES


class RegimeTests(unittest.TestCase):
    def test_reference_regime_reproduces_implementation(self):
        rng = np.random.default_rng(3141)
        for _ in range(100):
            a, b = ContentWorkspace(), ContentWorkspace()
            x = np.concatenate((rng.random(2),rng.dirichlet([1,1,1],2).ravel(),
                                rng.uniform(-1,1,4),rng.random(2)))
            a.set_state(x)
            b.set_state(x)
            inputs = (rng.random(2),rng.dirichlet([1,1,1],2),rng.uniform(-1,1,(2,2)),
                      rng.random(2),rng.uniform(-1,1,2))
            a.step(*inputs)
            candidate_step(REGIMES[0])(b,*inputs)
            np.testing.assert_allclose(a.state_vector(),b.state_vector(),atol=2e-16,rtol=0)
