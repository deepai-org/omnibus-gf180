"""Test a stationary repeated-use interpretation of the intervention kernel.

If a one-step row is an exact self-loop, every power of that same Markov kernel
also stays there. Compare with direct 20-step evolution from the very same
initial ensemble. A mismatch invalidates that stationary label-only model, not
all possible stochastic coarse-grainings or explicitly time-dependent models.
"""
import json
from experiments.population_kernel import PROBES,row
from experiments.reduced_persistence import project
from experiments.return_replay import prepare
from model.configuration import joint_configured


def evaluate():
    a=joint_configured()
    a.set_state(prepare(factory=joint_configured))
    background=project(a)
    results=[]
    for labels in PROBES:
        short,long=row(labels,background,1),row(labels,background,20)
        absorbing=short['self_transition_probability']==1
        results.append(dict(initial=list(labels),one_step_self=short['self_transition_probability'],
            direct_twenty_step_self=long['self_transition_probability'],
            stationary_composition_tv=(1-long['self_transition_probability']) if absorbing else None,
            conclusion='stationary label-only kernel falsified' if absorbing and
                long['self_transition_probability']<1 else 'not falsified by this probe'))
    return results


if __name__ == '__main__':
    print(json.dumps(evaluate(),indent=2))
