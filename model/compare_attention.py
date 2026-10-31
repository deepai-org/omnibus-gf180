"""Exploratory matched-controller sweep, not a held-out AST acceptance test.

Run: python3 -m model.compare_attention
No parameters are fitted separately for individual conditions. This sweep was
used during model development, so future acceptance needs untouched conditions.
"""

import json

import numpy as np

from .attention import Attention


def score(gain, tau, direct_feedback):
    plant = Attention(actuator_gain=gain, actuator_tau=tau)
    error = 0.0
    for k in range(800):
        target = np.array([.65, .2]) if (k // 160) % 2 == 0 else np.array([.2, .65])
        plant.step(target, direct_feedback=direct_feedback)
        error += float(np.sum((plant.aperture.mean(axis=1) - target) ** 2)) * plant.dt
    return error


def comparison():
    return [dict(gain=gain, tau=tau, model_error=score(gain, tau, False),
                 direct_feedback_error=score(gain, tau, True))
            for gain in (.65, 1., 1.4) for tau in (.5, 1., 3.)]


if __name__ == '__main__':
    print(json.dumps(comparison(), indent=2))
