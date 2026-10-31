# Content-bearing workspace rework

Active objective: integrate recurrent content, reciprocal specialist participation,
and a declared causal motif into the agent. The content component now replaces
source selection in the default Agent; reciprocal specialist integration remains
incomplete. The integrated model passes the existing 72-case composition grid
(maximum report time 14.175 normalized units). This is not the requested new
cross-specialist task, and does not establish distributed ignition.
Analog development remains paused.

## Current shared configuration

`model/configuration.py` is now the sole factory for the primary contextual task,
ignition/persistence sweep, free competition and return-replay demonstrations.
It starts with uniform context, unforced source selection, context source 1,
context-prior gain 0.04, and the fixed 0.85-context/0.15-content association tensor.
Stimulus preparation and declared lesions differ; immutable weights do not.
Reduced-equation tests use the corresponding `configured_transition` wrapper.
Legacy component/ablation configurations remain explicitly separate.

Rerunning persistence on this shared configuration gives 0.500 units intact and
0.175 with all returns cut. Matched replay still has exactly zero nominal state
error; a full content perturbation gives 0.150 live versus 0.500 replay, with
maximum state divergence 0.4224. Individual cuts give sensory 0.175, observer
0.425, memory 0.500. Memory's continuous state effect is nonzero (maximum
difference 0.0217) despite unchanged thresholded duration. Earlier 0.775-unit
figures below describe older preparation/configuration and must not be combined
with current task results as a single-design claim. Tests now require the actual
aggregate shortening and individual state effects, not an unjustified fixed
ratio or a claim that every individual cut shortens thresholded duration.

The hardware target is a configurable physical recurrent fabric. A suitable
uploaded weight/configuration set may supply the demonstrated architecture;
power-on discovery or hardwiring this particular workload is not required.
Nevertheless, hardware capability must be supported by a realizable configuration,
not inferred merely from programmability. One simultaneous configuration remains
the target; separate theory-specific demonstrations are not a substitute.

## Complete initial motif

`model/content_workspace.py` has 14 stored scalar coordinates:

| State | Count | Role |
|---|---:|---|
| Candidate activity a | 2 | Recurrent excitation and mutual competition |
| Candidate grouping g | 6 | Two three-way grouping populations |
| Candidate qualities z | 4 | Two object qualities per candidate |
| Adaptation h | 2 | Activity-dependent release |

Three-way grouping populations are normalized, so 14 stored coordinates are
not 14 independently intervenable unconstrained variables. Interventions must
respect their simplex. We retain all coordinates instead of claiming a smaller
causal model while hiding content state. The approximate 6–10-state suggestion
was not a license to omit payload or adaptation.

Declared boundary inputs per candidate: evidence strength E, availability v,
grouping target G, two quality targets Z, and signed content-specific specialist
feedback F. All must eventually come from actual agent states, not fixture truth.
In Agent, F currently measures agreement between local grouping and maintained
grouping. Evidence is biased by learned source values; availability comes from
physical visibility. These are agent signals, not ground-truth scene labels.
Current Agent gains are self=0.8 and specialist-return=0.65; standalone component
defaults remain the historical 1.2/0.25 for isolated comparison. These are explicit
immutable component parameters, not hidden state. Independent-equation tests
exercise both configurations. The equation block below shows the historical
component-default coefficients; substitute the Agent gains for integrated trials.
The selected candidate supplies a graded, centered grouping prior to its sensory
specialist: `0.01*a_selected*(g_selected - 1/3)`. Local agreement returns to
candidate activity. The observer adds `0.2*v*(support-conflict)` to that feedback,
clipped to [-1,1]. These coefficients describe the current uploaded-configuration
candidate, not theory constants. No additional retained state is introduced.
Independent sensory-feedback and observer-feedback lesion switches preserve
the remaining dynamics and do not directly disable reporting.
The selected sensory prior can include the centered retrieved association,
`context_prior_gain*contrast*a_selected*(memory - sum(memory)/3)`, where
`contrast = clip(4*mean((observed_pattern-mean(observed_pattern))²),0,1)`.
This measured contrast factor prevents a contextual orientation prior from
inventing segmentation in uniform evidence. The uploaded gain
defaults to zero and is 0.04 in the contextual-ambiguity candidate.
`context_feedback=False` removes
only this predictive return; it does not disable retrieval, inspection or reporting.
Context and selected content now address an uploaded 3×3×3 association tensor.
Each context/content pair supplies a normalized three-way rule. The existing
three retained `workspace.memory` coordinates hold the retrieved result; no new
dynamic coordinates are hidden in the association component. Memory readiness
requires both sufficient activity and agreement with the currently addressed
rule, so a changed address initiates retrieval rather than reusing stale content.
Retrieved-rule agreement returns to candidate activity with coefficient 0.1;
the `memory_feedback` lesion removes only this return path. Default weights
preserve the old fixed-context rule task; nontrivial uploaded mappings are tested
separately. Their necessity in a cross-stream task remains unproven.

