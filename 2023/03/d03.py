import os

directions = {
    "^": (0, 1),
    "v": (0, -1),
    ">": (1, 0),
    "<": (-1, 0),
}


def solve(data, part):
    instructions = list(data.strip())

    pos = [(0, 0), (0, 0)]  # santa and robot.
    seen = set([(0, 0)])

    for n, i in enumerate(instructions):
        dx, dy = directions[i]
        x, y = pos[n % part]
        pos[n % part] = (x + dx, y + dy)
        seen.add(pos[n % part])

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
