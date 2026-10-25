# OMNIBUS-GF180: one-die multi-theory experimental agent

Date: 2026-10-25. Status: pre-schematic research architecture.

## 1. Objective and claim boundary

Build one wafer.space GF180MCU 1x1 die that performs a small but meaningful perceptual-control task using physically instantiated recurrent perception, global access, higher-order monitoring, an attention model, and predictive control together.

Optimize for the number of **substantive, independently testable mechanisms that operate concurrently**, not the number of theory names attached to blocks. No claim that this device is conscious, that all variants of a theory are satisfied, or that a minimum size for consciousness is known.

The principal deliverable is a causal-intervention laboratory with a working autonomous agent. A collection of disconnected demonstration circuits does not meet the objective.

The baseline is 192 continuous-time state nodes and 3,072 dedicated directed weighted edges. A 256-node/4,096-edge variant is a stretch option only after extracted layout and behavioral evidence justify it. These are engineering allocations, not scientific thresholds. Functional feasibility must precede schematic commitment. Failure to fit or function is a result to report, not a reason to relabel a simpler mechanism as compliant.

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
| CEMI | Optional endogenous field-mediated feedback | Separate field effects from conducted interference and show behavioral contribution | Field-feedback experiment only |
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

Initial target local time scales: 10–100 microseconds, subject to extracted characterization. Implement delayed context and workspace persistence through continuously powered recurrent attractors, not passive charge retention for 10 milliseconds. Long adaptation constants are optional and excluded from the baseline functional dependency. Prefer rescaling task timing to requiring extremely small leak currents. Specify a nominal maximum of 2 pF total intentional state capacitance per node, counting both differential sides and any adaptation capacitor; increases require an area review. This is a design limit to test, not a claim that 2 pF suffices. Verify memory stability and reset across noise, mismatch and PVT.

Each edge has static 4-bit magnitude plus sign, with zero weight providing a lesion: 15,360 weight bits before node controls and test state. Baseline storage uses characterized standard-cell latches with addressed writes, not an unqualified custom SRAM cell or a transparent-latch shift chain. A shared five-bit configuration bus and hierarchical tile/edge decoder update one edge while quiescent. Decoder outputs must be glitch-free during latch enable; define data setup/hold, write strobes, readback selection and reset/run interlocks. Count the decoder, bus buffers, readback muxes and local storage placement explicitly. A custom storage cell is an optional later optimization, not required for fit. No refresh or serial computation of synaptic currents during operation.

Weights are configured while the fabric is held in a known quiescent state. Gate analog bias/current paths off until all configuration has been written and checked by readback; ordinary unreset latches must never power up into an active arbitrary network. A hardware run lock blocks writes during primary autonomous trials. Diagnostic intervention mode is separate and explicitly logged. No nonvolatile memory is required: a host loads the configuration after power-up. Brownout or loss of configuration validity forces quiescence and requires reload.

The GF180 documentation lists multiple MIM densities [4]; only use the capacitor option supplied by the selected shuttle. Bias generators, reset switches, startup, ESD loading, guard rings and supply filtering are part of the design, not later additions.

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

## 9. IIT, criticality and field experiments

### IIT

Reserve a reconfigurable 4–8-node subset of the main network for clamping, intervention and exhaustive small-state model studies. It participates in the primary agent normally; isolating it creates a different experimental condition.

Estimate intervention-based transition models at declared discretizations and sampling intervals. Check approximate Markov behavior and sensitivity to hidden state. Exact calculations on these reduced models are not exact measurements of whole-chip consciousness or proof that the full fabric is the maximal complex. Include configuration, adaptation, support electronics and environmental feedback in causal-boundary discussions.

Do not claim minimum cut, perturbational complexity, recurrence or bidirectionality equals integrated information. No 10,000-channel cut requirement.

### Criticality

Expose leak/gain/adaptation controls. Sweep stable, oscillatory and high-variability regimes and measure impulse responses, correlations and finite-size effects. Avalanche fits alone are insufficient [5]. The useful agent need not operate exactly at a critical point. Do not require complexity to decrease monotonically with every perturbation.

No active digital homeostat in the baseline autonomous mode. Any future servo that changes gain is part of the causal system regardless of its speed.

### Optional field experiment

Not populated in the baseline. Only add a field experiment if the primary agent passes its tests and extracted whole-chip layout retains margin after a maximum 0.3 mm² allocation. A dedicated source electrode driven by aggregate fabric activity, capacitive pickup electrodes and threshold modulation may test endogenous electric-field feedback. Include grounded shields, disconnected pickups, matched conducted injection and supply/substrate monitors.

This is a localized coupling experiment, not a promised realization of CEMI. Quantify whether any effect exceeds ordinary supply/substrate crosstalk. Default disabled; enabling it must not destabilize the primary agent. Drop it first if physical margin is inadequate. Do not use floating-gate programming or exotic process assumptions.

## 10. Observation, interventions and causal boundary

