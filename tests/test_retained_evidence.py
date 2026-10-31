"""Reports after withdrawal require a real, decaying acquisition trace."""
import unittest
import numpy as np
from model.configuration import configured
from model.agent import Agent
from model.perception import scene


class RetainedEvidenceTests(unittest.TestCase):
    def test_forced_workspace_selection_does_not_block_other_stream_evidence(self):
        agent = Agent(source=0)
        for _ in range(400):
            agent.step([np.zeros(4),scene('horizontal',.73,-.61)],
                       [[0]*4,[1]*4],task_enabled=False,input_enabled=(0,1))
        self.assertGreater(agent.support[1],.9)
        self.assertEqual(agent.support[0],0)
        self.assertEqual(agent.content.activity[1],0)

    @classmethod
    def setUpClass(cls):
        agent = configured()
        for _ in range(600):
            agent.step([np.zeros(4),scene('horizontal',.73,-.61)],
                       [[0]*4,[1]*4],task_enabled=False,input_enabled=(0,1))
        for _ in range(80):
            agent.step(np.zeros((2,4)),np.zeros((2,4)),
                       task_enabled=False,input_enabled=(0,0))
        for _ in range(1600):
            result = agent.step([[0,.7,-.7,0],[0]*4],[[1,0,0,1],[0]*4],
                                input_enabled=(1,0))
            if result['report_enabled']:
                break
        if not result['report_enabled'] or not result['yes']:
            raise AssertionError('physical acquisition failed')
        cls.acquired = agent.state_vector()

    def agent(self):
        agent = configured()
        agent.set_state(self.acquired)
        return agent

    def test_recent_physical_evidence_survives_shutter_briefly(self):
        agent = self.agent()
        acquired_stability = agent.support.copy()
        reports = []
        for _ in range(80):
            result = agent.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0))
            reports.append(result['report_enabled'])
        self.assertTrue(reports[0])
        self.assertFalse(any(reports[-20:]))
        np.testing.assert_array_equal(agent.support,acquired_stability)

    def test_confident_content_without_observer_evidence_cannot_report(self):
        agent = self.agent()
        agent.observer.evidence[:] = 0
        result = agent.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0))
        self.assertFalse(result['report_enabled'])

    def test_partial_observation_does_not_use_withdrawal_exception(self):
        agent = self.agent()
        agent.attention.aperture[:] = 0
        result = agent.step(np.zeros((2,4)),[[1,0,0,0],[0]*4],input_enabled=(1,0))
        self.assertFalse(result['report_enabled'])
