from aoc import get_input
import re
from collections import defaultdict


def solve(data, part):
    reindeers = list(parse_input(data))
    seconds = 2503

    if part == 1:
        return max(distance(reindeer, seconds) for reindeer in reindeers)
    else:
        winners = defaultdict(int)
        for s in range(1, seconds + 1):
            w = winner(reindeers, s)
            winners[w] += 1

        return max(winners.values())


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


def winner(reindeers, s):
    distances = {r[0]: distance(r, s) for r in reindeers}
    return max(distances, key=distances.get)


def parse_input(data):
    for line in data.splitlines():
        match = re.search(
            r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.",
            line.strip(),
        )
        name, speed, duration, rest = (
            match[1],
            int(match[2]),
            int(match[3]),
            int(match[4]),
        )
        yield (name, speed, duration, rest)


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
