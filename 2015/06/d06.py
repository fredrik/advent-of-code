from collections import defaultdict
import os
import re

pattern = re.compile(r"^([a-z ]+) (\d+),(\d+) through (\d+),(\d+)$")


def solve(data, part):
    grid = defaultdict(int)  # keyed by tuple (x,y)

    for line in data.splitlines():
        # parse
        m = pattern.match(line)
        action = m.group(1)
        a, b, c, d = map(int, m.group(2, 3, 4, 5))
        assert a <= c, f"{a} <= {c}"
        assert b <= d, f"{b} <= {d}"

        # act
        for p in points_between((a, b), (c, d)):
            match action:
                case "turn on":
                    if part == 1:
                        grid[p] = 1
                    else:
                        grid[p] += 1
                case "turn off":
                    if part == 1:
                        grid[p] = 0
                    else:
                        grid[p] = max(0, grid[p] - 1)
                case "toggle":
                    if part == 1:
                        grid[p] = 1 if grid[p] == 0 else 0
                    else:
                        grid[p] += 2

    # sum
    return sum(grid.values())


def points_between(q, r):
    for i in range(q[0], r[0] + 1):
        for j in range(q[1], r[1] + 1):
            yield (i, j)


# ---s


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
