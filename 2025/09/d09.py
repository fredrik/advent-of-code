from aoc import get_input
from itertools import combinations


def solve(input, part):
    points = list(parse_input(input))

    if part == 1:
        return max(area(p1, p2) for p1, p2 in combinations(points, 2))
    else:
        return max(
            area(p1, p2)
            for p1, p2 in combinations(points, 2)
            if valid_rectangle(p1, p2, points)
        )


def valid_rectangle(p1, p2, points):
    x1, y1 = p1
    x2, y2 = p2
    xmin, xmax = min(x1, x2), max(x1, x2)
    ymin, ymax = min(y1, y2), max(y1, y2)

    # check corners.
    corners = [(xmin, ymin), (xmin, ymax), (xmax, ymin), (xmax, ymax)]
    ps = set(points)
    if not all(c in ps or point_in_points(c, points) for c in corners):
        return False

    # check edges.
    edges = [
        ((xmin, ymin), (xmin, ymax)),
        ((xmax, ymin), (xmax, ymax)),
        ((xmin, ymin), (xmax, ymin)),
        ((xmin, ymax), (xmax, ymax)),
    ]
    if any(
        segments_intersect(*e, *p)
        for e in edges
        for p in zip(points, points[1:] + [points[0]])
    ):
        return False
    
    return True


def point_in_points(point, points):
    # ray casting!
    x, y = point
    inside = False
    for (xi, yi), (xj, yj) in zip(points, points[-1:] + points[:-1]):
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            inside = not inside
    return inside


def segments_intersect(a1, a2, b1, b2):
    (a1x, a1y), (a2x, a2y), (b1x, b1y), (b2x, b2y) = a1, a2, b1, b2
    if a1y == a2y and b1x == b2x:  # a horizontal, b vertical
        return min(a1x, a2x) < b1x < max(a1x, a2x) and min(b1y, b2y) < a1y < max(
            b1y, b2y
        )
    if a1x == a2x and b1y == b2y:  # a vertical, b horizontal
        return min(b1x, b2x) < a1x < max(b1x, b2x) and min(a1y, a2y) < b1y < max(
            a1y, a2y
        )
    return False


def area(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2
    return (abs(p1x - p2x) + 1) * (abs(p1y - p2y) + 1)


def parse_input(input):
    for line in input:
        a, b = line.rstrip().split(",")
        yield int(a), int(b)


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
