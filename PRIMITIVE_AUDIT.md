# Reference-model to circuit obligations

The executable model uses idealized arithmetic corresponding to intended circuit classes. It is **not yet a primitive-qualified implementation**. Its 98 stored scalar coordinates do not establish minimum size, transistor count, physical path count or fit within 10.5 mm². The original block ceilings are constraints, not measurements of this model.

## Functions that must have physical realizations

| Model function | Required implementation or reduction | Missing evidence |
|---|---|---|
| Leaky states, context recurrence, learning retention | Differential integrators, controlled leak/gain, reset and bounded outputs | Extracted dynamics, area, leakage, noise and retention |
| Hypothesis prediction and residuals | Fixed sparse summation, signed subtraction, visibility gating | Real input loading, gains and saturation |
| Precision-weighted residual energy | Squaring, summation, bounded gain and normalization | Noise/error propagation, denominator floor and area |
| Group competition | Minimum/comparison, rectified differences, divisive normalization | Finite settling, offset, tie behavior and interaction with inference |
| Quality population | Four shared bounded smoothstep ramps per quality, adjacent differences forming five units | Matched monotone transfers, nonnegative differences under mismatch, preserved geometry/decisions |
| Observer | Evidence/conflict/prediction products, bounded rational functions and integrators | Calibration, dynamic range and physical cost |
| Representation stability | 13 squared differences per stream (3 grouping, 10 quality), fixed weighted sum, saturation and existing leaky state | Squarer area, offsets, noise bias and threshold calibration; removal of old convergence comparators does not prove an area saving |
| Workspace/source selection | Comparators, Boolean gates, coherent analog selection, fanout | Hazards, offset, tie resolution and break-before-make/coherence behavior |
| Attention forward model | Fixed-gain sums, integrators, saturation and telemetry filtering | Plant/telemetry identification and stability under mismatch |
| Context attractor | Local products and shared inhibitory sum | Basin size under physical error, cue-overwrite behavior and loading |
| Frozen evaluation/learning gates | Controlled analog switches and retained values | Off-state leakage, charge injection and exposure-time accuracy |

Fixed arithmetic constants need gain ratios, not necessarily general dividers. Variable denominators are different: learned precision `0.25/v`, observer `power/(0.1+power)` and `support/(1+conflict+dependence)`, and group normalization require real bounded division or a validated approximation. Quality-population normalization has been removed algebraically.

The revised quality encoder uses 16 shared smoothstep ramps (two streams × two
qualities × four ramps). For each quality, bounded ramps r0..r3 yield
`[1-r0, r0-r1, r1-r2, r2-r3, r3]`. Their sum is identically one; no runtime
division is needed. Each ramp is `u²(3-2u)` for a fixed-offset clipped linear u.
The literal expression has two products per ramp, 32 total rather than the
previous 40 squaring operations, and removes four variable-normalization
networks. These are expression counts, not extracted transistor or area counts.
There are at most two active units, with C1 continuity and ideal decoded error
below 0.049 over [-1,1]. The previous encoder's detailed trajectories need not
be preserved; task, representation and intervention tests must be rerun.

Ramp sharing is local spatial fanout, not time multiplexing. Physical ramps
must preserve ordering and endpoint matching; arbitrary independent offsets
can produce negative differences or excess population activity. A clamp would
break exact normalization and cannot be added without testing. This circuit
qualification remains open despite the algebraic reduction.

## Reduction already justified

Workspace query demand is zero or one-hot for every valid combination of readiness predicates. Suppressing one query preserves this property. The normalization and rectifier originally applied to that vector were redundant and have been removed. `tests/test_query_logic.py` exhaustively checks the actual shared demand function over its Boolean input combinations. This validates the algebraic reduction, not comparator timing or analog hazards.

## Important remaining idealizations

- Python `argmax` and exact thresholds imply instantaneous, offset-free selection. The fixed 0.001 source tie bias is especially sensitive to actual resolution and mismatch; no physical guarantee currently supports it.
- Scalar clipping assumes ideal saturation. Soft limits and recovery can change both control dynamics and intervention results.
- Normalized populations are treated as exact. Real normalization has finite bandwidth and can introduce additional state and feedback.
- Several Boolean readiness paths inspect residuals and many state values simultaneously. Their comparisons, wiring and fanout are not free.
- The two unused second-quality coordinates of the one-object hypotheses have been removed. This eliminates bookkeeping storage, not a measured silicon area. The remaining state organization is not proven minimal.
- Environmental task/cue/reward signals and physical sensing are explicit interfaces, not yet a fully laid-out host-independent fixture.

## Implementation gate

Before claiming a joint agent built from qualified GF180 primitives, lower each equation to a bounded circuit network, enumerate static/dynamic nodes and dedicated paths, and test its finite-bandwidth/offset/saturation model in the same tasks. Then price and extract representative repeated blocks—especially the population encoder, variable-gain/normalization paths and comparators—before extrapolating area. Neither adding a transistor budget label nor counting Python states completes this gate.
