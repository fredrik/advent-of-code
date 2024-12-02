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


def report_is_safe(levels):
    is_increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    differ_by_some = all(
        (abs(levels[i] - levels[i + 1]) in [1, 2, 3]) for i in range(len(levels) - 1)
    )
    return (is_increasing or is_decreasing) and differ_by_some


def report_is_somewhat_safe(levels):
    for i in range(len(levels)):
        copy = levels.copy()
        copy.pop(i)
        if report_is_safe(copy):
            return True


def main():
    safe = []
    lines = input.strip().splitlines()
    for line in lines:
        levels = list(map(int, line.split()))
        if report_is_somewhat_safe(levels):
            safe.append(levels)

    print(len(safe))


if __name__ == "__main__":
    main()
