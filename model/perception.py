"""A 2x2 scene specialist with explicit recurrent grouping and predictive error.

Input is four spatial samples plus visibility, never the grouping label.
Three generative hypotheses describe horizontal pairs, vertical pairs, or one
object. Each hypothesis has object-quality latents; competition selects the
organization. Grouping activity modulates hypothesis update gain without
turning unobserved predictions into evidence. Integration is explicit Euler.
"""

from dataclasses import dataclass

import numpy as np

from .primitives import normalize_positive, quality_decode, quality_encode, rect


GROUPS = ("horizontal", "vertical", "one_object")
# Pixels are top-left, top-right, bottom-left, bottom-right.
BASIS = np.array([
    [[1, 0], [1, 0], [0, 1], [0, 1]],
    [[1, 0], [0, 1], [1, 0], [0, 1]],
    [[1, 0], [1, 0], [1, 0], [1, 0]],
], dtype=float)


@dataclass(frozen=True)
class PerceptionParameters:
    dt: float = 0.025
    tau_input: float = 0.5
    tau_latent: float = 1.0
    tau_group: float = 1.0
    tau_quality: float = 0.5
    feedback_gain: float = 0.25
    competition_margin: float = 0.025
    complexity_cost: float = 0.04

    def __post_init__(self):
        taus = (self.tau_input, self.tau_latent, self.tau_group, self.tau_quality)
        if self.dt <= 0 or min(taus) <= 0 or self.dt > min(taus) / 8:
            raise ValueError("time step must be positive and <= smallest tau/8")
        if self.competition_margin <= 0 or not 0 <= self.feedback_gain <= 1:
            raise ValueError("invalid competition/feedback parameters")


class Perception:
    """22 persistent real-valued states, plus algebraic circuit signals."""

    state_count = 22

    def __init__(self, parameters=None):
        self.p = parameters or PerceptionParameters()
        self.x = np.zeros(4)
        self.latents = np.zeros(5)
        self.group = np.full(3, 1 / 3)
        self.quality = quality_encode(np.zeros(2))

    def state_vector(self):
        return np.concatenate((self.x, self.latents, self.group, self.quality.ravel()))

    @property
    def z(self):
        """Read-only hypothesis view; one-object hypothesis has only one latent."""
        view = np.append(self.latents, 0.).reshape(3, 2)
        view.flags.writeable = False
        return view

    def set_state(self, state):
        s = np.asarray(state, dtype=float)
        if s.shape != (self.state_count,) or not np.all(np.isfinite(s)):
            raise ValueError("invalid state vector")
        self.x = s[:4].copy()
        self.latents = s[4:9].copy()
        self.group = s[9:12].copy()
        self.quality = s[12:].reshape(2, 5).copy()

    def signals(self, visible, precision=1.0, prior=None):
        mask = np.asarray(visible, dtype=float)
        if mask.shape != (4,) or not np.all(np.isfinite(mask)) or np.any((mask < 0) | (mask > 1)):
            raise ValueError("visibility must contain four values in [0, 1]")
        if not np.isfinite(precision) or not 0 < precision <= 4:
            raise ValueError("precision must lie in (0, 4]")
        prior = np.zeros(3) if prior is None else np.asarray(prior, dtype=float)
        if prior.shape != (3,) or not np.all(np.isfinite(prior)):
            raise ValueError("invalid prior")
        prediction = np.einsum("hij,hj->hi", BASIS, self.z)
        # The observed voltage is aperture-scaled; predictions must pass through
        # the same observation model before comparison. Fractional aperture is
        # a gain, not a declaration that the object's quality became smaller.
        residual = self.x - mask * prediction
        error = mask * residual
        evidence_cost = precision * np.sum(mask * residual ** 2, axis=1) / max(mask.sum(), 1)
        cost = evidence_cost + self.p.complexity_cost * np.array([1, 1, 0]) - prior
        # Comparator/min, subtractors, rectifiers, normalization. No softmax oracle.
        activation = rect(self.p.competition_margin - (cost - np.min(cost)))
        group_target = normalize_positive(activation)
        reconstruction = self.group @ prediction
        # Feedback changes inference rate, not the observations or equilibrium
        # fit. In particular, missing pixels supply no synthetic residual.
        gain = 1 + self.p.feedback_gain * self.group
        latent_drive = np.einsum("hij,hi->hj", BASIS, precision * gain[:, None] * mask * error)
        # Each object latent is driven by two pixels, except the one-object model.
        latent_drive /= np.maximum(BASIS.sum(axis=1), 1)
        z_for_readout = self.z.copy()
        z_for_readout[2, 1] = self.z[2, 0]
        qualities = np.clip(self.group @ z_for_readout, -1, 1)
        return {
            "prediction": prediction, "error": error, "cost": cost,
            "latent_drive": latent_drive, "group_target": group_target,
            "reconstruction": reconstruction, "quality_target": quality_encode(qualities),
        }

    def step(self, samples, visible, precision=1.0, prior=None, feedback=True):
        samples = np.asarray(samples, dtype=float)
        if samples.shape != (4,) or not np.all(np.isfinite(samples)) or np.any(np.abs(samples) > 1):
            raise ValueError("four finite samples in [-1, 1] required")
        signals = self.signals(visible, precision, prior)
        latent_drive = signals["latent_drive"]
        if not feedback:
            latent_drive = np.einsum("hij,hi->hj", BASIS, precision * np.asarray(visible) * signals["error"])
            latent_drive /= np.maximum(BASIS.sum(axis=1), 1)
            signals['latent_drive'] = latent_drive
        # Targets all computed from the same pre-step state, avoiding update-order causality.
        # A missing measurement cannot enter even an otherwise masked state.
        self.x += self.p.dt / self.p.tau_input * (np.asarray(visible) * samples - self.x)
        self.latents = np.clip(self.latents + self.p.dt / self.p.tau_latent * latent_drive.ravel()[:5], -1, 1)
        self.group += self.p.dt / self.p.tau_group * (signals["group_target"] - self.group)
        self.quality += self.p.dt / self.p.tau_quality * (signals["quality_target"] - self.quality)
        return signals

    def result(self):
        return {
            "group": GROUPS[int(np.argmax(self.group))],
            "group_activity": self.group.copy(),
            "qualities": quality_decode(self.quality),
            "population": self.quality.copy(),
        }


def scene(group, first, second):
    """Environment-only generator. Truth labels never enter Perception.step."""
    return BASIS[GROUPS.index(group)] @ np.array([first, second])
