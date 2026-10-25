# OMNIBUS-GF180: one-die multi-theory experimental agent

Date: 2026-10-25. Status: pre-schematic research architecture.

## 1. Objective and claim boundary

Build one wafer.space GF180MCU 1x1 die that performs a small but meaningful perceptual-control task using physically instantiated recurrent perception, global access, higher-order monitoring, an attention model, and predictive control together.

Optimize for the number of **substantive, independently testable mechanisms that operate concurrently**, not the number of theory names attached to blocks. No claim that this device is conscious, that all variants of a theory are satisfied, or that a minimum size for consciousness is known.

The principal deliverable is a causal-intervention laboratory with a working autonomous agent. A collection of disconnected demonstration circuits does not meet the objective.

The baseline is a purpose-built continuous-time perceptual controller with explicit internal models, not a generic neural fabric. Its planning ceilings are 192 primary states and 3,072 dedicated weighted connections; neither is a population quota to fill. There is no 256-node expansion in this tapeout plan. Optimize joint implementation of the primary mechanisms before optional theory experiments. Functional feasibility must precede schematic commitment. Failure to fit or function is a result to report, not a reason to relabel a simpler mechanism as compliant.

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

## 5. Integrated architecture and state ceilings

### 5.1 One agent, not independent theory demonstrations

The primary target is simultaneous restricted implementations of recurrent perception, functional global access, computational higher-order monitoring, an attention schema and explicit predictive inference. Active inference is a secondary joint target once its equations and circuit implementation pass. IIT and field experiments must not displace resources needed to make these primary mechanisms real. This is an implementation priority, not a ranking of which consciousness theories are true.

Use two recurrent perceptual specialists and a common context-dependent controller. The following paths are mandatory during normal operation, not enabled only for a theory-specific demonstration:

1. Context memory and workspace content generate top-down sensory predictions. Separate bottom-up evidence and signed error paths update each specialist's latent content; controllable precision determines error influence. Each specialist must represent at least a small relation between features, not merely classify one scalar.
2. Actual attention gates the two sensory streams. A distinct schema predicts the gate's allocation and dynamics from command copies and observed consequences. Its allocation error changes subsequent attention commands. It must not be a second name for the command signal.
3. An observer receives evidence, prediction, error, command copies, actual attention feedback and selected workspace content on distinct paths. It estimates reliability and prediction-versus-evidence support. Those estimates influence precision, workspace admission and answer/defer decisions.
4. Two source-linked candidate representations compete for a persistent workspace selection. One common selection gates a structured bundle of content, source identity and validity/reliability. Broadcast the bundle over dedicated paths to perception/prediction, context memory, monitoring and action selection. Do not select each field independently and accidentally combine different candidates.
5. The action controller uses workspace content, context, observer estimates and predicted observation outcomes to answer, defer or inspect a stream. Its efference copies update prediction and monitoring. Environmental consequences feed back into the same inference system.

The workspace does not replace local recurrence. Observer and schema receive bottom-up feedback as well as command copies, and their outputs must have nonredundant causal roles. No external controller may supply their estimates or replace a failed inference computation. A finite-state environment fixture is not part of their implementation.

Primary demonstration: the same frozen configuration must use these coupled paths for context-selected feature identification, delayed-cue comparison and observation-before-answer decisions. These are three modes of one small task family, not three separately programmed agents. Maintain the same signal meanings and broadcast representation across modes. Verify that removal of each claimed mechanism has its predicted selective consequence; an engineered bottleneck alone is insufficient evidence of a useful mechanism.

### 5.2 Replace generic recurrence with explicit primitives

Implement repeated prediction/error/precision motifs, rather than allocating arbitrary synapses and hoping training discovers the computation. Use fixed-wired unity/subtraction paths where appropriate and programmable gains only where the model, calibration or interventions require them. Replacing a programmable edge with fixed circuitry is permitted only with the necessary intervention access retained.

Use leaky continuous-time states for perception, explicit set/reset recurrent attractors for context, persistent selection with controlled release for workspace, and slow negative feedback only where the model needs adaptation. Dedicated product, difference and comparison circuits implement the stated equations; they are not presumed to emerge from generic nodes. This may save configuration storage but savings must be demonstrated by extracted layout.

The next specification is a named-state and primitive inventory: variable, equation, units/range, input paths, output consumers, memory mechanism, calibration and intervention port for every state. Circuit counts follow that inventory. The allocations below remain area-sizing ceilings, not evidence that these mechanisms fit.

### 5.3 Provisional allocation envelopes

Each node is one continuously evolving analog state, not a software neuron. Auxiliary internal voltages and service logic are additional physical states and must not be ignored in causal claims.

