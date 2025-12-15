from aoc import get_input

import re

OPCODES = {
    0: "adv",
    1: "bxl",
    2: "bst",
    3: "jnz",
    4: "bxc",
    5: "out",
    6: "bdv",
    7: "cdv",
}


def solve(input, part):
    reg_a, program, target = parse_input(input)

    if part == 1:
        output = evaluate(program, reg_a)
        return ",".join(map(str, output))
    else:

        def recurse(a=0, i=0):
            output = evaluate(program, a)

            if output == target:
                return a
            if output == target[-i:] or not i:
                for n in range(8):
                    if found := recurse(a * 8 + n, i + 1):
                        return found

        return recurse()


def evaluate(program, a):
    regs = {
        "a": a,
        "b": 0,
        "c": 0,
    }
    pointer = 0
    output = []
    while pointer < len(program):
        opcode, operand = program[pointer]
        pointer = execute(opcode, operand, regs, pointer, output)

    return output


def execute(opcode, operand, regs, pointer, output):
    match OPCODES[opcode]:
        case "adv":
            regs["a"] = regs["a"] // 2 ** combo(operand, regs)
        case "bdv":
            regs["b"] = regs["a"] // 2 ** combo(operand, regs)
        case "cdv":
            regs["c"] = regs["a"] // 2 ** combo(operand, regs)
        case "bxc":
            regs["b"] = regs["b"] ^ regs["c"]
        case "bxl":
            regs["b"] = regs["b"] ^ operand
        case "bst":
            regs["b"] = combo(operand, regs) % 8
        case "jnz":
            if regs["a"] != 0:
                return operand
        case "out":
            output.append(combo(operand, regs) % 8)

    return pointer + 1


def combo(operand, regs):
    match operand:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return regs["a"]
        case 5:
            return regs["b"]
        case 6:
            return regs["c"]


def parse_input(input):
    reg_a = int(re.findall(r"Register A: (\d+)", input)[0])
    ints = map(int, re.findall(r"Program: (.*)\n", input)[0].split(","))
    program = list(zip(ints, ints))
    target = [code for ops in program for code in ops]
    return reg_a, program, target


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
