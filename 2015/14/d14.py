import re
import os
import sys

def solve(input, part):
    reindeers = parse_input(input)
    seconds = 2503

    if part == 1:
        return max(distance(reindeer, seconds) for reindeer in reindeers)
    else:
        return

def distance(reindeer, seconds):
    name, speed, duration, rest = reindeer
    distance = 0

    while seconds > 0:
        if seconds > duration:
            distance += speed * duration
        else:
            distance += speed * seconds
        seconds = seconds - duration - rest

    return distance


def parse_input(input):
    for line in input:
        match = re.search(
        r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.",
        line.strip(),
        )
        name, speed, duration, rest = match[1], int(match[2]), int(match[3]), int(match[4])
        yield (name, speed, duration, rest)
# ---

def get_input():
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, "r") as f:
        return f.readlines()


if __name__ == "__main__":
    input = get_input()
    print("part 1:", solve(input, 1))
    print("part 2:", solve(input, 2))
