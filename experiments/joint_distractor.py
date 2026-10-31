"""Same uploaded configuration/task, separately named interaction lesions.

Interpretation and retained context are scored separately from Boolean answers:
an always-negative answer may accidentally match half of this balanced task.
These edge/gate interventions are not IIT partitions or activity-matched cuts.
"""
import json
from experiments.context_ambiguity import run_case
from model.configuration import joint_configured as configured


CONDITIONS = (
    ('intact',None,()),
    ('retrieved_context_to_sensory','context_return',()),
    ('workspace_to_sensory','sensory_return',()),
    ('inspection','inspection',()),
    ('observer_context_admission','context_admission',()),
    ('sensory_persistence',None,('sensory',)),
    ('observer_selection_and_persistence',None,('observer',)),
    ('memory_persistence',None,('memory',)),
)


def evaluate_condition(name,lesion,cuts,factory=configured):
    rows = [run_case(c,s,lesion=lesion,return_cuts=cuts,
                     factory=factory,distractor=True)
            for c in ('horizontal','vertical') for s in (-1,1)]
    interpreted = [r['group'][0 if r['context']=='horizontal' else 1]>.85 for r in rows]
    retained = [r['retained_context'][0 if r['context']=='horizontal' else 1]>.85 for r in rows]
    return dict(condition=name,total=len(rows),
                correct_answers=sum(r['correct'] for r in rows),
                reports=sum(r['report'] for r in rows),
                correct_interpretations=sum(interpreted),
                correct_retained_context=sum(retained),
                coherent_success=sum(r['correct'] and g and c and r['selected_source']==0
                                     for r,g,c in zip(rows,interpreted,retained)),rows=rows)


if __name__ == '__main__':
    for condition in CONDITIONS:
        result=evaluate_condition(*condition)
        print(json.dumps({k:v for k,v in result.items() if k!='rows'}),flush=True)
