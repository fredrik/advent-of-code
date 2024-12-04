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
    xs, ys, _ = [], [], []
    freq = {}

    lines = input.strip().splitlines()
    for line in lines:
        x, y = map(int, line.split())
        xs.append(x)
        ys.append(y)

    for y in ys:
        if y in freq:
            freq[y] += 1
        else:
            freq[y] = 1

    total_score = 0
    for x in xs:
        score = x * freq.get(x, 0)
        total_score += score
        # print(f"{x} {score}")

    print(total_score)


if __name__ == "__main__":
    main()
