def solve(input, part):
    locks, keys = parse_input(input)

    count = 0
    for lock in locks:
        for key in keys:
            if key_fits_lock(key, lock):
                count += 1
    return count


def key_fits_lock(key, lock):
    for i in range(len(key)):
        if key[i] + lock[i] > 5:
            return False
    return True


# ---


def parse_input(input):
    locks, keys = [], []

    def parse_design(lines):
        design = [0] * len(lines[0])
        for line in lines:
            for i, c in enumerate(line):
                if c == "#":
                    design[i] += 1
        return design

    for chunk in input.strip().split("\n\n"):
        lines = chunk.splitlines()
        if lines[0][0] == "#":  # lock
            locks.append(parse_design(lines[1:-1]))
        else:  # key
            keys.append(parse_design(lines[1:-1]))
    return locks, keys


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
    # print("part 1:", solve(input, 1))
    print("part 2:", solve(input, 2))
