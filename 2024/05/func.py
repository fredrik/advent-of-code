# maximal functional style
def part1(input):
    rules, updates = parse_input(input)

    def middle_element(update):
        return int(update[len(update) // 2])

    return sum(map(middle_element, filter(partial(valid_update, rules=rules), updates)))


# funtional style
def part1(input):
    rules, updates = parse_input(input)
    return sum(int(update[int(len(update) / 2)]) for update in updates if valid_update(update, rules))


def part2(input):
    rules, updates = parse_input(input)
    return sum(
        int(reordered[int(len(reordered) / 2)])
        for update in updates
        if not valid_update(update, rules)
        for reordered in [reorder(update, rules)]
    )
