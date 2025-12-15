from aoc import get_input

from collections import defaultdict
from itertools import combinations


def solve(input, part):
    grid, towers = parse_input(input)
    pairs = find_pairs(towers)

    if part == 1:
        for t1, t2 in pairs:
            dx, dy = (t1[0] - t2[0], t1[1] - t2[1])
            set_xy(grid, t1[0] + dx, t1[1] + dy, "#")
            set_xy(grid, t2[0] - dx, t2[1] - dy, "#")
        return count_antinodes(grid)
    else:
        for t1, t2 in pairs:
            n = 1
            while True:
                dx, dy = (t1[0] - t2[0], t1[1] - t2[1])
                set_xy(grid, t1[0] + dx * n, t1[1] + dy * n, "#")
                set_xy(grid, t2[0] - dx * n, t2[1] - dy * n, "#")
                if oob(grid, t1[0] + dx * n, t1[1] + dy * n) and oob(
                    grid, t2[0] - dx * n, t2[1] - dy * n
                ):
                    break
                n += 1
        return count_antinodes_part2(grid)


def find_pairs(towers):
    pairs = set()
    for freq, ts in towers.items():
        for c in combinations(ts, 2):
            pairs.add(c)
    return pairs


def set_xy(grid, x, y, value):
    max_x, max_y = len(grid[0]), len(grid)
    if x in range(0, max_x) and y in range(0, max_y):
        grid[y][x] = value


def oob(grid, x, y):
    max_x, max_y = len(grid[0]), len(grid)
    return x not in range(0, max_x) or y not in range(0, max_y)


def xy(grid, x, y):
    return grid[y][x]


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


def parse_input(input):
    grid = defaultdict(dict)
    towers = defaultdict(list)
    for y, line in enumerate(input):
        grid[y] = defaultdict(str)
        for x, freq in enumerate([f for f in line.strip()]):
            grid[y][x] = freq
            if freq != ".":
                towers[freq].append((x, y))
    return grid, towers


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
