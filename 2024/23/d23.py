import os

from collections import defaultdict


def solve(data, part):
    graph = make_graph(edges(data))

    if part == 1:
        return part1(graph)
    else:
        return part2(graph)


def part1(graph):
    return len(
        set(
            tuple(sorted((k, c, s)))
            for k in graph.keys()
            if k.startswith("t")
            for c in graph[k]
            for s in graph[k] & graph[c]
        )
    )


def part2(graph):
    largest_clique = max(find_cliques(graph), key=len)
    return ",".join(sorted(largest_clique))


# ---


def edges(data):
    for line in data.splitlines():
        a, b = line.split("-")
        yield a, b


def make_graph(edges):
    graph = defaultdict(set)
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)
    return graph


def find_cliques(graph):
    clique = []
    bron_kerbosch(r=set(), p=set(graph.keys()), x=set(), graph=graph, clique=clique)
    return clique


def bron_kerbosch(r, p, x, graph, clique):
    if len(p) == 0 and len(x) == 0:
        clique.append(r)
        return
    for v in set(p):
        n = graph[v]
        bron_kerbosch(r.union(set([v])), p.intersection(n), x.intersection(n), graph, clique)
        p.remove(v)
        x.add(v)


# ---


def get_input_data():
    if os.environ.get("INPUT"):
        filename = os.environ.get("INPUT")
        # todo: make sure path is relative and in the same directory and exists and so on etc
    else:
        # default
        filename = "input.txt"

    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    data = get_input_data()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
