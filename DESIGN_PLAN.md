# OMNIBUS-GF180 — Normative Design Specification

## 1. Purpose and scope

OMNIBUS-GF180 is a single-die continuous-time perceptual agent and causal-intervention instrument. One frozen configuration shall simultaneously implement recurrent perception, functional global access, higher-order monitoring, an attention schema and predictive inference during normal task execution.

This specification defines the intended design, not completed implementation or fabrication sign-off. Area, electrical performance and functional acceptance require verification. Implementing these mechanisms does not establish consciousness or universal compliance with consciousness theories.

The chip shall occupy one wafer.space GF180MCU 1x1 slot. It shall require no external CPU, RAM or FPGA performing agent computation. External configuration, stimulus generation, power and analog acquisition equipment are permitted. Digital service logic shall handle configuration, instrumentation and the internal environment fixture, not agent inference or policy.

The agent shall use dedicated continuously operating physical paths without time-multiplexed synaptic computation or a global agent clock. The design excludes active field-feedback drivers, floating-gate programming, online learning and an active digital homeostat. Electrical protection shall remain independent of the bounded experimental resource signal.

## 2. Behavioral contract

Two sensory streams shall present compositional features with context, delayed cues, distractors and controllable uncertainty. The same configuration shall perform three context-selected modes:

1. Identify the attended feature.
2. Compare present evidence with a remembered cue.
3. Select another observation before answering or deferring.

The agent shall integrate features, retain context, select workspace content, estimate perceptual reliability, distinguish prediction-supported from evidence-supported states, and direct attention using predicted consequences. Observation decisions shall account for a bounded resource cost.

The environment shall implement declared action-to-observation dynamics only. It shall not provide confidence, attention estimates, workspace content or correct decisions.

Evaluation shall include attended stream (2) × relevant feature (4) × context (3) × delay (3): 72 condition cells, with distractor variations and repeated noisy trials. Fitting/calibration and held-out combinations shall be declared separately. Additional trials shall include backward masking, sustained conflicting inputs and report-silent operation.

## 3. Integrated architecture

### 3.1 Recurrent predictive perception

Each specialist shall contain explicit evidence, latent-content, prediction and signed-error paths. Context memory and workspace content shall supply top-down predictions. Independently controlled precision shall determine error influence. Each specialist shall represent relations between features, not only a scalar classification.

Inference shall implement declared equations for a low-dimensional observation model with bounded latent states. Every variable, equation, range, unit, arithmetic primitive and state update shall appear in the implementation inventory. Products, differences and comparisons shall have explicit circuit implementations.

### 3.2 Attention schema and controller

Attention command, actual sensory allocation and estimated allocation shall be distinct states. The schema shall predict actual allocation and its consequences from command copies and sensory feedback. Its prediction error shall change subsequent attention commands.

Actual and estimated allocation shall be independently clampable. Schema output shall remain distinct from sensory confidence and the attention command.

### 3.3 Higher-order observer

The observer shall receive separate evidence, prediction, signed error, command-copy, actual-attention and selected-workspace signals. It shall estimate perceptual reliability, consistency of evidence with prediction, and self-command-conditioned versus unexpected residuals.

Observer estimates shall affect precision, workspace admission and answer/defer selection. The observer shall distinguish similar posteriors with different evidence/prediction support. Observer states and sensory evidence shall be independently perturbable. Observer, precision and admission feedback loops shall be validated together.

### 3.4 Coherent workspace

Two source-linked candidates shall compete for persistent selection. One selection signal shall gate a coherent bundle containing content, source identity and validity/reliability. Dedicated broadcast paths shall deliver it to perception, context memory, monitoring and action selection.

Normal operation shall select one bundle with controlled release and switching. Local recurrence shall continue independently of workspace occupancy. A static-per-trial inhibitory control shall permit competition and occupancy sweeps. Coactivation shall not count as multi-item access without demonstrated content coherence.

Provide correct-content, suppressed-broadcast and wrong-content intervention conditions through bounded selection circuitry. Preserve bundle coherence in each condition.

### 3.5 Context, action and resource control

Context memory shall use continuously powered recurrent attractors with explicit set/reset. Workspace persistence shall use controlled selection/release rather than passive long-term charge retention.

