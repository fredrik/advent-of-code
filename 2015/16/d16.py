import re
import os
import sys
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


def solve(input, part):
    sues = parse_input(input)

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




def parse_input(input):
    sues = {}
    for line in input:
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
