from aoc import get_input


def solve(input, part):
    max_x, max_y = 101, 103
    robots = parse_input(input)

    if part == 1:
        for sec in range(100):
            for i, robot in enumerate(robots):
                pos, vel = robot
                px, py = pos
                vx, vy = vel
                px = (px + vx) % max_x
                py = (py + vy) % max_y
                pos = (px, py)
                robots[i] = (pos, vel)
        return robot_count(robots, max_x, max_y)
    else:
        threshold = max_x * max_y * 0.2
        total_max = 0

        for sec in range(0, 10000000):
            for i, robot in enumerate(robots):
                pos, vel = robot
                px, py = pos
                vx, vy = vel
                px = (px + vx) % max_x
                py = (py + vy) % max_y
                pos = (px, py)
                robots[i] = (pos, vel)

            if sec % 1000 == 0:
                print("tick", sec)

            max_seen = has_large_region(make_grid(max_x, max_y, robots), threshold)
            if max_seen > total_max:
                total_max = max_seen
                print("total_max", total_max)
                print(f"after sec: {sec + 1}")
                print_grid(max_x, max_y, robots)

        return robot_count(robots, max_x, max_y)


def robot_count(robots, max_x, max_y):
    quads = [0, 0, 0, 0]
    mx, my = max_x // 2, max_y // 2
    for r in robots:
        x, y = r[0]
        if x < mx and y < my:
            quads[0] += 1
        if x > mx and y < my:
            quads[1] += 1
        if x < mx and y > my:
            quads[2] += 1
        if x > mx and y > my:
            quads[3] += 1
    return quads[0] * quads[1] * quads[2] * quads[3]


def has_large_region(grid, threshold):
    if not grid or not grid[0]:
        return False

    rows, cols = len(grid), len(grid[0])
    visited = set()

    def measure_region(row, col):
        if (
            row < 0
            or row >= rows
            or col < 0
            or col >= cols
            or grid[row][col] != 1
            or (row, col) in visited
        ):
            return 0

        size = 1
        visited.add((row, col))

        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        for dx, dy in directions:
            next_row, next_col = row + dx, col + dy
            size += measure_region(next_row, next_col)
            if size > threshold:
                return size

        return size

    max_seen = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and (i, j) not in visited:
                size = measure_region(i, j)
                if size > max_seen:
                    max_seen = size
                if size > threshold:
                    return max_seen

    return max_seen


def make_grid(max_x, max_y, robots):
    grid = [[0 for _ in range(max_x)] for _ in range(max_y)]
    for pos, vel in robots:
        x, y = pos
        grid[y][x] = 1
    return grid


def print_grid(max_x, max_y, robots):
    grid = [["." for _ in range(max_x)] for _ in range(max_y)]
    for pos, vel in robots:
        x, y = pos
        grid[y][x] = "1"

    for row in grid:
        print("".join(row))
    print()


def parse_input(input):
    robots = []
    for line in input:
        p, v = line.strip().split(" ")
        px, py = p.split("=")[1].split(",")
        p = (int(px), int(py))
        vx, vy = v.split("=")[1].split(",")
        v = (int(vx), int(vy))
        robots.append((p, v))
    return robots


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
