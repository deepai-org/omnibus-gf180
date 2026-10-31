"""Population-preserving finite intervention scheme, NOT a validated TPM.

Eight units retain activity, adaptation, both local groupings, retrieved memory
and retrieval drive (14 continuous coordinates). Remaining reduced state is an
explicit supplied background, never silently discarded. Two realization profiles
permit within-category sensitivity checks. No trajectory is quantized/reset by
these helpers; they apply only at the declared intervention instant.
"""
import numpy as np

NAMES = ('a0','a1','h0','h1','local0','local1','memory','retrieve')
ALPHABETS = (2,2,2,2,4,4,4,2)
# Population labels 0/1/2 = H/V/G; 3 = unresolved. Memory also requires mass.
SCALARS = (0,1,2,3,32)


def encode(state):
    x = np.asarray(state,dtype=float)
    if x.shape != (35,) or not np.all(np.isfinite(x)):
        raise ValueError('35 finite reduced coordinates required')
    bits = [int(x[i]>=.5) for i in SCALARS[:4]]
    for start in (14,17,26):
        p = x[start:start+3]
        mass = p.sum()
        label = int(np.argmax(p)) if mass>=.5 and p.max()>.5*mass else 3
        bits.append(label)
    return tuple(bits+[int(x[32]>=.5)])


def realize(labels,background,profile='far'):
    if len(labels)!=8 or any(not isinstance(v,(int,np.integer)) or not 0<=v<n
                             for v,n in zip(labels,ALPHABETS)):
        raise ValueError('valid eight-unit mixed-alphabet state required')
    if profile not in ('far','near'):
        raise ValueError('unknown realization profile')
    x = np.array(background,dtype=float,copy=True)
    if x.shape != (35,) or not np.all(np.isfinite(x)):
        raise ValueError('explicit finite 35-coordinate background required')
    low,high,peak = (.1,.9,.8) if profile=='far' else (.4,.6,.6)
    for index,label in zip(SCALARS,(*labels[:4],labels[7])):
        x[index] = high if label else low
    for start,label in zip((14,17,26),labels[4:7]):
        p = np.full(3,1/3)
        if label<3:
            p[:] = (1-peak)/2
            p[label] = peak
        elif start==26:
            # Two explicitly different unresolved-memory realizations.
            p *= .1 if profile=='far' else .4
        x[start:start+3] = p
    return x
