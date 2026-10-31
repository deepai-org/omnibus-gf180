import unittest

from model.evaluate_noise import run_noisy


class NoiseTests(unittest.TestCase):
    def test_seeded_observation_noise_is_reproducible(self):
        a = run_noisy('horizontal', .005, 17)
        self.assertEqual(a, run_noisy('horizontal', .005, 17))
        self.assertTrue(a['correct'])

    def test_invalid_noise_fails(self):
        with self.assertRaises(ValueError):
            run_noisy('horizontal', -.1, 17)

    def test_noisy_negative_answer_and_acquisition_lesion(self):
        result = run_noisy('vertical', .05, 211, quality_sign=-1)
        self.assertTrue(result['correct'])
        self.assertFalse(result['answer'])
        result = run_noisy('horizontal', .02, 307, suppress='inspect')
        self.assertFalse(result['reported'])

    def test_invalid_time_window_fails(self):
        for duration, dt in ((0, .025), (.001, .025), (float('nan'), .025), (1, 0)):
            with self.subTest(duration=duration, dt=dt), self.assertRaises(ValueError):
                run_noisy('horizontal', 0, 17, duration=duration, dt=dt)


if __name__ == '__main__':
    unittest.main()
