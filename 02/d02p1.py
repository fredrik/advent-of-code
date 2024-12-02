# input = """
# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# """

with open("input.txt", "r") as file:
    input = file.read()


def report_is_safe(report):
    r = range(len(report) - 1)  # a reusable range!
    is_increasing = all(report[i] < report[i + 1] for i in r)
    is_decreasing = all(report[i] > report[i + 1] for i in r)
    differ_by_some = all((abs(report[i] - report[i + 1]) in [1, 2, 3]) for i in r)
    return (is_increasing or is_decreasing) and differ_by_some


def main():
    safe_count = 0
    for line in input.strip().splitlines():
        report = list(map(int, line.split()))
        if report_is_safe(report):
            safe_count += 1
    print(safe_count)


if __name__ == "__main__":
    main()
