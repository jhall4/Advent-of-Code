import sys
import pathlib

from utils import data_importer

codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def get_elf_set(elf):
    return set(range(int(elf[0]), int(elf[1])+1))


def part_one(data):
    full_overlaps = 0
    for elves in data:
        elf1 = get_elf_set(elves[0])
        elf2 = get_elf_set(elves[1])

        overlap = elf1 & elf2

        if len(overlap) >= len(elf1) or len(overlap) >= len(elf2):
            full_overlaps += 1
    return full_overlaps


def part_two(data):
    partial_overlaps = 0
    for elves in data:
        elf1 = get_elf_set(elves[0])
        elf2 = get_elf_set(elves[1])

        overlap = elf1 & elf2

        if len(overlap) > 0:
            partial_overlaps += 1
    return partial_overlaps


def main():
    """ Main program """
    # Code goes over here.
    data = data_importer.get_as_multidimensional_array(
        "aoc_2022/data/day4.txt", '\n', ',', '-')

    part_one_result = part_one(data)
    print("Day One - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day One - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
