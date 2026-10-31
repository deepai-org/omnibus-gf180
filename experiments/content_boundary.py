"""Declared conditional dependency graph, NOT integrated information.

When all specialist inputs are clamped, content does not return to activity
inside the 14-coordinate component. Its payload-bearing loops close through
external specialists. This audit prevents labeling an activity-only SCC as the
entire workspace's intrinsic substrate.
"""
import json


def graph():
    names = ['a0','a1'] + [f'g{i}{j}' for i in range(2) for j in range(3)]
    names += [f'z{i}{j}' for i in range(2) for j in range(2)] + ['h0','h1']
    edges = {(n,n) for n in names}
    for i in range(2):
        edges.update(((f'a{i}',f'a{1-i}'),(f'a{i}',f'h{i}'),(f'h{i}',f'a{i}')))
        edges.update((f'a{i}',f'g{i}{j}') for j in range(3))
        edges.update((f'a{i}',f'z{i}{j}') for j in range(2))
    return names, edges


def components():
    names, edges = graph()
    reach = {n:{n} for n in names}
    for source,target in edges:
        reach[source].add(target)
    for k in names:
        for i in names:
            if k in reach[i]:
                reach[i].update(reach[k])
    remaining = set(names)
    groups = []
    for n in names:
        if n in remaining:
            group = sorted(m for m in remaining if m in reach[n] and n in reach[m])
            groups.append(group)
            remaining.difference_update(group)
    return groups


if __name__ == '__main__':
    print(json.dumps(dict(boundary='all specialist inputs externally clamped',
                         components=components(),
                         warning='Simplex coordinates are constrained; graph SCCs are not IIT complexes.'),indent=2))
