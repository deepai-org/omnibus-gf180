import unittest
from experiments.joint_distractor import evaluate_condition,CONDITIONS


class JointDistractorTests(unittest.TestCase):
    def test_intact_and_memory_prior_cut_have_selective_difference(self):
        intact=evaluate_condition(*CONDITIONS[0])
        cut=evaluate_condition(*CONDITIONS[1])
        self.assertEqual(intact['coherent_success'],4)
        self.assertEqual(cut['coherent_success'],0)
        self.assertEqual(cut['reports'],0)
        self.assertEqual(cut['correct_retained_context'],4)

    def test_condition_names_are_unique_and_interventions_explicit(self):
        self.assertEqual(len({c[0] for c in CONDITIONS}),len(CONDITIONS))
        self.assertIn(('memory_persistence',None,('memory',)),CONDITIONS)
