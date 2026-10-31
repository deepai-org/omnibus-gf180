from itertools import product
import unittest

import numpy as np
from model.workspace import query_demand


class QueryLogicTests(unittest.TestCase):
    def test_demand_is_zero_or_one_hot_without_normalization(self):
        # Exhaustive Boolean domain, including readiness combinations that the
        # ordinary task may never reach. This proves the removal algebraically
        # at this interface, not the timing behavior of physical comparators.
        for memory, supported, confident, admitted, pending, comparison in product((0, 1), repeat=6):
            evidence = confident and supported and admitted and not pending
            demand = query_demand(memory, supported, evidence, pending, comparison)
            self.assertIn(demand.sum(), (0, 1))
            for suppression in range(4):
                lesioned = demand.copy()
                lesioned[suppression] = 0
                self.assertIn(lesioned.sum(), (0, 1))


if __name__ == '__main__':
    unittest.main()
