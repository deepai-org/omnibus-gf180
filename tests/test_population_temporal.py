import unittest
from experiments.population_kernel import row
from experiments.reduced_persistence import project
from model.configuration import joint_configured


class PopulationTemporalTests(unittest.TestCase):
    def test_same_label_can_hide_evolution_needed_for_later_transition(self):
        labels=(0,0,0,0,0,0,0,0)
        background=project(joint_configured())
        short=row(labels,background,1)
        long=row(labels,background,20)
        self.assertEqual(short['self_transition_probability'],1)
        self.assertLess(long['self_transition_probability'],1)