```text
t_i = clip(2*(v_i*E_i + 0.25*F_i + 1.2*a_i
              - 1.2*a_other - 0.9*h_i - 0.45), 0, 1)
da_i/dt = (t_i-a_i)/0.5
dg_i/dt = v_i*a_i*(G_i-g_i)/0.5
dz_i/dt = v_i*a_i*(Z_i-z_i)/0.5
dh_i/dt = (a_i-h_i)/8
```

All update targets use pre-step state. Readout returns one candidate's coherent
group/quality bundle; validity requires activity >0.7 and a >0.2 margin over the
competitor. This readout threshold is not itself the proposed ignition mechanism.
Recurrence is inside the activity dynamics. Content is retained when unavailable;
adaptation releases its active broadcast even though inactive payload storage
remains. Exact ties do not qualify as a valid winner.

## Initial component evidence

Four tests cover weak-input nonbroadcast, strong-input content acquisition,
short persistence after input removal followed by release, recurrence ablation,
and switching to a competing input. These establish only a component starting
point, not distributed ignition, GNWT compliance or positive integrated information.
Numerical coefficients are development choices, not accepted theory constants.

Integrated intervention tests show that a conflicting maintained payload changes
the answer without replacing local sensory evidence, that a content prior changes
ambiguous local grouping while leaving the other specialist unchanged on that
step, and that observer conflict reduces workspace activation relative to its
return-path lesion. These are causal path checks, not evidence that every path
is necessary for the proposed cross-specialist task. The report-gate lesion is
explicitly only a gate check and cannot substitute for broadcast-disruption
experiments on reciprocal interactions.

## Remaining implementation sequence

### Content-dependent association configuration

The unforced contextual candidate now uses a single uploaded tensor,
`0.85*context_association + 0.15*content_association`, for all conditions. It
preserves all 16 contextual/conflict successes while making selected content
affect retrieved rule and retrieval demand. The default tensor lacked that
feedback dependency despite accepting a content address. Numerical intervention
tests distinguish the two configurations. The reduced block graph correspondingly
joins the four-coordinate memory/retrieval component to the ten-coordinate
activity/adaptation/local-grouping component. This is a structural change in
configured connectivity, not an added state block or a positive IIT result.
See CAUSAL_MODEL_STATUS.md for the upstream-boundary limitations.

### Analytical reduction rather than arbitrary coordinate selection

`experiments/reduced_persistence.py` now provides a 35-coordinate sufficient
statistic for shuttered persistence. It preserves the ten payload coordinates,
and explicitly retains local grouping, context, retrieval, observer return and
observation contrast alongside competition/adaptation. It replaces the larger
observer and input states by algebraically closed summaries, not binary bins.
The earlier 31-coordinate version used content-weighted observer summaries;
those were adequate for trajectories but overlapped the content variable under
intervention. Six per-hypothesis evidence-minus-conflict coordinates replace
the two weighted summaries, so independent content interventions no longer
redefine observer state. All eight return-cut combinations and randomized
content/clamp interventions commute with reduction in the tested cases.
The transition matches 400 full-agent steps and 100 randomized one-step tests,
including unforced selection and varied association weights. See
CAUSAL_MODEL_STATUS.md for the exact mode assumptions and derivation. This makes
the causal model more manageable but does not yet supply IIT coarse-graining,
partition/exclusion results or an acquisition-mode model.

### Selective broadcast-disruption control

`experiments/selective_broadcast.py` uses the same unforced contextual agent and
fully exposed object inputs for both ambiguous and clear conditions. Cutting
the outgoing sensory prior (`sensory_feedback=False`, historically labeled
`sensory_return` by this fixture) leaves local sensory updates, inbound agreement,
retrieval and report predicates intact. It must not be confused with the newer
Agent `sensory_return` argument, which cuts inbound agreement.

Across 32 trials, ambiguous context/sign cases go from 4/4 correct reports intact
to 0/4 reports with the prior cut. Clear local controls—including contradictory
and uniform scenes—remain 12/12 correct in both arms. A regression test also
checks preserved correct local grouping in a contradictory clear-scene control.
Thus this is a selective deficit with physical sensory information matched,
not a global report-disable effect or an inability to inspect. These remain
development cases, not held-out generalization, and they are not an IIT metric.

### Boundary closure evidence

The current-model screen in `experiments/workspace_closure.py` evaluates nested
14-, 17-, 35- and 79-coordinate candidate boundaries. All have omitted-state
witnesses that change next-step included state while candidate state and future
inputs are identical. In particular, adding sensory and observer states does
not eliminate dependence on the stored context and query machinery. See
CAUSAL_MODEL_STATUS.md for magnitudes and semantics. No Phi is computed from
these failed autonomous boundaries. This is a concrete remaining architectural
gap, not merely an expensive solver run: a compact complete motif or a justified
conditional/coarse-grained interpretation is still required.

