import unittest
from experiments.agent_ignition import run_case


class AgentIgnitionTests(unittest.TestCase):
    def test_identical_preparation_return_cut_shortens_persistence(self):
        intact = run_case(.7,4)
        cut = run_case(.7,4,cut_after=True)
        self.assertEqual(intact['at_removal'],cut['at_removal'])
        self.assertGreater(intact['active_time_after_removal'],
                           cut['active_time_after_removal'])
        self.assertLess(intact['final_activity'],1e-6)
        self.assertLess(cut['final_activity'],1e-6)

    def test_weak_and_zero_inputs_remain_local(self):
        for amplitude in (0,.02):
            row = run_case(amplitude,4)
            self.assertEqual(row['peak'],0)
            self.assertEqual(row['active_time_after_removal'],0)

    def test_strong_longer_pulse_persists_then_releases(self):
        short = run_case(.7,.25)
        long = run_case(.7,4)
        self.assertLess(short['peak'],.7)
        self.assertGreater(long['peak'],.9)
        self.assertGreater(long['active_time_after_removal'],0)
        self.assertLess(long['final_activity'],1e-6)
        self.assertGreater(long['at_removal']['group'][0],.9)
