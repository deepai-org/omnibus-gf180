import unittest
from experiments.cross_stream import run_case


class CrossStreamTests(unittest.TestCase):
    def test_same_object_different_remembered_context_changes_answer(self):
        answers = []
        for context in ('horizontal', 'vertical'):
            row = run_case(context, 'horizontal', 1)
            self.assertTrue(row['correct'], row)
            self.assertEqual(row['cue_group'], context)
            self.assertEqual(row['local_group'], 'horizontal')
            self.assertTrue(row['inspected'])
            answers.append(row['answer'])
        self.assertEqual(answers, [True, False])

    def test_context_path_lesion_preserves_cue_perception_but_loses_answer(self):
        row = run_case('horizontal', 'horizontal', 1, 'context')
        self.assertFalse(row['correct'], row)
        self.assertEqual(row['cue_group'], 'horizontal')

    def test_inspection_is_needed_for_ambiguous_object(self):
        row = run_case('horizontal', 'horizontal', 1, 'inspection')
        self.assertFalse(row['report'], row)

