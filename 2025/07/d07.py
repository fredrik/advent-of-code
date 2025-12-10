from aoc import get_input
from aoc_vcr import Recorder


def solve(input, part):
    grid = parse_input(input)

    if part == 1:
        with Recorder(year=2025, day=7, part=1) as rec:
            splits = 0
            for r, row in enumerate(grid):
                for c, cell in enumerate(row):
                    if cell == "S":
                        grid[r + 1][c] = "|"
                    if cell == "." and grid[r - 1][c] == "|":
                        grid[r][c] = "|"
                    if cell == "^" and grid[r - 1][c] == "|":
                        grid[r][c + 1] = "|"
                        grid[r][c - 1] = "|"
                        splits += 1

                    rec.snapshot(grid=grid, splits=splits)
            return splits
    else:
        return count_timelines(grid)


cache = {}


def count_timelines(grid, start_r=0, start_c=0):
    for r in range(start_r, len(grid)):
        for c in range(start_c, len(grid[0])):
            cell = grid[r][c]
            if cell == "S":
                grid[r + 1][c] = "|"
            if cell == "." and grid[r - 1][c] == "|":
                grid[r][c] = "|"
            if cell == "^" and grid[r - 1][c] == "|":
                left_copy = [row[:] for row in grid]
                left_copy[r][c - 1] = "|"
                left_key = (r, c, tuple(left_copy[r]))
                if left_key in cache:
                    left_count = cache[left_key]
                else:
                    cache[left_key] = count_timelines(left_copy, r, c + 1)
                    left_count = cache[left_key]

                right_copy = [row[:] for row in grid]
                right_copy[r][c + 1] = "|"
                right_key = (r, c, tuple(right_copy[r]))
                if right_key in cache:
                    right_count = cache[right_key]
                else:
                    cache[right_key] = count_timelines(right_copy, r, c + 1)
                    right_count = cache[right_key]

                return left_count + right_count
        start_c = 0
    return 1


def parse_input(input):
    return [list(line.rstrip()) for line in input]


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
