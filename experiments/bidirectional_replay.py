"""Two-way state-boundary replay at the declared discrete transition grain.

For cut A|B, evaluate F_A(x_A, r_B) and F_B(r_A, x_B) separately, with r the
unperturbed recorded trajectory. Both parts retain their own evolving state;
neither receives the other's perturbed state. Same external input at every step.
This is an externally driven causal control, NOT IIT maximum-entropy noising,
an autonomous split chip, or a claim about individual transistor-level cuts.
"""
import json
import numpy as np
from model.configuration import joint_configured as configured
from experiments.return_replay import prepare


PARTITIONS = {
    'content': ('content.',),
    'content_memory': ('content.','workspace.memory'),
    'content_memory_observer': ('content.','workspace.memory','observer.'),
}


def step(state):
    a=configured()
    a.set_state(state)
    a.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0))
    return a.state_vector()


def record(initial,steps=80,advance=step):
    states=[initial.copy()]
    for _ in range(steps):
        states.append(advance(states[-1]))
    return np.stack(states)


def partitioned(initial,reference,selected,advance=step):
    selected=np.asarray(selected,dtype=bool)
    if selected.shape!=initial.shape or not selected.any() or selected.all():
        raise ValueError('proper nonempty state partition required')
    state=initial.copy()
    states=[state.copy()]
    for background in reference[:-1]:
        left=advance(np.where(selected,state,background))
        right=advance(np.where(selected,background,state))
        state=np.where(selected,left,right)
        states.append(state.copy())
    return np.stack(states)


def evaluate():
    initial=prepare(factory=configured)
    reference=record(initial)
    a=configured()
    a.set_state(initial)
    a.content.group[0]=a.content.group[0][[1,0,2]]
    perturbed=a.state_vector()
    live=record(perturbed)
    rows=[]
    for name,prefixes in PARTITIONS.items():
        selected=np.array([n.startswith(prefixes) for n in a.state_names()])
        nominal=partitioned(initial,reference,selected)
        cut=partitioned(perturbed,reference,selected)
        rows.append(dict(partition=name,coordinates=int(selected.sum()),
            nominal_max_error=float(np.max(np.abs(nominal-reference))),
            cut_other_side_change=float(np.max(np.abs(cut[:,~selected]-reference[:,~selected]))),
            live_other_side_change=float(np.max(np.abs(live[:,~selected]-reference[:,~selected]))),
            perturbed_live_cut_difference=float(np.max(np.abs(live-cut)))))
    return rows


if __name__ == '__main__':
    print(json.dumps(evaluate(),indent=2))
