import os
from itertools import combinations


def solve(input, part):
    fresh, items = parse_input(input)

    if part == 1:
        return sum(is_fresh(i, fresh) for i in items)
    else:
        while True:
            new_fresh = flatten_fresh(fresh)
            if new_fresh == fresh:
                break
            fresh = new_fresh
        return sum(b - a for a, b in fresh)


def is_fresh(i, fresh):
    for a, b in fresh:
        if i >= a and i <= b:
            return True
    return False


def flatten_fresh(fresh):
    create, delete = set(), set()
    for x, y in combinations(fresh, 2):
        if inside(x, y):
            delete.add(x)
            continue
        if inside(y, x):
            delete.add(y)
            continue
        if overlap(x, y):
            delete.add(x)
            delete.add(y)
            create.add(make_overlap(x, y))

        # default: keep
        create.add(x)
        create.add(y)
    return create - delete


def make_overlap(x, y):
    a, b = x
    c, d = y
    return (min(a, c), max(b, d))


def overlap(x, y):
    a, b = x
    c, d = y
    return (a < c and b >= c and b <= d) or (c < a and d >= a and d <= b)


def inside(x, y):
    """
    Is x inside y?
    """
    a, b = x
    c, d = y
    if a >= c and b <= d:
        return True


# ---


def parse_input(data):
    fresh, items = set(), set()
    for line in data:
        line = line.strip()
        if "-" in line:
            a, b = line.split("-")
            fresh.add((int(a), int(b) + 1))
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
