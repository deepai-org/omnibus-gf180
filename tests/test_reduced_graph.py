import unittest
import numpy as np
from experiments.reduced_graph import analyze
from experiments.reduced_persistence import project,transition
from experiments.return_replay import configured
from experiments.context_ambiguity import association_weights


class ReducedGraphTests(unittest.TestCase):
    def test_uploaded_content_dependence_really_closes_selection_memory_path(self):
        a = configured()
        a.content.group[:] = [[1,0,0],[0,1,0]]
        a.workspace.memory[:] = [1,0,0]
        a.rule[:] = [1,0,0]
        a.workspace.query[0] = .5
        x = project(a)
        x[:2] = [.8,.2]
        y = x.copy()
        y[:2] = [.2,.8]
        for weights,dependent in ((None,False),(association_weights(),True)):
            left = transition(x,forced_source=None,weights=weights)
            right = transition(y,forced_source=None,weights=weights)
            changed = np.max(np.abs(left[26:29]-right[26:29]))>0
            self.assertEqual(changed,dependent)
            self.assertEqual(bool(left[32]!=right[32]),dependent)

    def test_population_preserving_recurrent_components(self):
        default = analyze(False)
        self.assertEqual(default['coordinates'],35)
        loops = [c for c in default['components'] if len(c['blocks'])>1]
        self.assertEqual(sorted(c['coordinates'] for c in loops),[4,10])
        coupled = analyze(True)
        loops = [c for c in coupled['components'] if len(c['blocks'])>1]
        self.assertEqual(len(loops),1)
        self.assertEqual(loops[0]['coordinates'],14)
        self.assertIn('memory',loops[0]['blocks'])
        self.assertIn('local0',loops[0]['blocks'])
