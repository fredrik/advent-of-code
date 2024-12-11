import os


def part1(input):
    stones = [int(x) for x in input.strip().split(" ")]
    for i in range(25):
        stones = blink(stones)
    return len(stones)


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
    print(part1(input))
