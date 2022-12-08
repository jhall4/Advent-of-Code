import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter

import numpy

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

def PartOne(data):
    numDays = 80
    return CalculateFishReproduction(data, numDays)


def PartTwo(data):
    numDays = 256
    return CalculateFishReproduction(data, numDays)


def main():
    """ Main program """
    # Code goes over here.
    data = DataImporter.GetCsvAsArray("aoc2021/Data/daysix.csv")

    partOneResult = PartOne(data)
    print("Day Six - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day Six - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
