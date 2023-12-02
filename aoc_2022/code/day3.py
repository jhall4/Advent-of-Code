import sys
import pathlib

from utils import data_importer

codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def get_priority(item_char):
    priority = 0
    for item in items:
        priority += 1
        if item_char == item:
            break
    return priority


def part_one(data):
    priority_total = 0
    for ruck_sack in data:
        sack_len = len(ruck_sack)
        sack_mid = int(sack_len/2)
        first_half = set(ruck_sack[0:sack_mid])
        second_half = set(ruck_sack[sack_mid:sack_len])
        shared_item = list(first_half & second_half)
        priority_total += get_priority(shared_item[0])
    return priority_total


def part_two(data):
    priority_total = 0
    for i in range(0, len(data), 3):
        elf1 = set(data[i])
        elf2 = set(data[i+1])
        elf3 = set(data[i+2])
        shared_item = list(elf1 & elf2 & elf3)
        priority_total += get_priority(shared_item[0])
    return priority_total


def main():
    """ Main program """
    # Code goes over here.
    data = data_importer.get_rows_as_array("aoc_2022/data/day3.txt")

    part_one_result = part_one(data)
    print("Day One - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day One - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
