import os
from itertools import product


def solve(input, part):
    grid = parse_grid(input)
    regions = find_all_regions(grid)

    if part == 1:
        return part1(grid, regions)
    else:
        return part2(regions)


def part1(grid, regions):
    perimeter_price = 0
    for region in regions:
        perimeter = 0
        for p in region:
            perimeter += 4 - len(list(matching_neighbours(grid, p)))
        perimeter_price += perimeter * len(region)
    return perimeter_price


def part2(regions):
    side_price = 0
    for region in regions:
        num_corners = 0
        for point in region:
            row, col = point

            for dr, dc in product([1, -1], repeat=2):
                row_neighbor = (row + dr, col)
                col_neighbor = (row, col + dc)
                diagonal_neighbor = (row + dr, col + dc)

                # exterior corners
                if row_neighbor not in region and col_neighbor not in region:
                    num_corners += 1

                # interior corners
                if row_neighbor in region and col_neighbor in region and diagonal_neighbor not in region:
                    num_corners += 1

        side_price += num_corners * len(region)

    return side_price


# ---


def parse_grid(input):
    grid = {}
    for row, line in enumerate(input.strip().split("\n")):
        for col, c in enumerate([c for c in line.strip()]):
            grid[(row, col)] = c

    return grid


def find_all_regions(grid):
    regions = []
    all_points = set()

    for point in grid:
        if point in all_points:
            continue

        region = find_region(grid, point)
        all_points |= region
        regions.append(region)

    return regions


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
