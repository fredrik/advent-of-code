import os
from collections import defaultdict


def part1(input):
    map = parse_input(input)
    position = find_starting_pos(map)
    direction = (-1, 0)
    while True:
        map[position] = "x"
        next_position = (position[0] + direction[0], position[1] + direction[1])

        if map[next_position] == "#":
            direction = turn(direction)
            next_position = (position[0] + direction[0], position[1] + direction[1])

        if map[next_position] == "":
            return len(list(filter(lambda x: x == "x", map.values())))

        position = next_position


def part2(input, window=None):
    map = parse_input(input)
    reachable_positions = evaluate_reachable_positions(map.copy())
    loops = 0
    for x, y in reachable_positions:
        causes_loop = evaluate_position(map.copy(), (x, y), window)
        if causes_loop:
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

    seen = set()
    position = find_starting_pos(map)
    direction = (-1, 0)

    while map[position] != "":
        loop_detected = (position, direction) in seen
        if loop_detected:
            return True

        seen.add((position, direction))
        map[position] = "x"

        next = next_position(position, direction)
        if map[next] == "#" or next == obstacle_position:
            direction = (direction[1], -direction[0])
        else:
            position = next


def next_position(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])


def find_starting_pos(input):
    for k, v in input.items():
        if v == "^":
            return k


def turn(direction):
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


if __name__ == "__main__":
    input = choose_input()
    print(part1(input))
    print(part2(input))
