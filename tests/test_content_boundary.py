import unittest
from experiments.content_boundary import components, graph


class ContentBoundaryTests(unittest.TestCase):
    def test_conditional_payload_has_no_return_path(self):
        blocks = components()
        self.assertIn(['a0','a1','h0','h1'],blocks)
        self.assertEqual(sum(map(len,blocks)),14)
        self.assertEqual(len(blocks),11)
        _, edges = graph()
        self.assertFalse(any(s.startswith(('g','z')) and t.startswith('a') for s,t in edges))
