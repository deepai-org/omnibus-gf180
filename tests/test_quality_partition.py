import unittest
import numpy as np
from model.primitives import QUALITY_CENTERS, quality_decode, quality_encode


class QualityPartitionTests(unittest.TestCase):
    def test_partition_sparse_monotone_and_bounded_decode_error(self):
        x = np.linspace(-1, 1, 10001)
        code = quality_encode(x)
        self.assertTrue(np.all(code >= 0))
        np.testing.assert_allclose(code.sum(axis=1), 1, atol=1e-15)
        self.assertLessEqual(np.max(np.count_nonzero(code > 1e-12, axis=1)), 2)
        decoded = quality_decode(code)
        self.assertTrue(np.all(np.diff(decoded) >= 0))
        self.assertLess(np.max(np.abs(decoded - x)), .049)

    def test_centers_and_continuous_first_derivative(self):
        np.testing.assert_allclose(quality_encode(QUALITY_CENTERS), np.eye(5))
        h = 1e-6
        for x in QUALITY_CENTERS[1:-1]:
            left = (quality_encode(x) - quality_encode(x-h)) / h
            right = (quality_encode(x+h) - quality_encode(x)) / h
            np.testing.assert_allclose(left, right, atol=3e-5)
