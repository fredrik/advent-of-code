import re
import os

from string import ascii_lowercase


# Santa's previous password expired, and he needs help choosing a new one.
def solve(input, part):
    initial_password = parse_input(input)

    if part == 1:
        print(f"initial: {initial_password}")
        for password in next_passwords(initial_password):
            print(f"password: {password}")
            if valid_password(password):
                return password
    else:
        return


def parse_input(input):
    return input[0].strip()


next_letters = dict(zip(iter(ascii_lowercase), iter(ascii_lowercase[1:])))
last_password = ["z", "z", "z", "z", "z", "z", "z", "z"]


def next_passwords(initial_password):
    def _next(p):
        for i in range(len(p) - 1, -1, -1):
            # print(f'i:{i}')
            if p[i] != "z":
                # print(f'p[{i}]: {p[i]} => {chr(ord(p[i]) + 1)}')
                p[i] = chr(ord(p[i]) + 1)
                return p
            else:
                if i == 0:
                    return last_password
                else:
                    # print(f'p[{i}]: {p[i]} => "a"')
                    p[i] = "a"

    password = [x for x in initial_password]

    while password != last_password:
        password = _next(password)
        yield "".join(password)


increasing_straight_line = [
    "".join(t)
    for t in (
        zip(iter(ascii_lowercase), iter(ascii_lowercase[1:]), iter(ascii_lowercase[2:]))
    )
]
pattern = re.compile(r"(\w)\1.*(\w)\2")


def valid_password(password):
    if "i" in password or "l" in password or "o" in password:
        return False

    if not any(abc in password for abc in increasing_straight_line):
        return False

    if not re.search(pattern, password):
        return False

    return True


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
