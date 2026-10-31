import unittest

import numpy as np

from model.agent import Agent
from model.primitives import categorical_memory_drive
from model.perception import scene


class ContextTests(unittest.TestCase):
    def test_removed_cue_controls_answer_after_delay(self):
        samples = np.stack([scene('horizontal', .73, -.61)] * 2)
        for rule in range(3):
            for delay in (.5, 2, 8):
                with self.subTest(rule=rule, delay=delay):
                    # Start in a DIFFERENT context so preload cannot pass this test.
                    a = Agent(rule=np.eye(3)[(rule + 1) % 3])
                    cue = np.eye(3)[rule]
                    for _ in range(80):
                        result = a.step(np.zeros((2, 4)), np.zeros((2, 4)),
                                        context_cue=cue, task_enabled=False)
                        self.assertFalse(result['report_enabled'])
                    self.assertGreater(a.rule[rule], .99)
                    for _ in range(round(delay / .025)):
                        result = a.step(np.zeros((2, 4)), np.zeros((2, 4)), task_enabled=False)
                        self.assertFalse(result['report_enabled'])
                    for _ in range(1600):
                        result = a.step(samples, np.ones((2, 4)))
                        if result['report_enabled']:
                            break
                    self.assertTrue(result['report_enabled'])
                    self.assertEqual(result['yes'], rule == 0)
                    self.assertGreater(a.rule[rule], .99)

    def test_memory_intervention_changes_answer_at_fixed_scene(self):
        samples = np.stack([scene('horizontal', .73, -.61)] * 2)
        answers = []
        for lesion in (False, True):
            a = Agent()
            for _ in range(80):
                a.step(np.zeros((2, 4)), np.zeros((2, 4)), context_cue=[0, 1, 0], task_enabled=False)
            if lesion:
                a.rule[:] = [1, 0, 0]
            for _ in range(1600):
                result = a.step(samples, np.ones((2, 4)))
                if result['report_enabled']:
                    break
            self.assertTrue(result['report_enabled'])
            self.assertEqual(a.sensory.specialists[0].result()['group'], 'horizontal')
            answers.append(result['yes'])
        self.assertEqual(answers, [False, True])

    def test_each_context_restores_after_in_basin_perturbation(self):
        for winner in range(3):
            x = np.roll(np.array([.6, .25, .15]), winner)
            for _ in range(400):
                x += .025 * categorical_memory_drive(x)
            self.assertGreater(x[winner], .999)
            self.assertAlmostEqual(x.sum(), 1)
            self.assertTrue(np.all(x >= 0))

    def test_crossing_basin_can_change_memory(self):
        x = np.array([.45, .5, .05])
        for _ in range(400):
            x += .025 * categorical_memory_drive(x)
        self.assertGreater(x[1], .999)

    def test_restoration_runs_inside_agent_without_new_states(self):
        a = Agent(rule=(.6, .25, .15))
        for _ in range(400):
            a.step(np.zeros((2, 4)), np.ones((2, 4)))
        self.assertGreater(a.rule[0], .999)
        self.assertEqual(a.state_vector().size, 110)


if __name__ == '__main__':
    unittest.main()
