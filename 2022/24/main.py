from enum import Enum
from typing import List, Tuple
from aockit import get_input


class Direction(Enum):
    UP = "^"
    DOWN = "v"
    RIGHT = ">"
    LEFT = "<"


class Blizzard:
    def __init__(self, direction: Direction, position: Tuple[int, int]) -> None:
        self.direction = direction
        self.position = position


def read_field(
    rows: List[str],
) -> Tuple[List[Blizzard], Tuple[int, int], Tuple[int, int], int, int]:
    x = 0
    y = 0
    first = True
    start = 0, 0
    end = 0, 0
    walls = set()
    blizzards = list()
    for row in rows:
        x = 0
        for c in row:
            if c == ".":
                if first:
                    first = False
                    start = x, y
                end = x, y
            elif c == "#":
                walls.add((x, y))
            else:
                if c == Direction.UP.value:
                    blizzards.append(Blizzard(Direction.UP, (x, y)))
                elif c == Direction.DOWN.value:
                    blizzards.append(Blizzard(Direction.DOWN, (x, y)))
                elif c == Direction.RIGHT.value:
                    blizzards.append(Blizzard(Direction.RIGHT, (x, y)))
                elif c == Direction.LEFT.value:
                    blizzards.append(Blizzard(Direction.LEFT, (x, y)))
                else:
                    raise Exception(f"Unknown field {c}")

            x += 1
        y += 1
    return blizzards, start, end, x - 2, y - 2


def move_blizzards(blizzards: List[Blizzard], max_x, max_y):
    for b in blizzards:
        x, y = b.position
        if b.direction == Direction.UP:
            y -= 1
            if y == 0:
                y = max_y
        elif b.direction == Direction.DOWN:
            y += 1
            if y == max_y + 1:
                y = 1
        elif b.direction == Direction.RIGHT:
            x += 1
            if x == max_x + 1:
                x = 1
        elif b.direction == Direction.LEFT:
            x -= 1
            if x == 0:
                x = max_x
        b.position = x, y


def print_blizzards(blizzards: List[Blizzard], max_x, max_y):
    dir = Direction.UP
    for y in range(max_y + 2):
        row = ""
        for x in range(max_x + 2):
            if x == 0 or y == 0 or x == max_x + 1 or y == max_y + 1:
                row += "#"
                continue
            count = 0
            for b in blizzards:
                if b.position == (x, y):
                    if count == 0:
                        dir = b.direction
                    count += 1
            if count == 0:
                row += "."
            elif count == 1:
                row += dir.value
            else:
                row += str(count)
        print(row)


offsets = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]


def how_long(blizzards, start, end, x, y) -> int:
    positions = {start}
    steps = 0
    while end not in positions:
        steps += 1
        to_add = list()
        for pos in positions:
            for x_off, y_off in offsets:
                n_pos = x_off + pos[0], y_off + pos[1]
                if n_pos == end:
                    to_add.append(n_pos)
                if n_pos[0] <= 0 or n_pos[1] <= 0:
                    continue
                if n_pos[0] == x + 1 or n_pos[1] == y + 1:
                    continue
                to_add.append(n_pos)
        for a in to_add:
            positions.add(a)
        move_blizzards(blizzards, x, y)
        for b in blizzards:
            if b.position in positions:
                positions.remove(b.position)
    return steps


def part1():
    data = get_input(2022, 24)
    rows = [row for row in data.split("\n") if row != ""]
    blizzards, start, end, x, y = read_field(rows)
    steps = how_long(blizzards, start, end, x, y)
    print("Part 1:", steps)


def part2():
    data = get_input(2022, 24)
    rows = [row for row in data.split("\n") if row != ""]
    blizzards, start, end, x, y = read_field(rows)

    a = how_long(blizzards, start, end, x, y)
    b = how_long(blizzards, end, start, x, y)
    c = how_long(blizzards, start, end, x, y)

    print("Part 2:", a + b + c)


if __name__ == "__main__":
    part1()
    part2()
