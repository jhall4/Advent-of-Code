import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter


def GetElfSet(elf):
    return set(range(int(elf[0]), int(elf[1])+1))


def PartOne(data):
    fullOverlaps = 0
    for elves in data:
        elf1 = GetElfSet(elves[0])
        elf2 = GetElfSet(elves[1])

        overlap = elf1 & elf2

        if len(overlap) >= len(elf1) or len(overlap) >= len(elf2):
            fullOverlaps += 1
    return fullOverlaps


def PartTwo(data):
    partialOverlaps = 0
    for elves in data:
        elf1 = GetElfSet(elves[0])
        elf2 = GetElfSet(elves[1])

        overlap = elf1 & elf2

        if len(overlap) > 0:
            partialOverlaps += 1
    return partialOverlaps


def main():
    """ Main program """
    # Code goes over here.
    data = DataImporter.GetAsMultiDimensionalArray("aoc2022/Data/day4.txt", '\n', ',', '-')


    partOneResult = PartOne(data)
    print("Day One - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day One - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
