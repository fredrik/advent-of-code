def solve(input, part):
    raw_patterns, raw_designs = input.split("\n\n")
    patterns = [p.strip() for p in raw_patterns.strip().split(",")]
    designs = [d.strip() for d in raw_designs.strip().split("\n")]

    if part == 1:
        return sum(1 for d in designs if all_possible_arrangements(d, patterns))
    else:
        return sum(all_possible_arrangements(d, patterns) for d in designs)


def all_possible_arrangements(design, patterns, cache={}):
    if design == "":
        return 1

    if design not in cache:
        cache[design] = sum(
            all_possible_arrangements(design[len(p) :], patterns, cache) for p in patterns if design.startswith(p)
        )

    return cache[design]


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
    print("part 1", solve(input, 1))
    print("part 2", solve(input, 2))
