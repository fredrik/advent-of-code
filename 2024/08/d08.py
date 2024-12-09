import os
from collections import defaultdict


def part1(input):
    grid = defaultdict(dict)
    towers = defaultdict(list)  # keyed by frequency
    for y, line in enumerate(input.strip().splitlines()):
        grid[y] = defaultdict(str)
        for x, freq in enumerate([f for f in line.strip()]):
            grid[y][x] = freq
            if freq == ".":
                grid[y][x] = "o"
            if freq != ".":
                towers[freq].append((x, y))

    pairs = find_pairs(towers)
    for t1, t2 in pairs:
        dx, dy = (t1[0] - t2[0], t1[1] - t2[1])
        set_xy(grid, t1[0] + dx, t1[1] + dy, "#")
        set_xy(grid, t2[0] - dx, t2[1] - dy, "#")

    print_grid(grid)

    return count_antinodes(grid)


def part2(input):
    grid = defaultdict(dict)
    towers = defaultdict(list)  # keyed by frequency
    for y, line in enumerate(input.strip().splitlines()):
        grid[y] = defaultdict(str)
        for x, freq in enumerate([f for f in line.strip()]):
            grid[y][x] = freq
            if freq != ".":
                towers[freq].append((x, y))

    pairs = find_pairs(towers)
    for t1, t2 in pairs:
        n = 1
        while True:
            dx, dy = (t1[0] - t2[0], t1[1] - t2[1])
            set_xy(grid, t1[0] + dx * n, t1[1] + dy * n, "#")
            set_xy(grid, t2[0] - dx * n, t2[1] - dy * n, "#")
            if oob(grid, t1[0] + dx * n, t1[1] + dy * n) and oob(grid, t2[0] - dx * n, t2[1] - dy * n):
                break
            n += 1

    print_grid(grid)

    return count_antinodes_part2(grid)


def oob(grid, x, y):
    max_x, max_y = len(grid[0]), len(grid)

    return x not in range(0, max_x) or y not in range(0, max_y)


def xy(grid, x, y):
    return grid[y][x]


def set_xy(grid, x, y, value):
    max_x, max_y = len(grid[0]), len(grid)
    if x in range(0, max_x) and y in range(0, max_y):
        grid[y][x] = value


def find_pairs(towers):
    from itertools import combinations

    pairs = set()
    for freq, ts in towers.items():
        for c in combinations(ts, 2):
            pairs.add(c)
    return pairs


def count_antinodes(grid):
    count = 0
    for y, xs in grid.items():
        for x, c in xs.items():
            if xy(grid, x, y) == "#":
                count += 1
    return count


def count_antinodes_part2(grid):
    count = 0
    for y, xs in grid.items():
        for x, c in xs.items():
            if xy(grid, x, y) != ".":
                count += 1
    return count


def print_grid(grid):
    for y, xs in grid.items():
        for x, c in xs.items():
            print(c, end="")
        print("\n", end="")
    print()


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        filename = "input.txt"
    else:
        filename = "input.small"

    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    input = choose_input()
    print(part1(input))
    print(part2(input))
