# Agent-derived causal model screening

Target theory: **IIT 4.0 (2023)**, as identified in REQUIREMENTS_LEDGER.md. This artifact contains boundary/coarse-graining tests and conditional-model **system integrated information φₛ** calculations using pinned PyPhi. It does not calculate structure integrated information Φ, certify a complex, or substitute graph connectivity/prediction accuracy for integration.

**Current status:** the agent has 110 stored coordinates and a revised recurrent
content workspace. No justified IIT calculation for that current substrate has
been completed. See WORKSPACE_REWORK.md for input-conditioned equations,
boundary dependencies, matched replay and individual return-path experiments.
Those experiments measure causal effects, not integrated information.

The primary demonstrations now share `model/configuration.py`, including
unforced selection and content-dependent association weights. Current intact
persistence is 0.500 units; aggregate return cut is 0.175; perturbed live/replay
is 0.150/0.500. Earlier 0.775 values in developmental reports refer to the prior
configuration. The reduced transition's explicit configured wrapper follows the
same factory parameters; generic parameterized equations remain available for
declared comparisons.

## Current workspace boundary falsification

### Bidirectional state-boundary replay

`python3 -m experiments.bidirectional_replay` compares three declared boundaries:
content (14 coordinates), content plus retrieved memory (17), and those plus
the full observer (35). For a boundary A|B and a recorded intact trajectory r,
the split transition is explicitly `F_A(x_A,r_B), F_B(r_A,x_B)`. Each side keeps
its own evolving retained state; cross-boundary state inputs are supplied from
the **unperturbed** recording. External inputs and uploaded parameters match.

All three controls match every nominal state exactly across 80 closed-shutter
steps. With an identical content-group perturbation, the live opposite side
changes by up to 0.78536124; the replayed opposite side is unchanged. A separate
observer-conflict intervention verifies blockage in the other direction for the
content boundary. Two tests cover nominal agreement, the three boundaries and
both propagation directions. Equal maximum effects do not rank these boundaries
or identify a preferred subsystem.

This improves on incoming-only return replay by actually disconnecting both
directions at the discrete state-transition boundary. It is still an externally
driven control: nominal matching is by construction, not evidence of an
autonomous factorization. It is not IIT's noising/partition distribution, and
these state-level substitutions have not been mapped to physical edge switches.
No Phi or exclusion claim is inferred. Justified integration analysis remains
outstanding.

The same two-way substitutions are now tested during acquisition by
`python3 -m experiments.acquisition_partition`: after the physical cue and delay,
the candidate has processed the ambiguous object plus checkerboard distractor
for 10 units. At that point, a content-group perturbation is applied and the
network evolves for four more units with the same externally supplied scene,
base visibility and input enables. Endogenous aperture dynamics are retained.
All three nominal replay partitions match exactly; the perturbation's opposite-
side effect is zero under replay and reaches 0.99357918 in the live agent.
This extends the matched causal control to the actual reasoning phase, rather
than assuming the shuttered reduction applies there. The equal maxima do not
rank partitions, measure information, or imply an answer-level effect of that
magnitude. The acquisition test and two shuttered replay tests pass.

### Complete acquisition reference contract

#### Constructive decoded-state redesign

An explicit redesign candidate now removes the whole-agent obstacle: use
decoded-quality drift rather than full population-shape drift in the stability
detector. The unreduced reference is `experiments.decoded_stability.configured`;
the actual reduced implementation is `experiments.decoded_agent.configured`,
with **94 retained coordinates** instead of 110. Each specialist stores two
decoded qualities, not ten population activities. Any population returned to
existing readout interfaces is an algebraic endpoint representation, not hidden
retained state or an estimate of uncertainty.

