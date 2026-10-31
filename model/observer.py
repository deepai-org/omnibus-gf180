"""Content-indexed evidence/prediction monitor, a partial HOT mechanism.

For each stream and grouping hypothesis retain observed support, unobserved
prediction strength and disagreement. These are not a posterior confidence
copy. They are engineering observables, not calibrated reality probabilities.
"""

import numpy as np


class Observer:
    state_count = 18

    def __init__(self, dt=.025, tau=1.):
        if not np.isfinite(dt) or not 0 < dt <= .125:
            raise ValueError('dt must lie in (0, .125]')
        self.dt = dt
        if not np.isfinite(tau) or tau < dt:
            raise ValueError('observer time constant must be finite and >= dt')
        self.tau = float(tau)
        self.evidence = np.zeros((2, 3))
        self.prediction = np.zeros((2, 3))
        self.conflict = np.zeros((2, 3))

    def state_vector(self):
        return np.concatenate((self.evidence.ravel(), self.prediction.ravel(), self.conflict.ravel()))

    def readout(self, groups):
        groups = np.asarray(groups, dtype=float)
        if groups.shape != (2, 3) or not np.all(np.isfinite(groups)) or np.any(groups < 0) or not np.allclose(groups.sum(axis=1), 1):
            raise ValueError('two normalized group populations required')
        support = np.sum(groups * self.evidence, axis=1)
        conflict = np.sum(groups * self.conflict, axis=1)
        dependence = np.sum(groups * self.prediction, axis=1)
        reliability = support / (1 + conflict + dependence)
        return {
            'support': support,
            'prediction_dependence': dependence,
            'conflict': conflict,
            'precision_scale': .5 + .5 * reliability,
            'admitted': reliability > .25,
        }

    def step(self, observed, visibility, predictions):
        x, mask, pred = map(lambda a: np.asarray(a, dtype=float), (observed, visibility, predictions))
        for a, shape in ((x, (2, 4)), (mask, (2, 4)), (pred, (2, 3, 4))):
            if a.shape != shape or not np.all(np.isfinite(a)):
                raise ValueError('invalid observer input')
        if np.any((mask < 0) | (mask > 1)) or np.any(np.abs(x) > 1) or np.any(np.abs(pred) > 1):
            raise ValueError('observer input outside normalized range')
        disagreement = np.sum(mask[:, None, :] * (x[:, None, :] - mask[:, None, :] * pred) ** 2, axis=2)
        disagreement /= np.maximum(mask.sum(axis=1)[:, None], 1)
        conflict = np.clip(disagreement / .25, 0, 1)
        evidence = mask.mean(axis=1)[:, None] * (1 - conflict)
        # Extrapolation on unavailable parts, not spontaneous-activity ground truth.
        power = np.mean((1 - mask[:, None, :]) * pred ** 2, axis=2)
        prediction = power / (.1 + power)
        self.evidence += self.dt/self.tau * (evidence - self.evidence)
        self.prediction += self.dt/self.tau * (prediction - self.prediction)
        self.conflict += self.dt/self.tau * (conflict - self.conflict)
