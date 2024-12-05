import os
from collections import defaultdict


def part1(input):
    rules, updates = parse_input(input)
    # print(f"rules: {rules}")
    # print(f"updates: {updates}")

    sum = 0
    for update in updates:
        valid_update = True
        seen = set()
        for i in range(len(update)):
            item = update[i]
            seen.add(item)
            if rules[item] & seen:
                valid_update = False
                break
        if valid_update:
            # update is valid. get middle number.
            sum += int(update[int(len(update) / 2)])

    print(sum)


def part2(input):
    rules, updates = parse_input(input)
    # print(f"rules: {rules}")
    # print(f"updates: {updates}")

    sum = 0
    for update in updates:
        valid_update = True
        seen = set()
        for i in range(len(update)):
            item = update[i]
            seen.add(item)
            if rules[item] & seen:
                valid_update = False
                break

        if not valid_update:
            reordered = reorder(update, rules)
            sum += int(reordered[int(len(reordered) / 2)])
            # print(f"invalid update: {update}")
            # print(f"reordered: {reordered}")
            # print()

    print(sum)


def reorder(update, rules):
    for i in range(len(update) - 1):
        item = update[i]
        next_item = update[i + 1]
        # print(f"item: {item}, next_item: {next_item}, itemrules: {rules[item]}, nextitemrules: {rules[next_item]}")
        if wrong_order(item, next_item, rules):
            # swap
            update[i], update[i + 1] = next_item, item
            return reorder(update, rules)

    return update


def wrong_order(item, next_item, rules):
    return rules[next_item] & {item}


def parse_input(input):
    rules_raw, updates_raw = input.strip().split("\n\n")

    rules = defaultdict(set)
    updates = []
    for rule in rules_raw.strip().splitlines():
        left, right = rule.split("|")
        rules[left.strip()].add(right.strip())
    for update in updates_raw.strip().splitlines():
        updates.append(update.strip().split(","))

    return rules, updates


def choose_input():
    if os.environ.get("LARGE_INPUT"):
        with open("input.txt", "r") as f:
            return f.read()
    else:
        with open("input.small", "r") as f:
            return f.read()


if __name__ == "__main__":
    input = choose_input()
    part1(input)
    part2(input)
