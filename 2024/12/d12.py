from aoc import get_input

from itertools import product


def solve(input, part):
    grid = parse_input(input)
    regions = find_all_regions(grid)

    if part == 1:
        perimeter_price = 0
        for region in regions:
            perimeter = 0
            for p in region:
                perimeter += 4 - len(list(matching_neighbours(grid, p)))
            perimeter_price += perimeter * len(region)
        return perimeter_price
    else:
        side_price = 0
        for region in regions:
            num_corners = 0
            for point in region:
                row, col = point

                for dr, dc in product([1, -1], repeat=2):
                    row_neighbor = (row + dr, col)
                    col_neighbor = (row, col + dc)
                    diagonal_neighbor = (row + dr, col + dc)

                    if row_neighbor not in region and col_neighbor not in region:
                        num_corners += 1

                    if (
                        row_neighbor in region
                        and col_neighbor in region
                        and diagonal_neighbor not in region
                    ):
                        num_corners += 1

            side_price += num_corners * len(region)

        return side_price


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
    directions = [
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0),
    ]
    r, c = point
    for dr, dc in directions:
        n = (r + dr, c + dc)
        if grid.get(n) == grid[point]:
            yield n


def parse_input(input):
    grid = {}
    for row, line in enumerate(input):
        for col, c in enumerate([c for c in line.strip()]):
            grid[(row, col)] = c

    return grid


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
