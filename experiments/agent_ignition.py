"""Integrated stimulus amplitude/duration sweep, with physical withdrawal.

Activity validity is reported separately from retained content and local state.
A zero-amplitude presentation is an essential negative control. No success
threshold is fitted to these trials. Times are normalized model units.
"""
import json
import numpy as np
from model.configuration import configured
from model.perception import scene


def run_case(amplitude, duration, dt=.025, cut_after=False,factory=configured):
    a = factory(dt=dt)
    samples = np.stack([scene('horizontal',amplitude,-amplitude),np.zeros(4)])
    peak = 0.
    reports = 0
    for _ in range(round(duration/dt)):
        result = a.step(samples,np.ones((2,4)),input_enabled=(1,0))
        peak = max(peak,float(a.content.activity[0]))
        reports += int(result['report_enabled'])
    at_removal = dict(activity=float(a.content.activity[0]),
                      group=a.content.group[0].tolist(),quality=a.content.quality[0].tolist(),
                      local_group=a.sensory.specialists[0].group.tolist(),
                      observer_support=float(a.observer.readout(a.content.group)['support'][0]))
    active_after = 0
    for _ in range(round(20/dt)):
        a.step(np.zeros((2,4)),np.zeros((2,4)),input_enabled=(0,0),
               recurrent_returns=not cut_after)
        active_after += int(a.content.bundle()['valid'])
    return dict(amplitude=amplitude,duration=duration,dt=dt,cut_after=cut_after,peak=peak,
                reports=reports,at_removal=at_removal,
                active_time_after_removal=active_after*dt,
                final_activity=float(a.content.activity[0]))


if __name__ == '__main__':
    for amplitude in (0,.02,.2,.7):
        for duration in (.25,1.,4.):
            print(json.dumps(run_case(amplitude,duration)),flush=True)
