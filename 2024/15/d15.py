from aoc import get_input

DIRECTIONS = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}


def solve(input, part):
    worldmap, instructions = parse_input(input)

    if part == 2:
        worldmap, robot_position = expand_worldmap(worldmap)
    else:
        robot_position = find_robot(worldmap)

    for instruction in instructions:
        dc, dr = DIRECTIONS[instruction]
        c, r = robot_position
        cc, rr = c, r
        while True:
            rr, cc = rr + dr, cc + dc
            v = worldmap[rr][cc]
            if v == "#":
                break
            if v == ".":
                if part == 1:
                    worldmap[rr][cc] = "O"
                    worldmap[r][c] = "."
                    worldmap[r + dr][c + dc] = "@"
                    robot_position = (c + dc, r + dr)
                else:
                    if (cc, rr) == (c + dc, r + dr):
                        worldmap[r][c] = "."
                        worldmap[r + dr][c + dc] = "@"
                        robot_position = (c + dc, r + dr)
                    else:
                        if instruction in "LR":
                            while rr != r or cc != c:
                                worldmap[rr][cc] = worldmap[rr - dr][cc - dc]
                                rr, cc = rr - dr, cc - dc
                            worldmap[r][c] = "."
                            worldmap[r + dr][c + dc] = "@"
                            robot_position = (c + dc, r + dr)
                        else:
                            connected = all_connected(worldmap, c, r, dc, dr, {})
                            if "#" in connected.values():
                                break
                            else:
                                for ccc, rrr in connected:
                                    worldmap[rrr][ccc] = "."
                                for (ccc, rrr), v in connected.items():
                                    worldmap[rrr + dr][ccc] = v
                                robot_position = (c + dc, r + dr)
                break

    if part == 1:
        return sum(gps(worldmap))
    else:
        return sum(gps_part2(worldmap))


def all_connected(worldmap, c, r, dc, dr, connected):
    assert dc == 0
    assert dr != 0

    v = worldmap[r][c]

    if v == ".":
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


def find_robot(worldmap):
    for r, row in enumerate(worldmap):
        for c, cell in enumerate(row):
            if cell == "@":
                return (c, r)
    return None


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


def parse_input(input):
    worldmap_str, instructions_str = input.split("\n\n")
    worldmap = [list(line) for line in worldmap_str.splitlines()]
    instructions = parse_instructions(instructions_str)
    return worldmap, instructions


def parse_instructions(instructions):
    lookup = {
        "^": "U",
        "v": "D",
        "<": "L",
        ">": "R",
    }
    return [lookup[i] for i in instructions if i != "\n"]


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
