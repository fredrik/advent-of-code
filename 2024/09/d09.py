from aoc import get_input


def solve(input, part):
    disk, identifiers, holes = parse_input(input)

    if part == 1:
        while True:
            for k in range(len(disk) - 1):
                if disk[k] == ".":
                    first_free = (k, ".")
                    break

            for k in range(len(disk) - 1, 0, -1):
                if disk[k] != ".":
                    last_block = (k, disk[k])
                    break

            if first_free[0] > last_block[0]:
                break

            disk[first_free[0]] = last_block[1]
            disk[last_block[0]] = "."
    else:
        for identifier in reversed(identifiers.keys()):
            (c, j, jj) = identifiers[identifier]

            free = None
            for i in range(len(holes) - 1):
                hc, hj, hjj = holes[i]
                if hj > j:
                    break
                elif c <= hc:
                    free = i
                    break
                else:
                    continue

            if free != None:
                (hc, hj, hjj) = holes[i]

                assert c <= hc

                for k in range(hj, hj + c):
                    disk[k] = identifier

                for k in range(j, jj):
                    disk[k] = "."

                holes[i] = (hc - c, hj + c, hj + c + (hc - c))

    checksum = 0
    for k, identifier in disk.items():
        if identifier != ".":
            checksum += k * identifier

    return checksum


def parse_input(input):
    counts = [int(c) for c in input[0].strip()]

    disk = {}
    identifiers = {}
    holes = []
    j = 0
    for i, c in enumerate(counts):
        if i % 2 == 0:
            identifier = i // 2
            identifiers[identifier] = (c, j, j + c)
            for k in range(j, j + c):
                disk[k] = identifier
        else:
            holes.append((c, j, j + c))
            for k in range(j, j + c):
                disk[k] = "."

        j += c

    return disk, identifiers, holes


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
