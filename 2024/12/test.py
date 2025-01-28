# usage:
# uv run test.py

from d12 import solve


testcases = {
    "input.mini": 80,
    "input.alt1": 236,
    "input.alt2": 368,
    "input.alt3": 436,
    "input.small": 1206,
}


def read_input(filename):
    with open(filename, "r") as f:
        return f.read()


for filename, expected in testcases.items():
    solution = solve(read_input(filename), 2)
    assert solution == expected, f"{solution} should be {expected} ({filename})"
    print(f"{solution} == {expected}, ok")
