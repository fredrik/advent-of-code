import heapq
import os

from collections import defaultdict


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
    shortest_length, shortest_paths = find_shortest_paths(graph, (start, EAST), end)
    return shortest_length


def part2(graph, start, end, grid):
    shortest_length, shortest_paths = find_shortest_paths(graph, (start, EAST), end)
    seats = set(node for path in shortest_paths for node, _ in path[:-1])
    return len(seats)


# ---


# dijsktra's algorithm.
def find_shortest_paths(graph, start, end):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    predecessors = defaultdict(list)

    def reconstruct_all_paths(node):
        if node == start:
            return [[start]]

        paths = []
        for pre in predecessors[node]:
            for path in reconstruct_all_paths(pre):
                paths.append(path + [node])

        return paths

    # priority queue.
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        if current_node == end:
            continue

        for neighbour, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(pq, (distance, neighbour))
                predecessors[neighbour] = [current_node]

            if distance == distances[neighbour]:
                if current_node not in predecessors[neighbour]:
                    predecessors[neighbour].append(current_node)

    if distances[end] == float("inf"):
        return None, []

    return distances[end], reconstruct_all_paths(end)


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
    graph = defaultdict(dict)

    def add_edge(node, neighbour, weight):
        graph[node][neighbour] = weight

    for point in grid:
        if grid[point] == "#":
            continue

        if grid[point] == "E":
            # edge-case for end of graph.
            # it doesn't matter which way we're facing.
            graph[point] = {}
            add_edge((point, EAST), point, weight=0)
            add_edge((point, WEST), point, weight=0)
            add_edge((point, NORTH), point, weight=0)
            add_edge((point, SOUTH), point, weight=0)
            continue

        # add expensively weighted edges for turning.
        add_edge((point, EAST), (point, NORTH), weight=1000)
        add_edge((point, EAST), (point, SOUTH), weight=1000)
        add_edge((point, WEST), (point, NORTH), weight=1000)
        add_edge((point, WEST), (point, SOUTH), weight=1000)
        add_edge((point, NORTH), (point, WEST), weight=1000)
        add_edge((point, NORTH), (point, EAST), weight=1000)
        add_edge((point, SOUTH), (point, EAST), weight=1000)
        add_edge((point, SOUTH), (point, WEST), weight=1000)

        for p, d in neighbours(grid, point):
            # point and direction of reachable neighbour.
            # this is moving 'forward', so the weight is 1.
            add_edge((point, d), (p, d), weight=1)

    return graph


def neighbours(grid, point):
    directions = [EAST, WEST, NORTH, SOUTH]
    r, c = point
    for dr, dc in directions:
        n = (r + dr, c + dc)
        if grid.get(n) in [".", "E"]:
            yield n, (dr, dc)


# ---


def get_input_data():
    if os.environ.get("INPUT"):
        filename = os.environ.get("INPUT")
    else:
        filename = "input.txt"

    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    data = get_input_data()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
