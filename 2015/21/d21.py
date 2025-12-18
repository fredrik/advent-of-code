from itertools import combinations
from aoc import get_input

WEAPONS = [
    (8, 4, 0),    # Dagger
    (10, 5, 0),   # Shortsword
    (25, 6, 0),   # Warhammer
    (40, 7, 0),   # Longsword
    (74, 8, 0),   # Greataxe
]

ARMOR = [
    (0, 0, 0),    # None
    (13, 0, 1),   # Leather
    (31, 0, 2),   # Chainmail
    (53, 0, 3),   # Splintmail
    (75, 0, 4),   # Bandedmail
    (102, 0, 5),  # Platemail
]

RINGS = [
    (0, 0, 0),    # None (slot 1)
    (0, 0, 0),    # None (slot 2)
    (25, 1, 0),   # Damage +1
    (50, 2, 0),   # Damage +2
    (100, 3, 0),  # Damage +3
    (20, 0, 1),   # Defense +1
    (40, 0, 2),   # Defense +2
    (80, 0, 3),   # Defense +3
]


def player_wins(player_hp, player_dmg, player_armor, boss_hp, boss_dmg, boss_armor):
    player_hit = max(1, player_dmg - boss_armor)
    boss_hit = max(1, boss_dmg - player_armor)
    player_turns = (boss_hp + player_hit - 1) // player_hit
    boss_turns = (player_hp + boss_hit - 1) // boss_hit
    return player_turns <= boss_turns


def solve(input, part):
    boss_hp, boss_dmg, boss_armor = parse_input(input)
    player_hp = 100

    results = []
    for w in WEAPONS:
        for a in ARMOR:
            for r1, r2 in combinations(RINGS, 2):
                cost = w[0] + a[0] + r1[0] + r2[0]
                dmg = w[1] + a[1] + r1[1] + r2[1]
                armor = w[2] + a[2] + r1[2] + r2[2]
                win = player_wins(player_hp, dmg, armor, boss_hp, boss_dmg, boss_armor)
                results.append((cost, win))

    if part == 1:
        return min(cost for cost, win in results if win)
    else:
        return max(cost for cost, win in results if not win)


def parse_input(input):
    vals = [int(line.split(": ")[1]) for line in input]
    return vals[0], vals[1], vals[2]


if __name__ == "__main__":
    data = get_input()
    print("part 1:", solve(data, 1))
    print("part 2:", solve(data, 2))
