# Source-bound IIT rerun

**Historical after inspection-deadlock fix:** `model/agent.py` has changed since
these files were generated. Their hashes intentionally remain unchanged. Do not
treat them as computations on the corrected revision; see ../../STATUS.md.

This sweep supersedes the historical numbers in CAUSAL_MODEL_STATUS.md.
All 374 defined analyses return system φₛ=0; 1,034 attempts are undefined,
not zero. This does not demonstrate a positive integrated candidate.

Each JSON file contains all nominal continuous/binary transition tables,
per-state/subset analyses, dependency matrices, sensitivity statistics, solver
revision, and SHA256 hashes of every `model/*.py` file. Check hashes before
treating results as current. These include uncommitted source contents.

Regenerate each of the four combinations with the pinned environment:

```sh
PYPHI_WELCOME_OFF=1 .venv-iit/bin/python -m model.iit --candidate distributed --phase early --output evidence/iit/distributed-early.json
```

Candidates: `distributed`, `attention`. Phases: `early`, `inspection`.
`--output` replaces the specified file. Dependency setup and boundary limitations
are described in ../../CAUSAL_MODEL_STATUS.md.

`early` is a historical identifier for fixed step 200, **not chronologically
earlier than inspection in this revision**. The event-defined inspection
checkpoint now occurs at step 136. Its query/aperture activities are recorded.
Intervention levels, bins, intervals and candidate definitions remain unchanged.
All 16 states and 11 multi-coordinate subsets are attempted at each interval.

All defined φₛ values are zero; sensitivity counts below are changed rows /16.

| Candidate / checkpoint | Interval | Defined analyses | Background changes | Within-bin changes |
|---|---:|---:|---:|---:|
| Distributed / fixed | 0.5 | 88 | 0 | 12 |
| Distributed / fixed | 2 | 22 | 16 | 2 |
| Distributed / inspection | 0.5 | 88 | 0 | 10 |
| Distributed / inspection | 2 | 22 | 16 | 8 |
| Attention / fixed | 0.5 | 44 | 0 | 8 |
| Attention / fixed | 2 | 11 | 0 | 0 |
| Attention / inspection | 0.5 | 88 | 3 | 8 |
| Attention / inspection | 2 | 11 | 0 | 0 |

An unchanged binary table need not imply continuous independence. The fixed
distributed candidate moves by up to 0.34885 at interval 0.5 under its omitted
background-state perturbation, and by 0.73514 at interval 2.

These are conditional finite-horizon reductions of the actual agent, not
validated autonomous causal substrates. They do not establish whole-agent zero
integration, structure Φ or exclusion/maximality. The next substantive step is
to justify a boundary and intervention distribution that preserve the actual
loop and pass closure tests, not to search for favorable scores or add arbitrary
noise. Physical stochastic dynamics also remain unqualified.
