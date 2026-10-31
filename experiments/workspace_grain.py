"""Within-bin counterexamples for binary activity/adaptation coarse-graining.

This deliberately tests a tempting FOUR-coordinate candidate, not an alleged
complete workspace. All other state starts identically and evolves. A changed
binary successor for the same initial bins disproves an exact deterministic
TPM at that grain; it does not preclude a declared stochastic intervention model.
"""
from itertools import product
import json
import numpy as np
from experiments.return_replay import configured, prepare


NAMES = ('content.activity[0]','content.activity[1]',
         'content.adaptation[0]','content.adaptation[1]')


def table(low,high,steps):
    initial = prepare()
    a = configured()
    chosen = [a.state_names().index(n) for n in NAMES]
    rows = []
    for bits in product((0,1),repeat=4):
        a = configured()
        state = initial.copy()
        state[chosen] = np.where(bits,high,low)
        a.set_state(state)
        for _ in range(steps):
            a.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0))
        end = a.state_vector()[chosen]
        rows.append(dict(initial=list(bits),final=(end>=.5).astype(int).tolist(),
                         continuous=end.tolist()))
    return rows


def evaluate():
    rows = []
    for steps in (1,20,80):
        center,near = table(.1,.9,steps),table(.4,.6,steps)
        witnesses = [dict(initial=a['initial'],far=a['final'],near=b['final'],
                          far_continuous=a['continuous'],near_continuous=b['continuous'])
                     for a,b in zip(center,near) if a['final']!=b['final']]
        rows.append(dict(steps=steps,duration=steps*.025,changed_rows=len(witnesses),
                         total=16,witnesses=witnesses))
    return dict(candidate=list(NAMES),threshold=.5,levels=[[.1,.9],[.4,.6]],
                interpretation='within-bin sensitivity, not IIT',results=rows)


if __name__ == '__main__':
    print(json.dumps(evaluate(),indent=2))
