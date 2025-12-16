from aoc import get_input
from functools import cache


def solve(data, part):
    containers = parse_input(data)

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


def parse_input(data):
    return tuple(int(line) for line in data.splitlines())


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
