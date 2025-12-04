import re
import os
import sys
from collections import defaultdict
from itertools import permutations


def solve(input, part):
    people, g = parse_input(input)

    if part == 1:
        return max(rate_happiness(order, g) for order in permutations(people))
    else:
        return


def rate_happiness(order, g):
    happiness = 0
    n = len(order)
    for i, p in enumerate(order):
        left, right = order[(i + 1) % n], order[(i - 1) % n]
        happiness += g[(p, left)] + g[(p, right)]
    return happiness


def parse_input(input):
    people = set()
    g = defaultdict(int)
    for line in input:
        match = re.search(
            r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)\.",
            line.strip(),
        )
        a, b, gainlose, n = match[1], match[4], match[2], int(match[3])
        g[(a, b)] = n if gainlose == "gain" else -n
        people.add(a)
        people.add(b)
    return people, g


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
