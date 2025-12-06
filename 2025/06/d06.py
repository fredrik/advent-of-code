import math
from aoc import get_input
from itertools import groupby


ops = {
    "+": sum,
    "*": math.prod,
}


def solve(input, part):
    if part == 1:
        homework = parse_input(input)
        return sum([ops[op](numbers) for op, numbers in homework])
    else:
        homework = list(parse_input_again(input))
        return sum([ops[op](numbers) for op, numbers in homework])


def parse_input(input):
    o = [[] for _ in range(len(input[0].strip().split()))]
    for line in input:
        for i, x in enumerate(line.strip().split()):
            o[i].append(x)
    return [(p[-1], [int(x) for x in p[:-1]]) for p in o]


def parse_input_again(input):
    d = {}
    for i, line in enumerate(input):
        for j, c in enumerate(line):
            d[(i, j)] = c

    cols = []
    for y in range(j):
        op = d[(i, y)]
        number = "".join([d[x, y] for x in range(i)]).strip()
        cols.append((op, int(number)) if number != "" else (None, None))

    groups = []
    current = []
    for c in cols:
        if c == (None, None):
            groups.append(current)
            current = []
        else:
            current.append(c)
    if current:
        groups.append(current)

    for group in groups:
        op = group[0][0]
        yield (op, [t[1] for t in group])


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
