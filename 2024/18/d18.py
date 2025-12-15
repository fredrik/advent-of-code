from aoc import get_input, Astar


def solve(input, part):
    falling, grid_size, start_time = parse_input(input)
    obstacles = set([f for i, f in enumerate(falling) if start_time > i])

    if part == 1:
        pathfinder = Astar(grid_size, obstacles)
        path = pathfinder.find_path((0, 0), (grid_size - 1, grid_size - 1))
        return len(path) - 1
    else:
        for t, f in enumerate(falling):
            if t < start_time:
                continue
            obstacles.add(f)
            pathfinder = Astar(grid_size, obstacles)
            path = pathfinder.find_path((0, 0), (grid_size - 1, grid_size - 1))
            if not path:
                return f


def parse_input(input):
    falling = [tuple(map(int, line.strip().split(","))) for line in input]

    if len(falling) > 100:
        grid_size = 71
        start_time = 1024
    else:
        grid_size = 7
        start_time = 12

    return falling, grid_size, start_time


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
