"""Equal-strength supported scene versus unexplained checkerboard input.

The good-source index belongs only to the stimulus fixture/scorer. Local
prediction residuals, not labels, feed the candidate recruitment mechanism.
This task-disabled selection probe is not a complete reasoning demonstration.
"""
import json
import numpy as np
from model.configuration import configured as historical_configured, joint_configured
from model.perception import scene


def configured(candidate=True,dt=.025):
    """Compatibility wrapper for the explicit candidate/comparator probe."""
    return (joint_configured if candidate else historical_configured)(dt=dt)


def run_case(good, candidate=False, cut=False):
    a = configured(candidate)
    samples = np.tile([.7,-.7,-.7,.7],(2,1))
    samples[good] = scene('horizontal',.7,-.7)
    counts = [0,0]
    for step in range(800):
        a.step(samples,np.ones((2,4)),task_enabled=False,observer_feedback=not cut)
        bundle = a.content.bundle()
        if bundle['valid']:
            counts[bundle['source']] += 1
    return dict(good=good,candidate=candidate,cut=cut,selected_steps=counts,
                final_source=a.source,final_activity=a.content.activity.tolist())


if __name__ == '__main__':
    for candidate in (False,True):
        for good in (0,1):
            for cut in (False,True):
                print(json.dumps(run_case(good,candidate,cut)),flush=True)