A 400-step randomized whole-agent comparison, initialized with arbitrary quality
populations, matches the projected unreduced **redesigned** reference within
1e-12, including report/query outputs. Checkpoint tests preserve signed qualities
and account for all 94 names/coordinates. This is not equivalence to the old
population-shape detector: the redesign must retain its own joint validation.
The reduced candidate solves all four contextual distractor cases at the same
14.075–14.325-unit latencies as its unreduced redesigned reference. The main
110-state joint demonstrator and its acquisition contract are unchanged.

`experiments.decoded_perception` reduces each sensory specialist from 22 to 14
continuous coordinates while exactly preserving input/latent/group dynamics and
the two decoded quality outputs. Because all five quality channels share one
linear first-order filter and downstream decoding is linear, their decoded
values obey a closed two-state update. The nonlinear `decode(encode(target))`
transfer is retained; it is not approximated as identity. A 500-step randomized
stimulus/mask/precision/prior test agrees within 1e-14, starting from arbitrary
normalized quality populations.

This local reduction alone does **not** remove 16 states from the original Agent. Its acquisition-stability
detector measures population-shape distance to a target. A second test constructs
identical decoded qualities with different population shapes and demonstrates
different stability errors. Whole-agent reduction therefore requires either
retaining the relevant shape information or explicitly redesigning and jointly
validating that detector. No state has been silently dropped from the joint
demonstrator or acquisition contract.

Projection now also checks the declared instance-level parameter boundary:
association weights, selection/context policies, sensory time constants and
gains, content/observer parameters, attention actuator parameters and component
timesteps. Equal dynamic state is not sufficient if these differ. Regression
tests change selection policy, content return gain, observer time constant and
attention gain without changing any state coordinate and require rejection.
This check binds the explicit parameters, not arbitrary monkeypatched Python
code; equation constants still require the same source revision.

`experiments.acquisition_contract` defines the intact joint candidate's full
continuous trial boundary. Of 110 stored coordinates, 106 are explicitly carried
between transitions. Two variance coordinates remain fixed at 0.25 and two
source-value coordinates at 0.5: learning-valid gates are zero and no reward is
supplied. Projection rejects changed values instead of silently dropping them.
The complete coordinate inventory is available through `inventory()`.

Every varying external input is named: two four-sample scenes, base visibility,
two physical input enables and Boolean task availability. The fixed uploaded
configuration, dt=0.025 and intact intervention settings are part of the contract.
No truth labels, remembered context labels, trial index or hidden stage are
inputs. Tests compare 200 sequential randomly varied input steps bit-for-bit
against the live agent and execute a full cue/delay/inspection/distractor trial
through state reconstruction at every step.

This is deliberately **not** an independent equation implementation or a compact
causal motif: it invokes Agent and exposes its state/input boundary. It supplies
an authoritative reference for testing smaller acquisition reductions. It does
not by itself validate a categorical TPM, justify a partition intervention,
or satisfy the original small-complete-motif goal. Prior 35-coordinate results
remain limited to the shuttered phase.

### Acquisition-phase counterexample in the joint candidate

`python3 -m experiments.acquisition_boundary` constructs two valid states of
`reliability_competition.configured` with identical 35-coordinate projections.
Observer evidence/conflict pairs are respectively (0.5, 0.25) and (0.75, 0.5),
so every stored difference is exactly 0.25. All other full-agent coordinates,
parameters and future inputs match. The test uses a declared state intervention,
not a claim that both states arise naturally on a nominal trial.

With shutters closed their projected successors agree within 2.8e-17. With
stream 0 visible, next activity differs by 0.00751: conflict-weighted recruitment
depends on conflict itself, not only evidence minus conflict. This falsifies an
acquisition-mode use of the existing 35-coordinate reduction while preserving
its intended closed-shutter scope. An acquisition model must retain separate
observer evidence/conflict information (or another proven sufficient statistic)
and separately account for prediction dependence, sensory inference state and
attention dynamics. Adding six observer coordinates alone is not asserted to
complete that model. The small conditional persistence model cannot stand in
for the substrate performing the entire reasoning task.

### Population-preserving intervention screen

#### Explicit stochastic intervention ensemble

