"""Fixed physical durations, two numerical steps, identical candidate weights."""
import json
from functools import partial
from model.configuration import joint_configured as configured
from experiments.context_ambiguity import run_case as context_case
from experiments.free_competition import run_case as competition


def evaluate(configuration=configured):
    for dt in (.025,.0125):
        factory=partial(configuration,dt=dt)
        cases=[context_case(c,s,factory=factory,distractor=True)
               for c in ('horizontal','vertical') for s in (-1,1)]
        switches=[competition(i,factory=factory) for i in (0,1)]
        yield dict(dt=dt,task_correct=sum(r['correct'] for r in cases),
                   task_total=len(cases),task_latencies=[r['elapsed'] for r in cases],
                   switches=switches)


if __name__ == '__main__':
    for row in evaluate():
        print(json.dumps(row),flush=True)
