"""Matched attention-control path interventions in the complete agent.

These interventions retain all estimator states and workspace completion wiring.
They are not whole-schema ablations or a claim of AST satisfaction.
"""
import json
import numpy as np

from model.agent import Agent
from model.attention import Attention
from model.perception import scene


class ControlIntervention(Attention):
    def __init__(self, mode, **kwargs):
        if mode not in ('model', 'direct', 'command'):
            raise ValueError('unknown attention control intervention')
        super().__init__(**kwargs)
        self.mode = mode

    def step(self, desired):
        return super().step(desired, schema_enabled=self.mode != 'command',
                            direct_feedback=self.mode == 'direct')


def run(mode, gain=1, tau=1):
    agent = Agent(rule=(0, 1, 0), source=0)
    agent.attention = ControlIntervention(mode, actuator_gain=gain, actuator_tau=tau)
    samples = np.stack([scene('vertical', .43, -.87), scene('horizontal', -.67, .51)])
    mask = np.array([[1, 0, 0, 1], [1, 1, 1, 1]])
    for k in range(1600):
        result = agent.step(samples, mask, learn_outcomes=False)
        if result['report_enabled']:
            break
    group = agent.sensory.specialists[0].result()['group']
    return dict(mode=mode, gain=gain, tau=tau, elapsed=(k+1)*.025,
                reported=result['report_enabled'],
                correct=bool(result['report_enabled'] and result['yes'] and group == 'vertical'),
                grouping=group, aperture=float(agent.inspection[0]),
                estimate=float(agent.attention.estimate[0]),
                query=result['query'])


def evaluate():
    return [run(mode, gain, tau) for gain in (.65, 1, 1.4)
            for tau in (1, 3) for mode in ('model', 'direct', 'command')]


if __name__ == '__main__':
    print(json.dumps(evaluate(), indent=2))