A sufficient phase-restricted boundary is now implemented in
`experiments/withdrawn_core.py`: 83 retained coordinates include the omitted
context and retrieval activity that defeated the smaller candidates. Under
fully closed physical input shutters and fixed experiment parameters, all 27
remaining coordinates can vary without changing the projected dynamics in the
screened trials. Repeated projected transitions exactly match the full-agent
trajectory. CAUSAL_MODEL_STATUS.md records the mode-specific dependency argument.
This is not a minimum-size result, does not cover acquisition, and is not yet
an appropriately coarse-grained IIT model.

### Unforced competition and acquisition

`python3 -m experiments.free_competition` presents a strong scene on either
stream against a weak competitor, then reverses amplitudes within the same
trial without resetting state or forcing ownership. Initial selection occurs
at 0.85 units; reversal at 2.525 (0→1) and 2.45 (1→0). No step has both
activities >0.7 in these runs. Selected grouping follows the new source rather
than copying the old winner's payload. These are two controlled stimulus
sequences, not exhaustive competition or reward-credit verification.

The contextual ambiguity/conflict experiment now also uses unforced selection.
Its fixture explicitly enables only the physically presented stream and closes
both during the blank delay. Removing forced ownership initially exposed a
deadlock: no visible evidence on the hidden new source could overcome the old
winner, so the new input was never inspected. Local acquisition now requests
inspection for each physically enabled under-covered stream without requiring
it to win global competition first. This uses existing inspection-request states;
it does not introduce a timer, label input or source-selection override. The
inspection lesion disables this local request as well as query-driven inspection.
All 16 contextual/conflict cases pass with this unforced configuration.

### Matched open-loop return control

`python3 -m experiments.return_replay` records 160 post-withdrawal return vectors
from a live agent, then replays those exact vectors through an external edge
intervention. Nominal replay matches all 110 state coordinates exactly. Both arms
have the same input sequence and immutable configuration. Replaying is an
experimental intervention, not part of autonomous operation or a hidden memory
inside the proposed fabric.

After identical preparation, swap the selected candidate's horizontal/vertical
group coordinates (a valid simplex intervention) in both live and replay arms.
The replay remains the **unperturbed** record; it is not regenerated to fit the
perturbed recipient. Live feedback shortens active time from 0.775 to 0.15 units;
replay stays at 0.775. Maximum state divergence is 0.6441. This separates responsive
feedback from matched nominal stimulation. Local trajectories are identical
before intervention, not forced to remain identical after it. It is an open-loop
edge replacement, not an IIT noising/minimum-information partition, and does not
establish exclusion. A null perturbation gives exactly zero divergence. Swapping
10%, 25%, 50% and 100% of grouping mass gives live active times 0.600, 0.300,
0.150 and 0.150; nominal replay remains 0.775 in every case. This is a declared
development sweep, not selected only for the full-swap effect. Individual
return lesions are now enumerated below; task-level matched-replay conditions
and IIT-defined partitions remain.

`python3 -m experiments.individual_returns` evaluates all eight subsets of three
inbound specialist pathways from the same prepared state. Active durations are:
intact 0.775; sensory cut 0.200; observer cut 0.700; memory cut 0.700;
sensory+observer cut 0.175; sensory+memory cut 0.175; observer+memory cut 0.625;
all three cut 0.175. Outgoing broadcasts, local state updates and external inputs
are unchanged. Thus sensory return dominates this preparation, while observer
and memory each make a smaller nonzero contribution. This does not show each
path is indispensable for every task or every operating point. The new
`sensory_return` switch cuts the inbound agreement term; `sensory_feedback` cuts
the outgoing sensory prior. They are deliberately separate interventions.

### Integrated strength/duration check

Current persistence revision: specialist return signals are weighted by retained
candidate activity, not by external input availability. Shuttering a stimulus
therefore removes feedforward evidence without also severing endogenous loops.
Local self-reinforcement is reduced from 1.2 to 0.8, and return gain increases
from 0.25 to 0.65. No new state or report predicate is added. `recurrent_returns`
cuts only the aggregate return to candidate activity; specialist local dynamics
and outgoing workspace priors remain enabled.

After the same strong four-unit exposure, intact and cut runs have identical
pre-intervention state. Intact activation persists 0.775 units after withdrawal;
cutting returns at withdrawal reduces this to 0.175. Both release by the end of
the 20-unit observation. Repeating with dt=0.0125 instead of 0.025 gives the same
two durations; retained grouping differs by less than 0.001. The contextual
16-case grid remains correct. This establishes a return-path contribution to
persistence, not necessity of every individual specialist or an IIT quantity.
It is a zero-return lesion, not an activity-matched/noised IIT partition.

The previous measurements below used the earlier gains and input-gated returns.

`python3 -m experiments.agent_ignition` now drives the actual agent at amplitudes
0, 0.02, 0.2 and 0.7 for durations 0.25, 1 and 4, followed by 20 units of physical
withdrawal. `input_enabled` is an external two-stream shutter; inspection cannot
reopen it. Initially, even zero input reached activity 0.9997 after four units:
the supposedly sensory evidence drive depended only on preference/availability.

