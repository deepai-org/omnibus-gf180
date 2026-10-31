"""All subsets of the three inbound specialist paths, same prepared state.

These are edge lesions, not IIT partitions. Outgoing broadcasts, sensory input,
and all stored coordinates are preserved; only selected return terms are zeroed.
"""
import json
from itertools import combinations
import numpy as np
from experiments.return_replay import prepare, trajectory


def evaluate():
    initial = prepare()
    baseline,_,names = trajectory(initial)
    activity = names.index('content.activity[0]')
    rows = []
    for n in range(4):
        for cuts in combinations(('sensory','observer','memory'),n):
            states,_,_ = trajectory(initial,cuts=cuts)
            rows.append(dict(cuts=list(cuts),active_time=float(np.sum(states[:,activity]>.7)*.025),
                             max_state_difference=float(np.max(np.abs(states-baseline)))))
    return rows


if __name__ == '__main__':
    print(json.dumps(evaluate(),indent=2))
