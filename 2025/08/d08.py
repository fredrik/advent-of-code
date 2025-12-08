import math
from aoc import get_input
from itertools import combinations


def solve(input, part):
    points = list(parse_input(input))

    if part == 1:
        n = 1000 # iterations.
        circuits, lookup = [], {}
        for _, a, b in sorted(distances(points))[:n]:
            circuits, lookup = attach(a, b, circuits, lookup)
        return math.prod(sorted((len(c) for c in circuits), reverse=True)[:3])
    else:
        m = 1000 # input size.
        circuits, lookup = [], {}
        for _, a, b in sorted(distances(points)):
            circuits, lookup = attach(a, b, circuits, lookup)
            if len(set(lookup.values())) == 1 and len(circuits[list(set(lookup.values()))[0]]) == m:
                return a[0] * b[0]



def attach(a, b, circuits, lookup):
    ca, cb = lookup.get(a), lookup.get(b)

    if ca is not None and cb is None:
        circuits[ca].add(b)
        lookup[b] = ca

    if cb is not None and ca is None:
        circuits[cb].add(a)
        lookup[a] = cb

    if ca is None and cb is None:
        # neither are in a circuit.
        circuit = {a, b}
        circuits.append(circuit)
        id = len(circuits) - 1
        lookup[a], lookup[b] = id, id

    if ca is not None and cb is not None:
        if ca != cb:
            # merde, it is a merge!
            # merge circuits by creating new and delete the two old.
            # create new.
            circuit = circuits[ca] | circuits[cb]
            circuits.append(circuit)
            id = len(circuits) - 1
            # point to new.
            for c in circuit:
                lookup[c] = id
            # clear old.
            circuits[ca], circuits[cb] = {}, {}

    return circuits, lookup


def distances(points):
    for a, b in combinations(points, 2):
        yield (distance(a, b), a, b)


def distance(a, b):
    return math.sqrt(sum((aa - bb) ** 2 for aa, bb in zip(a, b)))


def parse_input(input):
    for line in input:
        yield tuple(map(int, (part for part in line.split(","))))


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