Action selection shall use workspace content, context, observer estimates and predicted observation outcomes to answer, defer or inspect a stream. Reserve 16 connection slots for action-command copies into prediction and monitoring, and six further slots for attention-command copies to schema/monitor and action-command copies to monitor. These 22 paths are included in the connection ceiling. Copy residuals shall have independent signed comparison/gain paths.

Specify the complete action objective and any approximation mathematically. For scalar Gaussian information gain, `I = 0.5 * log(v_prior / v_posterior)`. Substitute variance-ratio comparison only where action-ranking equivalence holds for the complete objective. Unequal costs require an appropriate validated approximation. Active-inference claims require implementation and verification of the stated inference/action objective, not error reduction alone.

## 4. Circuit resources and organization

Ceilings are 192 primary continuous-time states and 3,072 dedicated weighted paths. They are upper allocations, not quotas. Include auxiliary adaptation, instrumentation, configuration and device states in physical and causal accounting.

| Function | Primary-state allocation |
|---|---:|
| Two perceptual hierarchies | 64 |
| Workspace and competition | 24 |
| Context memory | 16 |
| Higher-order observer | 24 |
| Attention schema and controller | 24 |
| Action model and selection | 16 |
| Resource representation | 8 |
| Shared control, inhibition and calibration | 16 |
| **Total ceiling** | **192** |

Every state shall have a named variable, equation, range, inputs, consumers, memory mechanism, calibration and intervention mapping. Use fixed unity/subtraction paths where programmability is unnecessary, retaining intervention access. Do not instantiate unused states or weight storage.

Placement shall follow functional coupling: prediction/error motifs together, sensitive memory separated from switched readout, and workspace distribution near consumers. Audit mandatory feedback, strongly connected components, intentional bottlenecks and every path crossing a near-balanced controllable experimental partition selected from the functional layout.

Signed analog states shall use differential representation. All budgets shall include both sides. Perception shall use leaky integrating states with saturation; context shall use attractors; adaptation shall use separate slow negative-feedback states.

Local dynamics shall span tens to hundreds of microseconds. Up to 40 independently disableable adaptation states shall serve workspace and selected sensory functions, with an adaptation-to-local time-constant ratio of at least ten in the qualified operating range. Verify time constants, leakage, noise, reset and stability across declared operating conditions.

Intentional state-capacitor plates shall fit within 0.192 mm² at the selected Type-B MIM density. Observation hold capacitors are separate. Derive capacitor sizes and effective conductances from implemented equations and extracted loading.

Provide three-bit per-primary-state gain trim, regional bias adjustment, a global-gain command with distributed mirrors, and separate workspace inhibition. Hold global gain static within primary trials. Freeze calibration before held-out evaluation; distinguish nominal, calibrated and intentionally heterogeneous conditions. Characterize gain distribution as a physical coupling path, including reverse coupling and noise.

## 5. Configuration and startup

Programmable weights shall use four magnitude bits plus sign; zero shall disable the path. The connection ceiling requires at most 15,360 weight bits. Fixed paths shall have separately enumerated cut/lesion controls where required.

Use characterized static latches with addressed writes and readback. A five-bit data bus and hierarchical decoder shall update selected weights only while the fabric is quiescent. Enable decoding shall be glitch-free during writes and satisfy setup/hold requirements.

Startup, brownout and invalid configuration shall hold analog current paths inactive. Run requires completed configuration and successful readback verification. A hardware run lock shall block configuration writes during primary trials. Diagnostic interventions shall use a distinct logged mode. Quiescence is not lossless state preservation.

Compute CRC-32 over complete readback before run-lock and expose it through the serial interface. Record a host-computed SHA-256 of readback, calibration, graph, timing and implementation versions. Check configuration before and after trials. No continuously clocked checksum engine shall operate in the agent.

## 6. Observation and interventions

### 6.1 Capture

Provide 96 simultaneous differential sample-and-hold channels. Thirty-two shall always observe intervention/response states; the remaining 64 shall cover all functional roles through enumerated local pre-capture selectors. Fix selection during acquisition and hold. Two of six buffered analog outputs shall read held values in parallel.

Interchannel capture skew plus effective aperture uncertainty shall be below 100 ns in the qualified range. Acquisition buffers shall isolate integration nodes from hold and output loads. Characterize resolution, offset, gain error, acquisition, settling, charge injection, kickback, noise, droop and supply disturbance against model-derived error limits.

