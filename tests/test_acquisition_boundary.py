import unittest
from experiments.acquisition_boundary import evaluate


class AcquisitionBoundaryTests(unittest.TestCase):
    def test_shuttered_statistic_does_not_close_acquisition_dynamics(self):
        row=evaluate()
        self.assertEqual(row['initial_projected_difference'],0)
        closed,opened=row['rows']
        self.assertLess(closed['max_reduced_difference'],1e-12)
        self.assertGreater(opened['activity_difference'],1e-6)
