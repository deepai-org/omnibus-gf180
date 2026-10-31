"""Two-way replay during the actual contextual distractor acquisition task.

Fixed declared stimulus and base visibility; the agent retains control of its
own aperture. Partitions are state-transition substitutions, not physical cuts
or IIT noising. No claim of post-cut behavioral success is made from state norms.
"""
import json
from functools import partial
import numpy as np
from model.configuration import joint_configured as configured
from experiments.bidirectional_replay import PARTITIONS,record,partitioned
from model.perception import scene


SAMPLES=np.array([[0,.7,-.7,0],[.7,-.7,-.7,.7]])
VISIBILITY=np.array([[1,0,0,1],[1,1,1,1]])


def advance(state,factory=configured):
    a=factory()
    a.set_state(state)
    a.step(SAMPLES,VISIBILITY)
    return a.state_vector()


def prepared(factory=configured):
    a=factory()
    dt=a.sensory.p.dt
    for _ in range(round(15/dt)):
        a.step([np.zeros(4),scene('horizontal',.73,-.61)],[[0]*4,[1]*4],
               input_enabled=(0,1),task_enabled=False)
    for _ in range(round(2/dt)):
        a.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0),task_enabled=False)
    for _ in range(round(10/dt)):
        a.step(SAMPLES,VISIBILITY)
    return a


def evaluate(factory=configured):
    a=prepared(factory)
    step=partial(advance,factory=factory)
    steps=round(4/a.sensory.p.dt)
    initial=a.state_vector()
    reference=record(initial,steps,step)
    a.content.group[0]=a.content.group[0][[1,0,2]]
    perturbed=a.state_vector()
    live=record(perturbed,steps,step)
    rows=[]
    for name,prefixes in PARTITIONS.items():
        selected=np.array([n.startswith(prefixes) for n in a.state_names()])
        nominal=partitioned(initial,reference,selected,step)
        cut=partitioned(perturbed,reference,selected,step)
        rows.append(dict(partition=name,coordinates=int(selected.sum()),
            nominal_max_error=float(np.max(np.abs(nominal-reference))),
            cut_other_side_change=float(np.max(np.abs(cut[:,~selected]-reference[:,~selected]))),
            live_other_side_change=float(np.max(np.abs(live[:,~selected]-reference[:,~selected]))),
            live_cut_difference=float(np.max(np.abs(live-cut)))))
    return rows


if __name__ == '__main__':
    print(json.dumps(evaluate(),indent=2))
