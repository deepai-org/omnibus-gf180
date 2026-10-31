import unittest
import numpy as np
from model.association import Association
from model.agent import Agent


class RetrievalSupportTests(unittest.TestCase):
    def test_correct_nonidentity_association_supports_its_candidate(self):
        weights = np.zeros((3,3,3))
        for c in range(3):
            for g in range(3):
                weights[c,g,(g+1)%3] = 1
        a = Association(weights)
        np.testing.assert_array_equal(a.retrieval_support([1,0,0],
            [[1,0,0],[0,1,0]],[0,1,0]),[1,-1])

    def test_empty_memory_cannot_support_candidates(self):
        np.testing.assert_array_equal(Association().retrieval_support([1,0,0],
            [[1,0,0],[0,1,0]],[0,0,0]),[0,0])

    def test_partial_mass_scales_return(self):
        np.testing.assert_allclose(Association().retrieval_support([1,0,0],
            [[1,0,0],[0,1,0]],[.3,0,0]),[.3,.3])

    def test_mode_explicit_and_no_extra_state(self):
        a = Agent(memory_return_mode='address_consistency')
        self.assertEqual(len(a.state_vector()),110)
        with self.assertRaises(ValueError):
            Agent(memory_return_mode='unknown')
