def solve(input, part):
    code = 0
    position = 50
    parsed = parse_input(input)
    for d, n in parsed:
        if d == "R":
            position = (position + n) % 100
        if d == "L":
            position = (position - n) % 100
        print(f"dial is at {position}")
        if position == 0:
            code += 1
    return code


def parse_input(input):
    # return tuples of direction and number of turns
    lines = input.strip().split("\n")
    return [(line[0], int(line[1:])) for line in lines]


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
    print("part 1:", solve(input, 1))
    # print("part 2:", solve(input, 2))
