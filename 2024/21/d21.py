import os
import networkx
from functools import cache
from itertools import product, pairwise


def solve(input, part):
    sequences = [[x for x in line] for line in input.splitlines()]
    npad, dpad = make_pads()

    seq = set(numpad_seq(npad, "A029A"))
    print("seq:", seq)
    assert seq == {"<A^A>^^AvvvA", "<A^A^>^AvvvA", "<A^A^^>AvvvA"}

    total = 0
    for sequence in sequences:
        print("".join(sequence))
        print(sequence)

        # shortest_len = find_shortest_input_sequence(npad, dpad, sequence)
        shortest_len = min(sum(count_presses(2, npad, src, dst) for src, dst in pairwise(["A"] + sequence)))
        numeric_code = int("".join(sequence).replace("A", ""))
        total += shortest_len * numeric_code

        print(shortest_len, numeric_code, "->", shortest_len * numeric_code)
        print()

    return total


def count_presses(num_chained, graph, src, dst):
    print(f'count_presses({num_chained}, "{src}", "{dst}")')
    if num_chained == 1:
        return len(next(iter(find_paths(graph, src, dst))))
    else:
        s = []
        for sequence in find_paths(graph, src, dst):
            print(f"sequence: {sequence} ({sequence.__class__})")
            print(list(sequence))
            s.append(sum(count_presses(num_chained - 1, graph, src, mid) for mid in pairwise(["A"] + list(sequence))))
        return min(s)

        return min(
            # sum(count_presses(num_chained - 1, graph, src, mid) for mid in pairwise(["A"] + sequence))
            # for sequence in find_paths(graph, src, dst)
        )


def find_shortest_input_sequence(npad, dpad, sequence):
    shortest = 99999
    for p1 in all_sequences(npad, sequence):
        for p2 in all_sequences(dpad, p1):
            for p3 in all_sequences(dpad, p2):
                if len(p3) < shortest:
                    shortest = len(p3)

    return shortest


def all_sequences(graph, sequence):
    @cache
    def all_shortest_paths(a, b):
        return list(networkx.all_shortest_paths(graph, a, b))

    def direction(path):
        pg = networkx.path_graph(path)
        for u, v in pg.edges():
            e = graph.get_edge_data(u, v)
            yield e["direction"]

    def find_all_sequences(seq, directions):
        if len(seq) <= 1:
            yield directions
        else:
            for p in all_shortest_paths(seq[0], seq[1]):
                ps = directions + list(direction(p)) + ["A"]
                yield from find_all_sequences(seq[1:], ps)

    return list(find_all_sequences(["A"] + sequence, []))


# ---


def find_paths(graph, src, dst):
    paths = set()
    print(f"networkx.all_shortest_paths: '{src}' -> '{dst}'")
    for p in networkx.all_shortest_paths(graph, src, dst):
        pg = networkx.path_graph(p)
        path = []
        for u, v in pg.edges():
            e = graph.get_edge_data(u, v)
            path.append(e["direction"])
        path.append("A")
        paths.add("".join(path))
    return paths


def numpad_seq(graph, seq):
    paths = ["".join(subpath) for subpath in product(*[find_paths(graph, src, dst) for src, dst in pairwise(seq)])]
    min_len = min(len(path) for path in paths)
    return [path for path in paths if len(path) == min_len]


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
