import os

def solve(input, part):
    seq, iterations = parse_input(input)

    if part == 1:
        for _ in range(iterations):
            seq = next_seq(seq)
        return len(seq)
    else:
        for _ in range(50):
            seq = next_seq(seq)
        return len(seq)

def next_seq(seq):
    if len(seq) == 1:
        return [1,seq[0]]

    r = [] # target

    x = seq.pop(0)
    count = 1

    while seq:
        y = seq.pop(0)

        if y == x:
            count += 1
        else:
            r.append(count)
            r.append(x)
            count = 1
            x = y

    if y == x:
        r.append(count)
        r.append(x)

    return r

def parse_input(input):
    return [int(x) for x in input[0].strip()], int(input[1].strip())

# ---

def get_input():
    if os.environ.get("INPUT"):
        filename = os.environ.get("INPUT")
    else:
        filename = "input.txt"
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, "r") as f:
        return f.readlines()


if __name__ == "__main__":
    input = get_input()
    print("part 1:", solve(input, 1))
    print("part 2:", solve(input, 2))