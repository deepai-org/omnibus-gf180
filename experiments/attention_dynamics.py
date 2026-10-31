"""Explicit continuous-state, input-conditioned model of one real agent loop.

No binning, hidden background-state averaging, or IIT score. The endogenous
desired command is an explicitly supplied boundary input, not inferred truth.
"""
import numpy as np

NAMES = ('aperture0', 'aperture1', 'aperture2', 'aperture3',
         'telemetry', 'estimate', 'predicted_telemetry')


def drive(state, desired, gain=1., tau=1.):
    x = np.asarray(state, dtype=float)
    if x.shape != (7,) or not np.all(np.isfinite(x)) or np.any((x < 0) | (x > 1)):
        raise ValueError('seven finite bounded states required')
    if not np.isfinite(desired) or not 0 <= desired <= 1:
        raise ValueError('explicit desired command in [0,1] required')
    if not np.isfinite(gain) or not .5 <= gain <= 1.5 or not np.isfinite(tau) or tau < .5:
        raise ValueError('parameters outside reference-model domain')
    a, f, e, p = x[:4], x[4], x[5], x[6]
    command = np.clip(5*desired - 4*e, 0, 1)
    return np.concatenate(((gain*command-a)/(tau*np.array([.8, 1, 1.2, 1.4])),
                           [(np.mean(a)-f)/.5,
                            (command-e)/1.1 + 8*(f-p), (e-p)/.5]))


def step(state, desired, dt=.025, gain=1., tau=1.):
    if not np.isfinite(dt) or not 0 < dt <= .025:
        raise ValueError('dt outside reference-model domain')
    return np.clip(np.asarray(state) + dt*drive(state, desired, gain, tau), 0, 1)


def read_stream(attention, stream=0):
    return np.concatenate((attention.aperture[stream],
                           [attention.feedback[stream], attention.estimate[stream],
                            attention.predicted_feedback[stream]]))


def write_stream(attention, state, stream=0):
    # Validate before mutation. This is an intervention, not a state inference.
    drive(state, .5)
    attention.aperture[stream] = state[:4]
    attention.feedback[stream], attention.estimate[stream], attention.predicted_feedback[stream] = state[4:]
