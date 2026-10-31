"""94-state candidate with an explicitly redesigned stability detector.

Equivalent to the 110-state decoded-stability candidate's readout dynamics, not
to the original population-shape detector. Reconstructed endpoint populations
are algebraic adapters only, never retained states or uncertainty estimates.
"""
import numpy as np
from model.agent import Agent
from model.perception import Perception
from model.primitives import quality_decode
from model.configuration import association_weights


class DecodedPerception(Perception):
    state_count=14

    @property
    def quality(self):
        population=np.zeros((2,5))
        population[:,0]=(1-self.decoded_quality)/2
        population[:,4]=(1+self.decoded_quality)/2
        return population

    @quality.setter
    def quality(self,value):
        self.decoded_quality=quality_decode(value).copy()

    def state_vector(self):
        return np.concatenate((self.x,self.latents,self.group,self.decoded_quality))

    def set_state(self,state):
        # Avoid inherited 22-state setter silently changing the representation.
        raise NotImplementedError('restore via DecodedAgent.set_state')


class DecodedAgent(Agent):
    state_count=94

    def __init__(self,**kwargs):
        if kwargs.get('decoded_stability',True) is not True:
            raise ValueError('reduced quality state requires decoded stability')
        kwargs['decoded_stability']=True
        super().__init__(**kwargs)

    def reset_trial(self):
        super().reset_trial()
        self.sensory.specialists=[DecodedPerception(self.sensory.p) for _ in range(2)]

    def state_fields(self):
        fields=[]
        for name,array in super().state_fields():
            if name.startswith('sensory.') and name.endswith('.quality'):
                index=int(name.split('.')[1])
                fields.append((name.replace('.quality','.decoded_quality'),
                               self.sensory.specialists[index].decoded_quality))
            else:
                fields.append((name,array))
        return fields


def configured(dt=.025):
    return DecodedAgent(rule=(1/3,1/3,1/3),context_source=1,context_prior_gain=.04,
                        association_weights=association_weights(),dt=dt,
                        reliability_selection=True)


def project(full):
    """Map the unreduced decoded-stability reference to the 94 retained states."""
    if not full.decoded_stability:
        raise ValueError('projection does not preserve population-shape stability')
    arrays=[]
    for name,array in full.state_fields():
        arrays.append(quality_decode(array) if name.startswith('sensory.') and
                      name.endswith('.quality') else array)
    return np.concatenate([a.ravel() for a in arrays])
