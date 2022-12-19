from typing import List, Tuple
from aockit import get_input

import re


def read_sensors(rows: List[str]):
    sensors = dict()
    pat = re.compile(r"^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$")
    for row in rows:
        match = pat.match(row)
        if match:
            sx = int(match.groups()[0])
            sy = int(match.groups()[1])
            bx = int(match.groups()[2])
            by = int(match.groups()[3])
            d = abs(sx - bx) + abs(sy - by)
            sensors[(sx, sy)] = d
    return sensors


def reduce(l:List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    change = True
    while change:
        change = False
        n_l = list()
        for x in range(len(l)):
            for y in range(len(l)):
                if x == y:
                    continue
                x1, x2 = l[x]
                x3, x4 = l[y]

                nx1 = 0
                nx2 = 0
                if x1 <= x3 and x3 <= x2:
                    change = True
                    nx1 = x1
                    nx2 = max(x2, x4)

                elif x1 <= x4 and x4 <= x2:
                    change = True
                    nx1 = min(x1, x3)
                    nx2 = x2

                elif x3 <= x1 and x1 <= x4:
                    change = True
                    nx1 = x3
                    nx2 = max(x2, x4)

                elif x3 <= x2 and x2 <= x4:
                    change = True
                    nx1 = min(x1, x3)
                    nx2 = x4


                if change:
                    for i in range(len(l)):
                        if i == x:
                            n_l.append((nx1, nx2))
                        elif i == y:
                            pass
                        else:
                            n_l.append(l[i])
                    l = n_l
                    break
            if change:
                break
    return l


def part1():
    data = get_input(2022, 15)
    data = data.split('\n')
    sensors = read_sensors(data)
    line = 2000000
    l = list()
    for sx, sy in sensors.keys():
        d = sensors[(sx, sy)]
        diff = abs(line - sy)
        if diff > d:
            continue
        x = d - diff
        l.append((sx-x, sx+x))

    l = reduce(l)

    amount = 0
    for a,b in l:
        amount += b-a

    print("Part 1:", amount)


def part2():
    data = get_input(2022, 15)
    data = data.split('\n')
    sensors = read_sensors(data)
    for line in range(4000000):
        l = list()
        for sx, sy in sensors.keys():
            d = sensors[(sx, sy)]
            diff = abs(line - sy)
            if diff > d:
                continue
            x = d - diff
            a = sx - x
            b = sx + x
            if b < 0:
                continue
            if a < 0:
                a = 0
            if a > 4000000:
                continue
            if b > 4000000:
                b = 4000000
            l.append((a, b))
        l = reduce(l)
        if len(l) > 1:
            y = line
            x = l[0][1]+1
            print("Part 2:", x*4000000+y)
            break


if __name__ == "__main__":
    part1()
    part2()
