import itertools


def solve(input, part):
    wires_raw, gates_raw = input.split("\n\n")
    wires = {wire.split(":")[0]: int(wire.split(":")[1]) for wire in wires_raw.strip().splitlines()}
    gatestuples = [tuple(gate.replace("->", "").strip().split()) for gate in gates_raw.strip().splitlines()]
    gates = {gate[3]: {"op": gate[1], "a": gate[0], "b": gate[2]} for gate in gatestuples}

    if part == 1:
        return part1(wires, gates)
    else:
        return part2(wires, gates)


def part1(wires, gates):
    return find_z(wires, gates)


def part2(wires, gates):
    find_z(wires, gates)

    def dig(name, depth=0):
        if depth > 2:
            return
        if depth == 0:
            print("dig", name)
        if name in wires:
            print(" " * depth, name, "wire", wires[name])
        else:
            g = gates[name]
            print(" " * depth, name, "=", g["op"], g["a"], g["b"])
            dig(g["a"], depth + 1)
            dig(g["b"], depth + 1)
        if depth == 0:
            print("++++++++++++")

    dig("z03")
    dig("z04")
    dig("z05")
    dig("z06")
    dig("z07")
    dig("z08")

    return

    # "there are exactly four pairs of gates whose output wires have been swapped"
    xval = 0
    xs = set([k for k in wires.keys() if k.startswith("x")])
    for n, xk in enumerate(sorted(xs)):
        v = wires[xk]
        xval += v << n
    yval = 0
    ys = set([k for k in wires.keys() if k.startswith("y")])
    for n, yk in enumerate(sorted(ys)):
        v = wires[yk]
        yval += v << n

    actual_output = xval + yval
    print(xval, "+", yval, "=", actual_output)
    print("erroneous output:", find_z(wires, gates))
    print(bin(actual_output))
    print(bin(find_z(wires, gates)))
    diff = actual_output ^ find_z(wires, gates)
    print(bin(diff))

    return

    # ---

    # for all permutations of 4 pairs of gates..

    print("number of gates:", len(gates))

    count = 0
    for perm in itertools.permutations(gates.keys(), 8):
        # reset
        gs = gates.copy()

        # swap
        a, b, c, d, e, f, g, h = perm

        # print("g[a]", gs[a])
        # print("g[b]", gs[b])
        # print("g[c]", gs[c])
        # print("g[d]", gs[d])

        # print("swap", a, b, c, d)

        gs[a], gs[b] = gs[b], gs[a]
        gs[c], gs[d] = gs[d], gs[c]
        gs[e], gs[f] = gs[f], gs[e]
        gs[g], gs[h] = gs[h], gs[g]

        # print("g[a]", gs[a])
        # print("g[b]", gs[b])
        # print("g[c]", gs[c])
        # print("g[d]", gs[d])

        # eval
        z = find_z(wires, gs)

        if z == actual_output:
            return ",".join(perm)

        count += 1
        if count % 100000 == 0:
            print(count, perm)

    print("exhausted all permutations", count)


def find_z(wires, gates):
    val = 0

    # z00 is the least significant bit
    # shift by n
    zs = set([k for k in gates.keys() if k.startswith("z")])
    for n, zk in enumerate(sorted(zs)):
        g = gates[zk]
        v = evaluate(g, wires, gates)
        # print(n, v, v << n)
        val += v << n

    return val


def evaluate(g, wires, gates):
    if "out" in g:
        return g["out"]

    a, b = g["a"], g["b"]
    if a in wires:
        aval = wires[a]
    else:
        aval = evaluate(gates[a], wires, gates)
    if b in wires:
        bval = wires[b]
    else:
        bval = evaluate(gates[b], wires, gates)

    # print("evaluate", g, a, aval, b, bval)

    if g["op"] == "AND":
        out = aval & bval
    elif g["op"] == "OR":
        out = aval | bval
    elif g["op"] == "XOR":
        out = aval ^ bval

    g["out"] = out
    return out


# ---


import os


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        filename = "input.txt"
    else:
        filename = "input.alt"

    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    input = choose_input()
    # print("part 1:", solve(input, 1))
    print("part 2:", solve(input, 2))
