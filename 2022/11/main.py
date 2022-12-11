from typing import Callable, List
from aockit import get_input


class Monkey:
    def __init__(self) -> None:
        self.items: List[int] = list()
        self.op: Callable[[int], int]
        self.divisible = 0
        self.yes = 0
        self.no = 0
        self.inspected = 0

    def set_op(self, conv: str):
        def generate_op(conv: str) -> Callable[[int], int]:
            operator, rhs_s = conv.split(' ')
            def op(old: int) -> int:
                rhs = old if rhs_s == "old" else int(rhs_s)
                if operator == "+":
                    return old + rhs
                elif operator == "*":
                    return old * rhs
                raise Exception("Not reached")
            return op
        self.op = generate_op(conv)

def parse_monkeys(rows: List[str]) -> List[Monkey]:
    monkeys = list()

    m = Monkey()
    for row in rows:
        if row == "":
            monkeys.append(m)
            m = Monkey()
        if row.startswith("  Starting items: "):
            for i in row[len("  Starging items: "):].split(", "):
                m.items.append(int(i))
        elif row.startswith("  Operation: "):
            m.set_op(row[len("  Operation: new = old "):])
        elif row.startswith("  Test:"):
            m.divisible = int(row[len("  Test: divisible by "):])
        elif row.startswith("    If t"):
            m.yes = int(row[-1])
        elif row.startswith("    If f"):
            m.no = int(row[-1])

    return monkeys


def part1():
    data = [row for row in get_input(2022, 11).split('\n')]
    monkeys = parse_monkeys(data)
    for _ in range(20):
        for m in monkeys:
            m.items.reverse()
            while m.items:
                m.inspected += 1
                item = m.items.pop()
                item = m.op(item) // 3
                if item % m.divisible == 0:
                    monkeys[m.yes].items.append(item)
                else:
                    monkeys[m.no].items.append(item)

    inspected = [m.inspected for m in monkeys]
    inspected.sort(reverse=True)
    print("Part 1:", inspected[0]*inspected[1])


def part2():
    data = [row for row in get_input(2022, 11).split('\n')]
    monkeys = parse_monkeys(data)
    divv = 1
    for m in monkeys:
        divv *= m.divisible

    for _ in range(10000):
        for m in monkeys:
            m.items.reverse()
            while m.items:
                m.inspected += 1
                item = m.items.pop()
                item = m.op(item)
                item = item % divv
                if item % m.divisible == 0:
                    monkeys[m.yes].items.append(item)
                else:
                    monkeys[m.no].items.append(item)

    inspected = [m.inspected for m in monkeys]
    inspected.sort(reverse=True)
    print("Part 2:", inspected[0]*inspected[1])


if __name__ == "__main__":
    part1()
    part2()
