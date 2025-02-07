import os

directions = {
    "^": (0, 1),
    "v": (0, -1),
    ">": (1, 0),
    "<": (-1, 0),
}


def solve(data, part):
    instructions = list(data.strip())

    if part == 1:
        return part1(instructions)
    else:
        return part2(instructions)


def part1(instructions):
    pos = (0, 0)
    seen = set([(0, 0)])

    for i in instructions:
        dx, dy = directions[i]
        x, y = pos
        pos = (x + dx, y + dy)
        seen.add(pos)

    return len(seen)


def part2(instructions):
    pos = [(0, 0), (0, 0)]  # santa and robot.
    seen = set([(0, 0)])

    for n, i in enumerate(instructions):
        dx, dy = directions[i]
        x, y = pos[n % 2]
        pos[n % 2] = (x + dx, y + dy)
        seen.add(pos[n % 2])

    return len(seen)


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
