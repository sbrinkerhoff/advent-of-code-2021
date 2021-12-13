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
"""
part2

After reviewing the available paths, you realize you
might have time to visit a single small cave twice.
Specifically, big caves can be visited any number of
times, a single small cave can be visited at most twice,
and the remaining small caves can be visited at most once.
However, the caves named start and end can only be visited
exactly once each: once you leave the start cave, you
may not return to it, and once you reach the end cave,
the path must end immediately.
"""


graph = defaultdict(list)
try:
    fname = sys.argv[1]
except:
    fname = "example2"

for line in [x.strip() for x in open(fname).readlines()]:
    a, b = line.split('-')
    if a == "start":
        graph[a].append(b)
    elif b == "end":
        graph[a].append(b)
    else:
        graph[a].append(b)
        graph[b].append(a)


def find_paths_2(graph, start='start', end='end', current_path=None, visited_twice=False):
    if current_path is None:
        current_path = [start]

    if start == end:
        yield current_path

    for x in [x for x in current_path if x.islower()]:
        if current_path.count(x) > 1:
            visited_twice = True

    else:
        for node in graph[current_path[-1]]:
            local_path = current_path + [node]

            if node == "start" or current_path[-1] == "end":
                continue

            if visited_twice and node.islower() and local_path.count(node) > 1:
                continue

            elif node.islower() and local_path.count(node) > 2:
                continue

            for result in find_paths_2(graph, node, end, local_path, visited_twice):
                yield result


paths = [x for x in find_paths_2(graph=graph)]
for x in paths:
    print(x)

print(len(paths))
