"""Identical ambiguous evidence, context-dependent object interpretation.

Horizontal and vertical fits are equally good for the off-diagonal contrast.
They assign opposite first-object qualities. The context cue specifies the
grouping convention, not the quality; contrast sign remains sensory evidence.
This fixture begins with both diagonal samples hidden and reveals contrast
through inspection. No labels are passed into the agent.
"""
import json
import numpy as np
from model.configuration import configured, association_weights
from model.perception import scene


def run_case(context, sign=1, lesion=None, exposed=False, clear_group=None,
             return_cuts=(), factory=configured, distractor=False):
    if set(return_cuts)-{'sensory','observer','memory'}:
        raise ValueError('unknown inbound specialist return')
    a = factory()
    dt = a.sensory.p.dt
    for _ in range(round(15/dt)):
        a.step(np.stack([np.zeros(4),scene(context,.73,-.61)]),
               [[0,0,0,0],[1,1,1,1]],task_enabled=False,input_enabled=(0,1))
    for _ in range(round(2/dt)):
        a.step(np.zeros((2,4)),np.zeros((2,4)),task_enabled=False,input_enabled=(0,0))
    samples = np.array([[0,.7*sign,-.7*sign,0],[0,0,0,0]])
    if distractor:
        samples[1] = [.7,-.7,-.7,.7]
    if clear_group is not None:
        samples[0] = scene(clear_group, .7*sign, -.7*sign)
    for k in range(round(40/dt)):
        result = a.step(samples,[[1,1,1,1] if exposed else [1,0,0,1],
                                [1,1,1,1] if distractor else [0,0,0,0]],
                        input_enabled=(1,int(distractor)),
                        context_feedback=lesion != 'context_return',
                        context_admission=lesion != 'context_admission',
                        sensory_feedback=lesion != 'sensory_return',
                        sensory_return='sensory' not in return_cuts,
                        observer_feedback='observer' not in return_cuts,
                        memory_feedback='memory' not in return_cuts,
                        suppress='inspect' if lesion == 'inspection' else None)
        if result['report_enabled']:
            break
    expected = (context == 'horizontal') == (sign > 0)
    if clear_group is not None:
        expected = clear_group == context and sign > 0
    return dict(context=context,sign=sign,lesion=lesion,exposed=exposed,
                return_cuts=list(return_cuts),distractor=distractor,
                retained_context=a.rule.tolist(),selected_source=a.source,
                clear_group=clear_group,expected=expected,
                report=result['report_enabled'],answer=result['yes'],
                correct=bool(result['report_enabled'] and result['yes']==expected),
                group=a.sensory.specialists[0].group.tolist(),
                aperture=a.attention.aperture[0].tolist(),elapsed=(k+1)*dt,dt=dt)


if __name__ == '__main__':
    for context in ('horizontal','vertical'):
        for sign in (-1,1):
            for lesion in (None,'context_return','sensory_return','inspection'):
                print(json.dumps(run_case(context,sign,lesion)),flush=True)
