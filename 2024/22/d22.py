def solve(input, part):
    initial = [int(x) for x in input.splitlines()]
    return sum([find_nth(i, 2000) for i in initial])


def find_nth(i, n):
    for _ in range(n):
        i = next_secret(i)
    return i


def next_secret(i):
    a = ((i * 64) ^ i) % 16777216
    b = ((a // 32) ^ a) % 16777216
    c = ((b * 2048) ^ b) % 16777216
    return c


# ---


def test_next_secret(i):
    for _ in range(10):
        i = next_secret(i)
        print(i)


# ---


import os


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        filename = "input.txt"
    else:
        filename = "input.small"

    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    input = choose_input()
    # print(test_next_secret(123))
    print("part 1:", solve(input, 1))
    # print("part 2:", solve(input, 2))
