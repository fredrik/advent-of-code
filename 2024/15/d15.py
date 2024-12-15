import os

directions = {
    # => dc, dr
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}


def solve(input, part2):
    worldmap, instructions = input.split("\n\n")
    worldmap, robot_position = parse_worldmap(worldmap)
    instructions = parse_instructions(instructions)

    # print_worldmap(worldmap)
    # print("robot_position", robot_position)
    # print("instructions", instructions)

    for instruction in instructions:
        dc, dr = directions[instruction]
        c, r = robot_position
        # find the next wall (and do nothing)
        # or find the next empty space (and move robot plus any boxes one step)
        cc, rr = c, r  # lookahead
        while True:
            rr, cc = rr + dr, cc + dc
            v = worldmap[rr][cc]
            if v == "#":
                break  # and do nothing
            if v == ".":
                worldmap[rr][cc] = "O"
                worldmap[r][c] = "."
                worldmap[r + dr][c + dc] = "@"
                robot_position = (c + dc, r + dr)
                break  # done.

        # # report
        # print("move", instruction)
        # print_worldmap(worldmap)
        # print()

    return sum(gps(worldmap))


def gps(worldmap):
    for r, row in enumerate(worldmap):
        for c, cell in enumerate(row):
            if cell == "O":
                yield c + r * 100


# --- parse and print ---


def parse_worldmap(worldmap):
    grid = []
    robot_position = None

    for r, line in enumerate(worldmap.splitlines()):
        grid.append([c for c in line])

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == "@":
                robot_position = (c, r)

    return grid, robot_position


def parse_instructions(instructions):
    lookup = {
        "^": "U",
        "v": "D",
        "<": "L",
        ">": "R",
    }
    return [lookup[i] for i in instructions if i != "\n"]


def print_worldmap(worldmap):
    for row in worldmap:
        print("".join(row))


# --- input basics ---


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        filename = "input.txt"
    else:
        filename = "input.mini"

    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    input = choose_input()
    print("part 1", solve(input, False))
    # print("part 2", solve(input, True))
