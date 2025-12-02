import re
import os


def solve(input, part):
    if part == 1:
        answer = 0
        for x in parse_input(input):
            if repeats(x):
                answer += x
        return answer
    else:
        # Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice.
        # So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.
        answer = 0
        for x in parse_input(input):
            if repeats_more(x):
                answer += x
        return answer


def parse_input(input):
    for r in input.strip().split(","):
        a, b = r.split("-")
        for x in range(int(a), int(b) + 1):
            yield x  # todo: there's a neater way to 'yield from' somehow.


def repeats(x: int):
    """You can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice."""
    return bool(re.search(r"^(\d+)\1$", str(x)))


def repeats_more(x: int):
    """You can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice."""
    return bool(re.search(r"^(\d+)\1+$", str(x)))


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
