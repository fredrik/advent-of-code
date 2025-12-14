import os
import sys
from functools import lru_cache


def get_input():
    """Returns a list of strings via readlines()"""

    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    filepath = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), filename)

    if not os.path.exists(filepath):
        sys.stderr.write(f"File does not exist: {filepath}")
        sys.exit(1)

    with open(filepath, "r") as f:
        return f.readlines()


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
