import unittest

import numpy as np

from model.agent import Agent
from model.observer import Observer
from model.perception import scene


class ObserverTests(unittest.TestCase):
    def test_aperture_attenuation_is_not_scene_conflict(self):
        o = Observer()
        for _ in range(400):
            o.step(np.full((2, 4), .3), np.full((2, 4), .5), np.full((2, 3, 4), .6))
        self.assertLess(np.max(o.conflict), .001)
        np.testing.assert_allclose(o.evidence, .5, atol=.001)

    def test_same_content_different_evidence_support(self):
        a, b = Observer(), Observer()
        x = np.full((2, 4), .6)
        predictions = np.full((2, 3, 4), .6)
        groups = np.array([[1, 0, 0]] * 2)
        for _ in range(400):
            a.step(x, np.ones((2, 4)), predictions)
            b.step(np.zeros((2, 4)), np.zeros((2, 4)), predictions)
        ra, rb = a.readout(groups), b.readout(groups)
        self.assertTrue(np.all(ra['admitted']))
        self.assertFalse(np.any(rb['admitted']))
        self.assertTrue(np.all(rb['prediction_dependence'] > .7))
        self.assertTrue(np.all(ra['precision_scale'] > rb['precision_scale']))

    def test_estimates_bound_to_content(self):
        o = Observer()
        predictions = np.zeros((2, 3, 4))
        predictions[:, 0, :] = .6
        predictions[:, 1, :] = -.6
        for _ in range(400):
            o.step(np.full((2, 4), .6), np.ones((2, 4)), predictions)
        supported = o.readout([[1, 0, 0]] * 2)
        unsupported = o.readout([[0, 1, 0]] * 2)
        self.assertTrue(np.all(supported['support'] > .9))
        self.assertTrue(np.all(unsupported['conflict'] > .9))
        self.assertEqual(o.state_vector().shape, (18,))

    def test_observer_clamp_changes_agent_reporting(self):
        a = Agent()
        samples = np.stack([scene('horizontal', .73, -.61)] * 2)
        for _ in range(1600):
            a.observer.evidence[:] = 0
            result = a.step(samples, np.ones((2, 4)))
            self.assertFalse(result['report_enabled'])
        # First-order content was still correctly discriminated under the clamp.
        self.assertEqual(a.sensory.specialists[0].result()['group'], 'horizontal')
        for _ in range(1000):
            result = a.step(samples, np.ones((2, 4)))
            if result['report_enabled']:
                break
        self.assertTrue(result['report_enabled'])
        self.assertTrue(result['yes'])


if __name__ == '__main__':
    unittest.main()
