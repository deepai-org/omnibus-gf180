import unittest
import numpy as np
from experiments.retention_timing import factory
from model.content_workspace import ContentWorkspace
from model.observer import Observer


class RetentionTimingTests(unittest.TestCase):
    def test_activity_time_constant_scales_only_activity_update(self):
        fast,slow = ContentWorkspace(),ContentWorkspace(activity_tau=1.)
        for a in (fast,slow):
            a.step([1,0],np.full((2,3),1/3),np.zeros((2,2)),[1,0])
        np.testing.assert_allclose(fast.activity,2*slow.activity)
        np.testing.assert_array_equal(fast.adaptation,slow.adaptation)
        np.testing.assert_array_equal(fast.group,slow.group)

    def test_observer_time_constant_scales_all_observer_states(self):
        fast,slow = Observer(),Observer(tau=2.)
        for a in (fast,slow):
            a.step(np.ones((2,4))*.3,np.full((2,4),.5),np.ones((2,3,4))*.4)
        np.testing.assert_allclose(fast.state_vector(),2*slow.state_vector())

    def test_factory_preserves_configuration_across_branch_creation(self):
        build = factory(1.,2.)
        a,b = build(),build()
        b.set_state(a.state_vector())
        self.assertEqual(b.content.activity_tau,1.)
        self.assertEqual(b.observer.tau,2.)
        np.testing.assert_array_equal(a.association.weights,b.association.weights)

    def test_invalid_time_constants(self):
        for value in (0,-1,float('nan'),float('inf')):
            with self.assertRaises(ValueError):
                ContentWorkspace(activity_tau=value)
            with self.assertRaises(ValueError):
                Observer(tau=value)
