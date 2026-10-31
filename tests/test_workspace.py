import unittest

import numpy as np

from model.primitives import quality_encode
from model.workspace import Workspace


def run_component(ambiguous=False, quality=.7, rule=(1, 0, 0), suppress=None):
    workspace = Workspace()
    queries = []
    revealed = not ambiguous
    result = None
    for _ in range(1200):
        # Minimal action-dependent fixture: requesting inspection reveals evidence.
        if workspace.query[1] > .9:
            revealed = True
        grouping = [1, 0, 0] if revealed else [.5, .5, 0]
        result = workspace.step(grouping, quality_encode([quality, -.7]), rule, suppress)
        if result['query'] and (not queries or queries[-1] != result['query']):
            queries.append(result['query'])
        if result['report_enabled']:
            break
    return workspace, queries, result


class WorkspaceTests(unittest.TestCase):
    def test_acquisition_does_not_require_or_imply_answer_readiness(self):
        w = Workspace()
        for _ in range(400):
            result = w.step([.5, .5, 0], quality_encode([.7, -.7]), [1, 0, 0],
                            supported=False, acquisition_requested=True,
                            inspection_complete=False)
        self.assertEqual(result['query'], 'inspect')
        self.assertFalse(result['report_enabled'])
        self.assertLess(w.comparison.sum(), .01)

    def test_evidence_changes_recruitment_sequence(self):
        _, clear, result = run_component()
        self.assertEqual(clear, ['retrieve', 'compare', 'answer'])
        self.assertTrue(result['report_enabled'])
        _, ambiguous, result = run_component(ambiguous=True)
        self.assertEqual(ambiguous, ['retrieve', 'inspect', 'compare', 'answer'])
        self.assertTrue(result['report_enabled'])

    def test_memory_and_population_both_control_answer(self):
        self.assertTrue(run_component(quality=.63)[2]['yes'])
        self.assertFalse(run_component(quality=-.63)[2]['yes'])
        self.assertFalse(run_component(rule=(0, 1, 0))[2]['yes'])

    def test_query_lesions_prevent_missing_computation(self):
        for query in ['retrieve', 'compare']:
            self.assertFalse(run_component(suppress=query)[2]['report_enabled'])
        self.assertFalse(run_component(ambiguous=True, suppress='inspect')[2]['report_enabled'])

    def test_ambiguous_evidence_never_answers_without_reveal(self):
        w = Workspace()
        for _ in range(1200):
            result = w.step([.5, .5, 0], quality_encode([.7, -.7]), [1, 0, 0])
        self.assertFalse(result['report_enabled'])
        self.assertEqual(result['query'], 'inspect')
        self.assertEqual(w.state_vector().shape, (9,))


if __name__ == '__main__':
    unittest.main()