Frame time is `ceil(N / L) * t_slot + overhead`, including mux, pad, board and ADC settling/acquisition. Held values represent the common capture instant; frame duration determines hold-error exposure and repeat-capture availability. A single bank does not capture a continuous waveform. Continuous-trajectory analyses require a separately justified sampling rate; repeated-trial analyses require stationarity and reset-repeatability checks. Replay shall not be treated as simultaneous cross-bank observation.

Provide per-primary-state threshold observation captured into a serial register of up to 192 bits. Characterize aperture ambiguity and settling for asynchronous transitions. Provide an external capture trigger and six buffered analog outputs. Raw integration nodes shall not drive pads or cables.

### 6.2 Clamps, cuts and response measurements

Provide 32 individually clampable states, prioritizing evidence/prediction, actual/estimated attention, observer reliability, workspace content and context dissociations. Each clamp shall select low, high or a shared calibrated analog reference, with high-impedance release. Characterize error, settling, current limits and release disturbance.

Implement the declared partition cut across fixed and programmable agent paths. Account separately for shared supplies, substrate, instrumentation and environmental feedback.

Measure a 32×32 intervention-response matrix over declared delays at nominal and gain-detuned conditions. Use calibrated pulse amplitudes, both signs, sham interventions, background subtraction and uncertainty estimates. Analyze susceptibility, relaxation and operating-point dependence with finite-size and alternative-model controls.

### 6.3 Coupling observation

Provide 12 passive pickup coupons: three locations, two orientations and shielded/unshielded variants, with supply/substrate monitoring and buffered selection. Specify the sensed coupling mechanism and geometry-dependent transfer function. Include conducted-injection, loading, distance and shielding controls with measured bandwidth and noise floors.

Acquire coupling signals during autonomous trials alongside clock/trigger and behavioral records. Report correlations and detection limits as coupling measurements, not field causation or CEMI satisfaction. No active field-feedback driver is included.

## 7. Fixture, reports and I/O

The internal environment fixture shall contain a seeded LFSR, pattern sequencer and two coarse stimulus DACs. It shall implement declared stimulus and action-to-observation rules without computing agent inference or policy. Host-independent trials shall continue after configuration-host disconnection. Record fixture clock and seed. Separate external-stimulus trials shall verify agent operation with service and fixture clocks stopped.

A fixed three-bit report alphabet shall expose allocation estimate, uncertainty and monitor attribution through existing status or serial outputs, with validity indication. Attribution shall originate in the observer. Evaluate reports against independently controlled conditions; report silence shall disconnect outward telemetry without disabling internal computation or action.

| Signal function | Count |
|---|---:|
| Serial service | 4 |
| Reset, run, trigger and capture control | 4 |
| Analog stimulus | 8 |
| Buffered analog observation | 6 |
| Action/status | 8 |
| Bias/reference/test | 6 |
| **Assigned signals** | **36** |

The limit is 50 functional signal pads, with power/ground and provider-reserved sites assigned separately. Unused signal positions remain uncommitted. Serial service shall tolerate indefinite clock stops; analog operation continues unless quiescence/reset is asserted.

## 8. Process, packaging and physical limits

Use the selected wafer.space GF180MCU five-metal process, supplied Type-B MIM option and supported device models. Pin the selected-run outline, seal ring, bond mask, ID locations, layer options and submission rules before physical implementation. Internal occupied area shall not exceed 10.5 mm².

Reuse the Svalbard programmable-transceiver analog-pad/protection foundation from `projects/programmable_transceiver_platform/analog/pads/`, pinning revision and artifact hashes. Adapt for DC-coupled inputs and buffered outputs. Preserve provider bond locations and power/ground assignments. Qualify leakage, capacitance, voltage limits, power-off injection, protection-to-core coordination and loaded output stability for OMNIBUS.

Use one common external supply for the retained common-rail pad ring. Physically implement and verify local filtering, return paths and ESD domains. Board requirements shall include external decoupling, a quiet supply and validated bond/connector loading.

