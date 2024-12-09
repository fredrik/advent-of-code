import os


def part1(input):
    counts = [int(c) for c in input.splitlines()[0]]

    disk = {}
    j = 0
    for i, c in enumerate(counts):
        if i % 2 == 0:
            # file
            identifier = i // 2
            for k in range(j, j + c):
                disk[k] = identifier
        else:
            # free space
            for k in range(j, j + c):
                disk[k] = "."

        j += c

    # print_layout(disk)

    while True:
        # too slow!
        # free = [(k, i) for (k,i) in disk.items() if i == '.']
        # blocks = [(k, i) for (k,i) in disk.items() if i != '.']
        # last_block = blocks[-1]
        # first_free = free[0]

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

    checksum = 0
    for k, identifier in disk.items():
        if identifier != ".":
            checksum += k * identifier

    return checksum


def part2(input):
    counts = [int(c) for c in input.splitlines()[0]]

    disk = {}
    identifiers = {}
    holes = []
    j = 0
    for i, c in enumerate(counts):
        if i % 2 == 0:
            # file
            identifier = i // 2
            identifiers[identifier] = (c, j, j + c)
            for k in range(j, j + c):
                disk[k] = identifier
        else:
            # free space
            holes.append((c, j, j + c))
            for k in range(j, j + c):
                disk[k] = "."

        j += c

    for identifier in reversed(identifiers.keys()):
        (c, j, jj) = identifiers[identifier]

        # find free space at at least c blocks long
        free = None
        for i in range(len(holes) - 1):
            hc, hj, hjj = holes[i]
            if hj > j:
                # all free holes located after file.
                break
            elif c <= hc:
                free = i
                break
            else:
                # free hole too small. find another.
                continue

        if free != None:
            (hc, hj, hjj) = holes[i]

            assert c <= hc

            # move the whole block to start of free space, possibly filling all free space.
            for k in range(hj, hj + c):
                disk[k] = identifier

            # move free space.
            for k in range(j, jj):
                disk[k] = "."

            # update holes. (identifiers can be left unupdated, we will not refer to it after this loop).
            holes[i] = (hc - c, hj + c, hj + c + (hc - c))

    # print_layout(disk)

    checksum = 0
    for k, identifier in disk.items():
        if identifier != ".":
            checksum += k * identifier

    return checksum


def print_layout(disk):
    print("disk layout: ", end="")
    for k in range(len(disk)):
        print(disk[k], end="")
    print()


def print_holes(holes):
    print("holes:")
    for hole in holes:
        print(hole)
    print()


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        filename = "input.txt"
    else:
        filename = "input.small"

    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    input = choose_input()
    print(part1(input))
    print(part2(input))
