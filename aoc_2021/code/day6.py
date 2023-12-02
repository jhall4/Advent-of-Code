import numpy
from utils import data_importer
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def CalculateFishReproduction(fishes, numDays):
    fishInGroups = numpy.zeros(9, dtype=int)

    for fish in fishes:
        fishInGroups[fish] += 1

    for i in range(numDays):
        newFish = fishInGroups[0]
        for j in range(len(fishInGroups)-1):
            fishInGroups[j] = fishInGroups[j + 1]

        fishInGroups[6] += newFish
        fishInGroups[8] = newFish

    return numpy.sum(fishInGroups)


def part_one(data):
    numDays = 80
    return CalculateFishReproduction(data, numDays)


def part_two(data):
    numDays = 256
    return CalculateFishReproduction(data, numDays)


def main():
    """ Main program """
    # Code goes over here.
    data = data_importer.get_as_array("aoc_2021/data/daysix.csv")

    part_one_result = part_one(data)
    print("Day Six - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day Six - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
