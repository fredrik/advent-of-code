from aoc import get_input

from collections import defaultdict


def solve(input, part):
    grid = parse_input(input)

    if part == 1:
        target = list("XMAS")
        return sum(
            [grid[(i + di * n, j + dj * n)] for n in range(4)] == target
            for dj in [-1, 0, 1]
            for di in [-1, 0, 1]
            for i, j in list(grid)
        )
    else:
        targets = (list("MAS"), list("SAM"))
        return sum(
            [grid[(i + d, j + d)] for d in [-1, 0, 1]] in targets
            and [grid[(i + d, j - d)] for d in [-1, 0, 1]] in targets
            for i, j in list(grid)
        )


def parse_input(input):
    g = defaultdict(str)
    for i, line in enumerate(input):
        for j, c in enumerate(line):
            g[(i, j)] = c
    return g


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
