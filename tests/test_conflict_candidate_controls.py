import unittest
from experiments.reliability_competition import configured
from experiments.free_competition import run_case as competition
from experiments.agent_ignition import run_case as ignition


class ConflictCandidateControls(unittest.TestCase):
    def test_selection_reverses_without_coactive_winners(self):
        for first in (0,1):
            row = competition(first,factory=configured)
            for phase in row['phases']:
                self.assertTrue(phase['final_valid'])
                self.assertEqual(phase['final_source'],phase['expected_source'])
                self.assertIsNotNone(phase['first_selected'])
                self.assertEqual(phase['simultaneous_high_steps'],0)

    def test_persistence_depends_on_returns_and_releases(self):
        intact = ignition(.7,4,factory=configured)
        cut = ignition(.7,4,cut_after=True,factory=configured)
        self.assertEqual(intact['at_removal'],cut['at_removal'])
        self.assertGreater(intact['active_time_after_removal'],cut['active_time_after_removal'])
        self.assertLess(intact['final_activity'],1e-6)
        self.assertLess(cut['final_activity'],1e-6)
