from aoc import get_input

import re

COST = {"a": 3, "b": 1}


def solve(input, part):
    machines = parse_input(input)

    costs = []
    for index, machine in enumerate(machines):
        solutions = find_solution(machine, 10000000000000 if part == 2 else 0)

        for m, n, c in solutions:
            costs.append(c)

    return sum(costs)


def find_solution(machine, prize_offset):
    px = prize_offset + machine["prize"][0]
    py = prize_offset + machine["prize"][1]
    ax = machine["a"][0]
    ay = machine["a"][1]
    bx = machine["b"][0]
    by = machine["b"][1]

    i = (px * by - py * bx) / (ax * by - ay * bx)
    j = (py * ax - px * ay) / (ax * by - ay * bx)

    if (i == int(i)) and (j == int(j)):
        return [(int(i), int(j), int(COST["a"] * i + COST["b"] * j))]
    else:
        return []


def parse_input(input):
    machines = []
    for lines in input.split("\n\n"):
        machine = {}
        match = re.search(r"Button A: X\+(\d+), Y\+(\d+)", lines)
        machine["a"] = (int(match.group(1)), int(match.group(2)))
        match = re.search(r"Button B: X\+(\d+), Y\+(\d+)", lines)
        machine["b"] = (int(match.group(1)), int(match.group(2)))
        match = re.search(r"Prize: X=(\d+), Y=(\d+)", lines)
        machine["prize"] = (int(match.group(1)), int(match.group(2)))
        machines.append(machine)
    return machines


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