The evidence drive is now multiplied by
`clip(4*mean(abs(observed_sensory_state)),0,1)` per stream. Learned preference is
still a bias, not stimulus evidence by itself. Acquisition can be requested
before broadcast when coverage is inadequate, so sensory evidence can be
obtained without requiring a pre-existing ignited workspace. This introduces no
new retained coordinates. Two direct feedback-intervention tests now start at
activity 0.5 rather than below the limiter, keeping their intervention point
within a responsive range after removal of the constant drive.

In the updated sweep, zero and 0.02 inputs never activate the workspace. A 0.7
pulse lasting 0.25 peaks at 0.058; lasting four units reaches 0.9995 with retained
horizontal grouping 0.954, remains active for 0.525 units after withdrawal, then
releases. At amplitude 0.2, one unit peaks at 0.0013 while four units reach 0.994.
These are integrated activation/content observations, not yet evidence that every
specialist retains a shared interpretation or that ignition is collective rather
than dominated by local reinforcement. The shorter one-unit strong pulse remains
active longer after removal (3.25 units) because adaptation has accumulated less;
duration effects are not monotonically stronger persistence. No report occurs
within these brief exposures. The 16-case contextual/conflict grid still passes.

### Cross-stream task evidence

Current fixed contextual-configuration check: `python3 -m experiments.context_conflict`
runs four ambiguous-context/sign cases plus twelve fully exposed clear-scene
controls, including context contradictions and uniform one-object scenes. All
16 report correctly. Before contrast gating, four uniform-scene controls timed
out because the prior opposed the simpler one-object hypothesis. That failure
motivated the contrast-dependent prediction, not per-case coefficient changes.

Reporting now additionally requires measured observation coverage >0.75;
insufficient coverage requests inspection regardless of current grouping
confidence. This prevents a confident interpretation of missing evidence from
bypassing acquisition. The criterion uses actual aperture-adjusted visibility,
not the inspection command, and still allows a reduced-gain actuator to complete
when adequate evidence is available. It is an explicit task-level evidence
criterion, not a consciousness-theory constant.

The earlier four-case timings and 2/4 lesion score below predate these two
changes and must not be cited as current measurements.

The saturation and gain-regime measurements below describe the revision before
the context-to-sensory predictive return was added; they remain useful negative
development evidence, not measurements of the latest full configuration.

`python3 -m experiments.context_ambiguity` adds a balanced four-condition task.
A perceived horizontal/vertical context cue is retained across a blank delay.
The object has off-diagonal contrast `[0, ±0.7, ∓0.7, 0]`, which has equally good
horizontal and vertical fits with opposite first-object qualities. Context
specifies the grouping convention; sensory contrast specifies the quality sign.
Neither alone determines the answer. Inspection exposes the contrast but cannot
remove the grouping ambiguity. One fixed prior coefficient (0.04) is used in
all conditions; these are development, not held-out, cases.

Important configuration boundary: enabling this prior unconditionally in the
older fixed-rule matching task failed three acquisition-lesion regressions.
There, the remembered rule specifies a question, not a reliable perceptual cue;
using it as evidence can produce an unjustified answer without inspection.
The prior is therefore an explicit immutable uploaded weight, zero in that
legacy workload and 0.04 throughout the new workload. This is a capability
demonstration, **not yet** one jointly validated configuration satisfying the
entire objective. Do not combine successes from these settings into a claim of
simultaneous theory satisfaction. The final joint configuration and task semantics
remain to be resolved and tested.

With context return, 4/4 cases are correct at 15.525 normalized units. Removing
the context or entire sensory return gives 2/4 (always false, no inspection).
Inspection lesions prevent reporting in all four. A matched-input control exposes
all object pixels from the start: intact horizontal/positive reports correctly at
11.35 units; context-return lesion remains at grouping `[0.5,0.5,0]` and cannot
report by 40 units. The latter isolates contextual disambiguation from the
acquisition effect. No report predicate checks whether the return path is enabled.
This establishes a useful context→sensory→maintained-content loop, not necessity
of every return path, distributed ignition, or an IIT result.

`python3 -m experiments.cross_stream` runs 18 fixed-configuration cases:
three perceived context cues × three object groupings × two quality signs.
The context is presented spatially to specialist 1 for 15 normalized units,
removed for a two-unit blank delay, then specialist 0 receives a diagonally
occluded object. Context labels never enter Agent inputs: the cue specialist's
settled grouping drives the existing recurrent context population. Context source
is an immutable configuration parameter, not additional dynamic state. Object
source is forced to 0 in this experiment; this does not test free competition.

All 18 cases report correctly, with maximum object-phase latency 14.175 units.
The same object under different retained contexts produces different answers.
For a positive horizontal-match case, removing the context acquisition path
preserves local cue perception but produces the wrong answer; removing inspection
prevents reporting within 40 units. However, separately removing sensory,
observer or memory return paths leaves that case correct at the same 13.9-unit
latency. This negative result means the task does **not yet** demonstrate the
requested necessity of reciprocal interactions. Do not count the goal complete
on this evidence. The answer distribution is imbalanced (only three positive
cases), so aggregate accuracy alone is particularly weak evidence.

