from aoc import get_input
from collections import defaultdict


def solve(input, part):
    graph = make_graph(parse_input(input))

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


def parse_input(input):
    for line in input:
        a, b = line.strip().split("-")
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
        bron_kerbosch(
            r.union(set([v])), p.intersection(n), x.intersection(n), graph, clique
        )
        p.remove(v)
        x.add(v)


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
