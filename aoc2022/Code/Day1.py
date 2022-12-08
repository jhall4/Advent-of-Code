import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter


def PartOne(data):
    calories = []
    for elf in data:
        calories.append(sum(elf))

    return max(calories)


def PartTwo(data):
    calories = []
    for elf in data:
        calories.append(sum(elf))

    calories.sort(reverse=True)
    topThreeCalTotal = 0
    for i in range(3):
        topThreeCalTotal += calories[i]

    return topThreeCalTotal


def main():
    """ Main program """
    # Code goes over here.
    data = DataImporter.GetNewLineDelimitedFileAs2dIntArray("aoc2022/Data/day1.txt")

    partOneResult = PartOne(data)
    print("Day One - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day One - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
