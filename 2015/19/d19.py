# --- Day 19: Medicine for Rudolph ---
#

from aoc import get_input
from collections import defaultdict
import re


def solve(input, part):
    replacements, molecule = parse_input(input)

    if part == 1:
        distinct = set()
        for source, becomes in replacements.items():
            for b in becomes:
                for match in re.finditer(source, molecule):
                    i = match.start()
                    distinct.add(
                        molecule[:i] + b + molecule[i + len(source) :]
                    )
        return len(distinct)
    else:

        

        return


def parse_input(input):
    parts = input.strip().split("\n\n")
    rules = defaultdict(list)
    for line in parts[0].split("\n"):
        src, dst = line.split(" => ")
        rules[src].append(dst)
    molecule = parts[1]
    return dict(rules), molecule


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