**This stationary label-only model is rejected.** In addition to conditional
output dependence below, `python3 -m experiments.population_temporal` finds that
all four declared probe labels have one-step self-transition probability 1,
but direct twenty-step self-transition probability 0. Repeated application of
the same one-step kernel would remain at the initial label forever; direct
evolution has disjoint support after twenty steps (TV distance 1). The same
256-member initial ensembles are used at both horizons. This is an exact
counterexample for this proposed stationary model, not a general rejection of
stochastic or explicitly time-dependent causal models.

The omitted within-label evolution and evolving background cannot be replaced
by reinitializing the intervention ensemble at every step. No further Phi
calculation should use this eight-unit kernel as if it were the current agent's
closed Markov substrate. A replacement needs retained causal state or a
separately validated grain/intervention policy; the negative tests remain as
regressions against reviving this shortcut. One temporal regression passes.

`python3 -m experiments.population_kernel` defines an independent near/far
realization choice for each of eight population units, giving 256 equiprobable
valid initial microstates per declared input label. This removes the earlier
all-near/all-far screen's shared realization choice. The background is prepared
with the joint candidate, all 35 reduced coordinates evolve, and labels are read
only at the 20-step endpoint. This ensemble is an experimental definition, not
an assumed physical noise process or proven stationary within-bin distribution.

Four declared input labels produce respectively 4, 8, 10 and 6 distinct output
labels. Total-variation distance between each measured joint output row and the
product of its output marginals is respectively 0, 0.1015625, 0.015625 and 0.
These are exact enumerations of the declared 256-state ensembles, not Monte
Carlo uncertainty. Two tests check the metric against known independent and
correlated distributions and validate the intervention realization count.

The installed solver's substrate uses per-unit factored transition probabilities;
its source explicitly checks conditional independence on joint-form input.
Therefore simply passing marginal probabilities for these correlated rows would
discard observed dependence. This is not an IIT result or a proof that no other
grain works. It identifies another unresolved obligation: a justified boundary,
unit definition and intervention distribution that preserve the dependencies
needed by the chosen formalism. Zero discrepancy in two rows does not validate
the full transition table or Markov closure.

`experiments.population_alphabet` defines eight candidate units: two activity,
two adaptation, two local interpretation populations, retrieved memory and
retrieval drive. The interpretation/memory units have H/V/G/unresolved labels;
the other units are binary. All 2,048 combinations have two valid continuous
realizations that round-trip through the full agent. These are interventions,
not validated dynamical macro-units. The other 21 coordinates of the exact
35-coordinate closed-shutter reduction remain explicit background and evolve.

`python3 -m experiments.population_grain` exhaustively compares those two
realizations from the same prepared shared-configuration background. Successor
labels agree after one step (0.025 units), but disagree for 1,536/2,048 initial
labels after 20 steps (0.5 units). Each local interpretation differs in 1,024
rows; activity 0 differs in 32 rows. Thus this label scheme fails exact
deterministic closure at the longer sampling interval. One-step agreement is
not proof of closure over all within-label realizations or backgrounds.

This does not rule out a declared stochastic intervention model, another grain,
or integrated information in the physical system. It rules out treating this
convenient categorical table as an exact autonomous substrate. Any subsequent
IIT calculation must specify its intervention distribution, boundary treatment
and sampling interval, and test sensitivity to those choices; no positive IIT
claim follows from the present screen.

`python3 -m experiments.workspace_closure` starts from the actual post-stimulus
agent and compares four declared candidates: content alone (14 coordinates),
content plus retrieved memory (17), plus observer (35), plus both full sensory
circuits (79). For each candidate, valid omitted-state interventions leave all
included coordinates identical; parameters and future external inputs also match.
All four fail deterministic autonomous closure, with next-step witnesses.

