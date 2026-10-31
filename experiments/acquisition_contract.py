"""Complete continuous acquisition reference for the fixed joint candidate.

This is an executable boundary contract backed by Agent, NOT an independent
equation derivation, compact motif, IIT TPM or physical implementation proof.
The default retains all 106 changing coordinates; an explicitly supplied reduced
candidate factory retains its 90. Four learning coordinates are fixed trial
parameters; reward and learning-valid inputs are deliberately unavailable.
"""
import numpy as np
from dataclasses import asdict
from model.configuration import joint_configured as configured


def parameters(agent):
    """Declared instance-level parameters; equation constants remain code-bound."""
    return dict(
        implementation=(type(agent).__module__+'.'+type(agent).__qualname__,
                        tuple(type(s).__module__+'.'+type(s).__qualname__
                              for s in agent.sensory.specialists)),
        agent={key:getattr(agent,key) for key in ('forced_source','context_source',
               'context_prior_gain','memory_return_mode','reliability_selection','decoded_stability')},
        association=agent.association.weights.tolist(),
        sensory=asdict(agent.sensory.p),
        specialists=[asdict(s.p) for s in agent.sensory.specialists],
        reliability_tau=agent.sensory.reliability.tau,
        workspace_dt=agent.workspace.dt,
        content={key:getattr(agent.content,key) for key in
                 ('dt','self_gain','return_gain','activity_tau')},
        observer=dict(dt=agent.observer.dt,tau=agent.observer.tau),
        attention=dict(dt=agent.attention.dt,gain=agent.attention.gain,
                       taus=agent.attention.taus.tolist()))


def inventory(factory=configured):
    a=factory()
    names=a.state_names()
    frozen=[i for i,n in enumerate(names) if n.startswith(('learned_variance[','source_value['))]
    dynamic=[i for i in range(len(names)) if i not in frozen]
    return names,dynamic,frozen,a.state_vector()[frozen]


def project(agent,factory=configured):
    """Project a state of the declared fixed configuration, rejecting learning."""
    if parameters(agent)!=parameters(factory()):
        raise ValueError('agent parameters differ from declared acquisition configuration')
    _,dynamic,frozen,values=inventory(factory)
    state=agent.state_vector()
    if not np.array_equal(state[frozen],values):
        raise ValueError('learning coordinates differ from declared fixed trial parameters')
    return state[dynamic].copy()


def transition(state, samples, visibility, *, input_enabled=(1,1), task_enabled=True,
               factory=configured):
    """Advance one dt=.025 step; every changing external input is explicit.

    Samples (2x4), base visibility (2x4), physical enables (2), task gate (bool).
    No context class, correct answer, reward, clocked stage, or trial index is
    supplied. All interventions are default/intact; do not reuse this contract
    for lesion/noising policies without explicitly extending the input boundary.
    """
    if not isinstance(task_enabled,(bool,np.bool_)):
        raise ValueError('Boolean task availability required')
    names,dynamic,_,_=inventory(factory)
    x=np.asarray(state,dtype=float)
    if x.shape!=(len(dynamic),) or not np.all(np.isfinite(x)):
        raise ValueError('finite complete acquisition state required')
    a=factory()
    full=a.state_vector()
    full[dynamic]=x
    a.set_state(full)
    result=a.step(samples,visibility,input_enabled=input_enabled,
                  task_enabled=task_enabled,reward=None,valid=(0,0))
    return project(a,factory),result
