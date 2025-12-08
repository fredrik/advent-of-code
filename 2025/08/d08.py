import math
from aoc import get_input
from itertools import combinations


def solve(input, part):
    points = list(parse_input(input))

    if part == 1:
        n = 1000

        circuits = []
        cl = {}  # lookup
        for d, a, b in sorted(distances(points))[:n]:
            # print(d, a, b)
            ca, cb = cl.get(a), cl.get(b)

            # print(f'ca:{ca}, cb:{cb}')

            if ca is not None and cb is None:
                circuits[ca].add(b)
                cl[b] = ca
                # print(f'added {b} to existing id {ca} -> {circuits}')

            if cb is not None and ca is None:
                circuits[cb].add(a)
                cl[a] = cb
                # print(f'added {a} to existing id {cb} -> {circuits}')

            if ca is None and cb is None:
                # neither are in a circuit.
                circuit = {a, b}
                circuits.append(circuit)
                id = len(circuits) - 1
                cl[a], cl[b] = id, id
                # print(f'add to new id {id} -> {circuits}')

            if ca is not None and cb is not None:
                if ca != cb:
                    # merge circuits by creating new and delete the two old.
                    # print(f'merde, it is a merge!')
                    # create new.
                    circuit = circuits[ca] | circuits[cb]
                    circuits.append(circuit)
                    id = len(circuits) - 1
                    # point to new.
                    for c in circuit:
                        cl[c] = id
                    # clear old.
                    circuits[ca], circuits[cb] = {}, {}
                    # print(f'merged: {ca} | {cb} = {id} -> {circuits}')

            # print()

        return math.prod(sorted((len(c) for c in circuits), reverse=True)[:3])
    else:
        return


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
