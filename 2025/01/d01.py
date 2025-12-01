def solve(input, part):
    code = 0
    position = 50
    turns = parse_input(input)

    if part == 1:
        for turn in turns:
            position = (position + turn) % 100
            if position == 0:
                code += 1
        return code
    else:
        for turn in turns:
            if turn > 0:
                code += (position + turn) // 100
            else:
                code += (abs((100 - position) % 100) - turn) // 100
            position = (position + turn) % 100
        return code


def parse_input(input):
    """Returns list of number of turns as a signed integer."""
    lines = input.strip().split("\n")
    return [int(line[1:]) if line[0] == "R" else -int(line[1:]) for line in lines]


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
    print("part 2:", solve(input, 2))
