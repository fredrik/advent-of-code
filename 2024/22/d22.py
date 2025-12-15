from aoc import get_input

from collections import defaultdict


def solve(input, part):
    initial = parse_input(input)

    if part == 1:
        return sum([find_nth(i, 2000) for i in initial])
    else:
        ns = find_all_ns(initial)
        buyers = []
        seen_seqs = set()
        for n in ns:
            seqs = defaultdict(int)
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
        n = [(price(secret), None)]
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


def parse_input(input):
    return [int(x.strip()) for x in input]


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
