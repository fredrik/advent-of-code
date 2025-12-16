from aoc import get_input
import re
from collections import defaultdict

some_sue = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def solve(data, part):
    sues = parse_input(data)

    if part == 1:
        for number, props in sues.items():
            if all(some_sue[k] == v for k, v in props.items()):
                return number
    else:
        normal = some_sue.keys() - {'cats', 'trees', 'pomeranians', 'goldfish'}
        for number, props in sues.items():
            if (
                all(some_sue[k] == v for k, v in props.items() if k in normal)
                and ('cats' not in props or props["cats"] > some_sue["cats"])
                and ('trees' not in props or props["trees"] > some_sue["trees"])
                and ('pomeranians' not in props or props["pomeranians"] < some_sue["pomeranians"])
                and ('goldfish' not in props or props["goldfish"] < some_sue["goldfish"])
            ):
                return number




def parse_input(data):
    sues = {}
    for line in data.splitlines():
        match = re.search(r"Sue (\d+): (.*)", line)
        number, rest = int(match[1]), match[2]
        sues[number] = defaultdict(
            int,
            {
                k.strip(): int(v.strip())
                for part in rest.split(",")
                for k, v in [part.strip().split(":")]
            },
        )
    return sues


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
