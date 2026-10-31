from itertools import product
import unittest
import numpy as np

from experiments.attention_dynamics import drive, step, read_stream, write_stream
from model.attention import Attention
from model.agent import Agent
from model.perception import scene


class AttentionDynamicsTests(unittest.TestCase):
    def test_all_binary_interventions_against_actual_component(self):
        # All seven retained variables independently intervened; no thresholding
        # of the output and no selection of favorable current states.
        for bits in product((0., 1.), repeat=7):
            state = np.array(bits)
            for desired in (0., .5, 1.):
                for gain, tau, dt in ((.65, .5, .025), (1., 1., .0125), (1.4, 3., .025)):
                    component = Attention(dt, actuator_gain=gain, actuator_tau=tau)
                    write_stream(component, state)
                    write_stream(component, 1-state, stream=1)
                    expected = step(state, desired, dt, gain, tau)
                    component.step([desired, 1-desired])
                    np.testing.assert_allclose(read_stream(component), expected, atol=2e-15, rtol=0)

    def test_interior_interventions_and_command_trajectory(self):
        rng = np.random.default_rng(801)
        component = Attention()
        state = rng.uniform(size=7)
        write_stream(component, state)
        for _ in range(500):
            desired = rng.uniform()
            state = step(state, desired)
            component.step([desired, rng.uniform()])
            np.testing.assert_allclose(read_stream(component), state, atol=2e-14, rtol=0)

    def test_replay_endogenous_input_from_complete_agent(self):
        agent = Agent(source=0)
        state = read_stream(agent.attention)
        samples = np.stack([scene('horizontal', .73, -.61)]*2)
        for _ in range(800):
            state = step(state, float(agent.desired_inspection[0]))
            agent.step(samples, np.array([[1, 0, 0, 1]]*2))
            np.testing.assert_allclose(read_stream(agent.attention), state, atol=2e-14, rtol=0)

    def test_recurrent_edges_exist_at_unsaturated_operating_point(self):
        x = np.full(7, .5)
        jacobian = np.column_stack([(drive(x+np.eye(7)[i]*1e-6, .5)-
                                    drive(x-np.eye(7)[i]*1e-6, .5))/2e-6 for i in range(7)])
        # Actual estimator->aperture->telemetry->estimator loop and prediction loop.
        self.assertLess(jacobian[0, 5], 0)
        self.assertGreater(jacobian[4, 0], 0)
        self.assertGreater(jacobian[5, 4], 0)
        self.assertLess(jacobian[5, 6], 0)
        self.assertGreater(jacobian[6, 5], 0)

    def test_invalid_inputs_rejected(self):
        for x, u in ((np.zeros(6), .5), (np.full(7, 2), .5), (np.zeros(7), np.nan)):
            with self.assertRaises(ValueError):
                drive(x, u)
