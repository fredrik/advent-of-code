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
        solutions = find_solution(machine)
        if len(solutions) > 1:
            print("multiple solutions!@#")
        for m, n, cost in solutions:
            print(m, n, cost)
            costs.append(cost)

        print()

    return sum(costs)


def find_solution(machine):
    solutions = []
    for i in range(100):
        for j in range(100):
            if (
                machine["prize"][0] == i * machine["a"][0] + j * machine["b"][0]
                and machine["prize"][1] == i * machine["a"][1] + j * machine["b"][1]
            ):
                solutions.append((i, j, cost["a"] * i + cost["b"] * j))
    return solutions


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
    print("part 1", solve(input, False))
    # print("part 2", solve(input, True))
