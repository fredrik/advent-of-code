import itertools

import networkx


def solve(input, part, diff_cutoff):
    nodes, edges, start, end = parse_input(input)

    graph = networkx.Graph(edges)
    paths = dict(networkx.shortest_path_length(graph, target=end))

    if part == 1:
        max_jump_length = 2
    else:
        max_jump_length = 20

    count = 0
    for x, y in graph.nodes:
        for nx, ny in jumps(nodes, x, y, max_jump_length):
            jump_length = abs(x - nx) + abs(y - ny)
            diff = paths[(x, y)] - paths[(nx, ny)] - jump_length
            if diff >= diff_cutoff:
                count += 1
    return count


def jumps(nodes, x, y, jump):
    i = range(-jump, jump + 1)
    j = range(-jump, jump + 1)
    prod = itertools.product(i, j)
    skips = [(x, y) for x, y in prod if abs(x) + abs(y) <= jump and (x, y) != (0, 0)]
    for dx, dy in skips:
        nx, ny = x + dx, y + dy
        if (nx, ny) in nodes and nodes[(nx, ny)] != "#":
            yield nx, ny


# ---


def parse_input(input):
    lines = input.strip().split("\n")

    nodes = {}
    edges = set()
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell == "#":
                continue
            if cell == "S":
                start_position = (x, y)
            if cell == "E":
                end_position = (x, y)
            nodes[(x, y)] = cell

    for x, y in nodes:
        for n in neighs(nodes, x, y):
            edges.add(((x, y), n))

    return nodes, edges, start_position, end_position


def neighs(nodes, x, y):
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if (nx, ny) in nodes and nodes[(nx, ny)] != "#":
            yield nx, ny


# ---


import os


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        filename = "input.txt"
        diff_cutoff = 100
    else:
        filename = "input.small"
        diff_cutoff = 50

    with open(filename, "r") as f:
        return f.read(), diff_cutoff


if __name__ == "__main__":
    input, diff_cutoff = choose_input()
    print("part 1:", solve(input, 1, diff_cutoff))
    print("part 2:", solve(input, 2, diff_cutoff))
