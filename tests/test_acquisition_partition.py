import unittest
from experiments.acquisition_partition import evaluate


class AcquisitionPartitionTests(unittest.TestCase):
    def test_nominal_matching_and_cross_boundary_blockage_during_reasoning(self):
        rows=evaluate()
        self.assertEqual(len(rows),3)
        for row in rows:
            self.assertEqual(row['nominal_max_error'],0)
            self.assertEqual(row['cut_other_side_change'],0)
            self.assertGreater(row['live_other_side_change'],0)
            self.assertGreater(row['live_cut_difference'],0)