For the 14-coordinate boundary, changing omitted local grouping changes next
activity by 0.05; observer conflict and retrieved memory change it by 0.00420
and 0.00438. Even the 79-coordinate boundary depends on omitted stored context
and query activity: retrieved memory changes by 0.000392 and 0.001497 next step.
Over one normalized unit the corresponding maximum differences reach 0.438
and 0.0212. The tested precision intervention has no effect during this shuttered
phase; that is not evidence of irrelevance during sensory acquisition.

This rejects *autonomous* transition models on these subsets, not all possible
conditional IIT analyses. Explicitly fixing omitted dependencies would define
a different, conditional intervention model whose limitations must accompany
any result. We have not demonstrated an adequate coarse-graining or excluded
larger candidates. Consequently, do not turn these subsets into binary TPMs and
interpret a resulting score as intrinsic integration of the entire workspace.
The implemented complete reference remains the 110-coordinate agent with its
external inputs and immutable configuration declared. A compact complete
content-bearing motif, justified coarse-graining and IIT partition/subset
evaluation remain unfinished architectural work.

### Sufficient boundary for the shuttered phase

`experiments/withdrawn_core.py` defines an 83-coordinate projected transition:
content 14 + both sensory circuits 44 + observer 18 + retrieved memory 3 +
stored context 3 + retrieval-query activity 1. It is **not** claimed minimal.
The fixed parameters are those of the persistence experiment; both physical
input enables are zero, task enabled, and no reward, cue or learning feedback
is supplied. This does not cover acquisition or reporting.

Dependency argument: the zero enables make visibility zero regardless of all
actuator states. Sensory evidence costs and latent error drives consequently
lose their precision dependence. Workspace feedforward evidence is multiplied
by zero availability, eliminating outcome-value dependence. Supported evidence
is false, so the retrieve-query target depends only on retained memory and its
addressed rule; inspection/comparison/answer activity cannot feed that target.
Memory updates use only the retained retrieval activity. Other query states and
attention can evolve, but their outputs cannot cross the closed input shutters.
Sensory/observer/content/context updates use coordinates retained in this set.
This eliminates the 27 omitted coordinates in this **mode**, not globally.

At the prepared persistence state, randomizing all 27 omitted coordinates in
100 valid trials over 20 steps gives exactly zero projected divergence. A pure
83-coordinate transition, reconstructing omitted coordinates canonically at
each step, matches 160 successive full-agent transitions exactly. These checks
support the dependency argument; they do not prove an arbitrary smaller or
binary coarse-graining valid. Normalized populations remain constrained, and
83 continuous coordinates do not provide a tractable exhaustive binary IIT
model merely by thresholding. A smaller content-bearing causal motif and/or
justified coarse-graining remains required for the intended IIT evaluation.

### Exact 35-coordinate sufficient-statistic reduction

`experiments/reduced_persistence.py` analytically reduces the same shuttered mode
to 35 coordinates without thresholding. It retains activity/adaptation (4),
the frozen content payload (10), local grouping populations (6), observer
evidence-minus-conflict coordinates (6), retrieved memory (3), stored context (3), retrieval query (1),
and observed spatial variance (2). Normalized populations remain constrained.

The observer coordinates are `evidence-conflict` per hypothesis and source.
With zero visibility, evidence and conflict targets both vanish, so each
difference decays exactly by `(1-dt)`. An earlier 31-coordinate version retained
only the content-weighted sums; it matched trajectories but a content intervention
also redefined those observer summaries. The current six differences remove that
overlap: changing content does not change the observer coordinates. Observed samples all decay by the same
input factor, so their spatial variance updates exactly by `(1-dt/0.5)^2`.
That variance supplies the contrast-dependent prior; the sample means and
individual samples are not otherwise needed by these closed-shutter equations.
Sensory latent error drives vanish; their remaining effects on quality and
prediction-dependence state do not feed the retained equations in this mode.

