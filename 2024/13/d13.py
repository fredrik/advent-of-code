import os
import re

cost = {
    "a": 3,
    "b": 1,
}


def solve(input, part2):
    machines = parse_input(input)
    # Button A: X+94, Y+34
    # Button B: X+22, Y+67
    # Prize: X=8400, Y=5400
    # =>
    # machine: {'a': (94, 34), 'b': (22, 67), 'prize': (8400, 5400)}

    # so, find 8400 = m*94 + n*22 and 5400 = m*34 + n*67
    # while, I think, minimizing 3*m + n

    costs = []
    for index, machine in enumerate(machines):
        print("machine", index)
        solutions = find_solution(machine, 10000000000000 if part2 else 0)
        if len(solutions) > 1:
            print("multiple solutions!@#")
        for m, n, cost in solutions:
            print(m, n, cost)
            costs.append(cost)

        print()

    return sum(costs)


def find_solution(machine, prize_offset):
    # solutions = []
    # for i in range(100000):
    #     for j in range(100000):
    #         if (
    #             prize_offset + machine["prize"][0] == i * machine["a"][0] + j * machine["b"][0]
    #             and prize_offset + machine["prize"][1] == i * machine["a"][1] + j * machine["b"][1]
    #         ):
    #             solutions.append((i, j, cost["a"] * i + cost["b"] * j))
    # return solutions

    px = prize_offset + machine["prize"][0]
    py = prize_offset + machine["prize"][1]
    ax = machine["a"][0]
    ay = machine["a"][1]
    bx = machine["b"][0]
    by = machine["b"][1]

    i = (px * by - py * bx) / (ax * by - ay * bx)
    j = (py * ax - px * by) / (ax * by - ay * bx)

    if (i == int(i)) and (j == int(j)):
        return [(i, j, cost["a"] * i + cost["b"] * j)]
    else:
        print(i, int(i))
        print(j, int(j))
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


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        filename = "input.txt"
    else:
        filename = "input.small"

    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    input = choose_input()
    # print("part 1", solve(input, False))
    print("part 2", solve(input, True))
