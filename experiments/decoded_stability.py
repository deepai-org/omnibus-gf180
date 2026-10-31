"""Explicit detector redesign candidate; no sensory state removed yet."""
import json
from model.configuration import joint_configured
from experiments.context_ambiguity import run_case


def configured(dt=.025):
    a=joint_configured(dt)
    a.decoded_stability=True
    return a


def evaluate():
    for lesion in (None,'context_return','context_admission','inspection'):
        rows=[run_case(c,s,lesion=lesion,factory=configured,distractor=True)
              for c in ('horizontal','vertical') for s in (-1,1)]
        yield dict(lesion=lesion,correct=sum(r['correct'] for r in rows),
                   reports=sum(r['report'] for r in rows),
                   latencies=[r['elapsed'] for r in rows])


if __name__ == '__main__':
    for row in evaluate():
        print(json.dumps(row),flush=True)
