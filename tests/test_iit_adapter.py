import unittest
from itertools import product

import numpy as np

from model.iit import transition_array, candidate_subsets, deterministic_dependencies, source_provenance


class IITAdapterTests(unittest.TestCase):
    def test_source_provenance_covers_agent_and_analysis(self):
        from hashlib import sha256
        from pathlib import Path
        import model.agent
        hashes = source_provenance()
        self.assertIn('iit.py', hashes)
        self.assertIn('primitives.py', hashes)
        self.assertEqual(hashes['agent.py'], sha256(Path(model.agent.__file__).read_bytes()).hexdigest())
        self.assertTrue(all(len(value) == 64 for value in hashes.values()))

    def test_dependency_audit_distinguishes_self_and_cross_coupling(self):
        np.testing.assert_array_equal(deterministic_dependencies(
            [[0, 0], [1, 0], [0, 1], [1, 1]]), np.eye(2))
        np.testing.assert_array_equal(deterministic_dependencies(
            [[0, 0], [0, 1], [1, 0], [1, 1]]), [[0, 1], [1, 0]])

    def test_all_multi_coordinate_subsets_are_included(self):
        subsets = candidate_subsets(4)
        self.assertEqual(len(subsets), 11)
        self.assertEqual(len(set(subsets)), 11)
        self.assertEqual({len(s) for s in subsets}, {2, 3, 4})

    def test_little_endian_rows_not_lexicographic_order(self):
        rows = [dict(initial=list(bits), final_binary=list(bits)) for bits in product((0, 1), repeat=2)]
        np.testing.assert_array_equal(transition_array(rows), [[0, 0], [1, 0], [0, 1], [1, 1]])

    def test_duplicate_rows_fail(self):
        rows = [dict(initial=[0, 0], final_binary=[0, 0])] * 4
        with self.assertRaises(ValueError):
            transition_array(rows)


if __name__ == '__main__':
    unittest.main()
