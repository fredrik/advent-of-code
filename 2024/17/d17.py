import re

opcodes = {0: "adv", 1: "bxl", 2: "bst", 3: "jnz", 4: "bxc", 5: "out", 6: "bdv", 7: "cdv"}
# all except 6 are in source

# operands:
# Combo operands 0 through 3 represent literal values 0 through 3.
# Combo operand 4 represents the value of register A.
# Combo operand 5 represents the value of register B.
# Combo operand 6 represents the value of register C.
# Combo operand 7 is reserved and will not appear in valid programs.


def solve(input, part):
    reg_a = int(re.findall(r"Register A: (\d+)", input)[0])
    ints = map(int, re.findall(r"Program: (.*)\n", input)[0].split(","))
    program = list(zip(ints, ints))  # (opcode, operand)

    print(list(map(lambda x: opcodes[x[0]], program)))

    regs = {
        "a": reg_a,
        "b": 0,
        "c": 0,
    }
    pointer = 0
    output = []
    while pointer < len(program):
        opcode, operand = program[pointer]
        pointer = execute(opcode, operand, regs, pointer, output)

    return ",".join(map(str, output))


def execute(opcode, operand, regs, pointer, output):
    match opcodes[opcode]:
        case "adv":
            regs["a"] = regs["a"] // 2 ** combo(operand, regs)
        case "bdv":
            regs["b"] = regs["a"] // 2 ** combo(operand, regs)
        case "cdv":
            regs["c"] = regs["a"] // 2 ** combo(operand, regs)
        case "bxl":
            # xor
            print(f"xor: regs['b'] = {regs['b']} & {operand} => {regs['b'] & operand}")
            regs["b"] = regs["b"] ^ operand
        case "bst":
            print(f"bst: regs['b'] = {combo(operand, regs)} % 8 => {combo(operand, regs) % 8}")
            regs["b"] = combo(operand, regs) % 8
        case "jnz":
            if regs["a"] != 0:
                return operand
        case "bxc":
            regs["b"] = regs["b"] ^ regs["c"]
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


# ---


import os


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        filename = "input.txt"
    else:
        filename = "input.small"

    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    input = choose_input()
    print("part 1", solve(input, 1))
    # print("part 2", solve(input, 2))
