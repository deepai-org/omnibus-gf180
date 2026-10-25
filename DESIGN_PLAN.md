# OMNIBUS-GF180: one-die multi-theory experimental agent

Date: 2026-10-25. Status: pre-schematic research architecture.

## 1. Objective and claim boundary

Build one wafer.space GF180MCU 1x1 die that performs a small but meaningful perceptual-control task using physically instantiated recurrent perception, global access, higher-order monitoring, an attention model, and predictive control together.

Optimize for the number of **substantive, independently testable mechanisms that operate concurrently**, not the number of theory names attached to blocks. No claim that this device is conscious, that all variants of a theory are satisfied, or that a minimum size for consciousness is known.

The principal deliverable is a causal-intervention laboratory with a working autonomous agent. A collection of disconnected demonstration circuits does not meet the objective.

The baseline is 192 continuous-time state nodes and 3,072 dedicated directed weighted edges. There is no 256-node expansion in this tapeout plan: measurement and intervention take priority over node count. These are engineering allocations, not scientific thresholds. Functional feasibility must precede schematic commitment. Failure to fit or function is a result to report, not a reason to relabel a simpler mechanism as compliant.

## 2. Physical envelope and exclusions

- One GF180MCU wafer.space 1x1 slot; historical KianV reference: approximately 20.14 mm² gross and 12.90 mm² internal core. These are reference measurements, not a current shuttle guarantee.
- Use the published Run 1 envelope, 3.88 × 5.07 mm (19.67 mm²), as the conservative planning reference [8], not a guarantee for a future shuttle. Provisional internal floorplan budget: 10.5 mm². Freeze exact outline, padframe, metal stack, capacitor option, voltage domains, package and submission rules before replicating tiles. A 0.55 mm border would leave about 11.04 mm²; this is a sensitivity calculation, not a padframe design.
- At most 50 functional signal pads; power and ground allocation must be checked separately against the actual package.
- No external RAM, FPGA, or host computation is required for the agent's inference, attention, monitoring, workspace, or action selection.
- External laboratory stimulus generation, ADC acquisition, power supply, configuration host, and a simple physical environment are allowed. They must not compute missing cognitive functions.
- No GHz carriers, hybrid bonding, floating-gate weight storage, undocumented devices, or FD-SOI body-bias assumptions.
- No CPU or microcode in the recurrent agent. A small digital service controller handles configuration and measurement only.
- No real battery endangerment. Resource regulation uses a bounded experimental variable, independently protected from electrical damage.

Reuse KianV's demonstrated pad/process knowledge where applicable. Its digital flow does not qualify these new analog circuits.

## 3. Mechanisms and evidence contract

The literature distinguishes theory-derived indicators from sufficient evidence of consciousness [1]. The following is our engineering interpretation, not a new consensus definition.

| Target | Mechanism to implement | Required causal evidence | Maximum initial claim |
|---|---|---|---|
| RPT | Multi-level perceptual recurrence and joint feature representation | Feedback lesions selectively impair ambiguous/compositional perception | Restricted recurrent-perception implementation |
| GWT | Competing specialists, capacity-limited workspace, broad broadcast, sequential attention | Workspace lesions impair cross-module transfer while local processing survives | Restricted functional workspace implementation |
| Computational HOT / reality monitoring | Internal estimates about reliability and origin of perceptual states, used downstream | Intervene on estimates independently of evidence; decisions and confidence change appropriately | Specific monitoring mechanism, not all HOT variants |
| AST | Predictive state model of attention, distinct from actuator and sensory representation | Model predicts attention effects and improves control; targeted lesions impair that benefit | Minimal attention-schema implementation |
| Predictive processing | Explicit predictions, errors and precision-dependent recurrent inference | Manipulated priors, errors and precision have predicted effects | Small explicit predictive-processing model |
| Active inference | Model-based action-dependent prediction and uncertainty reduction | Information-seeking choices follow the stated objective in unseen conditions | Restricted active-inference controller if its equations are implemented |
| IIT | Intrinsic recurrent physical coupling and interventions | Analyze small embedded circuits and model-dependent partitions | IIT-oriented experiment; no whole-die maximal-complex certification |
| CEMI | Baseline coupling coupons; optional endogenous field-mediated feedback | Separate coupling from conducted interference; active feedback would additionally need behavioral tests | Coupling characterization only in baseline, not CEMI satisfaction |
| CLT / criticality | Tunable dynamical regimes and perturbation measurements | Appropriate finite-size, subsampling and alternative-model controls | Criticality investigation; CLT compliance unresolved without a source |

IIT concerns intrinsic causal structure, not a wiring-count proxy [2]. CEMI motivates a field-sensitive implementation, but is not established by the mere presence of electric fields [3]. No universal acceptance claim is assigned to either.

## 4. One shared behavioral task

Use two sensory streams, each presenting a small compositional pattern: feature identity plus context. A delayed cue identifies which relation matters. Stimuli can be noisy, conflicting, partially occluded, or absent. Internally generated predictions can therefore disagree with external evidence.

