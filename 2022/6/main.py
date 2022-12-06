from aockit import get_input


def get_for_length(data: str, length: int) -> int:
    index = 0
    for i in range(len(data)):
        if len(set(data[i:i+length])) == length:
            index = i + length
            break
    return index


def part1():
    data = get_input(2022, 6)
    start = get_for_length(data, 4)
    print(f"Part 1: {start}")



def part2():
    data = get_input(2022, 6)
    start = get_for_length(data, 14)
    print(f"Part 2: {start}")


if __name__ == "__main__":
    part1()
    part2()
