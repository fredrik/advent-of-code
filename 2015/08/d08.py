import os


def solve(data, part):
    count = 0
    for line in data.splitlines():
        escaped = bytes(line, "utf-8").decode("unicode_escape")
        a, b = len(line), len(escaped) - 2
        count = count + a - b
    return count


# ---s


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
