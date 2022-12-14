from typing import Dict, List, Tuple
from aockit import get_input


Position = Tuple[int, int]
Cave = Dict[Position, str]


def add_path(cave: Cave, x1:int, y1:int, x2:int, y2:int):
    d_x = x2 - x1
    d_y = y2 - y1

    if d_x > 0:
        for i in range(d_x + 1):
            cave[x1+i, y1] = "#"
    elif d_x < 0:
        for i in range(abs(d_x) + 1):
            cave[x2+i, y1] = "#"
    if d_y > 0:
        for i in range(d_y + 1):
            cave[x1, y1+i] = "#"
    elif d_y < 0:
        for i in range(abs(d_y) + 1):
            cave[x1, y2+i] = "#"


def reconstruct_cave(cave_data: List[str]) -> Tuple[Cave, int, int, int, int]:
    cave = dict()
    min_x, max_x, min_y, max_y = 9999, 0, 9999, 0
    for path in cave_data:
        if path == "":
            continue
        positions = path.split(' -> ')
        for i in range(len(positions) - 1):
            x1, y1 = positions[i].split(',')
            x2, y2 = positions[i+1].split(',')
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            add_path(cave, x1, y1, x2, y2)

            min_x = min(min_x, x1, x2)
            max_x = max(max_x, x1, x2)
            min_y = min(min_y, y1, y2)
            max_y = max(max_y, y1, y2)


    return cave, min_x, min_y, max_x, max_y


def add_sand(cave: Cave, max_depth: int) -> bool:
    x = 500
    y = 0

    while y != (max_depth + 10):
        if (x, y+1) not in cave:
            y += 1
            continue
        elif (x-1, y+1) not in cave:
            x -= 1
            y += 1
        elif (x+1, y+1) not in cave:
            x += 1
            y += 1
        else:
            cave[x, y] = "o"
            return True
    return False


def add_sand_with_floor(cave: Cave, max_depth: int) -> bool:
    x = 500
    y = 0

    while True:
        if (x, y+1) not in cave and y+1 != max_depth:
            y += 1
            continue
        elif (x-1, y+1) not in cave and y+1 != max_depth:
            x -= 1
            y += 1
            continue
        elif (x+1, y+1) not in cave and y+1 != max_depth:
            x += 1
            y += 1
            continue
        else:
            cave[x, y] = "o"
            if x == 500 and y == 0:
                return False
            return True


def part1():
    cave_data = get_input(2022, 14)
    cave, _, _, _, y2 = reconstruct_cave(cave_data.split('\n'))

    count = 0
    while add_sand(cave, y2):
        count += 1
    print("Part 1:", count)


def part2():
    cave_data = get_input(2022, 14)
    cave, _, _, _, y2 = reconstruct_cave(cave_data.split('\n'))

    count = 0
    while add_sand_with_floor(cave, y2+2):
        count += 1
    count += 1

    print("Part 2:", count)


if __name__ == "__main__":
    part1()
    part2()
