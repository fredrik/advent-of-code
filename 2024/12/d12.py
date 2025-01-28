import os


def solve(input, part):
    if part == 1:
        return part1(input)
    else:
        return part2(input)


def part1(input):
    grid = parse_grid(input)

    regions = []
    all_points = set()

    for point in grid:
        if point in all_points:
            continue

        region = find_region(grid, point)
        all_points |= region
        regions.append(region)

    price = 0
    for region in regions:
        perimeter = 0
        for p in region:
            matching_neighs = [n for n in neighbours(p) if grid.get(n) == grid[p]]
            perimeter += 4 - len(matching_neighs)
        price += perimeter * len(region)
    return price


def part2(input):
    pass


# ---


def parse_grid(input):
    grid = {}
    for row, line in enumerate(input.strip().split("\n")):
        for col, c in enumerate([c for c in line.strip()]):
            grid[(row, col)] = c
    return grid


def find_region(grid, point):
    region = set()

    queue = [point]
    while queue:
        p = queue.pop()
        if p in region:
            continue

        region.add(p)

        for n in neighbours(p):
            if grid.get(n) == grid[p]:
                queue.append(n)


def neighbours(point):
    # all neighbouring points.
    # can be outside grid, so must be checked by caller.
    directions = [
        (0, -1),  # up
        (0, 1),  # down
        (-1, 0),  # left
        (1, 0),  # right
    ]
    for dx, dy in directions:
        yield point[0] + dx, point[1] + dy


# ---


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        filename = "input.txt"
    else:
        filename = "input.small"

    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    input = choose_input()
    print("part 1:", solve(input, 1))
    print("part 2:", solve(input, 2))
