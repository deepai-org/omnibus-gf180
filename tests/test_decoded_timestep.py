"""The reduced candidate must retain behavior without a favorable Euler step."""
import unittest
from experiments.candidate_timestep import evaluate
from experiments.decoded_agent import configured


class DecodedTimestepTests(unittest.TestCase):
    def test_task_and_switching_at_two_steps(self):
        rows=list(evaluate(configured))
        for row in rows:
            self.assertEqual(row['task_correct'],4,row)
            for first,switch in enumerate(row['switches']):
                self.assertEqual([p['final_source'] for p in switch['phases']],
                                 [first,1-first])
                for phase in switch['phases']:
                    self.assertEqual(phase['simultaneous_high_steps'],0)
        for coarse,fine in zip(rows[0]['task_latencies'],rows[1]['task_latencies']):
            self.assertLess(abs(coarse-fine),.1)
