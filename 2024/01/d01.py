from aoc import get_input
from collections import defaultdict


def solve(input, part):
    xs, ys = parse_input(input)

    if part == 1:
        return sum(abs(x - y) for x, y in zip(sorted(xs), sorted(ys)))
    else:
        freq = defaultdict(int)
        for y in ys:
            freq[y] += 1
        return sum(x * freq[x] for x in xs)


def parse_input(input):
    xs, ys = [], []
    for line in input:
        x, y = map(int, line.split())
        xs.append(x)
        ys.append(y)
    return xs, ys


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
