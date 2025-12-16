# --- Day 18: Like a GIF For Your Yard ---

from aoc import get_input, parse_grid, neighbours
from collections import defaultdict


def solve(input, part):
    grid = parse_grid(input)

    if part == 1:
        for _ in range(100):
            grid = mutate_grid(grid)
        return sum(v == "#" for v in grid.values())
    else:
        return


def mutate_grid(grid):
    def on(k):
        n = sum(v == "#" for v in neighbours(grid, k))
        return (grid[k] == "#" and n == 2) or (n == 3)

    return {k: "#" if on(k) else "." for k in grid}


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
