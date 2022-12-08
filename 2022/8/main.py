from aockit import get_input


def part1():
    data = get_input(2022, 8)
    data = [[int(i) for i in row] for row in data.split('\n') if row != ""]

    count = 0

    width = len(data[0])
    height = len(data)
    for y in range(height):
        for x in range(width):
            # left
            if x == 0:
                count += 1
                continue
            
            visible = True
            for i in range(1, x+1):
                if data[y][x-i] >= data[y][x]:
                    visible = False
                    break
            if visible:
                count += 1
                continue

            # right
            if x == len(data[y]) - 1:
                count += 1
                continue

            visible = True
            for i in range(1, width - x):
                if data[y][x+i] >= data[y][x]:
                    visible = False
                    break
            if visible:
                count += 1
                continue

            # up
            if y == 0:
                count += 1
                continue

            visible = True
            for i in range(1, y+1):
                if data[y-i][x] >= data[y][x]:
                    visible = False
                    break
            if visible:
                count += 1
                continue

            # down
            if y == len(data) - 1:
                count += 1
                continue

            visible = True
            for i in range(1, height - y):
                if data[y+i][x] >= data[y][x]:
                    visible = False
                    break
            if visible:
                count += 1
                continue
    print(count)

def part2():
    data = get_input(2022, 8)
    data = [[int(i) for i in row] for row in data.split('\n') if row != ""]

    highest_score = 0

    width = len(data[0])
    height = len(data)
    for y in range(height):
        for x in range(width):
            if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                continue
            
            # left
            left = 0
            for i in range(1, x+1):
                left += 1
                if data[y][x-i] >= data[y][x]:
                    break

            # right
            right = 0
            for i in range(1, width - x):
                right += 1
                if data[y][x+i] >= data[y][x]:
                    break

            # up
            up = 0
            for i in range(1, y+1):
                up += 1
                if data[y-i][x] >= data[y][x]:
                    break

            # down
            down = 0
            for i in range(1, height - y):
                down += 1
                if data[y+i][x] >= data[y][x]:
                    break

            current = right * left * up * down
            if current > highest_score:
                highest_score = current
    print(highest_score)


if __name__ == "__main__":
    part1()
    part2()
