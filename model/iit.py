"""IIT 4.0 (2023) system-phi calculations on explicitly conditional models.

No whole-agent or physical-complex claim. Requires requirements-iit.txt.
Run: PYPHI_WELCOME_OFF=1 .venv-iit/bin/python -m model.iit
"""

from itertools import product, combinations
from importlib.metadata import distribution
import json
from hashlib import sha256
from pathlib import Path

import numpy as np

from .causal import boundary_screen


FORMALISM = 'IIT_4_0_2023'
REVISION = '134a8f31b49db512322465ed3ba5da7194d362fd'


def source_provenance():
    """Bind generated evidence to source contents, including uncommitted work."""
    return {path.name: sha256(path.read_bytes()).hexdigest()
            for path in sorted(Path(__file__).parent.glob('*.py'))}


def candidate_subsets(n):
    """All multi-coordinate subsets; no favorable-score subset selection."""
    return tuple(subset for size in range(2, n + 1) for subset in combinations(range(n), size))


def transition_array(rows):
    """Convert explicit bit tuples to PyPhi's little-endian state-row order."""
    n = len(rows[0]['initial'])
    if len(rows) != 2 ** n:
        raise ValueError('complete binary intervention table required')
    tpm = np.empty((2 ** n, n))
    seen = set()
    for row in rows:
        bits, output = tuple(row['initial']), tuple(row['final_binary'])
        if len(bits) != n or len(output) != n or any(x not in (0, 1) for x in bits + output):
            raise ValueError('invalid binary row')
        index = sum(bit << i for i, bit in enumerate(bits))
        if index in seen:
            raise ValueError('duplicate initial state')
        seen.add(index)
        tpm[index] = output
    return tpm


def deterministic_dependencies(tpm):
    """Bit-intervention dependencies in the surrogate, not a Phi estimator."""
    tpm = np.asarray(tpm)
    n = tpm.shape[1]
    if tpm.shape != (2 ** n, n) or not np.all((tpm == 0) | (tpm == 1)):
        raise ValueError('complete deterministic binary TPM required')
    dependencies = np.zeros((n, n), dtype=int)
    for source in range(n):
        for state in range(2 ** n):
            dependencies[source] |= (tpm[state] != tpm[state ^ (1 << source)])
    return dependencies


def reference_checks(pyphi):
    # These are solver/interface sanity checks, not stand-ins for the agent.
    independent = pyphi.Substrate(np.array([[0, 0], [1, 0], [0, 1], [1, 1]], dtype=float))
    swap = pyphi.Substrate(np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float))
    results = {}
    for name, substrate in [('independent_identity', independent), ('bidirectional_swap', swap)]:
        result = pyphi.analyze(substrate, (0, 0), formalism=FORMALISM, compute='sia', parallel=False, progress=False)
        results[name] = float(result.phi)
    if not np.isclose(results['independent_identity'], 0) or not np.isclose(results['bidirectional_swap'], 2):
        raise RuntimeError('IIT 2023 reference sanity check failed')
    return results


def analyze(candidate='distributed', phase='early'):
    import pyphi
    provenance = json.loads(distribution('pyphi').read_text('direct_url.json') or '{}')
    if provenance.get('vcs_info', {}).get('commit_id') != REVISION:
        raise RuntimeError('Install the exact solver revision in requirements-iit.txt')
    result = dict(formalism=FORMALISM, pyphi_version=pyphi.__version__, requested_revision=REVISION,
                  model_source_sha256=source_provenance(),
                  quantity='system integrated information phi_s; not structure Phi',
                  reference_checks=reference_checks(pyphi), conditional_models=[])
    screen = boundary_screen(candidate, phase)
    result['candidate'] = candidate
    result['phase'] = phase
    result['checkpoint_step'] = screen['checkpoint_step']
    result['checkpoint_inspect_query'] = screen['checkpoint_inspect_query']
    result['checkpoint_aperture'] = screen['checkpoint_aperture']
    result['coordinates'] = screen['names']
    result['background_intervention'] = screen['background_intervention']
    for report in screen['reports']:
        tpm = transition_array(report['nominal_table'])
        substrate = pyphi.Substrate(tpm)
        analyses = []
        for state in product((0, 1), repeat=4):
            for subset in candidate_subsets(4):
                try:
                    sia = pyphi.analyze(substrate, state, subset=subset, formalism=FORMALISM,
                                        compute='sia', parallel=False, progress=False)
                except pyphi.exceptions.StateUnreachableForwardsError:
                    analyses.append(dict(state=state, subset=subset, phi_s=None,
                                         status='unreachable: no defined analysis'))
                else:
                    analyses.append(dict(state=state, subset=subset, phi_s=float(sia.phi), status='computed'))
        result['conditional_models'].append(dict(duration=report['duration'], analyses=analyses,
            nominal_transition_table=report['nominal_table'],
            deterministic_dependencies=deterministic_dependencies(tpm).tolist(),
            background_sensitivity=report['background_sensitivity'], within_bin_sensitivity=report['within_bin_sensitivity']))
    return result


if __name__ == '__main__':
    import argparse
    from .causal import CANDIDATES
    parser = argparse.ArgumentParser()
    parser.add_argument('--candidate', choices=CANDIDATES, default='distributed')
    parser.add_argument('--phase', choices=('early', 'inspection'), default='early')
    parser.add_argument('--output', type=Path, help='Save complete provenance-bound JSON evidence')
    args = parser.parse_args()
    result = analyze(args.candidate, args.phase)
    encoded = json.dumps(result, indent=2) + '\n'
    if args.output:
        args.output.write_text(encoded)
        print(args.output)
    else:
        print(encoded, end='')
