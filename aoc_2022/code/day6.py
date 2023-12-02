import sys
import pathlib

from utils import data_importer

codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def find_marker_position(data, marker_len):
    for i in range(len(data)):
        end = min(i+marker_len, len(data))
        buffer = set(data[i:end])
        if len(buffer) == marker_len:
            return end
    return 0


def part_one(data):
    return find_marker_position(data, 4)


def part_two(data):
    return find_marker_position(data, 14)


def main():
    """ Main program """
    # Code goes over here.
    data = data_importer.get_file_as_string("aoc_2022/data/day6.txt")

    part_one_result = part_one(data)
    print("Day One - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day One - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
