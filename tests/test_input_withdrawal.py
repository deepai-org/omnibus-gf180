import unittest
import numpy as np
from model.agent import Agent


class WithdrawalTests(unittest.TestCase):
    def test_actuator_cannot_reopen_withdrawn_input(self):
        a = Agent(source=0)
        a.attention.aperture[:] = 1
        a.desired_inspection[:] = 1
        for _ in range(100):
            result = a.step(np.ones((2,4)),np.ones((2,4)),input_enabled=(0,0))
        np.testing.assert_array_equal(a.sensory.specialists[0].x,np.zeros(4))
        np.testing.assert_array_equal(a.content.activity,np.zeros(2))
        self.assertFalse(result['report_enabled'])

    def test_invalid_input_enable_is_rejected(self):
        a = Agent()
        for enable in ((1,),(-1,1),(1,float('nan')),(2,1)):
            with self.assertRaises(ValueError):
                a.step(np.zeros((2,4)),np.ones((2,4)),input_enabled=enable)