The independently written transition matches 400 full-agent steps to 1e-12,
and matches 100 randomized valid one-step interventions, including unforced
selection and nontrivial uploaded association tensors. This is an exact
sufficient-statistic reduction under the stated equations/mode, supported by
the algebra and numerical tests—not a claim of global minimality or of an
acquisition-mode reduction. It retains content rather than silently treating it
as a fixed experiment parameter. No binary TPM or Phi is inferred from it.

Intervention checks additionally compare every subset of the three return-path
cuts over 100 steps, and 100 content/intervention-clamp cases. Reduction and
full-agent intervention agree to 1e-12. Five reduced-model tests pass, including
an explicit check that content intervention leaves observer coordinates intact.
These cover named interventions; they do not establish every IIT-required
macro-intervention distribution or partition/noising semantics.

The reduction now includes a constructive `lift(state, agent)` for admissible
35-coordinate interventions. Grouping/context changes preserve their simplexes;
observer difference d is realized by evidence=max(d,0), conflict=max(-d,0);
variance v in [0,1] is realized by a zero-mean ±sqrt(v) spatial pattern. Retained
activity, payload, memory and retrieval states are written explicitly. Inputs
are validated before mutation. This is a declared realization, not an IIT
maximum-entropy intervention measure.

One hundred randomized admissible reduced states round-trip through this lift
and project back, and their next transitions agree with the reduced equations.
Alternative micro-realizations add common-mode observer activity and permute
the spatial samples while preserving reduced coordinates. One hundred such
pairs agree through ten subsequent steps to 1e-12. Thus the tested reduction
does not depend on those arbitrary choices of observer split or spatial pattern
in the shuttered mode. It still does not specify a finite alphabet, sampling
measure, IIT partition operator or exclusion search.

### Population-preserving structural decomposition

`experiments/reduced_graph.py` keeps normalized grouping/memory populations as
whole blocks. With unforced selection and the default content-independent
association tensor, the reduced equations have a 10-coordinate recurrent
activity/adaptation/local-grouping component and a separate four-coordinate
memory/retrieval component. The latter drives the former but receives no
selected-content return through that default tensor. Payload, observer difference,
variance and stored context are separate upstream/frozen blocks in this mode.

The contextual candidate now uploads one fixed association tensor across its
entire task grid: `0.85*context_association + 0.15*content_association`. Changing
selected content therefore changes the retrieved rule and retrieval demand.
A numerical intervention test verifies those dependencies; they disappear with
the default tensor. This joins memory/retrieval with the main recurrent component
into 14 coordinates at the structural-block level. All 16 contextual/conflict
cases and the four contextual regression tests pass with the new tensor.
No dynamic state was added. These are structural SCCs, not IIT complexes,
and they still have declared upstream context/bias dependencies. In particular,
a larger SCC does not establish positive integrated information or exclusion.

### Binary-grain rejection on current activity/adaptation state

`python3 -m experiments.workspace_grain` explicitly tests the tempting four
activity/adaptation coordinates at threshold 0.5. For each of all 16 bit states,
it compares continuous interventions at 0.1/0.9 and 0.4/0.6, with identical
omitted-state initialization and future shuttered inputs. Both representatives
belong to the same starting bins. Binary successors differ in 0/16 rows after
one step, 2/16 after 20 steps, and 12/16 after 80 steps (0.025, 0.5 and 2 units).
The one-step agreement is not proof of a valid grain: the selected representatives
are far enough from threshold that little can change over one short step.

For example, initial bits `[1,0,0,0]` remain `[1,0,0,0]` at 0.5 units from
0.1/0.9 representatives, but become `[0,0,0,0]` from 0.4/0.6 representatives.
This falsifies an exact deterministic binary transition model at those longer
lags. A stochastic macro-model would require a declared within-bin intervention
distribution, background treatment, and checks of history/Markov dependence;
averaging these two tables is not that justification. The test does not claim
that no useful coarse-graining exists, nor that this content-free four-coordinate
subset meets the original objective. No Phi is reported from the rejected model.

