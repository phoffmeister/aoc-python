from typing import List, Tuple
from aockit import get_input


Point = Tuple[int, int, int]

def parse_points(rows: List[str]) -> List[Point]:
    ps: List[Point] = list()
    for r in rows:
        x, y, z = r.split(',')
        ps.append((int(x), int(y), int(z)))
    return ps

ns = [
        (0,0,1),
        (0,0,-1),
        (0,1,0),
        (0,-1,0),
        (1,0,0),
        (-1,0,0),
      ]

def add_p(a: Point, b: Point):
    return a[0] + b[0], a[1] + b[1], a[2] + b[2]

def check_free_sides(points: List[Point]):
    free_sides = 0
    checked = set()
    for point in points:
        possible = 6
        for n_off in ns:
            n = (point[0] + n_off[0], point[1] + n_off[1], point[2] + n_off[2])
            if n in checked:
                possible -= 2
        free_sides += possible
        checked.add(point)
    return free_sides


def part1():
    data = get_input(2022, 18)
    rows = [r for r in data.split('\n') if r != ""]
    points = parse_points(rows)
    sides = check_free_sides(points)
    print("Part 1:", sides)



def part2():
    data = get_input(2022, 18)
    rows = [r for r in data.split('\n') if r != ""]
    points = {p for p in parse_points(rows)}
    outer = min(points, key=lambda a: a[0])
    outer = outer[0] - 1, outer[1], outer[2]

    edge = set()
    to_do = {outer}
    
    while to_do:
        current = to_do.pop()
        edge.add(current)
        
        for n1_off in ns:
            n1 = add_p(current, n1_off)
            if n1 in edge:
                continue
            if n1 in points:
                continue

            is_on_surface = False
            for n2_off in ns:
                n2 = add_p(n1, n2_off)
                if n2 == current:
                    continue
                if n2 in points:
                    is_on_surface = True
                    break
            if is_on_surface:
                to_do.add(n1)

        for n1_off in ns:
            n1 = add_p(current, n1_off)
            if n1 in points:
                continue

            is_on_surface = False
            for n2_off in ns:
                n2 = add_p(n1, n2_off)
                if n2 == current:
                    continue
                if n2 in edge:
                    continue
                if n2 in points:
                    continue
                for n3_off in ns:
                    n3 = add_p(n2, n3_off)
                    if n3 in points:
                        is_on_surface = True
                        break
                if is_on_surface:
                    to_do.add(n2)
                    break

    total = 0
    for e in edge:
        for n1_off in ns:
            n1 = add_p(e, n1_off)
            if n1 in points:
                total += 1
    print("Part 2:", total)


if __name__ == "__main__":
    part1()
    part2()
