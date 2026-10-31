"""Seeded correlated observation-noise stress test, not physical noise data.

Noise is part of the environment, before aperture attenuation. It does not
provide hidden truth, confidence or query choices to the agent. Its correlation
time and stationary variance are explicit and independent of integration step.
"""

import json

import numpy as np

from .agent import Agent
from .perception import GROUPS, scene


def run_noisy(group, sigma, seed, duration=40, dt=.025, quality_sign=1, suppress=None):
    if (not np.isfinite(sigma) or sigma < 0 or not np.isfinite(duration)
            or not np.isfinite(dt) or dt <= 0 or duration < dt):
        raise ValueError('finite nonnegative noise and positive duration required')
    agent = Agent(rule=np.eye(3)[GROUPS.index(group)], source=0, dt=dt)
    if quality_sign not in (-1, 1):
        raise ValueError('quality sign must be -1 or 1')
    truth = np.stack([scene(group, quality_sign * .73, quality_sign * -.61)] * 2)
    mask = np.array([[1, 0, 0, 1]] * 2)
    rng = np.random.default_rng(seed)
    noise = rng.normal(0, sigma, (2, 4))
    decay = np.exp(-dt / .5)
    innovation = sigma * np.sqrt(1 - decay ** 2)
    for k in range(int(duration / dt)):
        noise = decay * noise + innovation * rng.normal(size=(2, 4))
        result = agent.step(np.clip(truth + noise, -1, 1), mask, learn_outcomes=False,
                            suppress=suppress)
        if result['report_enabled']:
            break
    inferred = agent.sensory.specialists[0].result()['group']
    return dict(group=group, sigma=sigma, seed=seed, reported=result['report_enabled'],
                quality_sign=quality_sign,
                correct=bool(result['report_enabled'] and result['yes'] == (quality_sign > 0) and inferred == group),
                inferred_group=inferred, answer=result['yes'], elapsed=(k + 1) * dt,
                convergence_support=float(agent.support[0]))


def evaluate():
    rows = [run_noisy(group, sigma, seed) for sigma in (0, .005, .02, .05)
            for group in GROUPS for seed in (17, 83)]
    summary = []
    for sigma in (0, .005, .02, .05):
        selected = [r for r in rows if r['sigma'] == sigma]
        summary.append(dict(sigma=sigma, total=len(selected), reports=sum(r['reported'] for r in selected),
                            correct=sum(r['correct'] for r in selected)))
    return dict(noise='OU observation noise, tau=.5, stationary standard deviation sigma',
                summary=summary, cases=rows)


if __name__ == '__main__':
    print(json.dumps(evaluate(), indent=2))
