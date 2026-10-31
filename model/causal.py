"""Agent-derived interventional transition tables for boundary screening.

Not an IIT implementation. No Phi is calculated. Omitted states are initialized
from a declared background, then evolve; this is a conditional finite-horizon
model and may fail closure under either background or within-bin changes.
"""

from copy import deepcopy
from itertools import product
import json

import numpy as np

from .agent import Agent
from .perception import scene


CANDIDATE = ('sensory.0.z[0,0]', 'observer.evidence[0,0]',
             'attention.estimate[0]', 'desired_inspection[0]')
CANDIDATES = {
    'distributed': (CANDIDATE, 'sensory.0.z[0,1]'),
    'attention': (('attention.aperture[0,0]', 'attention.feedback[0]',
                   'attention.estimate[0]', 'attention.predicted_feedback[0]'),
                  'attention.aperture[0,1]'),
}


def transition_table(agent, samples, visibility, names=CANDIDATE, steps=40,
                     low=.1, high=.9, threshold=.5):
    if not isinstance(steps, int) or steps < 1 or not low < threshold < high:
        raise ValueError('invalid transition sampling parameters')
    if not 1 <= len(names) <= 8 or len(set(names)) != len(names):
        raise ValueError('one to eight distinct state coordinates required')
    indices = [agent.state_names().index(name) for name in names]
    rows = []
    for bits in product((0, 1), repeat=len(indices)):
        trial = deepcopy(agent)
        state = trial.state_vector()
        state[indices] = np.where(bits, high, low)
        trial.set_state(state)
        for _ in range(steps):
            trial.step(samples, visibility)
        final = trial.state_vector()[indices]
        rows.append({'initial': list(bits), 'final_continuous': final.tolist(),
                     'final_binary': (final >= threshold).astype(int).tolist()})
    return rows


def difference(a, b):
    if len(a) != len(b) or any(x['initial'] != y['initial'] for x, y in zip(a, b)):
        raise ValueError('transition rows must have identical interventions')
    return {
        'changed_rows': sum(x['final_binary'] != y['final_binary'] for x, y in zip(a, b)),
        'max_continuous_difference': float(max(np.max(np.abs(
            np.asarray(x['final_continuous']) - y['final_continuous'])) for x, y in zip(a, b))),
    }


def boundary_screen(candidate='distributed', phase='early'):
    if phase not in ('early', 'inspection'):
        raise ValueError('unknown checkpoint phase')
    names, background_name = CANDIDATES[candidate]
    samples = np.stack([scene('horizontal', .73, -.61)] * 2)
    visibility = np.array([[1, 0, 0, 1]] * 2)
    agent = Agent()
    for step in range(200 if phase == 'early' else 2000):
        agent.step(samples, visibility)
        if phase == 'inspection' and agent.workspace.query[1] > .9 and agent.inspection[0] > .25:
            break
    else:
        if phase == 'inspection':
            raise RuntimeError('declared active-inspection checkpoint not reached')
    other = deepcopy(agent)
    # Change a declared omitted state, never one of the candidate coordinates.
    background_state = other.state_vector()
    background_state[other.state_names().index(background_name)] = .9
    other.set_state(background_state)
    reports = []
    for steps in (20, 80):
        nominal = transition_table(agent, samples, visibility, names=names, steps=steps)
        background = transition_table(other, samples, visibility, names=names, steps=steps)
        within_bin = transition_table(agent, samples, visibility, names=names, steps=steps, low=.4, high=.6)
        reports.append({'steps': steps, 'duration': steps * agent.sensory.p.dt,
                        'background_sensitivity': difference(nominal, background),
                        'within_bin_sensitivity': difference(nominal, within_bin),
                        'nominal_table': nominal})
    return {'candidate': candidate, 'phase': phase, 'checkpoint_step': step + 1,
            'checkpoint_inspect_query': float(agent.workspace.query[1]),
            'checkpoint_aperture': float(agent.inspection[0]),
            'names': names, 'background_intervention': background_name,
            'interpretation': 'boundary screen, not IIT Phi', 'reports': reports}


if __name__ == '__main__':
    print(json.dumps(boundary_screen(), indent=2))