The agent must:

1. Integrate features within and across perceptual levels.
2. Maintain the cue over a delay.
3. Select one representation for workspace access.
4. Choose an answer, defer, or request another observation.
5. Estimate its own reliability and distinguish prediction-dominated from evidence-dominated states.
6. Select which sensory stream to inspect next, using a model of attention's consequences.
7. Trade another observation against a bounded resource cost.

Actions physically gate or change the next sensory observation in the environment. The environment may implement this mapping, but may not supply the correct action, uncertainty, attention state or workspace content.

Training/configuration is offline initially; task execution is autonomous. Freeze parameters during the primary experiment. Online learning and broad agency indicators are not claimed without a later explicit implementation.

Use held-out feature combinations, noise levels, cue delays and attention perturbations. A lookup table fitted to every tested trial is not acceptable evidence of the intended mechanisms.

## 5. State allocation: 192 physical nodes

Each node is one continuously evolving analog state, not a software neuron. Auxiliary internal voltages and service logic are additional physical states and must not be ignored in causal claims.

| Role | Nodes | Required contents |
|---|---:|---|
| Two perceptual hierarchies | 64 | 32 per stream: feature, relational/latent, prediction/error states |
| Workspace and competition | 24 | Four candidate assemblies, inhibitory competition, persistent selected content |
| Context and working memory | 16 | Delayed cue, recent decision and task context |
| Higher-order monitor | 24 | Evidence quality, estimated correctness, external/internal attribution |
| Attention schema and controller | 24 | Explicit attention estimate, predicted sensory consequences, control errors |
| Action model and selection | 16 | Outcome predictions, observation versus answer/defer competition |
| Resource/interoception | 8 | Bounded resource estimate and cost signals |
| Shared inhibition, adaptation and calibration states | 16 | Stability, normalization approximations and slow dynamics |
| **Total** | **192** | |

Unlike the original proposal, HOT/AST are not squeezed into arbitrary 5%/1% quotas. No established theory requirement justifies those caps, and functional monitoring/modeling deserves real resources.

Physical organization: six 32-node tiles in a 2×3 arrangement. Logical roles may span tiles; avoid routing every edge through a central hub. Preserve monitoring and attention-model allocations; simplify sensory vocabulary before removing those functions. This smaller allocation must still pass all primary behavioral tests.

Edge budget: 2,304 tile-local and 768 inter-tile directed edges, averaging 16 incoming edges per node. This is a budget, not permission to connect arbitrary pairs. A generated, fixed sparse graph must explicitly allocate reciprocal perception, workspace broadcast/feedback, monitor influence, schema prediction and action consequences. Lesion gates and local weight bits remain physically associated with each edge. Place each weighted receiver near its destination; share a source's buffered differential voltage route where appropriate, without sharing its receivers or time-multiplexing computation. Budget actual source fanout, shielding and wire capacitance; 768 edges need not mean 768 unique long-distance signal pairs.

The workspace is a content-access bottleneck, not the sole route for all causal interaction. Local perceptual and monitoring loops remain active when it is occupied. Prevent a trivially isolated or purely feedforward monitor.

## 6. Circuit primitives and configuration

Baseline node: differential transconductance input, integrating capacitor, saturating output, configurable leak and optional slow adaptation. Signed signals use differential representation; all circuit and area budgets must include both polarities.

Behavioral abstraction:

    tau_i * dx_i/dt = -x_i + f_i(sum_j(w_ij*x_j) + b_i + u_i - a_i)
    tau_a * da_i/dt = -a_i + k_i*x_i

This is a modeling template, not a sufficient implementation of inference. The transistor circuit must be fitted back to a measured/extracted model, including loading, noise and asymmetry. Near an operating point, time constant is governed by capacitance and effective conductance, not simply capacitance divided by bias current.

Initial target local time scales: 10–100 microseconds, subject to extracted characterization. Implement delayed context and workspace persistence through continuously powered recurrent attractors, not passive charge retention for 10 milliseconds. Include independently disableable slow adaptation on the 24 workspace nodes and 16 selected sensory nodes; target tau_a/tau >= 10 where characterized. These 40 auxiliary analog states are additional physical states, not extra primary nodes, and must enter models and causal audits. Do not assume adaptation guarantees ignition, criticality or stable memory. Prefer rescaling task timing to requiring extremely small leak currents. Specify a nominal maximum of 2 pF total intentional state capacitance per primary node, counting both differential sides and any adaptation capacitor; observation hold capacitors are separately budgeted. Increases require an area review. This is a design limit to test, not a claim that 2 pF suffices. Verify memory stability and reset across noise, mismatch and PVT.