The next task/design revision must expose genuinely ambiguous evidence and
content competition where specialist return influences matter, without merely
adding a report gate that fails whenever a pathway is disabled.

### Why the return lesions currently fail to matter

`python3 -m experiments.workspace_drive` instruments the actual inputs to the
workspace update without changing them. In the positive horizontal-match case,
all 529 active object-phase steps have an upper-clipped activation target, both
intact and under each of the three return lesions. Intact pre-clipping drive
ranges from 2.043 to 2.605 against an upper bound of 1. Feedback itself ranges
from -0.536 to 1. Thus variable specialist influence is present but erased by
the activation limiter during this active phase. This explains the zero latency
effect in this case; it is not a proof about all possible operating points.

The excessive fixed feedforward drive plus strong local self-recurrence must be
rebalanced toward specialist-supported amplification. Simply increasing return
weights or adding a lesion-sensitive report predicate would not establish the
desired distributed mechanism. Preserve controlled release, weak-input locality
and strong-input persistence when revising these dynamics.

`python3 -m experiments.workspace_regimes` compares the existing activation
coefficients (self, return, adaptation) = (1.2,0.25,0.9) with fixed candidates
(0.8,0.5,0.3) and (0.9,0.5,0.45). Each is applied to a complete trial, with no
per-condition coefficient changes. Three task conditions (positive match,
positive mismatch, negative match), each intact and with three separate return
lesions, yield 36 runs. All report the correct answer at 13.9 units. Neither
candidate demonstrates the required dependence; neither is promoted to Agent.
The baseline experimental update independently matches 100 randomized valid
implementation updates. These are development comparisons, not held-out results.

This rejects these two simple gain rebalances as sufficient fixes. The task's
inspection reveals evidence that local inference can resolve alone, and the
constant workspace evidence drive remains strong. The next architectural/task
change must make returned content resolve or sustain a genuinely ambiguous
interpretation; do not keep tuning solely until an arbitrary lesion causes a
timeout. Persistence and strength/duration checks are still required before
promoting any revised regime.

### Explicit causal equations

`experiments/content_dynamics.py` independently implements all 14 coordinates,
with grouping-simplex constraints and all boundary inputs explicit. It matches
500 randomized valid one-step interventions to numerical precision. An explicit
competition-edge cut changes activity while preserving same-step payload and
adaptation updates. That intervention is **not** an IIT partition calculation.
Changing supplied specialist feedback changes the next state at fixed internal
state: the component is input-conditioned, not causally closed. Candidate subset,
partition and coarse-graining analysis must preserve this distinction.

`experiments/content_boundary.py` enumerates the conditional dependency graph:
with specialist inputs clamped, activity/adaptation form a four-coordinate
strongly connected component; payload coordinates have no return path to it
inside that boundary. Grouping simplex constraints remain in force. These graph
components are not IIT complexes. A content-bearing intrinsic analysis must
include the specialist loop closures or explicitly justify a different boundary;
an activity-only score cannot stand in for the whole workspace.

### Remaining steps

1. Add state restoration/intervention support and independent causal equations;
   characterize strength/duration dependence and sensitivity to timestep.
2. Replacement of source selection is implemented: learned preferences are an
   input, and query/comparison consume maintained grouping and qualities.
   Validate selection changes and credit ownership across longer agent trials.
3. Connect content-specific sensory priors, memory association, observer
   evaluation and attention/action, with explicit return influences. Keep local
   inference distinct from workspace content; do not replace all states with
   copies of the winner. Sensory, observer and associative-memory paths now have
   direct intervention tests; task-level necessity and path accounting remain.
4. Build the cross-specialist task: contextual cue, ambiguous object, remembered
   association, and requested missing evidence must jointly determine the answer.
   Suppress/wrong-content broadcast and matched partition interventions must
   selectively impair this behavior while preserving local competence.
5. Analyze the actual connected motif under declared boundary and intervention
   semantics, including partition/subset alternatives. Do not threshold an
   arbitrary subset or search unreported settings for a favorable IIT score.

Current inventory: replacing two existing selection states with the
14-state motif changes 98 stored coordinates to 110, before any additional
consumer/association state. This is arithmetic, not a fit or route estimate.
The eventual feedback boundary includes specialist memory; the isolated motif
must not be presented as autonomous while F and other inputs evolve externally.
# Task necessity audit: inbound returns

## 94-state decoded-quality candidate

`experiments.decoded_agent.configured` is a structural candidate, not a silent
change to the 110-state joint factory. It redesigns acquisition stability to
measure decoded-quality drift, then exactly reduces each specialist's ten
filtered quality-population states to two decoded states. All other retained
state, query control, recurrence and observation loops remain. The corresponding
unreduced redesigned reference is `experiments.decoded_stability.configured`.

