from aoc import get_input


def solve(input, part):
    grid = parse_input(input)

    if part == 1:
        counter = 0
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == "S":
                    grid[r + 1][c] = "|"
                if cell == "." and grid[r-1][c] == "|":
                    grid[r][c] = '|'
                if cell == '^' and grid[r-1][c] == "|":
                    grid[r][c+1] = "|"
                    grid[r][c-1] = "|"
                    counter += 1

            # print_grid(grid); print()

        return counter
    else:
        return


def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, end="")
        print()


def parse_input(input):
    return [list(line.rstrip()) for line in input]


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
