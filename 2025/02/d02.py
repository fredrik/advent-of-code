import re
import os


def solve(input, part):
    answer = 0
    for x in parse_input(input):
        if repeats(part, x):
            answer += x
    return answer


def parse_input(input):
    for r in input.strip().split(","):
        a, b = r.split("-")
        for x in range(int(a), int(b) + 1):
            yield x  # todo: there's a neater way to 'yield from' somehow.


def repeats(part: int, x: int):
    patterns = {1: r"^(\d+)\1$", 2: r"^(\d+)\1+$"}
    return bool(re.search(patterns[part], str(x)))


# ---


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        filename = "input.txt"
    else:
        filename = "input.small"

    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    input = choose_input()
    print("part 1:", solve(input, 1))
    print("part 2:", solve(input, 2))