The numerical capacitor populations, storage counts and per-region examples in later sections are conservative costing references for these ceilings. The named-state inventory supersedes them before schematic freeze. Do not interpret them as instructions to retain an unused state, weight latch or adaptation branch.

| Role | Nodes | Required contents |
|---|---:|---|
| Two perceptual hierarchies | 64 | 32 per stream: feature, relational/latent, prediction/error states |
| Workspace and competition | 24 | Two source-linked candidate bundles, common selection, persistent content and release |
| Context and working memory | 16 | Delayed cue, recent decision and task context |
| Higher-order monitor | 24 | Evidence quality, estimated correctness, external/internal attribution |
| Attention schema and controller | 24 | Explicit attention estimate, predicted sensory consequences, control errors |
| Action model and selection | 16 | Outcome predictions, observation versus answer/defer competition |
| Resource/interoception | 8 | Bounded resource estimate and cost signals |
| Shared inhibition, adaptation and calibration states | 16 | Stability, normalization approximations and slow dynamics |
| **Total** | **192** | |

Unlike the original proposal, HOT/AST are not squeezed into arbitrary 5%/1% quotas. No established theory requirement justifies those caps, and functional monitoring/modeling deserves real resources.

These counts are provisional implementation allocations, not proof of identifiability or minimality. Each role must carry named variables and permit the interventions in Section 8 without destroying its comparator. Gate A must show that the allocated states suffice; an identifiability table alone cannot establish that 24 nodes are enough.

Physical organization follows the functional graph: place prediction/error motifs together, memory away from switched readout, and broadcast near its consumers. Six 32-node-equivalent regions remain a floorplanning reference only; identical tiles and balanced ring wiring are no longer requirements. Reuse circuit primitives rather than forcing identical macro contents. Preserve the observer/schema functions before expanding sensory vocabulary.

Connection ceiling: 3,072 weighted paths, with the earlier 2,304 local/768 long-range split retained only as a costing reference. Derive the actual count from the required functional paths; do not populate unused edges. Lesion controls and any weight bits remain physically associated with their paths. Place weighted receivers near destinations and share buffered source routes where appropriate without time-multiplexing receivers. Budget actual fanout, shielding and wire capacitance. Fixed arithmetic connections and internal device nodes still count in physical and causal audits even when they require no weight storage.

The workspace is a content-access bottleneck, not the sole route for all causal interaction. Local perceptual and monitoring loops remain active when it is occupied. Prevent a trivially isolated or purely feedforward monitor.

Graph-generation rules: verify the mandatory directed paths in Section 5.1, functional feedback involving each primary mechanism, and full enumeration of paths crossing the experimental partition. Audit strongly connected components and bottlenecks, explaining intentional ones rather than adding wires just to satisfy a graph metric. No obligatory three-tile fanout or equal edge allocation across region pairs: those constraints could waste area and distort the intended computation. Select a near-balanced controllable partition after functional placement. Connectivity does not prove IIT exclusion/maximality or a particular value of integrated information.

## 6. Circuit primitives and configuration

Baseline node: differential transconductance input, integrating capacitor, saturating output, configurable leak and optional slow adaptation. Signed signals use differential representation; all circuit and area budgets must include both polarities.

Behavioral abstraction:

    tau_i * dx_i/dt = -x_i + f_i(sum_j(w_ij*x_j) + b_i + u_i - a_i)
    tau_a * da_i/dt = -a_i + k_i*x_i

This is a modeling template, not a sufficient implementation of inference. The transistor circuit must be fitted back to a measured/extracted model, including loading, noise and asymmetry. Near an operating point, time constant is governed by capacitance and effective conductance, not simply capacitance divided by bias current.

Initial target local time scales span tens to hundreds of microseconds, subject to extracted characterization. Implement delayed context and workspace persistence through continuously powered recurrent attractors, not passive charge retention for 10 milliseconds. Include independently disableable slow adaptation on the 24 workspace nodes and 16 selected sensory nodes; target tau_a/tau >= 10 where characterized. These 40 auxiliary analog states are additional physical states, not extra primary nodes, and must enter models and causal audits. Slow adaptation is not trivial: it needs adequate small-signal conductance, leakage margin and stability. Do not assume it guarantees ignition or criticality.

Use three capacitor populations as circuit candidates: 64 sensory nodes at 0.3 pF per side; 88 workspace/context/monitor/schema nodes at 1.5 pF per side; and 40 remaining nodes at 0.8 pF per side. At 10 nS effective per-side conductance the illustrative time constants are 30, 150 and 80 microseconds, respectively; verify the actual differential-mode conductance convention. Their total primary-state capacitance is 366.4 pF, or 0.1832 mm² of plates at 2 fF/µm². Reserving 0.2 pF per side for each of 40 adaptation states adds 16 pF, taking the candidate total to 382.4 pF / 0.1912 mm². This replaces the uniform 2 pF-per-node limit: slow nodes may use 3.4 pF including adaptation. The hold bank remains separate. These capacitor values and conductances are feasibility candidates, not achieved constants or a guarantee of improved integration. Prefer task-time rescaling to unverified tiny leak currents; verify PVT, mismatch, noise and state stability.

