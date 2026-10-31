import unittest
import numpy as np
from model.agent import Agent
from experiments.free_competition import run_case


class CompetitionTests(unittest.TestCase):
    def test_hidden_new_source_can_request_acquisition_before_winning(self):
        a = Agent()
        a.content.activity[:] = [0,.9]
        self.assertEqual(a.source,1)
        a.step(np.zeros((2,4)),[[1,0,0,1],[0,0,0,0]],input_enabled=(1,0))
        self.assertGreater(a.desired_inspection[0],0)
        self.assertEqual(a.desired_inspection[1],0)

    def test_reversal_selects_new_content_without_reset(self):
        for first in (0,1):
            result = run_case(first)
            for phase in result['phases']:
                self.assertTrue(phase['final_valid'])
                self.assertEqual(phase['final_source'],phase['expected_source'])
                self.assertIsNotNone(phase['first_selected'])
                self.assertLess(phase['first_selected'],5)
                self.assertEqual(phase['simultaneous_high_steps'],0)
                self.assertGreater(phase['group'][phase['expected_source']],.9)
