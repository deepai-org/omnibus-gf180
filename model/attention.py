"""Compressed forward estimate and controller for two four-part apertures.

Eight aperture states are summarized by two estimates. Two slow feedback states
model measurable aperture telemetry. This is a control mechanism candidate,
not a claim that an engineering state observer by itself satisfies AST.
"""

import numpy as np


class Attention:
    state_count = 14

    def __init__(self, dt=.025, actuator_tau=1.0, actuator_gain=1.0):
        if not np.isfinite(dt) or not 0 < dt <= .025:
            raise ValueError('dt must lie in (0, .025]')
        if not np.isfinite(actuator_tau) or actuator_tau < .5:
            raise ValueError('actuator tau must be finite and >= .5')
        if not np.isfinite(actuator_gain) or not .5 <= actuator_gain <= 1.5:
            raise ValueError('actuator gain outside characterized model range')
        self.dt = dt
        self.taus = actuator_tau * np.array([.8, 1, 1.2, 1.4])
        self.gain = actuator_gain
        self.aperture = np.zeros((2, 4))
        self.feedback = np.zeros(2)
        self.estimate = np.zeros(2)
        self.predicted_feedback = np.zeros(2)

    def state_vector(self):
        return np.concatenate((self.aperture.ravel(), self.feedback, self.estimate,
                               self.predicted_feedback))

    def step(self, desired, schema_enabled=True, feedback_enabled=True, direct_feedback=False):
        desired = np.asarray(desired, dtype=float)
        if desired.shape != (2,) or not np.all(np.isfinite(desired)) or np.any((desired < 0) | (desired > 1)):
            raise ValueError('two desired allocations in [0, 1] required')
        # The direct-feedback control uses the same telemetry, gain and bounds;
        # only the estimate-to-controller path is bypassed. Estimator state is
        # retained and evolves to keep the component/state load matched.
        control_state = self.feedback if direct_feedback else self.estimate
        command = np.clip(desired + 4 * (desired - control_state), 0, 1) if schema_enabled else desired
        actual = self.aperture.mean(axis=1)
        # Efference-copy prediction plus innovation from delayed physical telemetry.
        estimate_drive = (command - self.estimate) / 1.1
        if feedback_enabled:
            estimate_drive += 8 * (self.feedback - self.predicted_feedback)
        predicted_feedback_drive = (self.estimate - self.predicted_feedback) / .5
        self.aperture += self.dt / self.taus * (self.gain * command[:, None] - self.aperture)
        self.aperture = np.clip(self.aperture, 0, 1)
        self.feedback += self.dt / .5 * (actual - self.feedback)
        self.estimate = np.clip(self.estimate + self.dt * estimate_drive, 0, 1)
        self.predicted_feedback = np.clip(self.predicted_feedback + self.dt * predicted_feedback_drive, 0, 1)
        return command
