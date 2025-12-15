from aoc import get_input


def solve(input, part):
    reports = parse_input(input)

    if part == 1:
        return len([r for r in reports if report_is_safe(r)])
    else:
        return len([r for r in reports if report_is_somewhat_safe(r)])


def report_is_safe(report):
    r = range(len(report) - 1)  # a reusable range!
    is_increasing = all(report[i] < report[i + 1] for i in r)
    is_decreasing = all(report[i] > report[i + 1] for i in r)
    differ_by_some = all((abs(report[i] - report[i + 1]) in [1, 2, 3]) for i in r)
    return (is_increasing or is_decreasing) and differ_by_some


def report_is_somewhat_safe(report):
    for i in range(len(report)):
        if report_is_safe(report[:i] + report[i + 1 :]):
            return True


def parse_input(input):
    return (list(map(int, line.split())) for line in input)


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
