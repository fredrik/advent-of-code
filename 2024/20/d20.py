import itertools
from collections import deque, defaultdict


def solve(input, part, diff_cutoff):
    graph, start, end = parse_input(input)

    distances = find_distances(graph, end)

    if part == 1:
        max_jump_length = 2
    else:
        max_jump_length = 20

    count = 0
    for x, y in graph:
        for nx, ny in jumps(graph, x, y, max_jump_length):
            jump_length = abs(x - nx) + abs(y - ny)
            diff = distances[(x, y)] - distances[(nx, ny)] - jump_length
            if diff >= diff_cutoff:
                count += 1
    return count


# bfs.
def find_distances(graph, target):
    distances = defaultdict(lambda: float("inf"))
    distances[target] = 0

    queue = deque([target])
    visited = set([target])

    while queue:
        current = queue.popleft()

        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
                distances[neighbour] = distances[current] + 1
    return distances


def jumps(graph, x, y, jump):
    i = range(-jump, jump + 1)
    j = range(-jump, jump + 1)
    prod = itertools.product(i, j)
    for dx, dy in [(x, y) for x, y in prod if abs(x) + abs(y) <= jump and (x, y) != (0, 0)]:
        nx, ny = x + dx, y + dy
        if (nx, ny) in graph: # avoid walls by checking that the jump lands on a node.
            yield (nx, ny)


# ---


def parse_input(input):
    lines = input.strip().split("\n")

    graph = defaultdict(set)  # adjacency

    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell == "#":
                continue
            if cell == "S":
                start_position = (x, y)
            if cell == "E":
                end_position = (x, y)
            graph[(x, y)] = set()

    for x, y in graph:
        for n in neighbours(graph, x, y):
            graph[(x, y)].add(n)

    return graph, start_position, end_position


def neighbours(graph, x, y):
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if (nx, ny) in graph:
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
