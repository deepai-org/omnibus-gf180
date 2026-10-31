import unittest
from experiments.workspace_closure import evaluate


class ClosureTests(unittest.TestCase):
    def test_omitted_state_witnesses_reject_all_proposed_autonomous_subsets(self):
        results = evaluate()
        self.assertEqual([r['coordinates'] for r in results],[14,17,35,79])
        for row in results:
            self.assertTrue(row['closure_falsified'],row)
            self.assertTrue(any(p['next_step']>1e-12 for p in row['probes']))
        # Inputs are physically withdrawn here; lack of a precision effect in
        # this phase must not be misread as global irrelevance of precision.
        for row in results:
            precision = next(p for p in row['probes'] if p['omitted']=='precision')
            self.assertEqual(precision['max_over_one_unit'],0)
