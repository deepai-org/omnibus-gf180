"""Counterexample to extending the shuttered 35-coordinate model to acquisition.

Observer evidence/conflict differences are equal, but their common modes differ.
The full model can distinguish these via recruitment/admission while observations
are present. Both realizations are valid full-agent states; no new weights or
future inputs differ within a paired trial. This is not an IIT calculation.
"""
from copy import deepcopy
import json
import numpy as np
from model.configuration import joint_configured as configured
from experiments.return_replay import prepare
from experiments.reduced_persistence import project
from model.perception import scene


def evaluate():
    a=configured()
    a.set_state(prepare(factory=configured))
    a.content.activity[:]=[.15,0]
    a.content.adaptation[:]=[.1,0]
    a.sensory.specialists[0].x[:]=scene('horizontal',.2,-.2)
    a.observer.evidence[:]=.5
    a.observer.conflict[:]=.25
    b=deepcopy(a)
    b.observer.evidence[:]=.75
    b.observer.conflict[:]=.5
    for agent in (a,b):
        agent.set_state(agent.state_vector())
    np.testing.assert_array_equal(project(a),project(b))
    rows=[]
    for visible in (False,True):
        left,right=deepcopy(a),deepcopy(b)
        samples=np.stack([scene('horizontal',.2,-.2),np.zeros(4)])
        for agent in (left,right):
            agent.step(samples,np.ones((2,4)),input_enabled=(int(visible),0))
        delta=np.abs(project(left)-project(right))
        rows.append(dict(visible=visible,max_reduced_difference=float(delta.max()),
                         activity_difference=float(delta[0]),
                         changed_coordinates=np.flatnonzero(delta>1e-12).tolist()))
    return dict(initial_projected_difference=0.,
                intervention='equal observer differences, different common modes',
                rows=rows)


if __name__ == '__main__':
    print(json.dumps(evaluate(),indent=2))
