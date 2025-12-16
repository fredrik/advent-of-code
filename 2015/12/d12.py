from aoc import get_input
import json

def solve(data, part):
    object = parse_input(data)

    if part == 1:
        return parse_value(object)
    else:
        return parse_value(object, ignore_red=True)

def parse_input(data):
    return json.loads(data)

def parse_value(v, ignore_red=False):
    if isinstance(v, (int, float)):
        return v
    if isinstance(v, list):
        return sum((parse_value(w, ignore_red) for w in v))
    if isinstance(v, dict):
        if ignore_red and "red" in v.values():
            return 0
        else:
            return sum((parse_value(w, ignore_red) for w in v.values()))
    return 0 # str or otherwise


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
