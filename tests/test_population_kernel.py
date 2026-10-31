import unittest
from experiments.population_kernel import factorization_distance,row
from experiments.reduced_persistence import project
from model.configuration import joint_configured


class PopulationKernelTests(unittest.TestCase):
    def test_factorization_metric_on_known_joint_distributions(self):
        suffix=(0,0,0,0,0,0)
        independent=[(a,b)+suffix for a in (0,1) for b in (0,1)]
        correlated=[(0,0)+suffix,(1,1)+suffix]
        self.assertAlmostEqual(factorization_distance(independent),0)
        self.assertAlmostEqual(factorization_distance(correlated),.5)

    def test_independent_realizations_preserve_input_label(self):
        result=row((1,0,0,0,0,1,0,1),project(joint_configured()),steps=1)
        self.assertEqual(result['realizations'],256)
        self.assertGreaterEqual(result['joint_vs_product_tv'],0)
        self.assertLessEqual(result['joint_vs_product_tv'],1)
