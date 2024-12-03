import re


def part_2(input):
    sum = 0
    enabled = True
    for line in input.strip().splitlines():
        for match in re.finditer(r"(mul\((\d+),(\d+)\))|(do\(\))|(don\'t\(\))", line):
            if match.group(0) == "do()":
                enabled = True
            if match.group(0) == "don't()":
                enabled = False
            if match.group(0).startswith("mul") and enabled:
                x = int(match.group(2))
                y = int(match.group(3))
                sum += x * y
    print(f"sum: {sum}")


# ---

small_input = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
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
    part_2(input)

# usage:
#
# for small input
# $> uv run d03p2.py
#
# for large input
# $> AOC_INPUT_FILE=input.txt uv run d03p2.py
