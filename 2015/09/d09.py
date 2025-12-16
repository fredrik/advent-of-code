from aoc import get_input
import re
from collections import defaultdict
from itertools import permutations

# Santa can start and end at any two (different) locations he wants, but he must
# visit each location exactly once. What is the shortest distance he can travel
# to achieve this?

def solve(data, part):
    g = parse_input(data)
    distances = []
    for path in permutations(g.keys()):
        distance = path_distance(g, path)
        distances.append(distance)

    if part == 1:
        return min(distances)
    else:
        return max(distances)

# data structure:
# {'London': {'Dublin': '464', 'Belfast': '518'}, 'Dublin': {'Belfast': '141'}}

def parse_input(data):
    g = defaultdict(dict)
    for line in data.splitlines():
        parts = re.match(r'(\w+) to (\w+) = (\d+)', line)
        g[parts[1]][parts[2]] = int(parts[3])
        g[parts[2]][parts[1]] = int(parts[3])
    return dict(g)

def path_distance(g, path):
    def pairwise(t):
        return zip(iter(t), iter(t[1:]))
    distance = 0
    for a,b in pairwise(path):
        distance += g[a][b]
    return distance


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))