from aoc import get_input
import hashlib


def solve(data, part):
    key = data.strip()
    i = 0
    while True:
        s = (key + str(i)).encode("utf-8")
        h = hashlib.md5(s).hexdigest()
        if compare(h, part):
            return i
        i += 1


def compare(h, part):
    if part == 1:
        return h[0:5] == "00000"
    if part == 2:
        return h[0:6] == "000000"

    0 / 0  # !


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
