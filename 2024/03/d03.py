from aoc import get_input

import re


def solve(input, part):
    if part == 1:
        muls = parse_input_part_1(input)
        return sum(x * y for x, y in muls)
    else:
        muls = parse_input_part_2(input)
        return sum(x * y for x, y in muls)


def parse_input_part_1(input):
    for line in input:
        for match in re.finditer(r"mul\((\d+),(\d+)\)", line):
            x = int(match.group(1))
            y = int(match.group(2))
            yield x, y


def parse_input_part_2(input):
    enabled = True
    for line in input:
        for match in re.finditer(r"(mul\((\d+),(\d+)\))|(do\(\))|(don\'t\(\))", line):
            if match.group(0) == "do()":
                enabled = True
            if match.group(0) == "don't()":
                enabled = False
            if match.group(0).startswith("mul") and enabled:
                x = int(match.group(2))
                y = int(match.group(3))
                yield x, y


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
