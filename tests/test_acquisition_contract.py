import unittest
import numpy as np
from experiments.acquisition_contract import inventory,project,transition
from experiments.reliability_competition import configured
from model.perception import scene


class AcquisitionContractTests(unittest.TestCase):
    def test_inventory_accounts_for_every_retained_coordinate(self):
        names,dynamic,frozen,values=inventory()
        self.assertEqual(len(names),110)
        self.assertEqual(len(dynamic),106)
        self.assertEqual(sorted(dynamic+frozen),list(range(110)))
        np.testing.assert_array_equal(values,[.25,.25,.5,.5])

    def test_reconstruction_matches_live_agent_with_changing_external_inputs(self):
        rng=np.random.default_rng(91)
        a=configured()
        state=project(a)
        for _ in range(200):
            samples=rng.uniform(-1,1,(2,4))
            visibility=rng.uniform(0,1,(2,4))
            enables=rng.integers(0,2,2)
            task=bool(rng.integers(0,2))
            state,result=transition(state,samples,visibility,input_enabled=enables,task_enabled=task)
            actual=a.step(samples,visibility,input_enabled=enables,task_enabled=task)
            np.testing.assert_array_equal(state,project(a))
            self.assertEqual(result,actual)

    def test_changed_learning_background_is_not_silently_dropped(self):
        a=configured()
        a.outcomes.value[0]=.7
        with self.assertRaises(ValueError):
            project(a)

    def test_identical_state_with_changed_dynamics_is_rejected(self):
        mutations=(lambda a:setattr(a,'reliability_selection',False),
                   lambda a:setattr(a.content,'return_gain',.7),
                   lambda a:setattr(a.observer,'tau',2.),
                   lambda a:setattr(a.attention,'gain',.9))
        for mutate in mutations:
            a=configured()
            before=a.state_vector().copy()
            mutate(a)
            np.testing.assert_array_equal(a.state_vector(),before)
            with self.assertRaises(ValueError):
                project(a)

    def test_complete_context_inspection_distractor_trial_runs_through_contract(self):
        state=project(configured())
        for _ in range(600):
            state,_=transition(state,[np.zeros(4),scene('horizontal',.73,-.61)],
                               [[0]*4,[1]*4],input_enabled=(0,1),task_enabled=False)
        for _ in range(80):
            state,_=transition(state,np.zeros((2,4)),np.zeros((2,4)),
                               input_enabled=(0,0),task_enabled=False)
        for _ in range(1600):
            state,result=transition(state,[[0,.7,-.7,0],[.7,-.7,-.7,.7]],
                                    [[1,0,0,1],[1]*4])
            if result['report_enabled']:
                break
        self.assertTrue(result['report_enabled'])
        self.assertTrue(result['yes'])
        self.assertEqual(result['source'],0)
