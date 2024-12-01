# input = """
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# """

with open("input.txt", "r") as file:
    input = file.read()


def main():
    xs, ys, distances = [], [], []

    lines = input.strip().splitlines()
    for line in lines:
        x, y = map(int, line.split())
        xs.append(x)
        ys.append(y)

    xs.sort()
    ys.sort()

    for x, y in zip(xs, ys):
        distance = abs(x - y)
        distances.append(distance)
        # print(f"{x} {y} {distance}")

    print(sum(distances))


if __name__ == "__main__":
    main()
