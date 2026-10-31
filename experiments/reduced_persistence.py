"""35-coordinate exact sufficient-statistic reduction for closed shutters.

Retains the 10 frozen payload coordinates rather than hiding them as constants.
Dynamic coordinates: activity/adaptation 4, local grouping 6, observer difference 6,
retrieved memory 3, stored context 3, retrieve query 1, observation variance 2.
No claim of acquisition-mode equivalence or IIT validity is made.
"""
import numpy as np
from model.primitives import categorical_memory_drive
from model.configuration import association_weights


def configured_transition(state,**kwargs):
    """Reduced dynamics with the one demonstrator's immutable configuration."""
    kwargs.setdefault('forced_source',None)
    kwargs.setdefault('weights',association_weights())
    return transition(state,**kwargs)


def project(a):
    cg = a.content.group
    observation = np.stack([s.x for s in a.sensory.specialists])
    return np.concatenate((a.content.activity,a.content.adaptation,cg.ravel(),
                           a.content.quality.ravel(),
                           np.stack([s.group for s in a.sensory.specialists]).ravel(),
                           (a.observer.evidence-a.observer.conflict).ravel(),
                           a.workspace.memory,a.rule,a.workspace.query[:1],
                           np.var(observation,axis=1)))


def lift(state, agent):
    """Declared constructive micro-intervention, not an IIT noising distribution.

    Observer difference d is realized as evidence=max(d,0), conflict=max(-d,0).
    Variance v is realized as a zero-mean ±sqrt(v) spatial pattern. Other omitted
    coordinates retain the supplied agent background. Population interventions
    must respect their simplex; variance lies in [0,1] for this explicit lift.
    """
    x = np.asarray(state,dtype=float)
    if x.shape != (35,) or not np.all(np.isfinite(x)):
        raise ValueError('35 finite reduced coordinates required')
    low = np.zeros(35)
    low[10:14] = -1
    low[20:26] = -1
    if np.any(x<low) or np.any(x>1):
        raise ValueError('reduced coordinates outside lift range')
    for g in (x[4:10].reshape(2,3),x[14:20].reshape(2,3),x[29:32]):
        if not np.allclose(g.sum(axis=-1),1):
            raise ValueError('normalized grouping and context required')
    # Validate before changing the supplied agent.
    agent.content.activity[:] = x[:2]
    agent.content.adaptation[:] = x[2:4]
    agent.content.group[:] = x[4:10].reshape(2,3)
    agent.content.quality[:] = x[10:14].reshape(2,2)
    for i,s in enumerate(agent.sensory.specialists):
        s.group[:] = x[14+3*i:17+3*i]
        s.x[:] = np.sqrt(x[33+i])*np.array([1,-1,1,-1])
    difference = x[20:26].reshape(2,3)
    agent.observer.evidence[:] = np.maximum(difference,0)
    agent.observer.conflict[:] = np.maximum(-difference,0)
    agent.workspace.memory[:] = x[26:29]
    agent.rule[:] = x[29:32]
    agent.workspace.query[0] = x[32]
    return agent


def transition(state,dt=.025,context_prior_gain=.04,forced_source=0,weights=None,
               cuts=(),return_override=None):
    x = np.asarray(state,dtype=float)
    if x.shape != (35,) or not np.all(np.isfinite(x)) or not 0<dt<=.025:
        raise ValueError('finite 35-coordinate state and valid timestep required')
    activity,adaptation = x[:2],x[2:4]
    cg,cq,local = x[4:10].reshape(2,3),x[10:14],x[14:20].reshape(2,3)
    observer = x[20:26].reshape(2,3)
    memory,rule,query,variance = x[26:29],x[29:32],x[32],x[33:35]
    owner = int(np.argmax(activity)) if forced_source is None else forced_source
    feedback = activity*(2*np.sum(local*cg,axis=1)-1)
    if 'sensory' in cuts:
        feedback = np.zeros(2)
    if 'observer' not in cuts:
        feedback = np.clip(feedback+.2*activity*np.sum(cg*observer,axis=1),-1,1)
    if 'memory' not in cuts:
        feedback = np.clip(feedback+.1*activity*(2*(cg@memory)-memory.sum()),-1,1)
    if return_override is not None:
        feedback = np.asarray(return_override,dtype=float)
        if feedback.shape != (2,) or not np.all(np.isfinite(feedback)) or np.any(np.abs(feedback)>1):
            raise ValueError('invalid return intervention')
    target = np.clip(2*(.8*activity+.65*feedback-1.2*activity[::-1]-.9*adaptation-.45),0,1)
    prior = np.zeros((2,3))
    prior[owner] = .01*activity[owner]*(cg[owner]-1/3)
    prior[owner] += context_prior_gain*np.clip(4*variance[owner],0,1)*activity[owner]*(memory-memory.sum()/3)
    cost = .04*np.array([1,1,0])-prior
    activation = np.maximum(.025-(cost-cost.min(axis=1)[:,None]),0)
    group_target = activation/activation.sum(axis=1)[:,None]
    if weights is None:
        weights = np.broadcast_to(np.eye(3)[:,None,:],(3,3,3))
    address = np.einsum('c,g,cgr->r',rule,cg[owner],weights)
    ready = memory.sum()>=.9 and np.max(np.abs(memory-address))<.1
    return np.concatenate((activity+dt/.5*(target-activity),
                           adaptation+dt/8*(activity-adaptation),cg.ravel(),cq,
                           (local+dt*(group_target-local)).ravel(),
                           (observer*(1-dt)).ravel(),memory+dt*query*(address-memory),
                           rule+dt*categorical_memory_drive(rule),
                           [query+dt/.5*(float(not ready)-query)],
                           variance*(1-dt/.5)**2))