`python3 -m experiments.decoded_agent_audit` reproduces the eight-condition joint
lesion pattern: intact coherent success 4/4; retrieved-context prior, workspace
prior, inspection and sensory-persistence cuts each 0/4; bypassed observer
context admission yields two accidental negative answers but no correct context
or interpretation; separate observer/memory persistence cuts retain 4/4.
Bidirectional switching remains correct with no simultaneous high winners;
reversal takes 3.000–3.025 units. Strong-pulse persistence remains 0.500 units
intact versus 0.175 with aggregate returns cut, followed by complete release.
Three reduced-agent regression tests pass, including randomized projected
equivalence, signed checkpoint restoration and intact/context-cut task behavior.

The lower count is an actual model-state reduction (94 versus 110), not a
proven silicon area saving or an IIT result. Clear-perception controls, the full
parameter-bound acquisition contract and partition experiments still need
explicit verification for this candidate before replacing the joint reference.

Follow-up controls now verify clear perception and the acquisition boundary:
the reduced candidate's fully exposed ambiguity test changes 4/4→0/4 after the
outgoing sensory-prior cut, while clear-local interpretation and answers remain
12/12 in both arms. Incoming-feedback replay matches all 94 coordinates exactly;
the content perturbation still distinguishes live and replayed responses
(maximum state difference 0.42369249; activity durations 0.150 versus 0.500).
The generalized acquisition contract accepts the reduced factory explicitly,
accounts for 90 changing coordinates plus four fixed learning parameters, and
rejects silently mixing it with the original contract. Three reduced-contract
tests cover 100 varied-input reconstruction steps, boundary mismatch rejection
and nominal replay. Bidirectional partition verification remains outstanding
for the reduced implementation.

Bidirectional acquisition partitions are now verified for the reduced candidate
as well. `acquisition_partition.evaluate(factory=decoded_agent.configured)`
matches all 94 nominal states exactly at the content, content+memory and
content+memory+observer boundaries. Perturbations cannot propagate across the
replayed boundary; live opposite-side effects reach 0.98307918. A stronger
regression compares the reduced cut trajectory with the projected trajectory of
the unreduced **decoded-stability** reference for all three boundaries, matching
within 1e-12 over 30 steps. Two tests pass. This verifies compatibility of the
reduction with these declared interventions, not with every possible partition
or IIT noising scheme; the population-shape reference is not the comparator.

## One-task interaction audit with distractor

### Numerical-step check of the joint candidate

`python3 -m experiments.candidate_timestep` repeats the four distractor task
cases and both switching directions with dt=0.025 and 0.0125. Cue duration
remains 15 units, blank delay 2, task timeout 40, and switching phase duration
20; fixtures now derive iteration counts and latency from the actual dt rather
than assuming 0.025. No weights, gains or behavioral thresholds change.

Both timesteps give 4/4 correct task answers. Latencies are 14.850/15.100 units
at dt=0.025 versus 14.875/15.125 at dt=0.0125. Both switching orders retain
correct final winners and zero simultaneous-high steps. Reversal delays change
from 3.000/3.025 to 2.9875/3.0375 units. This is a two-resolution robustness
check, not proof of continuous-time convergence or analog noise tolerance.

### Matched physical-input and replay controls

`selective_broadcast.evaluate(factory=reliability_competition.configured,
distractor=True)` exposes every object pixel in both arms. With this same
candidate, ambiguous-context answers change from 4/4 intact to 0/4 after cutting
the outgoing sensory prior; clear-local answers **and local group identification**
remain 12/12 correct in both arms. Thus the deficit is not a blanket loss of
perception, missing pixels, or a directly disabled report gate.

`return_replay.evaluate(factory=reliability_competition.configured)` also follows
the same configuration. Open-loop nominal replay matches all 110 coordinates
exactly over 160 steps. An identical content perturbation then produces a
0.42369249 maximum live/replayed state difference; live perturbed activity lasts
0.150 units versus 0.500 with the unperturbed feedback replay. This is an
activity-matched nominal control for reciprocal causation, not IIT partition
noising. The independent 35-coordinate closed-shutter equations match this
candidate's prepared trajectory to 1e-12 over 160 steps; this is not an
acquisition-mode reduction or proof of a finite categorical IIT substrate.

`python3 -m experiments.joint_distractor` evaluates the same conflict-weighted,
observer-admitted candidate across four balanced context/contrast conditions.
No per-condition weights or source overrides change. Correct interpretation,
retained context and selected source are checked in addition to the answer.

| Removed interaction | Correct answers / 4 | Reports / 4 | Correct interpretations / 4 | Correct retained context / 4 |
|---|---:|---:|---:|---:|
| None | 4 | 4 | 4 | 4 |
| Retrieved context → sensory prior | 0 | 0 | 0 | 4 |
| Workspace → sensory priors | 0 | 0 | 0 | 4 |
| Inspection | 0 | 0 | 0 | 4 |
| Observer → context-write admission | 2 | 4 | 0 | 0 |
| Sensory → workspace persistence | 0 | 0 | 0 | 4 |
| Observer → workspace recruitment/persistence | 4 | 4 | 4 | 4 |
| Memory → workspace persistence | 4 | 4 | 4 | 4 |

