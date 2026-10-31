import unittest
import numpy as np
from experiments.bidirectional_replay import evaluate,record,partitioned
from experiments.reliability_competition import configured
from experiments.return_replay import prepare


class BidirectionalReplayTests(unittest.TestCase):
    def test_nominal_match_and_blocked_outward_perturbation_for_all_boundaries(self):
        rows=evaluate()
        self.assertEqual([r['coordinates'] for r in rows],[14,17,35])
        for row in rows:
            self.assertEqual(row['nominal_max_error'],0)
            self.assertEqual(row['cut_other_side_change'],0)
            self.assertGreater(row['live_other_side_change'],0)
            self.assertGreater(row['perturbed_live_cut_difference'],0)

    def test_inward_perturbation_also_cannot_cross_partition(self):
        a=configured()
        initial=prepare(factory=configured)
        a.set_state(initial)
        reference=record(initial,20)
        selected=np.array([n.startswith('content.') for n in a.state_names()])
        a.observer.conflict[:]=1
        changed=a.state_vector()
        cut=partitioned(changed,reference,selected)
        live=record(changed,20)
        np.testing.assert_array_equal(cut[:,selected],reference[:,selected])
        self.assertGreater(np.max(np.abs(live[:,selected]-reference[:,selected])),0)
