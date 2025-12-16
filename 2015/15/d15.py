from aoc import get_input
import math
import re


def solve(data, part):
    ingredients = list(parse_input(data))

    if part == 1:
        return max(recipe_score(ingredients))
    else:
        return max(recipe_score(ingredients, 500))


def recipe_score(ingredients, max_cals=None):
    for amounts in partitions(100, len(ingredients)):
        tot = [0, 0, 0, 0, 0]
        for ingredient, amount in zip(ingredients, amounts):
            for i, ing in enumerate(ingredient):
                tot[i] += ing * amount

        properties, calories = tot[:4], tot[4]

        if max_cals and calories != max_cals:
            continue

        yield math.prod([max(0, p) for p in properties])


def partitions(n, parts):
    if parts == 1:
        yield (n,)
    else:
        for i in range(n + 1):
            for rest in partitions(n - i, parts - 1):
                yield (i,) + rest


def parse_input(data):
    for line in data.splitlines():
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

        yield (cap, dur, fla, tex, cal)


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
