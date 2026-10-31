"""Context cue -> blank delay -> ambiguous object, one fixed configuration.

Class labels occur only in the fixture and scorer, never as Agent.step inputs.
This is a cross-specialist task, not yet a proof of reciprocal-path necessity.
"""
import json
from itertools import product
import numpy as np
from model.agent import Agent
from model.perception import GROUPS, scene


def run_case(context, group, sign, lesion=None, delay=2.):
    a = Agent(rule=(1/3, 1/3, 1/3), source=0,
              context_source=None if lesion == 'context' else 1)
    samples = np.stack([np.zeros(4), scene(context, .73, -.61)])
    mask = np.array([[0, 0, 0, 0], [1, 1, 1, 1]])
    for _ in range(600):
        a.step(samples, mask, task_enabled=False,input_enabled=(0,1))
    cue_group = a.sensory.specialists[1].result()['group']
    for _ in range(round(delay/a.sensory.p.dt)):
        a.step(np.zeros((2, 4)), np.zeros((2, 4)), task_enabled=False,input_enabled=(0,0))
    retained = a.rule.copy()
    samples = np.stack([scene(group, sign*.73, -sign*.61), np.zeros(4)])
    mask = np.array([[1, 0, 0, 1], [0, 0, 0, 0]])
    options = dict(suppress='inspect' if lesion == 'inspection' else None,
                   sensory_feedback=lesion != 'sensory_return',
                   observer_feedback=lesion != 'observer_return',
                   memory_feedback=lesion != 'memory_return')
    inspected = False
    for k in range(1600):
        result = a.step(samples, mask, input_enabled=(1,0), **options)
        inspected |= result['query'] == 'inspect'
        if result['report_enabled']:
            break
    expected = context == group and sign > 0
    return dict(context=context, group=group, sign=sign, lesion=lesion,
                report=result['report_enabled'], answer=result['yes'], expected=expected,
                correct=bool(result['report_enabled'] and result['yes'] == expected),
                cue_group=cue_group, retained_context=retained.tolist(),
                local_group=a.sensory.specialists[0].result()['group'],
                inspected=inspected, elapsed=(k+1)*a.sensory.p.dt)


if __name__ == '__main__':
    rows = [run_case(c, g, s) for c, g, s in product(GROUPS, GROUPS, (-1, 1))]
    print(json.dumps(dict(total=len(rows), correct=sum(r['correct'] for r in rows),
                         max_elapsed=max(r['elapsed'] for r in rows),
                         failures=[r for r in rows if not r['correct']]), indent=2))
