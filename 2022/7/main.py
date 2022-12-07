from typing import List
from aockit import get_input


class Node:
    def __init__(self, name) -> None:
        self.name = name

    def size(self) -> int:
        raise Exception("Please implement me")

class Folder(Node):
    def __init__(self, name: str, parent) -> None:
        super().__init__(name)
        self.nodes: List[Node] = list()
        self.parent = parent
        self.size_stash = -1


    def size(self) -> int:
        if self.size_stash != -1:
            return self.size_stash
        total = 0
        for n in self.nodes:
            total += n.size()
        self.size_stash = total
        return self.size_stash

    def get_dir(self, name:str):
        for n in self.nodes:
            if n.name == name:
                return n
        return None


class File(Node):
    def __init__(self, name: str, file_size: int, folder: Folder) -> None:
        super().__init__(name)
        self.file_size = file_size
        self.folder = folder

    def size(self) -> int:
        return self.file_size

def get_total_thresh(t: int, current: Folder) -> int:
    total = 0
    if current.size() <= t:
        total += current.size()

    for n in current.nodes:
        if isinstance(n, Folder):
            total += get_total_thresh(t, n)

    return total

def read_data(data) -> Folder:
    root = Folder('/', None)
    current = root

    in_ls = False
    for row in data[1:]:
        if in_ls:
            if row[0] == "$":
                in_ls = False
            else:
                if row[:3] == "dir":
                    current.nodes.append(Folder(row[4:], current))
                else:
                    s, n = row.split(' ')
                    current.nodes.append(File(n, int(s), current))
            
        if row[0] == "$":
            cmd = row[2:4]
            if cmd == "cd":
                target = row[5:]
                if target == "..":
                    current = current.parent
                else:
                    new_folder = current.get_dir(target)
                    if not new_folder:
                        print(f'Error at {row}')
                        break
                    current = new_folder
                    pass
            elif cmd == "ls":
                in_ls = True
    return root


def part1():
    data = [row for row in get_input(2022, 7).split('\n') if row != ""]
    root = read_data(data)

    thresh = 100000
    total = get_total_thresh(thresh, root)
    print(f"Part 1: {total}")


def find_smallest_bigger_than(f: Folder, to_free: int, current_smallest) -> int:
    smal = current_smallest
    if f.size() > to_free and f.size() < current_smallest:
        smal = f.size()

    for n in f.nodes:
        if isinstance(n, Folder):
            if n.size() < smal:
                smal = find_smallest_bigger_than(n, to_free, smal)
    return smal


def part2():
    data = [row for row in get_input(2022, 7).split('\n') if row != ""]
    root = read_data(data)
    available = 70000000
    needed = 30000000
    used = root.size()

    to_free = needed - (available - used)
    smallest_fitting = find_smallest_bigger_than(root, to_free, 9999999999)
    print(f"Part 2: {smallest_fitting}")


if __name__ == "__main__":
    part1()
    part2()
