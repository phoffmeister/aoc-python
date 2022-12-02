from typing import Dict, Tuple
from aockit import get_input

# A - ROCK
# B - PAPER
# C - SCISSORS

# X - ROCK
# Y - PAPER
# Z - SCISSORS

result: Dict[Tuple[str, str], int] = {
    ('A', 'X'): 3 + 1,
    ('A', 'Y'): 6 + 2,
    ('A', 'Z'): 0 + 3,
    ('B', 'X'): 0 + 1,
    ('B', 'Y'): 3 + 2,
    ('B', 'Z'): 6 + 3,
    ('C', 'X'): 6 + 1,
    ('C', 'Y'): 0 + 2,
    ('C', 'Z'): 3 + 3,
}

how: Dict[Tuple[str, str], str] = {
    ('A', 'X'): 'Z',
    ('A', 'Y'): 'X',
    ('A', 'Z'): 'Y',
    ('B', 'X'): 'X',
    ('B', 'Y'): 'Y',
    ('B', 'Z'): 'Z',
    ('C', 'X'): 'Y',
    ('C', 'Y'): 'Z',
    ('C', 'Z'): 'X',
}

def part1():
    data = get_input(2022, 2)
    score = 0

    for row in data.split('\n'):
        if row == "":
            continue
        other, me = row.split(' ')
        score += result[(other, me)]

    print(f"Part1: {score}")


def part2():
    data = get_input(2022, 2)
    score = 0
    for row in data.split('\n'):
        if row == "":
            continue
        other, goal = row.split(' ')

        me = how[(other, goal)]
        score += result[(other, me)]

    print(f"Part2: {score}")


if __name__ == "__main__":
    part1()
    part2()
