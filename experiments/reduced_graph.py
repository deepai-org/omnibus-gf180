"""Structural block graph of the exact shuttered reduction, not IIT.

Normalized three-way populations stay whole. Two declared configurations:
default content-independent association vs a generic content-dependent tensor.
Both use unforced selection. Edges describe possible equation dependencies,
not derivatives at one saturated operating point.
"""
import json


def graph(content_dependent=False):
    sizes = {**{f'{p}{i}':n for p,n in (('a',1),('h',1),('content',3),
             ('quality',2),('local',3),('observer',3),('variance',1)) for i in (0,1)},
             'memory':3,'rule':3,'retrieve':1}
    edges = {(n,n) for n in sizes}
    for i in (0,1):
        edges.update((n,f'a{i}') for n in (f'a{1-i}',f'h{i}',f'content{i}',
                                           f'local{i}',f'observer{i}','memory'))
        edges.add((f'a{i}',f'h{i}'))
        edges.update((n,f'local{i}') for n in ('a0','a1',f'content{i}','memory',f'variance{i}'))
    edges.update((('retrieve','memory'),('rule','memory'),('memory','retrieve'),('rule','retrieve')))
    if content_dependent:
        edges.update((n,target) for n in ('a0','a1','content0','content1')
                     for target in ('memory','retrieve'))
    return sizes,edges


def analyze(content_dependent=False):
    sizes,edges = graph(content_dependent)
    reachable = {n:{n} for n in sizes}
    for a,b in edges:
        reachable[a].add(b)
    for k in sizes:
        for n in sizes:
            if k in reachable[n]:
                reachable[n].update(reachable[k])
    remaining = set(sizes)
    components = []
    for n in sizes:
        if n in remaining:
            group = sorted(m for m in remaining if m in reachable[n] and n in reachable[m])
            remaining.difference_update(group)
            components.append(dict(blocks=group,coordinates=sum(sizes[m] for m in group)))
    return dict(content_dependent=content_dependent,coordinates=sum(sizes.values()),
                components=components,edges=sorted(edges),
                interpretation='structural SCCs, not IIT complexes or Phi')


if __name__ == '__main__':
    print(json.dumps([analyze(False),analyze(True)],indent=2))
