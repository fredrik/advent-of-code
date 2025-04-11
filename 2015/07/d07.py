from collections import defaultdict
from functools import cache
import os
import re


def solve(data, part):
    parsed = parse(data)

    # for k, v in parsed.items():
    #     print(k, v)
    # print()
    #
    # for k in sorted(parsed.keys()):
    #     print(k, "=", evaluate(("var", k, None), parsed))

    return evaluate(("var", "a", None), parsed)


def parse(data):
    def var_or_lit(x):
        if re.fullmatch("[0-9]+", x):
            return ("lit", int(x), None)
        elif re.fullmatch("[a-z]+", x):
            return ("var", x, None)
        else:
            raise Exception(f"unparsable var or lit: {x}")

    d = defaultdict(tuple)
    for line in data.splitlines():
        left, right = line.split(" -> ")
        parts = left.split(" ")
        rhs = right.strip()

        if "NOT" in left:
            a = var_or_lit(parts[1])
            lhs = ("not", a, None)
        elif "AND" in left:
            a, b = var_or_lit(parts[0]), var_or_lit(parts[2])
            lhs = ("and", a, b)
        elif "OR" in left:
            a, b = var_or_lit(parts[0]), var_or_lit(parts[2])
            lhs = ("or", a, b)
        elif "LSHIFT" in left:
            a, b = var_or_lit(parts[0]), var_or_lit(parts[2])
            lhs = ("lshift", a, b)
        elif "RSHIFT" in left:
            a, b = var_or_lit(parts[0]), var_or_lit(parts[2])
            lhs = ("rshift", a, b)
        else:
            lhs = var_or_lit(parts[0])

        d[rhs] = lhs
    return d


# left hand side: op or var or val
# operand: var or val
# op: AND, OR, NOT, LSHIFT, RSHIFT


def evaluate(instruction, d):
    @cache
    def eval(n):
        # print("eval:", n)
        op, a, b = n
        match op:
            case "lit":
                return a
            case "var":
                if a not in d:
                    raise Exception(f"No such variable '{a}'")
                return eval(d[a])
            case "not":
                # bitwise complement.
                return ~eval(a) & 65535
            case "and":
                # bitwise AND.
                return eval(a) & eval(b)
            case "or":
                # bitwise OR.
                return eval(a) | eval(b)
            case "lshift":
                # left shift by b bits.
                return eval(a) << eval(b)
            case "rshift":
                # right shift by b bits.
                return eval(a) >> eval(b)
            case _:
                raise Exception(f"unknown op!: {op}")

    return eval(instruction)


# ---s


def get_input_data():
    if os.environ.get("INPUT"):
        filename = os.environ.get("INPUT")
    else:
        filename = "input.txt"

    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, "r") as f:
        return f.read()


if __name__ == "__main__":
    data = get_input_data()
    print("part 1:", solve(data, 1))
    # print("part 2:", solve(data, 2))
