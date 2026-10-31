import unittest
from experiments.population_grain import evaluate


class PopulationGrainTests(unittest.TestCase):
    def test_counts_and_reproducibility(self):
        labels = [(0,0,0,0,3,3,3,0), (1,0,0,0,0,1,0,1)]
        result = evaluate((1,20), labels)
        self.assertEqual(result, evaluate((1,20), labels))
        self.assertEqual(result['total_rows'], 2)
        for row in result['results']:
            self.assertLessEqual(row['changed_rows'], 2)
            self.assertEqual(len(row['changed_by_unit']), 8)
            self.assertGreaterEqual(sum(row['changed_by_unit']), row['changed_rows'])

    def test_invalid_horizon(self):
        with self.assertRaises(ValueError):
            evaluate((0,))
