from aoc import get_input

from collections import defaultdict


def solve(input, part):
    grid, lookup = parse_input(input)
    graph = make_graph(grid)

    if part == 1:
        paths = defaultdict(int)
        for trailhead in lookup[0]:
            for peak in lookup[9]:
                if find_path(graph, trailhead, peak):
                    paths[trailhead] += 1
        return sum(paths.values())
    else:
        trails = defaultdict(int)
        for trailhead in lookup[0]:
            for peak in lookup[9]:
                paths = find_paths(graph, trailhead, peak)
                if paths:
                    trails[trailhead] += len(paths)
        return sum(trails.values())


def make_graph(grid):
    graph = defaultdict(list)
    for y in grid:
        for x in grid[y]:
            graph[(x, y)] = list(walkable_neighbours(grid, (x, y)))
    return graph


def find_path(graph, start, end):
    def dfs(start, end, visited, path):
        visited.add(start)
        path.append(start)

        if start == end:
            return True

        for neighbour in graph[start]:
            if neighbour not in visited:
                if dfs(neighbour, end, visited, path):
                    return True

        path.pop()
        return False

    visited = set()
    path = []
    dfs(start, end, visited, path)
    return path


def find_paths(graph, start, end):
    def dfs(start, end, visited, path, all_paths):
        visited.add(start)
        path.append(start)

        if start == end:
            all_paths.append(path[:])
        else:
            for neighbour in graph[start]:
                if neighbour not in visited:
                    dfs(neighbour, end, visited, path, all_paths)

        path.pop()
        visited.remove(start)

    visited = set()
    path = []
    all_paths = []

    dfs(start, end, visited, path, all_paths)

    return all_paths


def walkable_neighbours(grid, coords):
    directions = [
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0),
    ]
    for dx, dy in directions:
        nx, ny = coords[0] + dx, coords[1] + dy
        if oob(grid, (nx, ny)):
            continue
        if xy(grid, *coords) == xy(grid, nx, ny) - 1:
            yield (nx, ny)


def xy(grid, x, y):
    return grid[y][x]


def oob(grid, coords):
    max_x, max_y = len(grid[0]), len(grid)
    return coords[0] < 0 or coords[0] >= max_x or coords[1] < 0 or coords[1] >= max_y


def parse_input(input):
    grid = defaultdict(dict)
    lookup = defaultdict(set)
    for y, line in enumerate(input):
        grid[y] = defaultdict(str)
        for x, c in enumerate([int(c) for c in line.strip()]):
            grid[y][x] = c
            lookup[c].add((x, y))
    return grid, lookup


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
