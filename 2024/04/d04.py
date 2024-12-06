import os
from collections import defaultdict
from itertools import chain

import numpy as np


def part1(input):
    xmas = np.array(["X", "M", "A", "S"])
    original_grid = np.array([[c for c in line] for line in input.strip().splitlines()])

    all_lines = (line for grid in rotations(original_grid) for line in chain(grid, diagonals(grid)))
    print(
        sum(
            (
                np.array_equal(line.take(range(i, i + len(xmas)), mode="clip"), xmas)
                for line in all_lines
                for i in range(line.size)
            )
        )
    )


def rotations(original_grid):
    for n in range(4):
        yield np.rot90(original_grid, k=n)


def diagonals(grid):
    for n in range(-len(grid), len(grid)):
        yield np.diagonal(grid, offset=n)


def part2(input):
    lines = input.strip().splitlines()
    w = len(lines)
    g = defaultdict(str)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            g[(i, j)] = c

    def has_mas(g, i, j):
        a = g[(i - 1, j - 1)]
        b = g[(i + 1, j + 1)]
        c = g[(i - 1, j + 1)]
        d = g[(i + 1, j - 1)]

        if ((a == "M" and b == "S") or (a == "S" and b == "M")) and (
            (c == "M" and d == "S") or (c == "S" and d == "M")
        ):
            return 1
        else:
            return 0

    count = 0
    for i in range(w):
        for j in range(w):
            if g[(i, j)] == "A":
                count += has_mas(g, i, j)
    print(count)


input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def choose_input():
    if os.environ.get("FILEMODE"):
        with open("input.txt", "r") as f:
            return f.read()
    else:
        return input


if __name__ == "__main__":
    input = choose_input()
    part1(input)
    part2(input)
