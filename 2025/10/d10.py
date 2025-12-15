from aoc import get_input
from collections import deque
import re

infinity = float("inf")
epsilon = 1e-9


def solve(input, part):
    machines = list(parse_input(input, part))
    if part == 1:
        return sum(presses(0, target, toggles) for target, toggles in machines)
    else:
        return sum(min_presses(target, toggles) for target, toggles in machines)


def presses(state, target, toggles):
    if state == target:
        return 0

    visited = {state}
    queue = deque([(state, 0)])

    while queue:
        current, depth = queue.popleft()
        for t in toggles:
            neighbour = current ^ t
            if neighbour == target:
                return depth + 1
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, depth + 1))


def min_presses(target, toggles):
    num_vars = len(toggles)
    num_dims = len(target)

    # Build constraint matrix: Ax <= b
    # Equality constraints become Ax <= b AND -Ax <= -b
    # Non-negativity: -x_i <= 0
    constraints = [[0] * (num_vars + 1) for _ in range(2 * num_dims + num_vars)]

    for i in range(num_vars):
        constraints[~i][i] = -1

    for i in range(num_dims):
        for j in range(num_vars):
            constraints[i][j] = toggles[j][i]
            constraints[i + num_dims][j] = -toggles[j][i]
        constraints[i][-1] = target[i]
        constraints[i + num_dims][-1] = -target[i]

    return ilp(constraints)


def ilp(constraints):
    num_vars = len(constraints[0]) - 1

    def branch(constraints, best):
        value, solution = simplex(constraints, [1] * num_vars)
        if value + epsilon >= best or value == -infinity:
            return best

        # Find first non-integer variable
        fractional = next(
            (
                (i, int(v))
                for i, v in enumerate(solution)
                if abs(v - round(v)) > epsilon
            ),
            (-1, 0),
        )

        if fractional[0] == -1:
            return min(best, value)

        var_idx, floor_val = fractional
        lo_constraint = [0] * num_vars + [floor_val]
        lo_constraint[var_idx] = 1
        best = branch(constraints + [lo_constraint], best)
        hi_constraint = [0] * num_vars + [~floor_val]
        hi_constraint[var_idx] = -1
        return branch(constraints + [hi_constraint], best)

    best = branch(constraints, infinity)
    return round(best) if best != infinity else 0


def simplex(constraints, costs):
    num_constraints = len(constraints)
    num_vars = len(constraints[0]) - 1

    non_basic = [*range(num_vars), -1]
    basic = [*range(num_vars, num_vars + num_constraints)]
    tableau = [[*row, -1] for row in constraints] + [
        costs + [0, 0],
        [0] * (num_vars + 2),
    ]

    for i in range(num_constraints):
        tableau[i][-2], tableau[i][-1] = tableau[i][-1], tableau[i][-2]

    def pivot(row, col):
        scale = 1 / tableau[row][col]
        for i in range(num_constraints + 2):
            if i == row:
                continue
            for j in range(num_vars + 2):
                if j != col:
                    tableau[i][j] -= tableau[row][j] * tableau[i][col] * scale
        for i in range(num_vars + 2):
            tableau[row][i] *= scale
        for i in range(num_constraints + 2):
            tableau[i][col] *= -scale
        tableau[row][col] = scale
        basic[row], non_basic[col] = non_basic[col], basic[row]

    def find(phase):
        while True:
            col = min(
                (i for i in range(num_vars + 1) if phase or non_basic[i] != -1),
                key=lambda c: (tableau[num_constraints + phase][c], non_basic[c]),
            )
            if tableau[num_constraints + phase][col] > -epsilon:
                return True
            candidates = [
                i for i in range(num_constraints) if tableau[i][col] > epsilon
            ]
            if not candidates:
                return False
            row = min(
                candidates, key=lambda r: (tableau[r][-1] / tableau[r][col], basic[r])
            )
            pivot(row, col)

    tableau[-1][num_vars] = 1
    row = min(range(num_constraints), key=lambda r: tableau[r][-1])

    if tableau[row][-1] < -epsilon:
        pivot(row, num_vars)
        if not find(1) or tableau[-1][-1] < -epsilon:
            return -infinity, None

    for i in range(num_constraints):
        if basic[i] == -1:
            pivot(i, min(range(num_vars), key=lambda c: (tableau[i][c], non_basic[c])))

    if find(0):
        solution = [0] * num_vars
        for i in range(num_constraints):
            if 0 <= basic[i] < num_vars:
                solution[basic[i]] = tableau[i][-1]
        return sum(costs[i] * solution[i] for i in range(num_vars)), solution
    return -infinity, None


def parse_input(input, part):
    def parse_toggles(str):
        return [
            tuple(map(int, s.split(",")))
            for s in str.replace("(", "").replace(")", "").split(" ")
        ]

    def to_binary(bitmask):
        return int("".join("1" if b else "0" for b in bitmask), 2)

    for line in input:
        match = re.search(r"\[(.+)\] (.*) \{(.*)\}", line)
        if match:
            lights = [s == "#" for s in match.group(1)]
            positions = parse_toggles(match.group(2))

            if part == 1:
                # lights and toggles as bitmasks for XOR
                toggles = [[i in pos for i in range(len(lights))] for pos in positions]
                yield (to_binary(lights), tuple(to_binary(t) for t in toggles))
            else:
                # joltages and toggles as tuples for ILP
                joltages = tuple(int(s.strip()) for s in match.group(3).split(","))
                toggles = tuple(
                    tuple(1 if i in pos else 0 for i in range(len(lights)))
                    for pos in positions
                )
                yield (joltages, toggles)


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
