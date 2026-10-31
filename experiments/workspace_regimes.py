"""Development comparison of fixed activation regimes, not per-case fitting.

These candidates are NOT installed in Agent. Each replaces only the component
update for an entire trial; all specialist paths and report predicates stay fixed.
The emitted failures are part of the result, not filtered candidates.
"""
import json
from unittest.mock import patch
import numpy as np
from model.content_workspace import ContentWorkspace
from experiments.cross_stream import run_case


REGIMES = ((1.2, .25, .9), (.8, .5, .3), (.9, .5, .45))


def candidate_step(gains):
    self_gain, return_gain, adaptation_gain = gains

    def step(w, evidence, groups, qualities, available, feedback=(0,0), recurrence=True):
        e, g, z, v, f = map(np.asarray, (evidence, groups, qualities, available, feedback))
        old = w.activity.copy()
        raw = 2*(e*v + return_gain*f + (self_gain*old if recurrence else 0)
                 -1.2*old[::-1]-adaptation_gain*w.adaptation-.45)
        w.activity += w.dt/.5*(np.clip(raw,0,1)-old)
        w.group += w.dt/.5*(v*old)[:,None]*(g-w.group)
        w.quality += w.dt/.5*(v*old)[:,None]*(z-w.quality)
        w.adaptation += w.dt/8*(old-w.adaptation)
    return step


def evaluate(gains):
    rows = []
    with patch.object(ContentWorkspace, 'step', candidate_step(gains)):
        for context, group, sign in (('horizontal','horizontal',1),
                                      ('vertical','horizontal',1),
                                      ('horizontal','horizontal',-1)):
            for lesion in (None, 'sensory_return','observer_return','memory_return'):
                rows.append(run_case(context,group,sign,lesion))
    return dict(gains=gains, rows=rows)


if __name__ == '__main__':
    for gains in REGIMES:
        result = evaluate(gains)
        print(json.dumps(dict(gains=gains, cases=[{k:r[k] for k in
              ('context','group','sign','lesion','correct','elapsed','local_group')}
              for r in result['rows']])), flush=True)
