from aoc import get_input


def solve(input, part):
    patterns, designs = parse_input(input)

    if part == 1:
        return sum(1 for d in designs if all_possible_arrangements(d, patterns))
    else:
        return sum(all_possible_arrangements(d, patterns) for d in designs)


def parse_input(input):
    raw_patterns, raw_designs = input.split("\n\n")
    patterns = [p.strip() for p in raw_patterns.strip().split(",")]
    designs = [d.strip() for d in raw_designs.strip().split("\n")]
    return patterns, designs


def all_possible_arrangements(design, patterns, cache={}):
    if design == "":
        return 1

    if design not in cache:
        cache[design] = sum(
            all_possible_arrangements(design[len(p) :], patterns, cache)
            for p in patterns
            if design.startswith(p)
        )

    return cache[design]


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