Each edge has static 4-bit magnitude plus sign, with zero weight providing a lesion: 15,360 weight bits before node controls and test state. Baseline storage uses characterized standard-cell latches with addressed writes, not an unqualified custom SRAM cell or a transparent-latch shift chain. A shared five-bit configuration bus and hierarchical tile/edge decoder update one edge while quiescent. Decoder outputs must be glitch-free during latch enable; define data setup/hold, write strobes, readback selection and reset/run interlocks. Count the decoder, bus buffers, readback muxes and local storage placement explicitly. A custom storage cell is an optional later optimization, not required for fit. No refresh or serial computation of synaptic currents during operation.

Weights are configured while the fabric is held in a known quiescent state. Gate analog bias/current paths off until all configuration has been written and checked by readback; ordinary unreset latches must never power up into an active arbitrary network. A hardware run lock blocks writes during primary autonomous trials. Diagnostic intervention mode is separate and explicitly logged. No nonvolatile memory is required: a host loads the configuration after power-up. Brownout or loss of configuration validity forces quiescence and requires reload.

The GF180 documentation lists multiple MIM densities [4]; only use the capacitor option supplied by the selected shuttle. Bias generators, reset switches, startup, ESD loading, guard rings and supply filtering are part of the design, not later additions.

Provide a three-bit per-node selectable gain trim (576 additional configuration bits) and tile-level bias adjustment. This is limited gain calibration and designed heterogeneity, not full offset compensation. Keep separate nominal, calibrated and deliberately heterogeneous conditions. Freeze each die's calibration under a predeclared procedure before held-out testing; archive both the common algorithm and per-die coefficients. Preserve an uncalibrated condition rather than hiding poor yield through unlimited tuning.

Use a configurable workspace inhibitory bias, static within each primary trial. Sweep occupancy, switching and cross-module transfer over the two candidate bundles. Normal operation selects one coherent bundle; weak-inhibition/coactivation conditions are diagnostics and must not be reported as valid two-item workspace access unless content coherence is demonstrated. Do not promise a particular monotonic capacity curve.

Add a required global-gain command with distributed local mirrors, separate from workspace inhibition and per-node trim. Hold it static within primary trials; use calibrated changes between trials for dynamical sweeps. Budget buffers, mirrors, decoupling and fanout inside the bias allocation; do not assume 0.01 mm². Compare broadcast lesions at fixed gain command and across gain-matched controls, measuring actual local responses because a fixed command does not guarantee unchanged effective gain or operating point. The gain line is itself a shared causal coupling path; characterize reverse coupling and noise. Do not call it consciousness or biological arousal by construction. If the schema estimates this state, require held-out prediction tests rather than merely feeding it the commanded value.

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

Make actual allocation and estimated allocation independently clampable. A schema error must be possible without forcing the actuator into the same error. Likewise expose independent observer-state and sensory-evidence interventions. Allocate clamp sites to these dissociations before distributing them for small-model partition experiments.

The monitor changes evidence weighting, workspace admission and answer/defer choice. Demonstrate that this is useful after matching first-order accuracy; a confidence readout with no causal role does not pass.

Define monitor outputs as estimates with explicit targets: expected perceptual correctness under the task, consistency of external evidence with the prediction, and self-command-conditioned versus unexpected residual. Do not equate a residual magnitude with attribution or a single confidence scalar with the full higher-order mechanism. The mapping must distinguish controlled cases with similar posteriors but different evidence/prediction support. Validate the observer's feedback stability jointly with precision and workspace admission rather than evaluating those loops separately.

Reserve 16 of the existing 3,072 edges for independently gateable efference-copy paths from internal action commands into sensory prediction and monitoring. Assign their sources/destinations before graph layout. Cross action-command present/absent with controlled external sensory change present/absent and copy enabled/lesioned. Hold or replay environmental input for the counterfactual trials. Copy injection creates a prediction, not proof that the world changed; test attribution errors as well as correct judgments. Charge control bits and gates to configuration/edge budgets.

Reserve six more existing edges (22 copy edges total, not an expanded edge budget) for attention-command copies to schema and monitor and action-command copies to monitor. Map prediction and signed prediction-error inputs separately for each sensory stream, alongside workspace content and sensory reliability. A posterior alone does not identify how much evidence versus prediction supported it. Provide independently gain-controlled signed comparison paths rather than sharing the copy residual with the primary prediction path. Gate A must count these extra primitives and determine whether prediction plus residual suffices or independent observed-evidence inputs are also needed.

