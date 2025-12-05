from collections import defaultdict

from aoc import get_input


def solve(input, part):
    grid = parse_input(input)

    if part == 1:
        _, removed_count = remove(grid)
        return removed_count
    else:
        total_removed = 0
        removed_count = None

        while removed_count != 0:
            grid, removed_count = remove(grid)
            total_removed += removed_count

        return total_removed


def remove(g):
    new_grid = defaultdict(str)
    ok = 0
    for i, j in list(g):
        if g[(i, j)] != "@":
            continue

        adjacents = sum(
            [
                True
                for di in [-1, 0, 1]
                for dj in [-1, 0, 1]
                if (di, dj) != (0, 0) and g[(i + di, j + dj)] == "@"
            ]
        )

        if adjacents < 4:
            ok += 1
            new_grid[(i, j)] = "."
        else:
            new_grid[(i, j)] = g[(i, j)]

    return new_grid, ok


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
