import networkx
import itertools


def solve(input, part):
    sequences = [[x for x in line] for line in input.splitlines()]
    npad, dpad = make_pads()

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

    def find_presses(g, sequence):
        def presses():
            # first, start at A and move to first input
            # print("".join(directions("A", sequence[0])), end="")
            yield directions(g, "A", sequence[0])
            yield "A"
            # move to each input
            for k1, k2 in pairs(sequence):
                # print("#", k1, k2)
                # print("".join(directions(k1, k2)), end="")
                yield directions(g, k1, k2)
                yield "A"

        return list(itertools.chain.from_iterable(presses()))

    # @cache
    def all_shortest_paths(g, sequence, paths=[]):
        if len(sequence) == 1:
            return

        for path in networkx.all_shortest_paths(g, sequence[0], sequence[1]):
            if new_path := all_shortest_paths(g, sequence[1:], paths + [path]):
                print("new_path", new_path)
                paths.append(new_path)

        return paths

        # if len(sequence) == 2:
        #     return list(networkx.all_shortest_paths(g, sequence[0], sequence[1]))

        # paths = []
        # for path in networkx.all_shortest_paths(g, sequence[0], sequence[1]):
        #     # print("call", sequence[1:])
        #     paths.append(list(path) + all_shortest_paths(g, sequence[1:]))
        # return paths

    def find_all_presses(g, sequence):
        def presses():
            for path in all_shortest_paths(g, sequence):
                yield path
                # yield presses_for(g, path)

        return list(itertools.chain.from_iterable(presses()))

    def presses_for(g, path):
        print("presses for", path)
        pg = networkx.path_graph(path)
        for u, v in pg.edges():
            e = g.get_edge_data(u, v)
            yield e["direction"]
        yield "A"

    def sort_sequence(s):
        return "A".join(
            ["".join(x) for x in map(reversed, map(sorted, "".join(s).split("A")))]
        )

    def find_shortest_input_sequence(sequence):
        # find the shortest sequence we need to press
        # in order to instruct the nearest robot to press
        # the sequence that will instruct the next robot, and so on.

        p = find_presses(npad, sequence)
        print("".join(p))

        p = find_all_presses(npad, sequence)
        # print("".join(p))
        print(p)

        # ===

        # p2 = find_presses(dpad, sort_sequence(p1))
        # print("".join(sort_sequence(p2)))

        shortest = 999
        # for q in find_all_presses(dpad, p2):
        #     continue
        #     for r in find_all_presses(dpad, q):
        #         print("".join((r)))
        #         if len(r) < shortest:
        #             shortest = len(r)

        return shortest

    sum = 0
    for sequence in sequences[:1]:
        numeric_code = int("".join(sequence).replace("A", ""))
        shortest_len = find_shortest_input_sequence(sequence)

        print(shortest_len, numeric_code, "->", shortest_len * numeric_code)
        sum += shortest_len * numeric_code

        print()

    return sum


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
