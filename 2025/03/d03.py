import os
from itertools import combinations

def solve(input, part):
    if part == 1:
        jolts = 0
        banks = parse_input(input)
        for bank in banks:
            m = max([int(a+b) for a,b in combinations(bank, 2)])
            print(f'b: {bank}, max: {m}')
            jolts += m
        return jolts
    else:
        return


def parse_input(input):
    for line in input:
        yield [x for x in line.strip()]

``
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