Each edge has static 4-bit magnitude plus sign, with zero weight providing a lesion: 15,360 weight bits before node controls and test state. Baseline storage uses characterized standard-cell latches with addressed writes, not an unqualified custom SRAM cell or a transparent-latch shift chain. A shared five-bit configuration bus and hierarchical tile/edge decoder update one edge while quiescent. Decoder outputs must be glitch-free during latch enable; define data setup/hold, write strobes, readback selection and reset/run interlocks. Count the decoder, bus buffers, readback muxes and local storage placement explicitly. A custom storage cell is an optional later optimization, not required for fit. No refresh or serial computation of synaptic currents during operation.

Weights are configured while the fabric is held in a known quiescent state. Gate analog bias/current paths off until all configuration has been written and checked by readback; ordinary unreset latches must never power up into an active arbitrary network. A hardware run lock blocks writes during primary autonomous trials. Diagnostic intervention mode is separate and explicitly logged. No nonvolatile memory is required: a host loads the configuration after power-up. Brownout or loss of configuration validity forces quiescence and requires reload.

The GF180 documentation lists multiple MIM densities [4]; only use the capacitor option supplied by the selected shuttle. Bias generators, reset switches, startup, ESD loading, guard rings and supply filtering are part of the design, not later additions.

Provide a three-bit per-node selectable gain trim (576 additional configuration bits) and tile-level bias adjustment. This is limited gain calibration and designed heterogeneity, not full offset compensation. Keep separate nominal, calibrated and deliberately heterogeneous conditions. Freeze each die's calibration under a predeclared procedure before held-out testing; archive both the common algorithm and per-die coefficients. Preserve an uncalibrated condition rather than hiding poor yield through unlimited tuning.

Use a configurable workspace inhibitory bias, static within each primary trial. Sweep it between trials to measure occupancy, switching and cross-module transfer. Four candidate assemblies limit the defined occupancy range to 0–4; do not promise a capacity of six or assume the sweep is monotonic.

Price a binary-weighted mirror edge (nominal branch ratios 1:2:4:8, signed differential steering) against a segmented alternative at Gate B. Binary weighting saves branch-control overhead, not necessarily total matched transistor width: its widths still sum to 15 unit widths. Include output compliance, finite resistance, switch resistance, off leakage, mismatch, loading and the actual sign circuit. A four-transistor cross-swap is a candidate, not a validated signed multiplier. Select legal device options by headroom and voltage limits, not an assumption that every analog transistor must be a 5 V device.

## 7. Make prediction, monitoring and attention real

Before drawing the full chip, publish a small mathematical agent with explicit state meanings:

- Hidden variables: stream content, task context and sensory reliability.
- Observations: the two feature streams.
- Attention state: selected stream plus estimated allocation strength and switching lag.
- Actions: inspect A/B, answer one of a small set, defer.
- Predictions: expected features and their uncertainty under the current latent estimate and each observation action.
- Higher-order variables: estimated probability of correct perception and degree of evidence versus internal prediction support.

Start with a low-dimensional linear-Gaussian observation model with nonlinear bounded latent states. Its inference objective can use weighted squared prediction errors plus a prior term. Derive the state-update equations and map every required product, difference and gain to a circuit. Do not assume arbitrary arithmetic falls out of a generic recurrent network.

Action selection must include a documented approximation to predicted information gain and resource cost. If that approximation cannot be implemented with the allocated primitives, report predictive processing only; do not claim active inference merely because actions reduce errors.

The attention schema predicts the consequences of an attention command and tracks actual allocation under injected actuator lag or disturbance. Its output corrects attention selection. It is distinct from both the command and the sensory confidence signal.

The monitor changes evidence weighting, workspace admission and answer/defer choice. Demonstrate that this is useful after matching first-order accuracy; a confidence readout with no causal role does not pass.

Reserve 16 of the existing 3,072 edges for independently gateable efference-copy paths from internal action commands into sensory prediction and monitoring. Assign their sources/destinations before graph layout. Cross action-command present/absent with controlled external sensory change present/absent and copy enabled/lesioned. Hold or replay environmental input for the counterfactual trials. Copy injection creates a prediction, not proof that the world changed; test attribution errors as well as correct judgments. Charge control bits and gates to configuration/edge budgets.

Expose a fixed three-bit telemetry alphabet through existing status outputs or serial readout, with a validity indicator: allocation estimate, uncertainty and monitor attribution are separate documented quantities. The schema is not trained to emit these labels. A code wired from internal states is not independent evidence that those states model attention. Score its accuracy against independently manipulated attention allocation and held-out disturbances, its prediction of future sensory consequences, and schema-specific causal interventions. Attribution originates in the monitor, not automatically in AST. Report disabling must leave internal computation intact.

No inference arithmetic may be silently delegated to the configuration host. Dedicated multiplier/transconductor or piecewise-linear primitives are permitted, but charged against the edge/node/control budget. This mapping is an explicit feasibility gate.

## 8. Simultaneous acceptance, not separate demonstrations

