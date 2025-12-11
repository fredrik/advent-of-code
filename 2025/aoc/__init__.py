import os
import sys


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