Rank the 0.5 mm² arithmetic reserve by the declared equations: independently adjustable precision weighting of errors; variance/uncertainty update if learning uncertainty is claimed; value comparison for answer/defer/inspect; then information-gain approximation and normalization where required by the model. A variable precision signal needs a variable-gain/product implementation, but fixed precision can be a static weight; no particular Gilbert/translinear topology is a theory requirement. Derive the actual circuit and state count before declaring predictive-processing or active-inference functionality complete.

For scalar Gaussian information gain, I = 0.5*log(v_prior/v_posterior). Comparing variance ratios preserves the ordering of information gain only when the objective is this term alone (or equal costs/constants cancel). It does not generally preserve the ordering of I minus action cost, sums across dimensions, or averages over uncertain outcomes. Use ratio comparison for a narrowly specified equal-cost observation task, or retain a validated bounded-error log approximation when costs compete. Multivariate models require the appropriate determinant/independence assumptions. Test action-ranking error on held-out cases; drop active-inference claims if the approximation fails rather than silently change the objective.

Expose a fixed three-bit telemetry alphabet through existing status outputs or serial readout, with a validity indicator: allocation estimate, uncertainty and monitor attribution are separate documented quantities. The schema is not trained to emit these labels. A code wired from internal states is not independent evidence that those states model attention. Score its accuracy against independently manipulated attention allocation and held-out disturbances, its prediction of future sensory consequences, and schema-specific causal interventions. Attribution originates in the monitor, not automatically in AST. Report disabling must leave internal computation intact.

No inference arithmetic may be silently delegated to the configuration host. Dedicated multiplier/transconductor or piecewise-linear primitives are permitted, but charged against the edge/node/control budget. This mapping is an explicit feasibility gate.

## 8. Simultaneous acceptance, not separate demonstrations

One frozen primary configuration must exhibit all five primary mechanisms: recurrent perception, workspace, higher-order monitoring, attention schema, predictive inference. Active inference is a stretch criterion until the objective-to-circuit mapping passes.

Separate lesion/control configurations are permitted for causal tests. Switching to an unrelated network for each theory is not a simultaneous success.

### Identifiability, not block names

| Mechanism | Nearest competing explanation | Separating experiment and remaining confounds |
|---|---|---|
| Workspace access | Scalar global gain or generic salience | Broadcast-only lesions at fixed gain command, with measured local gain/operating-point controls and local task preservation |
| Higher-order monitoring | Epiphenomenal confidence telemetry | Intervene on monitor states at fixed evidence; test specific changes in weighting and answer/defer decisions |
| Attention schema | Direct attention controller | Schema lesion versus an independently implemented parameter-matched controller, with actuator disturbances and predictive-state interventions |
| Predictive inference | Generic recurrent dynamics | Independently manipulate priors, precision and error channels; predict quantitative trajectories from the declared equations |
| Perceptual recurrence | Feedforward paths plus adaptation/memory | Static acyclic inter-node control with adaptation controls; document topology/current mismatches and retained temporal dynamics |
| Critical dynamics | Generic nonlinear response near instability | Multiple pulse sizes/signs, gain conditions, relaxation and finite-size/model comparisons; no single statistic certifies criticality |

These tests improve causal discrimination but do not make every mechanism uniquely identified under all hidden-state alternatives.

For workspace access include correct-content, broadcast-suppressed and wrong-content conditions. Implement content substitution through a bounded candidate-input selector or existing configurable paths, not a general crossbar. Preserve bundle coherence and match loading/current as far as possible. This distinguishes content-dependent access from loss of excitation. Charge any selector to workspace circuitry; no unpriced test fabric.

Primary success requires the full task family on one frozen configuration with all five mechanisms active. Each mechanism must pass its own discriminating intervention while the other mechanisms retain their intended operation as far as the task permits. Do not count disconnected demonstrations, redundant sidecar estimates, or separate parameter sets as simultaneous satisfaction. Report the specific implemented theory-derived criteria, not a total score implying universal theory compliance.

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

Do not replace this with a purported nonrecurrent round-robin control. A -> B in one phase and B -> A in the next is a causal feedback loop through stored state, even if every instantaneous graph is acyclic. Arbitrarily partitioning edges into thirds also does not guarantee each third is a DAG. A scheduled-edge experiment may be useful later as a distinct temporal-rewiring control, with graph proofs, gate circuitry, duty/current matching and switching artifacts budgeted. The existing static configuration/run lock does not provide free dynamic edge gating. No such hardware is added in this baseline.

