import unittest
from experiments.reliability_competition import run_case,configured
from experiments.context_ambiguity import run_case as contextual_case


class ReliabilityCompetitionTests(unittest.TestCase):
    def test_same_candidate_configuration_still_solves_ambiguous_context_task(self):
        for context in ('horizontal','vertical'):
            for sign in (-1,1):
                row = contextual_case(context,sign,factory=configured)
                self.assertTrue(row['correct'],row)

    def test_measured_reliability_selects_supported_content_in_either_position(self):
        for good in (0,1):
            row = run_case(good,candidate=True)
            self.assertEqual(row['final_source'],good)
            self.assertGreater(row['selected_steps'][good],0)
            self.assertEqual(row['selected_steps'][1-good],0)

    def test_return_cut_restores_wrong_selection_when_bad_source_has_tie_advantage(self):
        row = run_case(1,candidate=True,cut=True)
        self.assertEqual(row['final_source'],0)
        self.assertGreater(row['selected_steps'][0],0)
