"""Same behavioral controls, one fixed 94-state candidate configuration."""
import json
from experiments.decoded_agent import configured
from experiments.joint_distractor import CONDITIONS,evaluate_condition
from experiments.free_competition import run_case as switching
from experiments.agent_ignition import run_case as ignition


def evaluate():
    for condition in CONDITIONS:
        row=evaluate_condition(*condition,factory=configured)
        yield dict(test='joint_task',result={k:v for k,v in row.items() if k!='rows'})
    for first in (0,1):
        yield dict(test='switching',result=switching(first,factory=configured))
    for cut in (False,True):
        yield dict(test='persistence',result=ignition(.7,4,cut_after=cut,factory=configured))


if __name__ == '__main__':
    for row in evaluate():
        print(json.dumps(row),flush=True)
