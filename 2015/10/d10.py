from aoc import get_input

def solve(data, part):
    seq, iterations = parse_input(data)

    if part == 1:
        for _ in range(iterations):
            seq = next_seq(seq)
        return len(seq)
    else:
        for _ in range(50):
            seq = next_seq(seq)
        return len(seq)

def next_seq(seq):
    r = [] # target

    x = seq[0]
    count = 1

    for y in seq[1:]:
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

def parse_input(data):
    lines = data.strip().split('\n')
    return [int(x) for x in lines[0].strip()], int(lines[1].strip())


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))