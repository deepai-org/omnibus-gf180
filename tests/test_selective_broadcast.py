import unittest
from experiments.context_ambiguity import run_case


class SelectiveBroadcastTests(unittest.TestCase):
    def test_same_prior_lesion_spares_clear_evidence_but_blocks_contextual_ambiguity(self):
        for clear in ('vertical',None):
            intact = run_case('horizontal',1,exposed=True,clear_group=clear)
            cut = run_case('horizontal',1,'sensory_return',exposed=True,clear_group=clear)
            self.assertTrue(intact['correct'],intact)
            if clear is None:
                self.assertFalse(cut['report'],cut)
            else:
                self.assertTrue(cut['correct'],cut)
                self.assertGreater(cut['group'][1],.85)
