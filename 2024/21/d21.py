from aoc import get_input, all_shortest_paths
from functools import cache
from itertools import product, pairwise

npad = {
    "A": {"0": "<", "3": "^"},
    "0": {"A": ">", "2": "^"},
    "1": {"2": ">", "4": "^"},
    "2": {"1": "<", "3": ">", "5": "^", "0": "v"},
    "3": {"2": "<", "6": "^", "A": "v"},
    "4": {"5": ">", "7": "^", "1": "v"},
    "5": {"4": "<", "6": ">", "8": "^", "2": "v"},
    "6": {"5": "<", "9": "^", "3": "v"},
    "7": {"8": ">", "4": "v"},
    "8": {"7": "<", "9": ">", "5": "v"},
    "9": {"8": "<", "6": "v"},
}
dpad = {
    "A": {"^": "<", ">": "v"},
    "^": {"A": ">", "v": "v"},
    "<": {"v": ">"},
    ">": {"v": "<", "A": "^"},
    "v": {"<": "<", ">": ">", "^": "^"},
}

depths = {
    1: 2,
    2: 25,
}


def solve(input, part):
    sequences = parse_input(input)
    return sum_of_complexities(sequences, depths[part])


def sum_of_complexities(sequences, depth):
    return sum(
        numeric_code(sequence) * fewest_presses(sequence, depth)
        for sequence in sequences
    )


def numeric_code(sequence):
    return int(sequence.replace("A", ""))


def fewest_presses(sequence, depth):
    return min(
        sum(count_presses(depth, src, dst) for src, dst in pairwise("A" + path))
        for path in numpad_paths(npad, "A" + sequence)
    )


@cache
def count_presses(depth, src, dst):
    if depth == 1:
        return min(len(path) for path in find_paths(dpad, src, dst))
    else:
        return min(
            sum(count_presses(depth - 1, a, b) for a, b in pairwise("A" + sequence))
            for sequence in find_paths(dpad, src, dst)
        )


def numpad_paths(graph, seq):
    paths = [
        "".join(subpath)
        for subpath in product(
            *[find_paths(graph, src, dst) for src, dst in pairwise(seq)]
        )
    ]
    min_len = min(len(path) for path in paths)
    return [path for path in paths if len(path) == min_len]


def find_paths(graph, src, dst):
    paths = all_shortest_paths(graph, src, dst)
    return set(
        "".join(graph[u][v] for u, v in zip(path, path[1:])) + "A" for path in paths
    )


def parse_input(input):
    return ["".join([x.strip() for x in line]) for line in input]


if __name__ == "__main__":
    input = get_input()
    print("part 1:", solve(input, 1))
    print("part 2:", solve(input, 2))
