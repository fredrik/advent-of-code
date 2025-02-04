import os
import networkx
from functools import cache
from itertools import product, pairwise


def solve(input, part):
    depth = {
        1: 2,
        2: 25,
    }.get(part)

    sequences = ["".join([x for x in line]) for line in input.splitlines()]
    # => ["029A", ...]

    npad, dpad = make_pads()

    total = 0
    for sequence in sequences:
        shortest_path = min(
            sum(count_presses(depth, dpad, src, dst) for src, dst in pairwise("A" + path))
            for path in numpad_paths(npad, "A" + sequence)
        )
        numeric_code = int(sequence.replace("A", ""))
        total += shortest_path * numeric_code

        # print("sequence", sequence)
        # print(shortest_path, numeric_code, "->", shortest_path * numeric_code)
        # print()

    return total


def numpad_paths(graph, seq):
    paths = ["".join(subpath) for subpath in product(*[find_paths(graph, src, dst) for src, dst in pairwise(seq)])]
    min_len = min(len(path) for path in paths)
    return [path for path in paths if len(path) == min_len]


@cache
def count_presses(depth, graph, src, dst):
    if depth == 1:
        return min(len(path) for path in find_paths(graph, src, dst))
    else:
        return min(
            sum(count_presses(depth - 1, graph, a, b) for a, b in pairwise("A" + sequence))
            for sequence in find_paths(graph, src, dst)
        )


def find_paths(graph, src, dst):
    return set(
        "".join([graph.get_edge_data(u, v)["direction"] for u, v in networkx.path_graph(p).edges()] + ["A"])
        for p in networkx.all_shortest_paths(graph, src, dst)
    )


# ---


def make_pads():
    npad, dpad = networkx.DiGraph(), networkx.DiGraph()

    # numerical pad
    npad.add_edge("A", "0", direction="<")
    npad.add_edge("A", "3", direction="^")

    npad.add_edge("0", "A", direction=">")
    npad.add_edge("0", "2", direction="^")

    npad.add_edge("1", "2", direction=">")
    npad.add_edge("1", "4", direction="^")

    npad.add_edge("2", "1", direction="<")
    npad.add_edge("2", "3", direction=">")
    npad.add_edge("2", "5", direction="^")
    npad.add_edge("2", "0", direction="v")

    npad.add_edge("3", "2", direction="<")
    npad.add_edge("3", "6", direction="^")
    npad.add_edge("3", "A", direction="v")

    npad.add_edge("4", "5", direction=">")
    npad.add_edge("4", "7", direction="^")
    npad.add_edge("4", "1", direction="v")

    npad.add_edge("5", "4", direction="<")
    npad.add_edge("5", "6", direction=">")
    npad.add_edge("5", "8", direction="^")
    npad.add_edge("5", "2", direction="v")

    npad.add_edge("6", "5", direction="<")
    npad.add_edge("6", "9", direction="^")
    npad.add_edge("6", "3", direction="v")

    npad.add_edge("7", "8", direction=">")
    npad.add_edge("7", "4", direction="v")

    npad.add_edge("8", "7", direction="<")
    npad.add_edge("8", "9", direction=">")
    npad.add_edge("8", "5", direction="v")

    npad.add_edge("9", "8", direction="<")
    npad.add_edge("9", "6", direction="v")

    # directional pad
    dpad.add_edge("A", "^", direction="<")
    dpad.add_edge("A", ">", direction="v")

    dpad.add_edge("^", "A", direction=">")
    dpad.add_edge("^", "v", direction="v")

    dpad.add_edge("<", "v", direction=">")

    dpad.add_edge(">", "v", direction="<")
    dpad.add_edge(">", "A", direction="^")

    dpad.add_edge("v", "<", direction="<")
    dpad.add_edge("v", ">", direction=">")
    dpad.add_edge("v", "^", direction="^")

    return npad, dpad


# ---


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
