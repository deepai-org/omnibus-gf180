import unittest
from experiments.individual_returns import evaluate


class IndividualReturnTests(unittest.TestCase):
    def test_all_cuts_have_state_effects_and_aggregate_cut_shortens_persistence(self):
        rows = evaluate()
        self.assertEqual(len(rows),8)
        self.assertEqual(len({tuple(r['cuts']) for r in rows}),8)
        baseline = rows[0]
        self.assertEqual(baseline['cuts'],[])
        self.assertEqual(baseline['max_state_difference'],0)
        for row in rows[1:]:
            self.assertGreater(row['max_state_difference'],0)
        # A thresholded duration can stay unchanged despite a continuous effect;
        # do not require every individual path to be indispensable here.
        self.assertLess(rows[-1]['active_time'],baseline['active_time'])
