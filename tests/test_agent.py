import unittest

import numpy as np

from model.agent import Agent
from model.perception import GROUPS, scene
from model.primitives import quality_encode
from model.workspace import Workspace


def trial(group, first, second, rule, ambiguous, source=0, suppress=None):
    a = Agent(rule, source)
    samples = np.stack([scene('vertical', -.7, .8)] * 2)
    samples[source] = scene(group, first, second)
    mask = np.ones((2, 4))
    if ambiguous:
        mask[source] = [1, 0, 0, 1]
    queries = []
    for _ in range(2000):
        result = a.step(samples, mask, suppress=suppress)
        if result['query'] and (not queries or queries[-1] != result['query']):
            queries.append(result['query'])
        if result['report_enabled']:
            return a, queries, result
    return a, queries, result


class AgentTests(unittest.TestCase):
    def test_joint_perception_and_workspace(self):
        for source in (0, 1):
            for group in GROUPS:
                for first, second in ((.73, -.61), (-.73, .61)):
                    with self.subTest(source=source, group=group, first=first):
                        rule = np.eye(3)[GROUPS.index(group)]
                        a, queries, result = trial(group, first, second, rule, True, source)
                        self.assertTrue(result['report_enabled'], queries)
                        self.assertEqual(result['yes'], first > 0)
                        self.assertEqual(a.state_vector().shape, (110,))
                        self.assertEqual(a.sensory.specialists[source].result()['group'], group)

    def test_wrong_memory_changes_answer(self):
        _, _, result = trial('horizontal', .73, -.61, (0, 1, 0), False)
        self.assertTrue(result['report_enabled'])
        self.assertFalse(result['yes'])

    def test_real_scene_changes_query_sequence(self):
        _, clear, clear_result = trial('horizontal', .73, -.61, (1, 0, 0), False)
        _, ambiguous, ambiguous_result = trial('horizontal', .73, -.61, (1, 0, 0), True)
        self.assertTrue(clear_result['report_enabled'])
        self.assertTrue(ambiguous_result['report_enabled'])
        self.assertNotIn('inspect', clear)
        self.assertIn('inspect', ambiguous)

    def test_inspection_lesion_blocks_ambiguous_scene(self):
        _, _, result = trial('horizontal', .73, -.61, (1, 0, 0), True, suppress='inspect')
        self.assertFalse(result['report_enabled'])

    def test_changed_content_invalidates_old_answer(self):
        w = Workspace()
        for _ in range(600):
            result = w.step([1, 0, 0], quality_encode([.7, -.7]), [1, 0, 0])
        self.assertTrue(result['report_enabled'])
        self.assertTrue(result['yes'])
        result = w.step([1, 0, 0], quality_encode([-.7, .7]), [1, 0, 0])
        self.assertFalse(result['report_enabled'])
        for _ in range(600):
            result = w.step([1, 0, 0], quality_encode([-.7, .7]), [1, 0, 0])
        self.assertTrue(result['report_enabled'])
        self.assertFalse(result['yes'])


if __name__ == '__main__':
    unittest.main()
