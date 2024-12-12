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

        if part2:
            sides = count_sides_graph(region, graph, grid)
            price += area * sides
            print(
                "region",
                region,
                "area",
                area,
                "sides",
                sides,
                "price",
                area * sides,
            )
            print()

        else:
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


def count_sides_graph(region, graph, grid):
    edge_nodes = [(x, y) for (x, y) in region if len(graph[(x, y)]) < 4]
    paths = find_paths(grid, edge_nodes[0], edge_nodes[0])  # find loops!
    print("found paths!", len(paths))
    return 1


def find_paths(grid, start, end):
    def dfs(grid, start, end, direction, visited, path, all_paths):
        visited.add((start, direction))
        path.append(start)

        # Base case.
        if start == end and len(path) > 1:
            all_paths.append(path[:])
        else:
            # Recursive case.
            for neighbour, direction in neighs(grid, *start):
                if (neighbour, direction) not in visited:
                    dfs(grid, neighbour, end, direction, visited, path, all_paths)

        # Backtrack.
        path.pop()
        visited.remove((start, direction))

    # connected plots of the same type, with direction
    def neighs(grid, x, y):
        directions = [
            (0, -1),  # up
            (0, 1),  # down
            (-1, 0),  # left
            (1, 0),  # right
        ]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if oob(grid, (nx, ny)):
                continue
            if xy(grid, x, y) == xy(grid, nx, ny):
                yield (nx, ny), direction

    visited = set()
    path = []
    all_paths = []
    direction = (1, 0)

    dfs(grid, start, end, direction, visited, path, all_paths)

    return all_paths


def count_sides(region, graph, grid):
    edge_nodes = [(x, y) for (x, y) in region if len(graph[(x, y)]) < 4]
    direction = (1, 0)
    starting_node = edge_nodes[0]
    print(xy(grid, *starting_node))
    node = starting_node
    sides = 0

    c = 0
    while True:
        c += 1
        if c > 100:
            print("PANIC", c, node)
            break

        x, y = node
        dx, dy = direction
        print("node", node, "dxdy", dx, dy)

        if (x + dx, y + dy) in edge_nodes:
            node = (x + dx, y + dy)
        else:
            # we need to turn 90 degrees
            sides += 1

            # find the first node that we can turn to, in clockwise order,
            # that is an edge node and has an external node to its left in reference to our direction
            next_x, next_y = x + dx, y + dy
            left_x, left_y = 0, 1

            # if (x + dy, y + dx) in edge_nodes:
            #     print("turn right")
            #     direction = dy, dx
            # else:
            #     print("turn left")
            #     direction = dy, -dx

            # if (x + dy, y - dx) in edge_nodes:
            #     # right
            #     # node = (x + dy, y - dx)
            #     direction = (dy, -dx)
            # elif (x + dy, y + dx) in edge_nodes:
            #     # left
            #     # node = (x + dy, y + dx)
            #     direction = dy, dx
            # else:
            #     # turn around
            #     # node = (x - dx, y - dy)
            #     direction = -dx, -dy

        if node == starting_node and direction == (1, 0):
            # done!
            break

    return sides


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
    # print("part 1", solve(input, False))
    print("part 2", solve(input, True))
