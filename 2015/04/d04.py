import hashlib
import os


def solve(data, part):
    for key in data.splitlines():
        i = 0
        while True:
            if hashlib.md5((key + str(i)).encode("utf-8")).hexdigest()[0:5] == "00000":
                return i
            i += 1


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
    # print("part 2:", solve(data, 2))
