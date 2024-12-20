import itertools

import networkx


def solve(input, part):
    nodes, edges, start, end = parse_input(input)
    g = networkx.Graph(edges)

    print(g)
    # print("nodes", g.nodes)
    # print("edges", g.edges)
    # print("start", start)
    # print("end", end)

    if part == 1:
        count = 0
        paths = dict(networkx.shortest_path_length(g, target=end))
        for node in g.nodes:
            x, y = node
            for nx, ny in reachable(nodes, x, y):
                cost = abs(x - nx) + abs(y - ny)
                diff = paths[(x, y)] - paths[(nx, ny)] - cost
                if diff >= 100:
                    count += 1

        return count


def reachable(nodes, x, y):
    skips = [
        p for p in itertools.product([-2, -1, 0, 1, 2], [-2, -1, 0, 1, 2]) if abs(p[0]) + abs(p[1]) <= 2 and p != (0, 0)
    ]
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
    else:
        filename = "input.small"

    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    input = choose_input()
    print("part 1:", solve(input, 1))
    # print("part 2:", solve(input, 2))
