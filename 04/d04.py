import re
import numpy as np


def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            print(grid[i][j], end="")
        print()
    print()


def get_matrix_diagonals(n):
    """
    Returns coordinates for all diagonals in an n x n matrix.
    Returns list of lists, where each inner list contains (row, col) tuples for one diagonal.
    """
    # Main diagonal and above
    diagonals = []
    for k in range(n):
        diagonal = []
        for i in range(n - k):
            diagonal.append((i, i + k))
        diagonals.append(diagonal)

    # Below main diagonal
    for k in range(1, n):
        diagonal = []
        for i in range(n - k):
            diagonal.append((i + k, i))
        diagonals.append(diagonal)

    return diagonals


def find_xmas(grid):
    XMAS = ("X", "M", "A", "S")
    count = 0

    # reporting
    whitelist = set()

    def add_to_whitelist(x, y):
        whitelist.add((x, y))

    def print_grid_whitelisted(grid):
        for i in range(len(grid)):
            for j in range(len(grid)):
                if (i, j) in whitelist:
                    print(grid[i][j], end="")
                else:
                    print(".", end="")
            print()
        print()

    # /reporting

    # assuming square grid
    width = height = len(grid)

    for i in range(width):
        for j in range(height):
            # if grid[i][j] != 'X':
            #     print(f'skip ({i},{j})')
            #     continue
            # else:
            #     print(f'inspect ({i},{j})')

            directions = [
                (0, 1, "forward"),
                (0, -1, "backward"),
                (-1, 0, "up"),
                (1, 0, "down"),
                # (1, 1, 'forward down'),
                # (1, -1, 'forward up'),
                # (-1, 1, 'backward down'),
                # (-1, -1, 'backward up'),
            ]

            for x, y, name in directions:
                maybe_xmas = tuple(
                    grid[(i + x * n) % width][(j + y * n) % height] for n in range(4)
                )
                if maybe_xmas == XMAS:
                    count += 1
                    print(f"found {maybe_xmas} at ({i},{j}) via {name}")
                    # print(f'line: {grid[i]}')
                    # print(f'line: {grid[(i+1)%height]}')
                    # print(f'line: {grid[(i+2)%height]}')
                    # print(f'line: {grid[(i+3)%height]}')

                    for n in range(4):
                        print(
                            f"({(i+x*n)%width},{(j+y*n)%height}) = {grid[(i+x*n)%width][(j+y*n)%height]}"
                        )

                    [
                        add_to_whitelist((i + x * n) % width, (j + y * n) % height)
                        for n in range(4)
                    ]

            print("------------")
            print()

    for coords in get_matrix_diagonals(width):
        diagonal = "".join([f"{grid[x][y]}" for (x, y) in coords])
        reversed_diagonal = "".join(reversed([f"{grid[x][y]}" for (x, y) in coords]))
        count += len(re.findall(r"XMAS", diagonal))
        count += len(re.findall(r"XMAS", reversed_diagonal))

    print()
    print(f"count: {count}")
    print()
    print_grid_whitelisted(grid)


def part_1(input):
    grid = []
    for line in input.strip().splitlines():
        grid.append(list(line))

    print_grid(grid)
    find_xmas(grid)


# ---

small_input = """
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
    import os

    if os.environ.get("AOC_INPUT_FILE"):
        with open(os.environ.get("AOC_INPUT_FILE"), "r") as file:
            return file.read()
    else:
        return small_input


if __name__ == "__main__":
    input = choose_input()
    part_1(input)

# usage:
#
# for small input
# $> uv run d04.py
#
# for large input
# $> AOC_INPUT_FILE=input.txt uv run d04.py
