"""Exhaustive within-label sensitivity screen, not an IIT transition model.

All omitted coordinates start from the same actual prepared agent and evolve
under the exact closed-shutter reduction. No state is reset between timesteps.
Different successors disprove deterministic closure for the declared labels.
Agreement would not prove closure over all realizations or backgrounds.
"""
from itertools import product
import json
from experiments.population_alphabet import ALPHABETS, NAMES, encode, realize
from experiments.reduced_persistence import project, configured_transition
from experiments.return_replay import configured, prepare


def evaluate(horizons=(1, 20), labels=None):
    if not horizons or any(not isinstance(n, int) or n < 1 for n in horizons):
        raise ValueError('positive integer horizons required')
    agent = configured()
    agent.set_state(prepare())
    background = project(agent)
    labels = product(*(range(n) for n in ALPHABETS)) if labels is None else labels
    results = {n: dict(steps=n, duration=n*.025, changed_rows=0,
                      changed_by_unit=[0]*8, witnesses=[]) for n in horizons}
    count = 0
    for initial in labels:
        states = [realize(initial, background, p) for p in ('far', 'near')]
        for step in range(1, max(horizons)+1):
            states = [configured_transition(s) for s in states]
            if step in results:
                far, near = map(encode, states)
                row = results[step]
                differences = [int(a != b) for a, b in zip(far, near)]
                row['changed_by_unit'] = [a+b for a,b in
                                         zip(row['changed_by_unit'], differences)]
                if any(differences):
                    row['changed_rows'] += 1
                    if len(row['witnesses']) < 4:
                        row['witnesses'].append(dict(initial=list(initial),
                                                    far=far, near=near))
        count += 1
    return dict(units=NAMES, alphabets=ALPHABETS, total_rows=count,
                boundary='closed shutters; prepared background evolves',
                interpretation='within-label sensitivity, not IIT',
                results=list(results.values()))


if __name__ == '__main__':
    print(json.dumps(evaluate(), indent=2))
