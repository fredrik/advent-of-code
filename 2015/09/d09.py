import re
import os
from collections import defaultdict

# Santa can start and end at any two (different) locations he wants, but he must
# visit each location exactly once. What is the shortest distance he can travel
# to achieve this?

def solve(input, part):
    if part == 1:
        g = parse_input(input)
        distances = []
        for path in all_paths(g):
            distance = path_distance(g, path)
            distances.append(distance)
            # print(f'{path}: {distance}')
        return min(distances)
    else:
        return 2

# data structure:
# {'London': {'Dublin': '464', 'Belfast': '518'}, 'Dublin': {'Belfast': '141'}}

def parse_input(input):
    g = defaultdict(dict)
    for line in input:
        parts = re.match(r'(\w+) to (\w+) = (\d+)', line)
        g[parts[1]][parts[2]] = int(parts[3])
        g[parts[2]][parts[1]] = int(parts[3])
    return dict(g)

def all_paths(g):
    def _paths(g, node, path):
        unvisited = set(g.keys()) - set(path)
        if not unvisited:
            yield path
        neighbours = set(g[node].keys())
        for neighbour in neighbours & unvisited:
            yield from _paths(g, neighbour, path + (neighbour,) )
    for node in g.keys():
        yield from _paths(g, node, (node,))

def path_distance(g, path):
    def pairwise(t):
        return zip(iter(t), iter(t[1:]))
    distance = 0
    for a,b in pairwise(path):
        distance += g[a][b]
    return distance





# ---

def get_input():
    if os.environ.get("INPUT"):
        filename = os.environ.get("INPUT")
    else:
        filename = "input.txt"
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, "r") as f:
        return f.readlines()


if __name__ == "__main__":
    input = get_input()
    print("part 1:", solve(input, 1))
    print("part 2:", solve(input, 2))