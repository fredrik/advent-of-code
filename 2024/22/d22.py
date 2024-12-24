from collections import defaultdict


def solve(input, part):
    if part == 1:
        return part1(input)
    else:
        return part2(input)


def part1(input):
    initial = [int(x) for x in input.splitlines()]
    return sum([find_nth(i, 2000) for i in initial])


def part2(input):
    initial = [int(x) for x in input.splitlines()]
    ns = find_all_ns(initial)
    buyers = []
    seen_seqs = set()
    for n in ns:
        seqs = defaultdict(int)  # seq -> max price
        for i, (price, diff) in enumerate(n):
            if price > 0:
                seq = tuple(map(lambda x: x[1], n[i - 3 : i + 1]))
                if seq not in seqs:
                    seqs[seq] = price
                    seen_seqs.add(seq)
        buyers.append(seqs)

    bananas = {}
    for seq in seen_seqs:
        bananas[seq] = sum([buyer[seq] for buyer in buyers])

    return max(bananas.values())


def find_all_ns(initial):
    ns = []

    def price(secret):
        return secret % 10

    for i in initial:
        secret = i
        prev = None
        n = [(price(secret), None)]  # initial price has no diff
        for _ in range(2000):
            prev = secret
            secret = next_secret(secret)
            diff = price(secret) - price(prev)
            n.append((price(secret), diff))
        ns.append(n)
    return ns


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
    print("part 1:", solve(input, 1))
    print("part 2:", solve(input, 2))

    # print(test_next_secret(123))
    # print(part2("123\n"))
