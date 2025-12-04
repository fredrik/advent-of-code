import os
from collections import defaultdict


def solve(input, part):
    grid = parse_input(input)

    if part == 1:
        c = defaultdict(lambda: ".")
        reachable = defaultdict(lambda: ".")
        ok = 0
        for i, j in list(grid):
            if grid[(i, j)] != "@":
                continue

            adjacents = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if (di, dj) == (0, 0):
                        continue
                    if grid[(i + di, j + dj)] == "@":
                        adjacents += 1

            if adjacents < 4:
                ok += 1
                reachable[(i, j)] = "x"
            else:
                reachable[(i, j)] = grid[(i, j)]

            c[(i, j)] = adjacents

        #     print(f"i: {i}, j:{j}")
        #     print(adjacents)

        # print_grid(grid)
        # print()
        # print_grid(reachable)
        # print()
        # print_grid(c)

        return ok
    else:
        total_removed = 0
        new_grid, removed_count = remove(grid)
        total_removed += removed_count

        while removed_count != 0:
            new_grid, removed_count = remove(new_grid)
            total_removed += removed_count

        return total_removed


def remove(g):
    new_grid = defaultdict(str)
    c = defaultdict(lambda: ".")
    reachable = defaultdict(lambda: ".")
    ok = 0
    for i, j in list(g):
        new_grid[(i, j)] = g[(i, j)]
        if g[(i, j)] != "@":
            continue

        adjacents = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if (di, dj) == (0, 0):
                    continue
                if g[(i + di, j + dj)] == "@":
                    adjacents += 1

        if adjacents < 4:
            ok += 1
            reachable[(i, j)] = "x"
            new_grid[(i, j)] = "."
        else:
            reachable[(i, j)] = g[(i, j)]

        c[(i, j)] = adjacents

    return new_grid, ok


def print_grid(c):
    for i in range(10):
        line = "".join([str(c[(i, j)]) for j in range(10)])
        print(line)


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
