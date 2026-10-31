"""Two bounded, persistent sensory-error estimates, not a gain homeostat.

Feedback must be a physically available measurement-minus-reference residual.
This component does not supply a reference oracle or solve credit assignment.
No update occurs without an explicit feedback-valid gate. Static synaptic
weights remain unchanged; the learned state controls sensory precision.
"""

import numpy as np

from .perception import Perception, PerceptionParameters


class Reliability:
    state_count = 2
    minimum = 0.0625
    maximum = 4.0
    reference_variance = 0.25

    def __init__(self, tau=20.0):
        if not np.isfinite(tau) or tau <= 0:
            raise ValueError("positive finite learning time required")
        self.tau = tau
        self.variance = np.full(2, self.reference_variance)

    @property
    def precision(self):
        return np.clip(self.reference_variance / self.variance, 0.0625, 4.0)

    def step(self, residual, valid, dt):
        error = np.asarray(residual, dtype=float)
        gate = np.asarray(valid, dtype=float)
        if error.shape != (2,) or gate.shape != (2,):
            raise ValueError("two residuals and two validity gates required")
        if not np.all(np.isfinite(error)) or np.any(np.abs(error) > 2):
            raise ValueError("residuals must be finite and within [-2, 2]")
        if not np.all(np.isfinite(gate)) or np.any((gate < 0) | (gate > 1)):
            raise ValueError("validity gates must lie in [0, 1]")
        if not np.isfinite(dt) or not 0 < dt <= self.tau / 8:
            raise ValueError("learning timestep must be within (0, tau/8]")
        target = np.clip(error * error, self.minimum, self.maximum)
        self.variance += dt / self.tau * gate * (target - self.variance)


class AdaptiveSpecialists:
    """Two scene circuits plus two learned states: 46 dynamic states total.

    Trial reset clears scene beliefs, never learned reliability. Feedback is
    applied after the scene update, so no same-step outcome look-ahead exists.
    This is a component assembly, not yet the full autonomous agent.
    """

    state_count = 46

    def __init__(self, parameters=None):
        self.p = parameters or PerceptionParameters()
        self.reliability = Reliability()
        self.reset_trial()

    def reset_trial(self):
        self.specialists = [Perception(self.p), Perception(self.p)]

    def step(self, samples, visibility, residual=(0, 0), valid=(0, 0), precision_scale=(1, 1), priors=None):
        if np.shape(samples) != (2, 4) or np.shape(visibility) != (2, 4):
            raise ValueError("two spatial scenes required")
        scale = np.asarray(precision_scale, dtype=float)
        if scale.shape != (2,) or not np.all(np.isfinite(scale)) or np.any((scale <= 0) | (scale > 1)):
            raise ValueError('two precision scales in (0, 1] required')
        precision = self.reliability.precision * scale
        priors = np.zeros((2, 3)) if priors is None else np.asarray(priors, dtype=float)
        if priors.shape != (2, 3) or not np.all(np.isfinite(priors)):
            raise ValueError('two finite grouping priors required')
        result = [s.step(x, mask, precision=float(p), prior=prior) for s, x, mask, p, prior in
                  zip(self.specialists, samples, visibility, precision, priors)]
        self.reliability.step(residual, valid, self.p.dt)
        return result

    def state_vector(self):
        return np.concatenate([s.state_vector() for s in self.specialists] +
                              [self.reliability.variance.copy()])


class OutcomeLearning:
    """Two retained source-value estimates; distinct from sensory variance.

    Reward is an explicit external consequence signal, not a scene-label input.
    Update exposure is measured in time; repeated feedback is not a free event.
    """
    state_count = 2

    def __init__(self):
        self.value = np.full(2, .5)

    def step(self, reward, owner, valid, dt):
        if not np.isfinite(reward) or not 0 <= reward <= 1 or owner not in (0, 1):
            raise ValueError('bounded reward and valid source required')
        if not np.isfinite(dt) or not 0 < dt <= 1:
            raise ValueError('invalid learning timestep')
        if valid:
            self.value[owner] += dt / 20 * (reward - self.value[owner])
