from aoc import get_input
import re
from collections import defaultdict
from itertools import permutations


def solve(data, part):
    people, g = parse_input(data)

    if part == 1:
        return max(rate_happiness(order, g) for order in permutations(people))
    else:
        for p in people:
            g[('Me', p)] = 0
            g[(p, 'Me')] = 0
        people.add('Me')
        return max(rate_happiness(order, g) for order in permutations(people))


def rate_happiness(order, g):
    happiness = 0
    n = len(order)
    for i, p in enumerate(order):
        left, right = order[(i + 1) % n], order[(i - 1) % n]
        happiness += g[(p, left)] + g[(p, right)]
    return happiness


def parse_input(data):
    people = set()
    g = defaultdict(int)
    for line in data.splitlines():
        match = re.search(
            r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)\.",
            line.strip(),
        )
        a, b, gainlose, n = match[1], match[4], match[2], int(match[3])
        g[(a, b)] = n if gainlose == "gain" else -n
        people.add(a)
        people.add(b)
    return people, g


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
