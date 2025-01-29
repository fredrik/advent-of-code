import sys
import random
import re


opcodes = {0: "adv", 1: "bxl", 2: "bst", 3: "jnz", 4: "bxc", 5: "out", 6: "bdv", 7: "cdv"}


def solve(input, part):
    if part == 1:
        return part1(input)
    else:
        return part2(input)


def part1(input):
    reg_a = int(re.findall(r"Register A: (\d+)", input)[0])
    ints = map(int, re.findall(r"Program: (.*)\n", input)[0].split(","))
    program = list(zip(ints, ints))  # (opcode, operand)

    output = evaluate(program, reg_a)

    return ",".join(map(str, output))


def part2(input):
    ints = map(int, re.findall(r"Program: (.*)\n", input)[0].split(","))
    program = list(zip(ints, ints))  # (opcode, operand)
    target = [code for ops in program for code in ops]  # flatten

    def recurse(a=0, i=0):
        output = evaluate(program, a)

        if output == target:
            return a
        if output == target[-i:] or not i:
            for n in range(8):
                if found := recurse(a * 8 + n, i + 1):
                    return found

    return recurse()


def explore(input):
    ints = map(int, re.findall(r"Program: (.*)\n", input)[0].split(","))
    program = list(zip(ints, ints))  # (opcode, operand)
    target = [code for ops in program for code in ops]  # flatten

    def show_output(output, a):
        o = int("".join(map(str, output)))
        print(output, "a:", a, oct(a), "=> o:", o, oct(o))

    def compare(output, target):
        # compare with target
        comp = [" "] * 16
        for i in range(len(output)):
            if output[i] == target[i]:
                comp[i] = output[i]
        print("comp", len(list(filter(lambda n: n != " ", comp))), comp)

    args = sys.argv[1:]
    if len(args) >= 1:
        if args[0] == "random":
            o = random.randint(0, 281474976710655)
        elif args[0].startswith("0o"):
            o = int(args[0], 8)
        else:
            o = int(args[0])

        if len(args) >= 2:
            if args[1].startswith("0o"):
                p = int(args[1], 8)
            else:
                p = int(args[1])

            # make a range of inputs.
            print("input:", o, oct(o), "to", p, oct(p))
            asses = range(o, p + 1)
        else:
            # only one input.
            print("input:", o, oct(o))
            asses = [o]

        for a in asses:
            output = evaluate(program, a)
            show_output(output, a)
            compare(output, target)

    else:
        # asses = range(8**8 - 20, 8**8 + 20)
        # asses = [8**8 - 2, 8**8 - 1, 8**8, 8**8 + 1, 8**8 + 2]

        offset = 0
        for suffix in range(0o00, 0o77 + 1):
            t = ["1"] * 16
            o = oct(suffix)[2:].zfill(2)
            t[offset], t[offset + 1] = o[0], o[1]
            a = int("".join(t), 8)

            output = evaluate(program, a)
            show_output(output, a)
            compare(output, target)

            interesting = f"{output[offset]}{output[offset + 1]}"
            print(o, "=> interesting", interesting)


# --


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
    match opcodes[opcode]:
        case "adv":
            regs["a"] = regs["a"] // 2 ** combo(operand, regs)
        case "bdv":
            regs["b"] = regs["a"] // 2 ** combo(operand, regs)
        case "cdv":
            regs["c"] = regs["a"] // 2 ** combo(operand, regs)
        case "bxc":
            # xor
            regs["b"] = regs["b"] ^ regs["c"]
        case "bxl":
            # xor
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


# ---


def choose_input():
    filename = "input.txt"  # TODO: let's make input.txt the default and support others via env var.

    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    input = choose_input()
    print("part 1", solve(input, 1))
    print("part 2", solve(input, 2))
    # explore(input)
