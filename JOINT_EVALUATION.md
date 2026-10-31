# Joint-agent composition evaluation

Reproduce:

```sh
python3 -m model.evaluate
```

The current 98-state model passes **72/72 cases**, produces a report in all cases, and has no grouping or answer failures. Maximum first-report time is 14.150 normalized units at dt=0.025 with the divider-free smoothstep quality population, accumulated representation stability, independent missing-evidence acquisition, grouping-dependent update gain and the aperture-consistent observation model. These are software-model results, not measured chip behavior.

## Fixed conditions and scoring

The Cartesian grid contains three scene organizations × three remembered grouping rules × two quality signs × two visibility conditions × two forced source selections. Each case uses the same circuit/update parameters. Only task data and the declared source intervention change. Every trial starts with the same learned values; outcome learning is frozen.

The tested object's qualities are `sign*0.43` and `-sign*0.87`. The nonselected stream presents a vertical distractor with qualities -0.67 and 0.51. Visibility is either complete or diagonal-only until agent inspection opens the missing inputs. These magnitudes differ from the principal integration examples; they were not fitted separately for individual cases.

The correct answer is yes only when the perceived organization matches the remembered rule and the first object's quality is positive. A case passes only if the agent emits a report, the inferred organization is correct, **and** the answer is correct. Correct negative answers alone cannot conceal wrong grouping. The timeout is 40 normalized units. Report timing and query traces are available through `run_case`; the CLI prints aggregate outcomes and full failure records.

## What coexists in these runs

- Both recurrent scene specialists and their sparse quality populations.
- Evidence-dependent workspace retrieval, inspection, comparison and report queries.
- Content-bound evidence/prediction monitoring that affects precision and admission.
- The forward attention estimator/controller and its physical aperture model.
- Persistent learning state, frozen for this evaluation rather than refitted per condition.

This is joint operation of implemented components, not proof that each component is necessary for success. Component/intervention tests provide separate, limited causal evidence.

## Coverage boundaries

This grid is **not** the design plan's 72-cell stream/feature/context/delay task battery. Identical counts do not make them equivalent. It does not test context retention after cue removal, varying delays, action-cost/preferences, spontaneous activity, noisy inputs, analog mismatch, complete HOT attribution, all GWT broadcast consumers, or field-mediated computation.

Source selection is forced in this grid to exercise each stream independently. The separate outcome-learning tests exercise adaptive source selection, reversal and frozen evaluation; they do not turn this grid into an adaptive-choice result. The observer/controller mechanisms remain imperfect and the matched attention-control sweep retains adverse cases. IIT integration and CLT Phi are not inferred from behavioral success.

## Correlated observation-noise stress test

Reproduce with `python3 -m model.evaluate_noise`. The environment adds stationary
Ornstein–Uhlenbeck observation noise before aperture attenuation, with correlation
time 0.5 normalized units. This is a declared synthetic input disturbance, not
a GF180 noise estimate or intrinsic state noise. The model receives no true scene
labels, noise amplitude, or noise realization. Circuit parameters remain fixed.

Each amplitude uses three organizations, two seeds (17, 83), diagonal initial
visibility, qualities 0.73 and -0.61, matching remembered rule, forced source zero,
and a 40-unit timeout at dt=0.025. Outcome learning is frozen. Both streams show
the same scene; this test does not establish distractor rejection.

| Stationary input σ | Reports / trials | Correct reports | Correct final grouping |
|---|---:|---:|---:|
| 0 | 6/6 | 6/6 | 6/6 |
| 0.005 | 6/6 | 6/6 | 6/6 |
| 0.02 | 6/6 | 6/6 | 6/6 |
| 0.05 | 6/6 | 6/6 | 6/6 |

The previous instantaneous convergence gate exposed a design failure, not successful uncertainty management.
At σ=0.02, correct perceptual grouping does not reach a report: the convergence
support remains below its 0.9 admission threshold at timeout in every case.
Its target requires instantaneous input tracking, latent drive, grouping and
quality residuals all below 0.02. Persistent noise makes this near-stationarity
criterion inappropriate as a general readiness rule. Initially the same support
signal prevented inspection recruitment: at σ=0.05 two vertical scenes remained
misgrouped as horizontal. The revised agent independently requests acquisition
when grouping confidence is below 0.85 and any actual input aperture is below
0.95. This uses available aperture signals, not fixture truth or noise amplitude.
It restores correct final grouping in all six high-noise cases, but does not
restore reports. Acquisition does not bypass evidence or observer admission.

The current revision integrates bounded grouping/quality population drift in
the same two retained support states (equation in model/README.md), restoring
reports in all 24 cases above. Independent observer admission and stale-answer
rejection remain in force. The intermediate acquisition-only revision restored
grouping but still produced no reports at the two higher noise levels. No
fixture noise amplitude enters readiness, and thresholds are not refitted per
condition. Squaring circuitry replaces parts of the old comparison logic;
unchanged state count is not unchanged physical area. These 24 development
trials are not a held-out robustness qualification. A separate limited
scene-change test follows; broader nonstationary behavior, near-decision
boundaries, intrinsic state noise and mismatch remain unqualified.

## Continuous scene revision

`python3 -m model.evaluate_switch` first presents a horizontal scene with a
positive first quality for 20 normalized units, then changes either quality
sign or spatial grouping for 25 units. There is no reset, change notification,
parameter update or report-triggered stage change inside the agent. Both input
streams are fully visible and identical; source zero is forced and learning
frozen. Noise uses the same OU process as above, with seed 419 and a continuous
noise trajectory across the change.

| Change | Input σ | Old report withdrawn | First correct new report |
|---|---:|---:|---:|
| Quality sign | 0 | 0.250 | 12.200 |
| Horizontal → vertical | 0 | 0.325 | 11.050 |
| Quality sign | 0.05 | 0.225 | 15.350 |
| Horizontal → vertical | 0.05 | 0.325 | 13.000 |

Times are relative to the external scene change, in normalized model units.
All four cases start with a correct positive report and end with the correct
negative report and grouping. No incorrect report occurs **after withdrawal**.
The old positive report persists during the initial sensing/inference delay;
the design does not promise instantaneous knowledge of external changes.
Tests require withdrawal within one unit and a revised report within 20 units.
These are regression limits for these fixtures, not universal latency bounds.
This extends the component-level changed-bundle test to the complete sensory
path. Near-boundary changes, masked changes, endogenous source switching and
arbitrary continuous environments remain unqualified.

The divider-free quality encoder preserves correctness but changes dynamics.
Compared with the prior normalized-quartic encoder, maximum clean report time
increases from 13.600 to 14.150. In the noisy sign-change run, the correct report
withdraws again at 16.975 and returns at 19.225; in the noisy grouping-change run
it withdraws at 16.850 and returns at 19.750. Neither emits an incorrect answer
after initial withdrawal, but stable uninterrupted reporting is not demonstrated.
This is an explicit behavioral cost of the current arithmetic simplification,
not evidence of a measured area/performance win on silicon.
