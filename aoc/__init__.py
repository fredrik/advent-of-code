import os
import sys
from functools import lru_cache, cache
from heapq import heappush, heappop
from collections import defaultdict


def get_input(raw=False):
    """
    Returns a list of strings via readlines(),
    or else the entire file as a string via read() if raw is True.
    """

    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    filepath = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), filename)

    if not os.path.exists(filepath):
        sys.stderr.write(f"File does not exist: {filepath}")
        sys.exit(1)

    with open(filepath, "r") as f:
        if raw:
            return f.read().strip()
        else:
            return f.readlines()


def parse_grid(input):
    g = defaultdict(str)
    for y, line in enumerate(input):
        for x, c in enumerate(line.strip()):
            g[(x, y)] = c
    return g


def neighbours(grid, key):
    x, y = key
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx or dy:  # skip (0, 0)
                yield grid.get((x + dx, y + dy))


def find_paths(graph, start, end):
    # dfs all-paths
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


def count_paths(graph, start, end):
    # memoized dfs on dag
    @lru_cache(maxsize=None)
    def dfs(node):
        if node == end:
            return 1
        else:
            return sum(dfs(n) for n in graph[node])

    return dfs(start)


def all_shortest_paths(graph, src, dst):
    # bfs all-shortest-paths
    if src == dst:
        return [[src]]

    queue = [[src]]
    visited = {src: 0}
    results = []

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if results and len(path) > len(results[0]):
            break

        for neighbor in graph.get(node, {}):
            new_path = path + [neighbor]
            if neighbor == dst:
                results.append(new_path)
            elif neighbor not in visited or visited[neighbor] >= len(new_path):
                visited[neighbor] = len(new_path)
                queue.append(new_path)

    return results


class Astar:
    def __init__(self, grid_size, obstacles):
        self.width, self.height = grid_size, grid_size
        self.obstacles = obstacles

        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid(self, x, y):
        return self.is_inbounds(x, y) and self.no_obstacle(x, y)

    @cache
    def is_inbounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def no_obstacle(self, x, y):
        return (x, y) not in self.obstacles

    @cache
    def manhattan_distance(self, x1, y1, x2, y2):
        """Calculate Manhattan distance heuristic"""
        return abs(x1 - x2) + abs(y1 - y2)

    def find_path(self, start, goal):
        start_x, start_y = start
        goal_x, goal_y = goal

        min_time_to_goal = self.manhattan_distance(start_x, start_y, goal_x, goal_y)
        max_time = min_time_to_goal * 12 + max(self.width, self.height)

        open_set = [(0, 0, start_x, start_y, 0)]  # (f_score, step, x, y, time)
        came_from = {(start_x, start_y, 0): None}
        g_score = {(start_x, start_y, 0): 0}
        step = 0
        min_f_score_to_goal = float("inf")

        while open_set:
            f, _, x, y, time = heappop(open_set)
            current = (x, y, time)

            if (x, y) == goal:
                min_f_score_to_goal = min(min_f_score_to_goal, f)
                return self._reconstruct_path(came_from, current)

            if f >= min_f_score_to_goal:
                break

            # time limit check
            remaining_dist = self.manhattan_distance(x, y, goal_x, goal_y)
            if time + remaining_dist >= max_time:
                continue

            for dx, dy in self.directions:
                next_x = x + dx
                next_y = y + dy
                next_time = time + 1

                if not self.is_valid(next_x, next_y):
                    continue

                next_state = (next_x, next_y, next_time)
                tentative_g = g_score[current] + 1

                if next_state not in g_score or tentative_g < g_score[next_state]:
                    came_from[next_state] = current
                    g_score[next_state] = tentative_g
                    f_score = tentative_g + self.manhattan_distance(
                        next_x, next_y, goal_x, goal_y
                    )
                    step += 1
                    heappush(open_set, (f_score, step, next_x, next_y, next_time))

        return None

    def _reconstruct_path(self, came_from, current):
        path = [(current[0], current[1])]
        while came_from[current] is not None:
            current = came_from[current]
            path.append((current[0], current[1]))
        return path[::-1]
