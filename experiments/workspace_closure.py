"""Falsify proposed workspace boundaries using valid omitted-state changes.

Candidate coordinates start identically in each pair, as do all future external
inputs and parameters. Any next-state difference disproves deterministic closure
for that boundary under this intervention. No binary coarse-graining or Phi.
Passing this finite screen would not prove closure.
"""
from copy import deepcopy
import json
import numpy as np
from experiments.return_replay import configured, prepare


CANDIDATES = {
    'content': ('content.',),
    'content_memory': ('content.','workspace.memory'),
    'content_memory_observer': ('content.','workspace.memory','observer.'),
    'content_memory_observer_sensory': ('content.','workspace.memory','observer.','sensory.'),
}


def evaluate():
    base = configured()
    base.set_state(prepare())
    for _ in range(12):
        base.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0))
    changes = {
        'local_group': ('sensory.0.group',np.array([0.,1.,0.])),
        'local_observation': ('sensory.0.x',np.array([-.7,.7,.7,-.7])),
        'observer_conflict': ('observer.conflict',np.ones((2,3))),
        'retrieved_memory': ('workspace.memory',np.array([0.,1.,0.])),
        'stored_context': ('rule',np.array([0.,1.,0.])),
        'query_activity': ('workspace.query',np.array([1.,0.,0.,0.])),
        'precision': ('learned_variance',np.array([4.,4.])),
    }
    results = []
    for name,prefixes in CANDIDATES.items():
        chosen = [i for i,n in enumerate(base.state_names()) if n.startswith(prefixes)]
        probes = []
        for label,(field,value) in changes.items():
            if field.startswith(prefixes):
                continue
            a,b = deepcopy(base),deepcopy(base)
            dict(b.state_fields())[field][:] = value
            # Validate full state and explicitly verify candidate identity.
            b.set_state(b.state_vector())
            np.testing.assert_array_equal(a.state_vector()[chosen],b.state_vector()[chosen])
            differences = []
            for _ in range(40):
                for agent in (a,b):
                    agent.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0))
                differences.append(float(np.max(np.abs(a.state_vector()[chosen]-b.state_vector()[chosen]))))
            probes.append(dict(omitted=label,field=field,next_step=differences[0],
                               max_over_one_unit=max(differences)))
        results.append(dict(candidate=name,coordinates=len(chosen),probes=probes,
                            closure_falsified=any(p['max_over_one_unit']>1e-12 for p in probes)))
    return results


if __name__ == '__main__':
    print(json.dumps(evaluate(),indent=2))
