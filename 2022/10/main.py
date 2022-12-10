from aockit import get_input
from typing import List


class Instruction():
    def __init__(self, cycles: int, addx: int) -> None:
        self.cycles = cycles
        self.addx = addx

def read_instructions(data) -> List[Instruction]:
    instructions = list()
    for row in data:
        if row.startswith("noop"):
            instructions.append(Instruction(1, 0))
        else:
            instructions.append(Instruction(2, int(row.split(" ")[1])))
    return instructions

important_cycles = [20, 60, 100, 140, 180, 220]

def part1():
    data = get_input(2022, 10)
    data = [d for d in data.split("\n") if d != ""]
    instructions = read_instructions(data)

    cycle = 0
    x = 1
    total = 0
    for ins in instructions:
        for _ in range(ins.cycles):
            cycle += 1
            if cycle in important_cycles:
                total += x * cycle
        x += ins.addx
    print(f"Part 1: {total}")


def part2():
    data = get_input(2022, 10)
    data = [d for d in data.split("\n") if d != ""]
    instructions = read_instructions(data)

    cycle = 0
    x = 1
    screen = ""
    for ins in instructions:
        for _ in range(ins.cycles):
            cycle += 1
            if abs(cycle-1 - x) <= 1:
                screen += "#"
            else:
                screen += " "
            if cycle == 40:
                cycle = 0
                screen += "\n"
        x += ins.addx
    print(f"Part 2:\n{screen}")


if __name__ == "__main__":
    part1()
    part2()
