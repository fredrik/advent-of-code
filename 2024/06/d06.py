import os
from collections import defaultdict


def part2(input, window=None):
    # brute force our way to success!
    map = parse_input(input)

    reachable_positions = evaluate_reachable_positions(map.copy())

    # print("\n".join(sorted([f"({p[0]}, {p[1]})" for p in reachable_positions])))
    # return len(reachable_positions)
    # compares well to thanks.py!

    # loops = 0
    # max_y = max(map.keys(), key=lambda x: x[0])[0]
    # max_x = max(map.keys(), key=lambda x: x[1])[1]
    # for y in range(max_y + 1):
    #     for x in range(max_x + 1):
    #         if (y, x) in reachable_positions:
    #             causes_loop = evaluate_position(map.copy(), (y, x))
    #             if causes_loop:
    #                 loops += 1
    # return loops

    # test one
    # reachable_positions = [(20, 5)]

    loops = 0
    for x, y in reachable_positions:
        causes_loop = evaluate_position(map.copy(), (x, y), window)
        if causes_loop:
            print("OBS", (x, y))  # compare to thanks.py
            loops += 1
    return loops


def evaluate_reachable_positions(map):
    seen = set()
    position = find_starting_pos(map)
    direction = (-1, 0)

    while True:
        seen.add(position)
        map[position] = "x"
        next_position = (position[0] + direction[0], position[1] + direction[1])

        if map[next_position] == "#":
            # direction = turn(direction)
            direction = (direction[1], -direction[0])
            next_position = (position[0] + direction[0], position[1] + direction[1])

        position = next_position

        if map[position] == "":
            return seen


def evaluate_position(map, obstacle_position, window):
    if obstacle_position == find_starting_pos(map):
        return False

    if map[obstacle_position] == "#":
        return False

    # map[obstacle_position] = "#"

    seen = set()

    # walk until we hit a wall or identify a loop
    position = find_starting_pos(map)
    direction = (-1, 0)

    while map[position] != "":
        # print(position, direction)

        # draw
        # ymax, xmax = window.getmaxyx()
        # print(ymax, xmax)

        # if window:
        #     window.clear()
        #     for (x, y), c in map.items():
        #         window.addstr(x, y, c)
        #     window.refresh()

        loop_detected = (position, direction) in seen
        if loop_detected:
            # print("Loop at", obstacle_position, "currently at", position, direction)
            # map = mark_loop_on_map(map, position, direction)
            # map[obstacle_position] = "O"
            # map[starting_position] = "^"
            # print_map(map)
            # print()
            # import time; time.sleep(100)
            return True

        # mark as visited
        seen.add((position, direction))
        map[position] = "x"

        # print_map(map)
        # print(position)
        # print(map[next_position])
        # print()

        # move
        # print("next_position", next_position(position, direction), "value", map[next_position(position, direction)])
        next = next_position(position, direction)
        # if next == obstacle_position:
        #     print("next is obstacle!!!", next)
        if map[next] == "#" or next == obstacle_position:
            # print(
            #     "turn debug",
            #     turn(direction) == (direction[1], -direction[0]),
            #     turn(direction),
            #     (direction[1], -direction[0]),
            # )
            # direction = turn(direction)
            # seen.add((position, direction))  # maybe not necessary

            # use thanks
            prev = direction
            direction = (direction[1], -direction[0])
            # print("turning", prev, direction)
        else:
            position = next


def mark_loop_on_map(map, position, direction):
    starting_position, starting_direction = position, direction
    while True:
        map[position] = "!"

        # move
        if map[next_position(position, direction)] == "#":
            direction = turn(direction)
        position = next_position(position, direction)

        # check if we're back at the start
        if (position, direction) == (starting_position, starting_direction):
            return map


def next_position(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])


def part1(input):
    map = parse_input(input)
    position = find_starting_pos(map)
    direction = (-1, 0)
    while True:
        map[position] = "x"
        next_position = (position[0] + direction[0], position[1] + direction[1])

        # print_map(map)
        # print(position)
        # print(map[next_position])

        # print()

        if map[next_position] == "#":
            direction = turn(direction)
            next_position = (position[0] + direction[0], position[1] + direction[1])

        position = next_position
        if map[position] == "":
            print_map(map)
            count = len(list(filter(lambda x: x == "x", map.values())))
            return count


def print_map(mmmap):
    max_y = max(mmmap.keys(), key=lambda x: x[0])[0]
    max_x = max(mmmap.keys(), key=lambda x: x[1])[1]
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            # print(f"{y},{x} = {mmmap[(y,x)]}", end="")
            print(mmmap[(y, x)], end="")
        print()


def find_starting_pos(input):
    for k, v in input.items():
        if v == "^":
            return k


def turn(direction):
    # turn 90 degrees to the right
    if direction == (-1, 0):
        return (0, 1)
    elif direction == (0, 1):
        return (1, 0)
    elif direction == (1, 0):
        return (0, -1)
    elif direction == (0, -1):
        return (-1, 0)


def parse_input(input):
    map = defaultdict(str)
    lines = input.strip().splitlines()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            map[(i, j)] = c
    return map


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        with open("input.txt", "r") as f:
            return f.read()
    else:
        with open("input.mini", "r") as f:
            return f.read()


def main(window):
    part2(input, window)
    # for i in range(10):
    #     window.addstr(10, 10, "[" + ("=" * i) + ">" + (" " * (10 - i)) + "]")
    #     window.refresh()
    #     time.sleep(0.5)


if __name__ == "__main__":
    input = choose_input()
    # print(part1(input))
    print(part2(input))

    # curses.wrapper(main)