One frozen primary configuration must exhibit all five primary mechanisms: recurrent perception, workspace, higher-order monitoring, attention schema, predictive inference. Active inference is a stretch criterion until the objective-to-circuit mapping passes.

Separate lesion/control configurations are permitted for causal tests. Switching to an unrelated network for each theory is not a simultaneous success.

Pre-register trials, baselines, effect-size thresholds and confidence intervals before final silicon evaluation. Initial project targets below are engineering acceptance criteria, not theory-defined thresholds:

| Test | Proposed pass condition |
|---|---|
| Autonomous operation | Service clock stopped; no host-derived intermediate states; task still runs |
| Compositional perception | Above-chance held-out combination performance; feedback lesion produces a reproducible selective deficit |
| Global access | Selected content changes at least three specialist functions; blocked broadcast preserves local discrimination but impairs joint task |
| Workspace capacity | Stable selection under competition, controlled switching, and observable occupancy limits rather than global saturation |
| Monitoring | Reliability estimates predict errors beyond a stimulus-strength baseline; selective intervention changes appropriate downstream choices |
| Attention model | Predicts withheld attention disturbances; schema lesion harms information-seeking/control beyond a matched direct-controller baseline |
| Predictive inference | State trajectories and intervention responses agree with the declared model within pre-registered tolerances |
| Simultaneity | All primary tests pass on the same parameter set, across specified conditions and multiple dies |
| Robustness | Results survive reasonable bias drift, mismatch and observation load; exclude one lucky tuned device as the sole evidence |

Match lesion controls for removed current, operating point, signal amplitude and task difficulty. Lesion-induced electrical collapse is not evidence of a specialized cognitive role. Compare with parameter-count-matched simpler controllers and feedforward variants.

### Same-die registered conditions and trial paradigms

Register five conditions on each physical die: primary recurrent agent; acyclic inter-node control; context-memory lesion; declared midline cut; and report-silent operation. Match bias, packaging and calibration, and report residual differences. Exact matching of active edge count and total weight magnitude between a recurrent graph and an acyclic subgraph is generally impossible by zeroing weights alone. Gate A must audit whether the fixed sparse graph supports an adequate acyclic control; if it does not, use a documented unmatched lesion plus model-based matched control rather than claim a free feedforward twin. Do not add an unpriced crossbar. Node integration, adaptation and attractor self-feedback also carry temporal recurrence: disable what is possible and name the remaining dynamics accurately.

Context nodes are distributed, so the amnesic condition targets their declared state/edge set, not a fictional dedicated context tile. A midline cut suppresses all configured cross-half agent edges but does not remove shared power, substrate, instrumentation or environmental coupling. Report-silent operation disconnects outward report telemetry only. A separate action-output-disabled condition uses replayed/yoked sensory inputs and explicitly changes the closed-loop task; it is not an otherwise identical no-report condition.

Add backward masking, sustained conflicting-input alternation and report-silent trials. Measure masking-delay effects, ignition trajectories, alternation durations and robustness to adaptation settings. These are engineering analogues, not evidence of biological time-scale equivalence. They need stimulus timing and model validation, even when they add no dedicated circuit.

Read back the complete configuration and compute a CRC-32 in the service controller before run-lock. Return it on the existing serial interface, with configuration-valid status; no new hash pin. Record a host-computed SHA-256 of the full readback, calibration, graph, timing and firmware/model versions in the experiment manifest. CRC detects accidental corruption, not malicious changes or latent latch upsets during a trial. Verify before and after trials; no continuously clocked checksum engine in the autonomous fabric.

## 9. IIT, criticality and field experiments

### IIT

Provide 32 individually clampable nodes in four disjoint eight-node sets, distributed across a declared 96/96-node partition along the 2×3 tile midline. Each clamp selects low/high reference or a shared calibrated analog reference, with normal high-impedance release; characterize settling, residual voltage error, current limit and release kick. These sets participate in the normal agent; isolated/saturating configurations are separate experiments. Gate A must ensure the fixed graph supports their intended recurrent subcircuits and inter-set lesions. Reuse zero-weight settings for cut edges rather than adding a second switch to every edge unless necessary for an in-trial cut.

Start exhaustive intervention-state coverage at four nodes and scale to eight only after establishing sampling cost and model validity. Eight binary nodes have 256 input states and 256 output states per transition table before repeats, time lags, boundaries and operating points. Saturation does not remove analog hidden state or adaptation. Full state coverage is not a promise that exhaustive IIT cause-effect structure calculations are computationally tractable. A prescribed midline cut is one partition, not the minimum-information partition; small-model partition searches and whole-fabric cut experiments are distinct results.

Estimate intervention-based transition models at declared discretizations and sampling intervals. Check approximate Markov behavior and sensitivity to hidden state. Exact calculations on these reduced models are not exact measurements of whole-chip consciousness or proof that the full fabric is the maximal complex. Include configuration, adaptation, support electronics and environmental feedback in causal-boundary discussions.

