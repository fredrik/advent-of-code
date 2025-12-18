from aoc import get_input


def solve(data, part):
    target = int(data.strip())

    if part == 1:
        return part1(target)
    else:
        return part2(target)


def sigma(h):
    total = 0
    i = 1
    while i * i <= h:
        if h % i == 0:
            total += i
            if i != h // i:
                total += h // i
        i += 1
    return total


def sigma2(h):
    total = 0
    min_divisor = h / 50
    i = 1
    while i * i <= h:
        if h % i == 0:
            if i >= min_divisor:
                total += i
            other = h // i
            if other != i and other >= min_divisor:
                total += other
        i += 1
    return total


def part1(target):
    for h in range(1, target):
        if 10 * sigma(h) >= target:
            return h


def part2(target):
    for h in range(1, target):
        if 11 * sigma2(h) >= target:
            return h


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
