import os

directions = {
    "^": (0, 1),
    "v": (0, -1),
    ">": (1, 0),
    "<": (-1, 0),
}


def solve(data, part):
    if part == 1:
        return part1(data)
    else:
        return part2(data)


def part1(data):
    instructions = list(data.strip())

    pos = (0, 0)
    seen = set([pos])

    for i in instructions:
        dx, dy = directions[i]
        x, y = pos
        pos = (x + dx, y + dy)
        seen.add(pos)

    return len(seen)


def part2(data):
    return 0


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
