"""Exploratory immutable timing configurations, NOT adopted baseline weights.

The same factory prepares each entire trial and every lesion branch. No slowing
or retuning occurs at withdrawal. All other parameters and fixture times match.
The exact reduced model currently describes only the default time constants.
"""
import json
from model.configuration import configured
from model.content_workspace import ContentWorkspace
from model.observer import Observer
from experiments.withdrawn_task import evaluate_case


def factory(activity_tau, observer_tau):
    def build():
        a = configured()
        dt = a.sensory.p.dt
        a.content = ContentWorkspace(dt,self_gain=.8,return_gain=.65,
                                     activity_tau=activity_tau)
        a.observer = Observer(dt,tau=observer_tau)
        return a
    return build


def evaluate():
    for activity_tau,observer_tau in ((.5,1.),(1.,1.),(.5,2.),(1.,2.)):
        rows = [evaluate_case(c,s,factory=factory(activity_tau,observer_tau))
                for c in ('horizontal','vertical') for s in (-1,1)]
        yield dict(activity_tau=activity_tau,observer_tau=observer_tau,
                   prior_reports=[r['prior_reports'] for r in rows],
                   branches=[dict(cuts=rows[0]['branches'][i]['cuts'],
                       correct=sum(bool(r['branches'][i]['first_report'] and
                           r['branches'][i]['first_report']['correct']) for r in rows))
                       for i in range(5)])


if __name__ == '__main__':
    for row in evaluate():
        print(json.dumps(row),flush=True)
