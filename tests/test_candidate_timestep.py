import unittest
from functools import partial
from experiments.reliability_competition import configured
from experiments.context_ambiguity import run_case


class CandidateTimestepTests(unittest.TestCase):
    def test_same_task_survives_half_step_without_changing_physical_durations(self):
        rows=[run_case('horizontal',1,factory=partial(configured,dt=dt),distractor=True)
              for dt in (.025,.0125)]
        for row in rows:
            self.assertTrue(row['correct'],row)
            self.assertGreater(row['retained_context'][0],.99)
        self.assertLess(abs(rows[0]['elapsed']-rows[1]['elapsed']),.5)
        self.assertEqual([r['dt'] for r in rows],[.025,.0125])
