# Instrumentation review decisions

2026-10-25. Incorporated into DESIGN_PLAN.md; no circuit performance or area is yet measured. The first supplied review labels twelve proposals A1–A12 despite its heading saying ten. The first-review table is historical; the second-review decisions below supersede its capture/fixture choices.

| Proposal | Decision |
|---|---|
| A1 simultaneous capture | Adopt 192-channel target/96 fallback with common strobe and two existing outputs. Budget differential hold capacitors, buffers, droop, skew, acquisition and kickback. Does not eliminate uncertainty or capture an entire waveform. |
| A2 clamps and cut | Adopt 32 clampable nodes, four eight-node sets and a declared 96/96 cut. Start exhaustive state acquisition at four nodes; distinguish state-table coverage from full IIT computation and one cut from a minimum partition. |
| A3 passive pickups | Adopt a small coupon/readout allocation with shielded and conducted controls. Reject universal orientation-sign discrimination and zero-cost active readout assumptions. Baseline is coupling measurement, not CEMI compliance. |
| A4 efference copy | Adopt 16 reserved existing edges with independent lesions and action/world counterfactual tests. A copied command predicts consequences; it is not evidence they occurred. |
| A5 same-die controls | Adopt five registered conditions and readback CRC plus host SHA-256 manifest. No extra hash pin. Exact acyclic matching requires graph feasibility; report silence and motor disconnection are different conditions. |
| A6 heterogeneity | Adopt three-bit gain trim and predeclared calibration/heterogeneity conditions. Does not establish a CLT requirement or compensate every mismatch. |
| A7 capacity sweep | Adopt inhibitory-bias sweep; characterize occupancy 0–4 for the existing four candidate assemblies, not a promised 1–6 range. |
| A8 bounded reports | Adopt telemetry with an independently validated behavioral meaning. Predicting a hardwired code from its source state is tautological; compare against controlled actual attention and future consequences instead. |
| A9 internal stimulus | Optional seeded sequencer/LFSR and coarse DAC fixture within the budget. Distinguish clocked internal environment from clock-stopped external-stimulus testing; PRNG is not entropy. |
| A10 adaptation | Adopt disableable adaptation on 40 selected nodes, with target time-scale ratio >=10 and explicit auxiliary-state accounting. No claim that adaptation alone guarantees ignition or criticality. |
| A11 overrun order | Protect capture/clamps and provenance; remove expansion, try lower weight resolution, then 96 captures and simplified optional service before reducing task scope. No unconditional promise that all coupons survive a hard physical limit. |
| A12 paradigms | Adopt masking, sustained conflict and report-silent controls with explicit timing and validation requirements. Biological comparisons remain qualitative unless independently justified. |

Storage is screened at 45% effective utilization, with a 35–60% sensitivity range, not assumed proven at either endpoint. Binary-weighted DACs are candidates: 1+2+4+8 still uses 15 unit widths. Capacitor arithmetic is 192 × 2 pF = 384 pF = 0.000384 µF; kT/C alone is not total circuit noise.

The exact CLT source, mathematical estimator and valence postulate remain unresolved. Neither the supplied review nor this revision establishes satisfaction of CLT, whole-chip IIT or CEMI. Bounded resource regulation is deliberately not a test of genuine existential precarity.

## Second review: timing, structure and identifiability

- **Reject the snapshot-smear premise.** Independent holds freeze all selected channels on the common strobe; later sequential conversion does not follow ongoing node evolution. Readout time matters for droop and frame cadence. The proposed tau/frame rule could be a continuous-trajectory oversampling choice, not a single-snapshot prerequisite. The plan now separates these contracts and corrects the aggregate/per-lane sample-rate arithmetic, with a primary ADC-design source.
- **Adopt 96-channel baseline and baseline deterministic fixture**, but not the assertion that replay is effectively simultaneous. Include all 32 intervention targets in every response capture; local selectors cover other roles. Analog noise and hidden state require ensemble/statistical treatment. Host independence is not the same as stopping the fixture clock.
- **Adopt heterogeneous capacitor candidates.** The proposed 64/88/40 populations sum to 366.4 pF across both sides, not 0.21 mm² of plates: at 2 fF/µm² this is 0.1832 mm². An explicit 16 pF adaptation allowance yields 0.1912 mm². Time constants remain circuit-dependent; slowing adaptation is not automatically easy.
- **Adopt global gain control, attention-command copies and separate monitor inputs.** Hold the gain command fixed and measure actual gain under lesions. Reserve six additional copy edges within the existing edge count. Charge signed residual primitives and gain distribution to real budgets.
- **Reject phased DAGs as a nonrecurrent control.** State retained between phases closes causal loops; arbitrary thirds need not be acyclic. Dynamic gates/current matching are not already provided by static weight latches. A temporal-rewiring experiment can be separately proposed later.
- **Adopt combinatorial test coverage, not a Phi proxy.** Define 72 factorial cells with explicit train/evaluation splits and repetitions; input vocabulary is not measured reachable-state repertoire or integrated information.
- **Adopt explicit graph constraints as engineering controls.** Six designated ring pairs among 15 possible unordered tile pairs, balanced bidirectional allocations, cycle coverage, no tile articulation and role connectivity. These do not establish IIT exclusion.
- **Rank arithmetic by the actual inference equations.** Ratio and log-ratio rank a pure information term equally, but not generally information minus unequal costs. Retain a suitable approximation for the latter or narrow the task/claim. Do not mandate a particular analog multiplier topology by theory name.
- **Adopt endogenous pickup observations and a 32×32 response experiment.** Include nuisance/coupling controls and report uncertainty. Offline loop products remain exploratory, not an identified CLT estimator.
- **Require a bounded four-node IIT-model analysis**, with declared version, quantity, boundary, uncertainty and solver validation. Six-to-eight-node analyses are conditional. Exact computation on an estimated model is not exact physical Phi.
- **Adopt the identifiability table**, but do not claim the table proves a 24-node allocation suffices. The executable model must show that required variables, pathways and interventions actually fit.
- **Do not claim net area savings.** Hold plates shrink, but selection, gain distribution, fixture and copy-path implementation are unpriced. Keep the 9.10 mm² block allocation and 1.40 mm² global overhead/margin until extraction.

No change to the scientific claim boundary, independent electrical safety, or exclusion of genuine-precarity valence experiments.

## Architecture refocus: simultaneous mechanisms first

The subsequent design direction supersedes the generic six-tile/ring organization and four-candidate workspace. Use explicit recurrent predictive specialists, an observer with separate evidence/prediction/error inputs, an attention model distinct from its actuator/controller, and two coherent source/content workspace candidates. All participate in normal operation across one context-selected task family. No disconnected per-theory demonstrations.

State and connection numbers are ceilings, not implementation targets. Derive counts from named equations and memory mechanisms; use fixed arithmetic paths where appropriate while retaining intervention access. Functional placement supersedes ring-balance and three-tile-fanout constraints. Select clamps for model-versus-modeled-state dissociations before optimizing small-IIT subsets. Extract different functional macros rather than extrapolating one generic neuron tile.

The stronger target is simultaneous implementation of explicit primary theory-derived criteria, not an expanded claim that the chip satisfies every version of HOT, IIT, FEP or field theories. Optional field and small-model analysis may not displace the hardware needed for the primary integrated agent.
