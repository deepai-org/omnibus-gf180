"""Exact projected state candidate for the fully shuttered operating phase.

83 coordinates retain content, both sensory circuits, observer, retrieved memory,
stored context and retrieval-query activity. Other query/attention coordinates
cannot affect these equations while both physical input enables are zero.
This is a phase-restricted continuous model, not a small binary IIT substrate.
"""
from copy import deepcopy
import json
import numpy as np
from experiments.return_replay import configured, prepare


def indices(agent):
    return [i for i,n in enumerate(agent.state_names())
            if n.startswith(('content.','sensory.','observer.','workspace.memory','rule['))
            or n == 'workspace.query[0]']


def transition(state):
    """One closed-phase step; all 83 retained coordinates are explicit.

    Fixed parameters are those of configured(); the other 27 coordinates are
    initialized canonically and discarded, relying on the declared shuttered
    dependency argument. No claim for acquisition, reporting or learning modes.
    """
    a = configured()
    selected = indices(a)
    state = np.asarray(state,dtype=float)
    if state.shape != (len(selected),):
        raise ValueError('83-coordinate closed-phase state required')
    full = a.state_vector()
    full[selected] = state
    a.set_state(full)
    a.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0))
    return a.state_vector()[selected]


def screen(trials=100, steps=20):
    rng = np.random.default_rng(9917)
    base = configured()
    base.set_state(prepare())
    included = indices(base)
    omitted = sorted(set(range(base.state_count))-set(included))
    reference = []
    a = deepcopy(base)
    for _ in range(steps):
        a.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0))
        reference.append(a.state_vector()[included])
    worst = 0.
    for _ in range(trials):
        a = deepcopy(base)
        state = a.state_vector()
        state[omitted] = rng.random(len(omitted))
        for i,n in enumerate(a.state_names()):
            if n.startswith('learned_variance'):
                state[i] = rng.uniform(.0625,4)
        a.set_state(state)
        for target in reference:
            a.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0))
            worst = max(worst,float(np.max(np.abs(a.state_vector()[included]-target))))
    return dict(included=len(included),omitted=len(omitted),trials=trials,steps=steps,
                max_error=worst,omitted_names=[base.state_names()[i] for i in omitted])


if __name__ == '__main__':
    print(json.dumps(screen(),indent=2))