**Historical rerun:** source-hashed transition tables and per-analysis results
are saved in [evidence/iit](evidence/iit/README.md): 374 defined results, all zero,
and 1,034 undefined attempts. Their source hashes describe older implementations;
they are not current-agent results and must not be cited as such.

**Historical revision boundary:** the numerical results below precede the independent
missing-evidence acquisition request in `Agent.step`. That change alters causal
trajectories. These are retained historical negative results, not verified
numbers for the revised agent. They are retained for comparison; the linked
rerun supersedes them without changing the boundary-validity caveats below.

Run the screening machinery on the present source (this does not reproduce the
older hash-bound results or establish a justified boundary):

```sh
python3 -m model.causal
python3 -m unittest discover -s tests -v
```

## Actual-agent intervention model

The historical 98-state agent used in this screening exposed canonical state names and a validated checkpoint restore (the first screening preceded outcome-learning/selection and pruning of two unused latent coordinates). Restoring all dynamic state reproduced subsequent deterministic evolution exactly in the tested context. Immutable parameters, any forced-source override, timestep and future environmental inputs must also match; these are not secretly included in the dynamic checkpoint. The current agent rejects older-length checkpoints. Recompute tables after architecture changes rather than assuming earlier values remain invariant.

The candidate contains four actual agent coordinates, selected for their named perception/monitoring/control roles, not for a favorable Phi result:

- First object-quality latent of stream 0's horizontal grouping hypothesis.
- Observer evidence-support estimate for that hypothesis.
- Stream 0's estimated aperture allocation.
- Stream 0's desired inspection state.

The environment presents the horizontal scene `(0.73, -0.61)` to both streams with initial diagonal-only visibility. After 200 integration steps, intervene on all 16 binary combinations using low/high values 0.1/0.9 and threshold 0.5. All unselected states start from the checkpoint and evolve normally; they are **not clamped, averaged away or excluded from the actual causal paths**. Record outputs after 20 and 80 steps, durations 0.5 and 2 in normalized units.

The resulting tables are deterministic, conditional finite-horizon maps. They are not automatically valid autonomous four-element transition probability models. The extraction intentionally does not enforce conditional independence or infer a stochastic process from one trajectory.

## Sensitivity results

The background intervention changes the omitted second quality latent of the same hypothesis to 0.9, leaving the four candidate initial coordinates unchanged. The within-bin control uses low/high values 0.4/0.6, retaining identical binary intervention labels.

| Duration | Background: changed binary rows / 16 | Within-bin: changed binary rows / 16 |
|---|---:|---:|
| 0.5 | 0 | 0 |
| 2.0 | 10 | 10 |

With the aperture-consistent observation model, duration 0.5 has a maximum continuous-output difference of 0.21849 under the background change. At duration 2, that difference reaches 0.66809. An unchanged thresholded table at a short interval therefore does not establish independence from omitted states.

These findings reject treating this table as a background-independent, bin-independent model of the entire agent. They do **not** reject IIT, prove zero integration, or prohibit an explicitly background-conditioned subsystem analysis. IIT analysis must specify how outside elements are treated and whether the chosen grain is admissible; those choices cannot be silently supplied by a simulator default.

## Required next evidence

### Implemented boundary-closure checks

`python3 -m unittest discover -s tests -p test_attention_boundary.py -v`
now tests the actual implemented attention component and its agent connection.
It establishes a specific limitation of the four-coordinate reduction:

- Telemetry integrates the mean of **four** physical aperture states. Changing
  omitted aperture 1 while holding all four candidate coordinates identical
  changes the next telemetry value by `dt/0.5 * delta_aperture/4`. This is a
  direct omitted cause, not merely a long-horizon statistical discrepancy.
- Mean aperture cannot replace those four states without additional dynamics.
  With equal means but aperture values `[.8,.2,.2,.2]` versus `[.2,.2,.2,.8]`,
  identical commands give a next-mean difference
  `-0.025*0.6*(1/0.8-1/1.4)/4 = -0.00200893`. The actuator time constants differ,
  so the next mean depends on how activity is distributed. Treating the mean as
  one independently intervenable Markov state would hide that information.
