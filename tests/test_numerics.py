import unittest

import numpy as np

from model.agent import Agent
from model.perception import scene


def integrate(dt, ambiguous):
    a = Agent(dt=dt)
    samples = np.stack([scene('horizontal', .73, -.61)] * 2)
    mask = np.array([[1, 0, 0, 1]] * 2) if ambiguous else np.ones((2, 4))
    first_report = None
    answers = set()
    queries = []
    for step in range(round(40 / dt)):
        result = a.step(samples, mask)
        if result['report_enabled']:
            first_report = (step + 1) * dt if first_report is None else first_report
            answers.add(result['yes'])
        if result['query'] and (not queries or queries[-1] != result['query']):
            queries.append(result['query'])
    return a.state_vector(), first_report, answers, queries


class NumericalTests(unittest.TestCase):
    def test_full_loop_timestep_refinement(self):
        for ambiguous in (False, True):
            with self.subTest(ambiguous=ambiguous):
                runs = [integrate(dt, ambiguous) for dt in (.025, .0125, .00625)]
                for state, report, answers, queries in runs:
                    self.assertIsNotNone(report)
                    self.assertEqual(answers, {True})
                    self.assertEqual('inspect' in queries, ambiguous)
                np.testing.assert_allclose(runs[0][0], runs[-1][0], atol=.02, rtol=0)
                self.assertLess(max(r[1] for r in runs) - min(r[1] for r in runs), .5)

    def test_bad_steps_fail_before_construction(self):
        for dt in (0, -.1, .1, float('nan')):
            with self.assertRaises(ValueError):
                Agent(dt=dt)


if __name__ == '__main__':
    unittest.main()
