import unittest
import numpy as np
from model.content_workspace import ContentWorkspace

GROUPS = [[1,0,0],[0,1,0]]
QUALITIES = [[.7,-.6],[-.4,.8]]


class ContentWorkspaceTests(unittest.TestCase):
    def test_checkpoint_and_invalid_intervention_are_atomic(self):
        w = ContentWorkspace()
        self.advance(w, [.8, 0], [1, 1], 120)
        saved = w.state_vector()
        other = ContentWorkspace()
        other.set_state(saved)
        np.testing.assert_array_equal(other.state_vector(), saved)
        for index, value in ((0, 2), (2, .2), (8, -2), (13, float('nan'))):
            invalid = saved.copy()
            invalid[index] = value
            with self.assertRaises(ValueError):
                other.set_state(invalid)
            np.testing.assert_array_equal(other.state_vector(), saved)

    def advance(self, w, evidence, available, steps, recurrence=True):
        for _ in range(steps):
            w.step(evidence, GROUPS, QUALITIES, available, recurrence=recurrence)

    def test_weak_input_remains_unbroadcast(self):
        w = ContentWorkspace()
        self.advance(w,[.15,0],[1,1],400)
        self.assertFalse(w.bundle()['valid'])

    def test_content_persistence_then_adaptive_release(self):
        w = ContentWorkspace()
        self.advance(w,[.8,0],[1,1],120)
        self.assertTrue(w.bundle()['valid'])
        self.assertEqual(w.bundle()['source'],0)
        np.testing.assert_allclose(w.bundle()['quality'],QUALITIES[0],atol=.02)
        held = w.group.copy(), w.quality.copy()
        self.advance(w,[0,0],[0,0],20)
        self.assertTrue(w.bundle()['valid'])
        np.testing.assert_array_equal(w.group,held[0])
        np.testing.assert_array_equal(w.quality,held[1])
        self.advance(w,[0,0],[0,0],1200)
        self.assertFalse(w.bundle()['valid'])

    def test_without_recurrence_no_sustained_broadcast(self):
        w = ContentWorkspace()
        self.advance(w,[.8,0],[1,1],120,recurrence=False)
        self.advance(w,[0,0],[0,0],40,recurrence=False)
        self.assertFalse(w.bundle()['valid'])

    def test_new_evidence_can_change_selected_content(self):
        w = ContentWorkspace()
        self.advance(w,[.8,0],[1,1],120)
        self.advance(w,[0,1],[0,1],800)
        self.assertTrue(w.bundle()['valid'])
        self.assertEqual(w.bundle()['source'],1)
        self.assertEqual(w.state_vector().shape,(14,))
