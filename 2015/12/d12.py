import json
import os
import sys

def solve(input, part):
    object = parse_input(input)

    if part == 1:
        return parse_value(object)
    else:
        return parse_value(object, ignore_red=True)

def parse_input(input):
    return json.loads(input)

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
# ---

def get_input():
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, "r") as f:
        return f.read()


if __name__ == "__main__":
    input = get_input()
    print("part 1:", solve(input, 1))
    print("part 2:", solve(input, 2))
