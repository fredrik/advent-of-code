def solve(input, part):
    wires_raw, gates_raw = input.split("\n\n")
    wires = {wire.split(":")[0]: int(wire.split(":")[1]) for wire in wires_raw.strip().splitlines()}
    gatestuples = [tuple(gate.replace("->", "").strip().split()) for gate in gates_raw.strip().splitlines()]
    gates = {gate[3]: {"op": gate[1], "a": gate[0], "b": gate[2]} for gate in gatestuples}

    # z00 is the least significant bit
    # shift by n
    val = 0
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
        filename = "input.large"

    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    input = choose_input()
    print("part 1:", solve(input, 1))
    # print("part 2:", solve(input, 2))
