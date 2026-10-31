"""Inbound edge necessity on the contextual task, not an IIT partition test.

Cut only during the object phase. Cue acquisition and blank delay are identical;
the same physical stimulus/inspection policy is available in every arm. Lesions
remove return terms, not the specialists or their other effects on the agent.
"""
import json
from experiments.context_ambiguity import run_case


def evaluate():
    for cuts in ((), ('sensory',), ('observer',), ('memory',),
                 ('sensory','observer','memory')):
        rows = [run_case(context,sign,return_cuts=cuts)
                for context in ('horizontal','vertical') for sign in (-1,1)]
        yield dict(cuts=list(cuts), correct=sum(r['correct'] for r in rows),
                   reports=sum(r['report'] for r in rows), total=len(rows), rows=rows)


if __name__ == '__main__':
    for result in evaluate():
        print(json.dumps(result),flush=True)
