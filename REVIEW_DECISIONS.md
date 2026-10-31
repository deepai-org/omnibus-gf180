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

## Regional regulation and action-objective review

This section records reasoning; DESIGN_PLAN.md retains only current normative requirements.

| Proposal | Disposition |
|---|---|
| A1 regional servo | Adopt eight bounded analog regional controllers from the 40-state auxiliary pool, leaving up to 32 adaptation states. Use heterogeneous fixed setpoints, explicit negative feedback and fixed-bias controls. This regulates activity, not automatically criticality. The full loop is part of the causal system. Neither regionality nor a global scalar alone determines irreducibility. |
| A2 loop audit | Adopt graph/cycle coverage reporting and gain-response sweeps. Reject a guarantee that 32 sites cover every short cycle twice: self-loops, disjoint cycles and functional clamp requirements can make it impossible. Products of closed-loop impulse responses at selected delays are not dimensionless open-loop gains; convolution, phase, normalization and coupled modes matter. Fiedler/min-cut metrics are descriptive, with directed-graph conventions stated, not IIT irreducibility certificates. |
| A3 staggered capture | Reject. Four groups capture different state subsets at different times; they do not create four samples per state or evade one-bank readout/reacquisition limits. The proposal also needs independent strobe control. Keep the common simultaneous aperture and accurately report sampling limits. |
| B1–B3 dissociations | Adopt local-versus-global broadcast lesions, bidirectional sweeps, and schema/controller comparisons at matched first-order performance. Hysteresis is an implementation hypothesis, not a universal GWT falsifier. Schema compression concerns represented variables and omitted mechanism details, not a mandated ratio of controller/node counts. |
| B4 recursion | Allocate four observer states to reliability of its own estimates, with a specified discrepancy input and downstream influence. Preserve content/source binding and independent first-/higher-order interventions. This is useful metacognitive circuitry, not a claim that all HOT theories require a third-order observer. |
| C field injection | Adopt a passive external-instrument loop and two protected pads, with full protection/loading and conducted/thermal controls. No on-chip driver. Null results bound this coupling experiment; they do not strengthen IIT/CLT by elimination. |
| D action objective | Adopt explicit expected information gain, expected log outcome preference and observation cost. Do not identify the review's information-minus-KL combination with expected free energy without a derivation: outcome entropy can be counted differently. Use two variances and one covariance with positive-definiteness checks, determinant-based Gaussian approximation and validated action ranking. Pure information seeking can itself arise as a preference-free active-inference special case; adding preferences broadens the task rather than automatically certifying FEP. |
| E heterogeneity/dither | Specify characterized gain-trim patterns and logged seeded dither through existing intervention paths. Do not promise exact ±5% capacitor changes without switchable capacitor hardware, area and resolution. Dither does not guarantee escape from collapse and may disrupt the agent. |
| F fit | Do not accept estimated +0.18 mm² as evidence. Allocate +0.20 mm² across bias/arithmetic/coupling, leaving 1.20 mm² global overhead/margin. All paths and donor states must be counted; identical state ceilings do not imply unchanged circuitry. |
| G topology/calibration | Require existing functional feedback and per-die calibration frozen across conditions. Do not require instrumentation or every support block to be bidirectionally bound, or infer IIT exclusion merely from block encapsulation. Predeclared interventions are not per-condition calibration. |
| H scope/data | Publish actual acquired data, matrices, calibration and structured models. Keep predeclared four-node selection, at least two lags, and estimation uncertainty. No exhaustive 192-node transition-table promise; 96 simultaneous channels and repeated stimuli cannot identify an unrestricted whole-chip stochastic model. Small-system IIT is meaningful within its declared formalism; no arbitrary 192-state lower bound is assumed. |

AST evidence remains a limited functional implementation without language behavior. A holdout-corpus qualia-talk experiment is not treated as a universal necessary AST acceptance test. Selecting the maximum integration proxy over many subsystems after seeing the same data would require selection-bias controls and held-out confirmation; the design instead uses a predeclared functional/observability rule.

Sources consulted for these distinctions:

- [Active inference, Bayesian optimal design, and expected utility](https://arxiv.org/abs/2110.04074): epistemic and preference-based value, including the preference-free special case.
- [Active inference and epistemic value](https://chrismathys.com/wp-content/uploads/2015/05/Friston-et-al.-2015-Active-inference-and-epistemic-value.pdf): expected information gain and expected log preference decomposition.
- [The attention schema theory: a mechanistic account of subjective awareness](https://pmc.ncbi.nlm.nih.gov/articles/PMC4407481/): simplified internal modeling of attention and its use, not a prescribed state-count ratio.
- [Cortical circuit dynamics are homeostatically tuned to criticality in vivo](https://pmc.ncbi.nlm.nih.gov/articles/PMC6934140/): circuit-dependent homeostatic/criticality mechanisms; not a qualification of our scalar analog servo.
- [IIT 4.0](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011465): intrinsic causal analysis rather than graph cuts or an assumed neuron-count threshold.
