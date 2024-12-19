from collections import defaultdict


def solve(input, part2):
    raw_patterns, raw_designs = input.split("\n\n")
    raw_patterns = [p.strip() for p in raw_patterns.strip().split(",")]
    patterns = defaultdict(set)
    for p in raw_patterns:
        patterns[len(p)].add(p)
    designs = [d.strip() for d in raw_designs.strip().split("\n")]

    return sum(1 for d in designs if design_possible(d, patterns))


def design_possible(design, patterns, ass=[]):
    if design == "":
        return ass

    # iterate over patterns by size, longest first.
    # try and match the start of the design.
    # n is a member of [9, 8, 7, 6, 5, 4, 3, 2]
    for n in reversed(sorted(patterns.keys())):
        if len(design) < n:
            continue
        for p in patterns[n]:
            if design[:n] == p:
                if ass := design_possible(design[n:], patterns, ass + [p]):
                    return ass

    return []


# ---


import os


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