Do not claim minimum cut, perturbational complexity, recurrence or bidirectionality equals integrated information. No 10,000-channel cut requirement.

### Criticality

Expose leak/gain/adaptation controls. Sweep stable, oscillatory and high-variability regimes and measure impulse responses, correlations and finite-size effects. Avalanche fits alone are insufficient [5]. The useful agent need not operate exactly at a critical point. Do not require complexity to decrease monotonically with every perturbation.

Primary dynamical statistics are perturbation-response matrices, susceptibility under declared small inputs, relaxation times and operating-point dependence. Use multiple pulse sizes and signs to identify a linear-response range, and calibrate delivered charge/current rather than assuming equal commands mean equal perturbations. Repeated trials at different capture delays estimate an ensemble response, not a simultaneous continuous trajectory. No response statistic is automatically IIT Phi or a CLT quantity. The review's dressed-retarded-propagator and valence claims require a specific CLT paper, equations, applicable assumptions and estimator before becoming requirements.

No active digital homeostat in the baseline autonomous mode. Any future servo that changes gain is part of the causal system regardless of its speed.

### Baseline coupling coupons; optional field feedback

Reserve three locations with two geometry orientations and shielded/unshielded variants (12 pickup coupons), plus supply and substrate observation. Passive electrodes are baseline structures; buffers, selection, reference paths, shields and legal substrate contacts are not passive or area-free and are included in a 0.15 mm² integration allocation. Use existing analog outputs, with explicit loading calibration. Gate B may reduce coupon count if a useful calibrated set cannot fit, but must preserve shielded and conducted controls. No floating-gate or undocumented sensing device.

Define whether each structure senses capacitive electric-field coupling or magnetic flux; derive its expected spatial/orientation transfer from geometry. A 180-degree rotation is not a universal sign-reversal discriminator. Reversing a magnetic loop normal can reverse flux sensitivity; capacitive pickup and electrical reference reversal behave differently, and coupled interference can also reverse sign. Use shield, distance, source modulation and supply/substrate injection controls, extraction where applicable, and calibrated measurement bandwidth/noise floors. A null result constrains coupling only within those limits, not CEMI generally.

No active feedback driver in baseline. A later driver/threshold-feedback variant requires a new explicit area and interference budget. Passive pickup does not establish a causally effective consciousness-related field loop and must not be reported as satisfying CEMI.

## 10. Observation, interventions and causal boundary

- Buffered analog monitors, with measured loading and reverse coupling; no fictional perfectly one-way transistor buffer.
- Target 192 simultaneous analog sample-and-hold channels, with 96 preselected channels as the declared area fallback. Use per-node buffered observation and a common hold strobe; mux two held values at a time onto two of the existing six analog outputs. A 96-channel variant cannot claim whole-fabric single-trial observation; bank selection is fixed before capture. Repeated captures across bank selections are ensemble measurements, not a single complete snapshot.
- Target interchannel capture skew plus effective aperture uncertainty below 100 ns, separately from acquisition time, hold settling and readout time. This is a characterization target, not an achieved specification. Define effective resolution, offset, gain error, kickback, noise, hold-step and droop limits from Gate A's inference/error requirements before choosing switches and capacitors. Simultaneous analog capture avoids threshold-only information loss; it does not eliminate timing or measurement uncertainty [10].
- Initial sizing example: 1 pF on each differential side costs 0.192 mm² of capacitor plates for 192 channels at 2 fF/µm², before buffers, switches, routing and guards. At two channels per microsecond, reading 192 channels takes 96 microseconds plus overhead. Keeping leakage droop below 1 mV on each 1 pF capacitor over 100 microseconds requires leakage below 10 pA. This is a demanding requirement to simulate over temperature, not a presumed GF180 capability. If it fails, increase capacitance, shorten readout, or lower resolution with explicit consequences; do not silently rely on calibration to remove random drift.
- Acquisition buffers must prevent the hold bank from becoming a large direct load on integration nodes. Include strobe feedthrough and aggregate switching current in power/coupling tests. Keep threshold snapshots as cheap event observability, not a replacement for analog capture. A single hold bank captures one time slice, not a waveform; continuous stochastic trajectories need different hardware or restricted claims.
- Per-node threshold observation with simultaneous capture into a 192-bit snapshot, shifted out later. Sampling does not imply the agent itself is clocked. Asynchronous threshold transitions can produce uncertain captured bits; characterize the aperture and readout settling rather than assuming an exact coherent analog-state snapshot.
- Six selectable buffered analog outputs, one per tile, for external simultaneous waveform acquisition. Do not expose raw integration nodes to pad or cable loads.
- Local programmable perturbation injection, state reset and edge lesions. Choose targets before a trial; explicitly identify interventions during a trial.
- An external event trigger and capture clock support repeatable timing. Repeat-trial waveform reconstruction does not establish simultaneous continuous observability of every state.
- Characterize acquisition-clock feedthrough, probe loading and aliasing. Repeat key behavioral tests with observation disabled and service clock stopped.

