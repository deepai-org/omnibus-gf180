import unittest

from model.evaluate_switch import evaluate


class ContinuousSceneTests(unittest.TestCase):
    def test_changed_scene_withdraws_and_revises_report(self):
        for row in evaluate():
            with self.subTest(scene=row['scene'], sigma=row['sigma']):
                self.assertTrue(row['initial_correct'])
                self.assertIsNotNone(row['withdrawal'])
                self.assertLess(row['withdrawal'], 1)
                self.assertIsNotNone(row['first_new_report'])
                self.assertGreater(row['first_new_report'], row['withdrawal'])
                self.assertLess(row['first_new_report'], 20)
                self.assertEqual(row['wrong_reports_after_withdrawal'], 0)
                self.assertEqual(row['final_group'], row['scene'][0])