- The seven-state stream component (four apertures plus telemetry, estimate and
  predicted telemetry) exactly reproduces 100 agent updates when supplied the
  same desired-command trajectory. Altering the other stream does not affect
  this result. This is an input-conditioned reproduction, not intrinsic closure.
- Identical seven-state checkpoints evolve differently under different desired
  commands. That input must be explicitly conditioned/noised under a declared
  theory-compatible boundary, or its generating state and causes included.
  Adding the desired-inspection state alone would still leave its workspace
  query drive outside the boundary.

The seven-state input-conditioned component is therefore a defensible next
**modeling boundary to investigate**, not a demonstrated IIT complex or a claim
that seven states are sufficient for the whole agent. No positive integration
score is inferred. A binary reduction still requires an intervention ensemble,
bin-closure tests and appropriate treatment of the endogenous command. These
tests change no agent equations, so the source hashes in evidence/iit remain
valid. This concrete closure failure takes priority over another unqualified
four-coordinate parameter sweep.

1. Specify the IIT 4.0 boundary, external conditioning/noising and macrostate intervention distribution, including omitted internal memory and environmental feedback.
2. Compare candidate boundaries and temporal grains drawn from the actual coupled agent. Declare the selection rule before selecting favorable scores; preserve adverse cases.
3. Validate any Markov/conditional-independence approximation, or use an appropriate enlarged state representation rather than hiding dependent channels in a factorized table.
4. Extend solver validation beyond the two interface/reference sanity checks below, and distinguish system φₛ from structure Φ. Keep the formalism explicitly pinned.
5. Compare candidate substrates and their alternatives. A result on this four-coordinate subset would not certify a whole-agent complex or silicon consciousness.

The agent's deterministic, ideal arithmetic remains a separate limitation. Physical noise, mismatch, continuous-time causal structure and sampled readout are not established by these software tables.

## Conditional IIT computation

