from aoc import get_input

import itertools
from collections import deque, defaultdict


def solve(input, part):
    graph, start, end, diff_cutoff = parse_input(input)

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
    for dx, dy in [
        (x, y) for x, y in prod if abs(x) + abs(y) <= jump and (x, y) != (0, 0)
    ]:
        nx, ny = x + dx, y + dy
        if (nx, ny) in graph:
            yield (nx, ny)


def neighbours(graph, x, y):
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if (nx, ny) in graph:
            yield nx, ny


def parse_input(input):
    graph = defaultdict(set)

    for y, row in enumerate(input):
        for x, cell in enumerate(row.strip()):
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

    if len(input) > 20:
        diff_cutoff = 100
    else:
        diff_cutoff = 50

    return graph, start_position, end_position, diff_cutoff


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
