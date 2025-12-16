from aoc import get_input


value = {"(": 1, ")": -1}


def solve(data, part):
    parens = list(data.strip())

    if part == 1:
        return part1(parens)
    else:
        return part2(parens)


def part1(parens):
    return sum(value[p] for p in parens)


def part2(parens):
    floor = 1
    floors = [floor := floor + value[p] for p in parens]
    return floors.index(-1)


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
