"""Same uploaded agent: contextual ambiguity vs clear local controls.

All object pixels are exposed in every condition to match physical information.
Cutting the outgoing sensory prior does not touch report predicates, local
sensory updates, memory acquisition or the incoming return pathways.
"""
import json
from itertools import product
from experiments.context_ambiguity import run_case
from model.perception import GROUPS
from model.configuration import configured


def evaluate(factory=configured,distractor=False):
    rows = []
    for context,sign in product(('horizontal','vertical'),(-1,1)):
        for clear in (None,'horizontal','vertical','one_object'):
            for lesion in (None,'sensory_return'):
                row = run_case(context,sign,lesion,exposed=True,clear_group=clear,
                               factory=factory,distractor=distractor)
                row['condition'] = 'contextual_ambiguity' if clear is None else 'clear_local_control'
                row['local_correct'] = None if clear is None else row['group'][GROUPS.index(clear)] > .85
                rows.append(row)
    summary = []
    for condition in ('contextual_ambiguity','clear_local_control'):
        for lesion in (None,'sensory_return'):
            subset = [r for r in rows if r['condition']==condition and r['lesion']==lesion]
            summary.append(dict(condition=condition,lesion=lesion,total=len(subset),
                                correct=sum(r['correct'] for r in subset),
                                reports=sum(r['report'] for r in subset),
                                local_correct=sum(r['local_correct'] is True for r in subset)
                                if condition=='clear_local_control' else None))
    return dict(summary=summary,rows=rows,
                intervention='sensory_return fixture label disables Agent.sensory_feedback (outgoing prior), not inbound sensory agreement')


if __name__ == '__main__':
    print(json.dumps(evaluate(),indent=2))
