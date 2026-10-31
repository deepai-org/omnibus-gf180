import unittest
from itertools import product
import numpy as np
from experiments.population_alphabet import ALPHABETS,encode,realize
from experiments.reduced_persistence import project,lift
from model.configuration import configured


class PopulationAlphabetTests(unittest.TestCase):
    def test_all_2048_states_have_valid_round_trip_realizations(self):
        background = project(configured())
        count = 0
        for labels in product(*(range(n) for n in ALPHABETS)):
            for profile in ('far','near'):
                state = realize(labels,background,profile)
                self.assertEqual(encode(state),labels)
                a = lift(state,configured())
                a.set_state(a.state_vector())
                np.testing.assert_allclose(project(a),state,atol=1e-15,rtol=0)
            count += 1
        self.assertEqual(count,2048)
