"""Explicit independent intervention ensemble; conditional dependence screen.

Each of eight units independently takes its declared near/far realization with
probability 1/2, giving 256 equiprobable valid initial microstates per input label.
The remaining reduced coordinates start at one declared prepared background and
evolve. Output quantization occurs only at the endpoint. This is not a validated
Markov coarse-graining, IIT TPM, or naturally occurring noise distribution.
"""
from collections import Counter
from itertools import product
import json
import numpy as np
from experiments.population_alphabet import realize,encode,ALPHABETS
from experiments.reduced_persistence import project,configured_transition
from experiments.return_replay import prepare
from model.configuration import joint_configured


COORDINATES=((0,),(1,),(2,),(3,),(14,15,16),(17,18,19),(26,27,28),(32,))
PROBES=((0,0,0,0,0,0,0,0),(1,0,0,0,0,1,0,1),
        (1,1,0,0,0,1,0,1),(1,0,1,0,0,1,0,1))


def factorization_distance(outputs):
    """Exact TV between empirical joint row and product of its marginals."""
    counts=Counter(map(tuple,outputs))
    total=sum(counts.values())
    if not total:
        raise ValueError('nonempty outcome ensemble required')
    marginals=[Counter() for _ in ALPHABETS]
    for state,count in counts.items():
        if len(state)!=len(ALPHABETS) or any(not 0<=s<n for s,n in zip(state,ALPHABETS)):
            raise ValueError('invalid output labels')
        for i,s in enumerate(state):
            marginals[i][s]+=count/total
    overlap=sum(min(count/total,np.prod([marginals[i][s] for i,s in enumerate(state)]))
                for state,count in counts.items())
    return float(max(0,1-overlap))


def row(labels,background,steps=20):
    if not isinstance(steps,int) or steps<1:
        raise ValueError('positive integer horizon required')
    far,near=(realize(labels,background,p) for p in ('far','near'))
    outputs=[]
    for choices in product((0,1),repeat=8):
        state=far.copy()
        for coords,choice in zip(COORDINATES,choices):
            if choice:
                state[list(coords)]=near[list(coords)]
        if encode(state)!=tuple(labels):
            raise AssertionError('intervention leaves declared input label')
        for _ in range(steps):
            state=configured_transition(state)
        outputs.append(encode(state))
    return dict(initial=list(labels),steps=steps,realizations=len(outputs),
                distinct_successors=len(set(outputs)),
                self_transition_probability=outputs.count(tuple(labels))/len(outputs),
                joint_vs_product_tv=factorization_distance(outputs))


def evaluate():
    a=joint_configured()
    a.set_state(prepare(factory=joint_configured))
    background=project(a)
    return [row(labels,background) for labels in PROBES]


if __name__ == '__main__':
    print(json.dumps(evaluate(),indent=2))
