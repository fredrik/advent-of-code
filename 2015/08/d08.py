from aoc import get_input


def solve(data, part):
    count = 0
    for line in data.splitlines():
        if part == 1:
            escaped = bytes(line, "utf-8").decode("unicode_escape")
            a = len(line)
            b = len(escaped) - 2
        else:
            a = len(line) + 2 + len([x for x in line if x in ["\\", '"']])
            b = len(line)
        count = count + a - b
    return count


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
