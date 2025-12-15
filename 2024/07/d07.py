from aoc import get_input


def solve(input, part):
    values = parse_input(input)

    total = 0
    for key, value in values.items():
        if solve_test_case(key, value, part2=(part == 2)):
            total += key
    return total


def solve_test_case(testvalue, numbers, part2=False):
    sums = [numbers.pop(0)]
    while len(numbers) > 0:
        x = numbers.pop(0)
        new_sums = []
        for s in sums:
            new_sums.append(s + x)
            new_sums.append(s * x)
            if part2:
                new_sums.append(int(str(s) + str(x)))
        sums = new_sums
    if testvalue in sums:
        return True


def parse_input(input):
    values = {}
    for line in input:
        testvalue, numbers = line.split(":")
        values[int(testvalue)] = [int(x) for x in numbers.strip().split(" ")]
    return values


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
