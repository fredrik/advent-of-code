import os
import sys
from functools import cache


def solve(input, part):
    containers = parse_input(input)

    combos = fitting_combinations(containers, 150)

    if part == 1:
        return len(combos)
    else:
        shortest = min(len(c) for c in combos)
        return len([c for c in combos if len(c) == shortest])


@cache
def fitting_combinations(cs, n, picked=tuple()):
    combos = []
    for i, c in enumerate(cs):
        if c > n:
            continue
        elif c == n:
            combos.append(picked + (c,))
        else:
            combos += fitting_combinations(cs[i + 1 :], n - c, picked + (c,))
    return combos


def parse_input(input):
    return tuple(int(line) for line in input)


# ---


def get_input():
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, "r") as f:
        return f.readlines()


if __name__ == "__main__":
    input = get_input()
    print("part 1:", solve(input, 1))
    print("part 2:", solve(input, 2))