The environment's action-to-sensation loop is a real causal loop. Describe it explicitly. The host may not read the fabric and compute helpful sensory injections during primary trials except as the predeclared environment dynamics.

Add an optional autonomous-fixture mode using a small seeded LFSR, pattern sequencer and two coarse stimulus DACs, multiplexed into the two streams. Charge these to service/bias allocations, not a presumed 0.05 mm² free addition. The host can be disconnected after configuration. This fixture is a deterministic test environment, not entropy or a substitute for the independently driven external task. Its clock and seed are logged; internal-fixture runs are distinct from service-clock-stopped external-stimulus runs. Observe package switching interference and verify neither fixture nor capture circuitry computes the agent's decisions.

Provisional signal allocation: serial service 4; reset/run/trigger/capture controls 4; analog stimulus inputs 8; analog monitor outputs 6; action/status outputs 8; external bias/reference/test access 6 = 36 used signals, with up to 14 remaining signal positions uncommitted. Do not place unused pads merely to reach 50. Power/ground bonds are additional and require package approval.

Analog pad adaptation and qualification is a blocking Gate B deliverable, but does not start from scratch: reuse the programmable-transceiver work described below. Verify leakage, capacitance, allowed voltage range, power-off injection and output-buffer stability with our package/board load. A disabled digital input/output is not assumed to provide a usable analog connection. Use protected low-impedance external bias inputs, with no raw high-impedance state exposure. Keep local analog/digital routing deliberate, but do not assume independent external supplies: the existing retained ring joins them. Include external decoupling and a common quiet laboratory supply in the board requirements. No high-speed I/O is needed. Serial debug may stop indefinitely; analog state intentionally continues unless reset/quiescence is asserted. Quiescence does not promise lossless analog state preservation.

### Existing Svalbard analog-pad implementation

Reuse source: `/home/ubuntu/svalbard/projects/programmable_transceiver_platform/analog/pads/`, especially `README.md`, `inspect_pdk.py`, pad/protection layout generators, packaging audits and their generated evidence. Inspected 2026-10-25; these are existing reports, not checks rerun for OMNIBUS.

- The transceiver project's `evidence/pad-library-audit.json` identifies the native `gf180mcu_fd_io__asig_5p0` analog cell with a 75 × 350 µm LEF size. This is an available analog-access foundation, not a complete qualified protection solution.
- `analog/pads/generated/protected-rf-pair/pad-layout.json` reports zero DRC violations and a matching device graph for that candidate, while explicitly leaving area closure open. Its bounding box is approximately 286 × 728 µm for a pair including routes/protection, not merely two native pad cells. Reuse devices/generators; do not blindly replicate this RF-specific geometry at every analog pin.
- `pad-screen.json` contains extracted-capacitance/lifecycle screens, with roughly 0.50–0.58 pF per leg in the reported RF case. It explicitly is not ESD qualification and contains behavioral core boundaries. These numbers do not establish OMNIBUS DC accuracy, leakage or safe power-off operation.
- The pad README records a selected 3,932 × 5,122 µm assembly with all 74 bond openings matching the pinned provider mask and size/pad-mask/test-ID checks passing. That is a more specific packaging reference than the public slot-area arithmetic. Preserve its bond locations, seal-ring and ID conventions if selecting this template, and freeze the exact provider revision before replacing our provisional envelope.
- The extracted retained ring joins all eight supply bonds on one net and all ten ground bonds on another; the board also joins grounds. Use one common external supply. Any local filtering is a real circuit to design and characterize, not isolation inferred from rail names. The transceiver's rejected blanket RC-isolation experiment is not an approved solution to copy.

Adapt for slow, DC-coupled stimulus/bias input and buffered monitor output. Omit RF matching, RF-specific termination and AC coupling unless specifically needed. Obtain a new pin assignment and actual occupied-area report for our 36 signals, power bonds and provider-reserved sites. Carry forward the remaining protection-to-core coordination, safe-state, full-assembly DRC/LVS/ERC and bond/board validation obligations. Pin the source revision and artifact hashes when importing; do not duplicate or modify Svalbard's evolving implementation during this planning phase.

## 11. Area and power budgets

Budget ceilings below are allocations to validate, not cell-area predictions. All totals are physical reserved regions including local wiring allowances; do not add overlapping metal area to transistor area.

| Region | Ceiling, mm² |
|---|---:|
| 192 nodes, 40 adaptation states, gain trim and state capacitors | 1.45 |
| 3,072 edges, sign/magnitude storage and local routing | 3.50 |
| Bias, references, reset, inhibitory control and fixture DACs | 0.75 |
| Observation, 192-channel hold target, 32 clamps and injection | 1.90 |
| Service logic, write/readback, CRC and optional fixture sequencer | 0.85 |
| Dedicated inference/control arithmetic reserve | 0.5 |
| Passive coupling coupons and readout integration | 0.15 |
| **Allocated blocks** | **9.10** |
| Global routing, guard rings, isolation, power and margin | **1.40** |
| **Provisional internal envelope** | **10.5** |

