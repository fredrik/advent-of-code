from aoc import get_input


def solve(input, part):
    wires, gates = parse_input(input)

    if part == 1:
        return find_z(wires, gates)
    else:
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

        for i in range(45 + 1):
            dig(f"z{str(i).zfill(2)}")

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

        correct_sum = xval + yval
        diff = correct_sum ^ find_z(wires, gates)
        print(xval, "+", yval, "=", correct_sum)
        print("erroneous output:", find_z(wires, gates))
        print("corr", format(correct_sum, "#050b"))
        print("err ", format(find_z(wires, gates), "#050b"))
        print("diff", format(diff, "#050b"))

        return "manual detective work"


def find_z(wires, gates):
    val = 0

    zs = set([k for k in gates.keys() if k.startswith("z")])
    for n, zk in enumerate(sorted(zs)):
        g = gates[zk]
        v = evaluate(g, wires, gates)
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

    if g["op"] == "AND":
        out = aval & bval
    elif g["op"] == "OR":
        out = aval | bval
    elif g["op"] == "XOR":
        out = aval ^ bval

    g["out"] = out
    return out


def parse_input(input):
    wires_raw, gates_raw = input.split("\n\n")
    wires = {
        wire.split(":")[0]: int(wire.split(":")[1])
        for wire in wires_raw.strip().splitlines()
    }
    gatestuples = [
        tuple(gate.replace("->", "").strip().split())
        for gate in gates_raw.strip().splitlines()
    ]
    gates = {
        gate[3]: {"op": gate[1], "a": gate[0], "b": gate[2]} for gate in gatestuples
    }
    return wires, gates


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
