import unittest
import numpy as np
from model.association import Association
from model.agent import Agent
from model.perception import scene
from model.workspace import Workspace
from model.primitives import quality_encode


class AssociationTests(unittest.TestCase):
    def test_weights_are_validated_and_detached_from_upload_buffer(self):
        weights = np.broadcast_to(np.eye(3)[:, None, :], (3, 3, 3)).copy()
        a = Association(weights)
        weights[:] = 0
        np.testing.assert_array_equal(a.retrieve([1, 0, 0], [1, 0, 0]), [1, 0, 0])
        with self.assertRaises(ValueError):
            Association(weights)
        with self.assertRaises(ValueError):
            a.weights[0, 0, 0] = 0

    def test_changed_association_revokes_stale_report(self):
        w = Workspace()
        for _ in range(800):
            result = w.step([1, 0, 0], quality_encode([.7, -.6]), [1, 0, 0])
        self.assertTrue(result['report_enabled'])
        result = w.step([1, 0, 0], quality_encode([.7, -.6]), [0, 1, 0])
        self.assertFalse(result['report_enabled'])
        for _ in range(800):
            result = w.step([1, 0, 0], quality_encode([.7, -.6]), [0, 1, 0])
        self.assertTrue(result['report_enabled'])
        self.assertFalse(result['yes'])

    def test_default_preserves_context_rule(self):
        a = Association()
        for c in np.eye(3):
            for g in np.eye(3):
                np.testing.assert_array_equal(a.retrieve(c, g), c)

    def test_content_and_context_jointly_address_uploaded_mapping(self):
        weights = np.zeros((3, 3, 3))
        for c in range(3):
            for g in range(3):
                weights[c, g, (c+g)%3] = 1
        a = Association(weights)
        for c in range(3):
            for g in range(3):
                np.testing.assert_array_equal(a.retrieve(np.eye(3)[c], np.eye(3)[g]),
                                              np.eye(3)[(c+g)%3])

    def test_uploaded_association_changes_agent_answer(self):
        weights = np.broadcast_to(np.eye(3)[:, None, :], (3, 3, 3)).copy()
        weights[0, 0] = [0, 1, 0]
        answers = []
        for mapping in (None, weights):
            a = Agent(source=0, association_weights=mapping)
            for _ in range(1000):
                result = a.step(np.stack([scene('horizontal', .73, -.61)]*2), np.ones((2, 4)))
            self.assertTrue(result['report_enabled'])
            answers.append(result['yes'])
        self.assertEqual(answers, [True, False])

    def test_memory_return_changes_candidate_activity(self):
        a = Agent(source=0)
        a.content.activity[:] = [.8, 0]
        a.content.group[0] = [1, 0, 0]
        a.workspace.memory[:] = [0, 1, 0]
        b = Agent(source=0)
        b.set_state(a.state_vector())
        a.step(np.zeros((2, 4)), np.ones((2, 4)))
        b.step(np.zeros((2, 4)), np.ones((2, 4)), memory_feedback=False)
        self.assertLess(a.content.activity[0], b.content.activity[0])
