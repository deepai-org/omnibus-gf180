import unittest
import numpy as np
from experiments.context_ambiguity import run_case


class ContextAmbiguityTests(unittest.TestCase):
    def test_unknown_return_cut_rejected(self):
        with self.assertRaises(ValueError):
            run_case('horizontal',return_cuts=('unknown',))

    def test_sensory_inbound_cut_is_not_outgoing_broadcast_cut(self):
        intact = run_case('horizontal',1)
        inbound = run_case('horizontal',1,return_cuts=('sensory',))
        self.assertTrue(inbound['correct'],inbound)
        self.assertGreater(inbound['elapsed'],intact['elapsed'])
        self.assertIsNone(inbound['lesion'])

    def test_uniform_and_contradictory_evidence_override_context(self):
        for group in ('vertical','one_object'):
            row = run_case('horizontal',1,exposed=True,clear_group=group)
            self.assertTrue(row['correct'],row)
            self.assertFalse(row['answer'])

    def test_context_and_contrast_jointly_determine_answer(self):
        for context in ('horizontal','vertical'):
            for sign in (-1,1):
                row = run_case(context,sign)
                self.assertTrue(row['correct'],row)
                self.assertGreater(min(row['aperture']),.9)

    def test_matched_visible_evidence_needs_context_return(self):
        intact = run_case('horizontal',1,exposed=True)
        cut = run_case('horizontal',1,'context_return',exposed=True)
        self.assertTrue(intact['correct'],intact)
        self.assertFalse(cut['report'],cut)
        np.testing.assert_allclose(cut['group'],[.5,.5,0],atol=1e-6)

    def test_inspection_lesion_blocks_hidden_contrast(self):
        row = run_case('horizontal',1,'inspection')
        self.assertFalse(row['report'],row)