The optional solver environment uses Python 3.13.17 and [PyPhi revision 134a8f31](https://github.com/wmayner/pyphi/tree/134a8f31b49db512322465ed3ba5da7194d362fd). Exact dependencies are in requirements-iit.txt. The adapter verifies installed commit provenance, explicitly selects `IIT_4_0_2023`, uses little-endian state-row ordering, and requests only system irreducibility analysis. It does not inherit the package's different 2026 formalism default.

Reproduce from the repository root:

```sh
python3 -m venv .venv-iit-bootstrap
.venv-iit-bootstrap/bin/python -m pip install uv==0.13.5
.venv-iit-bootstrap/bin/uv venv --python 3.13.17 .venv-iit
.venv-iit-bootstrap/bin/uv pip install --python .venv-iit/bin/python -r requirements-iit.txt
PYPHI_WELCOME_OFF=1 .venv-iit/bin/python -m model.iit
```

The independent two-bit identity system gives φₛ=0; a two-bit bidirectional swap gives φₛ=2 under this formalism. These test solver invocation, state ordering and the chosen formalism; they do not validate the entire library or serve as agent evidence.

For each extracted nominal model, analyze all 16 current binary states across **all 11 subsets of size two through four**, not just a chosen pair. Outside elements of a subset use the solver's conditional background treatment within the four-coordinate surrogate. The omitted physical/model states were already absorbed into the conditional finite-horizon transition table; this second boundary treatment does not undo that approximation. Singleton candidates and structure Φ are not computed, so this is not a complete exclusion/complex search.

| Model duration | Candidate | Defined states / 16 | φₛ range over defined states |
|---|---|---:|---:|
| 0.5 | All four coordinates | 8 | 0–0 |
| 0.5 | Perception/observer pair | 8 | 0–0 |
| 2.0 | All four coordinates | 5 | 0–0 |
| 2.0 | Perception/observer pair | 5 | 0–0 |

Other states have no reachable predecessor under the solver's forward check and are reported **undefined**, never replaced with zero. The full per-state output is emitted by the command above.

The expanded subset sweep attempts 176 analyses per lag. At duration 0.5, 88 are defined; at duration 2, 55 are defined. All 143 defined analyses return φₛ=0. Undefined cases remain explicit in the output.

The deterministic dependency audit flips each input bit while holding other surrogate inputs fixed. Rows are sources and columns are destinations, in the four-coordinate order above:

```text
duration 0.5             duration 2.0
1 0 0 0                  1 1 0 0
0 1 0 0                  0 1 0 0
0 0 0 0                  0 0 0 0
0 0 0 1                  0 1 1 1
```

Neither surrogate retains a cycle between distinct coordinates. This is a statement about these thresholded transition tables, not the continuous agent's wiring. It identifies a failure of this chosen reduction to capture multi-coordinate recurrence; dependency matrices are not substituted for the solver's φₛ calculation. A different justified boundary/temporal grain must preserve the relevant causal loop before testing its irreducibility.

**Result:** these particular surrogate models do not demonstrate a positive integrated candidate under IIT 4.0 (2023). This is not evidence that the complete agent or fabricated circuit has zero integration: background dependence, coarse-graining, unmodeled noise and omitted internal state remain substantial. Conversely, those caveats do not license treating the result as positive. The next analysis must justify a better boundary/grain or change the architecture, not add arbitrary noise or search unreported parameter settings until a favorable score appears.

## Second boundary and active operating point

A second candidate follows a real implemented control loop: stream 0's first aperture state, measured telemetry, allocation estimate and predicted telemetry, in that order. The omitted-background intervention changes the second aperture state to 0.9. It does not add a separate demonstration circuit.

Both candidates are evaluated at the original early checkpoint (200 steps) and at an event-defined active checkpoint: the first step with inspection-query activity above 0.9 and stream-0 mean aperture above 0.25. The active checkpoint occurs at step 478 in this configuration. This selection follows actual task activity, not a favorable integration result. All previous binning, intervention amplitudes and durations are retained.

```sh
PYPHI_WELCOME_OFF=1 .venv-iit/bin/python -m model.iit --candidate attention --phase early
PYPHI_WELCOME_OFF=1 .venv-iit/bin/python -m model.iit --candidate distributed --phase inspection
PYPHI_WELCOME_OFF=1 .venv-iit/bin/python -m model.iit --candidate attention --phase inspection
```

Each cell below attempts 176 state/subset analyses:

| Candidate / checkpoint | Duration | Defined analyses | Positive φₛ analyses | Maximum φₛ |
|---|---:|---:|---:|---:|
| Distributed / early | 0.5 | 88 | 0 | 0 |
| Distributed / early | 2.0 | 55 | 0 | 0 |
| Attention / early | 0.5 | 33 | 0 | 0 |
| Attention / early | 2.0 | 11 | 0 | 0 |
| Distributed / inspection | 0.5 | 88 | 0 | 0 |
| Distributed / inspection | 2.0 | 22 | 0 | 0 |
| Attention / inspection | 0.5 | 88 | 0 | 0 |
| Attention / inspection | 2.0 | 11 | 0 | 0 |

All 396 defined analyses are zero. Undefined cases remain distinct from zero. The active attention candidate **does** retain cross-coordinate cycles at duration 0.5, with dependency matrix:

```text
1 1 0 0
1 1 1 1
1 1 1 0
1 1 1 0
```

Thus absence of a binary cycle explains only some earlier reductions, not all zero results; cycle presence is insufficient to infer positive φₛ. At duration 2, both attention tables collapse to constant output. The active attention table at duration 0.5 also changes 3/16 output rows under the background intervention and 8/16 under the within-bin control. These remain fragile surrogate models, not a resolved intrinsic substrate. No tested boundary is promoted to a positive result, and no whole-agent integration claim follows.
