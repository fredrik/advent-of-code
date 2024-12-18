from astar import Astar
from time import time


def solve(input, grid_size, start_time, part2):
    falling = [tuple(map(int, line.split(","))) for line in input.splitlines()]
    obstacles = set([f for i, f in enumerate(falling) if start_time > i])

    if not part2:
        pathfinder = Astar(grid_size, obstacles)
        path = pathfinder.find_path((0, 0), (grid_size - 1, grid_size - 1))
        return len(path) - 1
    else:
        for t, f in enumerate(falling):
            if t < start_time:
                # skip forward to start_time.
                continue
            obstacles.add(f)
            pathfinder = Astar(grid_size, obstacles)
            t0 = time()
            path = pathfinder.find_path((0, 0), (grid_size - 1, grid_size - 1))
            if not path:
                return f
            elapsed = "{:.2f}s".format(time() - t0)
            print(f"path found at t={t} ({f}) elapsed: {elapsed}")


# ---


import os


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        filename = "input.txt"
        grid_size = 71
        start_time = 1024
    else:
        filename = "input.small"
        grid_size = 7
        start_time = 12

    with open(filename, "r") as f:
        return f.read(), grid_size, start_time


if __name__ == "__main__":
    input, grid_size, start_time = choose_input()
    print("part 1", solve(input, grid_size, start_time, False))
    print("part 2", solve(input, grid_size, start_time, True))
