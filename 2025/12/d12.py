from aoc import get_input


def solve(input, part):
    shapes, regions = parse_input(input)

    if part == 1:
        count = 0
        for width, height, counts in regions:
            if can_fit_region(shapes, width, height, counts):
                count += 1
        return count
    else:
        return "Merry Christmas!"


def can_fit_region(shapes, width, height, counts):
    total_cells = sum(counts[i] * len(shapes[i]) for i in range(len(counts)))
    if total_cells > width * height:
        return False
    if sum(counts) == 0:
        return True

    placements = {}
    for idx, count in enumerate(counts):
        if count > 0:
            p = []
            for orientation in get_orientations(shapes[idx]):
                max_r = max(r for r, c in orientation)
                max_c = max(c for r, c in orientation)
                for sr in range(height - max_r):
                    for sc in range(width - max_c):
                        mask = 0
                        for r, c in orientation:
                            mask |= 1 << ((r + sr) * width + (c + sc))
                        p.append(mask)
            if not p:
                return False
            placements[idx] = p

    pieces = []
    for idx, count in enumerate(counts):
        pieces.extend([idx] * count)
    pieces.sort(key=lambda s: len(placements[s]))

    def backtrack(i, used):
        if i == len(pieces):
            return True
        for mask in placements[pieces[i]]:
            if (used & mask) == 0:
                if backtrack(i + 1, used | mask):
                    return True
        return False

    return backtrack(0, 0)


def get_orientations(cells):
    orientations = set()
    current = normalize(cells)
    for _ in range(4):
        orientations.add(current)
        orientations.add(flip_h(current))
        current = rotate_90(current)
    return orientations


def rotate_90(cells):
    return normalize({(c, -r) for r, c in cells})


def flip_h(cells):
    return normalize({(r, -c) for r, c in cells})


def normalize(cells):
    if not cells:
        return frozenset()
    min_r = min(r for r, c in cells)
    min_c = min(c for r, c in cells)
    return frozenset((r - min_r, c - min_c) for r, c in cells)


def parse_input(lines):
    shapes = {}
    regions = []
    shape_idx = None
    shape_rows = []

    def parse_shape(rows):
        cells = set()
        for row, line in enumerate(rows):
            for col, ch in enumerate(line):
                if ch == "#":
                    cells.add((row, col))
        return cells

    for line in lines:
        line = line.rstrip("\n")
        if line.endswith(":") and line[:-1].isdigit():
            if shape_idx is not None:
                shapes[shape_idx] = parse_shape(shape_rows)
            shape_idx = int(line[:-1])
            shape_rows = []
        elif "x" in line and ": " in line:
            if shape_idx is not None:
                shapes[shape_idx] = parse_shape(shape_rows)
                shape_idx = None
            size, counts = line.split(": ")
            w, h = map(int, size.split("x"))
            regions.append((w, h, list(map(int, counts.split()))))
        elif shape_idx is not None and line:
            shape_rows.append(line)

    return shapes, regions


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