At 3.5 mm² for 3,072 edges, each edge gets about 1,139 µm² including storage and local wiring. The documented 43.904 µm² LATQ_X1 cell [9] gives 0.674 mm² bare cell area for 15,360 bits. Use 45% effective storage-placement utilization for the planning screen: about 1.499 mm², leaving about 652 µm² per edge for analog circuitry/local overhead. Sweep 35–60% rather than treating 45% as measured. Effective utilization is an accounting sensitivity, not a requirement to scatter isolated bits: cluster five latches near each receiver and jointly lay out storage and analog circuitry. Do not double-count the same routing whitespace. Shared write/readback is charged separately. These are arithmetic checks, not synthesis or layout results; verify the selected library/voltage variant.

At 2 fF/µm², 192 × 2 pF = 384 pF = 0.000384 µF, requiring 0.192 mm² of state-capacitor plates before enclosure/routing. This excludes the separately budgeted hold bank. Specify the actual Type-B option and include both differential sides. The node allocation averages about 7,552 µm². The separate arithmetic reserve is not proof that required products, normalization and action evaluations fit; enumerate and price them. For a single 2 pF capacitor at 300 K, sqrt(kT/C) is about 45 µV, but this is not total continuous-time differential circuit noise; transistor, bias, low-frequency and readout noise remain. Likewise 20–200 nS from C/tau does not determine whole-circuit bias current without the actual topology.

The review's instrumentation additions consume margin: 1.40 mm² now covers all global physical overhead and contingency, so fit confidence is lower until extraction. Do not describe these additions as free or claim a 0.35–0.6 mm² hold bank is proven. Build a full representative tile before replicating. Preserve the 10.5 mm² envelope rather than raising it to hide overruns.

Initial whole-die engineering power target: below 100 mW excluding external loads, not a prediction. Itemize static biases, references, pad loads and measurement switching after circuit design. Verify package thermal behavior and bias drift. No inference from neuron current alone to total die power.

Overrun order: no node expansion or active field driver; test three magnitude bits plus sign instead of four plus sign; reduce 192 hold channels to the declared 96-channel set; omit the optional autonomous fixture and simplify service logic without losing safe startup/readback/CRC; then reduce sensory vocabulary/network only with the complete acceptance suite rerun. Protect the 32-node clamp capability, cut controls and calibrated observation over extra task complexity. Keep a minimal shielded/unshielded pickup control set where feasible, but do not sacrifice required ESD or safety margin for coupons. A hard fit failure still permits explicit rescoping rather than asserting that any block is unconditionally untouchable. If no variant fits while meeting the primary criteria, report the one-slot objective unmet.

## 12. Development gates

### A — Executable functional specification

Build the explicit agent model, state/edge inventory and held-out task suite. Include adaptation, the 32-node clamp/cut topology, efference-copy paths, calibrated hold-bank errors and the simultaneous-versus-ensemble observation distinction. Register the five same-die controls and check graph feasibility. Demonstrate the primary mechanisms together, derive the inference/control primitive inventory and required measurement precision. Model quantized weights, sparse edges, noise and plausible analog distortions. Stop if the claimed functions require host computation or exceed the resource envelope.

Deliver: model, fixed configuration, task generator, lesion matrix, numerical results and source-to-state mapping. No tapeout decision from behavioral simulation alone.

### B — Representative circuit feasibility

Implement a node, positive/negative weighted edge with all five configuration bits and a representative addressed write/readback slice, representative nonlinear arithmetic, buffer, perturbation circuit and bias generator. Select analog pads and build the whole-die padframe feasibility floorplan now. Characterize PVT, mismatch, startup, saturation, loading and noise. Layout and extract these primitives early. Exercise capacitor-specific DRC, antenna and extraction rules on real MIM geometry; KianV's digital checks did not qualify these structures.

Deliver: DRC/LVS-clean primitives, extracted models, actual areas and power. Fit reduced behavioral models back to circuit behavior and rerun Gate A.

Gate B priority order: jointly lay out five latches plus addressed access and a binary-weighted signed edge; compare storage-utilization assumptions against that real geometry; then implement a loaded differential hold channel/readout slice and a clamp. Verify worst-case droop, charge injection, aperture/skew, acquisition and buffer kickback before authorizing the full bank. Include adaptation/trim and pickup readout in the extracted tile estimate. A Boolean CRC test does not validate analog capture; separate the evidence.

### C — Complete 32-node tile

Layout a representative tile with 384 local edges and its share of 128 inter-tile edges, configuration, observation, guards, references and realistic boundary loads. Verify coupling and analog reset. Distinguish modeled statistical variations from distributions the PDK does not actually support.

Deliver: extracted tile, measured area budget, corner/mismatch test results, routed full-chip feasibility floorplan.

