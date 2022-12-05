from typing import Dict, List
from aockit import get_input
from dataclasses import dataclass


@dataclass
class Step:
    amount: int
    start: int
    dest: int


class Day5:
    def __init__(self):
        self.stack: Dict[int, List[str]] = dict()
        self.steps: List[Step] = list()

        for i in range(1, 10):
            self.stack[i] = list()


def parse_input(data: str) -> Day5:
    data_in = [d for d in data.split('\n')]

    ret = Day5()

    data_initial = data_in[:8]
    for row in data_initial:
        for i in range(1, 10):
            char = row[1+4*(i-1)]
            if char != " ":
                ret.stack[i].append(char)

    for i in range(1, 10):
        ret.stack[i].reverse()

    for row in data_in[10:-1]:
        _, amount, _, start, _, dest = row.split(" ")
        ret.steps.append(Step(int(amount), int(start), int(dest)))

    return ret


def part1():
    data = get_input(2022, 5)
    d = parse_input(data)
    for step in d.steps:
        for _ in range(step.amount):
            d.stack[step.dest].append(d.stack[step.start].pop())
    last = ""
    for i in range(1, 10):
        last += d.stack[i][-1]
    print(f"Part 1: {last}")


def part2():
    data = get_input(2022, 5)
    d = parse_input(data)
    for step in d.steps:
        rep = ""
        for _ in range(step.amount):
            rep = d.stack[step.start].pop() + rep

        for c in rep:
            d.stack[step.dest].append(c)
    last = ""
    for i in range(1, 10):
        last += d.stack[i][-1]
    print(f"Part 2: {last}")


if __name__ == "__main__":
    part1()
    part2()
