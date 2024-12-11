import os


def part2(input):
    stones = [int(x) for x in input.strip().split(" ")]

    count = 0
    for stone in stones:
        count += count_stones(stone, 75)
    return count


memo = {}


def count_stones(stone, generations):
    key = (stone, generations)
    if key in memo:
        return memo[key]
    else:
        memo[key] = count_stones_actual(stone, generations)
        return memo[key]


def count_stones_actual(stone, generations):
    if generations == 0:
        return 1
    val = stone
    if val == 0:
        return count_stones(1, generations - 1)
    elif len(str(val)) % 2 == 0:
        strval = str(val)
        left = int(strval[0 : len(strval) // 2])
        right = int(strval[len(strval) // 2 :])
        return count_stones(left, generations - 1) + count_stones(right, generations - 1)
    else:
        return count_stones(val * 2024, generations - 1)


# ----------------


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        with open("input.txt", "r") as f:
            return f.read()
    else:
        with open("input.mini", "r") as f:
            return f.read()


if __name__ == "__main__":
    input = choose_input()
    print(part2(input))
