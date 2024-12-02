def part_1_functional(input):
    parsed_input = (list(map(int, line.split())) for line in input.strip().splitlines())
    safe_reports = filter(
        lambda report: report_is_safe(report),
        parsed_input,
    )
    print(len(list(safe_reports)))


def part_1_imperative(input):
    safe_count = 0
    for line in input.strip().splitlines():
        report = list(map(int, line.split()))
        if report_is_safe(report):
            safe_count += 1
    print(safe_count)


def part_2_imperative(input):
    safe_count = 0
    for line in input.strip().splitlines():
        report = list(map(int, line.split()))
        if report_is_somewhat_safe(report):
            safe_count += 1
    print(safe_count)


def report_is_somewhat_safe(levels):
    for i in range(len(levels)):
        copy = levels.copy()
        copy.pop(i)
        if report_is_safe(copy):
            return True


def report_is_safe(report):
    r = range(len(report) - 1)  # a reusable range!
    is_increasing = all(report[i] < report[i + 1] for i in r)
    is_decreasing = all(report[i] > report[i + 1] for i in r)
    differ_by_some = all((abs(report[i] - report[i + 1]) in [1, 2, 3]) for i in r)
    return (is_increasing or is_decreasing) and differ_by_some


# ---

small_input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def choose_input():
    import os

    if os.environ.get("AOC_INPUT_FILE"):
        with open(os.environ.get("AOC_INPUT_FILE"), "r") as file:
            return file.read()
    else:
        return small_input


if __name__ == "__main__":
    input = choose_input()
    part_1_functional(input)
    part_1_imperative(input)
    part_2_imperative(input)

# usage:
#
# for small input
# $> uv run d02.py
#
# for large input
# $> AOC_INPUT_FILE=input.txt uv run d02.py
