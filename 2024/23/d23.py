import os
from collections import defaultdict

import networkx as nx


def solve(input, part):
    if part == 1:
        return part1(input)
    else:
        return part2(input)


def part1(input):
    graph = make_graph(edges(input))
    return len(
        set(
            tuple(sorted((k, c, s)))
            for k in graph.keys()
            if k.startswith("t")
            for c in graph[k]
            for s in graph[k] & graph[c]
        )
    )


def part2(input):
    graph = nx.Graph(edges(input))
    largest_clique = max(nx.find_cliques(graph), key=len)
    return ",".join(sorted(largest_clique))


# ---


def make_graph(edges):
    graph = defaultdict(set)
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)
    return graph


def edges(input):
    for line in input.splitlines():
        a, b = line.split("-")
        yield a, b


# ---


def get_input_data():
    if os.environ.get("INPUT"):
        filename = os.environ.get("INPUT")
        # todo: make sure path is relative and in the same directory etc
    else:
        # default
        filename = "input.txt"

    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    data = get_input_data()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
