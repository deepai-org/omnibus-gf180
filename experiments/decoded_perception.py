"""Exact 14-coordinate local readout reduction, NOT whole-agent equivalence.

The ten quality-population coordinates are used linearly by quality_decode.
Their common first-order filter therefore closes exactly on two decoded values:
q' = q + dt/tau * (decode(encode(target)) - q).
The nonlinear encode/decode transfer is preserved, not replaced by identity.
Agent's population-shape stability detector still prevents global substitution.
"""
import numpy as np
from model.perception import Perception,PerceptionParameters
from model.primitives import quality_decode


def project(perception):
    return np.concatenate((perception.x,perception.latents,perception.group,
                           quality_decode(perception.quality)))


def transition(state,samples,visibility,precision=1.,prior=None,parameters=None):
    x=np.asarray(state,dtype=float)
    if x.shape!=(14,) or not np.all(np.isfinite(x)) or np.any(np.abs(x)>1):
        raise ValueError('fourteen bounded finite coordinates required')
    if np.any(x[9:12]<0) or not np.isclose(x[9:12].sum(),1):
        raise ValueError('normalized grouping required')
    a=Perception(parameters or PerceptionParameters())
    a.x[:]=x[:4]
    a.latents[:]=x[4:9]
    a.group[:]=x[9:12]
    # signals and the first twelve updates do not depend on old quality shape.
    signals=a.step(samples,visibility,precision=precision,prior=prior)
    q=x[12:]+a.p.dt/a.p.tau_quality*(quality_decode(signals['quality_target'])-x[12:])
    return np.concatenate((a.x,a.latents,a.group,q))
