import os
from collections import defaultdict


def part1(input):
    grid, lookup = parse_grid(input)
    graph = make_graph(grid)

    # # display
    # print_grid(grid)
    # print_lookup(lookup)
    # print_graph(graph)
    # print("+" * 16)

    paths = defaultdict(int)
    for trailhead in lookup[0]:
        for peak in lookup[9]:
            if find_path(graph, trailhead, peak):
                paths[trailhead] += 1
    return sum(paths.values())


def find_path(graph, start, end):
    def dfs(start, end, visited, path):
        visited.add(start)
        path.append(start)

        # Base case.
        if start == end:
            return True

        # Recursive case.
        for neighbour in graph[start]:
            if neighbour not in visited:
                if dfs(neighbour, end, visited, path):
                    return True

        # No path found.
        path.pop()
        return False

    visited = set()
    path = []
    dfs(start, end, visited, path)
    return path


def part2(input):
    grid, lookup = parse_grid(input)
    graph = make_graph(grid)

    # # display
    # print_grid(grid)
    # print_lookup(lookup)
    # print_graph(graph)
    # print("+" * 16)

    trails = defaultdict(int)
    for trailhead in lookup[0]:
        for peak in lookup[9]:
            paths = find_paths(graph, trailhead, peak)
            if paths:
                trails[trailhead] += len(paths)
    return sum(trails.values())


def find_paths(graph, start, end):
    def dfs(start, end, visited, path, all_paths):
        visited.add(start)
        path.append(start)

        # Base case.
        if start == end:
            all_paths.append(path[:])
        else:
            # Recursive case.
            for neighbour in graph[start]:
                if neighbour not in visited:
                    dfs(neighbour, end, visited, path, all_paths)

        # Backtrack.
        path.pop()
        visited.remove(start)

    visited = set()
    path = []
    all_paths = []

    dfs(start, end, visited, path, all_paths)

    return all_paths


def find_paths_to_top(grid, paths, coords):
    value = xy(grid, *coords)
    if value == 9:
        return [coords]
    new_paths = []
    for nc in neighbours(grid, coords):
        if nc in paths:
            new_paths.append(paths[nc])
        else:
            n = xy(grid, *nc)
            if n == value + 1:
                new_paths.append([coords] + find_paths_to_top(grid, paths, nc))
    return new_paths


# ----


def parse_grid(input):
    grid = defaultdict(dict)
    lookup = defaultdict(set)  # height to coords lookup
    for y, line in enumerate(input.strip().split("\n")):
        grid[y] = defaultdict(str)
        for x, c in enumerate([int(c) for c in line.strip()]):
            grid[y][x] = c
            lookup[c].add((x, y))
    return grid, lookup


def make_graph(grid):
    graph = defaultdict(list)  # adjacency graph
    for y in grid:
        for x in grid[y]:
            graph[(x, y)] = list(walkable_neighbours(grid, (x, y)))
    return graph


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


def print_graph(graph):
    for n in graph:
        print(n, graph[n])
    print()


def walkable_neighbours(grid, coords):
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
        if xy(grid, *coords) == xy(grid, nx, ny) - 1:
            yield (nx, ny)


def neighbours(grid, coords):
    directions = [
        (0, -1),  # up
        (0, 1),  # down
        (-1, 0),  # left
        (1, 0),  # right
    ]
    for dx, dy in directions:
        if not oob(grid, (coords[0] + dx, coords[1] + dy)):
            yield (coords[0] + dx, coords[1] + dy)


def xy(grid, x, y):
    return grid[y][x]


def oob(grid, coords):
    max_x, max_y = len(grid[0]), len(grid)
    return coords[0] < 0 or coords[0] >= max_x or coords[1] < 0 or coords[1] >= max_y


# ----


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        with open("input.txt", "r") as f:
            return f.read()
    else:
        with open("input.small", "r") as f:
            return f.read()


if __name__ == "__main__":
    input = choose_input()
    print(part1(input))
    print(part2(input))
