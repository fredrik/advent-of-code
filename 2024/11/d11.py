from aoc import get_input


def solve(input, part):
    stones = parse_input(input)

    if part == 1:
        for i in range(25):
            stones = blink(stones)
        return len(stones)
    else:
        count = 0
        for stone in stones:
            count += count_stones(stone, 75)
        return count


def blink(stones):
    insertions = []
    for i in range(len(stones)):
        val = stones[i]
        strval = str(val)
        if val == 0:
            stones[i] = 1
        elif len(strval) % 2 == 0:
            stones[i] = int(strval[0 : len(strval) // 2])
            insertions.append([i + 1, int(strval[len(strval) // 2 :])])
        else:
            stones[i] = val * 2024
    made = 0
    for insertion in insertions:
        stones.insert(insertion[0] + made, insertion[1])
        made += 1
    return stones


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
        return count_stones(left, generations - 1) + count_stones(
            right, generations - 1
        )
    else:
        return count_stones(val * 2024, generations - 1)


def parse_input(input):
    return [int(x) for x in input[0].strip().split(" ")]


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
