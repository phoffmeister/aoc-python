from aockit import get_input


def parsed(data: str):
    a, b = data.split(',')
    a1, a2 = a.split('-')
    b1, b2 = b.split('-')
    return ((int(a1), int(a2)), (int(b1), int(b2)))


def part1():
    data = [parsed(r) for r in get_input(2022, 4).split('\n') if r != ""]
    count = 0
    for ((a1, a2), (b1, b2)) in data:
        if a1 <= b1 and a2 >= b2:
            count += 1
        elif a1 >= b1 and a2 <= b2:
            count += 1

    print(f"Part 1: {count}")


def part2():
    data = [parsed(r) for r in get_input(2022, 4).split('\n') if r != ""]
    count = 0
    for ((a1, a2), (b1, b2)) in data:
        if a1 >= b1 and a1 <= b2:
            count += 1
        elif a2 >= b1 and a2 <= b2:
            count += 1
        elif b1 >= a1 and b1 <= a2:
            count += 1
        elif b2 >= a1 and b2 <= a2:
            count += 1

    print(f"Part 2: {count}")


if __name__ == "__main__":
    part1()
    part2()
