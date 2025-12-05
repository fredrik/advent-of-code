import os
from collections import defaultdict


def solve(input, part):
    fresh, items = parse_input(input)

    if part == 1:
        return sum(is_fresh(i, fresh) for i in items)
    else:
        return


def is_fresh(i, fresh):
    for a,b in fresh:
        if i >= a and i <= b:
            print(f'{i} is fresh')
            return True
    return False

# ---


def parse_input(data):
    fresh, items = set(), set()
    for line in data:
        line = line.strip()
        if '-' in line:
            a,b = line.split('-')
            fresh.add((int(a), int(b)+1))
            # for x in range(int(a), int(b)+1):
            #     fresh.add(x)
            continue
        if line.strip() == "":
            continue
        items.add(int(line))
    return fresh, items


def get_input_data():
    if os.environ.get("INPUT"):
        filename = os.environ.get("INPUT")
    else:
        filename = "input.txt"

    with open(filename, "r") as f:
        return f.readlines()


if __name__ == "__main__":
    data = get_input_data()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
