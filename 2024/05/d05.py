from aoc import get_input

from collections import defaultdict


def solve(input, part):
    rules, updates = parse_input(input)

    if part == 1:
        return sum(
            middle_element(update) for update in updates if valid_update(update, rules)
        )
    else:
        return sum(
            middle_element(order_correctly(update, rules))
            for update in updates
            if not valid_update(update, rules)
        )


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


if __name__ == "__main__":
    data = get_input(raw=True)
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
