from aoc import get_input, find_paths


def solve(input, part):
    graph = parse_input(input)

    if part == 1:
        return len(find_paths(graph, "you", "out"))
    else:
        return


def parse_input(input):
    graph = {}
    for line in input:
        left, right = line.split(":")
        graph[left] = set(r.strip() for r in right.strip().split(" "))
    return graph


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
