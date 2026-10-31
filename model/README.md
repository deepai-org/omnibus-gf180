# Executable component model

Run from repository root:

```sh
python3 -m unittest discover -s tests -v
```

Requires NumPy as specified in requirements.txt. This is an idealized continuous-state reference, not a trained network, circuit simulation, full agent or fit result.

## State and primitive accounting

Each scene specialist has 22 real states: four gated input integrators, five object-quality latents across three grouping hypotheses, three grouping activities, and ten quality-population activities. The one-object hypothesis has one latent, not two. Two specialists plus two persistent error-variance estimates total 46 states. Algebraic signals are not free hardware: products, rectification, min/comparison, normalization, saturating bounds, gain and fanout must all be priced in circuit implementation. State count alone does not prove area feasibility.

The scene is a 2×2 spatial arrangement. Horizontal pairs, vertical pairs and a single object are competing generative hypotheses. Hypothesis errors drive object latents and grouping competition. Group activity feeds back through bounded update gain `1 + 0.25*group_activity`; missing pixels supply no residual. Reconstructions predict missing parts but are not reused as evidence for competing hypotheses. A five-unit compact-support population represents each of two inferred qualities; downstream readout decodes that population, not the original stimulus. Hidden measurements cannot enter input storage. Tests include identical feature histograms with different organization and ambiguous diagonal-only visibility.

A matched-state feedback ablation changes convergence speed but preserves the tested fitted equilibrium. This establishes a dynamical role for that feedback path, **not necessity for eventual grouping accuracy**. Earlier cross-hypothesis completion mixing biased observed qualities toward zero in ambiguous scenes and was removed. Local latent/error recurrence remains even when grouping-gain feedback is disabled; that control is not a wholly feedforward twin.

The quality encoder now uses four shared bounded cubic smoothstep ramps per
quality. Adjacent differences form five units whose activities sum to one
without a normalization divider. At most two units are active; the ideal
mapping is C1 continuous, monotone under the fixed population readout, and has
maximum decoding error below 0.049 on [-1,1]. This replaces the earlier
normalized quartic bumps. It reduces ideal arithmetic obligations, not a
measured silicon area; mismatch and finite-bandwidth transfer realization
remain open (PRIMITIVE_AUDIT.md).

Fractional aperture is modeled as observation gain: `observed` integrates `aperture * scene`, and prediction is compared as `aperture * predicted_scene`. With residual `r`, the evidence cost is proportional to `sum(aperture*r²)` and the latent update projects `aperture²*r` through the hypothesis basis. Perception and observation monitoring use the same gated prediction. This prevents partial opening from being interpreted as a change of object quality or as scene conflict. Tests verify quality recovery at aperture gains 0.5, 0.75 and 1 and zero observer conflict for a correctly predicted attenuated signal. Noise/precision calibration remains a separate unverified issue.

Two slow variance estimates learn squared physically supplied residuals under validity gates. They survive scene reset and set subsequent sensory precision. Tests supply residuals explicitly: an autonomous sensory-reference acquisition mechanism remains missing. Separately, two source-outcome values learn `dV_i/dt = eligible_i*(reward-V_i)/20` from bounded environmental consequences after reporting. They are not relabeled sensory variances. An integrated test delivers negative feedback only after an incorrect report, then resets transient state and freezes learning. The retained values select the other source and produce a correct subsequent answer. Feedback before reporting cannot train. This is a narrow feedback-driven choice demonstration, not general agency or the full active-inference objective.

Time is dimensionless, with default latent/group tau=1 and dt=.025. No mapping to GF180 microseconds has been verified. Targets within a specialist use its pre-step state; reliability feedback updates after both specialists consume the previous precision. Numerical integration is a simulation technique, not a proposed shared clock in the physical agent.

## Remaining integration

The three stored categorical-rule states have explicit restoring recurrence: `dx_i/dt = 4*x_i*(x_i - sum_j x_j²)` on normalized nonnegative activity. A supplied normalized context cue adds `4*(cue_i-x_i)`; removing it removes that term. Products and shared inhibition are circuit obligations, not free simulator storage. Tests recover each category from within-basin perturbation and show that crossing a basin boundary can change memory. No extra dynamic states were added.

