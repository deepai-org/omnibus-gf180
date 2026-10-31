import unittest
from experiments.workspace_grain import evaluate


class WorkspaceGrainTests(unittest.TestCase):
    def test_binary_coarse_grain_has_valid_within_bin_counterexamples(self):
        result = evaluate()
        self.assertEqual(result['levels'],[[.1,.9],[.4,.6]])
        self.assertEqual([r['total'] for r in result['results']],[16,16,16])
        self.assertGreater(result['results'][1]['changed_rows'],0)
        self.assertGreater(result['results'][2]['changed_rows'],0)
        for row in result['results']:
            self.assertEqual(row['changed_rows'],len(row['witnesses']))
            for witness in row['witnesses']:
                self.assertNotEqual(witness['far'],witness['near'])
