"""Activity-matched open-loop replay vs live specialist return.

Record an intact trajectory after stimulus withdrawal, then deliver those exact
signals through an external intervention port. Nominal replay must reproduce
all 110 coordinates. Perturbed replay remains fixed to the *unperturbed* record;
it is not recomputed from the recipient. This is not an IIT partition/noising rule.
"""
import json
from unittest.mock import patch
import numpy as np
from model.configuration import configured
from model.content_workspace import ContentWorkspace
from model.perception import scene


def prepare(factory=configured):
    a = factory()
    samples = np.stack([scene('horizontal',.7,-.7),np.zeros(4)])
    for _ in range(160):
        a.step(samples,np.ones((2,4)),input_enabled=(1,0))
    return a.state_vector()


def trajectory(initial, replay=None, perturb=False, steps=160, cuts=(),factory=configured):
    a = factory()
    a.set_state(initial)
    if perturb:
        # Valid simplex-preserving content intervention, same in both arms.
        fraction = float(perturb)
        if not np.isfinite(fraction) or not 0 <= fraction <= 1:
            raise ValueError('perturbation fraction must lie in [0,1]')
        original_group = a.content.group[0].copy()
        a.content.group[0] = (1-fraction)*original_group + fraction*original_group[[1,0,2]]
    returns, states = [], []
    original = ContentWorkspace.step
    def record(w, evidence, groups, qualities, available, feedback=(0,0), recurrence=True):
        returns.append(np.asarray(feedback).copy())
        original(w,evidence,groups,qualities,available,feedback,recurrence)
    with patch.object(ContentWorkspace,'step',record):
        for k in range(steps):
            a.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0),
                   return_override=None if replay is None else replay[k],
                   sensory_return='sensory' not in cuts,
                   observer_feedback='observer' not in cuts,
                   memory_feedback='memory' not in cuts)
            states.append(a.state_vector())
    return np.stack(states),np.stack(returns),a.state_names()


def evaluate(perturbation=1.,factory=configured):
    initial = prepare(factory=factory)
    live,record,names = trajectory(initial,factory=factory)
    replay,_,_ = trajectory(initial,record,factory=factory)
    live_changed,changed_returns,_ = trajectory(initial,perturb=perturbation,factory=factory)
    replay_changed,_,_ = trajectory(initial,record,perturb=perturbation,factory=factory)
    i = names.index('content.activity[0]')
    return dict(perturbation=perturbation,nominal_max_state_error=float(np.max(np.abs(live-replay))),
                perturbed_max_state_difference=float(np.max(np.abs(live_changed-replay_changed))),
                perturbed_return_difference=float(np.max(np.abs(changed_returns-record))),
                intact_active_time=float(np.sum(live[:,i]>.7)*.025),
                live_perturbed_active_time=float(np.sum(live_changed[:,i]>.7)*.025),
                replay_perturbed_active_time=float(np.sum(replay_changed[:,i]>.7)*.025),
                steps=len(record),states=initial.size)


if __name__ == '__main__':
    print(json.dumps(evaluate(),indent=2))
