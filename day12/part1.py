#!/usr/bin/env python3
from collections import defaultdict
import sys

"""Your goal is to find the number of distinct paths
that start at start, end at end, and don't visit small
caves more than once. There are two types of caves:
big caves (written in uppercase, like A) and small
caves (written in lowercase, like b). It would be a
waste of time to visit any small cave more than once,
but big caves are large enough that it might be worth
visiting them multiple times. So, all paths you find
should visit small caves at most once, and can visit
big caves any number of times.
"""

graph = defaultdict(list)

for line in [x.strip() for x in open(sys.argv[1]).readlines()]:
    a, b = line.split('-')
    graph[a].append(b)
    graph[b].append(a)


def find_paths(graph, start='start', end='end', current_path=None):
    if current_path is None:
        current_path = [start]

    if start == end:
        yield current_path
    else:
        for node in graph[current_path[-1]]:
            if node == node.lower():  # we only visit it once
                if node not in current_path:
                    for result in find_paths(graph, node, end, current_path + [node]):
                        yield result
            elif node == node.upper():  # we can visit it multiple times
                for result in find_paths(graph, node, end, current_path + [node]):
                    yield result
            else:
                raise Exception('Invalid node: {}'.format(node))


paths = [x for x in find_paths(graph=graph)]
for x in paths:
    print(x)

print(len(paths))
