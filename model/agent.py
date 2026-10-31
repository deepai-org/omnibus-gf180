"""Closed perception/query/inspection loop; incomplete theory-demonstrator.

Two specialists operate concurrently. Learned source values bias competing
content populations; adaptation permits selection changes within a trial. A forced
source remains available as an intervention. Convergence is separate from the
evidence/prediction observer. Attention has a forward-estimate/controller candidate;
its presence alone does not establish AST.
"""

import numpy as np

from .learning import AdaptiveSpecialists, OutcomeLearning
from .attention import Attention
from .observer import Observer
from .workspace import Workspace
from .content_workspace import ContentWorkspace
from .association import Association
from .perception import PerceptionParameters
from .primitives import categorical_memory_drive, quality_encode, quality_decode


class Agent:
    # Sensory 46; workspace 9; support 2; desired 2; attention 14; rule 3;
    # observer 18; outcome values 2; content workspace 14 replaces selection 2.
    state_count = 110

    def __init__(self, rule=(1, 0, 0), source=None, dt=.025, association_weights=None,
                 context_source=None, context_prior_gain=0., memory_return_mode='content_match',
                 reliability_selection=False, decoded_stability=False):
        rule = np.asarray(rule, dtype=float)
        if rule.shape != (3,) or not np.all(np.isfinite(rule)) or np.any(rule < 0) or not np.isclose(rule.sum(), 1):
            raise ValueError('normalized stored grouping rule required')
        if source not in (None, 0, 1):
            raise ValueError('source must be None (adaptive) or identify a specialist')
        self.rule = rule.copy()
        self.association = Association(association_weights)
        if memory_return_mode not in ('content_match','address_consistency'):
            raise ValueError('unknown memory return circuit')
        self.memory_return_mode = memory_return_mode
        self.reliability_selection = bool(reliability_selection)
        self.decoded_stability = bool(decoded_stability)
        self.forced_source = source
        if context_source not in (None, 0, 1):
            raise ValueError('context source must identify a specialist or be None')
        self.context_source = context_source
        if not np.isfinite(context_prior_gain) or not 0 <= context_prior_gain <= .1:
            raise ValueError('context prior gain must lie in [0,.1]')
        self.context_prior_gain = float(context_prior_gain)
        self.outcomes = OutcomeLearning()
        if not np.isfinite(dt) or not 0 < dt <= .025:
            raise ValueError('agent dt must lie in (0, .025]')
        self.sensory = AdaptiveSpecialists(PerceptionParameters(dt=dt))
        self.reset_trial()

    def reset_trial(self):
        self.sensory.reset_trial()
        self.workspace = Workspace(self.sensory.p.dt)
        self.support = np.zeros(2)
        self.desired_inspection = np.zeros(2)
        self.attention = Attention(self.sensory.p.dt)
        self.observer = Observer(self.sensory.p.dt)
        self.content = ContentWorkspace(self.sensory.p.dt, self_gain=.8, return_gain=.65)

    @property
    def source(self):
        return self.forced_source if self.forced_source is not None else int(np.argmax(self.content.activity))

    @property
    def inspection(self):
        return self.attention.aperture.mean(axis=1)

    def state_vector(self):
        return np.concatenate([a.ravel() for _, a in self.state_fields()])

    def state_fields(self):
        """Named dynamic-state views, in the canonical checkpoint order."""
        fields = []
        for i, s in enumerate(self.sensory.specialists):
            fields.extend((f'sensory.{i}.{name}', s.latents if name == 'z' else getattr(s, name))
                          for name in ('x', 'z', 'group', 'quality'))
        fields.append(('learned_variance', self.sensory.reliability.variance))
        fields.extend((f'workspace.{name}', getattr(self.workspace, name))
                      for name in ('query', 'memory', 'comparison'))
        fields.extend([('support', self.support), ('desired_inspection', self.desired_inspection)])
        fields.extend((f'attention.{name}', getattr(self.attention, name))
                      for name in ('aperture', 'feedback', 'estimate', 'predicted_feedback'))
        fields.append(('rule', self.rule))
        fields.extend((f'observer.{name}', getattr(self.observer, name))
                      for name in ('evidence', 'prediction', 'conflict'))
        fields.append(('source_value', self.outcomes.value))
        fields.extend((f'content.{name}', getattr(self.content, name))
                      for name in ('activity', 'group', 'quality', 'adaptation'))
        return fields

    def state_names(self):
        return [f'{name}[{",".join(map(str, index))}]'
                for name, array in self.state_fields()
                for index in ([(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)]
                              if name.endswith('.z') else np.ndindex(array.shape))]

    def set_state(self, state):
        """Restore dynamic state; immutable parameters/source are separate context.

        Interventions must respect each stored population's normalization.
        Validate the complete candidate before mutating any state.
        """
        state = np.asarray(state, dtype=float)
        if state.shape != (self.state_count,) or not np.all(np.isfinite(state)):
            raise ValueError('invalid agent state')
        offset = 0
        candidates = []
        for name, array in self.state_fields():
            value = state[offset:offset + array.size].reshape(array.shape)
            offset += array.size
            low, high = (-1, 1) if name.endswith(('.x', '.z', '.decoded_quality')) or name == 'content.quality' else (0, 1)
            if name == 'learned_variance':
                low, high = .0625, 4
            if np.any(value < low) or np.any(value > high):
                raise ValueError(f'out-of-range state: {name}')
            if (name.endswith('.group') or name.endswith('.quality') and name != 'content.quality'
                    or name == 'rule'):
                if not np.allclose(value.sum(axis=-1), 1):
                    raise ValueError(f'unnormalized population: {name}')
            candidates.append((array, value.copy()))
        for array, value in candidates:
            array[:] = value

    def step(self, samples, base_visibility, residual=(0, 0), valid=(0, 0), suppress=None,
             reward=None, learn_outcomes=True, context_cue=None, task_enabled=True,
             broadcast_enabled=True, sensory_feedback=True, observer_feedback=True,
             memory_feedback=True, context_feedback=True, input_enabled=(1, 1),
             context_admission=True,
             recurrent_returns=True, return_override=None, sensory_return=True):
        override = None if return_override is None else np.asarray(return_override,dtype=float)
        if override is not None and (override.shape != (2,) or not np.all(np.isfinite(override)) or
                                     np.any(np.abs(override)>1)):
            raise ValueError('return intervention requires two finite values in [-1,1]')
        if reward is not None and (not np.isfinite(reward) or not 0 <= reward <= 1):
            raise ValueError('reward must lie in [0, 1]')
        cue = None if context_cue is None else np.asarray(context_cue, dtype=float)
        if cue is not None and (cue.shape != (3,) or not np.all(np.isfinite(cue)) or
                                np.any(cue < 0) or not np.isclose(cue.sum(), 1)):
            raise ValueError('context cue must be a normalized three-state signal')
        samples = np.asarray(samples, dtype=float)
        base = np.asarray(base_visibility, dtype=float)
        if samples.shape != (2, 4) or base.shape != (2, 4):
            raise ValueError('two four-part scenes required')
        if not np.all(np.isfinite(base)) or np.any((base < 0) | (base > 1)):
            raise ValueError('invalid base visibility')
        enabled = np.asarray(input_enabled, dtype=float)
        if enabled.shape != (2,) or not np.all(np.isfinite(enabled)) or np.any((enabled < 0)|(enabled > 1)):
            raise ValueError('two bounded physical input enables required')
        # Inspection cannot reopen a physically withdrawn stimulus. This input
        # belongs to the fixture, not to the agent's report/control machinery.
        mask = (base + (1 - base) * self.attention.aperture)*enabled[:,None]
        owner = self.source
        group = self.content.group[owner].copy()
        retrieved_rule = self.association.retrieve(self.rule, group)
        population = quality_encode(self.content.quality[owner])
        broadcast_valid = (broadcast_enabled and self.content.activity[owner] > .7 and
                           self.content.activity[owner]-self.content.activity[1-owner] > .2)
        coverage = float(np.mean(mask[owner]))
        command = self.workspace.query[1] if task_enabled and (broadcast_valid or coverage <= .75) else 0
        context_drive = categorical_memory_drive(self.rule)
        if cue is not None:
            context_drive += 4 * (cue - self.rule)
        groups = np.stack([s.group for s in self.sensory.specialists])
        local_monitoring = self.observer.readout(groups) if self.reliability_selection else None
        if self.context_source is not None:
            c = self.context_source
            # Physical cue acquisition, not a fixture-provided class label.
            # The recurrent context population holds the result after removal.
            context_admitted = (not self.reliability_selection or not context_admission or
                                local_monitoring['admitted'][c])
            if (np.max(mask[c]) > 0 and self.support[c] > .9 and
                    np.max(groups[c]) > .85 and context_admitted):
                context_drive += 4*(groups[c]-self.rule)
        qualities = np.stack([quality_decode(s.quality) for s in self.sensory.specialists])
        monitoring = self.observer.readout(self.content.group)
        # A physically withdrawn input is not evidence against a recently
        # acquired representation. Existing observer evidence provides a bounded
        # trace: it decays without observations and cannot be created by a
        # confident content population alone. Partially visible inputs still
        # require acquisition rather than this withdrawn-input exception.
        retained_evidence = enabled[owner] == 0 and monitoring['admitted'][owner]
        supported = (self.support[owner] > .9 and broadcast_valid and
                     (coverage > .75 or retained_evidence))
        # Graded content-specific return path, distinct from the report gate.
        # A lesion removes this prior without silencing local inference.
        priors = np.zeros((2, 3))
        if broadcast_enabled and sensory_feedback:
            priors[owner] = .01*self.content.activity[owner]*(group-1/3)
            if context_feedback:
                # Retrieved association supplies a prediction, not a truth label.
                # Its spatial fit is still evaluated by the sensory/observer paths.
                memory = self.workspace.memory
                observed_pattern = self.sensory.specialists[owner].x
                contrast = np.clip(4*np.mean((observed_pattern-observed_pattern.mean())**2),0,1)
                priors[owner] += self.context_prior_gain*contrast*self.content.activity[owner]*(memory-memory.sum()/3)
        available = (np.max(mask, axis=1) > 0).astype(float)
        if self.forced_source is not None:
            available[1-self.forced_source] = 0
        observed = np.stack([s.x for s in self.sensory.specialists])
        strength = np.clip(4*np.mean(np.abs(observed),axis=1),0,1)
        evidence = strength*np.clip(.55 + .4*self.outcomes.value + np.array([.001, 0]), 0, 1)
        if self.reliability_selection and observer_feedback:
            # Candidate-specific evidence must be able to recruit a currently
            # suppressed population. Use each local claim's measured reliability,
            # not the not-yet-acquired workspace payload or a fixture label.
            # Penalize contradiction rather than demanding prior confidence:
            # ambiguous evidence may require workspace/context to be resolved.
            evidence *= 1-.5*local_monitoring['conflict']
        # Internal loops persist when an external shutter closes. Recruitment,
        # not physical input availability, weights their return to activity.
        recruitment = self.content.activity
        feedback = recruitment*(2*np.sum(groups*self.content.group, axis=1)-1)
        if not sensory_return:
            feedback = np.zeros(2)
        if observer_feedback:
            feedback = np.clip(feedback + .2*recruitment*(monitoring['support']-
                                                       monitoring['conflict']), -1, 1)
        if memory_feedback:
            # Retrieved association is a distinct retained population, not a copy
            # of selected content. Its match returns to candidate competition.
            if self.memory_return_mode == 'address_consistency':
                memory_support = self.association.retrieval_support(
                    self.rule,self.content.group,self.workspace.memory)
            else:
                memory_support = (2*(self.content.group @ self.workspace.memory)-
                                  self.workspace.memory.sum())
            feedback = np.clip(feedback + .1*recruitment*memory_support, -1, 1)
        if not recurrent_returns:
            feedback = np.zeros(2)
        if override is not None:
            # Experiment-only external edge clamp/replay, not autonomous state.
            feedback = override.copy()
        predictions = []
        targets = []
        for i, specialist in enumerate(self.sensory.specialists):
            signals = specialist.signals(mask[i], float(self.sensory.reliability.precision[i] * monitoring['precision_scale'][i]), prior=priors[i])
            predictions.append(signals['prediction'])
            # Accumulate representational stability rather than demanding that
            # every noisy input and unused latent reach instantaneous rest.
            # Evidence support remains independently checked by the observer.
            drift = np.sum((signals['group_target'] - specialist.group) ** 2)
            if self.decoded_stability:
                drift += np.mean((quality_decode(signals['quality_target'])-
                                  quality_decode(specialist.quality))**2)
            else:
                drift += np.mean(np.sum((signals['quality_target'] - specialist.quality) ** 2, axis=1))
            targets.append(float(np.clip(1 - drift / .01, 0, 1)))
        # Acquisition is complete when its evidence is usable, even if actuator
        # saturation prevents the requested physical position. This does not
        # bypass stability, grouping confidence or observer admission.
        acquired = supported and np.max(group) >= .85 and monitoring['admitted'][self.source]
        result = self.workspace.step(group, population, retrieved_rule, suppress, supported,
                                     inspection_complete=(self.attention.estimate[self.source] > .95 or acquired),
                                     admitted=monitoring['admitted'][self.source], enabled=task_enabled,
                                     acquisition_requested=(enabled[owner] > 0 and
                                                            (coverage <= .75 or (broadcast_valid and np.max(group) < .85)) and
                                                            np.min(mask[self.source]) < .95))
        self.sensory.step(samples, mask, residual, valid, monitoring['precision_scale'], priors=priors)
        self.observer.step(observed, mask, predictions)
        dt = self.sensory.p.dt
        # This trace certifies stability during acquisition, not stability of
        # an unobserved sensory network relaxing toward its default state.
        # Hold it while the physical input is absent. Retention is still bounded
        # by decaying observer evidence and adaptive workspace release; this
        # trace alone cannot authorize a report. New observations update it.
        observed_input = (np.max(mask,axis=1) > 0).astype(float)
        self.support += dt * observed_input * (np.asarray(targets) - self.support)
        self.attention.step(self.desired_inspection)
        # Local orienting must not wait for an already selected global content:
        # a hidden new input otherwise cannot displace an old winner to be seen.
        requests = np.zeros(2)
        if task_enabled and suppress != 'inspect':
            requests = enabled*(np.mean(mask,axis=1) <= .75)
        requests[owner] = max(requests[owner], command)
        self.desired_inspection += dt*requests*(1-self.desired_inspection)
        self.rule += dt * context_drive
        if reward is not None:
            self.outcomes.step(reward, owner, learn_outcomes and result['report_enabled'], dt)
        self.content.step(evidence, groups, qualities, available, feedback)
        result['source'] = owner
        return result
