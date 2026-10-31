"""Independent input-conditioned equations for all 14 workspace coordinates.

This is NOT an autonomous IIT substrate: specialist targets, feedback and
availability are boundary inputs. Simplex coordinates must not be binarized
independently. `cut_competition` is a directed-edge intervention on both
cross-candidate inhibitory edges, not an IIT minimum-information partition.
"""
import numpy as np


def transition(state, evidence, groups, qualities, available, feedback,
               dt=.025, recurrence=True, cut_competition=False, self_gain=1.2, return_gain=.25):
    x = np.asarray(state, dtype=float)
    if x.shape != (14,) or not np.all(np.isfinite(x)):
        raise ValueError('fourteen finite coordinates required')
    if not np.isfinite(dt) or not 0 < dt <= .025:
        raise ValueError('invalid timestep')
    if not all(np.isfinite(gain) and 0 <= gain <= 2 for gain in (self_gain,return_gain)):
        raise ValueError('invalid recurrent gains')
    e, g, z, v, f = map(lambda x: np.asarray(x, dtype=float),
                       (evidence, groups, qualities, available, feedback))
    for value, shape, low, high in ((e,(2,),0,1),(g,(2,3),0,1),
                                   (z,(2,2),-1,1),(v,(2,),0,1),(f,(2,),-1,1)):
        if value.shape != shape or not np.all(np.isfinite(value)) or np.any((value<low)|(value>high)):
            raise ValueError('invalid boundary input')
    if not np.allclose(g.sum(axis=1), 1):
        raise ValueError('normalized grouping targets required')
    a, h = x[:2], x[12:]
    inhibitory = np.zeros(2) if cut_competition else 1.2*a[::-1]
    excitatory = self_gain*a if recurrence else np.zeros(2)
    target = np.clip(2*(v*e + return_gain*f + excitatory-inhibitory-.9*h-.45),0,1)
    derivative = np.concatenate(((target-a)/.5,
                                  (v[:,None]*a[:,None]*(g-x[2:8].reshape(2,3))/.5).ravel(),
                                  (v[:,None]*a[:,None]*(z-x[8:12].reshape(2,2))/.5).ravel(),
                                  (a-h)/8))
    return x + dt*derivative
