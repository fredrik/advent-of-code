import os


def part1(input):
    values = parse_input(input)

    sum = 0
    for key, value in values.items():
        if solve_test_case(key, value):
            sum += key
    return sum


def part2(input):
    values = parse_input(input)

    sum = 0
    for key, value in values.items():
        if solve_test_case(key, value, part2=True):
            sum += key
    return sum


def solve_test_case(testvalue, numbers, part2=False):
    sums = [numbers.pop(0)]
    while len(numbers) > 0:
        x = numbers.pop(0)
        new_sums = []
        for sum in sums:
            new_sums.append(sum + x)
            new_sums.append(sum * x)
            if part2:
                new_sums.append(int(str(sum) + str(x)))
        sums = new_sums
    if testvalue in sums:
        return True


def parse_input(input):
    values = {}
    for line in input.strip().split("\n"):
        testvalue, numbers = line.split(":")
        values[int(testvalue)] = [int(x) for x in numbers.strip().split(" ")]
    return values


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        with open("input.txt", "r") as f:
            return f.read()
    else:
        with open("input.small", "r") as f:
            return f.read()


if __name__ == "__main__":
    input = choose_input()
    print(part1(input))
    print(part2(input))
