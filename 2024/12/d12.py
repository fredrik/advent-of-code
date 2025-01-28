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
            perimeter += 4 - len(list(matching_neighbours(grid, p)))
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

        for n in matching_neighbours(grid, p):
            queue.append(n)

    return region


def matching_neighbours(grid, point):
    # matching neighbours. must be inside the grid by definition.
    directions = [
        (0, -1),  # up
        (0, 1),  # down
        (-1, 0),  # left
        (1, 0),  # right
    ]
    r, c = point
    for dr, dc in directions:
        n = (r + dr, c + dc)
        if grid.get(n) == grid[point]:
            yield n


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