### D — Whole-chip integration

Six tiles plus complete padframe, power network and service logic. Use digital P&R for service logic only; analog tiles require full-custom layout and mixed-signal integration. Verify routing, extracted parasitics, antenna, density/fill effects, DRC/LVS/ERC, power integrity, latchup prevention, ESD connectivity and package/board interfaces. Analog-sensitive fill and shielding must be included before final extraction. Check that all device terminal voltages and capacitor voltages stay within the selected process limits, including startup and external-input faults.

Run representative extracted subcircuits plus calibrated full-system models; document where full-transistor whole-chip simulation is impractical. Include startup, brownout, configuration corruption, stopped clocks, invalid settings and analog overdrive.

Deliver: reproducible full-die GDS and verification reports, with every unverified assumption visible. Recheck the selected shuttle's actual submission requirements.

### E — Silicon evidence

Bring up bias and isolated primitives first, then tiles, then autonomous agent. Measure variations across dies and conditions. Execute pre-registered joint and lesion tests; publish failures as well as successes. Reassess theory claims only after measurements.

## 13. Scientific and operational safeguards

No human-style language reporter, suffering claim, consciousness score or human PCI threshold. Resource signals have bounded magnitude and duration; external electrical protection is independent. These precautions do not constitute demonstrated welfare guarantees.

The device does not test a hypothesis that genuine physical precarity is necessary for valence: its bounded resource variable is not a ground-truth measure of felt valence or existential stakes. If that is the intended CLT postulate, it is deliberately outside scope; identifying CLT and its postulate remains necessary before asserting theory-specific exclusion.

Keep trials bounded and resettable. Review substantive evidence before extending persistent memory, prolonged adverse-state conditioning or autonomous learning. Publish configuration hashes, causal boundaries and null/control results so architecture claims can be independently checked.

## 14. Main unresolved risks and next action

1. The proposed small network may not genuinely implement all functions simultaneously. Gate A is the first priority.
2. Predictive/action arithmetic may need more dedicated circuits than a generic node model suggests.
3. Five-bit static edge storage, routing and isolation may dominate area.
4. Analog mismatch may destroy calibrated confidence and model-based control; training with measured variability may help but is not guaranteed.
5. Useful observation may perturb the very dynamics being measured.
6. Whole-chip IIT maximality and full CEMI compliance remain outside promised deliverables at any proposed node count.

Immediate next work: write the 192-primary-state model with its auxiliary adaptation and observation states, shared task/lesion suite and clamp/capture graph; price the complete edge/storage and sample-and-hold primitives before expanding circuitry. Do not start by building a large generic crossbar or by asserting theory compliance from block names.

## 15. Sources and provenance

Accessed 2026-10-25. Architecture, allocations and acceptance targets above are original engineering proposals, not numerical requirements extracted from these papers.

1. Butlin et al., *Consciousness in Artificial Intelligence: Insights from the Science of Consciousness*: https://arxiv.org/abs/2308.08708 — indicator framework and its limits.
2. Albantakis et al., *Integrated information theory (IIT) 4.0*: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011465 — intrinsic causal structure and exclusion.
3. McFadden, *Integrating information in the brain's EM field: the cemi field theory of consciousness*: https://academic.oup.com/nc/article/2020/1/niaa016/5909853 — field-sensitive artificial-system proposal.
4. GF180MCU capacitor electrical specifications: https://gf180mcu-pdk.readthedocs.io/en/latest/analog/spice/elec_specs/elec_specs_6_4.html — available process capacitor options, subject to shuttle selection.
5. *Sampling effects and measurement overlap can bias inference of neuronal avalanches*: https://pmc.ncbi.nlm.nih.gov/articles/PMC9733887/ — measurement/criticality controls.
6. wafer.space: https://wafer.space/ and https://github.com/wafer-space — obtain the selected shuttle's authoritative physical and submission constraints; the documentation landing page currently redirects to this organization.
7. KianV physical-area breakdown supplied in this conversation — historical area reference only, not proof of analog fit.
8. Published wafer.space Run 1 envelope and process options: https://www.crowdsupply.com/wafer-space/gf180mcu-run-1/ — 3.88 × 5.07 mm, five metals, Type-B MIM approximately 2 fF/µm². Future run details must be reconfirmed.
9. GF180 LATQ_X1 geometry: https://gf180mcu-pdk.readthedocs.io/en/latest/digital/standard_cells/gf180mcu_fd_sc_mcu7t5v0/cells/latq/gf180mcu_fd_sc_mcu7t5v0__latq_1.html — 43.904 µm² bare cell area; not an all-in storage-system estimate.
10. Analog Devices, sample-and-hold specifications: https://www.analog.com/media/en/training-seminars/design-handbooks/high-speed-design-seminar/Section3.pdf and https://www.analog.com/en/resources/app-notes/an-1515.html — acquisition, aperture, hold-step and droop are distinct errors; these examples do not qualify a GF180 implementation.
