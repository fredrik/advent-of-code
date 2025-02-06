import os
from collections import defaultdict
from itertools import chain


def solve(data, part):
    grid = parse_input(data)

    if part == 1:
        return part1(grid)
    else:
        return part2(grid)


def part1(grid):
    target = list("XMAS")

    return sum(
        [grid[(i + di * n, j + dj * n)] for n in range(4)] == target
        for dj in [-1, 0, 1]
        for di in [-1, 0, 1]
        for i, j in list(grid)
    )


def part2(grid):
    targets = (list("MAS"), list("SAM"))

    return sum(
        [grid[(i + d, j + d)] for d in [-1, 0, 1]] in targets
        and [grid[(i + d, j - d)] for d in [-1, 0, 1]] in targets
        for i, j in list(grid)
    )


# ---


def parse_input(data):
    g = defaultdict(str)
    for i, line in enumerate(data.strip().splitlines()):
        for j, c in enumerate(line):
            g[(i, j)] = c
    return g


def get_input_data():
    if os.environ.get("INPUT"):
        filename = os.environ.get("INPUT")
    else:
        filename = "input.txt"

    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    data = get_input_data()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
