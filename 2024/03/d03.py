import re


def part_1(input):
    sum = 0
    for line in input.strip().splitlines():
        for match in re.finditer(r"mul\((\d+),(\d+)\)", line):
            x = int(match.group(1))
            y = int(match.group(2))
            sum += x * y

    print(f"sum: {sum}")


# ---

small_input = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""


def choose_input():
    import os

    if os.environ.get("AOC_INPUT_FILE"):
        with open(os.environ.get("AOC_INPUT_FILE"), "r") as file:
            return file.read()
    else:
        return small_input


if __name__ == "__main__":
    input = choose_input()
    part_1(input)

# usage:
#
# for small input
# $> uv run d03.py
#
# for large input
# $> AOC_INPUT_FILE=input.txt uv run d03.py
