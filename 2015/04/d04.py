import hashlib
import os


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


# ---


def get_input_data():
    if os.environ.get("INPUT"):
        filename = os.environ.get("INPUT")
    else:
        filename = "input.txt"

    filepath = os.path.join(os.path.dirname(__file__), filename)

    with open(filepath, "r") as f:
        return f.read()


if __name__ == "__main__":
    data = get_input_data()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
