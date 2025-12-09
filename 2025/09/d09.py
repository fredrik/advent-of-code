from aoc import get_input
from itertools import combinations


def solve(input, part):
    points = list(parse_input(input))

    if part == 1:
        return max(area(p1, p2) for p1, p2 in combinations(points, 2))
    else:
        return


def area(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2
    return abs((p1x - p2x + 1) * (p1y - p2y + 1))


def parse_input(input):
    # return [int(x), int(y) for line in input for x,y in line.split(',')]
    for line in input:
        a, b = line.rstrip().split(",")
        yield int(a), int(b)


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
