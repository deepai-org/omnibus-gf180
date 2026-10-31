"""Joint-agent composition grid; no per-case parameter fitting.

Run python3 -m model.evaluate. This is not the plan's full 72-cell temporal task:
it is a separately enumerated 72-case grouping/context/quality/visibility/source
grid. The distinction matters: equal cell counts do not imply equal coverage.
"""

from itertools import product
import json

import numpy as np

from .agent import Agent
from .perception import GROUPS, scene


def cases():
    return [dict(group=g, rule=r, sign=sign, occluded=occluded, source=source)
            for g, r, sign, occluded, source in product(GROUPS, GROUPS, (-1, 1), (False, True), (0, 1))]


def run_case(case, duration=40):
    g, rule, sign, source = (case[k] for k in ('group', 'rule', 'sign', 'source'))
    a = Agent(rule=np.eye(3)[GROUPS.index(rule)], source=source)
    first, second = sign * .43, -sign * .87
    samples = np.stack([scene('vertical', -.67, .51)] * 2)
    samples[source] = scene(g, first, second)
    mask = np.ones((2, 4))
    if case['occluded']:
        mask[source] = [1, 0, 0, 1]
    queries = []
    for k in range(round(duration / a.sensory.p.dt)):
        result = a.step(samples, mask, learn_outcomes=False)
        if result['query'] and (not queries or queries[-1] != result['query']):
            queries.append(result['query'])
        if result['report_enabled']:
            break
    actual_group = a.sensory.specialists[source].result()['group']
    expected = g == rule and first > 0
    return dict(case=case, report=bool(result['report_enabled']), answer=bool(result['yes']),
                expected=expected, group=actual_group, expected_group=g,
                correct=bool(result['report_enabled'] and result['yes'] == expected and actual_group == g),
                elapsed=(k + 1) * a.sensory.p.dt, queries=queries)


def evaluate():
    rows = [run_case(case) for case in cases()]
    return dict(total=len(rows), correct=sum(row['correct'] for row in rows),
                reports=sum(row['report'] for row in rows),
                max_elapsed=max(row['elapsed'] for row in rows),
                failures=[row for row in rows if not row['correct']])


if __name__ == '__main__':
    print(json.dumps(evaluate(), indent=2))
