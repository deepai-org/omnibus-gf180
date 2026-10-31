import unittest
from experiments.withdrawn_task import evaluate_case


class WithdrawnTaskTests(unittest.TestCase):
    def test_branches_start_before_any_answer(self):
        row = evaluate_case('horizontal',-1)
        self.assertEqual(row['prior_reports'],0)
        self.assertEqual(len(row['branches']),5)
        self.assertTrue(row['branches'][0]['first_report']['correct'])
        self.assertIsNone(row['branches'][1]['first_report'])
        self.assertIsNone(row['branches'][-1]['first_report'])
        for branch in row['branches']:
            self.assertEqual(len(branch['trace']),6)
            self.assertGreaterEqual(branch['report_count'],0)
            if branch['first_report'] is not None:
                self.assertTrue(branch['first_report']['correct'])
                self.assertGreater(branch['first_report']['delay'],0)

    def test_invalid_fixture_rejected(self):
        for args in [('unknown',1,14.5),('horizontal',0,14.5),('horizontal',1,0)]:
            with self.assertRaises(ValueError):
                evaluate_case(*args)
