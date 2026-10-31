import unittest
import numpy as np
from functools import partial
from experiments.decoded_agent import configured,project
from experiments.decoded_stability import configured as full_configured
from experiments.acquisition_partition import evaluate,prepared,advance
from experiments.bidirectional_replay import record,partitioned,PARTITIONS


class DecodedPartitionTests(unittest.TestCase):
    def test_reduced_acquisition_partitions_match_nominal_and_block_transmission(self):
        rows=evaluate(factory=configured)
        for row in rows:
            self.assertEqual(row['nominal_max_error'],0)
            self.assertEqual(row['cut_other_side_change'],0)
            self.assertGreater(row['live_other_side_change'],0)

    def test_reduction_commutes_with_declared_two_way_cuts(self):
        full=prepared(full_configured)
        reduced=configured()
        reduced.set_state(project(full))
        full_step=partial(advance,factory=full_configured)
        reduced_step=partial(advance,factory=configured)
        full_ref=record(full.state_vector(),30,full_step)
        reduced_ref=record(reduced.state_vector(),30,reduced_step)
        full.content.group[0]=full.content.group[0][[1,0,2]]
        reduced.set_state(project(full))
        for prefixes in PARTITIONS.values():
            full_mask=np.array([n.startswith(prefixes) for n in full.state_names()])
            reduced_mask=np.array([n.startswith(prefixes) for n in reduced.state_names()])
            full_cut=partitioned(full.state_vector(),full_ref,full_mask,full_step)
            reduced_cut=partitioned(reduced.state_vector(),reduced_ref,reduced_mask,reduced_step)
            reader=full_configured()
            for f,r in zip(full_cut,reduced_cut):
                reader.set_state(f)
                np.testing.assert_allclose(project(reader),r,atol=1e-12,rtol=0)
