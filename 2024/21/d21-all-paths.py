import os
import networkx


def solve(input, part):
    sequences = [[x for x in line] for line in input.splitlines()]
    npad, dpad = make_pads()

    sum = 0
    for sequence in sequences:
        print("".join(sequence))

        shortest_len = find_shortest_input_sequence(npad, dpad, sequence)
        numeric_code = int("".join(sequence).replace("A", ""))
        sum += shortest_len * numeric_code

        print(shortest_len, numeric_code, "->", shortest_len * numeric_code)
        print()

    return sum


def find_shortest_input_sequence(npad, dpad, sequence):
    shortest = 99999
    for p1 in all_sequences(npad, sequence):
        print("p1", p1)
        for p2 in all_sequences(dpad, p1):
            print("p2", p2)
            for p3 in all_sequences(dpad, p2):
                print("p3", p3)
                if len(p3) < shortest:
                    shortest = len(p3)
                    print("new shortest", len(p3))
    return shortest


def all_sequences(graph, sequence):
    # @cache
    def all_shortest_paths(a, b):
        return list(networkx.all_shortest_paths(graph, a, b))

    def direction(path):
        pg = networkx.path_graph(path)
        for u, v in pg.edges():
            e = graph.get_edge_data(u, v)
            yield e["direction"]

    def find_all_sequences(seq, directions):
        if len(seq) == 1:
            yield directions
        else:
            for p in all_shortest_paths(seq[0], seq[1]):
                yield from find_all_sequences(seq[1:], directions[:-1] + list(direction(p)) + ["A"])

    return list(find_all_sequences(sequence, []))

    # return list(itertools.chain.from_iterable(find_all_sequences(sequence, [])))
    # all = list(find_all_sequences(sequence, []))
    # return all
    # return [x for l in all for x in l]
    # return [p for part in list(find_all_sequences(sequence, [])) for p in part]


# def find_presses(g, sequence):
#     def presses():
#         # first, start at A and move to first input
#         # print("".join(directions("A", sequence[0])), end="")
#         yield directions(g, "A", sequence[0])
#         yield "A"
#         # move to each input
#         for k1, k2 in pairs(sequence):
#             # print("#", k1, k2)
#             # print("".join(directions(k1, k2)), end="")
#             yield directions(g, k1, k2)
#             yield "A"

#     return list(itertools.chain.from_iterable(presses()))


def pairs(s):
    # ['0', '2', '9', 'A'] => [('0', '2'), ('2', '9'), ('9', 'A')]
    a, b = iter(s), iter(s)
    next(b)
    return list(zip(a, b))


def directions(g, k1, k2):
    path = networkx.shortest_path(g, k1, k2)
    pg = networkx.path_graph(path)
    for u, v in pg.edges():
        e = g.get_edge_data(u, v)
        yield e["direction"]


def sort_sequence(s):
    return "A".join(["".join(x) for x in map(reversed, map(sorted, "".join(s).split("A")))])


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
    # print("part 2:", solve(input, 2))
