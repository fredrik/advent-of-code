import os
import networkx as nx


EAST = (0, 1)
WEST = (0, -1)
NORTH = (-1, 0)
SOUTH = (1, 0)


def solve(input, part):
    grid, start, end = parse_grid(input)
    graph = make_graph(grid)

    if part == 1:
        return part1(graph, start, end)
    else:
        return part2(graph, start, end, grid)


def part1(graph, start, end):
    path = nx.shortest_path(graph, (start, EAST), end, weight="weight")
    return nx.path_weight(graph, path, "weight")


def part2(graph, start, end, grid):
    paths = nx.all_shortest_paths(graph, (start, EAST), end, weight="weight")
    seats = set(node for path in paths for node, _ in path[:-1])
    return len(seats)


# ---


def parse_grid(input):
    grid, start, end = {}, None, None
    for row, line in enumerate(input.strip().split("\n")):
        for col, c in enumerate([c for c in line.strip()]):
            grid[(row, col)] = c
            if c == "S":
                start = (row, col)
            if c == "E":
                end = (row, col)

    return grid, start, end


def make_graph(grid):
    graph = nx.DiGraph()

    for point in grid:
        if grid[point] == "#":
            continue

        if grid[point] == "E":
            # end edge-case
            graph.add_node(point)
            graph.add_edge((point, EAST), point, weight=0)
            graph.add_edge((point, WEST), point, weight=0)
            graph.add_edge((point, NORTH), point, weight=0)
            graph.add_edge((point, SOUTH), point, weight=0)

        # add a node for each direction we can face.
        graph.add_node((point, EAST))
        graph.add_node((point, WEST))
        graph.add_node((point, NORTH))
        graph.add_node((point, SOUTH))

        # add edges for turning.
        graph.add_edge((point, EAST), (point, NORTH), weight=1000)
        graph.add_edge((point, EAST), (point, SOUTH), weight=1000)
        graph.add_edge((point, WEST), (point, NORTH), weight=1000)
        graph.add_edge((point, WEST), (point, SOUTH), weight=1000)
        graph.add_edge((point, NORTH), (point, WEST), weight=1000)
        graph.add_edge((point, NORTH), (point, EAST), weight=1000)
        graph.add_edge((point, SOUTH), (point, EAST), weight=1000)
        graph.add_edge((point, SOUTH), (point, WEST), weight=1000)

        for p, d in neighbours(grid, point):
            # point and direction of reachable neighbour.
            graph.add_edge((point, d), (p, d), weight=1)

    return graph


def neighbours(grid, point):
    directions = [EAST, WEST, NORTH, SOUTH]
    r, c = point
    for d in directions:
        dr, dc = d
        n = (r + dr, c + dc)
        if grid.get(n) in [".", "E"]:
            yield n, d


# --- input basics ---


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        filename = "input.txt"
    else:
        filename = "input.small"

    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    input = choose_input()
    print("part 1", solve(input, 1))
    print("part 2", solve(input, 2))
