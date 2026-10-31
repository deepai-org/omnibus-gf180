"""Fixed-duration acquisition followed by matched closed-shutter branches.

Exposure times are fixture parameters, not triggered by an answer. Branches
share every stored coordinate at withdrawal; only inbound return terms differ.
Record prior reports explicitly so repetition cannot count as new computation.
"""
import json
import numpy as np
from model.configuration import configured
from model.perception import scene


def evaluate_case(context, sign, exposure=14.5, factory=configured):
    if context not in ('horizontal','vertical') or sign not in (-1,1):
        raise ValueError('declared context and contrast required')
    if not np.isfinite(exposure) or exposure <= 0:
        raise ValueError('positive finite exposure required')
    a = factory()
    for _ in range(600):
        a.step([np.zeros(4),scene(context,.73,-.61)],[[0]*4,[1]*4],
               task_enabled=False,input_enabled=(0,1))
    for _ in range(80):
        a.step(np.zeros((2,4)),np.zeros((2,4)),task_enabled=False,input_enabled=(0,0))
    prior_reports = 0
    steps = round(exposure/.025)
    for _ in range(steps):
        result = a.step([[0,.7*sign,-.7*sign,0],[0]*4],[[1,0,0,1],[0]*4],
                        input_enabled=(1,0))
        prior_reports += int(result['report_enabled'])
    initial = a.state_vector()
    expected = (context == 'horizontal') == (sign > 0)
    rows = []
    for cuts in ((),('sensory',),('observer',),('memory',),
                 ('sensory','observer','memory')):
        b = factory()
        b.set_state(initial)
        first = None
        report_count = 0
        trace = []
        for step in range(80):
            result = b.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0),
                            sensory_return='sensory' not in cuts,
                            observer_feedback='observer' not in cuts,
                            memory_feedback='memory' not in cuts)
            if step in (0,3,7,15,31,79):
                monitoring = b.observer.readout(b.content.group)
                owner = b.source
                addressed = b.association.retrieve(b.rule,b.content.group[owner])
                trace.append(dict(delay=(step+1)*.025,
                                  activity=float(b.content.activity[0]),
                                  stability=float(b.support[0]),
                                  admitted=bool(monitoring['admitted'][0]),
                                  memory_ready=bool(b.workspace.memory.sum()>=.9 and
                                      np.max(np.abs(b.workspace.memory-addressed))<.1),
                                  group_confidence=float(b.content.group[0].max()),
                                  comparison=b.workspace.comparison.tolist(),
                                  answer_query=float(b.workspace.query[3])))
            if result['report_enabled']:
                report_count += 1
                if first is None:
                    first = dict(delay=(step+1)*.025, answer=bool(result['yes']),
                                 correct=bool(result['yes']==expected))
        rows.append(dict(cuts=list(cuts),first_report=first,report_count=report_count,
                         trace=trace))
    return dict(context=context,sign=sign,exposure=steps*.025,
                prior_reports=prior_reports,expected=expected,branches=rows)


if __name__ == '__main__':
    for context in ('horizontal','vertical'):
        for sign in (-1,1):
            print(json.dumps(evaluate_case(context,sign)),flush=True)
