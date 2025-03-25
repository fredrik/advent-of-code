import os
from string import ascii_lowercase


def solve(data, part):
    count = 0
    for line in data.splitlines():
        if nice(line):
            count += 1
    return count


def nice(line):
    bad_strings = set(["ab", "cd", "pq", "xy"])
    for s in bad_strings:
        if s in line:
            return False
    return twice(line) and vowels(line)


def twice(line):
    for letter in ascii_lowercase:
        if letter * 2 in line:
            return True


def vowels(line):
    vs = [x for x in line if x in set("aeiou")]
    return len(vs) >= 3


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
    # print("part 2:", solve(data, 2))
