"""Boundary tests on the real attention implementation, not a toy IIT circuit."""

from copy import deepcopy
import unittest
import numpy as np

from model.agent import Agent
from model.attention import Attention
from model.perception import scene


def checkpoint():
    agent = Agent(source=0)
    samples = np.stack([scene('horizontal', .73, -.61)] * 2)
    mask = np.array([[1, 0, 0, 1]] * 2)
    for _ in range(136):
        agent.step(samples, mask)
    return agent, samples, mask


def stream_state(attention):
    return np.concatenate((attention.aperture[0], [attention.feedback[0],
                           attention.estimate[0], attention.predicted_feedback[0]]))


class AttentionBoundaryTests(unittest.TestCase):
    def test_four_coordinate_boundary_omits_direct_telemetry_cause(self):
        a, samples, mask = checkpoint()
        b = deepcopy(a)
        original = b.attention.aperture[0, 1]
        b.attention.aperture[0, 1] = .9
        # All four original IIT coordinates are initially identical.
        indices = [0, 4, 5, 6]
        np.testing.assert_array_equal(stream_state(a.attention)[indices],
                                      stream_state(b.attention)[indices])
        a.step(samples, mask)
        b.step(samples, mask)
        expected = a.sensory.p.dt / .5 * (.9 - original) / 4
        self.assertAlmostEqual(b.attention.feedback[0] - a.attention.feedback[0], expected)
        self.assertGreater(abs(expected), .001)

    def test_mean_aperture_is_not_a_closed_macrostate(self):
        a, b = Attention(), Attention()
        a.aperture[0] = [.8, .2, .2, .2]
        b.aperture[0] = [.2, .2, .2, .8]
        self.assertAlmostEqual(a.aperture[0].mean(), b.aperture[0].mean())
        # Identical telemetry/estimate/prediction and identical external drive.
        a.step([.5, 0])
        b.step([.5, 0])
        expected = -.025 * .6 * (1/.8 - 1/1.4) / 4
        self.assertAlmostEqual(a.aperture[0].mean() - b.aperture[0].mean(), expected)
        self.assertGreater(abs(expected), .001)

    def test_seven_state_component_matches_agent_under_declared_drive(self):
        agent, samples, mask = checkpoint()
        component = deepcopy(agent.attention)
        # Make the other stream entirely different. It cannot affect stream 0
        # under this explicitly supplied command trajectory.
        component.aperture[1] = .9
        component.feedback[1] = .1
        component.estimate[1] = .7
        component.predicted_feedback[1] = .2
        for _ in range(100):
            command = agent.desired_inspection.copy()
            component.step(command)
            agent.step(samples, mask)
            np.testing.assert_array_equal(stream_state(component), stream_state(agent.attention))

    def test_seven_states_still_require_external_desired_command(self):
        a, b = Attention(), Attention()
        np.testing.assert_array_equal(stream_state(a), stream_state(b))
        a.step([0, 0])
        b.step([1, 0])
        self.assertGreater(np.max(np.abs(stream_state(a) - stream_state(b))), .01)
