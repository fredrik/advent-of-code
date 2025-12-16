from aoc import get_input
import re

from string import ascii_lowercase


# Santa's previous password expired, and he needs help choosing a new one.
def solve(data, part):
    initial_password = parse_input(data)

    if part == 1:
        return next_password(initial_password)
    else:
        return next_password(next_password(initial_password))

def parse_input(data):
    return data.strip().split('\n')[0].strip()

def next_password(password):
    for password in next_passwords(password):
        if valid_password(password):
            return password


next_letters = dict(zip(iter(ascii_lowercase), iter(ascii_lowercase[1:])))
last_password = ["z", "z", "z", "z", "z", "z", "z", "z"]


def next_passwords(initial_password):
    def _next(p):
        for i in range(len(p) - 1, -1, -1):
            if p[i] != "z":
                p[i] = chr(ord(p[i]) + 1)
                return p
            else:
                if i == 0:
                    return last_password
                else:
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


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
