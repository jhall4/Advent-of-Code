import sys
import pathlib

from collections import namedtuple

from utils import data_importer

codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


DIR = "dir"
FILE = "file"
FileTup = namedtuple('File', 'type name size')
DirTup = namedtuple('Dir', 'type name children')


def build_file_system(data):
    root_dir = DirTup(DIR, "/", [])
    nav_list = [root_dir]
    for line in data:
        contents = line.split(' ')
        if contents[0] == '$':
            command = contents[1]
            if command == "cd":
                destination = contents[2]
                if destination == '/':
                    nav_list = [root_dir]
                elif destination == "..":
                    nav_list = nav_list[:-1]
                else:
                    for child in nav_list[-1].children:
                        if child.type == DIR and child.name == destination:
                            nav_list.append(child)
                            break
            continue
        elif contents[0] == DIR:
            nav_list[-1].children.append(DirTup(DIR, contents[1], []))
            continue
        else:
            nav_list[-1].children.append(FileTup(FILE,
                                                 contents[1], int(contents[0])))
            continue
    return root_dir


def get_dir_sizes(node, sizes_list):
    dir_size = 0
    for child in node.children:
        if child.type == FILE:
            dir_size += child.size
        else:  # child.type == DIR:
            child_size, sizes_list = get_dir_sizes(child, sizes_list)
            dir_size += child_size
    sizes_list.append(dir_size)
    return dir_size, sizes_list


def part_one(data):
    root_node = build_file_system(data)
    dir_sizes_list = []
    _, dir_sizes_list = get_dir_sizes(root_node, dir_sizes_list)

    size_total = 0
    for dir_size in dir_sizes_list:
        if dir_size <= 100001:
            size_total += dir_size
    return size_total


def part_two(data):
    root_node = build_file_system(data)
    dir_sizes_list = []
    root_dir_size, dir_sizes_list = get_dir_sizes(root_node, dir_sizes_list)

    disk_size = 70000000
    space_needed = 30000000
    min_space_needed = space_needed - (disk_size - root_dir_size)

    dir_sizes_list.sort()
    for size in dir_sizes_list:
        if size >= min_space_needed:
            return size
    return 0


def main():
    """ Main program """
    # Code goes over here.
    data = data_importer.get_rows_as_array("aoc_2022/data/day7.txt")

    part_one_result = part_one(data)
    print("Day One - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day One - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
