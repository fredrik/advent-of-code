import math
import re
import os
import sys


def solve(input, part):
    ingredients = list(parse_input(input))

    if part == 1:
        return max(recipe_score(ingredients))

    else:
        return


def recipe_score(ingredients):
    for amounts in partitions(100, len(ingredients)):
        tot = [0, 0, 0, 0]
        for ingredient, amount in zip(ingredients, amounts):
            for i, ing in enumerate(ingredient):
                tot[i] += ing * amount
        yield math.prod([max(0, t) for t in tot])


def partitions(n, parts):
    if parts == 1:
        yield (n,)
    else:
        for i in range(n + 1):
            for rest in partitions(n - i, parts - 1):
                yield (i,) + rest


def parse_input(input):
    for line in input:
        match = re.search(
            r"(\w+): capacity ([\-\d]+), durability ([\-\d]+), flavor ([\-\d]+), texture ([\-\d]+), calories ([\-\d]+)",
            line.strip(),
        )
        _, cap, dur, fla, tex, cal = (
            match[1],
            int(match[2]),
            int(match[3]),
            int(match[4]),
            int(match[5]),
            int(match[6]),
        )

        # yield {cap: cap, dur: dur, fla: fla, tex: tex, cal: cal}
        yield (cap, dur, fla, tex)


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
