from aoc import get_input

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


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
