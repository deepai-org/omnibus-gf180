"""Continuous scene changes without trial reset or an agent-visible change flag."""

import json
import numpy as np

from .agent import Agent
from .perception import scene


def run_switch(new_scene, sigma=0, seed=419):
    agent = Agent(source=0)
    dt = agent.sensory.p.dt
    mask = np.ones((2, 4))
    rng = np.random.default_rng(seed)
    noise = rng.normal(0, sigma, (2, 4))
    decay = np.exp(-dt / .5)
    innovation = sigma * np.sqrt(1 - decay ** 2)

    def step(values):
        nonlocal noise
        noise = decay * noise + innovation * rng.normal(size=(2, 4))
        return agent.step(np.clip(np.stack([values] * 2) + noise, -1, 1),
                          mask, learn_outcomes=False)

    for _ in range(800):
        result = step(scene('horizontal', .73, -.61))
    initial_correct = result['report_enabled'] and result['yes']
    transitions = []
    withdrawal = None
    first_new_report = None
    wrong_reports_after_withdrawal = 0
    for k in range(1000):
        result = step(scene(*new_scene))
        elapsed = (k + 1) * dt
        state = (result['report_enabled'], result['yes'])
        if not transitions or transitions[-1]['state'] != state:
            transitions.append(dict(time=elapsed, state=state))
        if not result['report_enabled'] and withdrawal is None:
            withdrawal = elapsed
        # Both declared changes make the correct answer negative.
        if withdrawal is not None and result['report_enabled']:
            wrong_reports_after_withdrawal += int(result['yes'])
            if not result['yes'] and first_new_report is None:
                first_new_report = elapsed
    return dict(scene=new_scene, sigma=sigma, initial_correct=bool(initial_correct),
                withdrawal=withdrawal, first_new_report=first_new_report,
                wrong_reports_after_withdrawal=wrong_reports_after_withdrawal,
                final_group=agent.sensory.specialists[0].result()['group'],
                transitions=transitions)


def evaluate():
    return [run_switch(s, sigma) for sigma in (0, .05)
            for s in (('horizontal', -.73, .61), ('vertical', .73, -.61))]


if __name__ == '__main__':
    print(json.dumps(evaluate(), indent=2))
