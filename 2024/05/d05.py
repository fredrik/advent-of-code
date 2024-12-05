import os
from collections import defaultdict


def part1(input):
    rules, updates = parse_input(input)

    sum = 0
    for update in updates:
        if valid_update(update, rules):
            sum += middle_element(update)
    return sum


def part2(input):
    rules, updates = parse_input(input)

    sum = 0
    for update in updates:
        if not valid_update(update, rules):
            reordered = order_correctly(update, rules)
            print(f"reordered: {reordered}")
            sum += middle_element(reordered)
    return sum


def valid_update(update, rules):
    seen = set()
    for i in range(len(update)):
        item = update[i]
        seen.add(item)
        if rules[item] & seen:
            return False
    else:
        return True


def order_correctly(update, rules):
    def wrong_order(item, next_item, rules):
        return rules[next_item] & {item}

    for i in range(len(update) - 1):
        item, next_item = update[i], update[i + 1]
        if wrong_order(item, next_item, rules):
            update[i], update[i + 1] = next_item, item  # swap
            return order_correctly(update, rules)

    return update


def middle_element(update):
    return int(update[len(update) // 2])


def parse_input(input):
    rules_raw, updates_raw = input.strip().split("\n\n")

    rules = defaultdict(set)
    for rule in rules_raw.strip().splitlines():
        left, right = rule.split("|")
        rules[left.strip()].add(right.strip())

    updates = []
    for update in updates_raw.strip().splitlines():
        updates.append(update.strip().split(","))

    return rules, updates


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        with open("input.txt", "r") as f:
            return f.read()
    else:
        with open("input.mini", "r") as f:
            return f.read()


if __name__ == "__main__":
    input = choose_input()
    print(part1(input))
    print(part2(input))