Context nodes are distributed, so the amnesic condition targets their declared state/edge set, not a fictional dedicated context tile. A midline cut suppresses all configured cross-half agent edges but does not remove shared power, substrate, instrumentation or environmental coupling. Report-silent operation disconnects outward report telemetry only. A separate action-output-disabled condition uses replayed/yoked sensory inputs and explicitly changes the closed-loop task; it is not an otherwise identical no-report condition.

Add backward masking, sustained conflicting-input alternation and report-silent trials. Measure masking-delay effects, ignition trajectories, alternation durations and robustness to adaptation settings. These are engineering analogues, not evidence of biological time-scale equivalence. They need stimulus timing and model validation, even when they add no dedicated circuit.

Define a minimum proposed factorial evaluation: attended stream (2) × relevant feature (4) × context (3) × delay level (3) = 72 condition cells, with independently varied distractors and multiple noisy repetitions. Both streams still exist on each trial; the factor of two is the queried/attended stream, not the number of simultaneous streams. Hold out declared combinations from fitting/calibration and distinguish training cells from evaluation cells; do not claim all 72 were held out if any were used to tune the agent. Preserve combinatorial coverage when simplifying stimulus encoding. Condition count is not reachable-state repertoire and neither is a monotonic proxy for IIT Phi or an undefined CLT quantity.

Read back the complete configuration and compute a CRC-32 in the service controller before run-lock. Return it on the existing serial interface, with configuration-valid status; no new hash pin. Record a host-computed SHA-256 of the full readback, calibration, graph, timing and firmware/model versions in the experiment manifest. CRC detects accidental corruption, not malicious changes or latent latch upsets during a trial. Verify before and after trials; no continuously clocked checksum engine in the autonomous fabric.

## 9. IIT, criticality and field experiments

### IIT

Provide 32 individually clampable states. Prioritize independent access to evidence versus prediction, actual versus estimated attention, observer reliability, selected workspace content and context. Organize four eight-state analysis sets where compatible with these functions; do not add otherwise unused states to manufacture convenient IIT subsystems. Derive a near-balanced experimental partition from the resulting functional layout, rather than requiring a 96/96 geometric midline. Each clamp selects low/high or a shared calibrated analog reference with normal high-impedance release; characterize error, settling, current limits and release kick. These states participate in the normal agent; isolating them creates a different condition. Cut both fixed and programmable cross-partition paths using explicitly budgeted controls, without assuming zero weights can interrupt a hardwired connection.

Start exhaustive intervention-state coverage at four nodes and scale to eight only after establishing sampling cost and model validity. Eight binary nodes have 256 input states and 256 output states per transition table before repeats, time lags, boundaries and operating points. Saturation does not remove analog hidden state or adaptation. Full state coverage is not a promise that exhaustive IIT cause-effect structure calculations are computationally tractable. A prescribed midline cut is one partition, not the minimum-information partition; small-model partition searches and whole-fabric cut experiments are distinct results.

Estimate intervention-based transition models at declared discretizations and sampling intervals. Check approximate Markov behavior and sensitivity to hidden state. Exact calculations on these reduced models are not exact measurements of whole-chip consciousness or proof that the full fabric is the maximal complex. Include configuration, adaptation, support electronics and environmental feedback in causal-boundary discussions.

Bounded deliverable: enumerate a four-node measured transition model, explicitly select the IIT version and quantity, publish the intervention/conditional boundary convention, solver and small known-result tests, and compute the selected quantity without algorithmic approximation on that estimated model if tractable. Sweep discretization and sampling lag, and propagate transition-estimation uncertainty. Six-to-eight-node analyses are conditional on measured-state adequacy and solver cost, not promised exact full IIT 4.0 structures. Report numerical precision and any approximation rather than treating a measured table as exact ground truth.

Do not claim minimum cut, perturbational complexity, recurrence or bidirectionality equals integrated information. No 10,000-channel cut requirement.

### Criticality

Expose leak/gain/adaptation controls. Sweep stable, oscillatory and high-variability regimes and measure impulse responses, correlations and finite-size effects. Avalanche fits alone are insufficient [5]. The useful agent need not operate exactly at a critical point. Do not require complexity to decrease monotonically with every perturbation.

Primary dynamical statistics are perturbation-response matrices, susceptibility under declared small inputs, relaxation times and operating-point dependence. Use multiple pulse sizes and signs to identify a linear-response range, and calibrate delivered charge/current rather than assuming equal commands mean equal perturbations. Repeated trials at different capture delays estimate an ensemble response, not a simultaneous continuous trajectory. No response statistic is automatically IIT Phi or a CLT quantity. The review's dressed-retarded-propagator and valence claims require a specific CLT paper, equations, applicable assumptions and estimator before becoming requirements.