This establishes necessary interactions among context memory, sensory inference,
workspace, observer and inspection **within one task/configuration**, not by
combining independent best-case demonstrations. The two correct answers after
context-admission removal are accidental negatives, not coherent reasoning.
The memory-to-sensory return is task-essential; the parallel direct memory-to-
activity return is not. Likewise observer context protection is necessary here,
while its activity return has its separate competition evidence. Do not claim
every individual return edge is necessary, or that these lesions are matched
IIT partitions. The complete causal-model and integration-analysis requirements
remain open, as does the fixed early-withdrawal completion gap.

## Conflict-weighted recruitment candidate

### Observer-protected context acquisition

The candidate now also requires content-indexed observer admission before a
visible context-source interpretation can update stored context. Stability and
confidence alone were insufficient: a checkerboard distractor produced a stable
but unsupported one-object interpretation that overwrote the earlier cue.
This admission gate adds no stored state. It is active only in the experimental
reliability-selection configuration; the baseline is unchanged.

The contextual task now optionally presents that distractor on the former cue
stream while the object is inspected. The candidate solves all four cases and
retains the correct context (14.850–15.100 units). The existing observer-to-
workspace return cut leaves all four correct, because it does not cut context
admission. A separately named `context_admission` lesion bypasses that gate;
the horizontal/positive case then corrupts context to one-object and answers
incorrectly. Tests check retained context and interpreted grouping, not just
answer accuracy, since an incorrect internal interpretation can accidentally
produce the correct negative answer.

This demonstrates a useful observer-to-context-memory role within the reasoning
task. It does not establish necessity of the distinct memory-to-workspace
persistence return. Historical candidate timings below precede this added gate
and require rechecking before joint adoption.

Joint-control audit (`python3 -m experiments.conflict_candidate_audit`): the same
candidate passes 12/12 clear context/scene/contrast cases, including contradictory
context, and switches in both directions without a reset or simultaneous high
winners. Initial selection is 0.875 units; reversal is 3.000–3.025 units.
Zero/weak inputs do not ignite; a short strong pulse remains below ignition.
A long strong pulse retains activity for 0.500 units, versus 0.175 with all
returns cut after identical preparation, then releases completely.

However, all four fixed-14.5-unit withdrawn-input cases fail to produce their
first answer (all have zero prior reports). This is worse than the baseline's
2/4 completion at that same cutoff. The candidate strengthens observer-guided
selection but is not yet a uniformly better joint configuration. Keep the cutoff
and report this tradeoff; do not combine its observer result with the baseline's
withdrawal result as if one configuration achieved both.

A new equal-strength competition probe exposes the baseline's observer problem:
it recognizes the checkerboard input as unsupported but can stay locked onto
it when it occupies tie-advantaged source 0. The existing activity-weighted
return cannot reliably recruit a suppressed supported alternative.

The candidate in `experiments.reliability_competition.configured` scales sensory
recruitment by `1 - 0.5 * local_claim_conflict`, using the observer's retained
content-indexed conflict state. The observer-return lesion disables both this
new recruitment influence and the existing persistence return. The fixture never
supplies a correct-source label. There is no added state; the baseline factory
still leaves this candidate option disabled pending broader joint validation.

The candidate selects the supported scene in either position; removing the
observer return restores erroneous source-0 selection when source 1 is supported.
The same candidate configuration also solves all four ambiguous-context cases
(14.825–15.050 units). An earlier confidence-proportional recruitment version
failed all four: uncertainty prevented the workspace recruitment needed to
resolve uncertainty. It was replaced, not retained as another option.

This is evidence of a useful observer-to-selection role, plus compatibility with
the context task. It does not yet demonstrate all specialist returns necessary
in one reasoning task, validate the new configuration's withdrawal/switching
behavior, or establish an IIT substrate. Baseline closed-shutter reduced dynamics
are unchanged because external recruitment is zero when shutters are closed.

## Memory-return semantics experiment (not adopted)

The existing return scores scene/rule category similarity. This is not generally
retrieval correctness: an uploaded association can legitimately map horizontal
content to a vertical rule. `Association.retrieval_support` provides a stateless
alternative: for each candidate address, score retained mass minus L1 distance
from the corresponding mass-scaled addressed rule. Empty memory gives zero;
correct nonidentity retrieval gives positive support; stale incompatible rules
can inhibit. Four unit tests cover this distinction, scaling, empty memory and
explicit configuration with unchanged 110-coordinate state count.

`python3 -m experiments.address_return` uses that return circuit throughout the
same fixed-withdrawal task. It still completes only 2/4 cases, now at 0.15 units
after withdrawal, and all return-cut arms also complete those two. No prior
reports occur. Thus semantic consistency alone does not establish useful
reciprocal dependence. The candidate is **not** the shared baseline or an added
normative silicon block. Baseline reduced equations/tests still apply only to
the default content-match circuit. A useful next memory workload must distinguish
correctly addressed retrieval from stale or irrelevant associations, rather than
rewarding a larger generic persistence signal.

## Retained-evidence report capability

### Timing alternatives screened, not adopted

