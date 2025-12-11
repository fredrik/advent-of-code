from collections import deque
import re
from aoc import get_input
from functools import cache


def solve(input, part):
    machines = list(parse_input(input))

    # for target, toggles in machines:
    #     print(
    #         format(target, '08b'),
    #         ', '.join([
    #             format(t, '08b') for t in toggles
    #         ])
    #     )

    if part == 1:
        return sum(presses(0, target, toggles) for target, toggles in machines)
    else:
        return


def presses(state, target, toggles):
    if state == target:
        return 0

    visited = {state}
    queue = deque([(state, 0)])

    while queue:
        current, depth = queue.popleft()
        for t in toggles:
            neighbour = current ^ t
            if neighbour == target:
                return depth + 1
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, depth + 1))


def parse_input(input):
    def parse_lights(str):
        return [True if s == "#" else False for s in str]

    def parse_toggles(str):
        return [
            tuple(map(int, s.split(",")))
            for s in str.replace("(", "").replace(")", "").split(" ")
        ]

    def to_binary(bitmask):
        return int("".join("1" if b else "0" for b in bitmask), 2)

    for line in input:
        match = re.search(r"\[(.+)\] (.*) \{", line)
        if match:
            lights = parse_lights(match.group(1))
            toggles = [
                [i in positions for i in range(len(lights))]
                for positions in parse_toggles(match.group(2))
            ]

            # lights and toggles are bit masks. convert to binary.
            # [False, True, True, False] => 0110
            yield (to_binary(lights), tuple(to_binary(t) for t in toggles))


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
