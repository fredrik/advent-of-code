from aoc import get_input, find_paths, count_paths
from collections import defaultdict


def solve(input, part):
    graph = parse_input(input)

    if part == 1:
        return len(find_paths(graph, "you", "out"))
    else:
        return (
            count_paths(graph, "svr", "dac")
            * count_paths(graph, "dac", "fft")
            * count_paths(graph, "fft", "out")
        ) + (
            count_paths(graph, "svr", "fft")
            * count_paths(graph, "fft", "dac")
            * count_paths(graph, "dac", "out")
        )


def parse_input(input):
    graph = defaultdict(set)
    for line in input:
        left, right = line.split(":")
        graph[left] = set(r.strip() for r in right.strip().split(" "))
    return graph


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
