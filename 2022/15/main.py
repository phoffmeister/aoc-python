from typing import List
from aockit import get_input

import re


def read_sensors(rows: List[str]):
    sensors = dict()
    beacons = set()
    pat = re.compile(r"^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$")
    min_x, max_x = 99999999999999999, 0
    for row in rows:
        match = pat.match(row)
        if match:
            sx = int(match.groups()[0])
            sy = int(match.groups()[1])
            bx = int(match.groups()[2])
            by = int(match.groups()[3])
            d = abs(sx - bx) + abs(sy - by)
            sensors[(sx, sy)] = (bx, by, d)
            beacons.add((bx, by))
            mi = sx - d
            ma = sx + d
            min_x = min(mi, min_x)
            max_x = max(ma, max_x)
    return sensors, beacons, min_x, max_x


def check_for_row(sensors, beacons, min_x, max_x, y):
    count = 0
    for x in range(min_x - 1, max_x + 2):
        if (x, y) in beacons:
            continue
        for sensor in sensors:
            beacon = sensors[sensor]
            d = abs(sensor[0] - x) + abs(sensor[1] - y)
            if d <= beacon[2]:
                count += 1
                break
    return count


def part1():
    data = get_input(2022, 15)
    data = data.split('\n')
    sensors = read_sensors(data)
    amount = check_for_row(*sensors, 2000000)
    print("Part 1:", amount)


def part2():
    data = get_input(2022, 15)
    data = data.split('\n')
    sensors = read_sensors(data)


if __name__ == "__main__":
    part1()
    part2()
