import unittest

import numpy as np

from model.agent import Agent
from model.perception import scene


class OutcomeTests(unittest.TestCase):
    def complete_trial(self, agent, samples, reward=True):
        agent.reset_trial()
        for _ in range(1600):
            result = agent.step(samples, np.ones((2, 4)))
            if result['report_enabled']:
                break
        self.assertTrue(result['report_enabled'])
        if reward:
            # Environmental scoring uses the emitted answer, never changes agent inputs.
            consequence = float(result['yes'])
            for _ in range(200):
                agent.step(samples, np.ones((2, 4)), reward=consequence)
        return result

    def test_reversed_source_contingency_is_relearned(self):
        agent = Agent()
        misleading = scene('horizontal', -.73, .61)
        useful = scene('horizontal', .73, -.61)
        original = np.stack([misleading, useful])
        self.assertFalse(self.complete_trial(agent, original)['yes'])
        good = self.complete_trial(agent, original)
        self.assertTrue(good['yes'])
        self.assertEqual(good['source'], 1)
        reversed_samples = np.stack([useful, misleading])
        results = [self.complete_trial(agent, reversed_samples) for _ in range(4)]
        self.assertFalse(results[0]['yes'])
        self.assertTrue(results[-1]['yes'])
        self.assertEqual(results[-1]['source'], 0)

    def test_checkpoint_restores_learned_choice_and_credit_owner(self):
        agent = Agent()
        samples = np.stack([scene('horizontal', -.73, .61), scene('horizontal', .73, -.61)])
        self.complete_trial(agent, samples)
        restored = Agent()
        restored.set_state(agent.state_vector())
        for _ in range(20):
            self.assertEqual(agent.step(samples, np.ones((2, 4)), reward=0),
                             restored.step(samples, np.ones((2, 4)), reward=0))
            np.testing.assert_array_equal(agent.state_vector(), restored.state_vector())
        original_result = self.complete_trial(agent, samples, reward=False)
        restored_result = self.complete_trial(restored, samples, reward=False)
        self.assertEqual(original_result, restored_result)
        self.assertEqual(restored_result['source'], 1)

    def test_outcome_changes_next_trial_choice_and_freezes(self):
        a = Agent()
        # Same underlying task; source 0 supplies a misleading quality sign.
        # Environment consequence is delivered only AFTER the emitted answer.
        samples = np.stack([scene('horizontal', -.73, .61), scene('horizontal', .73, -.61)])
        mask = np.ones((2, 4))
        for _ in range(1600):
            result = a.step(samples, mask)
            if result['report_enabled']:
                break
        self.assertTrue(result['report_enabled'])
        self.assertEqual(result['source'], 0)
        self.assertFalse(result['yes'])
        reward = float(result['yes'])  # Task's externally evaluated correct answer is yes.
        for _ in range(200):
            a.step(samples, mask, reward=reward)
        self.assertLess(a.outcomes.value[0], a.outcomes.value[1])
        self.assertEqual(a.source, 0)  # Credit cannot migrate during feedback.
        learned = a.outcomes.value.copy()
        a.reset_trial()
        np.testing.assert_array_equal(a.outcomes.value, learned)
        for _ in range(1600):
            result = a.step(samples, mask, reward=0, learn_outcomes=False)
            if result['report_enabled']:
                break
        self.assertTrue(result['report_enabled'])
        self.assertEqual(result['source'], 1)
        self.assertTrue(result['yes'])
        np.testing.assert_array_equal(a.outcomes.value, learned)

    def test_feedback_before_answer_cannot_train(self):
        a = Agent()
        before = a.outcomes.value.copy()
        a.step(np.zeros((2, 4)), np.ones((2, 4)), reward=0)
        np.testing.assert_array_equal(before, a.outcomes.value)


if __name__ == '__main__':
    unittest.main()
