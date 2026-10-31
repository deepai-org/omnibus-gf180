import unittest

from model.evaluate import cases, run_case


class EvaluationTests(unittest.TestCase):
    def test_grid_has_all_distinct_combinations(self):
        grid = cases()
        self.assertEqual(len(grid), 72)
        self.assertEqual(len({tuple(c.items()) for c in grid}), 72)

    def test_case_scores_group_and_answer_together(self):
        result = run_case(dict(group='vertical', rule='horizontal', sign=1, occluded=True, source=1))
        self.assertTrue(result['correct'])
        self.assertEqual(result['group'], 'vertical')
        self.assertFalse(result['answer'])
        self.assertIn('inspect', result['queries'])


if __name__ == '__main__':
    unittest.main()
