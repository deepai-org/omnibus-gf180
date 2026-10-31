"""Content-bearing recurrent workspace candidate used by Agent.

Fourteen retained states, with explicit specialist inputs. Do not mistake this
component's tests for collective ignition or a whole-agent IIT result.
"""
import numpy as np


class ContentWorkspace:
    state_count = 14

    def __init__(self, dt=.025, self_gain=1.2, return_gain=.25, activity_tau=.5):
        if not np.isfinite(dt) or not 0 < dt <= .025:
            raise ValueError('dt must be in (0,.025]')
        self.dt = dt
        if not np.isfinite(activity_tau) or activity_tau < dt:
            raise ValueError('activity time constant must be finite and >= dt')
        self.activity_tau = float(activity_tau)
        if not all(np.isfinite(v) and 0 <= v <= 2 for v in (self_gain, return_gain)):
            raise ValueError('recurrent gains must lie in [0,2]')
        self.self_gain, self.return_gain = float(self_gain), float(return_gain)
        self.activity = np.zeros(2)
        self.group = np.full((2, 3), 1/3)
        self.quality = np.zeros((2, 2))
        self.adaptation = np.zeros(2)

    def state_vector(self):
        return np.concatenate((self.activity, self.group.ravel(), self.quality.ravel(), self.adaptation))

    def set_state(self, state):
        """Atomic checkpoint/intervention; grouping interventions stay on-simplex."""
        state = np.asarray(state, dtype=float)
        if state.shape != (14,) or not np.all(np.isfinite(state)):
            raise ValueError('fourteen finite coordinates required')
        low = np.zeros(14)
        low[8:12] = -1
        if np.any(state < low) or np.any(state > 1):
            raise ValueError('state outside physical encoding range')
        groups = state[2:8].reshape(2, 3)
        if not np.allclose(groups.sum(axis=1), 1):
            raise ValueError('grouping interventions must preserve normalization')
        self.activity[:] = state[:2]
        self.group[:] = groups
        self.quality[:] = state[8:12].reshape(2, 2)
        self.adaptation[:] = state[12:]

    def step(self, evidence, groups, qualities, available, feedback=(0, 0), recurrence=True):
        evidence, groups, qualities, available, feedback = map(
            lambda x: np.asarray(x, dtype=float), (evidence, groups, qualities, available, feedback))
        for value, shape, low, high in ((evidence, (2,), 0, 1), (groups, (2,3), 0, 1),
                                      (qualities, (2,2), -1, 1), (available, (2,), 0, 1),
                                      (feedback, (2,), -1, 1)):
            if value.shape != shape or not np.all(np.isfinite(value)) or np.any((value < low)|(value > high)):
                raise ValueError('invalid specialist input')
        if not np.allclose(groups.sum(axis=1), 1):
            raise ValueError('normalized grouping populations required')
        old = self.activity.copy()
        excitation = self.self_gain*old if recurrence else np.zeros(2)
        target = np.clip(2*(evidence*available + self.return_gain*feedback + excitation
                            -1.2*old[::-1] - .9*self.adaptation - .45), 0, 1)
        # All right-hand sides use pre-step values. No hidden timer or latch.
        self.activity += self.dt/self.activity_tau*(target-old)
        acquire = available*old
        self.group += self.dt/.5*acquire[:,None]*(groups-self.group)
        self.quality += self.dt/.5*acquire[:,None]*(qualities-self.quality)
        self.adaptation += self.dt/8*(old-self.adaptation)

    def bundle(self):
        source = int(np.argmax(self.activity))
        other = 1-source
        valid = self.activity[source] > .7 and self.activity[source]-self.activity[other] > .2
        return dict(source=source, valid=bool(valid), group=self.group[source].copy(),
                    quality=self.quality[source].copy(), activity=float(self.activity[source]))
