import re
import os
import itertools
from string import ascii_lowercase


def solve(data, part):
    count = 0
    for line in data.splitlines():
        if nice(line, part):
            count += 1
    return count


def nice(line, part):
    if part == 1:
        return nice_part_one(line)
    else:
        return nice_part_two(line)


def nice_part_one(line):
    def twice(line):
        for letter in ascii_lowercase:
            if letter * 2 in line:
                return True

    def vowels(line):
        vs = [x for x in line if x in set("aeiou")]
        return len(vs) >= 3

    for s in set(["ab", "cd", "pq", "xy"]):
        if s in line:
            return False

    return twice(line) and vowels(line)


def nice_part_two(line):
    def pair(line):
        for t in itertools.product(ascii_lowercase, ascii_lowercase):
            p = "".join(t)
            pattern = re.compile(f"{p}.*{p}")
            if pattern.search(line):
                return True

    def repeats(line):
        for x in ascii_lowercase:
            pattern = re.compile(f"{x}[a-z]{x}")
            if pattern.search(line):
                return True

    return pair(line) and repeats(line)


# ---


def get_input_data():
    if os.environ.get("INPUT"):
        filename = os.environ.get("INPUT")
    else:
        filename = "input.txt"

    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, "r") as f:
        return f.read()


if __name__ == "__main__":
    data = get_input_data()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
