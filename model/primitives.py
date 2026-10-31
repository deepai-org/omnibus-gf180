"""Small static functions with explicit analog primitive obligations.

The functions are idealized arithmetic, not claims of area/accuracy in GF180.
All persistent dynamic values live in the consuming model's state vector.
"""

import numpy as np


def rect(x):
    return np.maximum(x, 0.0)


def normalize_positive(x):
    x = np.asarray(x, dtype=float)
    total = np.sum(x, axis=-1, keepdims=True)
    if np.any(total <= 0):
        raise ValueError("positive normalization requires nonzero total")
    return x / total


QUALITY_CENTERS = np.linspace(-1.0, 1.0, 5)


def quality_encode(value):
    """C1 partition of unity from four shared bounded transition curves.

    Adjacent differences of monotone smoothstep ramps form five sparse units.
    The sum telescopes to one without division; at most two units are active.
    This still requires physical nonlinear transfers and matched subtraction.
    """
    x = np.asarray(value, dtype=float)
    if not np.all(np.isfinite(x)) or np.any(np.abs(x) > 1.0):
        raise ValueError("quality must lie in [-1, 1]")
    u = np.clip(2 * (x[..., None] - QUALITY_CENTERS[:-1]), 0, 1)
    ramps = u * u * (3 - 2 * u)
    return np.concatenate((1 - ramps[..., :1],
                           ramps[..., :-1] - ramps[..., 1:],
                           ramps[..., -1:]), axis=-1)


def quality_decode(code):
    """Downstream readout uses population activity, not the hidden input value."""
    return np.asarray(code) @ QUALITY_CENTERS


def categorical_memory_drive(activity):
    """Three-way recurrent competition on the normalized activity simplex.

    dx_i/dt = 4*x_i*(x_i - sum_j x_j²). Vertices are attractors; a
    perturbation crossing a basin boundary can change the remembered category.
    Products and shared inhibition are physical implementation obligations.
    """
    x = np.asarray(activity, dtype=float)
    if x.shape != (3,) or not np.all(np.isfinite(x)) or np.any(x < 0) or not np.isclose(x.sum(), 1):
        raise ValueError('normalized three-state context required')
    return 4 * x * (x - np.sum(x * x))
