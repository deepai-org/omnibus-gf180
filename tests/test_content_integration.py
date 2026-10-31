"""Content dependence, not a claim of distributed ignition or IIT integration."""
import unittest
import numpy as np
from model.agent import Agent
from model.perception import scene


class ContentIntegrationTests(unittest.TestCase):
    def test_content_prior_changes_ambiguous_local_inference(self):
        a = Agent(source=0)
        samples = np.stack([scene('horizontal', .73, -.61)] * 2)
        mask = np.tile([1, 0, 0, 1], (2, 1))
        # Prepare local beliefs without task-driven acquisition.
        for _ in range(400):
            a.step(samples, mask, task_enabled=False, sensory_feedback=False)
        a.content.activity[:] = [.8, 0]
        a.content.group[0] = [0, 1, 0]
        b = Agent(source=0)
        b.set_state(a.state_vector())
        a.step(samples, mask, task_enabled=False)
        b.step(samples, mask, task_enabled=False, sensory_feedback=False)
        self.assertGreater(a.sensory.specialists[0].group[1],
                           b.sensory.specialists[0].group[1])
        np.testing.assert_array_equal(a.sensory.specialists[1].state_vector(),
                                      b.sensory.specialists[1].state_vector())

    def test_observer_evidence_changes_workspace_persistence_drive(self):
        a = Agent(source=0)
        a.content.activity[:] = [.8, 0]
        a.observer.evidence[:] = 0
        a.observer.conflict[:] = 1
        b = Agent(source=0)
        b.set_state(a.state_vector())
        samples = np.zeros((2, 4))
        a.step(samples, np.ones((2, 4)), task_enabled=False)
        b.step(samples, np.ones((2, 4)), task_enabled=False, observer_feedback=False)
        self.assertLess(a.content.activity[0], b.content.activity[0])

    def prepared(self):
        a = Agent(source=0)
        samples = np.stack([scene('horizontal', .73, -.61)] * 2)
        for _ in range(800):
            result = a.step(samples, np.ones((2, 4)))
        self.assertTrue(result['report_enabled'])
        self.assertTrue(result['yes'])
        return a, samples

    def test_broadcast_gate_preserves_clear_local_perception(self):
        a, samples = self.prepared()
        for _ in range(200):
            result = a.step(samples, np.ones((2, 4)), broadcast_enabled=False)
        self.assertFalse(result['report_enabled'])
        self.assertEqual(a.sensory.specialists[0].result()['group'], 'horizontal')
        # This gate test alone is NOT evidence for reciprocal broadcast necessity.

    def test_payload_not_raw_sensory_bypass_determines_answer(self):
        a, samples = self.prepared()
        for _ in range(200):
            a.content.quality[0] = [-.73, .61]
            result = a.step(samples, np.ones((2, 4)))
        self.assertTrue(result['report_enabled'])
        self.assertFalse(result['yes'])
        self.assertEqual(a.sensory.specialists[0].result()['group'], 'horizontal')

    def test_all_content_states_survive_agent_checkpoint(self):
        a, samples = self.prepared()
        b = Agent(source=0)
        b.set_state(a.state_vector())
        for _ in range(30):
            a.step(samples, np.ones((2, 4)))
            b.step(samples, np.ones((2, 4)))
        np.testing.assert_array_equal(a.state_vector(), b.state_vector())
