from collections import defaultdict


def solve(input, part):
    conns = parse_input(input)
    tkeys = set(k for k in conns.keys() if k.startswith("t"))

    threes = set()
    for k in tkeys:
        for c in conns[k]:
            shared = conns[k] & conns[c]
            for s in shared:
                t = tuple(sorted((k, c, s)))
                threes.add(t)

    # for t in sorted(list(threes)):
    #     print(t)

    return len(threes)


# ---


def parse_input(input):
    conns = defaultdict(set)
    for line in input.splitlines():
        a, b = line.split("-")
        conns[a].add(b)
        conns[b].add(a)

    return conns


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
    # print("part 2:", solve(input, 2))