The delayed-context test starts with the wrong stored rule, loads a different rule for two normalized time units, removes the cue for delays 0.5, 2 or 8, then presents the same horizontal scene. All three cues at all three delays produce the corresponding correct answer. A context intervention changes the answer without changing first-order grouping. The external `task_enabled` signal gates retrieval/reporting during cue/delay and releases the agent at scene onset; it does not prescribe internal query stages. Stored context continues evolving during this interval. Physical cue routing, retention/noise qualification and the full temporal-task matrix remain unverified; ideal attractors do not prove indefinite fault tolerance.

Outcome-learning tests also reverse which source produces correct answers: after initially learning source 1, negative consequences drive recovery to source 0 within the four tested reversal trials. Restoring a full checkpoint preserves learned source values, feedback ownership, subsequent updates and the next trial's selected source. This is a deterministic two-source test; it does not establish robust exploration or adaptation under arbitrary reward schedules.

`workspace.py` is a nine-state query-control prototype: four competing query activities, three retrieved rule activities, and two comparison activities. Retrieval fills a memory readout; uncertainty demands inspection; supported evidence demands comparison; completed comparison permits reporting. All demand signals depend on current states, with no elapsed-trial counter or service-script stage. Its component fixture reveals ambiguous evidence only in response to inspection. Clear and ambiguous evidence therefore produce different query sequences. The comparison consumes decoded population activity and the retrieved grouping rule, rather than stimulus truth.

Standalone workspace tests use idealized specialist activities. `agent.py` connects both evolving scene circuits through a maintained content bundle. The assembly now has **110 stored dynamic coordinates**: 46 sensory/learning, nine query/retrieval/comparison, two convergence monitors, two inspection requests, 14 attention/actuator coordinates, three context states, 18 observer states, two source-outcome values and 14 content-workspace coordinates. The content workspace replaces the former two-coordinate source selector. Recurrent competition and adaptation permit release; whole-agent switching and reward-credit behavior still need broader validation. `source=0`/`source=1` are interventions, not free competition. Uploaded association weights and optional `context_source` are immutable configuration outside the checkpoint. See WORKSPACE_REWORK.md for current mechanisms, evidence and missing work.

The two unused one-object latent coordinates were removed from storage and checkpoints. Surviving canonical names are unchanged; raw 100-value legacy checkpoints are rejected rather than silently reinterpreted. The convenience hypothesis view `Perception.z` is read-only; interventions use the five stored `latents` or named full-agent checkpoints.

