import unittest
import numpy as np
from model.configuration import configured,association_weights,joint_configured
from experiments import context_ambiguity,return_replay,agent_ignition,free_competition


class ConfigurationTests(unittest.TestCase):
    def test_joint_experiments_reference_one_model_owned_factory(self):
        from experiments import (joint_distractor,acquisition_partition,bidirectional_replay,
                                 conflict_candidate_audit,candidate_timestep,
                                 acquisition_contract,acquisition_boundary)
        for module in (joint_distractor,acquisition_partition,bidirectional_replay,
                       conflict_candidate_audit,candidate_timestep,
                       acquisition_contract,acquisition_boundary):
            self.assertIs(module.configured,joint_configured)
        self.assertTrue(joint_configured().reliability_selection)
        self.assertFalse(configured().reliability_selection)

    def test_primary_demonstrations_share_one_factory(self):
        for module in (context_ambiguity,return_replay,agent_ignition,free_competition):
            self.assertIs(module.configured,configured)
        a = configured()
        self.assertIsNone(a.forced_source)
        self.assertEqual(a.context_source,1)
        self.assertEqual(a.context_prior_gain,.04)
        np.testing.assert_array_equal(a.association.weights,association_weights())
        np.testing.assert_allclose(a.rule,[1/3]*3)
