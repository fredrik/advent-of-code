import os

directions = {
    # => dc, dr
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}


def solve_part1(input):
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


def solve_part2(input):
    worldmap, instructions = input.split("\n\n")
    worldmap, robot_position = parse_worldmap(worldmap)
    worldmap, robot_position = expand_worldmap(worldmap)
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
                if (cc, rr) == (c + dc, r + dr):
                    worldmap[r][c] = "."
                    worldmap[r + dr][c + dc] = "@"
                    robot_position = (c + dc, r + dr)

                else:
                    # there were boxes.
                    if instruction in "LR":
                        # step backwards and move the boxes one position at a time.
                        while rr != r or cc != c:
                            worldmap[rr][cc] = worldmap[rr - dr][cc - dc]
                            rr, cc = rr - dr, cc - dc
                        worldmap[r][c] = "."
                        worldmap[r + dr][c + dc] = "@"
                        robot_position = (c + dc, r + dr)

                    else:
                        # up or down. we need to find all connected boxes.
                        connected = all_connected(worldmap, c, r, dc, dr, {})
                        if "#" in connected.values():
                            break
                        else:
                            # reset
                            for ccc, rrr in connected:
                                worldmap[rrr][ccc] = "."
                            # move
                            for (ccc, rrr), v in connected.items():
                                worldmap[rrr + dr][ccc] = v

                            robot_position = (c + dc, r + dr)
                break  # done.

        # # report
        # print("move", instruction)
        # print_worldmap(worldmap)
        # print()

    return sum(gps_part2(worldmap))


def all_connected(worldmap, c, r, dc, dr, connected):
    # direction is either up or down.
    assert dc == 0
    assert dr != 0

    v = worldmap[r][c]

    if v == ".":  # empty space
        return connected

    if (c, r) in connected:
        return connected

    connected[(c, r)] = v

    if v == "#":
        return connected
    if v == "[":
        return all_connected(worldmap, c + 1, r, dc, dr, connected) | all_connected(
            worldmap, c, r + dr, dc, dr, connected
        )
    if v == "]":
        return all_connected(worldmap, c - 1, r, dc, dr, connected) | all_connected(
            worldmap, c, r + dr, dc, dr, connected
        )
    if v == "@":
        return all_connected(worldmap, c, r + dr, dc, dr, connected)

    # assert v == "."
    return connected


def gps(worldmap):
    for r, row in enumerate(worldmap):
        for c, cell in enumerate(row):
            if cell == "O":
                yield c + r * 100


def gps_part2(worldmap):
    for r, row in enumerate(worldmap):
        for c, cell in enumerate(row):
            if cell == "[":
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


def expand_worldmap(worldmap):
    new_worldmap = []
    robot_position = None

    lookup = {
        "#": ["#", "#"],
        "O": ["[", "]"],
        ".": [".", "."],
        "@": ["@", "."],
    }
    for row in worldmap:
        new_row = []
        for cell in row:
            new_row += lookup[cell]
        new_worldmap.append(new_row)

    for r, row in enumerate(new_worldmap):
        for c, cell in enumerate(row):
            if cell == "@":
                robot_position = (c, r)

    return new_worldmap, robot_position


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
        filename = "input.small"

    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    input = choose_input()
    print("part 1", solve_part1(input))
    print("part 2", solve_part2(input))
