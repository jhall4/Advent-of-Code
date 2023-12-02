import sys
import pathlib

from utils import data_importer

codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def part_one(data):
    calories = []
    for elf in data:
        calories.append(sum(elf))

    return max(calories)


def part_two(data):
    calories = []
    for elf in data:
        calories.append(sum(elf))

    calories.sort(reverse=True)
    top_three_cal_total = 0
    for i in range(3):
        top_three_cal_total += calories[i]

    return top_three_cal_total


def main():
    """ Main program """
    # Code goes over here.
    data = data_importer.get_new_line_delimited_file_as_2d_int_array(
        "aoc_2022/data/day1.txt")

    part_one_result = part_one(data)
    print("Day One - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day One - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
