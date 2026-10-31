"""Evidence-dependent query competition, not a service-clock stage machine.

This component is deliberately small. It does not yet implement the complete
workspace broadcast, attention schema, or higher-order observer. Inputs must
come from specialist states; the environment never supplies a correct answer.
"""

import numpy as np

from .primitives import quality_decode


QUERIES = ('retrieve', 'inspect', 'compare', 'answer')


def query_demand(memory, supported, evidence, pending, comparison):
    return np.array([
        1 - memory,
        memory * float(pending or (supported and not evidence)),
        memory * evidence * (1 - comparison),
        memory * evidence * comparison,
    ])


class Workspace:
    # Query activity (4), retrieved grouping rule (3), answer evidence (2).
    state_count = 9

    def __init__(self, dt=.025):
        if not np.isfinite(dt) or not 0 < dt <= .0625:
            raise ValueError('dt must lie in (0, .0625]')
        self.dt = dt
        self.query = np.array([1., 0., 0., 0.])
        self.memory = np.zeros(3)
        self.comparison = np.zeros(2)

    def state_vector(self):
        return np.concatenate((self.query, self.memory, self.comparison))

    def step(self, grouping, population, stored_rule, suppress=None, supported=True,
             inspection_complete=True, admitted=True, enabled=True,
             acquisition_requested=False):
        grouping = np.asarray(grouping, dtype=float)
        population = np.asarray(population, dtype=float)
        rule = np.asarray(stored_rule, dtype=float)
        for value, shape in ((grouping, (3,)), (population, (2, 5)), (rule, (3,))):
            if value.shape != shape or not np.all(np.isfinite(value)) or np.any(value < 0):
                raise ValueError('finite nonnegative specialist activities required')
        if not np.isclose(grouping.sum(), 1) or not np.isclose(rule.sum(), 1):
            raise ValueError('group and stored rule must be normalized')
        if not np.allclose(population.sum(axis=1), 1):
            raise ValueError('quality populations must be normalized')

        if not enabled:
            # External task availability gates retrieval/reporting, not internal
            # query order. Context memory itself remains powered and recurrent.
            self.query += self.dt / .5 * (np.array([1., 0., 0., 0.]) - self.query)
            self.memory -= self.dt * self.memory
            self.comparison -= self.dt * self.comparison
            return {'query': None, 'inspect': 0., 'report_enabled': False, 'yes': False}

        # Comparator thresholds are circuit parameters, not a hidden stage index.
        memory_ready = float(self.memory.sum() >= .9 and
                             np.max(np.abs(self.memory-rule)) < .1)
        pending_inspection = self.query[1] > .1 and not inspection_complete
        evidence_ready = float(np.max(grouping) >= .85 and supported and admitted and not pending_inspection)
        match = float(grouping @ self.memory)
        quality = float(quality_decode(population)[0])
        positive = np.clip(.5 + quality / .4, 0, 1)
        yes = np.clip(match * positive, 0, 1)
        answer_target = np.array([yes, 1 - yes])
        # Previously acquired evidence must not authorize a stale decision.
        comparison_ready = float(self.comparison.sum() >= .9 and
                                 np.max(np.abs(self.comparison - answer_target)) < .1)
        # Missing evidence may recruit an acquisition before inference settles.
        # This request cannot authorize comparison or reporting.
        demand = query_demand(memory_ready, supported or acquisition_requested,
                              evidence_ready, pending_inspection, comparison_ready)
        if suppress is not None:
            demand[QUERIES.index(suppress)] = 0
        # Readiness predicates make these demands mutually exclusive. A divider
        # or analog normalization loop would add cost without changing the result.
        target = demand

        # Concrete task: does the scene match the remembered grouping rule AND
        # is its first object's quality positive? Geometry affects the decision.
        old_query = self.query.copy()
        self.query += self.dt / .5 * (target - self.query)
        self.memory += self.dt * old_query[0] * (rule - self.memory)
        self.comparison += self.dt * (old_query[2] + old_query[3]) * (answer_target - self.comparison)
        return {
            'query': QUERIES[int(np.argmax(self.query))] if self.query.max() > .5 else None,
            'inspect': float(self.query[1]),
            'report_enabled': bool(self.query[3] > .9 and memory_ready and evidence_ready and comparison_ready),
            'yes': bool(self.comparison[0] > self.comparison[1]),
        }
