from astar import Astar


def solve(input, grid_size, start_time, part2):
    falling = [tuple(map(int, line.split(","))) for line in input.splitlines()]
    obstacles = [f for i, f in enumerate(falling) if start_time > i]

    pathfinder = Astar(grid_size, obstacles, start_time)
    path = pathfinder.find_path((0, 0), (grid_size - 1, grid_size - 1))

    return len(path) - 1


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
    # print("part 2", solve(input, True))
