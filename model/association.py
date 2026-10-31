"""Uploaded context × content → rule weights; no hidden retained state.

Each output is a normalized grouping rule. Retrieval activity is retained in
Workspace.memory, not duplicated here. Weights are immutable trial parameters.
"""
import numpy as np


class Association:
    def __init__(self, weights=None):
        if weights is None:
            weights = np.broadcast_to(np.eye(3)[:, None, :], (3, 3, 3))
        weights = np.asarray(weights, dtype=float)
        if (weights.shape != (3, 3, 3) or not np.all(np.isfinite(weights)) or
                np.any(weights < 0) or not np.allclose(weights.sum(axis=2), 1)):
            raise ValueError('normalized context-by-content association weights required')
        self.weights = weights.copy()
        self.weights.flags.writeable = False

    def retrieve(self, context, content):
        context, content = map(lambda x: np.asarray(x, dtype=float), (context, content))
        for value in (context, content):
            if (value.shape != (3,) or not np.all(np.isfinite(value)) or
                    np.any(value < 0) or not np.isclose(value.sum(), 1)):
                raise ValueError('normalized context and content required')
        return np.einsum('c,g,cgr->r', context, content, self.weights)

    def retrieval_support(self, context, contents, memory):
        """Address-consistency return, distinct from content/rule similarity.

        A valid association may map a scene to a different rule category. Match
        the retained rule to each candidate's addressed rule, not to the scene
        label itself. Empty memory contributes zero; stale retrieval can inhibit.
        This is a stateless alternative return circuit, not answer correctness.
        """
        contents, memory = np.asarray(contents,dtype=float), np.asarray(memory,dtype=float)
        if contents.shape != (2,3):
            raise ValueError('two candidate content populations required')
        if (memory.shape != (3,) or not np.all(np.isfinite(memory)) or
                np.any(memory<0) or memory.sum()>1+1e-12):
            raise ValueError('subnormalized retained rule required')
        addresses = np.stack([self.retrieve(context,c) for c in contents])
        mass = memory.sum()
        return mass-np.sum(np.abs(memory[None,:]-mass*addresses),axis=1)
