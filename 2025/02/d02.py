import re

from aoc import get_input


def solve(input, part):
    return sum([x for x in parse_input(input) if repeats(part, x)])


def repeats(part: int, x: int):
    patterns = {1: r"^(\d+)\1$", 2: r"^(\d+)\1+$"}
    return bool(re.search(patterns[part], str(x)))


def parse_input(input):
    for r in input[0].strip().split(","):
        a, b = r.split("-")
        yield from range(int(a), int(b) + 1)


if __name__ == "__main__":
    input = get_input()
    print("part 1:", solve(input, 1))
    print("part 2:", solve(input, 2))