Each stability monitor integrates `clip(1 - drift/0.01, 0, 1)` with tau=1.
Drift is the squared distance between current and target grouping populations
plus the mean squared distance between current and target quality populations
(sum over each population's units, mean over the two qualities). Admission
requires the retained stability above 0.9. These fixed development parameters
are identical across input-noise conditions; no noise amplitude or truth enters
the agent. Unlike the former instantaneous four-residual predicate, this does
not require raw noisy inputs or unused hypothesis latents to reach rest.
The independent observer still checks evidence support; stable hallucination
is not authorized by this monitor alone. Calibration is not established.

Uncertain grouping with incomplete physical apertures independently requests
inspection, even before stability. The fixture maps aperture states into
visibility of missing inputs. An inspection request persists until estimated
completion or stable, confident, observer-admitted evidence. The latter allows
useful partial acquisition to finish despite actuator saturation. Clear scenes
skip inspection; ambiguous scenes recruit it. No
fixture supplies a grouping label or answer. These two retained stability states
are **not a substitute for HOT reality monitoring**.

`attention.py` implements a compressed allocation-estimate/controller candidate. Eight aperture states have heterogeneous time constants; two filtered mean-allocation signals provide physical telemetry. Each stream has two model states: `d estimate/dt = (command-estimate)/1.1 + 8*(telemetry-predicted_telemetry)` and `d predicted_telemetry/dt = (estimate-predicted_telemetry)/0.5`. The command is `clip(desired + 4*(desired-estimate), 0, 1)`. Matching the predicted and measured telemetry delays avoids comparing an instantaneous prediction against delayed evidence. These normalized coefficients are model parameters, not extracted hardware data. Tests perturb plant gain/delay, disconnect feedback and intervene on estimates at fixed plant state.

Run `python3 -m model.compare_attention` for an exploratory nine-condition comparison against direct feedback using the same plant, telemetry, controller gain and command bounds; estimator states continue evolving in the bypass control. The metric is integrated squared allocation error during alternating target demands. The model improves error in five conditions and worsens it in four. At unit plant gain, model/direct errors are 0.2920/0.3653, 0.5317/0.5818 and 1.5972/1.7051 for tau multipliers 0.5, 1 and 3. The largest tested regression is high gain 1.4 and tau 0.5: 0.7543 versus 0.5325. This sweep informed development and is **not held-out validation**. Do not describe the estimator as universally superior or the direct controller as incapable of the task. Untouched conditions, task-consequence predictions and schema-specific behavioral dissociations remain outstanding; an engineering observer alone does not establish AST.

Reporting requires both supported evidence and a comparison consistent with the current bundle. Changed content invalidates an old answer and causes recomparison. Tests cover both source selections, all three grouping types, both quality signs, wrong remembered rules, inspection lesions and evidence-dependent query sequences. They establish a closed perception/query/inspection loop, not all required mechanisms simultaneously. Threshold comparators, memory holds and query competition still require circuit pricing. Cue-loaded rule changes and learned source choice are implemented as described above; arbitrary within-trial source switching remains absent. Synthetic input-noise and scene-change tests are documented in JOINT_EVALUATION.md; physical noise/mismatch remains unqualified.

`Agent(dt=...)` supports timestep refinement across all connected modules. The full-loop numerical test runs clear and ambiguous horizontal scenes for 40 normalized time units at dt=0.025, 0.0125 and 0.00625. All six runs report the correct answer, clear scenes avoid inspection and ambiguous scenes request it. Final-state maximum differences between coarse and fine integration are below 0.02; first-report times span less than 0.5 time units for each case. These are explicit regression tolerances, not proofs of continuous-time convergence or physical stability. Entire trajectories, near-threshold cases, other scene families, noise and mismatch still need broader numerical qualification. Static model coefficients remain unchanged across the timestep sweep.

`observer.py` retains three estimates for each of two streams and three grouping hypotheses: observed support, unobserved prediction strength and disagreement. Visibility-weighted residual energy produces bounded conflict; visible fraction times agreement produces evidence support; prediction energy on unavailable parts produces prediction dependence. Leaky updates use tau=1. Group activity selects a content-bound readout with `reliability = support / (1 + conflict + prediction_dependence)`. This controls precision scale `0.5 + 0.5*reliability` and workspace admission above 0.25. These are declared engineering heuristics, **not calibrated probabilities of external reality**. No latent scene truth enters the observer.

Tests distinguish fixed perceptual content with different evidence support and verify content binding. A joint-agent support clamp blocks reporting without destroying first-order grouping; release restores reporting. The observer is therefore not merely telemetry, but full HOT remains unverified: command-conditioned attribution, temporal binding under source changes, reliability-of-estimate states and held-out confidence calibration are missing. The clamp test demonstrates a causal reporting gate, not by itself metacognitive competence.

The complete higher-order observer, full preference/cost-based action objective and sensory-reference acquisition remain to implement. The outcome-feedback fixture/interface needs physical implementation; it currently provides only consequences, not inferred scene state or policy. Attention-model validation remains partial as described above. Recurrence lesions need matched controls. The current tests do not establish necessity of recurrence or a complete joint-mechanism result. IIT models must come from the resulting agent; no disconnected demonstration is substituted. All primitive area, leakage, noise, retention, mismatch and timing claims require circuit evidence.
# Joint demonstrator entry point

Use `from model.configuration import joint_configured` for the current joint
workspace/context/observer/inspection demonstrator. `joint_configured()` creates
the fixed 110-coordinate model used by the joint-task and partition controls.
The older `configured()` factory remains a historical comparator, not a second
configuration whose best results may be combined with the joint model's.

This model remains incomplete against the full goal: compact complete causal
modeling and justified IIT analysis are unresolved. Passing behavioral controls
is not a consciousness or integrated-information claim. See STATUS.md and
CAUSAL_MODEL_STATUS.md for current evidence and limitations.
