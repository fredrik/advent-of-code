import os
from itertools import combinations


def solve(input, part):
    banks = parse_input(input)
    k = 2 if part == 1 else 12

    jolts = 0
    for bank in banks:
        r = []
        for i, d in enumerate(bank):
            while r and r[-1] < d and len(r) + len(bank) - i > k:
                r.pop()
            if len(r) < k:
                r.append(d)
        jolts += int("".join(r))
    return jolts


def parse_input(input):
    for line in input:
        yield [x for x in line.strip()]


# ---


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        filename = "input.txt"
    else:
        filename = "input.small"

    with open(filename, "r") as f:
        return f.readlines()


if __name__ == "__main__":
    input = choose_input()
    print("part 1:", solve(input, 1))
    print("part 2:", solve(input, 2))