`python3 -m experiments.retention_timing` applies each timing pair for the entire
cue/acquisition/withdrawal trial, never just after withdrawal. The fixture stays
at 14.5 units and all four cases have zero preceding reports.

| Activity τ | Observer τ | Intact correct / 4 | Sensory-cut correct / 4 | All-return-cut correct / 4 |
|---:|---:|---:|---:|---:|
| 0.5 | 1 | 2 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 |
| 0.5 | 2 | 2 | 2 | 2 |
| 1 | 2 | 0 | 0 | 0 |

No candidate improves joint task success and reciprocal dependence. The
baseline remains activity τ=0.5, observer τ=1. Timing is now explicit in the
component constructors for controlled experiments; no additional dynamic state
is introduced. The independently checked reduced dynamics still describe the
baseline constants only. Changing a component's timing requires reconstructing
that experimental configuration; the normal Agent reset restores its defaults.

Implementation correction from the full regression: acquisition stability is
gated by **physical visibility**, not workspace eligibility. A forced workspace
selection must not prevent the other specialist from acquiring evidence/context.
The first full run after stability holding passed 146/147 tests and exposed this
distinction in the legacy cross-stream task. After correcting the mask, all
three cross-stream tests pass; a direct regression additionally requires visible
stream 1 to acquire stable evidence while its workspace activity is forced off.
This fix does not alter the unforced shared configuration's equations.

**Current partial improvement:** acquisition stability now updates only while
the corresponding physical input is available. Without observations, local
sensory relaxation cannot overwrite that historical stability trace. Report
permission still expires through observer evidence decay and workspace release;
holding stability is not an indefinitely valid answer certificate. This changes
no state count, feedback gain, task cutoff or scoring deadline.

At the same 14.5-unit cutoff, the horizontal/negative and vertical/positive
cases now produce their first correct answer 0.2 units after withdrawal.
Cutting the sensory return or all returns prevents both completions. The other
two cases still fail intact; observer-only and memory-only return cuts do not
prevent the successful cases. Thus post-withdrawal computation is demonstrated
for two cases, not the full task, and the reciprocal-role requirement remains
open. Regression tests also require report permission to expire while the
historical stability trace remains held.

**Historical follow-up before this change:** `python3 -m experiments.withdrawn_task` withdraws
the ambiguous object at a fixed 14.5 units, before any answer in all four
context/contrast cases. All five matched branches (intact, each return cut,
aggregate cut) produce zero reports over the following two units. In the intact
horizontal/negative case, stability falls from 0.972 at 0.025 after withdrawal
to 0.814 at 0.2; answer-query activity rises only to 0.878 at 0.1 before
declining. Workspace activity reaches 0.768 at 0.2 and 0.509 at 0.4. Thus
answer retention below must not be described as demonstrated post-withdrawal
completion. Stability handling and persistence/computation timescales need
joint design work; moving the fixture cutoff later would hide this gap.

The report support gate no longer categorically requires present visibility.
With a physically closed input, it may use the existing content-indexed observer
admission criterion (support divided by one plus conflict and prediction
dependence, greater than 0.25). It still requires stable support, a valid selected
broadcast, ready memory, comparison and query state. Partial visibility does not
qualify for this exception. No new retained state or fixture-provided truth label
is introduced; observer evidence decays when observations cease.

`tests/test_retained_evidence.py` prepares the shared agent through the physical
context/inspection task, then closes the shutter. A report survives initial
withdrawal but ceases within the tested two-unit interval. Removing observer
evidence prevents reporting despite the otherwise acquired state; partial
visibility with inspection closed also prevents reporting. This demonstrates a
prerequisite for delayed-evidence tasks, not that each inbound persistence path
is necessary. The task necessity audit below remains an unresolved requirement.

`python3 -m experiments.task_returns` tests the shared configuration on all four
context/contrast combinations. Preparation, physical evidence and outgoing
broadcast are unchanged. Only specified inbound persistence terms are removed
during the object phase; specialists retain their other functions.

| Inbound cut | Correct / 4 | Report latency (model units) |
|---|---:|---:|
| None | 4 | 14.700–14.975 |
| Sensory | 4 | 29.975 |
| Observer | 4 | 14.700–14.975 |
| Memory | 4 | 14.675–14.925 |
| All three | 4 | 28.525–28.875 |

This is **not** evidence that all reciprocal interactions are task-essential.
The sensory return accelerates completion, but continuous stimulus availability
lets the agent finish without any of these persistence returns. Observer and
memory return terms have little effect on this task's answers/latency, despite
their measurable continuous-state effects in withdrawal experiments. Inbound
cuts here are distinct from the existing outgoing sensory-prior/context lesions,
which prevent ambiguous interpretation.

The task-essential reciprocity requirement remains open. A next discriminating
workload should require retaining evidence across actual unavailable-input
intervals and choosing between conflicting interpretations using reliability
and context. It must preserve clear-evidence controls and use the same uploaded
configuration. Merely shortening the scoring deadline until lesions fail would
not establish that the missing interactions perform the intended computation.
