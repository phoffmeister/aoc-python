from typing import Dict, List, Tuple
from aockit import get_input

Point = Tuple[int, int]
HeightMap = Dict[Point, int]

def parse_map(rows: List[str]) -> Tuple[HeightMap, Point, Point]:
    the_map = dict()
    y = 0
    start = (-1 , -1)
    end = (-1 , -1)
    for row in rows:
        x = 0
        for c in row:
            if c == "S":
                start = (x, y)
                the_map[start] = 0
            elif c == "E":
                end = (x, y)
                the_map[end] = ord('z') - ord('a')
            else:
                the_map[(x, y)] = ord(c) - ord('a')
            x += 1
        y += 1

    return the_map, start, end

dirs = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

the_max = 999999999999999999

def get_path_len(came_from, current):
    total = 0
    while current in came_from:
        current = came_from[current]
        total += 1
    return total

def find(the_map: HeightMap, start, goal):
    open_set = {start}
    came_from = dict()

    def h(a):
        return abs(a[0] - goal[0]) - 1

    g_score = dict()
    g_score[start] = 0

    f_score = dict()
    f_score[start] = h(start)

    while open_set:
        lowest_f_score = the_max
        current = (-1, -1)
        for el in open_set:
            score = f_score.get(el, the_max)
            if score < lowest_f_score:
                lowest_f_score = score
                current = el

        if current[0] == goal[0] and current[1] == goal[1]:
            return get_path_len(came_from, current)

        open_set.remove(current)
        for d in dirs:
            neighbor = current[0] + d[0], current[1] + d[1]
            if neighbor not in the_map:
                continue
            if the_map[neighbor] > the_map[current] + 1:
                continue

            tentative_g_score = g_score.get(current, the_max) + 1
            if tentative_g_score < g_score.get(neighbor, the_max):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor)
                if neighbor not in open_set:
                    open_set.add(neighbor)


def part1():
    data = get_input(2022, 12)
    data = [row for row in data.split('\n') if row != ""]
    the_map, start, end = parse_map(data)
    print("Part 1:", find(the_map, start, end))


def part2():
    data = get_input(2022, 12)
    data = [row for row in data.split('\n') if row != ""]
    the_map, _, end = parse_map(data)
    shortest = the_max
    for pos in the_map:
        h = the_map[pos]
        if h == 0:
            maybe_better = find(the_map, pos, end)
            if maybe_better and maybe_better < shortest:
                shortest = maybe_better
    print("Part 2:", shortest)


if __name__ == "__main__":
    part1()
    part2()
