from typing import List
from aockit import get_input
import functools

def read_packets(rows):
    packets = list()
    for row in rows:
        if row == "":
            continue
        packets.append(eval(row))
    return packets


def right_order(a: List, b: List) -> int:
    i = -1
    while True:
        i += 1
        if i >= len(a) and i >= len(b):
            return 0
        if i >= len(a):
            return 1
        if i >= len(b):
            return -1
        if type(a[i]) == int and type(b[i]) == list:
            inner = right_order([a[i]], b[i])
            if inner != 0:
                return inner
            continue
        if type(a[i]) == list and type(b[i]) == int:
            inner = right_order(a[i], [b[i]])
            if inner != 0:
                return inner
            continue
        if type(a[i]) == list and type(b[i]) == list:
            inner = right_order(a[i], b[i])
            if inner != 0:
                return inner
            continue
        if a[i] == b[i]:
            continue
        if a[i] > b[i]:
            return -1
        else:
            return 1


def part1():
    data = get_input(2022, 13)
    data = data.split('\n')
    packets = read_packets(data)
    total = 0
    for i in range(0, len(packets), 2):
        packet_index = (i//2)+1
        a = packets[i]
        b = packets[i+1]
        p = right_order(a, b)
        if p == 1:
            total += packet_index
    print("Part1", total)


def part2():
    data = get_input(2022, 13)
    data = data.split('\n')
    packets = read_packets(data)
    a = [[2]]
    b = [[6]]
    packets.append(a)
    packets.append(b)
    packets.sort(key=functools.cmp_to_key(right_order), reverse=True)
    i_a = packets.index(a) + 1
    i_b = packets.index(b) + 1
    print("Part2", i_a * i_b)


if __name__ == "__main__":
    part1()
    part2()