Required response experiment: use the 32 intervention nodes as sources and retain all 32 among the baseline simultaneously held channels. Estimate the 32×32 causal response matrix over declared delays at nominal and gain-detuned operating points, with sham pulses and both pulse signs. Define normalization, background subtraction and uncertainty. Any closed-loop-product analysis is an explicitly named exploratory project statistic, not a published CLT estimator or proof of irreducibility. Extend to additional operating points where needed to distinguish generic nonlinear dynamics.

No active digital homeostat in the baseline autonomous mode. Any future servo that changes gain is part of the causal system regardless of its speed.

### Baseline coupling coupons; optional field feedback

Reserve three locations with two geometry orientations and shielded/unshielded variants (12 pickup coupons), plus supply and substrate observation. Passive electrodes are baseline structures; buffers, selection, reference paths, shields and legal substrate contacts are not passive or area-free and are included in a 0.15 mm² integration allocation. Use existing analog outputs, with explicit loading calibration. Gate B may reduce coupon count if a useful calibrated set cannot fit, but must preserve shielded and conducted controls. No floating-gate or undocumented sensing device.

Define whether each structure senses capacitive electric-field coupling or magnetic flux; derive its expected spatial/orientation transfer from geometry. A 180-degree rotation is not a universal sign-reversal discriminator. Reversing a magnetic loop normal can reverse flux sensitivity; capacitive pickup and electrical reference reversal behave differently, and coupled interference can also reverse sign. Use shield, distance, source modulation and supply/substrate injection controls, extraction where applicable, and calibrated measurement bandwidth/noise floors. A null result constrains coupling only within those limits, not CEMI generally.

No active feedback driver in baseline. A later driver/threshold-feedback variant requires a new explicit area and interference budget. Passive pickup does not establish a causally effective consciousness-related field loop and must not be reported as satisfying CEMI.

Acquire pickup and supply/substrate channels during autonomous trials using spare analog-monitor outputs where possible, retaining clocks/triggers as nuisance regressors and testing loading with acquisition disabled. Correlate with behavioral states under gain, stimulus and matched supply-injection controls. Correlation with activity may simply reflect normal switching currents and does not establish field causation. Publish detection limits and negative results as coupling observations, not a refutation of CEMI.

## 10. Observation, interventions and causal boundary

- Buffered analog monitors, with measured loading and reverse coupling; no fictional perfectly one-way transistor buffer.
- Baseline: 96 simultaneous differential sample-and-hold channels. Assign 32 permanently to the clamp/response nodes and distribute the other 64 across all functional roles with local pre-capture selection. Enumerate selectable pairs/groups and price their input buffers/muxes; no free arbitrary 192-to-96 crossbar. Mux two held values at a time onto two existing analog outputs. Selection is fixed during acquisition/hold. This cannot claim whole-fabric single-trial observation; repeated captures across selections are ensemble measurements. A 192-channel bank is a later revision option only after fit and measurement justification.
- Target interchannel capture skew plus effective aperture uncertainty below 100 ns, separately from acquisition time, hold settling and readout time. This is a characterization target, not an achieved specification. Define effective resolution, offset, gain error, kickback, noise, hold-step and droop limits from Gate A's inference/error requirements before choosing switches and capacitors. Simultaneous analog capture avoids threshold-only information loss; it does not eliminate timing or measurement uncertainty [10].
- Initial sizing example: 1 pF on each differential side costs 0.096 mm² of capacitor plates for 96 channels at 2 fF/µm², before buffers, switches, routing and guards. At two converted channel values per microsecond, a 96-channel frame takes 48 microseconds plus overhead. Keeping leakage droop below 1 mV per 1 pF capacitor over 50 microseconds requires leakage below 20 pA; budget the actual maximum hold interval including stalls. This is a demanding requirement to simulate over temperature, not a presumed GF180 capability. If it fails, increase capacitance, shorten readout, or lower resolution explicitly. Do not silently rely on calibration to remove random drift.
- Acquisition buffers must prevent the hold bank from becoming a large direct load on integration nodes. Include strobe feedthrough and aggregate switching current in power/coupling tests. Keep threshold snapshots as cheap event observability, not a replacement for analog capture. A single hold bank captures one time slice, not a waveform; continuous stochastic trajectories need different hardware or restricted claims.
- Per-node threshold observation with simultaneous capture into a 192-bit snapshot, shifted out later. Sampling does not imply the agent itself is clocked. Asynchronous threshold transitions can produce uncertain captured bits; characterize the aperture and readout settling rather than assuming an exact coherent analog-state snapshot.
- Six selectable buffered analog outputs, one per tile, for external simultaneous waveform acquisition. Do not expose raw integration nodes to pad or cable loads.
- Local programmable perturbation injection, state reset and edge lesions. Choose targets before a trial; explicitly identify interventions during a trial.
- An external event trigger and capture clock support repeatable timing. Repeat-trial waveform reconstruction does not establish simultaneous continuous observability of every state.
- Characterize acquisition-clock feedthrough, probe loading and aliasing. Repeat key behavioral tests with observation disabled and service clock stopped.

