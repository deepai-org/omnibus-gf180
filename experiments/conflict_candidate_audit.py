"""Joint controls for one conflict-weighted recruitment configuration."""
import json
from model.configuration import joint_configured as configured
from experiments.free_competition import run_case as competition
from experiments.agent_ignition import run_case as ignition
from experiments.context_ambiguity import run_case as context_case
from experiments.withdrawn_task import evaluate_case as withdrawn


def evaluate():
    for first in (0,1):
        yield dict(test='switching',result=competition(first,factory=configured))
    for amplitude,duration,cut in ((0,4,False),(.02,4,False),(.7,.25,False),
                                   (.7,4,False),(.7,4,True)):
        yield dict(test='ignition',result=ignition(amplitude,duration,
                   cut_after=cut,factory=configured))
    for context in ('horizontal','vertical'):
        for sign in (-1,1):
            for group in ('horizontal','vertical','one_object'):
                yield dict(test='clear',result=context_case(context,sign,exposed=True,
                           clear_group=group,factory=configured))
            row = withdrawn(context,sign,factory=configured)
            yield dict(test='withdrawal',result=dict(context=context,sign=sign,
                       prior_reports=row['prior_reports'],branches=[
                           dict(cuts=b['cuts'],first_report=b['first_report'])
                           for b in row['branches']]))


if __name__ == '__main__':
    for row in evaluate():
        print(json.dumps(row),flush=True)
