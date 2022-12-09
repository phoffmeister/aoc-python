from typing import List, Tuple
from aockit import get_input


dirs = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

def again(head, tail):
    same_row_or_col = head[0] == tail[0] or head[1] == tail[1]
    distance = abs(head[0] - tail[0]) + abs(head[1] - tail[1])
    a = same_row_or_col and (distance > 1)
    b = (not same_row_or_col) and (distance > 2)
    return a or b

def part1():
    inp = get_input(2022, 9)
    data = [(row.split(' ')[0], int(row.split(' ')[1])) 
            for row in inp.split('\n') if row != ""]

    start = (0, 0)
    positions = set()

    head = start
    tail = start

    positions.add(start)
    for d, amount in data:
        dd = dirs[d]
        for _ in range(amount):
            head = (head[0] + dd[0], head[1] + dd[1])

            while again(head, tail):
                x_diff =  head[0] - tail[0]
                x = 1 if x_diff > 0 else -1 if x_diff < 0 else 0
                y_diff =  head[1] - tail[1]
                y = 1 if y_diff > 0 else -1 if y_diff < 0 else 0
                tail = (tail[0]+x, tail[1]+y)

                positions.add(tail)

    print(len(positions))


def part2():
    inp = get_input(2022, 9)
    data = [(row.split(' ')[0], int(row.split(' ')[1])) 
            for row in inp.split('\n') if row != ""]

    start = (0, 0)
    positions = set()

    rope: List[Tuple[int, int]] = [start for _ in range(10)]

    positions.add(start)
    for d, amount in data:
        dd = dirs[d]
        for _ in range(amount):
            rope[0] = (rope[0][0] + dd[0], rope[0][1] + dd[1])

            for i in range(len(rope)-1):
                head = rope[i]
                tail = rope[i+1]

                while again(head, tail):
                    x_diff =  head[0] - tail[0]
                    x = 1 if x_diff > 0 else -1 if x_diff < 0 else 0
                    y_diff =  head[1] - tail[1]
                    y = 1 if y_diff > 0 else -1 if y_diff < 0 else 0
                    rope[i+1] = (tail[0]+x, tail[1]+y)
                    tail = (tail[0]+x, tail[1]+y)

                    if i == 8:
                        positions.add(tail)

    print(len(positions))


if __name__ == "__main__":
    part1()
    part2()
