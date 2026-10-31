import unittest
import numpy as np
from experiments.context_ambiguity import run_case
from experiments.reliability_competition import configured


class ContextDistractorTests(unittest.TestCase):
    def test_supported_context_survives_unsupported_distractor(self):
        for context,index in (('horizontal',0),('vertical',1)):
            for sign in (-1,1):
                row=run_case(context,sign,factory=configured,distractor=True)
                self.assertTrue(row['correct'],row)
                self.assertGreater(row['retained_context'][index],.99)
                self.assertGreater(row['group'][index],.9)

    def test_context_admission_lesion_exposes_corruption_not_just_answer_rate(self):
        row=run_case('horizontal',1,lesion='context_admission',
                     factory=configured,distractor=True)
        self.assertFalse(row['correct'])
        self.assertGreater(row['retained_context'][2],.99)
