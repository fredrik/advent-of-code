import os
from collections import defaultdict


def solve(input, part2=False):
    grid, lookup = parse_grid(input)
    graph = make_graph(grid)
    regions = find_regions(grid, graph)

    print_grid(grid)
    print_lookup(lookup)
    print_regions(regions)
    # print_graph(graph)

    price = 0
    for region in regions:
        area = len(region)

        perimeter = 0
        for x, y in region:
            perimeter += 4 - len(graph[(x, y)])

        price += area * perimeter
        print(
            "region",
            region,
            "area",
            area,
            "perimeter",
            perimeter,
            "price",
            area * perimeter,
        )

    return price


def find_regions(grid, graph):
    regions = []
    seen = set()
    for y in grid:
        for x in grid[y]:
            if (x, y) in seen:
                continue
            region = all_connected_nodes(graph, x, y, set())
            regions.append(region)
            for node in region:
                seen.add(node)
    return regions


def all_connected_nodes(graph, x, y, seen):
    nodes = [(x, y)]
    seen.add((x, y))
    for node in graph[(x, y)]:
        if node not in seen:
            seen.add(node)
            nodes += all_connected_nodes(graph, *node, seen)
    return nodes


def print_grid(grid):
    for y in grid:
        for x in grid[y]:
            print(grid[y][x], end="")
        print()
    print()


def print_lookup(lookup):
    for c in lookup:
        print(c, lookup[c])
    print()


def print_regions(regions):
    pass


def parse_grid(input):
    grid = defaultdict(dict)
    lookup = defaultdict(set)
    for y, line in enumerate(input.strip().split("\n")):
        grid[y] = defaultdict(str)
        for x, c in enumerate([c for c in line.strip()]):
            grid[y][x] = c
            lookup[c].add((x, y))
    return grid, lookup


# adjacency graph
def make_graph(grid):
    graph = defaultdict(list)
    for y in grid:
        for x in grid[y]:
            graph[(x, y)] = list(neighbours(grid, (x, y)))
    return graph


# connected plots of the same type
def neighbours(grid, coords):
    directions = [
        (0, -1),  # up
        (0, 1),  # down
        (-1, 0),  # left
        (1, 0),  # right
    ]
    for dx, dy in directions:
        nx, ny = coords[0] + dx, coords[1] + dy
        if oob(grid, (nx, ny)):
            continue
        if xy(grid, *coords) == xy(grid, nx, ny):
            yield (nx, ny)


def xy(grid, x, y):
    return grid[y][x]


def oob(grid, coords):
    max_x, max_y = len(grid[0]), len(grid)
    return coords[0] < 0 or coords[0] >= max_x or coords[1] < 0 or coords[1] >= max_y


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        filename = "input.txt"
    else:
        filename = "input.mini"

    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    input = choose_input()
    print("part 1", solve(input, False))
    # print("part 2", solve(input, True))