### Capture timing contract

A common-strobe hold bank captures states at one instant (within its characterized aperture/skew) and isolates those samples from subsequent node evolution. Sequential conversion reads frozen values, not a rolling live-node frame [11]. Therefore do **not** impose tau_min >= 20 × frame-readout-time as a requirement for single-snapshot validity. Frame time controls hold-error exposure and, with one bank, the next capture's availability. Fast stochastic trajectories cannot be recovered from slow sparse frames simply because each frame is simultaneous.

Define frame time as ceil(N/L) × t_slot plus overhead, where L is the number of parallel analog output/ADC lanes and t_slot includes mux settling, pad/board settling and ADC acquisition. At 192 channels, two lanes and 50 ns slots the ideal frame is 4.8 microseconds (40 million values/s aggregate). An aggregate 50 MSPS rate implies 3.84 microseconds; 9.6 microseconds corresponds to 20 MSPS aggregate. None of these rates is qualified for our pad/hold circuitry merely because an external ADC supports it. Retain the slower baseline until Gate B validates the full load chain.

For snapshots require bounded aperture error approximately |dx/dt| × timing uncertainty, hold droop, noise and settling relative to the declared measurement resolution. For continuous frame trajectories require a sampling rate justified by measured dynamics/bandwidth and the estimator; a conservative samples-per-time-constant target may be chosen for that mode, not applied retroactively to frozen snapshots. For ensemble impulse responses vary capture delay independently of readout time and test stationarity/reset repeatability. No millisecond loop-time or biological specious-present claim follows from readout arithmetic.

The environment's action-to-sensation loop is a real causal loop. Describe it explicitly. The host may not read the fabric and compute helpful sensory injections during primary trials except as the predeclared environment dynamics.

Include an autonomous-fixture mode in the baseline using a small seeded LFSR, pattern sequencer and two coarse stimulus DACs, multiplexed into the two streams. Define action-to-observation rules in Gate A, without computing the agent's inference or policy. Charge it to service/bias allocations, not a presumed 0.05 mm² free addition. Host-independent operation means the host can be disconnected after configuration; the fixture retains its own clock. This is not fully clock-stopped operation, and service-clock-stopped external-stimulus trials remain a separate test. The fixture provides repeatable commands, not deterministic analog state trajectories or entropy. Reset, thermal noise, mismatch drift and near-critical sensitivity must be measured before combining replay trials. Do not call replayed bank captures effectively simultaneous or use them to invent cross-bank single-trial covariance. Log seed/timing and observe switching interference.

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
| Observation, 96-channel holds/selectors, 32 clamps and injection | 1.90 |
| Service logic, write/readback, CRC and baseline fixture sequencer | 0.85 |
| Dedicated inference/control arithmetic reserve | 0.5 |
| Passive coupling coupons and readout integration | 0.15 |
| **Allocated blocks** | **9.10** |
| Global routing, guard rings, isolation, power and margin | **1.40** |
| **Provisional internal envelope** | **10.5** |

At 3.5 mm² for 3,072 edges, each edge gets about 1,139 µm² including storage and local wiring. The documented 43.904 µm² LATQ_X1 cell [9] gives 0.674 mm² bare cell area for 15,360 bits. Use 45% effective storage-placement utilization for the planning screen: about 1.499 mm², leaving about 652 µm² per edge for analog circuitry/local overhead. Sweep 35–60% rather than treating 45% as measured. Effective utilization is an accounting sensitivity, not a requirement to scatter isolated bits: cluster five latches near each receiver and jointly lay out storage and analog circuitry. Do not double-count the same routing whitespace. Shared write/readback is charged separately. These are arithmetic checks, not synthesis or layout results; verify the selected library/voltage variant.

The Section 6 heterogeneous capacitor candidate occupies about 0.1912 mm² of plates including the stated adaptation capacitors, before enclosure/routing. The 96-channel differential hold bank adds 0.096 mm² of plates in its own allocation. Specify the actual Type-B option and include both sides. The node allocation averages about 7,552 µm². The arithmetic reserve is not proof that required products, normalization and action evaluations fit; enumerate and price them. For a single 2 pF capacitor at 300 K, sqrt(kT/C) is about 45 µV, but this is not total continuous-time differential circuit noise. Effective conductance likewise does not determine whole-circuit current without the topology.

The review's instrumentation additions consume margin: 1.40 mm² now covers all global physical overhead and contingency, so fit confidence is lower until extraction. Do not describe these additions as free or claim a 0.35–0.6 mm² hold bank is proven. Build a full representative tile before replicating. Preserve the 10.5 mm² envelope rather than raising it to hide overruns.

