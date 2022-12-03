from aockit import get_input


def part1():
    data = get_input(2022, 3)
    count = 0
    for row in data.split('\n'):
        if row == "":
            continue
        l = len(row)
        a, b = row[:int(l/2)], row[int(l/2):]

        for c1 in a:
            if c1 in b:
                if c1.islower():
                    c = ord(c1) + 1 - ord('a')
                else:
                    c = 26 + ord(c1) + 1 - ord('A')
                count += c
                break
    print(f"Part 1: {count}")


def part2():
    data = get_input(2022, 3)
    count = 0
    groups = [row for row in data.split('\n') if row != ""]

    for i in range(0, len(groups)-2, 3):
        for c1 in groups[i]:
            if c1 in groups[i+1] and c1 in groups[i+2]:
                if c1.islower():
                    c = ord(c1) + 1 - ord('a')
                else:
                    c = 26 + ord(c1) + 1 - ord('A')
                count += c
                break

    print(f"Part 2: {count}")


if __name__ == "__main__":
    part1()
    part2()