- Buffered analog monitors, with measured loading and reverse coupling; no fictional perfectly one-way transistor buffer.
- Per-node threshold observation with simultaneous capture into a 192-bit snapshot, shifted out later. Sampling does not imply the agent itself is clocked. Asynchronous threshold transitions can produce uncertain captured bits; characterize the aperture and readout settling rather than assuming an exact coherent analog-state snapshot.
- Six selectable buffered analog outputs, one per tile, for external simultaneous waveform acquisition. Do not expose raw integration nodes to pad or cable loads.
- Local programmable perturbation injection, state reset and edge lesions. Choose targets before a trial; explicitly identify interventions during a trial.
- An external event trigger and capture clock support repeatable timing. Repeat-trial waveform reconstruction does not establish simultaneous continuous observability of every state.
- Characterize acquisition-clock feedthrough, probe loading and aliasing. Repeat key behavioral tests with observation disabled and service clock stopped.

The environment's action-to-sensation loop is a real causal loop. Describe it explicitly. The host may not read the fabric and compute helpful sensory injections during primary trials except as the predeclared environment dynamics.

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
| 192 nodes including integration/adaptation capacitors | 1.3 |
| 3,072 edges, sign/magnitude storage and local routing | 3.2 |
| Bias, references, reset and distribution | 0.7 |
| Observation, capture and injection | 1.2 |
| Service digital logic, write/readback and configuration distribution | 0.8 |
| Dedicated inference/control arithmetic reserve | 0.5 |
| Field experiment (baseline omitted) | 0.0 |
| **Allocated blocks** | **7.7** |
| Global routing, guard rings, isolation, power and margin | **2.8** |
| **Provisional internal envelope** | **10.5** |

At 3.2 mm² for 3,072 edges, each edge gets about 1,042 µm² including storage and local wiring. The documented 43.904 µm² LATQ_X1 cell [9] gives 0.674 mm² bare cell area for 15,360 bits, or about 1.124 mm² with an assumed 60% placement utilization. That leaves approximately 676 µm² per edge for analog circuitry/local overhead inside this allocation; shared write/readback circuitry is charged to the separate service budget. These are arithmetic checks, not a synthesis or layout result. Verify the chosen library/voltage variant before using this cell.

At 2 fF/µm², 192 × 2 pF requires 0.192 mm² of capacitor plates before enclosure, routing and matching overhead. Specify the actual Type-B option and include both differential sides. The node allocation averages about 6,771 µm². The separate arithmetic reserve is not proof that the required products, normalization and action evaluations fit; Gate A must enumerate them and Gate B must price them.

Initial whole-die engineering power target: below 100 mW excluding external loads, not a prediction. Itemize static biases, references, pad loads and measurement switching after circuit design. Verify package thermal behavior and bias drift. No inference from neuron current alone to total die power.

If over budget: simplify service logic without losing safe startup/readback, reduce weight resolution if behavioral tests permit, and revise the task/network explicitly. Never silently remove required monitoring or schema functions. Any reduction reruns the complete simultaneous acceptance suite. If no variant fits, report the one-slot objective unmet. Expansion to 256 nodes/4,096 edges is allowed only after a complete candidate floorplan, extracted tile areas and the shared behavioral suite establish that the expansion fits the same internal envelope with margin; it is not the baseline.

## 12. Development gates

### A — Executable functional specification

Build the explicit agent model, state/edge inventory and held-out task suite. Demonstrate the primary mechanisms together, and derive the inference/control primitive inventory. Model quantized weights, sparse edges, noise and plausible analog distortions. Stop if the claimed functions require host computation or exceed the resource envelope.

Deliver: model, fixed configuration, task generator, lesion matrix, numerical results and source-to-state mapping. No tapeout decision from behavioral simulation alone.

### B — Representative circuit feasibility

Implement a node, positive/negative weighted edge with all five configuration bits and a representative addressed write/readback slice, representative nonlinear arithmetic, buffer, perturbation circuit and bias generator. Select analog pads and build the whole-die padframe feasibility floorplan now. Characterize PVT, mismatch, startup, saturation, loading and noise. Layout and extract these primitives early. Exercise capacitor-specific DRC, antenna and extraction rules on real MIM geometry; KianV's digital checks did not qualify these structures.

Deliver: DRC/LVS-clean primitives, extracted models, actual areas and power. Fit reduced behavioral models back to circuit behavior and rerun Gate A.

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

Keep trials bounded and resettable. Review substantive evidence before extending persistent memory, prolonged adverse-state conditioning or autonomous learning. Publish configuration hashes, causal boundaries and null/control results so architecture claims can be independently checked.

## 14. Main unresolved risks and next action

1. The proposed small network may not genuinely implement all functions simultaneously. Gate A is the first priority.
2. Predictive/action arithmetic may need more dedicated circuits than a generic node model suggests.
3. Five-bit static edge storage, routing and isolation may dominate area.
4. Analog mismatch may destroy calibrated confidence and model-based control; training with measured variability may help but is not guaranteed.
5. Useful observation may perturb the very dynamics being measured.
6. Whole-chip IIT maximality and full CEMI compliance remain outside promised deliverables at any proposed node count.

Immediate next work: write the 192-state functional model and shared task/lesion suite, while specifying a complete representative node/edge/configuration circuit and the analog padframe for an early extracted-area check. Do not start by building a large generic crossbar or by asserting theory compliance from block names.

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
