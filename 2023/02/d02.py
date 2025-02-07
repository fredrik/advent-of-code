import os
import math


def solve(data, part):
    parts = [line.split("x") for line in data.splitlines()]
    measurements = [list(map(int, p)) for p in parts]

    if part == 1:
        return part1(measurements)
    else:
        return part2(measurements)


def part1(measurements):
    def paper(measurement):
        L, W, H = measurement
        a, b, _ = sorted(measurement)  # a*b is size of smallest side
        return 2 * L * W + 2 * W * H + 2 * H * L + a * b

    return sum(paper(m) for m in measurements)


def part2(measurements):
    def wrapping(measurement):
        a, b, _ = sorted(measurement)
        perimeter = 2 * (a + b)
        return perimeter

    def bow(measurement):
        return math.prod(measurement)

    return sum(wrapping(m) + bow(m) for m in measurements)


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