Do not book the second review's claimed net area saving. Halving hold count removes 0.096 mm² of plates in the illustrative design, but selection, gain distribution, separate copy residuals, adaptation and baseline fixture overhead still need layout. Keep the observation ceiling and total 9.10 mm² allocation unchanged as conservative reservations until complete block estimates support redistribution. No new scan chain is implied: configuration already uses addressed readback/CRC.

Initial whole-die engineering power target: below 100 mW excluding external loads, not a prediction. Itemize static biases, references, pad loads and measurement switching after circuit design. Verify package thermal behavior and bias drift. No inference from neuron current alone to total die power.

Overrun order: no node expansion, 192-channel bank or active field driver; test three magnitude bits plus sign instead of four plus sign; simplify fixture/service implementation without losing baseline host-independent trials or safe startup/readback/CRC; simplify sensory encoding while preserving the factorial test and primary mechanism tests. Protect the 96-channel capture bank (including the 32-node response set), clamp/cut capability and separate monitor/schema interventions over extra task complexity. Keep a minimal shielded/unshielded pickup set where feasible, but never sacrifice ESD or safety margin. If these requirements cannot fit, explicitly rescope and rerun acceptance rather than silently dropping conditions or claiming node/vocabulary counts guarantee theory satisfaction.

## 12. Development gates

### A — Executable functional specification

Build the explicit agent model, state/edge inventory and held-out task suite. Include adaptation, the 32-node clamp/cut topology, efference-copy paths, calibrated hold-bank errors and the simultaneous-versus-ensemble observation distinction. Register the five same-die controls and check graph feasibility. Demonstrate the primary mechanisms together, derive the inference/control primitive inventory and required measurement precision. Model quantized weights, sparse edges, noise and plausible analog distortions. Stop if the claimed functions require host computation or exceed the resource envelope.

Gate A must additionally produce the identifiability experiments, baseline fixture/timing model, graph-rule checks, 72-cell factorial definition, separate precision/prediction/error paths and an inventory of objectives whose action rankings survive any information-gain approximation. Determine snapshot and trajectory requirements separately. A node allocation is accepted only after these models show the named variables and interventions can coexist.

Deliver: model, fixed configuration, task generator, lesion matrix, numerical results and source-to-state mapping. No tapeout decision from behavioral simulation alone.

### B — Representative circuit feasibility

Implement a node, positive/negative weighted edge with all five configuration bits and a representative addressed write/readback slice, representative nonlinear arithmetic, buffer, perturbation circuit and bias generator. Select analog pads and build the whole-die padframe feasibility floorplan now. Characterize PVT, mismatch, startup, saturation, loading and noise. Layout and extract these primitives early. Exercise capacitor-specific DRC, antenna and extraction rules on real MIM geometry; KianV's digital checks did not qualify these structures.

Deliver: DRC/LVS-clean primitives, extracted models, actual areas and power. Fit reduced behavioral models back to circuit behavior and rerun Gate A.

Gate B priority order: jointly lay out five latches plus addressed access and a binary-weighted signed edge; compare storage-utilization assumptions against that real geometry; then implement a loaded differential hold channel/readout slice and a clamp. Verify worst-case droop, charge injection, aperture/skew, acquisition and buffer kickback before authorizing the full bank. Include adaptation/trim and pickup readout in the extracted tile estimate. A Boolean CRC test does not validate analog capture; separate the evidence.

### C — Representative functional macro

Layout a complete sensory prediction/error motif with its precision control, plus representative observer/schema interfaces and realistic loads. Separately extract an attractor memory and coherent workspace selection/broadcast slice; a sensory macro cannot stand in for these electrically different structures. Include configuration, fixed paths, clamps, capture, guards, bias and real route lengths. Verify coupling and reset. Distinguish modeled statistical variations from distributions the PDK actually supports.

Deliver: extracted functional macros, inventory-derived area budget, corner/mismatch results and a routed whole-chip feasibility floorplan. Do not extrapolate one generic node to every function.

### D — Whole-chip integration

Integrate the inventory-defined functional macros with padframe, power and service logic. Use digital P&R for service logic only; analog macros require full-custom layout and mixed-signal integration. Verify routing, extracted parasitics, antenna, density/fill effects, DRC/LVS/ERC, power integrity, latchup prevention, ESD connectivity and package/board interfaces. Analog-sensitive fill and shielding must be included before final extraction. Check device and capacitor voltages including startup and external-input faults.

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
11. Analog Devices, simultaneous sampling: https://www.analog.com/en/resources/technical-articles/2022/07/16/06/48/adcs-for-simultaneous-sampling.html — simultaneous track/hold acquisition followed by sequential conversion is distinct from multiplexing live inputs.
