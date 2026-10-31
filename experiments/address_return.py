"""Candidate memory-return semantics; baseline configuration is unchanged."""
import json
from model.agent import Agent
from model.configuration import association_weights
from experiments.withdrawn_task import evaluate_case


def configured():
    return Agent(rule=(1/3,1/3,1/3),context_source=1,context_prior_gain=.04,
                 association_weights=association_weights(),
                 memory_return_mode='address_consistency')


if __name__ == '__main__':
    for context in ('horizontal','vertical'):
        for sign in (-1,1):
            print(json.dumps(evaluate_case(context,sign,factory=configured)),flush=True)
