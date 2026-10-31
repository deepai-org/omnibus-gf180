"""Named uploaded configurations: joint demonstrator and historical comparator.

Experiments may change stimuli, initial state and declared interventions, but
must not silently choose different weights/source overrides for each result.
"""
import numpy as np
from .agent import Agent


def association_weights():
    context = np.broadcast_to(np.eye(3)[:,None,:],(3,3,3))
    content = np.broadcast_to(np.eye(3)[None,:,:],(3,3,3))
    return .85*context+.15*content


def configured(dt=.025):
    """Historical comparison configuration; not the latest joint demonstrator."""
    return Agent(rule=(1/3,1/3,1/3),context_source=1,context_prior_gain=.04,
                 association_weights=association_weights(),dt=dt)


def joint_configured(dt=.025):
    """One fixed configuration for the joint task and its causal controls."""
    return Agent(rule=(1/3,1/3,1/3),context_source=1,context_prior_gain=.04,
                 association_weights=association_weights(),dt=dt,
                 reliability_selection=True)
