import math
from aoc import get_input


ops = {
    "+": sum,
    "*": math.prod,
}


def solve(input, part):
    homework = parse_input(input)

    if part == 1:
        print(homework)

        return sum([ops[op](numbers) for op, numbers in homework])

    else:
        return


def parse_input(input):
    o = [[] for _ in range(len(input[0].strip().split()))]
    for line in input:
        for i, x in enumerate(line.strip().split()):
            o[i].append(x)
    return [(p[-1], [int(x) for x in p[:-1]]) for p in o]


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
