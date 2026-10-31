"""Unforced source competition and within-trial evidence reversal.

No source override, state reset, value reward or class cue is delivered between
phases. Both local specialists remain live. External amplitudes are the stimuli.
"""
import json
import numpy as np
from model.configuration import configured
from model.perception import scene


def run_case(first=0,factory=configured):
    a = factory()
    dt = a.sensory.p.dt
    phases = []
    for winner in (first,1-first):
        amplitudes = [.02,.02]
        amplitudes[winner] = .7
        samples = np.stack([scene('horizontal',amplitudes[0],-amplitudes[0]),
                            scene('vertical',amplitudes[1],-amplitudes[1])])
        first_selected = None
        coactive = 0
        for k in range(round(20/dt)):
            a.step(samples,np.ones((2,4)))
            bundle = a.content.bundle()
            if bundle['valid'] and bundle['source']==winner and first_selected is None:
                first_selected = (k+1)*dt
            coactive += int(np.all(a.content.activity>.7))
        phases.append(dict(expected_source=winner,first_selected=first_selected,
                           final_source=a.content.bundle()['source'],
                           final_valid=a.content.bundle()['valid'],
                           activity=a.content.activity.tolist(),
                           group=a.content.bundle()['group'].tolist(),
                           simultaneous_high_steps=coactive))
    return dict(initial_source=first,phases=phases)


if __name__ == '__main__':
    print(json.dumps([run_case(i) for i in (0,1)],indent=2))