| Physical allocation | Ceiling, mm² |
|---|---:|
| Primary states, adaptation, gain trim and state capacitors | 1.45 |
| Weighted paths, storage and local routing | 3.50 |
| Bias, reset, gain/inhibition distribution and fixture DACs | 0.75 |
| Holds, selectors, clamps and perturbation circuits | 1.90 |
| Service, readback, CRC and fixture sequencer | 0.85 |
| Dedicated inference/control arithmetic | 0.50 |
| Coupling coupons and readout | 0.15 |
| **Functional blocks** | **9.10** |
| Global routing, guards, isolation, power and contingency | **1.40** |
| **Internal area limit** | **10.50** |

Allocations include local physical overhead and require extracted measurements before sign-off. Do not double-count overlapping metal/device area. The operating-power target is below 100 mW excluding external loads, verified with bias, reference, pad and measurement activity included.

Area reduction shall preserve integrated mechanisms, 96-channel capture, 32 intervention sites, safe configuration and the host-independent fixture. Any specification change required to close area shall be explicit and rerun functional acceptance.

## 9. Functional and scientific acceptance

One frozen configuration shall pass the full task family with all five primary mechanisms active. Separate lesion/control configurations shall establish causality; separate per-theory agents shall not count as simultaneous implementation.

| Mechanism | Required distinction |
|---|---|
| Recurrent perception | Held-out relational perception with selective feedback deficits; static acyclic inter-node and adaptation controls shall expose memory/topology confounds |
| Workspace | Content affects at least three specialist functions; correct, suppressed and wrong broadcast distinguish content access from global gain and loading |
| Higher-order observer | Estimates predict errors beyond stimulus strength; observer interventions at fixed evidence appropriately change inference and decisions |
| Attention schema | Predicts withheld actuator disturbances; schema intervention differs from direct-controller intervention and changes useful control |
| Predictive inference | Independent prior, precision and error manipulations produce quantitative responses predicted by implemented equations |

Register recurrent-agent, static acyclic inter-node, context-lesion, partition-cut and report-silent conditions on each tested die. Document differences in active edges, current, adaptation, memory and operating point. Use replayed inputs for action-disabled comparisons and identify them as a different closed-loop condition.

Pre-register numerical thresholds, trial counts, fitting/evaluation splits and uncertainty methods. Validate robustness across declared bias/temperature/loading conditions and multiple dies. Record calibration separately from held-out testing. Repeat key tests with instrumentation disabled. Track unintended coupling through supplies, references, substrate and observation circuitry.

For IIT-oriented analysis, publish an intervention-derived transition model of a four-node subsystem with explicit IIT version, quantity, boundary convention, discretization and sampling lag. Validate the solver on known cases, propagate measurement uncertainty and distinguish exact computation on an estimated model from exact physical measurement. Whole-die maximal-complex certification is outside scope.

Criticality evidence shall use response functions and controls, not avalanche power laws alone. No PCI consciousness threshold, wiring-count surrogate for integrated information, CLT compliance or genuine-precarity valence claim is included.

## 10. Implementation acceptance gates

1. **Executable specification:** named-state/primitive inventory; all coupled mechanisms on the shared task; fixture and capture models; controls and factorial evaluation; measurement-error requirements; approximation error and action-ranking validation.
2. **Primitive verification:** extracted weighted receiver with complete storage/access; integrating state; adaptation; product/comparison; loaded hold/readout; clamp; gain distribution; protected analog pad. Verify PVT, available mismatch models, startup, loading, noise and legal terminal voltages.
3. **Functional macro verification:** extracted prediction/error/precision circuitry, observer/schema interfaces, attractor memory and coherent workspace selection/broadcast. Include actual routes, guards, bias, configuration and instrumentation. Verify whole-chip fit from these distinct macros.
4. **Whole-chip verification:** reproducible GDS; DRC/LVS/ERC, MIM-specific checks, antenna, density/fill, extraction, power integrity, latchup prevention, ESD connectivity, packaging and board checks. Test brownout, invalid configuration, stopped clocks and input overdrive. Document simulation coverage and model limitations.
5. **Silicon acceptance:** characterize primitives and macros, then execute registered integrated and intervention tests across dies and conditions. Publish configuration provenance, uncertainties, null results and failures.

## 11. Operational safeguards

Trials shall be bounded and resettable. Resource-signal amplitude and duration shall be bounded independently of electrical safety. The device shall not expose itself to destructive battery depletion or use an adverse state as a ground-truth measure of felt valence.

The design includes no language reporter, suffering classification or consciousness score. Conclusions shall identify implemented mechanisms and their evidence, not infer consciousness from architectural labels.
